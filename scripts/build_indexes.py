"""Regenerate the projects and papers index pages and per-project pages.

Reads:
  projects/*.yml
  projects/landscape/*.yml
  docs/papers/notes/*.md  (YAML front-matter)
  papers/references.bib

Writes:
  docs/projects/<slug>.md   (one per project, FULLY auto-generated)
  docs/projects/index.md    (comparison matrix between markers)
  docs/papers/index.md      (by-theme + by-year sections between markers)

No external dependencies beyond PyYAML. Run from repo root:

    python scripts/build_indexes.py
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = REPO_ROOT / "projects"
LANDSCAPE_DIR = PROJECTS_DIR / "landscape"
PAPERS_NOTES_DIR = REPO_ROOT / "docs" / "papers" / "notes"
BIB_FILE = REPO_ROOT / "papers" / "references.bib"
DOCS_PROJECTS_DIR = REPO_ROOT / "docs" / "projects"
DOCS_PROJECTS_INDEX = DOCS_PROJECTS_DIR / "index.md"
DOCS_PAPERS_INDEX = REPO_ROOT / "docs" / "papers" / "index.md"

GITHUB_BASE = "https://github.com/bhanneke/RISE/blob/main"

PROJECT_AUTO_START = "<!-- AUTO-GENERATED:projects-start -->"
PROJECT_AUTO_END = "<!-- AUTO-GENERATED:projects-end -->"
PAPERS_THEME_START = "<!-- AUTO-GENERATED:papers-by-theme-start -->"
PAPERS_THEME_END = "<!-- AUTO-GENERATED:papers-by-theme-end -->"
PAPERS_YEAR_START = "<!-- AUTO-GENERATED:papers-by-year-start -->"
PAPERS_YEAR_END = "<!-- AUTO-GENERATED:papers-by-year-end -->"

SCORE_KEYS = [
    "lifecycle_coverage",
    "autonomy_level",
    "architectural_transparency",
    "inputs_supported",
    "outputs_reproducibility",
    "internal_evaluation",
    "openness",
    "maturity_traction",
    # v0.2 — architectural dimensions from ARIS Table 4 analogy
    "cross_family_policy",
    "assurance_runtime",
    "cross_platform_portability",
]
SCORE_HEADERS = [
    "LC", "AUT", "ARC", "IN", "OUT", "EVAL", "OPEN", "MAT",
    "XF", "RUN", "PORT",
]
SCORE_LABELS = {
    "lifecycle_coverage": "Lifecycle coverage",
    "autonomy_level": "Autonomy level",
    "architectural_transparency": "Architectural transparency",
    "inputs_supported": "Inputs supported",
    "outputs_reproducibility": "Outputs / reproducibility",
    "internal_evaluation": "Internal evaluation",
    "openness": "Openness",
    "maturity_traction": "Maturity / traction",
    "cross_family_policy": "Cross-family policy",
    "assurance_runtime": "Runtime assurance",
    "cross_platform_portability": "Cross-platform portability",
}

PAGE_HEADER = "<!-- DO NOT EDIT — auto-generated from {path} by scripts/build_indexes.py -->"


def load_projects() -> list[dict[str, Any]]:
    files = sorted(PROJECTS_DIR.glob("*.yml"))
    files += sorted(LANDSCAPE_DIR.glob("*.yml"))
    projects: list[dict[str, Any]] = []
    for f in files:
        with f.open("r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        if not data:
            continue
        data["_path"] = f.relative_to(REPO_ROOT).as_posix()
        projects.append(data)
    return projects


def parse_front_matter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    front = yaml.safe_load(text[4:end]) or {}
    return front, text[end + 5 :]


def load_papers() -> list[dict[str, Any]]:
    papers: list[dict[str, Any]] = []
    if not PAPERS_NOTES_DIR.exists():
        return papers
    for f in sorted(PAPERS_NOTES_DIR.glob("*.md")):
        with f.open("r", encoding="utf-8") as fh:
            text = fh.read()
        front, _ = parse_front_matter(text)
        if not front:
            continue
        # Filename relative to docs/, used for in-site links.
        front["_doc_path"] = f.relative_to(REPO_ROOT / "docs").as_posix()
        front["_filename"] = f.stem
        papers.append(front)
    return papers


def load_bibtex_citekeys() -> set[str]:
    if not BIB_FILE.exists():
        return set()
    text = BIB_FILE.read_text(encoding="utf-8")
    return set(re.findall(r"@\w+\{([^,\s]+),", text))


# ── Proper brace-aware bibtex parser ──────────────────────────────────

def _bib_read_value(body: str, start: int) -> tuple[str, int]:
    if start >= len(body):
        return "", start
    if body[start] == "{":
        depth, i = 1, start + 1
        while i < len(body) and depth > 0:
            if body[i] == "{":
                depth += 1
            elif body[i] == "}":
                depth -= 1
                if depth == 0:
                    return body[start + 1 : i], i + 1
            i += 1
        return body[start + 1 :], len(body)
    elif body[start] == '"':
        end = body.find('"', start + 1)
        if end == -1:
            return body[start + 1 :], len(body)
        return body[start + 1 : end], end + 1
    end = start
    while end < len(body) and body[end] not in ",\n":
        end += 1
    return body[start:end].strip(), end


def load_bibtex_entries() -> dict[str, dict[str, str]]:
    """Parse references.bib into {citekey: {field: value}}."""
    if not BIB_FILE.exists():
        return {}
    text = BIB_FILE.read_text(encoding="utf-8")
    entries: dict[str, dict[str, str]] = {}
    for entry_match in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        kind, citekey = entry_match.group(1), entry_match.group(2)
        body_start = entry_match.end()
        depth, i = 1, body_start
        while i < len(text) and depth > 0:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        body = text[body_start:i]
        fields = {"_kind": kind}
        j = 0
        while j < len(body):
            fm = re.match(r"\s*(\w+)\s*=\s*", body[j:])
            if not fm:
                j += 1
                continue
            name = fm.group(1).lower()
            val_start = j + fm.end()
            value, val_end = _bib_read_value(body, val_start)
            # Strip remaining {} (e.g. {AI}) for display
            value = re.sub(r"[{}]", "", value)
            fields[name] = re.sub(r"\s+", " ", value).strip()
            j = val_end
            while j < len(body) and body[j] in ", \n\t":
                j += 1
        entries[citekey] = fields
    return entries


def short_authors(author_field: str) -> str:
    """Render BibTeX author list as 'Lastname et al.' or 'A & B'."""
    if not author_field:
        return "?"
    authors = [a.strip() for a in re.split(r"\s+and\s+", author_field)]
    def lastname(a: str) -> str:
        if "," in a:
            return a.split(",", 1)[0].strip()
        parts = a.split()
        return parts[-1] if parts else a
    if len(authors) == 1:
        return lastname(authors[0])
    if len(authors) == 2:
        return f"{lastname(authors[0])} & {lastname(authors[1])}"
    return f"{lastname(authors[0])} et al."


def venue_short(entry: dict[str, str]) -> str:
    v = (entry.get("journal") or entry.get("booktitle") or
         entry.get("howpublished") or entry.get("institution") or "")
    if not v and entry.get("eprint"):
        v = "arXiv"
    return v


# ── per-project page rendering ────────────────────────────────────────


def chips(label: str, items: list[str] | None) -> str:
    if not items:
        return ""
    chips_str = " ".join(f"`{x}`" for x in items)
    return f"**{label}:** {chips_str}\n\n"


def render_project_page(
    project: dict[str, Any],
    papers_by_ck: dict[str, dict[str, Any]],
) -> str:
    name = project["name"]
    slug = project["slug"]
    src_path = project["_path"]

    out: list[str] = []
    out.append(PAGE_HEADER.format(path=src_path))
    out.append("")
    out.append(f"# {name}")
    out.append("")

    meta_bits = []
    if project.get("type"):
        meta_bits.append(f"`{project['type']}`")
    if project.get("status"):
        meta_bits.append(f"status: `{project['status']}`")
    if project.get("focus"):
        meta_bits.append(f"focus: `{project['focus']}`")
    if project.get("discipline"):
        meta_bits.append(f"discipline: `{project['discipline']}`")
    if project.get("year_started"):
        meta_bits.append(f"started: {project['year_started']}")
    if meta_bits:
        out.append(" · ".join(meta_bits))
        out.append("")
    if project.get("url"):
        out.append(f"**Project page:** <{project['url']}>")
        out.append("")
    out.append(f"**Source:** [`{src_path}`]({GITHUB_BASE}/{src_path})")
    out.append("")

    positioning = (project.get("positioning") or "").strip()
    if positioning:
        out.append("## Positioning")
        out.append("")
        out.append(positioning)
        out.append("")

    contribution = (project.get("distinctive_contribution") or "").strip()
    if contribution:
        out.append("## Distinctive contribution")
        out.append("")
        out.append(contribution)
        out.append("")

    # Scores table
    scores = project.get("scores") or {}
    if scores:
        out.append("## Evaluation scores")
        out.append("")
        out.append("| Dimension | Score (0–3) | Note |")
        out.append("|---|:---:|---|")
        for k in SCORE_KEYS:
            v = scores.get(k) or {}
            s = v.get("score") if isinstance(v, dict) else None
            note = v.get("note") if isinstance(v, dict) else ""
            out.append(
                f"| {SCORE_LABELS[k]} | {('—' if s is None else s)} | {note or ''} |"
            )
        out.append("")
        if project.get("scored_on"):
            out.append(f"*Scored on {project['scored_on']}. See the [evaluation rubric]({GITHUB_BASE}/projects/EVALUATION.md).*")
            out.append("")

    # Tag chips
    out.append("## Tags")
    out.append("")
    out.append(chips("Pipeline stages", project.get("pipeline_stages")))
    out.append(chips("Architectural features", project.get("architectural_features")))

    if project.get("inputs"):
        out.append(chips("Inputs", project.get("inputs")))
    if project.get("outputs"):
        out.append(chips("Outputs", project.get("outputs")))
    if project.get("data_sources"):
        out.append(chips("Data sources", project.get("data_sources")))
    if project.get("knowledge_sources"):
        out.append(chips("Knowledge sources", project.get("knowledge_sources")))

    # Limitations
    limitations = project.get("limitations") or []
    if limitations:
        out.append("## Limitations")
        out.append("")
        for x in limitations:
            out.append(f"- {x}")
        out.append("")

    # Related
    related = project.get("related") or []
    if related:
        out.append("## Related projects in this catalog")
        out.append("")
        for r in related:
            out.append(f"- [`{r}`]({r}.md)")
        out.append("")

    # Papers describing the project itself
    papers_list = project.get("papers") or []
    if papers_list:
        out.append("## Papers describing this project")
        out.append("")
        for p in papers_list:
            title = p.get("title", "")
            authors = p.get("authors") or []
            year = p.get("year", "")
            venue = p.get("venue", "")
            a = ", ".join(authors) if authors else "?"
            line = f"- **{title}** — {a} ({year})"
            if venue:
                line += f". *{venue}*"
            links = []
            if p.get("arxiv_id"):
                aid = p["arxiv_id"]
                links.append(f"[arXiv:{aid}](https://arxiv.org/abs/{aid})")
            if p.get("doi"):
                links.append(f"[doi]({p['doi'] if p['doi'].startswith('http') else 'https://doi.org/' + p['doi']})")
            if p.get("ssrn_id"):
                links.append(f"[SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id={p['ssrn_id']})")
            if p.get("url") and not links:
                links.append(f"[link]({p['url']})")
            if links:
                line += ". " + " · ".join(links)
            out.append(line)
        out.append("")

    # Cross-references in external surveys
    compared = project.get("compared_in") or []
    if compared:
        out.append("## Also compared in")
        out.append("")
        for c in compared:
            src = c.get("source", "?")
            ck = c.get("citekey")
            note = c.get("note", "")
            line = f"- **{src}**"
            if ck:
                line += f" ([`{ck}`]({GITHUB_BASE}/papers/references.bib))"
            if note:
                line += f" — {note}"
            out.append(line)
        out.append("")

    # References
    refs = project.get("references") or []
    if refs:
        out.append("## Related references (literature catalog)")
        out.append("")
        for ck in refs:
            paper = papers_by_ck.get(ck)
            if paper:
                year = paper.get("year", "")
                title = paper.get("title", "")
                authors = paper.get("authors") or []
                a = authors[0] if authors else "?"
                if len(authors) > 1:
                    a += " et al."
                out.append(
                    f"- {a} ({year}). "
                    f"[*{title}*](../papers/notes/{paper['_filename']}.md) "
                    f"`{ck}`"
                )
            else:
                out.append(
                    f"- `{ck}` "
                    f"([BibTeX]({GITHUB_BASE}/papers/references.bib))"
                )
        out.append("")

    return "\n".join(out).rstrip() + "\n"


def write_project_pages(
    projects: list[dict[str, Any]],
    papers_by_ck: dict[str, dict[str, Any]],
) -> int:
    DOCS_PROJECTS_DIR.mkdir(parents=True, exist_ok=True)
    # Wipe previous auto-generated pages (anything except index.md).
    for old in DOCS_PROJECTS_DIR.glob("*.md"):
        if old.name == "index.md":
            continue
        old.unlink()
    written = 0
    for p in projects:
        slug = p.get("slug")
        if not slug:
            continue
        content = render_project_page(p, papers_by_ck)
        (DOCS_PROJECTS_DIR / f"{slug}.md").write_text(content, encoding="utf-8")
        written += 1
    return written


# ── projects index (matrix) ───────────────────────────────────────────


def render_projects_section(projects: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("")
    lines.append("### Comparison matrix")
    lines.append("")
    header = ["Project", "Type", "Focus"] + SCORE_HEADERS + ["Discipline"]
    lines.append("| " + " | ".join(header) + " |")
    lines.append("|" + "|".join(["---"] * len(header)) + "|")
    for p in sorted(
        projects,
        key=lambda x: (x.get("type", "") != "owned", x.get("slug", "")),
    ):
        scores = p.get("scores", {}) or {}
        row_scores = []
        for k in SCORE_KEYS:
            v = scores.get(k, {})
            s = v.get("score") if isinstance(v, dict) else None
            row_scores.append("—" if s is None else str(s))
        cells = [
            f"[{p['name']}]({p['slug']}.md)",
            p.get("type", ""),
            f"`{p.get('focus', '—')}`",
            *row_scores,
            p.get("discipline", ""),
        ]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    lines.append(
        "*Score columns: LC = lifecycle coverage, AUT = autonomy, "
        "ARC = architectural transparency, IN = inputs supported, "
        "OUT = outputs/reproducibility, EVAL = internal evaluation, "
        "OPEN = openness, MAT = maturity/traction, "
        "XF = cross-family policy, RUN = runtime assurance, "
        "PORT = cross-platform portability. Scale 0–3. "
        f"See the [evaluation rubric]({GITHUB_BASE}/projects/EVALUATION.md).*"
    )
    lines.append("")

    lines.append("### One-line summaries")
    lines.append("")
    for p in sorted(
        projects,
        key=lambda x: (x.get("type", "") != "owned", x.get("slug", "")),
    ):
        positioning = (p.get("positioning") or "").strip().split("\n")[0]
        # First sentence only.
        first_sentence = re.split(r"(?<=[.!?])\s", positioning, maxsplit=1)[0]
        lines.append(
            f"- **[{p['name']}]({p['slug']}.md)** — {first_sentence}"
        )
    lines.append("")
    return "\n".join(lines)


# ── papers index ──────────────────────────────────────────────────────


def status_badge(status: str) -> str:
    """Visible inline marker for note completion state."""
    return {
        "queued":     " ⚠️ *stub*",
        "skimmed":    " · skimmed",
        "read":       "",
        "re-reading": " · re-reading",
    }.get(status or "", "")


def _open_access_label(url: str) -> str:
    """Short, recognizable label for a secondary open-access URL."""
    u = url.lower()
    if "nber.org" in u:           return "NBER"
    if "ssrn.com" in u:           return "SSRN"
    if "arxiv.org" in u:          return "arXiv"
    if "openreview.net" in u:     return "OpenReview"
    if "papers.nips.cc" in u or "papers.neurips.cc" in u: return "NeurIPS"
    if "aclanthology.org" in u:   return "ACL"
    if "blog." in u:              return "blog"
    return "open"


def render_papers_table(papers: list[dict[str, Any]], bib: dict[str, dict[str, str]]) -> str:
    """Render the full filterable papers table — bib is the source of truth.

    Columns: Year · Authors · Title · Venue · DOI/arXiv · Themes · Status · Note
    """
    # Build by_citekey for papers (notes data: status, themes, doc_path)
    notes_by_ck = {p.get("citekey"): p for p in papers if p.get("citekey")}

    # Include every bib entry, even if it has no note
    rows = []
    for ck in sorted(bib.keys()):
        entry = bib[ck]
        note = notes_by_ck.get(ck, {})
        year = entry.get("year") or note.get("year", "") or "?"
        authors = short_authors(entry.get("author", "") or
                                " and ".join(note.get("authors", []) or []))
        title = entry.get("title") or note.get("title", "") or ""
        # Convert BibTeX dash conventions to real Unicode dashes
        title = title.replace("---", "—").replace("--", "–")
        venue = venue_short(entry) or note.get("venue", "")
        doi = entry.get("doi", "")
        arxiv = entry.get("eprint", "")
        themes = " ".join(f"`{t}`" for t in (note.get("themes") or []))
        status = (note.get("status") or "—")

        # Build link cell — prefer DOI (real journal DOI > derived arXiv DOI),
        # then bib url field, then howpublished URL. arXiv has assigned DOIs of
        # the form 10.48550/arXiv.<eprint> since 2022, so we always derive one
        # when an eprint is present and no real DOI is set. When an entry has
        # BOTH a journal DOI and an open-access URL (e.g., NBER/SSRN preprint),
        # render both so readers can reach a freely-readable copy.
        links = []
        if doi:
            doi_url = doi if doi.startswith("http") else "https://doi.org/" + doi
            links.append(f'<a href="{doi_url}" target="_blank" rel="noopener">doi</a>')
            # Secondary open-access link if explicitly provided
            extra = entry.get("url", "")
            if extra and extra.startswith("http"):
                label = _open_access_label(extra)
                links.append(f'<a href="{extra}" target="_blank" rel="noopener">{label}</a>')
        elif arxiv:
            doi_url = f"https://doi.org/10.48550/arXiv.{arxiv}"
            links.append(f'<a href="{doi_url}" target="_blank" rel="noopener">doi (arXiv)</a>')
        elif entry.get("url"):
            links.append(f'<a href="{entry["url"]}" target="_blank" rel="noopener">link</a>')
        elif entry.get("howpublished", "").startswith("http"):
            links.append(f'<a href="{entry["howpublished"]}" target="_blank" rel="noopener">link</a>')
        link = " · ".join(links) if links else "—"

        # Title links to note if note exists; else plain (raw HTML)
        if note.get("_filename"):
            title_cell = f'<a href="notes/{note["_filename"]}/">{title}</a>'
        else:
            title_cell = title

        # Themes as raw HTML chips
        theme_chips = " ".join(f"<code>{t}</code>" for t in (note.get("themes") or []))

        rows.append({
            "ck": ck,
            "year": str(year),
            "authors": authors,
            "title_cell": title_cell,
            "title_plain": title,
            "venue": venue,
            "link": link,
            "themes": theme_chips,
            "status": status,
        })

    # Collect per-paper themes for the facet dropdown
    themes_per_row: dict[str, list[str]] = {}
    for ck in sorted(bib.keys()):
        note = notes_by_ck.get(ck, {})
        themes_per_row[ck] = note.get("themes") or []

    n_total = len(rows)
    n_with_note = sum(1 for r in rows if r["status"] != "—")
    n_read = sum(1 for r in rows if r["status"] == "read")

    # Distinct values for per-column filter dropdowns
    all_years   = sorted({r["year"] for r in rows if r["year"]}, reverse=True)
    all_venues  = sorted({r["venue"] for r in rows if r["venue"]})
    all_themes  = sorted({t for ts in themes_per_row.values() for t in ts})
    all_status  = sorted({r["status"] for r in rows if r["status"]})

    def header_select(col, values):
        items = "\n".join(f'<option value="{v}">{v}</option>' for v in values)
        return (f'<select data-filter-col="{col}" onchange="applyPaperFilters()" '
                f'style="width:100%; padding:0.2em; font-size:0.85em; '
                f'border:1px solid #ccc; border-radius:3px; background:white; font-weight:normal;">'
                f'<option value="">— any —</option>{items}</select>')

    out: list[str] = []
    out.append(
        f"*{n_total} bibliographic entries; {n_with_note} have curator notes "
        f"({n_read} fully read). Filter via the column headers or the search box.*"
    )
    out.append("")

    # Global text search + reset
    out.append("""<div style="margin:1em 0; display:flex; gap:0.5em; align-items:center;">
  <input type="text" id="paperFilter" placeholder="🔍 search author / title / venue / theme / citekey…"
    style="flex:1; padding:0.5em; font-size:1em; border:1px solid #ccc; border-radius:4px;"
    oninput="applyPaperFilters()">
  <button type="button" onclick="resetPaperFilters()"
    style="padding:0.5em 1em; border:1px solid #ccc; border-radius:4px; background:#f5f5f5; cursor:pointer;">
    Reset
  </button>
  <span id="paperCount" style="white-space:nowrap; color:#666; font-size:0.9em;"></span>
</div>

<script>
function applyPaperFilters() {
  var q = (document.getElementById('paperFilter').value || '').toLowerCase().trim();
  var sels = document.querySelectorAll('#papersTable select[data-filter-col]');
  var facets = {};
  sels.forEach(function(s){ if (s.value) facets[s.dataset.filterCol] = s.value; });
  var rows = document.querySelectorAll('#papersTable tbody tr');
  var shown = 0;
  rows.forEach(function(row){
    var ok = true;
    Object.keys(facets).forEach(function(col){
      var cell = row.getAttribute('data-' + col) || '';
      if (col === 'themes') {
        if (cell.split('|').indexOf(facets[col]) === -1) ok = false;
      } else if (cell !== facets[col]) {
        ok = false;
      }
    });
    if (ok && q) {
      if (row.textContent.toLowerCase().indexOf(q) === -1) ok = false;
    }
    row.style.display = ok ? '' : 'none';
    if (ok) shown++;
  });
  var c = document.getElementById('paperCount');
  if (c) c.textContent = shown + ' / ' + rows.length + ' papers';
}
function resetPaperFilters() {
  document.getElementById('paperFilter').value = '';
  document.querySelectorAll('#papersTable select[data-filter-col]').forEach(function(s){ s.value = ''; });
  applyPaperFilters();
}
document.addEventListener('DOMContentLoaded', applyPaperFilters);
</script>
""")

    # Build the HTML table directly
    out.append('<table id="papersTable" markdown>')
    out.append("<thead>")
    out.append("<tr>"
               "<th>Year</th><th>Authors</th><th>Title</th>"
               "<th>Venue</th><th>Link</th><th>Themes</th>"
               "<th>Citekey</th><th>Note</th>"
               "</tr>")
    # Filter row inside thead
    out.append("<tr>"
               f"<th>{header_select('year', all_years)}</th>"
               "<th></th>"
               "<th></th>"
               f"<th>{header_select('venue', all_venues)}</th>"
               "<th></th>"
               f"<th>{header_select('themes', all_themes)}</th>"
               "<th></th>"
               f"<th>{header_select('status', all_status)}</th>"
               "</tr>")
    out.append("</thead>")
    out.append("<tbody markdown>")
    for r in sorted(rows, key=lambda x: (x["year"], x["authors"])):
        theme_attr = "|".join(themes_per_row.get(r["ck"], []))
        out.append(
            f'<tr data-year="{r["year"]}" data-venue="{r["venue"]}" '
            f'data-themes="{theme_attr}" data-status="{r["status"]}">'
            f"<td>{r['year']}</td>"
            f"<td>{r['authors']}</td>"
            f"<td>{r['title_cell']}</td>"
            f"<td>{r['venue']}</td>"
            f"<td>{r['link']}</td>"
            f"<td>{r['themes']}</td>"
            f"<td><code>{r['ck']}</code></td>"
            f"<td>{r['status']}</td>"
            f"</tr>"
        )
    out.append("</tbody>")
    out.append("</table>")
    out.append("")
    return "\n".join(out)


def render_papers_by_theme(papers: list[dict[str, Any]], bib: dict[str, dict[str, str]] | None = None) -> str:
    bib = bib or {}
    by_theme: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for p in papers:
        for t in p.get("themes", []) or []:
            by_theme[t].append(p)
    if not by_theme:
        return "\n*No papers indexed yet.*\n"
    lines: list[str] = [""]
    for theme in sorted(by_theme.keys()):
        lines.append(f"### `{theme}`")
        lines.append("")
        for p in sorted(by_theme[theme], key=lambda x: (x.get("year", 0), x.get("citekey", ""))):
            ck = p.get("citekey", "")
            entry = bib.get(ck, {})
            # Use bib as source of truth, fall back to note
            title = entry.get("title") or p.get("title", "") or ""
            year = entry.get("year") or p.get("year", "") or "?"
            authors = short_authors(entry.get("author", "")) if entry.get("author") else (
                (p.get("authors", [None])[0] or "?") + (" et al." if len(p.get("authors", []) or []) > 1 else "")
            )
            lines.append(
                f"- **{year}** — {authors}. "
                f"[*{title}*](notes/{p['_filename']}.md) "
                f"`{ck}`{status_badge(p.get('status', ''))}"
            )
        lines.append("")
    return "\n".join(lines)


def render_papers_by_year(papers: list[dict[str, Any]], bib: dict[str, dict[str, str]] | None = None) -> str:
    bib = bib or {}
    # Year sourced from bib
    by_year: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for p in papers:
        ck = p.get("citekey", "")
        year = bib.get(ck, {}).get("year") or p.get("year", "") or "?"
        by_year[str(year)].append(p)
    if not by_year:
        return "\n*No papers indexed yet.*\n"
    lines: list[str] = [""]
    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f"### {year}")
        lines.append("")
        for p in sorted(by_year[year], key=lambda x: x.get("citekey", "")):
            ck = p.get("citekey", "")
            entry = bib.get(ck, {})
            title = entry.get("title") or p.get("title", "") or ""
            authors = short_authors(entry.get("author", "")) if entry.get("author") else (
                (p.get("authors", [None])[0] or "?") + (" et al." if len(p.get("authors", []) or []) > 1 else "")
            )
            lines.append(
                f"- {authors}. "
                f"[*{title}*](notes/{p['_filename']}.md) "
                f"`{ck}`{status_badge(p.get('status', ''))}"
            )
        lines.append("")
    # Summary at top
    n_total = len(papers)
    n_filled = sum(1 for p in papers if (p.get("status") or "") in ("skimmed", "read", "re-reading"))
    n_stubs = sum(1 for p in papers if (p.get("status") or "") == "queued")
    header = (
        f"*{n_filled}/{n_total} notes have been filled with abstract-grounded summaries; "
        f"{n_stubs} remain as stubs marked ⚠️ (front-matter verified, but Summary / Contribution / Method / Critique not yet written).*\n"
    )
    return header + "\n".join(lines)


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end),
        re.DOTALL,
    )
    new_block = f"{start}\n{replacement}\n{end}"
    if pattern.search(text):
        # literal replacement: bibtex-derived content may contain LaTeX
        # escapes (e.g. {\^\i}) that re.sub would misparse as escape sequences
        return pattern.sub(lambda _m: new_block, text)
    return text + "\n\n" + new_block + "\n"


# ── validation ────────────────────────────────────────────────────────


def validate(
    projects: list[dict[str, Any]],
    papers: list[dict[str, Any]],
) -> list[str]:
    errors: list[str] = []
    citekeys = load_bibtex_citekeys()
    slugs = {p.get("slug") for p in projects}

    for p in projects:
        for ref in p.get("references", []) or []:
            if ref not in citekeys:
                errors.append(
                    f"{p['_path']}: references unknown citekey '{ref}'"
                )
        for rel in p.get("related", []) or []:
            if rel not in slugs:
                errors.append(
                    f"{p['_path']}: related project '{rel}' not found"
                )

    for paper in papers:
        ck = paper.get("citekey")
        if ck and ck not in citekeys:
            errors.append(
                f"{paper['_doc_path']}: citekey '{ck}' missing from references.bib"
            )
        for rel in paper.get("relates_to_projects", []) or []:
            if rel not in slugs:
                errors.append(
                    f"{paper['_doc_path']}: relates_to_projects '{rel}' not found"
                )

    return errors


# ── main ──────────────────────────────────────────────────────────────


def main() -> int:
    projects = load_projects()
    papers = load_papers()
    papers_by_ck = {p["citekey"]: p for p in papers if p.get("citekey")}

    errors = validate(projects, papers)
    for e in errors:
        print(f"  WARN: {e}", file=sys.stderr)

    pages_written = write_project_pages(projects, papers_by_ck)

    projects_section = render_projects_section(projects)
    projects_text = DOCS_PROJECTS_INDEX.read_text(encoding="utf-8")
    projects_text = replace_between(
        projects_text, PROJECT_AUTO_START, PROJECT_AUTO_END, projects_section
    )
    DOCS_PROJECTS_INDEX.write_text(projects_text, encoding="utf-8")

    bib_entries = load_bibtex_entries()
    papers_text = DOCS_PAPERS_INDEX.read_text(encoding="utf-8")
    # New: full filterable table from bib (single source of truth)
    PAPERS_TABLE_START = "<!-- AUTO-GENERATED:papers-table-start -->"
    PAPERS_TABLE_END = "<!-- AUTO-GENERATED:papers-table-end -->"
    papers_text = replace_between(
        papers_text, PAPERS_TABLE_START, PAPERS_TABLE_END,
        render_papers_table(papers, bib_entries),
    )
    papers_text = replace_between(
        papers_text, PAPERS_THEME_START, PAPERS_THEME_END,
        render_papers_by_theme(papers, bib_entries),
    )
    papers_text = replace_between(
        papers_text, PAPERS_YEAR_START, PAPERS_YEAR_END,
        render_papers_by_year(papers, bib_entries),
    )
    DOCS_PAPERS_INDEX.write_text(papers_text, encoding="utf-8")

    print(
        f"=== Summary ===\n"
        f"Projects indexed:   {len(projects)}\n"
        f"Project pages built: {pages_written}\n"
        f"Papers indexed:     {len(papers)}\n"
        f"Validation warnings: {len(errors)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
