# Regression Discontinuity Design

## Core Idea

Regression discontinuity (RD) exploits a known threshold in a running variable (also called score, forcing variable, or assignment variable) that determines treatment assignment. Units just above and just below the cutoff are assumed to be comparable in all respects except treatment status, creating a local quasi-experiment at the cutoff.

RD is widely considered the most credible quasi-experimental design because the identification assumptions are partially testable and the design closely approximates a local randomized experiment.

## Sharp RD

In the sharp design, treatment is a deterministic function of the running variable:

D_i = 1(X_i >= c)

where X_i is the running variable and c is the cutoff. Every unit above the cutoff is treated; every unit below is untreated. The treatment effect at the cutoff is:

tau_SRD = lim_{x -> c+} E[Y | X = x] - lim_{x -> c-} E[Y | X = x]

This identifies the local average treatment effect (LATE) at the cutoff point X = c. It is not informative about effects away from the cutoff without additional assumptions.

## Fuzzy RD

In the fuzzy design, crossing the cutoff changes the probability of treatment but does not determine it perfectly:

lim_{x -> c+} P(D = 1 | X = x) != lim_{x -> c-} P(D = 1 | X = x)

The fuzzy RD estimand is:

tau_FRD = [lim E[Y | X = x from right] - lim E[Y | X = x from left]] / [lim P(D=1 | X = x from right) - lim P(D=1 | X = x from left)]

This is the ratio of the jump in the outcome to the jump in the treatment probability. It is interpretable as the LATE for compliers at the cutoff (units induced into treatment by crossing the threshold). Fuzzy RD is implemented as a local IV regression, with the running variable centered at the cutoff and the indicator 1(X >= c) as the instrument.

## Local Polynomial Estimation

RD estimates are obtained by fitting local polynomial regressions on each side of the cutoff separately.

**Local linear regression** (polynomial order p = 1):
- Fits a weighted linear regression on each side of the cutoff within a bandwidth h.
- The treatment effect is the difference in intercepts at the cutoff.
- Recommended as the default specification (Gelman and Imbens 2019 argue against higher-order polynomials in global fits).

**Bias-variance tradeoff:**
- Smaller bandwidth reduces bias (units are more comparable) but increases variance (fewer observations).
- Larger bandwidth reduces variance but introduces bias from extrapolation.

**Kernel weighting:**
- Observations closer to the cutoff receive more weight.
- Common kernels: triangular (optimal for boundary estimation), Epanechnikov, uniform.
- Triangular kernel is the MSE-optimal choice for RD at boundary points.

## Bandwidth Selection

### Imbens and Kalyanaraman (2012)
- MSE-optimal bandwidth for local linear RD.
- Minimizes the integrated MSE of the treatment effect estimator.
- Original standard choice; now largely superseded by CCT.

### Calonico, Cattaneo, and Titiunik (2014, 2020) - CCT
- Bias-corrected RD estimator with robust confidence intervals.
- Uses an MSE-optimal bandwidth for point estimation and a separate (typically larger) bandwidth for bias correction.
- Accounts for the bias introduced by local polynomial approximation.
- Standard in current applied work; implemented in `rdrobust` (R, Stata, Python).

**Practical guidance:**
- Report results at the MSE-optimal bandwidth from CCT.
- Show robustness to bandwidth choices: half the optimal, 1.5x optimal, and double the optimal.
- Use the bias-corrected confidence intervals from `rdrobust`, not conventional ones.
- With discrete running variables, see Cattaneo, Idrobo, and Titiunik (2020) for adapted methods.

## Validity Tests

### McCrary (2008) Density Test
- Tests for manipulation of the running variable around the cutoff.
- If units can precisely sort above or below the cutoff, the RD design is invalid (endogenous selection).
- The test checks for a discontinuity in the density of the running variable at the cutoff.
- A significant jump in density suggests manipulation.
- Modern implementation: Cattaneo, Jansson, and Ma (2020) `rddensity` package provides improved density tests.

**When to worry about manipulation:**
- Running variable is self-reported or easily manipulated (test scores when retaking is easy).
- Institutional knowledge suggests agents can game the threshold.
- Bunching at the cutoff is visible in histograms.

**When manipulation is less concerning:**
- Running variable is determined before agents know the cutoff.
- Running variable is difficult to manipulate precisely (birth weight, vote shares).

### Covariate Balance at the Cutoff
- Pre-determined covariates should not show discontinuities at the cutoff.
- Run the RD specification using each covariate as the outcome. No significant jumps expected.
- This is the RD analogue of balance tests in randomized experiments.
- Failure of covariate balance suggests either manipulation or a confounding discontinuity.

### Placebo Cutoffs
- Estimate the RD at fake cutoff values away from the true cutoff.
- The treatment effect should be zero at placebo cutoffs.
- Helps assess whether the outcome function is smooth away from the cutoff.

### Placebo Outcomes
- Test outcomes that should not be affected by treatment.
- A discontinuity in a placebo outcome suggests a confounding discontinuity at the cutoff.

## Donut Hole RD

When observations very close to the cutoff are subject to manipulation or heaping:
- Exclude observations within a small window around the cutoff (the "donut").
- Re-estimate using only observations outside the donut but within the bandwidth.
- The donut should be motivated by institutional knowledge of manipulation, not chosen to obtain desired results.
- Report results with and without the donut for transparency.

Limitations:
- The estimand changes (no longer the effect at the cutoff itself).
- Requires extrapolation to the cutoff from further away, increasing reliance on functional form.
- Should be treated as a robustness check rather than the primary specification.

## RD-Specific Pitfalls

**Global polynomial fitting**: Fitting high-order polynomials to all data (not local) produces misleading results. Gelman and Imbens (2019) show global polynomial RD estimates are sensitive to polynomial order, have poor coverage, and can generate wide confidence intervals with incorrect coverage. Use local polynomial estimation instead.

**Discrete running variables**: When the running variable takes few unique values, local polynomial methods may perform poorly. Mass points create complications for bandwidth selection and inference. Use methods from Cattaneo, Idrobo, and Titiunik (2020) for discrete running variables.

**Multiple cutoffs and scores**: When different cutoffs apply to different subgroups, normalize the running variable (subtract the relevant cutoff) to pool observations. With multiple running variables (e.g., passing both a math and reading threshold), use the geographic/multivariate RD framework from Cattaneo et al.

**Treatment effect heterogeneity**: The RD estimate is local to the cutoff. It may differ substantially from the ATE. Explore heterogeneity by estimating the RD separately for subgroups defined by pre-treatment covariates.

## Practical Checklist

1. Plot the raw data: outcome against running variable with the cutoff marked. Use binned scatter plots (evenly-spaced or quantile-spaced bins).
2. Run McCrary/rddensity test for manipulation of the running variable. Show the density histogram.
3. Test covariate balance at the cutoff for all available pre-treatment covariates.
4. Estimate the RD using `rdrobust` with default (MSE-optimal) bandwidth and triangular kernel.
5. Report bias-corrected estimates and robust confidence intervals.
6. Show robustness to bandwidth choice (0.5h, 0.75h, h, 1.25h, 1.5h, 2h).
7. Show robustness to polynomial order (local linear and local quadratic).
8. Test placebo cutoffs and placebo outcomes.
9. If manipulation is a concern, report donut hole estimates.
10. For fuzzy RD, report both the first stage (jump in treatment probability) and the reduced form (jump in outcome) alongside the fuzzy RD estimate.

## Key References

- Cattaneo, M., Idrobo, N., and Titiunik, R. (2020). A Practical Introduction to Regression Discontinuity Designs (Elements in Quantitative and Computational Methods). Cambridge.
- Calonico, S., Cattaneo, M., and Titiunik, R. (2014). Robust nonparametric confidence intervals for regression-discontinuity designs. Econometrica.
- Imbens, G. and Lemieux, T. (2008). Regression discontinuity designs: A guide to practice. Journal of Econometrics.
- Lee, D. and Lemieux, T. (2010). Regression discontinuity designs in economics. Journal of Economic Literature.
- McCrary, J. (2008). Manipulation of the running variable in the regression discontinuity design. Journal of Econometrics.
- Gelman, A. and Imbens, G. (2019). Why high-order polynomials should not be used in regression discontinuity designs. Journal of Business and Economic Statistics.
