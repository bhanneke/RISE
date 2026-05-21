"""Regenerate the skills index pages from source YAML files.

Reads:
  skills/*.yml

Writes:
  docs/skills/<pack-slug>.md   (one per pack)
  docs/skills/index.md         (overview + cross-pack table)

No external dependencies beyond PyYAML.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / "skills"
DOCS_SKILLS_DIR = REPO_ROOT / "docs" / "skills"
DOCS_SKILLS_INDEX = DOCS_SKILLS_DIR / "index.md"


_MD_LINK_RE = re.compile(r"\[([^\]\n]+)\]\(([^)\n]+)\)")


def _strip_broken_relative_links(text: str) -> tuple[str, int]:
    """Strip relative markdown links from bundled SKILL.md text.

    Upstream SKILL.md files reference sibling files (references/, assets/,
    rules/, templates/, agents/, examples/) and other skills via relative
    paths. We don't bundle those files, so the links 404 on the live site.
    Keep absolute (http/https/mailto) and pure-anchor (#foo) links; drop the
    wrapper on everything else, preserving the visible label.

    Returns (new_text, n_stripped).
    """
    stripped = 0

    def repl(m: re.Match) -> str:
        nonlocal stripped
        label, target = m.group(1), m.group(2).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        # Image links survive on absolute URLs above; relative image refs
        # would have leading "!" outside the match, so a plain link wrapper
        # here is safe to flatten.
        stripped += 1
        return label

    return _MD_LINK_RE.sub(repl, text), stripped


def copy_skill_details(packs: list[dict]) -> int:
    """Build marketplace-style per-skill pages from skills/<pack>/details/."""
    n_total = 0
    n_links_stripped = 0
    for p in packs:
        pack = p["pack"]
        pack_slug = pack["slug"]
        pack_name = pack["name"]
        pack_source = pack.get("source_url", "")
        pack_license = pack.get("license", "")
        src_details = SKILLS_DIR / pack_slug / "details"
        if not src_details.exists():
            continue
        dst_dir = DOCS_SKILLS_DIR / pack_slug
        dst_dir.mkdir(parents=True, exist_ok=True)
        skills_by_slug = {s.get("slug"): s for s in (p.get("skills") or [])}

        for src in sorted(src_details.glob("*.md")):
            skill_slug = src.stem
            text = src.read_text(encoding="utf-8")

            # Strip leading YAML front-matter from the SKILL.md if present —
            # otherwise it renders as a horizontal rule + raw key:value lines.
            if text.startswith("---\n"):
                end = text.find("\n---\n", 4)
                if end != -1:
                    text = text[end + 5:].lstrip("\n")

            # Strip relative markdown links pointing at sibling files we don't
            # bundle (references/, assets/, rules/, templates/, …). See
            # _strip_broken_relative_links for rationale.
            text, n_stripped = _strip_broken_relative_links(text)
            n_links_stripped += n_stripped

            # Demote SKILL.md's H1 to H2 — the page already has its own H1.
            text_lines = text.splitlines()
            for i, ln in enumerate(text_lines):
                if ln.startswith("# "):
                    text_lines[i] = "#" + ln  # # → ##
                elif ln.startswith("## "):
                    text_lines[i] = "#" + ln  # ## → ###
                elif ln.startswith("### "):
                    text_lines[i] = "#" + ln  # etc., so we don't collide with H1
            text = "\n".join(text_lines)

            meta = skills_by_slug.get(skill_slug, {})
            name = meta.get("name", skill_slug)
            category = meta.get("category", "—")
            field = meta.get("field", "—")
            stages = meta.get("pipeline_stages") or []
            source_url = meta.get("details_url", pack_source)
            updated = meta.get("last_update", pack.get("last_update", "—"))
            description = meta.get("description", "")
            github_repo_match = re.search(r"github\.com/([^/]+/[^/]+)", source_url or "")
            github_repo = github_repo_match.group(1).split("/blob/")[0].rstrip("/") if github_repo_match else None
            github_repo = github_repo.split("/tree/")[0] if github_repo else None

            page_url = f"https://bhanneke.github.io/RISE/skills/{pack_slug}/{skill_slug}/"

            # Install / fetch block (text varies by pack)
            if pack_slug == "hundredx-os":
                install_html = (
                    '<p style="font-size:0.9em; color:#555;">'
                    'Curator-private skill — copy text from '
                    f'<code>100xOS/shared/skills/{meta.get("source_path","")}</code>.'
                    '</p>'
                )
            elif github_repo:
                src_path = meta.get("source_path", "")
                install_html = (
                    f'<button onclick="navigator.clipboard.writeText('
                    f'`gh api repos/{github_repo}/contents/{src_path} --jq .content | base64 -d`);'
                    f' this.textContent=&apos;&#x2713; copied&apos;;" '
                    f'style="background:#00897b; color:white; border:none; '
                    f'padding:0.4em 0.8em; border-radius:4px; cursor:pointer; '
                    f'font-size:0.9em; margin-right:0.5em;">'
                    f'&#128203; copy fetch command</button>'
                    f'<button onclick="navigator.clipboard.writeText(&apos;{page_url}&apos;);'
                    f' this.textContent=&apos;&#x2713; copied&apos;;" '
                    f'style="background:#fff; color:#333; border:1px solid #ccc; '
                    f'padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">'
                    f'&#128279; share link</button>'
                )
            else:
                install_html = '<p style="font-size:0.9em; color:#555;">No automated install — open the source link.</p>'

            stages_chip = " · ".join(f"<code>{x}</code>" for x in stages) if stages else "—"
            stars_badge = (
                f'<img src="https://img.shields.io/github/stars/{github_repo}?style=flat" '
                f'alt="GitHub stars" style="vertical-align:middle;">'
            ) if github_repo else ""

            # Top metadata card — RAW HTML at the document top level so it does NOT
            # interfere with the markdown rendering of the SKILL.md body below.
            card = (
                '<div class="skill-card" style="background:#fafafa; '
                'border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; '
                'margin:1em 0 1.5em; font-size:0.95em;">'
                f'<div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;">'
                f'<div><b>Pack:</b> <a href="../{pack_slug}/">{pack_name}</a></div>'
                f'<div><b>Category:</b> <code>{category}</code></div>'
                f'<div><b>Field:</b> {field}</div>'
                f'<div><b>License:</b> <code>{pack_license}</code></div>'
                f'<div><b>Updated:</b> {updated}</div>'
                f'</div>'
                f'<div style="margin-top:0.5em;"><b>Stages:</b> {stages_chip}</div>'
                f'<div style="margin-top:0.8em;">{install_html}</div>'
                f'<div style="margin-top:0.6em; font-size:0.9em;">'
                f'<a href="{source_url}" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a>'
                f'{(" &middot; " + stars_badge) if stars_badge else ""}'
                f'</div>'
                '</div>'
            )

            page = (
                f"<!-- DO NOT EDIT — auto-copied from skills/{pack_slug}/details/{skill_slug}.md -->\n\n"
                f"# `{name}`\n\n"
                f"{description}\n\n"
                f"{card}\n\n"
                f"{text}\n"
            )
            (dst_dir / f"{skill_slug}.md").write_text(page, encoding="utf-8")
            n_total += 1
    if n_links_stripped:
        print(f"Relative links stripped: {n_links_stripped}")
    return n_total

GITHUB_BASE = "https://github.com/bhanneke/RISE/blob/main"

INDEX_AUTO_START = "<!-- AUTO-GENERATED:skills-start -->"
INDEX_AUTO_END = "<!-- AUTO-GENERATED:skills-end -->"


def load_packs() -> list[dict[str, Any]]:
    packs = []
    for f in sorted(SKILLS_DIR.glob("*.yml")):
        if f.name.startswith("_"):
            continue
        with f.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        if not data or "pack" not in data:
            continue
        data["_path"] = f.relative_to(REPO_ROOT).as_posix()
        packs.append(data)
    return packs


PAGE_HEADER = "<!-- DO NOT EDIT — auto-generated from {path} by scripts/build_skills_index.py -->"


def render_pack_page(pack_data: dict[str, Any]) -> str:
    pack = pack_data["pack"]
    skills = pack_data.get("skills", []) or []
    name = pack["name"]
    slug = pack["slug"]
    src_path = pack_data["_path"]

    out: list[str] = []
    out.append(PAGE_HEADER.format(path=src_path))
    out.append("")
    out.append(f"# {name}")
    out.append("")

    meta_bits = []
    if pack.get("license"):
        meta_bits.append(f"license: `{pack['license']}`")
    if pack.get("total_skills"):
        meta_bits.append(f"{pack['total_skills']} skills")
    if pack.get("last_update"):
        meta_bits.append(f"last update: {pack['last_update']}")
    if meta_bits:
        out.append(" · ".join(meta_bits))
        out.append("")

    if pack.get("source_url"):
        out.append(f"**Source:** <{pack['source_url']}>")
        out.append("")

    if pack.get("maintainers"):
        out.append(f"**Maintainers:** {', '.join(pack['maintainers'])}")
        out.append("")

    if pack.get("related_project"):
        out.append(f"**Related project entry:** "
                   f"[`{pack['related_project']}`](../projects/{pack['related_project']}.md)")
        out.append("")

    if pack.get("compatibility"):
        chips = " ".join(f"`{c}`" for c in pack["compatibility"])
        out.append(f"**Compatibility:** {chips}")
        out.append("")

    if pack.get("notes"):
        out.append(f"> {pack['notes']}")
        out.append("")

    out.append(f"**Source YAML:** [`{src_path}`]({GITHUB_BASE}/{src_path})")
    out.append("")

    # Skills table grouped by category
    out.append("## Skills")
    out.append("")
    by_cat: dict[str, list[dict]] = defaultdict(list)
    for s in skills:
        by_cat[s.get("category", "unspecified")].append(s)
    # Determine which detail pages exist for this pack
    pack_details_dir = SKILLS_DIR / slug / "details"
    have_details = {f.stem for f in pack_details_dir.glob("*.md")} if pack_details_dir.exists() else set()

    for cat in sorted(by_cat.keys()):
        out.append(f"### `{cat}` ({len(by_cat[cat])})")
        out.append("")
        out.append("| Skill | Field | Stages | Description | Full text | Source | Updated |")
        out.append("|---|---|---|---|---|---|---|")
        for s in sorted(by_cat[cat], key=lambda x: x.get("slug", "")):
            s_slug = s.get("slug", "")
            name = s.get("name", s_slug)
            field = s.get("field", "—") or "—"
            stages = " ".join(f"`{x}`" for x in (s.get("pipeline_stages") or []))
            desc = s.get("description", "") or "—"
            details = s.get("details_url", "")
            origin_cell = f"[origin]({details})" if details else "—"
            updated = s.get("last_update", "") or "—"
            # Source-tree-relative link: from docs/skills/<pack>.md → docs/skills/<pack>/<skill>.md
            full_cell = f"[view]({slug}/{s_slug}.md)" if s_slug in have_details else "—"
            # Make the skill name clickable: prefer the bundled detail page,
            # else fall back to the external origin URL (so packs without
            # bundled SKILL.md text — e.g., cunningham-substack — still link
            # somewhere). Otherwise render as plain code.
            if s_slug in have_details:
                name_cell = f"[`{name}`]({slug}/{s_slug}.md)"
            elif details:
                name_cell = f"[`{name}`]({details}){{ target=_blank rel=noopener }}"
            else:
                name_cell = f"`{name}`"
            out.append(
                f"| {name_cell} | {field} | {stages} | {desc} | {full_cell} | {origin_cell} | {updated} |"
            )
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def render_index(packs: list[dict[str, Any]]) -> str:
    out: list[str] = []
    total_skills = sum(len(p.get("skills") or []) for p in packs)
    out.append(f"*{len(packs)} skill packs · {total_skills} skills indexed.*")
    out.append("")

    # Cross-pack matrix
    out.append("## Pack overview")
    out.append("")
    out.append("| Pack | License | Skills | Project | Runtimes |")
    out.append("|---|---|---|---|---|")
    for p in packs:
        pk = p["pack"]
        n = len(p.get("skills") or [])
        proj = pk.get("related_project", "")
        proj_link = f"[{proj}](../projects/{proj}.md)" if proj else "—"
        compat = " ".join(f"`{c}`" for c in (pk.get("compatibility") or [])[:4])
        out.append(
            f"| [{pk['name']}]({pk['slug']}.md) | `{pk.get('license','?')}` "
            f"| {n} | {proj_link} | {compat} |"
        )
    out.append("")

    # Filterable all-skills table with per-column header filters
    out.append('<h2 id="all-skills">All skills</h2>')
    out.append("")

    # Collect facet values
    all_packs = sorted({p["pack"]["slug"] for p in packs})
    all_cats = sorted({s.get("category", "—") for p in packs for s in (p.get("skills") or [])})
    all_fields = sorted({s.get("field", "—") for p in packs for s in (p.get("skills") or [])})
    all_stages = sorted({st for p in packs for s in (p.get("skills") or []) for st in (s.get("pipeline_stages") or [])})

    def header_select(col, values):
        items = "\n".join(f'<option value="{v}">{v}</option>' for v in values)
        return (f'<select data-filter-col="{col}" onchange="applyFilters()" '
                f'style="width:100%; padding:0.2em; font-size:0.85em; border:1px solid #ccc; border-radius:3px; background:white; font-weight:normal;">'
                f'<option value="">— any —</option>{items}</select>')

    out.append(f"""<div style="margin:1em 0;">
  <input type="text" id="skillFilter" placeholder="🔍 free-text search across all fields…"
    style="width:100%; padding:0.5em 0.7em; font-size:1em; border:1px solid #ccc; border-radius:4px;"
    oninput="applyFilters()">
  <div style="display:flex; justify-content:space-between; align-items:center; margin-top:0.5em;">
    <button onclick="resetFilters()" style="padding:0.3em 0.8em; font-size:0.85em;">reset all</button>
    <span id="skillCount" style="color:#666; font-size:0.9em;"></span>
  </div>
</div>

<script>
function applyFilters() {{
  var q = (document.getElementById('skillFilter').value || '').toLowerCase().trim();
  var facets = {{}};
  document.querySelectorAll('select[data-filter-col]').forEach(function(sel) {{
    if (sel.value) facets[sel.dataset.filterCol] = sel.value;
  }});
  var n_visible = 0, n_total = 0;
  document.querySelectorAll('#skillsTable tbody tr').forEach(function(row) {{
    n_total++;
    var matchesText = !q || row.textContent.toLowerCase().includes(q);
    var matchesFacets = true;
    for (var col in facets) {{
      var rowVal = row.dataset[col] || '';
      if (col === 'stages') {{
        if (!rowVal.split(' ').includes(facets[col])) {{ matchesFacets = false; break; }}
      }} else {{
        if (rowVal !== facets[col]) {{ matchesFacets = false; break; }}
      }}
    }}
    var show = matchesText && matchesFacets;
    row.style.display = show ? '' : 'none';
    if (show) n_visible++;
  }});
  document.getElementById('skillCount').textContent = n_visible + ' / ' + n_total + ' skills';
}}
function resetFilters() {{
  document.getElementById('skillFilter').value = '';
  document.querySelectorAll('select[data-filter-col]').forEach(function(sel) {{ sel.value = ''; }});
  applyFilters();
}}
document.addEventListener('DOMContentLoaded', applyFilters);
</script>

<style>
#skillsTable {{ font-size:0.9em; width:100%; }}
#skillsTable th {{ vertical-align:top; padding:0.4em 0.5em; background:#f5f5f5; }}
#skillsTable th .col-label {{ display:block; font-size:0.9em; margin-bottom:0.3em; }}
#skillsTable td {{ padding:0.4em 0.5em; vertical-align:top; }}
</style>

<div style="overflow-x:auto;">
<table id="skillsTable">
<thead><tr>
<th><span class="col-label">Skill</span></th>
<th><span class="col-label">Pack</span>{header_select("pack", all_packs)}</th>
<th><span class="col-label">Field</span>{header_select("field", all_fields)}</th>
<th><span class="col-label">Category</span>{header_select("category", all_cats)}</th>
<th><span class="col-label">Stages</span>{header_select("stages", all_stages)}</th>
<th><span class="col-label">Description</span></th>
<th><span class="col-label">Detail</span></th>
<th><span class="col-label">Source</span></th>
</tr></thead>
<tbody>""")
    rows = []
    for p in packs:
        pk = p["pack"]
        pack_slug = pk["slug"]
        pack_name = pk["name"]
        pack_details_dir = SKILLS_DIR / pack_slug / "details"
        have_details = ({f.stem for f in pack_details_dir.glob("*.md")}
                        if pack_details_dir.exists() else set())
        for s in p.get("skills") or []:
            s_slug = s.get("slug", "")
            name = s.get("name", s_slug)
            field = s.get("field", "—") or "—"
            cat = s.get("category", "—") or "—"
            stages_list = s.get("pipeline_stages") or []
            stages_html = " ".join(f"<code>{x}</code>" for x in stages_list)
            stages_attr = " ".join(stages_list)
            desc = s.get("description", "—") or "—"
            source_url = s.get("details_url", "")
            source_cell = f'<a href="{source_url}" target="_blank" rel="noopener">↗</a>' if source_url else "—"
            detail_cell = (f'<a href="{pack_slug}/{s_slug}/">view</a>'
                           if s_slug in have_details else "—")
            rows.append((cat, name, pack_slug,
                         f'<tr data-pack="{pack_slug}" data-category="{cat}" '
                         f'data-field="{field}" data-stages="{stages_attr}">'
                         f"<td><code>{name}</code></td>"
                         f'<td><a href="{pack_slug}/">{pack_name}</a></td>'
                         f"<td>{field}</td>"
                         f"<td><code>{cat}</code></td>"
                         f"<td>{stages_html}</td>"
                         f"<td>{desc}</td>"
                         f"<td>{detail_cell}</td>"
                         f"<td>{source_cell}</td>"
                         f"</tr>"))
    for _, _, _, row_html in sorted(rows):
        out.append(row_html)
    out.append("</tbody></table>")
    out.append("</div>")
    out.append("")

    # Skills by category — click to filter the table above
    out.append("## Skill count by category")
    out.append("")
    out.append("*Click a category to filter the table above.*")
    out.append("")
    cat_counts: Counter[str] = Counter()
    for p in packs:
        for s in p.get("skills") or []:
            cat_counts[s.get("category", "unspecified")] += 1
    out.append('<table style="font-size:0.95em; max-width:30em;">')
    out.append("<thead><tr><th>Category</th><th style='text-align:right;'>Count</th></tr></thead>")
    out.append("<tbody>")
    for cat, n in sorted(cat_counts.items(), key=lambda x: (-x[1], x[0])):
        out.append(
            f'<tr style="cursor:pointer;" onclick="setCategoryFilter(\'{cat}\')">'
            f'<td><code>{cat}</code></td>'
            f'<td style="text-align:right;">{n}</td>'
            f'</tr>'
        )
    out.append("</tbody></table>")
    out.append("")
    out.append("""<script>
function setCategoryFilter(cat) {
  var sel = document.querySelector('select[data-filter-col="category"]');
  if (sel) {
    sel.value = cat;
    applyFilters();
    document.getElementById('skillsTable').scrollIntoView({behavior:'smooth', block:'start'});
  }
}
</script>
""")

    return "\n".join(out)


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    new_block = f"{start}\n{replacement}\n{end}"
    if pattern.search(text):
        return pattern.sub(new_block, text)
    return text + "\n\n" + new_block + "\n"


def main():
    packs = load_packs()
    DOCS_SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    # Wipe previous per-pack pages and per-skill subdirs
    for old in DOCS_SKILLS_DIR.glob("*.md"):
        if old.name == "index.md":
            continue
        old.unlink()
    for d in DOCS_SKILLS_DIR.iterdir():
        if d.is_dir():
            import shutil
            shutil.rmtree(d)

    # Per-pack pages
    for p in packs:
        content = render_pack_page(p)
        (DOCS_SKILLS_DIR / f"{p['pack']['slug']}.md").write_text(content, encoding="utf-8")

    # Per-skill detail pages (copied from skills/<pack>/details/)
    n_details = copy_skill_details(packs)
    print(f"Per-skill detail pages: {n_details}")

    # Index page
    idx_text = DOCS_SKILLS_INDEX.read_text(encoding="utf-8") if DOCS_SKILLS_INDEX.exists() else ""
    if not idx_text:
        idx_text = (
            "# Skills catalog\n\n"
            "Curated collections of Markdown-defined research skills "
            "(SKILL.md files, plugin commands, MCP servers) shipped by "
            "the projects in the [catalog](../projects/index.md).\n\n"
            "The pages below are **auto-generated** from `skills/*.yml`. "
            "Do not edit by hand — edit the YAML sources.\n\n"
            f"{INDEX_AUTO_START}\n*(Run `python scripts/build_skills_index.py` to populate.)*\n{INDEX_AUTO_END}\n"
        )
    idx_text = replace_between(idx_text, INDEX_AUTO_START, INDEX_AUTO_END, render_index(packs))
    DOCS_SKILLS_INDEX.write_text(idx_text, encoding="utf-8")

    print(f"=== Summary ===")
    print(f"Packs indexed:  {len(packs)}")
    print(f"Skills indexed: {sum(len(p.get('skills') or []) for p in packs)}")
    print(f"Pages written:  {len(packs) + 1}")


if __name__ == "__main__":
    sys.exit(main())
