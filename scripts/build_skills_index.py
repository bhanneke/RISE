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

GITHUB_BASE = "https://github.com/bhanneke/RISE/blob/main"

INDEX_AUTO_START = "<!-- AUTO-GENERATED:skills-start -->"
INDEX_AUTO_END = "<!-- AUTO-GENERATED:skills-end -->"


def load_packs() -> list[dict[str, Any]]:
    packs = []
    for f in sorted(SKILLS_DIR.glob("*.yml")):
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
    for cat in sorted(by_cat.keys()):
        out.append(f"### `{cat}` ({len(by_cat[cat])})")
        out.append("")
        out.append("| Skill | Field | Stages | Description | Source | Updated |")
        out.append("|---|---|---|---|---|---|")
        for s in sorted(by_cat[cat], key=lambda x: x.get("slug", "")):
            slug = s.get("slug", "")
            name = s.get("name", slug)
            field = s.get("field", "—") or "—"
            stages = " ".join(f"`{x}`" for x in (s.get("pipeline_stages") or []))
            desc = s.get("description", "") or "—"
            details = s.get("details_url", "")
            details_cell = f"[link]({details})" if details else "—"
            updated = s.get("last_update", "") or "—"
            out.append(
                f"| `{name}` | {field} | {stages} | {desc} | {details_cell} | {updated} |"
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

    # Filterable all-skills table
    out.append("## All skills (filterable)")
    out.append("")
    out.append("""<input type="text" id="skillFilter" placeholder="🔍 filter by skill name / pack / field / category / pipeline stage…"
  style="width:100%; padding:0.5em; margin:1em 0; font-size:1em; border:1px solid #ccc; border-radius:4px;"
  oninput="filterSkills(this.value)">

<script>
function filterSkills(q) {
  q = q.toLowerCase().trim();
  document.querySelectorAll('#skillsTable tbody tr').forEach(function(row) {
    row.style.display = (!q || row.textContent.toLowerCase().includes(q)) ? '' : 'none';
  });
}
</script>
""")
    out.append('<table id="skillsTable">')
    out.append("<thead><tr>"
               "<th>Skill</th><th>Pack</th><th>Field</th><th>Category</th>"
               "<th>Stages</th><th>Description</th><th>Source</th><th>Updated</th>"
               "</tr></thead>")
    out.append("<tbody>")
    rows = []
    for p in packs:
        pk = p["pack"]
        pack_slug = pk["slug"]
        pack_name = pk["name"]
        for s in p.get("skills") or []:
            name = s.get("name", s.get("slug", ""))
            field = s.get("field", "—") or "—"
            cat = s.get("category", "—") or "—"
            stages = " ".join(f"<code>{x}</code>" for x in (s.get("pipeline_stages") or []))
            desc = s.get("description", "—") or "—"
            details = s.get("details_url", "")
            details_cell = f'<a href="{details}">link</a>' if details else "—"
            updated = s.get("last_update", "—") or "—"
            rows.append((cat, name, pack_slug,
                         f"<tr>"
                         f"<td><code>{name}</code></td>"
                         f'<td><a href="{pack_slug}.md">{pack_name}</a></td>'
                         f"<td>{field}</td>"
                         f"<td><code>{cat}</code></td>"
                         f"<td>{stages}</td>"
                         f"<td>{desc}</td>"
                         f"<td>{details_cell}</td>"
                         f"<td>{updated}</td>"
                         f"</tr>"))
    for _, _, _, row_html in sorted(rows):
        out.append(row_html)
    out.append("</tbody></table>")
    out.append("")

    # Skills by category across all packs
    out.append("## Skill count by category (across packs)")
    out.append("")
    cat_counts: Counter[str] = Counter()
    for p in packs:
        for s in p.get("skills") or []:
            cat_counts[s.get("category", "unspecified")] += 1
    out.append("| Category | Count |")
    out.append("|---|---:|")
    for cat, n in sorted(cat_counts.items(), key=lambda x: (-x[1], x[0])):
        out.append(f"| `{cat}` | {n} |")
    out.append("")

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

    # Wipe previous per-pack pages
    for old in DOCS_SKILLS_DIR.glob("*.md"):
        if old.name == "index.md":
            continue
        old.unlink()

    # Per-pack pages
    for p in packs:
        content = render_pack_page(p)
        (DOCS_SKILLS_DIR / f"{p['pack']['slug']}.md").write_text(content, encoding="utf-8")

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
