<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/build-paper.md -->

# `/build-paper`

Compiles the LaTeX paper to PDF through the pdflatex and bibtex cycle and lists common compilation failures.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-24</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/build-paper/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/build-paper/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/build-paper/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Build Paper Skill

Compile the paper from LaTeX source to PDF.

### Examples
- `/build-paper` -- full compile cycle for main.tex
- `/build-paper --quick` -- single pdflatex pass (faster, no bibliography update)
- `/build-paper path/to/file.tex` -- compile a specific file

### Workflow

#### Full Build (default)
1. Run pdflatex (first pass)
2. Run bibtex
3. Run pdflatex (second pass -- resolve references)
4. Run pdflatex (third pass -- finalize)
5. Check for errors/warnings
6. Report result

#### Quick Build (--quick)
1. Run single pdflatex pass
2. Report result

### Commands

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

### Output

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

### Common Issues
- **Undefined references**: Run full build (not quick)
- **Missing citations**: Check the `.bib` file has the key
- **Package errors**: Check `\usepackage` declarations
- **Font warnings**: Usually harmless (font substitution)
