---
name: data-analysis
description: End-to-end R data analysis pipeline — exploration → cleaning → regression → publication-ready tables and figures. Use when user says "analyze this dataset", "run a regression on X", "explore this CSV", "full analysis workflow", "get me summary stats and a regression", or points at a `.csv`/`.rds`/`.dta` and asks for empirical results. Produces numbered R scripts in `scripts/R/` and outputs to `output/`.
argument-hint: "[dataset path or description of analysis goal]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Agent", "Task", "Monitor"]
---

# Data Analysis Workflow

Run an end-to-end data analysis in R: load, explore, analyze, and produce publication-ready output.

**Input:** `$ARGUMENTS` — a dataset path (e.g., `data/county_panel.csv`) or a description of the analysis goal (e.g., "regress wages on education with state fixed effects using CPS data").

---

## Constraints

- **Follow R code conventions** in `.claude/rules/r-code-conventions.md`
- **Save all scripts** to `scripts/R/` with descriptive names
- **Save all outputs** (figures, tables, RDS) to `output/`
- **Use `saveRDS()`** for every computed object — Quarto slides may need them
- **Use project theme** for all figures (check for custom theme in `.claude/rules/`)
- **Run r-reviewer** on the generated script before presenting results

---

## Workflow Phases

### Phase 0: Pre-Flight Report

**Before writing any analysis code, produce a Pre-Flight Report** showing you read the inputs. This prevents the common failure mode where the agent hallucinates variable names or skips project conventions.

Output block (in your response to the user, before Phase 1):

```markdown
## Pre-Flight Report

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

### Phase 1: Setup and Data Loading

1. Create R script with proper header (title, author, purpose, inputs, outputs)
2. Load required packages at top (`library()`, never `require()`)
3. Set seed once at top in YYYYMMDD format (per `r-code-conventions.md`), e.g. `set.seed(20260415)` (INV-9)
4. Load and inspect the dataset

### Phase 2: Exploratory Data Analysis

Generate diagnostic outputs:
- **Summary statistics:** `summary()`, missingness rates, variable types
- **Distributions:** Histograms for key continuous variables
- **Relationships:** Scatter plots, correlation matrices
- **Time patterns:** If panel data, plot trends over time
- **Group comparisons:** If treatment/control, compare pre-treatment means

Save all diagnostic figures to `output/diagnostics/`.

### Phase 3: Main Analysis

Based on the research question:
- **Regression analysis:** Use `fixest` for panel data, `lm`/`glm` for cross-section
- **Standard errors:** Cluster at the appropriate level (document why)
- **Multiple specifications:** Start simple, progressively add controls
- **Effect sizes:** Report standardized effects alongside raw coefficients

#### Specification ledger — every run, kept or not

Every specification estimated in this phase, including the ones dropped and the ones that failed, gets one row appended to `quality_reports/spec-ledger.md` as it is run. It is the record a referee's "what else did you try?" deserves: it keeps the search visible rather than preventing it, and it records specifications without advising which to run.

- **Append only.** Never edit or delete a row; a correction is a new row. A commit that changes a committed row fails the repo-hygiene gate.
- **Status** is `kept`, `dropped` or `failed`; **Why** says why for anything not kept.
- **Estimate** is optional. On restricted data, leave it empty until the number has cleared disclosure review ([`confidential-data.md`](../../rules/confidential-data.md)).
- Escape a `|` inside a formula as `\|`, or the table breaks. A specification containing a backtick (a Stata local macro such as `` `x' ``) goes in a double-backtick span: ``` `` reg y `controls' `` ```.

```bash
LEDGER=quality_reports/spec-ledger.md
[ -f "$LEDGER" ] || printf '%s\n' "# Specification ledger" "" \
  "Every specification estimated, kept or not, one row each, appended as it is run. Never edit a past row; a correction is a new row." "" \
  "| Date | Commit | Script:line | Outcome | Specification | Sample | Status | Why | Estimate |" \
  "|---|---|---|---|---|---|---|---|---|" > "$LEDGER"
if REV=$(git rev-parse --short HEAD 2>/dev/null); then       # -dirty = anything uncommitted outside quality_reports/, untracked files included
  [ -n "$(git status --porcelain -- . ':(exclude)quality_reports' 2>/dev/null)" ] && REV="$REV-dirty"
else
  REV="no-commit"
fi
printf '| %s | %s ' "$(date +%F)" "$REV" >> "$LEDGER"          # one printf + one heredoc per specification
cat >> "$LEDGER" <<'EOF'
| scripts/R/03_analyze.R:42 | log_wage | `feols(log_wage ~ treat + age \| id + year, cluster = ~id)` | panel 2010-2019 | kept | main specification | 0.082 (0.021) |
EOF
```

### Phase 4: Publication-Ready Output

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

### Phase 5: Save and Review

1. `saveRDS()` for all key objects (regression results, summary tables, processed data)
2. Create `output/` subdirectories as needed with `dir.create(..., recursive = TRUE)`
3. Run the r-reviewer agent on the generated script:

```
Delegate to the r-reviewer agent:
"Review the script at scripts/R/[script_name].R"
```

4. Address any Critical or High issues from the review.

---

## Script Structure

Follow this template:

```r
# ============================================================
# [Descriptive Title]
# Author: [from project context]
# Purpose: [What this script does]
# Inputs: [Data files]
# Outputs: [Figures, tables, RDS files]
# ============================================================

# 0. Setup ----
library(tidyverse)
library(fixest)
library(modelsummary)

set.seed(20260415)  # YYYYMMDD per r-code-conventions.md (INV-9)

dir.create("output/analysis", recursive = TRUE, showWarnings = FALSE)

# 1. Data Loading ----
# [Load and clean data]

# 2. Exploratory Analysis ----
# [Summary stats, diagnostic plots]

# 3. Main Analysis ----
# [Regressions, estimation]

# 4. Tables and Figures ----
# [Publication-ready output]

# 5. Export ----
# [saveRDS for all objects, ggsave for all figures]
```

---

## Important

- **Reproduce, don't guess.** If the user specifies a regression, run exactly that.
- **Show your work.** Print summary statistics before jumping to regression.
- **Check for issues.** Look for multicollinearity, outliers, perfect prediction.
- **Use relative paths.** All paths relative to repository root.
- **No hardcoded values.** Use variables for sample restrictions, date ranges, etc.

## Long-running fits: use the Monitor tool (Apr 2026)

For regressions, simulations, or bootstrap loops that take more than a couple of minutes, launch via Bash with `run_in_background: true` and then use Anthropic's **Monitor tool** to stream R stdout into the conversation in real time. Pattern:

1. Background-launch with Bash `run_in_background: true`, sending all output to a log: `mkdir -p output && Rscript scripts/R/03_analyze.R > output/03_analyze.log 2>&1`. The background job notifies you by itself when the process exits.
2. Start Monitor with a command that follows that log and filters for milestones and failures, e.g. `tail -f output/03_analyze.log | grep --line-buffered -E "Coefficients table written|Error|Execution halted"`. Monitor has no job-id parameter: the stdout of its own `command` is the event stream. `tail -f` never exits, so set `timeout_ms` above the expected runtime (or `persistent: true`) and stop the monitor with TaskStop once the job finishes.
3. Continue or course-correct based on what the stream reveals.

This avoids the polling-loop anti-pattern (`sleep 30; check; sleep 30; check`) and avoids burning cache on idle waits. Especially useful when paired with the [Cost-Conscious Parallelism](https://psantanna.com/claude-code-my-workflow/workflow-guide.html#cost-conscious-parallelism) section of the guide.
