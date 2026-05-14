"""Regenerate the projects and papers index pages from source files.

Reads:
  projects/*.yml
  projects/landscape/*.yml
  papers/notes/*.md  (YAML front-matter)
  papers/references.bib

Writes:
  docs/projects/index.md   (auto-generated section between markers)
  docs/papers/index.md     (auto-generated sections between markers)

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
PAPERS_NOTES_DIR = REPO_ROOT / "papers" / "notes"
BIB_FILE = REPO_ROOT / "papers" / "references.bib"
DOCS_PROJECTS_INDEX = REPO_ROOT / "docs" / "projects" / "index.md"
DOCS_PAPERS_INDEX = REPO_ROOT / "docs" / "papers" / "index.md"

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
]
SCORE_HEADERS = ["LC", "AUT", "ARC", "IN", "OUT", "EVAL", "OPEN", "MAT"]


def load_projects() -> list[dict[str, Any]]:
    files = sorted([p for p in PROJECTS_DIR.glob("*.yml")])
    files += sorted([p for p in LANDSCAPE_DIR.glob("*.yml")])
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
    for f in sorted(PAPERS_NOTES_DIR.glob("*.md")):
        with f.open("r", encoding="utf-8") as fh:
            text = fh.read()
        front, _ = parse_front_matter(text)
        if not front:
            continue
        front["_path"] = f.relative_to(REPO_ROOT).as_posix()
        papers.append(front)
    return papers


def load_bibtex_citekeys() -> set[str]:
    if not BIB_FILE.exists():
        return set()
    text = BIB_FILE.read_text(encoding="utf-8")
    return set(re.findall(r"@\w+\{([^,\s]+),", text))


def render_projects_section(projects: list[dict[str, Any]]) -> str:
    lines: list[str] = []
    lines.append("")
    lines.append("### Comparison matrix")
    lines.append("")
    lines.append(
        "| Project | Type | "
        + " | ".join(SCORE_HEADERS)
        + " | Discipline |"
    )
    lines.append(
        "|---|---|"
        + "|".join(["---"] * len(SCORE_HEADERS))
        + "|---|"
    )
    for p in projects:
        scores = p.get("scores", {}) or {}
        row_scores = []
        for k in SCORE_KEYS:
            v = scores.get(k, {})
            s = v.get("score") if isinstance(v, dict) else None
            row_scores.append("—" if s is None else str(s))
        lines.append(
            f"| [{p['name']}](../../{p['_path']}) "
            f"| {p.get('type', '')} "
            f"| " + " | ".join(row_scores) + " "
            f"| {p.get('discipline', '')} |"
        )
    lines.append("")
    lines.append(
        "*Score columns: LC = lifecycle coverage, AUT = autonomy, "
        "ARC = architectural transparency, IN = inputs supported, "
        "OUT = outputs/reproducibility, EVAL = internal evaluation, "
        "OPEN = openness, MAT = maturity/traction. Scale 0–3. "
        "See [`projects/EVALUATION.md`](../../projects/EVALUATION.md).*"
    )
    lines.append("")

    lines.append("### Entries")
    lines.append("")
    for p in projects:
        lines.append(f"#### [{p['name']}](../../{p['_path']})")
        positioning = (p.get("positioning") or "").strip()
        if positioning:
            lines.append("")
            lines.append(positioning)
        lines.append("")
    return "\n".join(lines)


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
                f"[*{p.get('title', '')}*](../../{p['_path']}) "
                f"`{p.get('citekey', '')}`"
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
                f"[*{p.get('title', '')}*](../../{p['_path']}) "
                f"`{p.get('citekey', '')}`"
            )
        lines.append("")
    return "\n".join(lines)


def replace_between(text: str, start: str, end: str, replacement: str) -> str:
    pattern = re.compile(
        re.escape(start) + r".*?" + re.escape(end),
        re.DOTALL,
    )
    new_block = f"{start}\n{replacement}\n{end}"
    if pattern.search(text):
        return pattern.sub(new_block, text)
    return text + "\n\n" + new_block + "\n"


def validate(projects: list[dict[str, Any]], papers: list[dict[str, Any]]) -> list[str]:
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
                f"{paper['_path']}: citekey '{ck}' missing from references.bib"
            )
        for rel in paper.get("relates_to_projects", []) or []:
            if rel not in slugs:
                errors.append(
                    f"{paper['_path']}: relates_to_projects '{rel}' not found"
                )

    return errors


def main() -> int:
    projects = load_projects()
    papers = load_papers()

    errors = validate(projects, papers)
    for e in errors:
        print(f"  WARN: {e}", file=sys.stderr)

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
        f"Projects indexed: {len(projects)}\n"
        f"Papers indexed:   {len(papers)}\n"
        f"Validation warnings: {len(errors)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
