<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-visual-formatting.md -->

# `visual-formatting`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

# Visual Formatting Review

## Purpose

This skill describes how to compile a LaTeX draft to PDF and visually inspect
the rendered output for formatting and typesetting issues that are invisible
in the source code. The goal is to catch problems before the paper reaches
Overleaf or a human reviewer.

---

## LaTeX Compilation Sequence

Always compile in this order to resolve all cross-references:

```
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

If compilation fails, capture the `.log` file and report the error. Common
causes:

| Error pattern | Likely cause | Fix |
|---|---|---|
| `Undefined control sequence` | Missing package or typo in command | Add `\usepackage{...}` or fix the command |
| `Missing $ inserted` | Math mode content outside `$...$` | Wrap in math mode |
| `File ... not found` | Missing figure or input file | Check path, provide placeholder |
| `Too many unprocessed floats` | Float queue overflow | Add `\clearpage` or use `[H]` placement |
| `Mismatched braces` | Unbalanced `{` / `}` | Count braces carefully, especially in `\renewcommand` |
| `Missing \begin{document}` | Preamble error before `\begin{document}` | Check for syntax errors in preamble |

---

## Page-by-Page Inspection Checklist

For each rendered page, check:

### Layout & Margins
- Text stays within margins (no overfull hbox warnings visible as text running into the margin)
- Consistent margins on all pages
- Page numbers present and correctly placed

### Tables
- Tables fit within page width (no column overflow)
- Table captions are present and correctly placed (above for tables)
- Column alignment is readable
- No tables split awkwardly across pages

### Figures
- Figures are placed near their first reference in the text
- Figure captions are present and correctly placed (below for figures)
- Figures are legible at the rendered size
- No figures pushed to end of document

### Headings & Text Flow
- No orphaned section headings at page bottom (heading with no body text following)
- No widows (single line of a paragraph at top of page)
- No orphans (single line of a paragraph at bottom of page)
- Section numbering is correct and sequential
- No excessive whitespace between sections

### Cross-References & Citations
- All `\ref{}` and `\eqref{}` references resolve (no "??" in output)
- All `\cite{}` references resolve (no "[?]" in output)
- Table and figure numbers match their references in text

### Typography
- No overfull hbox warnings visible (text extending past margins)
- Consistent font usage throughout
- Equations are properly typeset and numbered
- Em-dashes, en-dashes, and hyphens used correctly

---

## Severity Classification

- **Critical**: Compilation failure, broken cross-references ("??"), tables/figures
  extending past page boundaries, missing sections
- **Major**: Orphaned headings, figures placed far from reference, significant
  whitespace gaps, table formatting that impairs readability
- **Minor**: Slight float placement preferences, minor whitespace inconsistencies,
  font size variations in tables

---

## Common LaTeX Fixes

| Problem | Fix |
|---|---|
| Table too wide | `\resizebox{\textwidth}{!}{...}` or `\begin{adjustbox}{max width=\textwidth}` |
| Orphaned heading | `\needspace{4\baselineskip}` before `\section{}` |
| Figure placement | Use `[htbp]` specifiers; add `\usepackage{float}` for `[H]` |
| Overfull hbox | `\sloppy` locally, or rewrite the paragraph |
| Unresolved reference | Recompile (may need 2nd pass) or check `\label` exists |
| Float queue overflow | `\clearpage` at strategic points |
| Bad page break | `\pagebreak` or `\nopagebreak` hints |


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/review/visual-formatting.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>review</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/review-visual-formatting/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
