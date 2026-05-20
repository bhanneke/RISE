<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/python-panel-data.md -->

# `python-panel-data`

Panel data analysis with Python using linearmodels and pandas.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> econometrics</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/analysis/python-panel-data/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/python-panel-data/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/analysis/python-panel-data/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Python Panel Data

### Purpose

This skill helps economists run panel data models in Python using `pandas`, `statsmodels`, and `linearmodels`, with correct fixed effects, clustering, and diagnostics.

### When to Use

- Estimating fixed effects or random effects models
- Running difference-in-differences on panel data
- Creating regression tables and plots in Python

### Instructions

Follow these steps to complete the task:

#### Step 1: Understand the Context

Before generating any code, ask the user:

- What is the unit of observation and panel identifiers?
- Which outcomes and regressors are required?
- What fixed effects or time effects are needed?
- How should standard errors be clustered?

#### Step 2: Generate the Output

Based on the context, generate Python code that:

1. **Loads and cleans the data** with `pandas`
2. **Sets a MultiIndex** for panel structure
3. **Fits the model** using `linearmodels.PanelOLS` or `RandomEffects`
4. **Outputs results** in a readable table and optional LaTeX

#### Step 3: Verify and Explain

After generating output:

- Interpret key coefficients
- Note assumptions (strict exogeneity, parallel trends, etc.)
- Suggest robustness checks (alternative clustering, placebo tests)

### Example Prompts

- "Run a two-way fixed effects model with firm and year effects"
- "Estimate a DiD using state and year fixed effects"
- "Export panel regression results to LaTeX"

### Example Output

```python
## ============================================
## Panel Data Analysis in Python
## ============================================
import pandas as pd
from linearmodels.panel import PanelOLS

## Load data
df = pd.read_csv("panel_data.csv")

## Set panel index
df = df.set_index(["firm_id", "year"])

## Create treatment indicator
df["treat_post"] = df["treated"] * df["post"]

## Two-way fixed effects model
model = PanelOLS.from_formula(
    "outcome ~ 1 + treat_post + EntityEffects + TimeEffects",
    data=df
)
results = model.fit(cov_type="clustered", cluster_entity=True)

print(results.summary)
```

### Requirements

#### Software

- Python 3.10+

#### Packages

- `pandas`
- `linearmodels`
- `statsmodels`

Install with:

```bash
pip install pandas linearmodels statsmodels
```

### Best Practices

1. **Always verify panel identifiers** and balanced vs unbalanced panels
2. **Cluster standard errors** at the appropriate level
3. **Check for missing data** before estimation

### Common Pitfalls

- Failing to set a proper panel index
- Using pooled OLS when fixed effects are required
- Misinterpreting coefficients without accounting for fixed effects

### References

- [linearmodels documentation](https://bashtage.github.io/linearmodels/)
- [statsmodels documentation](https://www.statsmodels.org/)
- [Wooldridge (2010) Econometric Analysis of Cross Section and Panel Data](https://mitpress.mit.edu/9780262232586/)

### Changelog

#### v1.0.0

- Initial release
