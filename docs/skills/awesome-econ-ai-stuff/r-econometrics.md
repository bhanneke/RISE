<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/r-econometrics.md -->

# `r-econometrics`

Run IV, DiD, and RDD analyses in R with proper diagnostics.

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
name: r-econometrics
description: Run IV, DiD, and RDD analyses in R with proper diagnostics
workflow_stage: analysis
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
author: Awesome Econ AI Community
version: 1.0.0
tags:
  - R
  - econometrics
  - causal-inference
  - fixest
  - regression
---

# R Econometrics

## Purpose

This skill helps economists run rigorous econometric analyses in R, including Instrumental Variables (IV), Difference-in-Differences (DiD), and Regression Discontinuity Design (RDD). It generates publication-ready code with proper diagnostics and robust standard errors.

## When to Use

- Running causal inference analyses
- Estimating treatment effects with panel data
- Creating publication-ready regression tables
- Implementing modern econometric methods (two-way fixed effects, event studies)

## Instructions

### Step 1: Understand the Research Design

Before generating code, ask the user:
1. What is your identification strategy? (IV, DiD, RDD, or simple regression)
2. What is the unit of observation? (individual, firm, country-year, etc.)
3. What fixed effects do you need? (entity, time, two-way)
4. How should standard errors be clustered?

### Step 2: Generate Analysis Code

Based on the research design, generate R code that:

1. **Uses the `fixest` package** - Modern, fast, and feature-rich for panel data
2. **Includes proper diagnostics:**
   - For IV: First-stage F-statistics, weak instrument tests
   - For DiD: Parallel trends visualization, event study plots
   - For RDD: Bandwidth selection, density tests
3. **Uses robust/clustered standard errors** appropriate for the data structure
4. **Creates publication-ready output** using `modelsummary` or `etable`

### Step 3: Structure the Output

Always include:
```r
# 1. Setup and packages
# 2. Data loading and preparation
# 3. Descriptive statistics
# 4. Main specification
# 5. Robustness checks
# 6. Visualization
# 7. Export results
```

### Step 4: Add Documentation

Include comments explaining:
- Why each specification choice was made
- Interpretation of key coefficients
- Limitations and assumptions

## Example Prompts

- "Run a DiD analysis with state and year fixed effects, clustering at the state level"
- "Estimate the effect of X on Y using Z as an instrument"
- "Create an event study plot showing treatment effects by year"
- "Run a sharp RDD with optimal bandwidth selection"

## Example Output

```r
# ============================================
# Difference-in-Differences Analysis
# ============================================

# Setup
library(tidyverse)
library(fixest)
library(modelsummary)

# Load data
df <- read_csv("data.csv")

# Prepare treatment variable
df <- df %>%
  mutate(
    post = year >= treatment_year,
    treated = state %in% treatment_states,
    treat_post = treated * post
  )

# ----------------------------------------
# Main DiD Specification
# ----------------------------------------

# Two-way fixed effects
did_model <- feols(
  outcome ~ treat_post | state + year,
  data = df,
  cluster = ~state
)

# View results
summary(did_model)

# ----------------------------------------
# Event Study
# ----------------------------------------

# Create relative time variable
df <- df %>%
  mutate(rel_time = year - treatment_year)

# Event study regression
event_study <- feols(
  outcome ~ i(rel_time, treated, ref = -1) | state + year,
  data = df,
  cluster = ~state
)

# Plot coefficients
iplot(event_study, 
      main = "Event Study: Effect on Outcome",
      xlab = "Years Relative to Treatment")

# ----------------------------------------
# Robustness: Alternative Specifications
# ----------------------------------------

# Different clustering
did_robust <- feols(
  outcome ~ treat_post | state + year,
  data = df,
  cluster = ~state + year  # Two-way clustering
)

# ----------------------------------------
# Export Results
# ----------------------------------------

modelsummary(
  list("Main" = did_model, "Two-way Cluster" = did_robust),
  stars = c('*' = 0.1, '**' = 0.05, '***' = 0.01),
  output = "results/did_table.tex"
)
```

## Requirements

### Software
- R 4.0+

### Packages
- `fixest` - Fast fixed effects estimation
- `modelsummary` - Publication-ready tables
- `tidyverse` - Data manipulation
- `ggplot2` - Visualization

Install with:
```r
install.packages(c("fixest", "modelsummary", "tidyverse"))
```

## Best Practices

1. **Always cluster standard errors** at the level of treatment assignment
2. **Run pre-trend tests** for DiD designs
3. **Report first-stage F-statistics** for IV (should be > 10)
4. **Use `feols` over `lm`** for panel data (faster and more features)
5. **Document all specification choices** in your code comments

## Common Pitfalls

- ❌ Not clustering standard errors at the right level
- ❌ Ignoring weak instruments in IV estimation
- ❌ Using TWFE with staggered treatment timing (use `did` or `sunab()` instead)
- ❌ Not reporting robustness checks

## References

- [fixest documentation](https://lrberge.github.io/fixest/)
- [Cunningham (2021) Causal Inference: The Mixtape](https://mixtape.scunning.com/)
- [Angrist & Pischke (2009) Mostly Harmless Econometrics](https://www.mostlyharmlesseconometrics.com/)

## Changelog

### v1.0.0
- Initial release with IV, DiD, RDD support


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/analysis/r-econometrics/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/analysis/r-econometrics/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/r-econometrics/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
