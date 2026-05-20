<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/r-econometrics.md -->

# `r-econometrics`

Run IV, DiD, and RDD analyses in R with proper diagnostics.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> econometrics</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/analysis/r-econometrics/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/r-econometrics/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/analysis/r-econometrics/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## R Econometrics

### Purpose

This skill helps economists run rigorous econometric analyses in R, including Instrumental Variables (IV), Difference-in-Differences (DiD), and Regression Discontinuity Design (RDD). It generates publication-ready code with proper diagnostics and robust standard errors.

### When to Use

- Running causal inference analyses
- Estimating treatment effects with panel data
- Creating publication-ready regression tables
- Implementing modern econometric methods (two-way fixed effects, event studies)

### Instructions

#### Step 1: Understand the Research Design

Before generating code, ask the user:
1. What is your identification strategy? (IV, DiD, RDD, or simple regression)
2. What is the unit of observation? (individual, firm, country-year, etc.)
3. What fixed effects do you need? (entity, time, two-way)
4. How should standard errors be clustered?

#### Step 2: Generate Analysis Code

Based on the research design, generate R code that:

1. **Uses the `fixest` package** - Modern, fast, and feature-rich for panel data
2. **Includes proper diagnostics:**
   - For IV: First-stage F-statistics, weak instrument tests
   - For DiD: Parallel trends visualization, event study plots
   - For RDD: Bandwidth selection, density tests
3. **Uses robust/clustered standard errors** appropriate for the data structure
4. **Creates publication-ready output** using `modelsummary` or `etable`

#### Step 3: Structure the Output

Always include:
```r
## 1. Setup and packages
## 2. Data loading and preparation
## 3. Descriptive statistics
## 4. Main specification
## 5. Robustness checks
## 6. Visualization
## 7. Export results
```

#### Step 4: Add Documentation

Include comments explaining:
- Why each specification choice was made
- Interpretation of key coefficients
- Limitations and assumptions

### Example Prompts

- "Run a DiD analysis with state and year fixed effects, clustering at the state level"
- "Estimate the effect of X on Y using Z as an instrument"
- "Create an event study plot showing treatment effects by year"
- "Run a sharp RDD with optimal bandwidth selection"

### Example Output

```r
## ============================================
## Difference-in-Differences Analysis
## ============================================

## Setup
library(tidyverse)
library(fixest)
library(modelsummary)

## Load data
df <- read_csv("data.csv")

## Prepare treatment variable
df <- df %>%
  mutate(
    post = year >= treatment_year,
    treated = state %in% treatment_states,
    treat_post = treated * post
  )

## ----------------------------------------
## Main DiD Specification
## ----------------------------------------

## Two-way fixed effects
did_model <- feols(
  outcome ~ treat_post | state + year,
  data = df,
  cluster = ~state
)

## View results
summary(did_model)

## ----------------------------------------
## Event Study
## ----------------------------------------

## Create relative time variable
df <- df %>%
  mutate(rel_time = year - treatment_year)

## Event study regression
event_study <- feols(
  outcome ~ i(rel_time, treated, ref = -1) | state + year,
  data = df,
  cluster = ~state
)

## Plot coefficients
iplot(event_study, 
      main = "Event Study: Effect on Outcome",
      xlab = "Years Relative to Treatment")

## ----------------------------------------
## Robustness: Alternative Specifications
## ----------------------------------------

## Different clustering
did_robust <- feols(
  outcome ~ treat_post | state + year,
  data = df,
  cluster = ~state + year  # Two-way clustering
)

## ----------------------------------------
## Export Results
## ----------------------------------------

modelsummary(
  list("Main" = did_model, "Two-way Cluster" = did_robust),
  stars = c('*' = 0.1, '**' = 0.05, '***' = 0.01),
  output = "results/did_table.tex"
)
```

### Requirements

#### Software
- R 4.0+

#### Packages
- `fixest` - Fast fixed effects estimation
- `modelsummary` - Publication-ready tables
- `tidyverse` - Data manipulation
- `ggplot2` - Visualization

Install with:
```r
install.packages(c("fixest", "modelsummary", "tidyverse"))
```

### Best Practices

1. **Always cluster standard errors** at the level of treatment assignment
2. **Run pre-trend tests** for DiD designs
3. **Report first-stage F-statistics** for IV (should be > 10)
4. **Use `feols` over `lm`** for panel data (faster and more features)
5. **Document all specification choices** in your code comments

### Common Pitfalls

- ❌ Not clustering standard errors at the right level
- ❌ Ignoring weak instruments in IV estimation
- ❌ Using TWFE with staggered treatment timing (use `did` or `sunab()` instead)
- ❌ Not reporting robustness checks

### References

- [fixest documentation](https://lrberge.github.io/fixest/)
- [Cunningham (2021) Causal Inference: The Mixtape](https://mixtape.scunning.com/)
- [Angrist & Pischke (2009) Mostly Harmless Econometrics](https://www.mostlyharmlesseconometrics.com/)

### Changelog

#### v1.0.0
- Initial release with IV, DiD, RDD support
