---
name: code-review
description: Structured code review for research code (Stata, R, Python) against DIME, Gentzkow-Shapiro, AEA, and IPA standards — catches silent failures, reproducibility risks, and style issues
---

# Code Review

*v1.0 — Structured code review for research code, drawing on DIME, Gentzkow-Shapiro, AEA, and IPA standards*

Review research code (Stata, R, or Python) against economics-specific quality standards. Catches silent failures, reproducibility risks, and style issues that generic linters miss.

**Argument:** `$ARGUMENTS`
- Path to a file (`.do`, `.R`, `.py`) or a directory
- Or a project name (will look in `~/Dropbox/Github/[project]/`)

**Modes** (append to argument):
- `quick` (default) — Single-file review: correctness, reproducibility risks, style
- `full` — Deep single-file review with project context (reads master do-file, config, related files)
- `pipeline` — Multi-file review: trace the full analysis pipeline, check dependencies and flow
- `replication` — AEA replication package audit (README, data citations, reproducibility, completeness)

**Flags:**
- `fix` — Also output a corrected version of the file (otherwise review-only)
- `severity:high` — Only report high-severity issues (skip style nitpicks)

Example: `/code-review ~/Dropbox/Github/graduation-coaching/code/dofiles/01_clean.do`
Example: `/code-review graduation-coaching pipeline`
Example: `/code-review my_analysis.do full fix`

---

## Instructions

### Step 0: Locate and Read the Code

1. If `$ARGUMENTS` contains a file path, read that file directly
2. If `$ARGUMENTS` is a project name, check these locations in order:
   - `~/Dropbox/Github/[project]/code/`
   - `~/Dropbox/Github/[project]/analysis/`
   - `~/Dropbox/Github/[project]/dofiles/`
   - Glob for `*.do`, `*.R`, `*.py` in the project repo
3. If a directory is given:
   - For `quick` or `full`: review each code file individually
   - For `pipeline`: trace the execution order from the master file
   - For `replication`: review the full package structure
4. Detect language from file extension: `.do` = Stata, `.R`/`.r` = R, `.py` = Python

If multiple files found and no mode specified, list them and ask which to review.

For `full` and `pipeline` modes, also read:
- Master do-file / main script (look for `master*.do`, `main*.do`, `run*.do`, `00_*.do`)
- Config file (look for `config*.do`, `profile.do`, `globals.do`, `paths.do`)
- Project's `CLAUDE.md` or `README.md` if available
- Project's HUB.md in eb-lab if available

Parse the mode from `$ARGUMENTS`. Default to `quick` if not specified.

---

### Step 1: Correctness Checks

Review the code for errors that could produce wrong results silently. These are the most important findings.

#### 1.1 Stata-Specific Correctness
- **Merge diagnostics**: Every `merge` must be followed by `assert _merge == 3` or explicit handling of `_merge` values (tabulate, keep/drop). Flag any merge without `_merge` inspection.
- **Sort stability**: `sort` in Stata is not stable. Flag any `sort` followed by operations that depend on row order (e.g., `gen id = _n`, `by ... : gen x = x[_n-1]`). Recommend `isid` checks or `sort ..., stable`.
- **Dropped observations**: Flag any `drop if` or `keep if` without a preceding or following count/assertion. The reviewer should verify the number of dropped obs is expected.
- **Missing values in comparisons**: In Stata, missing values are greater than any number. Flag `if x > threshold` without `& !missing(x)`. Flag `drop if x > threshold` especially.
- **String/numeric mismatch**: Flag comparisons between string and numeric variables (e.g., merge keys where one side is string, the other numeric).
- **Preserve/restore**: Every `preserve` must have a matching `restore`. Flag unmatched pairs.
- **Temporary files**: `tempfile` and `tempvar` usage — flag any that are created but never used, or used after `clear`.
- **Collapse without saving**: Flag `collapse` without a preceding `preserve` or `save/tempfile` — the original data is destroyed.
- **Destring/tostring issues**: Flag `destring, force` without checking what was forced to missing.
- **Factor variable traps**: Flag regressions using `i.` on variables with many levels without checking for singletons or collinearity.

#### 1.2 R-Specific Correctness
- **Unhandled NAs**: Operations on vectors with NAs without `na.rm = TRUE` or explicit `filter(!is.na(...))`.
- **Left joins dropping data**: Flag `left_join` without checking for unexpected row count changes.
- **Factor level issues**: Implicit factor ordering in regressions.
- **Package conflicts**: Multiple packages loaded that mask each other's functions (e.g., `dplyr::filter` vs `stats::filter`).

#### 1.3 Python-Specific Correctness
- **Pandas merge issues**: `pd.merge` without `validate=` parameter. Missing `how=` specification.
- **Silent type coercion**: Operations that silently convert types (e.g., int to float due to NaN).
- **Index alignment**: Operations on DataFrames with misaligned indices.

#### 1.4 Cross-Language Correctness
- **Hardcoded values**: Magic numbers without explanation (e.g., `drop if age > 65` — is 65 the right cutoff?).
- **Commented-out code that affects results**: Large blocks of commented-out analysis that suggest the code was modified and may not reflect the intended specification.
- **Off-by-one errors**: Loop bounds, date ranges, age cutoffs.
- **Inconsistent sample restrictions**: Different `if` conditions across regressions that should use the same sample.

---

### Step 2: Reproducibility Checks

Review for issues that would cause the code to fail or produce different results on another machine or in the future.

#### 2.1 Path and Environment
- **Hardcoded paths**: Any absolute path that includes a username, machine name, or drive letter. Should use config files, globals, or relative paths.
- **Missing version specification**: For Stata: no `version` command. For R: no `sessionInfo()` or `renv.lock`. For Python: no `requirements.txt` or environment file.
- **Platform-specific code**: Forward vs back slashes, OS-specific commands.
- **Working directory assumptions**: Code that assumes a specific working directory without setting it.

#### 2.2 Randomness and Determinism
- **Unseeded randomness**: Any use of random numbers (`runiform()`, `sample()`, `np.random`) without a preceding `set seed` / `set.seed()` / `np.random.seed()`.
- **Sort-dependent operations**: Results that depend on sort order where the sort is not unique (see 1.1).
- **Floating point issues**: Comparisons using `==` on floating point numbers.

#### 2.3 Dependencies
- **Undocumented packages**: Community-contributed commands (Stata: `ssc install`; R: `install.packages`; Python: `pip install`) that are used but not listed in a requirements file or package installer script.
- **Version-sensitive commands**: Commands whose behavior changed between versions (e.g., Stata's `reghdfe` updates, R package breaking changes).

#### 2.4 File Dependencies
- **Input files not documented**: Data files read by the code but not listed in README or data documentation.
- **Output files not tracked**: Files created by the code that aren't mentioned in documentation.
- **Circular dependencies**: File A reads output of File B which reads output of File A.

---

### Step 3: Style and Readability

Review for issues that make code harder to understand, maintain, or review. Lower priority than correctness and reproducibility.

**Skip this section if `severity:high` flag is set.**

#### 3.1 Stata Style (based on DIME Analytics + Gentzkow-Shapiro)
- **`#delimit ;`**: Flag use of `#delimit` — prefer `///` for line continuation.
- **Abbreviations**: Flag abbreviated command names (`gen` is OK, but flag `g`, `d` for `drop`, `ren` for `rename`, `ta` for `tab`, `su` for `sum`). Only flag genuinely ambiguous abbreviations — `gen`, `reg`, `tab`, `sum` are universally understood and acceptable.
- **Variable abbreviation**: Flag reliance on partial variable name matching (Stata's dangerous default). Recommend `set varabbrev off`.
- **Indentation**: Inconsistent indentation, especially inside loops and if-blocks.
- **Line length**: Lines over 100 characters.
- **Magic numbers**: Unnamed numeric constants. Should be stored in locals/globals with descriptive names.
- **Commenting**: Major sections without header comments. Complex logic without inline explanation.

#### 3.2 R Style (based on tidyverse style guide)
- Long pipes (`%>%` or `|>`) without intermediate assignments.
- Functions over 50 lines without decomposition.
- Inconsistent naming (mixing `snake_case` and `camelCase`).

#### 3.3 Python Style
- Defer to Ruff/PEP 8. Only flag issues a linter wouldn't catch (e.g., misleading variable names in an econometric context).

#### 3.4 Cross-Language Style
- **Dead code**: Large commented-out blocks, unused variables, unreachable branches.
- **Copy-paste code**: Repeated blocks that should be a function/loop.
- **Naming**: Variable names that don't convey meaning (e.g., `x1`, `temp2`, `var_new`).

---

### Step 4: Documentation Checks

#### 4.1 File-Level
- Does the file have a header comment explaining: purpose, inputs, outputs, author, date?
- Is it clear where this file fits in the pipeline (what runs before/after it)?

#### 4.2 Data Transformations
- Are merge ratios documented (e.g., "expect 1:1 merge, N = 5,000")?
- Are sample restrictions explained (why drop these observations)?
- Are variable constructions documented (how is this index built)?

#### 4.3 Analysis
- Are regression specifications motivated (why these controls? why this functional form)?
- Are robustness checks documented (what is being tested and why)?
- Is it clear which tables/figures each code block produces?

---

### Step 5: Pipeline-Specific Checks (pipeline mode only)

*Skip unless mode = `pipeline` or `replication`.*

#### 5.1 Execution Order
- Is there a master file that runs everything in order?
- Can the full pipeline run from a single command ("push-button replication")?
- Are there files that must be run manually or out of order?

#### 5.2 Data Flow
- Trace the data from raw inputs to final outputs. Map: `raw data → cleaning → construction → analysis → tables/figures`.
- Flag any breaks in the chain (a file reads data that no previous file creates).
- Flag any data files that are created but never used downstream.

#### 5.3 Runtime
- Estimate total runtime if possible (flag long-running operations).
- Are there expensive operations that could be cached or skipped on re-runs?

---

### Step 6: Replication Package Checks (replication mode only)

*Skip unless mode = `replication`.*

Run the AEA Data Editor checklist. For each item, assess: Met / Partial / Missing / Can't Assess.

#### 6.1 README
- Follows AEA template structure (or equivalent)?
- Data availability statements for each data source?
- Computational requirements (software, hardware, runtime, storage)?
- Instructions for replicators (clear step-by-step)?

#### 6.2 Data
- Data citations in standard format (author, title, distributor, date, DOI)?
- License/terms of use for each dataset?
- Access instructions for restricted data?
- PII check — any risk of identifiable information?

#### 6.3 Code
- All code included and runnable?
- Package/dependency management (Stata: package installer do-file; R: `renv.lock`; Python: `requirements.txt`)?
- Version pinning (Stata version, R version, Python version)?
- Output mapping: which script produces which table/figure?

#### 6.4 Outputs
- All tables and figures in the paper reproducible from provided code + data?
- In-text statistics traceable to code?
- Appendix materials included?

#### 6.5 Legal and Ethical
- LICENSE file present?
- IRB approval documented?
- RCT registration cited?
- Data use agreements acknowledged?

---

### Step 7: Generate Output

**Classify each finding by severity:**
- **CRITICAL** — Will produce wrong results or prevent replication. Fix immediately.
- **HIGH** — Significant reproducibility risk or code quality issue. Fix before sharing.
- **MEDIUM** — Style or documentation issue that makes code harder to review. Fix when convenient.
- **LOW** — Nitpick. Optional improvement.

Save the report to the same directory as the reviewed file:
`review_[filename]_[YYYY-MM-DD].md`

For pipeline/replication reviews, save to the project root:
`code_review_[project]_[YYYY-MM-DD].md`

If the `fix` flag is set, also save a corrected version:
`[filename]_reviewed.[ext]`

Tell the user the full path to the output file(s).

---

## Output Format

```markdown
# Code Review: [filename or project name]

**Date:** [YYYY-MM-DD]
**Mode:** [quick / full / pipeline / replication]
**Language:** [Stata / R / Python]
**File(s) reviewed:** [path(s)]
**Reviewer:** /code-review skill v1.0
**Standards:** DIME Analytics, Gentzkow-Shapiro, AEA Data Editor

---

## Summary

**Overall assessment:** [Clean / Minor Issues / Needs Revision / Significant Problems]
**Findings:** [N] critical, [N] high, [N] medium, [N] low

[2-3 sentence summary of the most important findings.]

---

## Critical & High Findings

### F1: [Title]
- **Severity:** [CRITICAL / HIGH]
- **Category:** [Correctness / Reproducibility / Documentation / Pipeline / Replication]
- **Location:** [file:line_number or file:section]
- **Issue:** [What's wrong]
- **Risk:** [What could go wrong if unfixed]
- **Fix:** [Specific recommendation]

[Repeat for each critical/high finding]

---

## Medium Findings

### F[N]: [Title]
- **Severity:** MEDIUM
- **Category:** [category]
- **Location:** [location]
- **Issue:** [description]
- **Fix:** [recommendation]

[Repeat]

---

## Low Findings

[Brief list format — one line per finding]

- **F[N]:** [location] — [issue] → [fix]

---

## File Summary Table

| Check Category | Status | Issues Found |
|---------------|--------|-------------|
| Correctness | [pass/warn/fail] | [count] |
| Reproducibility | [pass/warn/fail] | [count] |
| Style | [pass/warn/fail] | [count] |
| Documentation | [pass/warn/fail] | [count] |
| Pipeline (if applicable) | [pass/warn/fail] | [count] |
| Replication (if applicable) | [pass/warn/fail] | [count] |

---

## Checklist (replication mode only)

| AEA Requirement | Status | Notes |
|----------------|--------|-------|
| [requirement] | [Met/Partial/Missing/Can't Assess] | [details] |

---

## Next Steps

1. [Highest-priority action]
2. [Second priority]
3. [Third priority]
```

---

## Principles

- **Correctness over style.** A well-formatted file with a wrong merge is worse than ugly code that produces correct results. Always prioritize findings that affect results.
- **Economics-aware.** Understand that `reghdfe` is a regression, that `_merge` matters, that `collapse` destroys data, that missing values sort high in Stata. Generic code review advice is insufficient.
- **Actionable findings.** Every issue comes with a specific fix. "This could be improved" is not a finding — "Line 47: `merge` without `_merge` check; add `assert _merge == 3` or `tab _merge` after merge" is.
- **Calibrate severity honestly.** Not everything is critical. A missing comment is LOW. A merge without diagnostics is HIGH. A hardcoded path is HIGH. An abbreviated command is LOW.
- **Do not fabricate.** If you cannot determine whether a pattern is an error or intentional, flag it as a question, not a finding. Say "Verify: is this intentional?" rather than "Bug: this is wrong."
- **Respect the author's intent.** Unusual patterns may be intentional. Flag them, explain the risk, but don't assume they're mistakes.
- **No scope creep.** Review the code as requested. Do not rewrite the analysis, suggest different specifications, or critique the research design (that's what `/review-paper` is for).
