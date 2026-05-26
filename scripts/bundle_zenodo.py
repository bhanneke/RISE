"""Build a Zenodo-ready release bundle of the RISE knowledge base.

Produces dist/rise-knowledge-base-v<VERSION>.zip containing:
  - README_BUNDLE.md         # what's in this bundle, how to cite
  - CITATION.cff             # citation metadata
  - LICENSE                  # CC-BY-4.0
  - papers/references.bib    # 35+ BibTeX entries
  - papers/schema.md         # note schema
  - papers/notes/            # 33 paper notes (markdown)
  - papers/pdfs/             # OA PDFs fetched by fetch_pdfs.py (if present)
  - projects/                # 37 project YAML entries + EVALUATION.md + VOCABULARY.md
  - docs/concept/            # 7 concept pages (definition, history, etc.)
  - docs/assets/rise-pipeline.svg

Run:
    python scripts/fetch_pdfs.py        # first, populate papers/pdfs/
    python scripts/bundle_zenodo.py     # then bundle

Output: dist/rise-knowledge-base-v<VERSION>.zip
"""

from __future__ import annotations

import argparse
import shutil
import zipfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"

DEFAULT_VERSION = f"0.2.0-{date.today().isoformat()}"

INCLUDE = [
    ("README_BUNDLE.md",        "_README_BUNDLE_GENERATED.md"),   # generated below
    ("CITATION.cff",            "CITATION.cff"),
    ("LICENSE",                 "LICENSE"),
    ("papers/",                 "papers/"),         # references.bib + schema.md + pdfs/
    ("docs/papers/notes/",      "papers/notes/"),   # the structured markdown notes
    ("projects/",               "projects/"),       # entire directory
    ("skills/",                 "skills/"),         # NEW: skill packs + SKILL.md text
    ("docs/concept/",           "docs/concept/"),
    ("docs/assets/",            "docs/assets/"),
]


def build_readme(version: str) -> str:
    npapers = len(list((ROOT / "docs" / "papers" / "notes").glob("*.md")))
    nproj = len(list((ROOT / "projects").glob("*.yml"))) + len(
        list((ROOT / "projects" / "landscape").glob("*.yml"))
    )
    pdfs_dir = ROOT / "papers" / "pdfs"
    npdfs = len(list(pdfs_dir.glob("*.pdf"))) if pdfs_dir.exists() else 0
    return f"""# RISE Knowledge Base — Zenodo bundle (v{version})

A snapshot of the **Research Information Systems Engineering** knowledge base
maintained at <https://github.com/bhanneke/RISE>.

## What's in this bundle

| Component | Count |
|---|---|
| Project entries (YAML + rubric scores) | {nproj} |
| Academic paper notes (markdown) | {npapers} |
| Open-access paper PDFs (fetched via arXiv / AISeL / NBER / Unpaywall) | {npdfs} |
| Concept pages | 7 |
| Evaluation rubric + vocabulary | 2 documents |
| Graphical abstract (SVG) | 1 |

## Top-level structure

```
papers/
├── references.bib          BibTeX database (canonical citations)
├── schema.md               note format
├── notes/                  one structured markdown note per paper
└── pdfs/                   open-access PDFs (where retrievable)

projects/
├── EVALUATION.md           11-dimension rubric (v0.2)
├── VOCABULARY.md           controlled tags (themes, stages, features, focus)
├── schema.md               project entry format
├── e2er.yml                owned project
└── landscape/              external systems evaluated against the rubric

docs/
├── concept/                7 conceptual pages introducing RISE
└── assets/rise-pipeline.svg   graphical abstract
```

## How to cite

See `CITATION.cff` for canonical citation. Suggested attribution:

> Hanneke, Björn (2026). *RISE: Research Information Systems Engineering — a
> curated knowledge base of papers and projects.* Version {version}.
> Zenodo. [DOI to be minted].

## Reproducibility note

PDF coverage is **open-access only**. Paywalled papers (typically EJIS,
PNAS, ISR, MISQ, Organization Science articles, and SSRN deposits behind
download walls) appear in `papers/references.bib` and `papers/notes/` but
not in `papers/pdfs/`. The `FETCH_LOG.csv` records which sources were
attempted and why each missing PDF failed.

## License

Content: **CC-BY-4.0** (see LICENSE). Third-party paper PDFs in
`papers/pdfs/` retain their original licenses — most are author-deposited
preprints (arXiv, AISeL, NBER) reproduced under their respective terms.
The bundling under CC-BY does not relicense them.
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--version", default=DEFAULT_VERSION)
    args = ap.parse_args()

    DIST.mkdir(parents=True, exist_ok=True)
    out = DIST / f"rise-knowledge-base-v{args.version}.zip"

    # Write generated README into a temp file so it can be added to the zip
    tmp_readme = DIST / "_README_BUNDLE_GENERATED.md"
    tmp_readme.write_text(build_readme(args.version), encoding="utf-8")

    n_files = 0
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for src, arc in INCLUDE:
            src_path = ROOT / src if not src.startswith("README_BUNDLE") else tmp_readme
            if not src_path.exists():
                print(f"  skip (missing): {src}")
                continue
            if src_path.is_file():
                zf.write(src_path, arcname=arc if not arc.startswith("_") else "README_BUNDLE.md")
                n_files += 1
            else:
                for f in src_path.rglob("*"):
                    if f.is_file():
                        if any(part.startswith(".") for part in f.relative_to(ROOT).parts):
                            continue
                        rel = f.relative_to(ROOT)
                        zf.write(f, arcname=str(rel))
                        n_files += 1

    tmp_readme.unlink(missing_ok=True)
    size_mb = out.stat().st_size / 1_000_000
    print(f"\n=== Bundle written ===")
    print(f"  Path:  {out.relative_to(ROOT)}")
    print(f"  Files: {n_files}")
    print(f"  Size:  {size_mb:.2f} MB")
    print()
    print("Next steps for Zenodo:")
    print("  1. Go to https://zenodo.org/uploads/new")
    print("  2. Drag-drop the .zip from the dist/ folder")
    print("  3. Fill in metadata (title, authors, keywords) — see CITATION.cff")
    print("  4. (Optional) link to GitHub repo for automatic future releases")


if __name__ == "__main__":
    main()
