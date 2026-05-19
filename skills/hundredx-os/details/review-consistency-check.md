# Consistency Check

## Purpose

This skill describes how to perform a mechanical number verification audit on an
academic paper draft. The goal is to cross-reference every quantitative claim in
the text against the source artifacts (data summaries, estimation output, analysis
results) and flag any discrepancies.

A consistency check is not about whether the methods are correct — that's the job
of the referee and technical reviewer. This is about whether the numbers in the
paper accurately reflect what the pipeline actually produced.

---

## Step 1: Extract Numerical Claims from the Draft

Systematically scan the draft for every quantitative statement:

### In-text claims
- "The sample contains N observations"
- "The coefficient on X is 0.45 (SE = 0.12)"
- "This represents a Y% increase relative to the mean"
- "The effect is significant at the Z% level"
- "The mean of X is M (SD = S)"

### Tables
- Every cell in every table is a checkable claim
- Pay special attention to: N rows, coefficient cells, SE/t-stat cells,
  R-squared values, number of fixed effects/clusters

### Figures
- Axis labels with specific values
- Annotated data points
- Reported statistics in figure notes

### Abstract and conclusion
- These often contain rounded or paraphrased versions of key results —
  verify they are consistent with the precise values in the body

---

## Step 2: Match Claims Against Source Artifacts

For each numerical claim, identify the source artifact:

| Claim type | Primary source | Secondary source |
|-----------|---------------|-----------------|
| Sample size (N) | summary_statistics.json | data_description.md |
| Variable means/SDs | summary_statistics.json | data_description.md |
| Coefficients | estimation_results.json | analysis output |
| Standard errors | estimation_results.json | analysis output |
| P-values | estimation_results.json (compute from coef/SE) | analysis output |
| R-squared | estimation_results.json | analysis output |
| Robustness coefficients | robustness results in analysis | — |
| Economic magnitudes | Derived from coefficient + mean | summary_statistics.json |

---

## Step 3: Apply Tolerance Rules

Not every small difference is a discrepancy. Apply these rules:

### Exact match required
- Sample sizes (integers): must match exactly
- Signs of coefficients: must match exactly
- Significance levels: if the paper says "significant at 5%", the p-value
  must actually be < 0.05

### Rounding tolerance
- A value is consistent if it rounds to the reported value at the reported
  precision level
- Example: actual = 0.4527, reported as 0.45 → **consistent**
- Example: actual = 0.4527, reported as 0.453 → **consistent**
- Example: actual = 0.4527, reported as 0.46 → **inconsistent** (minor)
- Example: actual = 0.4527, reported as 0.54 → **inconsistent** (critical — transposed digits)

### Derived quantity tolerance
- For percentage changes: (coefficient / mean) × 100
  - Allow 0.5 percentage point tolerance for rounding in the chain
- For standard deviation units: coefficient / SD
  - Allow 0.05 SD tolerance for rounding

---

## Step 4: Classify Discrepancies by Severity

### Critical
- Wrong sign on a coefficient
- Sample size off by more than 10%
- Main result coefficient off by more than 20% of its value
- Claiming significance when p-value > reported threshold
- Transposed digits (0.45 vs 0.54)

### Major
- Coefficient off by 5-20% of its value
- Standard error off by more than 10%
- Summary statistic (mean/SD) off by more than 10%
- Economic magnitude incorrectly computed
- Robustness result direction inconsistent with text description

### Minor
- Rounding differences within 5% of value
- R-squared differences in third decimal place
- Number of observations off by a small count (< 1%)
- Slight imprecision in derived quantities

---

## Step 5: Common Error Patterns

Watch for these frequent mistakes:

1. **Transposed digits**: 0.453 → 0.435 or 0.543
2. **Wrong specification**: Reporting coefficient from column (2) as if it
   were from column (1)
3. **Stale numbers**: Draft references an earlier estimation run; numbers
   have since been updated in the artifacts
4. **Unit confusion**: Reporting a coefficient in levels when the variable
   is in logs (or vice versa)
5. **Percentage vs. percentage points**: "5% increase" vs. "5 percentage
   point increase" — these are very different
6. **Off-by-one in sample size**: Often caused by dropping NAs at different
   stages of the pipeline
7. **Clustered vs. robust SEs**: Draft reports one but estimation used the other
8. **Weighted vs. unweighted**: Summary stats computed with/without weights

---

## Step 6: Handle Unverifiable Claims

Some claims cannot be checked against available artifacts:

- Claims referencing external literature ("Smith (2020) finds...")
- Qualitative characterizations ("the effect is economically large")
- Claims about data that was collected but not stored in artifacts

Mark these as "unverifiable" rather than "consistent" or "inconsistent".
A high proportion of unverifiable claims (> 30%) is itself a flag — it
suggests the artifacts don't fully document the analysis.

---

## Output Structure

The consistency report should be organized as:

```
# Consistency Check Report

## Summary
- Total claims checked: N
- Consistent: N (X%)
- Inconsistent: N (Y%)
- Unverifiable: N (Z%)
- Overall verdict: PASS / FAIL

## Critical Discrepancies
[If any — these must be fixed before the paper can proceed]

## Major Discrepancies
[These should be fixed]

## Minor Discrepancies
[Nice to fix but not blocking]

## Detailed Check Log
[Every claim, its source, and the verification result]
```
