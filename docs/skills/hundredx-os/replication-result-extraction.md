<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-result-extraction.md -->

# `result-extraction`

*Pack: [100xOS shared skills](../hundredx-os.md) · category `replication` · field `economics`*

---

# Skill: Result Extraction

You are cataloging empirical results from an academic paper for replication purposes.

## What Counts as a "Result"
- Every row in every regression table
- Every panel in every table
- Summary statistics (Table 1 is almost always summary stats)
- Figures that show empirical findings (coefficient plots, event study plots)
- Statistical tests mentioned in text (Hausman, Wald, F-statistics)
- Robustness checks, even if in appendix

## Priority Classification
- **Primary**: Main specification that answers the core research question. Usually Table 3 or 4.
- **Secondary**: Extensions, heterogeneity analysis, mechanism tests
- **Robustness**: Alternative specifications, placebo tests, subsample analysis

## Coefficient Extraction
- Extract exact values: coefficient, standard error, t-statistic, p-value
- Note significance: * p<0.10, ** p<0.05, *** p<0.01 (or paper's convention)
- Note if SEs are robust, clustered, bootstrapped, etc.
- Record N, R-squared, F-statistic for each specification

## Model Identification
- What is the dependent variable?
- What are the independent variables (treatment, controls)?
- What fixed effects are included?
- How are standard errors computed?
- Is it OLS, IV, DiD, RDD, probit/logit, GMM, etc.?

## Replicability Assessment
For each result, assess:
- **High**: Public data + clear methodology + code available
- **Medium**: Public data + clear methodology, no code
- **Low**: Proprietary data or unclear methodology
