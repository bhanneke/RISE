<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/stata-regression.md -->

# `stata-regression`

Run regression analyses in Stata with publication-ready output tables.

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
name: stata-regression
description: Run regression analyses in Stata with publication-ready output tables.
workflow_stage: analysis
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
author: Awesome Econ AI Community
version: 1.0.0
tags:
  - stata
  - regression
  - esttab
  - econometrics
---

# Stata Regression

## Purpose

This skill produces reproducible regression analysis workflows in Stata, including model diagnostics and publication-ready tables using `esttab` or `outreg2`.

## When to Use

- Estimating linear or nonlinear regression models in Stata
- Producing tables for academic papers and reports
- Running robustness checks and alternative specifications

## Instructions

Follow these steps to complete the task:

### Step 1: Understand the Context

Before generating any code, ask the user:

- What is the dependent variable and key regressors?
- What controls and fixed effects are required?
- How should standard errors be clustered?
- What output format is needed (LaTeX, Word, or CSV)?

### Step 2: Generate the Output

Based on the context, generate Stata code that:

1. **Loads and checks the data** - Handle missing values and verify variable types
2. **Runs the requested specification** - Use `regress`, `reghdfe`, or `xtreg` as appropriate
3. **Adds robust or clustered standard errors** - Match the study design
4. **Exports tables** - Use `esttab` or `outreg2` with clear labels

### Step 3: Verify and Explain

After generating output:

- Explain what each model estimates
- Highlight assumptions and diagnostics
- Suggest robustness checks or alternative models

## Example Prompts

- "Run OLS with firm and year fixed effects, clustering by firm"
- "Estimate a logit model and export results to LaTeX"
- "Create a regression table with three specifications"

## Example Output

```stata
* ============================================
* Regression Analysis with Stata
* ============================================

* Load data
use "data.dta", clear

* Summary stats
summarize y x1 x2 x3

* Main regression with clustered SEs
regress y x1 x2 x3, vce(cluster firm_id)
eststo model1

* Alternative specification with fixed effects
reghdfe y x1 x2 x3, absorb(firm_id year) vce(cluster firm_id)
eststo model2

* Export table
esttab model1 model2 using "results/regression_table.tex", replace se label
```

## Requirements

### Software

- Stata 17+

### Packages

- `estout` (for `esttab`)
- `reghdfe` (optional, for high-dimensional fixed effects)

Install with:

```stata
ssc install estout
ssc install reghdfe
```

## Best Practices

1. **Match standard errors to the design** (cluster where treatment varies)
2. **Report all model variants** used in the analysis
3. **Document variable definitions** and transformations

## Common Pitfalls

- Not clustering standard errors at the correct level
- Omitting fixed effects when required by the design
- Exporting tables without clear labels and notes

## References

- [Stata Regression Reference Manual](https://www.stata.com/manuals/rregress.pdf)
- [reghdfe documentation](https://github.com/sergiocorreia/reghdfe)
- [estout documentation](https://repec.sowi.unibe.ch/stata/estout/)

## Changelog

### v1.0.0

- Initial release


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/analysis/stata-regression/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>meleantonio/awesome-econ-ai-stuff</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../awesome-econ-ai-stuff.md">awesome-econ-ai-stuff (Antonio Mele)</a></dd>
<dt><b>Category</b></dt><dd><code>analysis</code></dd>
<dt><b>Field</b></dt><dd>econometrics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>data-analysis</code></dd>
<dt><b>License</b></dt><dd>Other (see repo)</dd>
<dt><b>Last update</b></dt><dd>2026</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff">⭐ meleantonio/awesome-econ-ai-stuff</a><br><img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/analysis/stata-regression/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/stata-regression/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
