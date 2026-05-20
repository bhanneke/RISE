<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-econometrics.md -->

# `econometrics`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/review/econometrics.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Econometrics Review Checklist

Systematic checklist for evaluating empirical methodology. For detailed
method-specific guidance, see the dedicated skill files (did.md, rdd.md,
iv-estimation.md, panel-data.md, etc.).

---

### 1. Identification Strategy

- [ ] Paper clearly states what it estimates (causal effect, descriptive, structural parameter)
- [ ] Identifying assumption stated explicitly (words AND formally)
- [ ] Most plausible threats discussed with evidence or arguments
- [ ] Estimand well-defined (ATE, ATT, LATE? For whom?)
- [ ] Direction of potential bias from assumption violations discussed

#### Method-Specific Quick Checks

**DiD:** Pre-trends shown (event study)? Staggered timing addressed? Anticipation tested?
**IV:** First-stage F reported? Exclusion argued substantively? Reduced form shown?
**RD:** Density test reported? Covariate continuity shown? Bandwidth robustness?
**RCT:** Balance table? Attrition tested? Pre-registration?

---

### 2. Standard Errors and Inference

- [ ] Clustering at treatment assignment level (report number of clusters)
- [ ] Few clusters (<40): wild bootstrap or randomization inference
- [ ] Multiple testing correction if many outcomes/subgroups tested
- [ ] Spatial correlation addressed if geographically proximate units

---

### 3. Robustness

- [ ] Alternative specifications (controls, functional form, FE)
- [ ] Alternative samples (dropping outliers, subsamples)
- [ ] Alternative variable definitions
- [ ] Placebo treatments (wrong time/place)
- [ ] Placebo outcomes (should-not-be-affected outcomes)
- [ ] Sensitivity analysis (Oster 2019, Conley et al. bounds)
- [ ] Leave-one-out for cross-region/country studies

---

### 4. Interpretation and Reporting

- [ ] Economic significance discussed alongside statistical significance
- [ ] Effect sizes in interpretable units (%, SD, benchmark comparison)
- [ ] Sign and magnitude consistent with theory and prior literature
- [ ] Confidence intervals or SEs reported (not just t-stats or p-values)
- [ ] No bright-line p-value treatment (0.049 vs 0.051)
- [ ] Null findings: minimum detectable effect reported

---

### Quick Reference: Common Pitfalls

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
