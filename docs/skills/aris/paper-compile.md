<!-- DO NOT EDIT — auto-copied from skills/aris/details/paper-compile.md -->

# `paper-compile`



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

---
name: paper-compile
description: "Compile LaTeX paper to PDF, fix errors, and verify output. Use when user says \"编译论文\", \"compile paper\", \"build PDF\", \"生成PDF\", or wants to compile LaTeX into a submission-ready PDF."
argument-hint: [paper-directory]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob
---

# Paper Compile: LaTeX to Submission-Ready PDF

Compile the LaTeX paper and fix any issues: **$ARGUMENTS**

## Constants

- **COMPILER = `latexmk`** — LaTeX build tool. Handles multi-pass compilation automatically.
- **ENGINE = `pdflatex`** — LaTeX engine. Options: `pdflatex` (default), `xelatex` (for CJK/custom fonts), `lualatex`.
- **MAX_COMPILE_ATTEMPTS = 3** — Maximum attempts to fix errors and recompile.
- **PAPER_DIR = `paper/`** — Directory containing LaTeX source files.
- **MAX_PAGES** — Page limit. ML conferences: main body to Conclusion end (excluding references & appendix). ICLR=9, NeurIPS=9, ICML=8. **IEEE venues: references ARE included in page count.** IEEE journal ≈ 12-14 pages, IEEE conference ≈ 5-8 pages (all inclusive).

## Workflow

### Step 1: Verify Prerequisites

Check that the compilation environment is ready:

```bash
# Check LaTeX installation
which pdflatex && which latexmk && which bibtex

# If not installed, provide instructions:
# macOS: brew install --cask mactex-no-gui
# Ubuntu: sudo apt-get install texlive-full
# Server: conda install -c conda-forge texlive-core
```

Verify all required files exist:

```bash
# Must exist
ls $PAPER_DIR/main.tex

# Should exist
ls $PAPER_DIR/references.bib
ls $PAPER_DIR/sections/*.tex
ls $PAPER_DIR/figures/*.pdf 2>/dev/null || ls $PAPER_DIR/figures/*.png 2>/dev/null
```

### Step 2: First Compilation Attempt

```bash
cd $PAPER_DIR

# Clean previous build artifacts
latexmk -C

# Full compilation (pdflatex + bibtex + pdflatex × 2)
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee compile.log
```

### Step 3: Error Diagnosis and Auto-Fix

If compilation fails, read `compile.log` and fix common errors:

**Missing packages:**
```
! LaTeX Error: File `somepackage.sty' not found.
```
→ Install via `tlmgr install somepackage` or remove the `\usepackage` if unused.

**Undefined references:**
```
LaTeX Warning: Reference `fig:xyz' on page 3 undefined
```
→ Check `\label{fig:xyz}` exists in the correct figure environment.

**Missing figures:**
```
! LaTeX Error: File `figures/fig1.pdf' not found.
```
→ Check if the file exists with a different extension (.png vs .pdf). Update the `\includegraphics` path.

**Citation undefined:**
```
LaTeX Warning: Citation `smith2024' undefined
```
→ Add the missing entry to `references.bib` or fix the citation key.

**`[VERIFY]` markers in text:**
→ Search for `[VERIFY]` markers left by `/paper-write`. These indicate unverified citations or facts. Search for the correct information or flag to the user.

**Overfull hbox:**
```
Overfull \hbox (12.5pt too wide) in paragraph at lines 42--45
```
→ Minor: usually ignorable. If severe (>20pt), rephrase the text or adjust figure width.

**BibTeX errors:**
```
I was expecting a `,' or a `}'---line 15 of references.bib
```
→ Fix BibTeX syntax (missing comma, unmatched braces, special characters in title).

**`\crefname` undefined for custom theorem types:**
→ Ensure `\crefname{assumption}{Assumption}{Assumptions}` and similar are in the preamble after `\newtheorem{assumption}`.

### Step 4: Iterative Fix Loop

```
for attempt in 1..MAX_COMPILE_ATTEMPTS:
    compile()
    if success:
        break
    parse_errors()
    auto_fix()
```

For each error:
1. Read the error message from `compile.log`
2. Locate the source file and line number
3. Apply the fix
4. Recompile

**Stuck after 2 attempts?** If Codex plugin is installed, invoke `/codex:rescue` — Codex can independently read the LaTeX source and `compile.log` to spot issues Claude missed (e.g., conflicting packages, encoding problems, subtle macro errors). If not installed, continue with Claude's own diagnosis.

### Step 5: Post-Compilation Checks

After successful compilation, verify the output:

```bash
# Check PDF exists and has content
ls -la main.pdf
# Check page count
pdfinfo main.pdf | grep Pages

# macOS: open for visual inspection
# open main.pdf
```

**Visual review (automated):**
If the compiled PDF exists, read it directly to check visual presentation:
- Figure quality: readable labels, legible text, distinguishable colors
- Layout: no orphaned section headers, no awkward page breaks
- Figures appear near their first text reference (not pages away)
- Tables: aligned columns, consistent decimal precision
- No overfull content visibly extending past margins

This is a quick visual scan, not a full review — the improvement loop does deeper visual review.

**Automated checks:**

- [ ] PDF file exists and is > 100KB (not empty/corrupt)
- [ ] Total page count is reasonable (MAX_PAGES + appendix + references)
- [ ] No "??" in the PDF (undefined references — grep the log)
- [ ] No "[?]" in the PDF (undefined citations — grep the log)
- [ ] Figures are rendered (not missing image placeholders)

```bash
# Check for undefined references
grep -c "LaTeX Warning.*undefined" compile.log

# Check for missing citations
grep -c "Citation.*undefined" compile.log
```

### Step 6: Page Count Verification

**CRITICAL**: Verify paper fits within MAX_PAGES.

**For ML conferences (ICLR/NeurIPS/ICML/CVPR/ACL/AAAI):** Main body = first page through end of Conclusion section (not necessarily §5 — could be §6, §7, or §8 depending on structure). References and appendix are NOT counted.

**For IEEE venues:** The TOTAL page count (including references) must fit within the limit. There is no separate "main body" counting — everything up to and including the references counts.

**Precise check using `pdftotext`:**
```bash
# Extract text and find where Conclusion ends vs References begin
pdftotext main.pdf - | python3 -c "
import sys
text = sys.stdin.read()
pages = text.split('\f')
for i, page in enumerate(pages):
    if 'Ethics Statement' in page or 'Reproducibility' in page:
        print(f'Conclusion ends on page {i+1}')
    if any(w in page for w in ['References', 'Bibliography']):
        lines = [l for l in page.split('\n') if l.strip()]
        for l in lines[:3]:
            if 'References' in l or 'Bibliography' in l:
                print(f'References start on page {i+1}')
                break
"
```

If Conclusion ends mid-page and References start on the same page, the main body is that page number (e.g., if both are on page 9, main body = ~8.5 pages, which is fine for a 9-page limit since it leaves room for the References header).

If over limit:
- Identify which sections are longest
- Suggest specific cuts (move proofs to appendix, compress tables, tighten writing)
- Report: "Main body is X pages (limit: MAX_PAGES). Suggestion: move [specific content] to appendix."

### Step 6.5: Stale File Detection

Check for orphaned section files not referenced by `main.tex`:

```bash
# Find all .tex files in sections/ and check which are \input'ed by main.tex
for f in paper/sections/*.tex; do
    base=$(basename "$f")
    if ! grep -q "$base" paper/main.tex; then
        echo "WARNING: $f is not referenced by main.tex — consider removing"
    fi
done
```

This prevents confusion from leftover files when section structure changes (e.g., old `5_conclusion.tex` left behind after restructuring to 7 sections).

### Step 7: Submission Readiness

For conference submission, additional checks:

- [ ] **Anonymous**: no author names, affiliations, or self-citations that reveal identity
- [ ] **Page limit**: main body within MAX_PAGES (to end of Conclusion)
- [ ] **Font embedding**: all fonts embedded in PDF
  ```bash
  pdffonts main.pdf | grep -v "yes"  # should return nothing (or only header)
  ```
- [ ] **No supplementary mixed in**: appendix clearly after `\newpage\appendix`
- [ ] **File size**: reasonable (< 50MB for most venues, < 10MB preferred)
- [ ] **No `[VERIFY]` markers**: search the PDF text for leftover markers

### Step 8: Output Summary

```markdown
## Compilation Report

- **Status**: SUCCESS / FAILED
- **PDF**: paper/main.pdf
- **Pages**: X (main body to Conclusion) + Y (references) + Z (appendix)
- **Within page limit**: YES/NO (MAX_PAGES = N)
- **Errors fixed**: [list of auto-fixed issues]
- **Warnings remaining**: [list of non-critical warnings]
- **Undefined references**: 0
- **Undefined citations**: 0

### Next Steps
- [ ] Visual inspection of PDF
- [ ] Run `/paper-write` to fix any content issues
- [ ] Submit to [venue] via OpenReview / CMT / HotCRP
```

## Key Rules

- **Never delete the user's source files** — only modify to fix errors
- **Keep compile.log** — useful for debugging
- **Don't suppress warnings** — report them, let the user decide
- **If LaTeX is not installed**, provide clear installation instructions rather than failing silently
- **Font embedding is critical** — some venues reject PDFs with non-embedded fonts
- **Page count rules differ by venue** — ML conferences: main body to Conclusion (refs excluded). **IEEE venues: total pages including references.**

## Common Venue Requirements

| Venue | Style File | Citation | Page Limit | Refs in limit? | Submission |
|-------|-----------|----------|------------|----------------|------------|
| ICLR 2026 | `iclr2026_conference.sty` | `natbib` (`\citep`/`\citet`) | 9 pages (to Conclusion end) | No | OpenReview |
| NeurIPS 2025 | `neurips_2025.sty` | `natbib` (`\citep`/`\citet`) | 9 pages (to Conclusion end) | No | OpenReview |
| ICML 2025 | `icml2025.sty` | `natbib` (`\citep`/`\citet`) | 8 pages (to Conclusion end) | No | OpenReview |
| IEEE Journal | `IEEEtran.cls` [journal] | `cite` (`\cite{}`, numeric) | ~12-14 pages (Transactions) / ~4-5 (Letters) | **Yes** | IEEE Author Portal / ScholarOne |
| IEEE Conference | `IEEEtran.cls` [conference] | `cite` (`\cite{}`, numeric) | 5-8 pages (varies by conf) | **Yes** | EDAS / IEEE Author Portal |


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/paper-compile/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/paper-compile/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
