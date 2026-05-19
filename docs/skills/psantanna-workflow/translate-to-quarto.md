<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/translate-to-quarto.md -->

# `/translate-to-quarto`



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
name: translate-to-quarto
description: Translate a Beamer `.tex` lecture to a Quarto RevealJS `.qmd` mirror. Multi-phase: TikZ extraction → slide-by-slide translation → citation conversion → automatic QA parity check. Use when user says "translate to quarto", "port to revealjs", "make an html version", "convert this beamer to quarto", "mirror this lecture in qmd", or after a Beamer deck is ready for web publication. Output lands in `Quarto/`.
argument-hint: "[LectureN_Topic.tex]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task"]
context: fork
---

# Beamer → Quarto Translation Workflow

Full translation of a Beamer LaTeX lecture to Quarto RevealJS HTML slides.

**CRITICAL: The Beamer .tex file is the SINGLE SOURCE OF TRUTH.**

---

## Phase 0: Pre-Flight Checks

### 0A. Environment Parity Audit
Scan Beamer for all custom environments. Verify CSS equivalents exist in your theme SCSS. If any are missing, create them FIRST.

### 0B. TikZ Freshness Verification
Run `/extract-tikz` to verify SVGs match current Beamer source.

### 0C. RDS Data Inventory
List all RDS files needed for interactive charts.

### 0D. Citation Key Mapping
Extract all citations from Beamer, map to bibliography keys.

## Phase 1: Pre-Translation Preparation
- Read complete Beamer source, count frames
- Inventory figures (TikZ → SVG, R plots → plotly, other → SVG)

## Phase 2: Create QMD File with YAML Header
- Standard RevealJS YAML with theme, logo, footer, bibliography
- Setup chunk for R data loading if needed

## Phase 3: Slide-by-Slide Translation
- Delegate to `beamer-translator` agent
- 1:1 frame-to-slide mapping
- Verbatim math, environment parity, no font reduction

## Phase 4: TikZ Diagram Integration
Reference extracted SVGs with 0-based indexing.

## Phase 5: R Figure Integration (Plotly-First)
Interactive plotly from RDS data, static SVG for TikZ/complex figures.

## Phase 6: First Render & Content Fidelity Check
Render, count slides, go through EVERY slide checking for issues.

## Phase 6.5: Pedagogical Review
Run pedagogy-reviewer before visual polish.

## Phase 7: Visual Polish
Semantic colors, transition slides, framing sentences.

## Phase 8: Proofreading
Run `/proofread` on the QMD file.

## Phase 9: Final Verification & Deployment
Render, open in browser, verify all elements.

## Phase 10: Beamer Source Sync
Apply any corrections back to Beamer source.

## Phase 11: Documentation
Update CLAUDE.md, session log, create PR.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/translate-to-quarto/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/translate-to-quarto/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/translate-to-quarto/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
