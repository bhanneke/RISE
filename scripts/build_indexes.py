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


def render_papers_by_theme(papers: list[dict[str, Any]]) -> str:
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
            authors = p.get("authors", []) or []
            author_str = authors[0] if authors else "?"
            if len(authors) > 1:
                author_str += " et al."
            lines.append(
                f"- **{p.get('year', '?')}** — {author_str}. "
                f"[*{p.get('title', '')}*](notes/{p['_filename']}.md) "
                f"`{p.get('citekey', '')}`{status_badge(p.get('status', ''))}"
            )
        lines.append("")
    return "\n".join(lines)


def render_papers_by_year(papers: list[dict[str, Any]]) -> str:
    by_year: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for p in papers:
        by_year[p.get("year", 0)].append(p)
    if not by_year:
        return "\n*No papers indexed yet.*\n"
    lines: list[str] = [""]
    for year in sorted(by_year.keys(), reverse=True):
        lines.append(f"### {year}")
        lines.append("")
        for p in sorted(by_year[year], key=lambda x: x.get("citekey", "")):
            authors = p.get("authors", []) or []
            author_str = authors[0] if authors else "?"
            if len(authors) > 1:
                author_str += " et al."
            lines.append(
                f"- {author_str}. "
                f"[*{p.get('title', '')}*](notes/{p['_filename']}.md) "
                f"`{p.get('citekey', '')}`{status_badge(p.get('status', ''))}"
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
        return pattern.sub(new_block, text)
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

    papers_text = DOCS_PAPERS_INDEX.read_text(encoding="utf-8")
    papers_text = replace_between(
        papers_text, PAPERS_THEME_START, PAPERS_THEME_END,
        render_papers_by_theme(papers),
    )
    papers_text = replace_between(
        papers_text, PAPERS_YEAR_START, PAPERS_YEAR_END,
        render_papers_by_year(papers),
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
