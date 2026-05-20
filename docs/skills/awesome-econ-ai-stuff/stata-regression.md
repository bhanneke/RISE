<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/stata-regression.md -->

# `stata-regression`

Run regression analyses in Stata with publication-ready output tables.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> econometrics</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/analysis/stata-regression/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/stata-regression/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/analysis/stata-regression/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Stata Regression

### Purpose

This skill produces reproducible regression analysis workflows in Stata, including model diagnostics and publication-ready tables using `esttab` or `outreg2`.

### When to Use

- Estimating linear or nonlinear regression models in Stata
- Producing tables for academic papers and reports
- Running robustness checks and alternative specifications

### Instructions

Follow these steps to complete the task:

#### Step 1: Understand the Context

Before generating any code, ask the user:

- What is the dependent variable and key regressors?
- What controls and fixed effects are required?
- How should standard errors be clustered?
- What output format is needed (LaTeX, Word, or CSV)?

#### Step 2: Generate the Output

Based on the context, generate Stata code that:

1. **Loads and checks the data** - Handle missing values and verify variable types
2. **Runs the requested specification** - Use `regress`, `reghdfe`, or `xtreg` as appropriate
3. **Adds robust or clustered standard errors** - Match the study design
4. **Exports tables** - Use `esttab` or `outreg2` with clear labels

#### Step 3: Verify and Explain

After generating output:

- Explain what each model estimates
- Highlight assumptions and diagnostics
- Suggest robustness checks or alternative models

### Example Prompts

- "Run OLS with firm and year fixed effects, clustering by firm"
- "Estimate a logit model and export results to LaTeX"
- "Create a regression table with three specifications"

### Example Output

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

### Requirements

#### Software

- Stata 17+

#### Packages

- `estout` (for `esttab`)
- `reghdfe` (optional, for high-dimensional fixed effects)

Install with:

```stata
ssc install estout
ssc install reghdfe
```

### Best Practices

1. **Match standard errors to the design** (cluster where treatment varies)
2. **Report all model variants** used in the analysis
3. **Document variable definitions** and transformations

### Common Pitfalls

- Not clustering standard errors at the correct level
- Omitting fixed effects when required by the design
- Exporting tables without clear labels and notes

### References

- [Stata Regression Reference Manual](https://www.stata.com/manuals/rregress.pdf)
- [reghdfe documentation](https://github.com/sergiocorreia/reghdfe)
- [estout documentation](https://repec.sowi.unibe.ch/stata/estout/)

### Changelog

#### v1.0.0

- Initial release
