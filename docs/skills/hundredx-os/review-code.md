<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-code.md -->

# `code`

*Pack: [100xOS shared skills](../hundredx-os.md) · category `review` · field `economics`*

---

# Code Review Checklist for Academic Research

## Purpose

Research code must be correct, reproducible, and understandable -- by your future self, by coauthors, and by referees or replicators who may examine it years later. This checklist covers the standards that distinguish reliable research code from fragile scripts that produce results no one can verify.

---

## 1. Reproducibility

Reproducibility is the single most important property of research code. If someone cannot run your code and get the same results, the research is unverifiable.

**Check these items:**

- [ ] A master script (e.g., `main.R`, `run_all.py`, `master.do`) runs the entire analysis from raw data to final tables and figures, in order, without manual intervention.
- [ ] All file paths are relative to the project root, not hardcoded to a specific machine (no `/Users/john/Desktop/project/`).
- [ ] A `README` documents how to run the code: required software, required packages (with versions), expected runtime, and the order of execution.
- [ ] Random seeds are set explicitly wherever randomness is involved (bootstrapping, simulation, sample splitting, machine learning). Document the seed value.
- [ ] The code produces the exact tables and figures that appear in the paper. Numbering in the code matches numbering in the manuscript.
- [ ] A `requirements.txt`, `renv.lock`, `environment.yml`, or equivalent pins all package versions. "It works on my machine" is not reproducibility.
- [ ] Raw data files are never modified by the code. Cleaning and transformation produce new files, leaving originals intact.

---

## 2. Documentation

Code documentation serves two audiences: someone trying to understand what the code does, and someone trying to verify that it does what the paper claims.

**Check these items:**

- [ ] Every script begins with a header comment explaining: purpose, inputs, outputs, and author/date.
- [ ] Non-obvious steps are explained with comments. The "why" matters more than the "what." Do not comment `x = x + 1  # add 1 to x` -- instead explain why you are adding 1.
- [ ] Variable construction matches the paper's variable definitions. If the paper says "we define firm size as the average number of employees over the fiscal year," the code should have a comment pointing to this definition.
- [ ] Sample restrictions are documented: which observations are dropped, why, and how many.
- [ ] Any hardcoded values (thresholds, cutoffs, parameters) are explained and ideally defined as named constants at the top of the script.
- [ ] Complex data merges document the expected merge rate. If you expect a 1:1 merge with 95% match rate, assert this in the code.

---

## 3. Data Handling

Data errors are the most common source of incorrect results in empirical economics.

**Check these items:**

- [ ] Data loading includes explicit type specifications (do not let the software guess whether "2024" is a number or a string).
- [ ] Merges are validated: check for unexpected duplicates, verify merge rates, and inspect unmatched observations.
- [ ] Missing values are handled explicitly, not silently dropped. Document the missing data pattern and the treatment (listwise deletion, imputation, indicator approach).
- [ ] Variable transformations (logs, winsorizing, standardization) are applied correctly. `log(0)` is undefined -- how do you handle zeros?
- [ ] Panel data is checked for balance: are there gaps? Duplicate observations within a panel unit-period?
- [ ] Monetary values are deflated with a clearly documented price index and base year.
- [ ] Categorical variables are coded consistently. Check for variations in spelling, capitalization, and whitespace.
- [ ] Intermediate datasets are saved at key processing steps to allow partial reruns and debugging.

---

## 4. Error Handling and Defensive Programming

Research code should fail loudly when assumptions are violated, not silently produce wrong results.

**Check these items:**

- [ ] Assertions validate key assumptions: expected number of observations, no negative values where impossible, no duplicate IDs in a cross-section.
- [ ] Merge diagnostics check for unexpected many-to-many merges. In Stata: `assert _merge == 3` or check `_merge` distribution. In R/Python: verify row counts before and after joins.
- [ ] Division by zero is handled or checked for.
- [ ] Regressions that fail to converge are caught and logged, not silently ignored.
- [ ] If code depends on external APIs or data downloads, failures are handled gracefully with clear error messages.
- [ ] Edge cases are tested: empty subsamples, single-observation groups, perfect collinearity.

---

## 5. Naming Conventions

Clear naming makes code self-documenting and reduces errors.

**Check these items:**

- [ ] Variable names are descriptive: `log_wage` not `x1`, `treatment_post` not `tp`, `firm_size_avg` not `fs`.
- [ ] Naming is consistent across scripts. If one script calls it `ln_income`, do not call it `log_inc` in another.
- [ ] File names indicate content and order: `01_clean_data.R`, `02_construct_variables.R`, `03_main_regressions.R`.
- [ ] Output files are named to match the paper: `table_1_summary_stats.tex`, `figure_3_event_study.pdf`.
- [ ] Temporary or intermediate variables are clearly marked and cleaned up.

---

## 6. Testing

Research code deserves the same testing discipline as production software, adapted to the academic context.

**Check these items:**

- [ ] Key functions have unit tests. If you wrote a function to compute a Herfindahl index, test it on a simple case where you know the answer.
- [ ] Regression results are sanity-checked: sign of coefficient, order of magnitude, comparison with back-of-envelope calculations.
- [ ] End-to-end tests verify that the pipeline produces expected output from known input. Use a small synthetic dataset.
- [ ] Sensitivity tests for hardcoded parameters are implemented (not just described in the paper). If you winsorize at the 1st and 99th percentiles, the code should make it easy to change this and rerun.
- [ ] After major refactoring, compare outputs to the previous version to verify nothing changed unintentionally.

---

## 7. Version Control

Version control is not optional for research code.

**Check these items:**

- [ ] The project uses Git (or equivalent). All code is tracked.
- [ ] `.gitignore` excludes data files (especially large or confidential ones), compiled files, and editor-specific files.
- [ ] Commits are atomic and have descriptive messages: "Add IV specification for Table 5" not "updates" or "stuff."
- [ ] The repository contains no API keys, passwords, or personally identifiable data.
- [ ] The state of the code that produced the submitted paper is tagged or recorded (e.g., `git tag v1-submission`).
- [ ] If data cannot be shared, the repository includes a data dictionary and instructions for obtaining the data.

---

## 8. Performance and Scalability

Not always critical, but important for large datasets or computationally intensive methods.

**Check these items:**

- [ ] Loops over observations are vectorized where possible (especially in R and Python -- avoid row-by-row operations on data frames).
- [ ] Bootstrap and simulation code can be parallelized.
- [ ] Memory usage is reasonable. Do not load the entire dataset into memory if you only need a subset.
- [ ] Long-running computations save intermediate results so they do not need to be rerun from scratch.
- [ ] Expected runtime is documented for key scripts.

---

## 9. Language-Specific Checks

### Stata
- [ ] `set seed` before any randomization.
- [ ] `assert` after merges to verify merge quality.
- [ ] `eststo` / `esttab` or equivalent for reproducible table output.
- [ ] `log using` to capture console output.

### R
- [ ] `set.seed()` before random operations.
- [ ] Use `renv` for package management.
- [ ] Prefer `tidyverse` or `data.table` consistently, not a mix that confuses readers.
- [ ] Use `fixest` or `lfe` for large fixed-effects regressions (orders of magnitude faster than `lm` with dummy variables).

### Python
- [ ] Use `pandas` with explicit `dtypes` on read.
- [ ] Prefer `statsmodels` or `linearmodels` for econometric regressions.
- [ ] Use virtual environments (`venv`, `conda`).
- [ ] Type hints for functions that will be reused.

---

## Pre-Submission Final Check

Before submitting a replication package:

- [ ] Clone the repository to a fresh directory and run the master script from scratch.
- [ ] Verify that every table and figure in the paper is produced.
- [ ] Verify that all numbers cited in the text (including those in the introduction and conclusion) can be traced to a specific line of code.
- [ ] Remove any dead code, commented-out experiments, or personal notes.
- [ ] Include a LICENSE file (MIT or BSD are common for research code).
- [ ] Check that the README answers: What software? What data? How to run? What to expect?
