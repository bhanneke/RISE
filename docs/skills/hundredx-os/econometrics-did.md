<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/econometrics-did.md -->

# `did`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/econometrics/did.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Difference-in-Differences

### Core Idea

Difference-in-differences (DiD) estimates causal effects by comparing changes in outcomes over time between a treated group and a control group. The first difference removes time-invariant unobservables; the second difference removes common time trends.

In the canonical 2x2 case (two groups, two periods):

tau_DiD = (Y_treat,post - Y_treat,pre) - (Y_control,post - Y_control,pre)

This equals the ATT (average treatment effect on the treated) under the parallel trends assumption.

### Parallel Trends Assumption

The identifying assumption: absent treatment, the treated and control groups would have followed the same trend in outcomes.

- This assumption concerns counterfactual outcomes and is fundamentally untestable.
- Pre-treatment trends provide suggestive evidence but cannot prove parallel trends would hold post-treatment.
- Violations arise from differential shocks, differential anticipation effects, or compositional changes.

Strategies to support parallel trends:
- Show parallel pre-trends in outcome variable (event study plot)
- Show balance on covariates and their trends
- Test placebo outcomes that should not be affected by treatment
- Use alternative control groups and check robustness
- Apply covariate-adjusted DiD (conditioning on observables that drive differential trends)

### Two-Way Fixed Effects (TWFE) Regression

The standard implementation:

Y_it = alpha_i + gamma_t + beta * D_it + epsilon_it

Where alpha_i are unit fixed effects, gamma_t are time fixed effects, and D_it is the treatment indicator.

**Problems with TWFE under staggered treatment timing:**

When different units receive treatment at different times, the TWFE beta is a weighted average of all possible 2x2 DiD comparisons, including:
- Clean comparisons: newly treated vs never-treated
- Problematic comparisons: newly treated vs already-treated (using already-treated units as controls)
- Negative weights: some comparisons enter with negative weights, so beta can be negative even when all unit-level effects are positive

Goodman-Bacon (2021) decomposition shows exactly which 2x2 comparisons contribute to the TWFE estimate and their weights. This diagnostic should be the first step when TWFE is applied to staggered designs.

### Event Study Specification

The dynamic event study regression:

Y_it = alpha_i + gamma_t + sum_{k != -1} beta_k * 1(t - E_i = k) + epsilon_it

Where E_i is the treatment adoption date for unit i, and k indexes periods relative to treatment. The period k = -1 is normalized to zero (reference period).

Interpretation:
- Pre-treatment coefficients (k < 0) test for differential pre-trends. If significantly different from zero, parallel trends is suspect.
- Post-treatment coefficients (k >= 0) trace out dynamic treatment effects.

TWFE event study problems under staggered treatment:
- Pre-treatment coefficients can show spurious trends even when parallel trends holds, due to contamination from heterogeneous treatment effects.
- Post-treatment coefficients are biased for the same reasons as static TWFE.
- Sun and Abraham (2021) show TWFE event study coefficients are weighted averages of cohort-specific effects with potentially negative weights.

### Modern DiD Estimators for Staggered Treatment

#### Callaway and Sant'Anna (2021)

- Estimates group-time average treatment effects: ATT(g, t) for each cohort g (defined by treatment timing) and time period t.
- Uses never-treated or not-yet-treated units as clean controls.
- Aggregation: ATT(g, t) can be aggregated to overall ATT, dynamic effects by event time, or group-specific effects.
- Allows conditioning on covariates via outcome regression, inverse probability weighting, or doubly robust methods.
- R package: `did`. Stata: `csdid`.

#### Sun and Abraham (2021)

- Interaction-weighted estimator that corrects the TWFE event study.
- Estimates cohort-specific event-study coefficients, then aggregates with appropriate weights.
- Requires a "last treated" or never-treated cohort as reference.
- Implemented via `eventstudyinteract` in Stata, `sunab()` in R `fixest`.

#### de Chaisemartin and D'Haultfoeuille (2020)

- Estimates the effect on "switchers" (units whose treatment status changes) at each period.
- Does not require parallel trends for all periods, only for consecutive periods.
- Allows for heterogeneous and dynamic effects.
- Stata: `did_multiplegt`. R: `DIDmultiplegt`.

#### Borusyak, Jaravel, and Spiess (2024)

- Imputation estimator: first estimates the counterfactual using untreated observations (unit and time FE), then computes treatment effects as residuals.
- Efficient under homoskedasticity; straightforward extension to covariates.
- Stata: `did_imputation`. R: `didimputation`.

#### Roth and Sant'Anna (2023)

- Pre-test and sensitivity analysis framework specifically for DiD.
- Addresses the problem that pre-testing for parallel trends distorts subsequent inference.
- Honest confidence intervals that account for possible violations of parallel trends consistent with pre-test results.
- R: `HonestDiD`.

### Pre-Trend Testing

Testing for pre-trends is standard practice but has important limitations:

- **Low power**: Failure to reject parallel pre-trends does not mean they hold. With small samples or short pre-periods, the test may simply lack power.
- **Pre-test bias (Roth 2022)**: Conditioning on passing a pre-trend test biases DiD estimates. Researchers who find significant pre-trends may adjust their specification until pre-trends disappear, inflating the false positive rate.
- **Recommendations**:
  - Report event study coefficients with confidence intervals, not just point estimates.
  - Use Roth (2022) sensitivity analysis: how large a violation of parallel trends (consistent with the pre-trend evidence) would be needed to explain away the result?
  - Power calculations for pre-trend tests: can you actually detect economically meaningful violations?
  - Apply HonestDiD (Roth and Sant'Anna 2023) for inference robust to possible trend violations.

### Covariate-Adjusted DiD

When parallel trends holds conditional on covariates but not unconditionally:

- **Outcome regression**: Include covariates interacted with time in the TWFE regression. Risk of misspecification.
- **Inverse probability weighting (Abadie 2005)**: Reweight control observations to match treated group on covariates. Requires correct propensity score model.
- **Doubly robust (Sant'Anna and Zhao 2020)**: Combines regression and IPW. Consistent if either the outcome model or the propensity score model is correctly specified.

### Triple Differences (DDD)

When parallel trends is implausible but a within-group comparison restores it:

tau_DDD = DiD(affected subgroup) - DiD(unaffected subgroup within same units)

The third difference removes group-specific trends that threaten the standard DiD. Requires that the unaffected subgroup's trend captures the counterfactual trend for the affected subgroup.

### Practical Checklist

1. Plot raw outcome trends for treated and control groups pre-treatment. Do they look parallel?
2. Run event study specification and plot coefficients with confidence intervals.
3. If staggered treatment: run Goodman-Bacon decomposition to diagnose TWFE issues.
4. Use modern estimators (Callaway-Sant'Anna or Borusyak-Jaravel-Spiess) as baseline.
5. Report TWFE alongside modern estimators for comparison with existing literature.
6. Cluster standard errors at the level of treatment assignment (typically unit or state level).
7. Conduct Roth (2022) sensitivity analysis for parallel trends violations.
8. Test placebo outcomes and alternative control groups.
9. Discuss potential anticipation effects and whether treatment timing is exogenous.
10. With few treated clusters, consider wild bootstrap or randomization inference.

### Key References

- Roth, J., Sant'Anna, P., Bilinski, A., and Poe, J. (2023). What's trending in difference-in-differences? A synthesis of the recent econometrics literature. Journal of Econometrics.
- Callaway, B. and Sant'Anna, P. (2021). Difference-in-differences with multiple time periods. Journal of Econometrics.
- Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. Econometrica.
- Sun, L. and Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. Journal of Econometrics.
- de Chaisemartin, C. and D'Haultfoeuille, X. (2020). Two-way fixed effects estimators with heterogeneous treatment effects. American Economic Review.
- Roth, J. (2022). Pretest with caution: Event-study estimates after testing for parallel trends. American Economic Review: Insights.
