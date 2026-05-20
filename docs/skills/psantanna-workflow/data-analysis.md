<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/data-analysis.md -->

# `/data-analysis`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/data-analysis/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/data-analysis/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/data-analysis/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Data Analysis Workflow

Run an end-to-end data analysis in R: load, explore, analyze, and produce publication-ready output.

**Input:** `$ARGUMENTS` — a dataset path (e.g., `data/county_panel.csv`) or a description of the analysis goal (e.g., "regress wages on education with state fixed effects using CPS data").

---

### Constraints

- **Follow R code conventions** in `.claude/rules/r-code-conventions.md`
- **Save all scripts** to `scripts/R/` with descriptive names
- **Save all outputs** (figures, tables, RDS) to `output/`
- **Use `saveRDS()`** for every computed object — Quarto slides may need them
- **Use project theme** for all figures (check for custom theme in `.claude/rules/`)
- **Run r-reviewer** on the generated script before presenting results

---

### Workflow Phases

#### Phase 0: Pre-Flight Report

**Before writing any analysis code, produce a Pre-Flight Report** showing you read the inputs. This prevents the common failure mode where the agent hallucinates variable names or skips project conventions.

Output block (in your response to the user, before Phase 1):

```markdown
### Pre-Flight Report

**Dataset:** [path]
- Variables found: [list from head()/names()]
- Rows: [count]
- Key types: [e.g., "outcome=numeric, treatment=binary, state=factor"]
- Missing-data summary: [% missing per key var]

**Project conventions read:**
- `.claude/rules/r-code-conventions.md` — [one-line summary of most relevant rule]
- `.claude/rules/content-invariants.md` — [INV-9, INV-10, INV-11, INV-12 applicable]

**Task interpretation:** [one sentence restating what the user asked for]

**Plan:** [3-5 bullet outline of the R script structure]
```

If any input cannot be read (missing file, unreadable format), stop and ask the user before proceeding.

#### Phase 1: Setup and Data Loading

1. Create R script with proper header (title, author, purpose, inputs, outputs)
2. Load required packages at top (`library()`, never `require()`)
3. Set seed once at top in YYYYMMDD format (per `r-code-conventions.md`), e.g. `set.seed(20260415)` (INV-9)
4. Load and inspect the dataset

#### Phase 2: Exploratory Data Analysis

Generate diagnostic outputs:
- **Summary statistics:** `summary()`, missingness rates, variable types
- **Distributions:** Histograms for key continuous variables
- **Relationships:** Scatter plots, correlation matrices
- **Time patterns:** If panel data, plot trends over time
- **Group comparisons:** If treatment/control, compare pre-treatment means

Save all diagnostic figures to `output/diagnostics/`.

#### Phase 3: Main Analysis

Based on the research question:
- **Regression analysis:** Use `fixest` for panel data, `lm`/`glm` for cross-section
- **Standard errors:** Cluster at the appropriate level (document why)
- **Multiple specifications:** Start simple, progressively add controls
- **Effect sizes:** Report standardized effects alongside raw coefficients

#### Phase 4: Publication-Ready Output

**Tables:**
- Use `modelsummary` for regression tables (preferred) or `stargazer`
- Include all standard elements: coefficients, SEs, significance stars, N, R-squared
- Export as `.tex` for LaTeX inclusion and `.html` for quick viewing

**Figures:**
- Use `ggplot2` with project theme
- Set `bg = "transparent"` for Beamer compatibility
- Include proper axis labels (sentence case, units)
- Export with explicit dimensions: `ggsave(width = X, height = Y)`
- Save as both `.pdf` and `.png`

#### Phase 5: Save and Review

1. `saveRDS()` for all key objects (regression results, summary tables, processed data)
2. Create `output/` subdirectories as needed with `dir.create(..., recursive = TRUE)`
3. Run the r-reviewer agent on the generated script:

```
Delegate to the r-reviewer agent:
"Review the script at scripts/R/[script_name].R"
```

4. Address any Critical or High issues from the review.

---

### Script Structure

Follow this template:

```r
## ============================================================
## [Descriptive Title]
## Author: [from project context]
## Purpose: [What this script does]
## Inputs: [Data files]
## Outputs: [Figures, tables, RDS files]
## ============================================================

## 0. Setup ----
library(tidyverse)
library(fixest)
library(modelsummary)

set.seed(20260415)  # YYYYMMDD per r-code-conventions.md (INV-9)

dir.create("output/analysis", recursive = TRUE, showWarnings = FALSE)

## 1. Data Loading ----
## [Load and clean data]

## 2. Exploratory Analysis ----
## [Summary stats, diagnostic plots]

## 3. Main Analysis ----
## [Regressions, estimation]

## 4. Tables and Figures ----
## [Publication-ready output]

## 5. Export ----
## [saveRDS for all objects, ggsave for all figures]
```

---

### Important

- **Reproduce, don't guess.** If the user specifies a regression, run exactly that.
- **Show your work.** Print summary statistics before jumping to regression.
- **Check for issues.** Look for multicollinearity, outliers, perfect prediction.
- **Use relative paths.** All paths relative to repository root.
- **No hardcoded values.** Use variables for sample restrictions, date ranges, etc.

### Long-running fits: use the Monitor tool (Apr 2026)

For regressions, simulations, or bootstrap loops that take more than a couple of minutes, launch via Bash with `run_in_background: true` and then use Anthropic's **Monitor tool** to stream R stdout into the conversation in real time. Pattern:

1. Background-launch: `Rscript scripts/R/03_analyze.R` with `run_in_background: true`. Capture the `bash_id`.
2. Use Monitor on the `bash_id` until a milestone fires (e.g., `Coefficients table written`, or process exit).
3. Continue or course-correct based on what the stream reveals.

This avoids the polling-loop anti-pattern (`sleep 30; check; sleep 30; check`) and avoids burning cache on idle waits. Especially useful when paired with the [Cost-Conscious Parallelism](https://psantanna.com/claude-code-my-workflow/workflow-guide.html#cost-conscious-parallelism) section of the guide.
