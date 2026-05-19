<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/replication-result-extraction.md -->

# `result-extraction`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

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


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/replication/result-extraction.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>replication</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>replication</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/replication-result-extraction/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
