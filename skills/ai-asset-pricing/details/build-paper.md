---
name: build-paper
description: Compile LaTeX to PDF using pdflatex + bibtex cycle
---

# Build Paper Skill

Compile the paper from LaTeX source to PDF.

## Examples
- `/build-paper` -- full compile cycle for main.tex
- `/build-paper --quick` -- single pdflatex pass (faster, no bibliography update)
- `/build-paper path/to/file.tex` -- compile a specific file

## Workflow

### Full Build (default)
1. Run pdflatex (first pass)
2. Run bibtex
3. Run pdflatex (second pass -- resolve references)
4. Run pdflatex (third pass -- finalize)
5. Check for errors/warnings
6. Report result

### Quick Build (--quick)
1. Run single pdflatex pass
2. Report result

## Commands

Use the pdflatex and bibtex paths from canonical local state reported by `tools/bootstrap.py audit` (or a repo-root `CLAUDE.local.md` compatibility shim if present). The general pattern:

**Full build:**
```bash
cd {latex_dir} && pdflatex -interaction=nonstopmode {file} && bibtex {stem} && pdflatex -interaction=nonstopmode {file} && pdflatex -interaction=nonstopmode {file}
```

**Quick build:**
```bash
cd {latex_dir} && pdflatex -interaction=nonstopmode {file}
```

**IMPORTANT**: Always `cd` to the directory containing the `.tex` file before compiling.

## Output

```
BUILD REPORT
============

Status: SUCCESS / FAILED
Warnings: N
Errors: N

[list of warnings if any]
[list of errors if any]

Output: {latex_dir}/{stem}.pdf
```

## Common Issues
- **Undefined references**: Run full build (not quick)
- **Missing citations**: Check the `.bib` file has the key
- **Package errors**: Check `\usepackage` declarations
- **Font warnings**: Usually harmless (font substitution)
