<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-result-extraction.md -->

# `result-extraction`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/replication/result-extraction.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Skill: Result Extraction

You are cataloging empirical results from an academic paper for replication purposes.

### What Counts as a "Result"
- Every row in every regression table
- Every panel in every table
- Summary statistics (Table 1 is almost always summary stats)
- Figures that show empirical findings (coefficient plots, event study plots)
- Statistical tests mentioned in text (Hausman, Wald, F-statistics)
- Robustness checks, even if in appendix

### Priority Classification
- **Primary**: Main specification that answers the core research question. Usually Table 3 or 4.
- **Secondary**: Extensions, heterogeneity analysis, mechanism tests
- **Robustness**: Alternative specifications, placebo tests, subsample analysis

### Coefficient Extraction
- Extract exact values: coefficient, standard error, t-statistic, p-value
- Note significance: * p<0.10, ** p<0.05, *** p<0.01 (or paper's convention)
- Note if SEs are robust, clustered, bootstrapped, etc.
- Record N, R-squared, F-statistic for each specification

### Model Identification
- What is the dependent variable?
- What are the independent variables (treatment, controls)?
- What fixed effects are included?
- How are standard errors computed?
- Is it OLS, IV, DiD, RDD, probit/logit, GMM, etc.?

### Replicability Assessment
For each result, assess:
- **High**: Public data + clear methodology + code available
- **Medium**: Public data + clear methodology, no code
- **Low**: Proprietary data or unclear methodology
