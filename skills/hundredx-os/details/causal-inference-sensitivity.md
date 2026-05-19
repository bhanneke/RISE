# Sensitivity Analysis for Causal Inference

## Motivation

No observational study can prove that unobserved confounding is absent. Sensitivity analysis asks: how large would unobserved confounding need to be to overturn the estimated causal effect? This shifts the question from "is there confounding?" (unanswerable) to "how much confounding would be needed?" (quantifiable and interpretable).

## Oster (2019) Method: Selection on Unobservables

### Framework

Oster extends the Altonji, Elder, and Taber (2005) idea that the degree of selection on observables provides information about the likely degree of selection on unobservables.

The central assumption: if the observed controls capture a representative proportion of the total selection, then the relationship between observed control inclusion and coefficient movements is informative about omitted variable bias.

### The Delta Parameter

Oster defines delta as the ratio of selection on unobservables to selection on observables:

delta = [Cov(unobservables, treatment) / Var(unobservables)] / [Cov(observables, treatment) / Var(observables)]

**Interpretation**:
- delta = 0: no selection on unobservables (OLS with controls is unbiased).
- delta = 1: selection on unobservables equals selection on observables (the "proportional selection" assumption).
- delta > 1: unobservables are more important than observables for selection.

### Computing Bounds

Oster provides a formula for bias-adjusted treatment effects as a function of delta and R_max (the R-squared that would obtain if all confounders were included).

**Inputs**:
1. Coefficient and R-squared from the short regression (no controls): beta_tilde, R_tilde.
2. Coefficient and R-squared from the controlled regression: beta_hat, R_hat.
3. R_max: the maximum R-squared achievable with all unobservables included. Oster recommends R_max = min(2.2 * R_hat, 1) as a heuristic, though researchers should justify this choice.

**Output**: The bias-adjusted beta* for a given (delta, R_max) pair. Or equivalently, the value of delta at which beta* = 0 (the "identified set" includes zero).

### Reporting

1. Report the controlled coefficient beta_hat and R_hat.
2. Compute beta* assuming delta = 1 and R_max = 2.2 * R_hat. If beta* has the same sign as beta_hat and is non-trivial in magnitude, the result is robust to proportional selection.
3. Compute the value of delta that sets beta* = 0. If delta > 1, unobservables would need to be more important than observables to explain away the result.
4. Show how beta* varies as delta ranges from 0 to 2 and as R_max varies.

### Limitations

- The proportional selection assumption (delta = 1) may not hold if researchers strategically include the strongest controls.
- R_max is unknown and the bound is sensitive to its choice.
- The method assumes linearity in the confounding structure.
- Does not account for nonlinear confounding or interaction effects.

## Altonji, Elder, and Taber (2005) — The Original Approach

### Idea

If the set of observed controls is chosen randomly from the full set of relevant variables, then the covariance of the treatment with observed controls should be informative about the covariance of the treatment with unobserved confounders.

### Implementation

Compare the treatment effect from a regression with no controls to one with a rich set of controls. If adding controls changes the coefficient only slightly, this suggests omitted variables are unlikely to generate large bias.

Formally, under the "equal selection" assumption:
- The bias from unobservables equals the coefficient shift from adding observables.
- The bias-adjusted estimate is 2 * beta_controlled - beta_uncontrolled.

### Comparison with Oster

Oster (2019) generalizes this by:
1. Allowing delta != 1 (unequal selection on observables vs unobservables).
2. Incorporating R-squared changes (movements in R-squared constrain the possible degree of omitted variable bias).
3. Providing a continuous sensitivity parameter rather than a binary "equal selection" assumption.

## Conley, Hansen, and Rossi (2012) — Plausibly Exogenous Instruments

### Problem

The exclusion restriction in IV requires that the instrument affects the outcome only through the endogenous variable. This is untestable in the just-identified case. Conley et al. relax this assumption to allow for "plausibly exogenous" instruments that may have a small direct effect on the outcome.

### Model

Y = X * beta + Z * gamma + epsilon

where gamma is the direct effect of the instrument Z on the outcome. The standard exclusion restriction sets gamma = 0. Conley et al. allow gamma to be non-zero but bounded.

### Approaches

**1. Union of confidence intervals (UCI)**: Assume gamma lies in a known interval [gamma_L, gamma_U]. For each gamma in this interval, compute the IV estimate of beta. Report the union of all confidence intervals across the range.

**2. Local-to-zero (LTZ)**: Treat gamma as a random variable with a known distribution (e.g., gamma ~ N(0, sigma^2_gamma)). The uncertainty about gamma inflates the standard error of beta.

**3. Prior specification**: Use a Bayesian approach with a prior on gamma. The posterior of beta incorporates uncertainty about the exclusion restriction.

### Practical Use

1. Start with gamma = 0 (standard IV) and report the baseline estimate.
2. Choose a range for gamma based on economic reasoning (e.g., the reduced-form coefficient on the instrument provides an upper bound on the direct effect).
3. Plot how the estimated beta and its confidence interval change as gamma varies.
4. Report the maximum |gamma| that preserves significance or the same sign as the baseline.
5. Discuss whether this threshold is plausible given the institutional setting.

## Masten and Poirier (2021) — Partial Identification with Sensitivity

### Framework

Masten and Poirier develop a sensitivity analysis framework based on partial identification. Instead of point-identifying a causal effect under untestable assumptions, they characterize the identified set (the set of parameter values consistent with the data and a relaxed set of assumptions).

### Key Idea

Parameterize departures from the identifying assumption (e.g., conditional independence, parallel trends, exclusion restriction) using a sensitivity parameter c.

- c = 0: the baseline assumption holds exactly, and the estimand is point-identified.
- c > 0: the assumption is violated by degree c, and the estimand is partially identified (lies in an interval).

The identified set grows with c, showing how the conclusion degrades as the assumption is relaxed.

### Application to Different Designs

**Selection on unobservables**: Bound the conditional mean of the outcome under treatment as a function of how far the unconfoundedness assumption fails.

**Difference-in-differences**: Allow the parallel trends assumption to be violated by c. The identified set for the ATT becomes an interval whose width depends on c and the data.

**IV**: Allow the exclusion restriction to fail by c (direct effect of instrument on outcome bounded by c).

### Practical Value

- Provides a unified sensitivity framework across research designs.
- Results are presented as breakdown points: the smallest c that overturns the conclusion.
- Easy to communicate: "the result is robust to violations of parallel trends up to c = 0.03 standard deviations per year."

## Breakpoint Analysis

### Concept

A breakpoint (or breakdown point) is the minimum amount of assumption violation required to change the qualitative conclusion (e.g., statistical significance, sign of the estimate).

Different sensitivity frameworks yield different breakpoint measures:
- Oster delta: the delta value at which the bias-adjusted estimate crosses zero.
- Conley gamma: the direct instrument-outcome effect at which the IV estimate becomes insignificant.
- Masten-Poirier c: the assumption violation magnitude at which the identified set includes zero.

### Reporting Best Practices

- Report the breakpoint alongside the main estimate.
- Calibrate the breakpoint against observable benchmarks. For example: "The unobserved confounder would need to explain 2.5 times as much variation as our richest control variable (parental income) to overturn the result."
- Compare breakpoints across specifications and samples.
- Present visual sensitivity plots: estimated effect (or confidence interval) as a function of the sensitivity parameter.

## Rosenbaum Bounds (Matching/Observational Studies)

### Framework

In the context of matching or propensity score methods, Rosenbaum (2002) asks: how much could a hidden bias (unobserved confounder) change the odds of treatment before the conclusion is overturned?

The sensitivity parameter Gamma represents the maximum ratio of treatment odds between two matched units that differ on an unobserved confounder:

1/Gamma <= [P(D=1|X,U) / P(D=0|X,U)] / [P(D=1|X,U') / P(D=0|X,U')] <= Gamma

At Gamma = 1, there is no hidden bias (perfect matching on all confounders). As Gamma increases, the bounds on the treatment effect widen.

### Reporting

- Report the Gamma value at which the result becomes insignificant.
- Calibrate: "A confounder that doubled the odds of treatment (Gamma = 2) would not overturn the finding."
- Higher Gamma breakpoints indicate more robust findings.

## E-Value (VanderWeele and Ding 2017)

The E-value quantifies the minimum strength of association (on the risk ratio scale) that an unmeasured confounder would need to have with both the treatment and the outcome (conditional on measured covariates) to explain away the observed effect.

**Computation**: For a risk ratio RR, the E-value is:

E = RR + sqrt(RR * (RR - 1))

**Interpretation**: "To explain away the observed risk ratio of 2.5, an unmeasured confounder would need to be associated with both the treatment and the outcome by a risk ratio of at least 4.2 each, above and beyond the measured covariates."

Originally developed for epidemiology but applicable to any setting with risk ratio or odds ratio outcomes.

## Practical Recommendations

1. **Always conduct sensitivity analysis** for the key identifying assumption. The specific method depends on the research design:
   - OLS with controls: Oster (2019) delta
   - IV: Conley et al. (2012) plausibly exogenous
   - DiD: Roth and Sant'Anna (2023) HonestDiD
   - Matching: Rosenbaum bounds
   - RD: placebo cutoffs and bandwidth sensitivity (built-in sensitivity)

2. **Calibrate sensitivity parameters** against observable benchmarks. Concrete comparisons ("1.5 times as important as parental education") are more persuasive than abstract numbers.
3. **Present sensitivity plots** showing how the estimate and confidence interval change as the sensitivity parameter varies.
4. **Report breakpoints** prominently. Readers should immediately see how fragile or robust the result is.
5. **Multiple methods**: When possible, apply more than one sensitivity framework. Concordance across methods strengthens the case.
6. **Be honest**: If the result is fragile, say so. Fragile results are informative; hiding fragility is not.

## Key References

- Oster, E. (2019). Unobservable selection and coefficient stability. Journal of Business and Economic Statistics.
- Altonji, J., Elder, T., and Taber, C. (2005). Selection on observed and unobserved variables. Journal of Political Economy.
- Conley, T., Hansen, C., and Rossi, P. (2012). Plausibly exogenous. Review of Economics and Statistics.
- Masten, M. and Poirier, A. (2021). Salvaging falsified instrumental variables models. Econometrica.
- Rosenbaum, P. (2002). Observational Studies, 2nd ed. Springer.
- VanderWeele, T. and Ding, P. (2017). Sensitivity analysis in observational research. Annals of Internal Medicine.
- Roth, J. and Sant'Anna, P. (2023). When is parallel trends sensitive to functional form? Econometrica.
