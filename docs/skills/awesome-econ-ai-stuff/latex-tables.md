<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/latex-tables.md -->

# `latex-tables`

Generate publication-ready regression tables in LaTeX.

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
name: latex-tables
description: Generate publication-ready regression tables in LaTeX.
workflow_stage: writing
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
author: Awesome Econ AI Community
version: 1.0.0
tags:
  - latex
  - tables
  - regression
  - booktabs
---

# LaTeX Tables

## Purpose

This skill creates clean, publication-ready tables in LaTeX for regression results and summary statistics, using standard academic formatting.

## When to Use

- Converting model output into LaTeX tables
- Standardizing table style across a paper
- Adding notes, significance stars, and labels

## Instructions

Follow these steps to complete the task:

### Step 1: Understand the Context

Before generating any code, ask the user:

- What type of table is needed (regression, summary stats, balance)?
- What software produced the results (Stata, R, Python)?
- Which formatting style is required (journal-specific, AEA, etc.)?

### Step 2: Generate the Output

Based on the context, generate LaTeX code that:

1. **Uses `booktabs`** for clean horizontal rules
2. **Includes labels and captions** for referencing in the paper
3. **Adds notes** for standard errors and significance
4. **Aligns numeric columns** for readability

### Step 3: Verify and Explain

After generating output:

- Explain how to compile the table
- Highlight any assumptions in the formatting
- Suggest refinements for journal submission

## Example Prompts

- "Create a regression table with three models in LaTeX"
- "Format summary statistics with mean and sd columns"
- "Add significance stars and standard error notes"

## Example Output

```latex
% ============================================
% Regression Table
% ============================================
\begin{table}[htbp]\centering
\caption{Effect of Treatment on Outcome}
\label{tab:main_results}
\begin{tabular}{lccc}
\toprule
 & (1) & (2) & (3) \\
\midrule
Treatment & 0.125*** & 0.118*** & 0.102** \\
 & (0.041) & (0.039) & (0.046) \\
Controls & No & Yes & Yes \\
Fixed Effects & No & Yes & Yes \\
\midrule
Observations & 2,145 & 2,145 & 2,145 \\
R-squared & 0.18 & 0.24 & 0.31 \\
\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item Notes: Standard errors in parentheses. * p<0.10, ** p<0.05, *** p<0.01.
\end{tablenotes}
\end{table}
```

## Requirements

### Software

- LaTeX distribution (TeX Live or MikTeX)

### Packages

- `booktabs`
- `threeparttable` (optional for notes)

## Best Practices

1. **Keep tables compact** and readable
2. **Use consistent notation** for standard errors and stars
3. **Provide clear captions and labels**

## Common Pitfalls

- Overly wide tables that do not fit the page
- Missing notes for standard errors
- Inconsistent labeling across tables

## References

- [LaTeX booktabs documentation](https://ctan.org/pkg/booktabs)
- [AEA Author Guidelines](https://www.aeaweb.org/journals/policies/author-instructions)

## Changelog

### v1.0.0

- Initial release


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/writing/latex-tables/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>meleantonio/awesome-econ-ai-stuff</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../awesome-econ-ai-stuff.md">awesome-econ-ai-stuff (Antonio Mele)</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>Other (see repo)</dd>
<dt><b>Last update</b></dt><dd>2026</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff">⭐ meleantonio/awesome-econ-ai-stuff</a><br><img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/writing/latex-tables/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/latex-tables/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
