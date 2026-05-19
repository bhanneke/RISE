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
