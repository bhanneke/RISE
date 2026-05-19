<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-econometrics.md -->

# `econometrics`



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

# Econometrics Review Checklist

Systematic checklist for evaluating empirical methodology. For detailed
method-specific guidance, see the dedicated skill files (did.md, rdd.md,
iv-estimation.md, panel-data.md, etc.).

---

## 1. Identification Strategy

- [ ] Paper clearly states what it estimates (causal effect, descriptive, structural parameter)
- [ ] Identifying assumption stated explicitly (words AND formally)
- [ ] Most plausible threats discussed with evidence or arguments
- [ ] Estimand well-defined (ATE, ATT, LATE? For whom?)
- [ ] Direction of potential bias from assumption violations discussed

### Method-Specific Quick Checks

**DiD:** Pre-trends shown (event study)? Staggered timing addressed? Anticipation tested?
**IV:** First-stage F reported? Exclusion argued substantively? Reduced form shown?
**RD:** Density test reported? Covariate continuity shown? Bandwidth robustness?
**RCT:** Balance table? Attrition tested? Pre-registration?

---

## 2. Standard Errors and Inference

- [ ] Clustering at treatment assignment level (report number of clusters)
- [ ] Few clusters (<40): wild bootstrap or randomization inference
- [ ] Multiple testing correction if many outcomes/subgroups tested
- [ ] Spatial correlation addressed if geographically proximate units

---

## 3. Robustness

- [ ] Alternative specifications (controls, functional form, FE)
- [ ] Alternative samples (dropping outliers, subsamples)
- [ ] Alternative variable definitions
- [ ] Placebo treatments (wrong time/place)
- [ ] Placebo outcomes (should-not-be-affected outcomes)
- [ ] Sensitivity analysis (Oster 2019, Conley et al. bounds)
- [ ] Leave-one-out for cross-region/country studies

---

## 4. Interpretation and Reporting

- [ ] Economic significance discussed alongside statistical significance
- [ ] Effect sizes in interpretable units (%, SD, benchmark comparison)
- [ ] Sign and magnitude consistent with theory and prior literature
- [ ] Confidence intervals or SEs reported (not just t-stats or p-values)
- [ ] No bright-line p-value treatment (0.049 vs 0.051)
- [ ] Null findings: minimum detectable effect reported

---

## Quick Reference: Common Pitfalls

| Pitfall | Why it matters | Check |
|---------|---------------|-------|
| Bad controls | Post-treatment variables bias estimates | Controls are pre-determined? |
| Wrong clustering | Underestimates SEs | Clustered at treatment level? |
| Staggered DiD + TWFE | Wrong sign with heterogeneous effects | Modern estimator used? |
| Weak instruments | IV biased toward OLS | F > 10? LIML reported? |
| p-hacking | False positives | Robustness, pre-registration? |
| Multiple testing | False positives | Outcomes/subgroups counted? |
| Log of zero | Undefined; log(1+x) distorts | Zeros in logged variables? |
| Survivorship bias | Selected sample | Entry/exit patterns checked? |


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/review/econometrics.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>review</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/review-econometrics/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
