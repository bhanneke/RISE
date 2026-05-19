# Technical Review

## Purpose

This skill describes how to conduct a technical/methodological review of a
research paper, focusing on the internal coherence of the data-to-results
pipeline. Unlike a referee report (which evaluates contribution and positioning),
the technical review asks: does the implementation actually do what the paper
claims it does?

---

## Step 1: Data Pipeline Verification

Trace the data from source to estimation sample:

### SQL / data construction
- Read the data queries. Do they construct the sample described in the paper?
- Are exclusion criteria in the code the same as those described in the text?
- Are variable definitions in the code consistent with the data description?
- Does the time period in the query match the stated time period?

### Sample construction
- How are missing values handled? Is it documented?
- Are there implicit filters (e.g., inner joins that drop observations)?
- Is the unit of observation what the paper claims? (e.g., firm-quarter,
  address-day, protocol-week)
- Are there duplicates? Is deduplication documented?

### Variable definitions
- Are continuous variables winsorized or trimmed? At what level?
- Are categorical variables grouped appropriately?
- Are log transformations applied where claimed? What about zeros?
- Do variable names in the code match the variable names in the paper?

**Red flags:**
- Unexplained sample size differences between data description and estimation
- Variables defined differently in different scripts
- Hardcoded filter values without documentation (e.g., `WHERE value > 1000`
  without explaining why 1000)

---

## Step 2: Estimation Code-to-Paper Alignment

Compare the estimation code against the stated econometric specification:

### Specification match
- Write out the estimating equation from the paper
- Write out what the code actually estimates
- Are they the same? Check:
  - Dependent variable
  - Independent variables (treatment, controls)
  - Fixed effects
  - Interaction terms
  - Sample restrictions

### Standard errors
- What level are standard errors clustered at in the code?
- Is this the level described in the paper?
- Is the number of clusters reported? Is it sufficient (>= 30)?
- If robust (HC) errors are used, which variant? (HC0, HC1, HC2, HC3)

### Fixed effects
- Which fixed effects are included in the code?
- Do they match what the paper reports?
- Are they collinear with the treatment variable? (This would absorb the
  effect of interest.)

### Functional form
- Level vs. log specification: does the code match the paper?
- Are polynomials or splines used as described?
- For binary outcomes: logit/probit vs. linear probability model — consistent?

---

## Step 3: Results Interpretation Check

### Effect size interpretation
- Is the coefficient interpreted in the correct units?
  - Log-level: a one-unit increase in X is associated with a (β×100)% change in Y
  - Log-log: a 1% increase in X is associated with a β% change in Y
  - Level-level: a one-unit increase in X is associated with a β-unit change in Y
- Are economic magnitudes computed from the right baseline?
  - "A one-SD increase in X leads to..." — is the SD from the estimation sample
    or the full sample?

### Significance and inference
- Do the reported significance stars match the standard errors?
  - Check: |coefficient / SE| > 1.96 for 5% significance
- Are confidence intervals correctly computed? (coef ± 1.96 × SE for 95%)
- If multiple testing is an issue, is there a correction?

### Robustness assessment
- Are the robustness checks addressing the actual threats to identification
  listed in the paper?
- Or are they "cosmetic" — e.g., adding an irrelevant control, changing a
  bandwidth that doesn't matter?
- A good robustness check directly tests a specific alternative explanation.
  Does each reported check do this?

---

## Step 4: Red Flag Detection

### P-value patterns
- Count the p-values in the paper. Is there unusual clustering just below
  conventional thresholds (0.05, 0.01, 0.10)?
- This is not proof of p-hacking, but a pattern worth noting.

### Specification searching
- Are there signs that many specifications were tried but only favorable
  ones reported?
- Does the paper report a "preferred specification" without justifying why
  it's preferred?
- Are there large jumps in coefficients across specifications? This suggests
  sensitivity to choices.

### Selective reporting
- Are there variables in the estimation code that don't appear in any table?
- Are there specifications in the code that aren't reported?
- Is there a "table graveyard" — tables mentioned in comments but not in the paper?

### Magic numbers
- Are there hardcoded values in the estimation or analysis code?
- Examples: `if p_value < 0.05`, `threshold = 100`, `winsorize_level = 0.01`
- These should be documented or parameterized.

### Suspiciously clean results
- All coefficients significant with the same sign
- R-squared suspiciously high for the type of regression
- Perfect monotonicity in heterogeneity results
- Zero standard errors or perfect prediction

---

## Step 5: Internal Consistency Across Pipeline Stages

The most common source of technical problems is inconsistency between
pipeline stages:

| Check | What to verify |
|-------|---------------|
| Data → Estimation | Does the estimation code read the data the data stage produced? Same variables, same sample? |
| Estimation → Analysis | Does the analysis script use the estimation results correctly? |
| Analysis → Draft | Does the draft accurately report what the analysis found? |
| RSD → Estimation | Does the estimation implement the strategy described in the Research Strategy Document? |
| RSD → Draft | Does the paper claim to do what the RSD says? |

---

## Output Structure

```
# Technical Review

## Summary Assessment
[Pass / Concerns / Fail — with one-paragraph justification]

## Data Pipeline
[Issues found, or confirmation that pipeline is sound]

## Estimation Implementation
[Code-to-paper alignment issues, or confirmation of alignment]

## Results Reporting
[Interpretation issues, significance checks, robustness assessment]

## Red Flags
[Any red flags detected, or "None detected"]

## Strengths
[What the implementation does well — be specific]

## Recommendations
[Specific actions to address each issue, mapped to pipeline stages]
```
