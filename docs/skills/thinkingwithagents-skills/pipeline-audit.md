<!-- DO NOT EDIT — auto-copied from skills/thinkingwithagents-skills/details/pipeline-audit.md -->

# `/pipeline-audit`

Adversarial audit of a data pipeline that checks variable construction, sample restrictions and analytical choices against the pre-analysis plan and grades findings as red, orange or yellow flags.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../thinkingwithagents-skills/">Thinking with Agents econ skills (Emily Beam and Erkmen Aslim)</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>CC-BY-4.0 (repo LICENSE, "Creative Commons Attribution 4.0 International, Copyright (c) 2026 Emily Beam")</code></div><div><b>Updated:</b> 2026-04-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code> · <code>replication</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/thinkingwithagents/skills/contents/pipeline-audit/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/thinkingwithagents-skills/pipeline-audit/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/thinkingwithagents/skills/blob/main/pipeline-audit/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/thinkingwithagents/skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Pipeline Audit — Adversarial Data Review

*v1.0 — Adversarial reviewer that challenges data pipeline outputs, assumptions, and integrity. Complements /code-review (which reviews code quality) by testing what the code actually produced.*

Review the outputs of a data cleaning or analysis pipeline by reading the data, checking for anomalies, and challenging the assumptions embedded in the pipeline. This is the "red team" for your data work.

**Argument:** `$ARGUMENTS`
- Path to a directory containing .dta output files (e.g., `data/for_analysis/`)
- Or a project name (will look in `~/Dropbox/Github/[project]/`)
- Or a specific .dta file to audit

**Modes** (append to argument):
- `quick` (default) — Scan outputs for red flags: duplicate IDs, unexpected missingness, implausible values
- `deep` — Full adversarial review: all quick checks + cross-file consistency, merge integrity, distribution analysis
- `pre-submission` — Publication-readiness check: all deep checks + AEA-style output verification, table-to-code tracing

**Flags:**
- `scope:cleaning` — Focus on cleaning pipeline outputs (raw -> for_analysis)
- `scope:analysis` — Focus on analysis outputs (regressions, tables)
- `vars:consumption,assets` — Focus on specific variable families
- `baseline:path/to/old.dta` — Compare against a previous version

Example: `/pipeline-audit ~/Dropbox/Github/graduation-coaching/data/for_analysis/ deep`
Example: `/pipeline-audit data/for_analysis/endline_analysis.dta quick vars:consumption`
Example: `/pipeline-audit bd-social scope:cleaning`

---

### Instructions

#### Step 0: Locate Data and Context

1. Resolve `$ARGUMENTS` to find the target .dta file(s):
   - If a directory: glob for `*.dta` files, report count
   - If a project name: check `~/Dropbox/Github/[project]/data/for_analysis/`, `data/`, `output/`
   - If a single file: use directly
2. Read the project's `AGENTS.md`, `CLAUDE.md`, or `README.md` if available — look for:
   - Expected unique identifiers (hhid, id, respondent_id)
   - Expected sample sizes
   - Variable naming conventions
   - Known data quality issues
3. If a `docs/` or `codebook/` directory exists, scan for data documentation

Parse mode and flags from `$ARGUMENTS`. Default to `quick`.

---

#### Step 1: Structural Integrity

Write a temporary Python script for all checks (use `uv run python` or `python3`). Never use `python -c`.

For each .dta file:

#### 1.1 ID Integrity
- Detect likely ID columns (hhid, id, respondent_id, or columns ending in `_id`)
- Test uniqueness: `df[id_col].is_unique`
- Report any duplicates with sample rows
- If multiple .dta files share an ID column, verify consistent ID sets across files

#### 1.2 Shape and Completeness
- Report: rows, columns, memory usage
- Flag files with 0 rows (empty output = pipeline failure)
- Flag files where >50% of columns are entirely missing
- Flag any column that is 100% missing

#### 1.3 Variable Type Audit
- Count: numeric, string, categorical columns
- Flag columns where the name suggests numeric but the type is string (e.g., `income_total` as string)
- Flag columns where >90% of values are the same (constant or near-constant)

---

#### Step 2: Value Plausibility (all modes)

#### 2.1 Distributional Red Flags
For each numeric column:
- Flag if min < 0 for variables that should be non-negative (expenditure, count, age, income)
- Flag extreme outliers: values > 10x the 99th percentile or < -10x the 1st percentile
- Flag suspiciously round distributions (all values multiples of 100, 1000, etc.)
- Report top 5 columns by coefficient of variation (most dispersed)

#### 2.2 Missing Value Patterns
- Report overall missingness rate per column
- Flag columns where missingness is suspiciously correlated with treatment/control (if treatment variable detected)
- Flag columns where missingness jumps sharply compared to nearby columns in the dataset
- Check for sentinel codes that survived cleaning (-99, -88, -77, -66 in numeric columns)

#### 2.3 Categorical/Indicator Checks
- For binary (0/1) columns: report balance. Flag if <1% or >99% are 1 (degenerate)
- For categorical columns: report number of unique values. Flag if >100 unique values (may be continuous stored as categorical)
- Check value labels exist for categorical variables (via pyreadstat metadata)

---

#### Step 3: Cross-File Consistency (deep and pre-submission modes)

*Skip for `quick` mode.*

#### 3.1 ID Coverage
- If multiple .dta files share an ID column:
  - Are the ID sets identical? Report any IDs present in one file but not another
  - Do key structural variables (treatment arm, strata, demographics) match across files?

#### 3.2 Variable Consistency
- If the same variable name appears in multiple files:
  - Do the distributions match? (Compare means, SDs, ranges)
  - Flag any where the mean differs by >10%

#### 3.3 Merge Residue
- Flag any `_merge` variables that survived into the output (should be dropped)
- Flag any variables named `_*` that look like temporary leftovers

---

#### Step 4: Assumption Challenges (deep and pre-submission modes)

*Skip for `quick` mode.*

This is the adversarial core. Challenge the pipeline's implicit assumptions:

#### 4.1 Sample Selection Bias
- If treatment variable exists: compare sample sizes by arm. Flag imbalance >10%
- Check if missingness patterns differ by treatment arm for key outcomes
- If attrition variable exists: profile attriters vs non-attriters on baseline characteristics

#### 4.2 Construction Validity
- For index/composite variables: check correlation with components. Flag if a component has near-zero correlation with the composite (may not belong)
- For per-capita variables: verify denominator is reasonable (household size > 0, not missing)
- For currency-converted variables: verify conversion factor is plausible (not 0, not extreme)

#### 4.3 Winsorization / Trimming
- Detect winsorized variables (names containing `wins`, `_w`, `_tr`)
- Verify winsorization was applied (compare min/max to percentile boundaries)
- Flag if winsorization thresholds seem too aggressive (>5% each tail)

#### 4.4 Time / Date Variables
- Check date variables for future dates (data entry errors)
- Check for dates outside the study period
- Flag if interview date range is implausibly short or long

---

#### Step 5: Analysis Output Checks (pre-submission mode only)

*Skip for `quick` and `deep` modes.*

#### 5.1 Regression Output Tables
- If results .dta or .csv files exist, check:
  - Do coefficient signs match economic intuition? (Treatment effects positive for graduation programs)
  - Are standard errors plausible relative to coefficient size?
  - Are sample sizes consistent across specifications?
  - Do R-squared values seem reasonable for the model type?

#### 5.2 Table-to-Data Traceability
- For each regression output: can we identify which .dta was the input?
- Are all outcome variables in the output traceable to a column in the analysis dataset?

---

#### Step 6: Generate Report

**Save report to:**
- Same directory as reviewed data: `pipeline_audit_[YYYY-MM-DD].md`
- Or project root if reviewing a project

**Classify each finding:**
- **RED FLAG** — Data integrity violation. Likely pipeline bug or data corruption. Investigate immediately.
- **ORANGE FLAG** — Suspicious pattern that may indicate a problem. Verify before proceeding.
- **YELLOW FLAG** — Unusual but potentially intentional. Document the decision if keeping.
- **CLEAN** — Passed the check.

---

### Output Format

```markdown
## Pipeline Audit: [project/directory]

**Date:** [YYYY-MM-DD]
**Mode:** [quick / deep / pre-submission]
**Files reviewed:** [N] .dta files ([total rows] observations, [total cols] variables)
**Reviewer:** /pipeline-audit v1.0

---

### Executive Summary

**Overall assessment:** [Clean / Minor Issues / Investigate / Significant Problems]

[2-3 sentences: what was checked, what was found, what needs attention]

**Red flags:** [N]  |  **Orange flags:** [N]  |  **Yellow flags:** [N]  |  **Clean checks:** [N]

---

### Red Flags

#### RF1: [Title]
- **File:** [filename]
- **Issue:** [description]
- **Evidence:** [specific values, counts, or statistics]
- **Action:** [what to investigate or fix]

---

### Orange Flags

#### OF1: [Title]
- **File:** [filename]
- **Issue:** [description]
- **Evidence:** [evidence]
- **Question:** [what to verify — phrased as a question for the PI]

---

### Yellow Flags

[Brief list format]
- **YF1:** [file] — [issue] — [why it might be OK]

---

### Clean Checks

| Check | Status | Notes |
|-------|--------|-------|
| ID uniqueness | PASS | [N] files, all unique on [hhid] |
| No empty files | PASS | All [N] files have data |
| No sentinel codes | PASS | No -99/-88/-77 in numeric columns |
| ... | ... | ... |

---

### File Inventory

| File | Rows | Cols | ID Column | Missing Rate | Notes |
|------|------|------|-----------|-------------|-------|
| [name] | [N] | [N] | [col] | [%] | [any flags] |

---

### Next Steps

1. [Highest-priority investigation]
2. [Second priority]
3. [Third priority]
```

---

### Principles

- **Adversarial, not adversary.** The goal is to find problems before reviewers, referees, or replicators do. Every flag is an opportunity to strengthen the work.
- **Evidence-based.** Every finding includes specific numbers, rows, or statistics. "Something looks wrong" is not a finding.
- **Calibrated severity.** A duplicate ID is a red flag. An unusual distribution is a yellow flag. Don't cry wolf.
- **Ask, don't assume.** When a pattern is ambiguous, phrase the finding as a question for the PI: "Is it expected that 23% of treated households have missing consumption data?"
- **Respect the pipeline.** The cleaning code may have already handled an issue. Check the code/logs before flagging something the pipeline explicitly addresses.
- **No false comfort.** A clean audit doesn't mean the data is perfect — it means the checks you ran didn't find problems. State what you checked and what you didn't.
