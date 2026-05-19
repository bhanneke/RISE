<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/extract-tikz.md -->

# `/extract-tikz`



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
name: extract-tikz
description: Extract TikZ diagrams from Beamer `.tex` source, compile each to a standalone PDF, and convert to SVG with 0-based indexing. Use when user says "extract the tikz", "regenerate the diagrams", "rebuild the SVGs", "sync tikz to quarto", or after editing TikZ blocks in a Beamer deck that also has a Quarto mirror.
argument-hint: "[LectureN, e.g., Lecture2]"
allowed-tools: ["Read", "Bash", "Glob", "Task"]
---

# Extract TikZ Diagrams to SVG

Extract TikZ diagrams from the Beamer source, compile to multi-page PDF, and convert each page to SVG for use in Quarto slides.

> **Creating a brand-new diagram instead of extracting?** Use [`/new-diagram`](../new-diagram/SKILL.md) — it scaffolds from `templates/tikz-snippets/` with the prevention rules pre-applied.

## Steps

### Step 0: Freshness Check (MANDATORY)

**Before compiling, verify that `extract_tikz.tex` matches the current Beamer source.**

1. Find the Beamer source: `ls Slides/$ARGUMENTS*.tex`
2. Extract all `\begin{tikzpicture}` blocks from Beamer
3. Compare with `Figures/$ARGUMENTS/extract_tikz.tex`
4. If ANY difference exists: update extract_tikz.tex from the Beamer source
5. If extract_tikz.tex doesn't exist: create it from scratch

### Step 1: Prevention pre-check (MANDATORY — halt on violation)

Before compiling, verify every `\begin{tikzpicture}` block in `Figures/$ARGUMENTS/extract_tikz.tex` satisfies the prevention rules in [`.claude/rules/tikz-prevention.md`](../../rules/tikz-prevention.md). The pre-check is a small Python script shared with `/new-diagram` so both skills enforce identical behavior:

```bash
python3 scripts/check-tikz-prevention.py "Figures/$ARGUMENTS/extract_tikz.tex"
```

What it checks:

- **P3 — `scale=X` without node scaling.** Bare `scale=` shrinks coordinates but not text. Allowed forms: `scale=X, every node/.style={scale=X}` or `scale=X, transform shape`. The checker parses the full `\begin{tikzpicture}[...]` options block even when it spans multiple lines.
- **P4 — Directional keyword on edge labels.** Every edge label (`node` inside a `\draw`) must carry `above`, `below`, `left`, `right`, or a compound (e.g. `above left`). `midway` alone is a path position, not a direction. The checker scans the full `\draw ...;` statement so `\draw` on one line and `node[...]{...}` on the next line are still linked.

Note what the pre-check does NOT enforce: P1 (boxed-node explicit dimensions) and P2 (coordinate-map comment) are structural and get flagged by `tikz-reviewer` in Step 8, not here.

Exit codes: `0` = all files pass, `1` = one or more P3/P4 violations (stderr lists file, line, snippet, rule), `2` = usage error.

If exit is non-zero: halt, report the offending lines, and ask the user to fix the Beamer source (single source of truth). Do NOT compile.

### Step 2: Navigate to the lecture's Figures directory
```bash
cd Figures/$ARGUMENTS
```

### Step 3: Compile the extract_tikz.tex file
```bash
TEXINPUTS=../../Preambles:$TEXINPUTS xelatex -interaction=nonstopmode extract_tikz.tex
```

### Step 4: Count the number of pages
```bash
pdfinfo extract_tikz.pdf | grep "Pages:"
```

### Step 5: Convert each page to SVG using 0-BASED INDEXING

**CRITICAL: PDF pages are 1-indexed, but output SVG files are 0-indexed!**

```bash
PAGES=$(pdfinfo extract_tikz.pdf | grep "Pages:" | awk '{print $2}')
for i in $(seq 1 $PAGES); do
  idx=$(printf "%02d" $((i-1)))
  pdf2svg extract_tikz.pdf tikz_exact_$idx.svg $i
done
```

### Step 6: Sync to docs/ for deployment
```bash
cd ../..
./scripts/sync_to_docs.sh $ARGUMENTS
```

### Step 7: Verify SVG files
- Read 2-3 SVG files to confirm they contain valid SVG markup
- Confirm file sizes are reasonable (not 0 bytes)

### Step 8: Visual Quality Review (tikz-reviewer)

Spawn the **tikz-reviewer** agent (via `Task` with `subagent_type=tikz-reviewer`) on the TikZ source blocks to catch label overlaps, geometric errors, and visual inconsistencies. The reviewer cites specific passes and formulas from [`.claude/rules/tikz-measurement.md`](../../rules/tikz-measurement.md). If it returns **NEEDS REVISION** or **REJECTED**, loop:

1. Apply the recommended fixes to the Beamer `.tex` source (single source of truth).
2. Re-copy the updated block to `extract_tikz.tex`.
3. Re-run the prevention pre-check (Step 1) and compile.
4. Regenerate SVGs, re-sync.
5. Re-invoke tikz-reviewer.

Stop when tikz-reviewer returns **APPROVED** (max 5 rounds).

### Step 9: Report results

## Source of Truth Reminder
TikZ diagrams MUST be edited in the Beamer `.tex` file first, then copied verbatim to `extract_tikz.tex`. See `.claude/rules/single-source-of-truth.md`.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/extract-tikz/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>figures</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/extract-tikz/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/extract-tikz/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
