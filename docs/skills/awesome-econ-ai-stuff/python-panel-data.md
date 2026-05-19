<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/python-panel-data.md -->

# `python-panel-data`

Panel data analysis with Python using linearmodels and pandas.

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
name: python-panel-data
description: Panel data analysis with Python using linearmodels and pandas.
workflow_stage: analysis
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
author: Awesome Econ AI Community
version: 1.0.0
tags:
  - python
  - pandas
  - linearmodels
  - panel-data
---

# Python Panel Data

## Purpose

This skill helps economists run panel data models in Python using `pandas`, `statsmodels`, and `linearmodels`, with correct fixed effects, clustering, and diagnostics.

## When to Use

- Estimating fixed effects or random effects models
- Running difference-in-differences on panel data
- Creating regression tables and plots in Python

## Instructions

Follow these steps to complete the task:

### Step 1: Understand the Context

Before generating any code, ask the user:

- What is the unit of observation and panel identifiers?
- Which outcomes and regressors are required?
- What fixed effects or time effects are needed?
- How should standard errors be clustered?

### Step 2: Generate the Output

Based on the context, generate Python code that:

1. **Loads and cleans the data** with `pandas`
2. **Sets a MultiIndex** for panel structure
3. **Fits the model** using `linearmodels.PanelOLS` or `RandomEffects`
4. **Outputs results** in a readable table and optional LaTeX

### Step 3: Verify and Explain

After generating output:

- Interpret key coefficients
- Note assumptions (strict exogeneity, parallel trends, etc.)
- Suggest robustness checks (alternative clustering, placebo tests)

## Example Prompts

- "Run a two-way fixed effects model with firm and year effects"
- "Estimate a DiD using state and year fixed effects"
- "Export panel regression results to LaTeX"

## Example Output

```python
# ============================================
# Panel Data Analysis in Python
# ============================================
import pandas as pd
from linearmodels.panel import PanelOLS

# Load data
df = pd.read_csv("panel_data.csv")

# Set panel index
df = df.set_index(["firm_id", "year"])

# Create treatment indicator
df["treat_post"] = df["treated"] * df["post"]

# Two-way fixed effects model
model = PanelOLS.from_formula(
    "outcome ~ 1 + treat_post + EntityEffects + TimeEffects",
    data=df
)
results = model.fit(cov_type="clustered", cluster_entity=True)

print(results.summary)
```

## Requirements

### Software

- Python 3.10+

### Packages

- `pandas`
- `linearmodels`
- `statsmodels`

Install with:

```bash
pip install pandas linearmodels statsmodels
```

## Best Practices

1. **Always verify panel identifiers** and balanced vs unbalanced panels
2. **Cluster standard errors** at the appropriate level
3. **Check for missing data** before estimation

## Common Pitfalls

- Failing to set a proper panel index
- Using pooled OLS when fixed effects are required
- Misinterpreting coefficients without accounting for fixed effects

## References

- [linearmodels documentation](https://bashtage.github.io/linearmodels/)
- [statsmodels documentation](https://www.statsmodels.org/)
- [Wooldridge (2010) Econometric Analysis of Cross Section and Panel Data](https://mitpress.mit.edu/9780262232586/)

## Changelog

### v1.0.0

- Initial release


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/analysis/python-panel-data/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/analysis/python-panel-data/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/python-panel-data/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
