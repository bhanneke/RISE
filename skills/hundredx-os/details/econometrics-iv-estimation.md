# Instrumental Variables Estimation

## Core Problem

OLS is inconsistent when an endogenous regressor is correlated with the error
term. Sources: omitted variables, simultaneity, measurement error. IV methods
resolve this by isolating exogenous variation through instruments.

## 2SLS

1. **First stage**: X = pi_0 + pi_1 * Z + pi_2 * W + v
2. **Second stage**: Y = beta_0 + beta_1 * X_hat + beta_2 * W + epsilon

- Never run two separate OLS regressions manually (SEs will be wrong).
- Use robust SEs or GMM-based estimators with heteroskedasticity.

## First-Stage Diagnostics

- **Staiger-Stock rule**: F > 10 (conventional, non-robust F, single
  endogenous variable).
- **Effective F (Olea-Pflueger 2013)**: Robust to heteroskedasticity and
  clustering. Threshold depends on desired max bias or size distortion.
- **Sanderson-Windmeijer (2016)**: Conditional F for multiple endogenous
  regressors. Test each individually.

Always report the first-stage F. A weak first stage undermines all IV inference.

## Weak Instruments

When instruments are weakly correlated with the endogenous variable:
- 2SLS is biased toward OLS (bias ~ 1/F).
- Confidence intervals have incorrect coverage.
- 2SLS may have no finite moments.

**Remedies:**
- **LIML**: Less biased than 2SLS under weak instruments. Approximately
  median-unbiased. Preferred when F < 20.
- **Fuller estimator**: Modified LIML with finite moments. Fuller(1)
  minimizes MSE; Fuller(4) minimizes bias.
- **Anderson-Rubin test**: Valid inference regardless of instrument strength.
  Confidence sets may be empty or unbounded.
- **CLR test (Moreira 2003)**: More powerful than AR with correct size.
- **tF procedure (Lee et al. 2022)**: Adjusts Wald t-test critical values
  based on first-stage F. Simple to implement.
- **JIVE**: Leave-one-out fitted values in first stage. Reduces
  many-instruments bias.

## Exclusion Restriction

1. **Relevance**: Cov(Z, X) != 0 (testable via first stage)
2. **Exclusion**: Cov(Z, epsilon) = 0 (not directly testable)

Strategies for arguing exclusion:
- Articulate the causal channel explicitly.
- Show instrument is uncorrelated with observable determinants (covariate
  balance).
- Falsification: test for direct effects in subsamples where first stage
  is zero.
- Sensitivity: Conley et al. (2012) plausibly exogenous bounds.

## Overidentification Tests

- **Sargan test**: Under homoskedasticity, Chi-squared with (L - K) df.
- **Hansen J test**: Robust to heteroskedasticity.
- Low power in finite samples. Failure to reject does not prove validity.
  If all instruments violate exclusion in the same direction, the test
  will not detect it.

## IV Strategy Catalog

### Shift-Share / Bartik
B_i = sum_k s_{ik} * g_k (local shares x national shifts). Requires
exogenous shares (GPSS 2020) OR exogenous shifts (BHJ 2022). See
dedicated shift-share skill for details.

### Judge / Examiner Designs
Leave-out mean of decision-maker's treatment rate as instrument. Requires
conditional random assignment + monotonicity. See dedicated judge-designs
skill.

### Distance Instruments
Geographic distance to facility creates cost-of-access variation. Concern:
residential sorting. Mitigate with historical/pre-determined distances.

### Policy Variation
Cross-jurisdictional or over-time variation in laws/regulations. Concerns:
policy endogeneity, simultaneous changes, selective migration.

### Lottery-Based
Draft lotteries, school lotteries, housing voucher lotteries. Clean
randomization but identifies LATE for compliers.

### Biological / Genetic
Twin births for family size, Mendelian randomization. Concerns: pleiotropy,
population stratification, dynastic effects.

### Weather / Environmental
Rainfall, temperature, natural disasters as instruments for
weather-sensitive variables. Concern: weather affects many outcomes
simultaneously.

## Practical Checklist

1. Report first-stage regression with F-statistic (robust or effective F).
2. Report both OLS and IV estimates. Large differences suggest endogeneity;
   IV >> OLS may indicate LATE vs ATE or weak instrument bias.
3. If overidentified, report Hansen J (interpret cautiously).
4. With F < 10, report LIML alongside 2SLS. Consider AR confidence sets.
5. Argue exclusion restriction explicitly. Show covariate balance.
6. If plausibly but not certainly exogenous, apply Conley et al. bounds.
7. Report reduced-form estimates (Z on Y). Valid even if first stage is weak.
8. Discuss what LATE the IV identifies. With heterogeneous effects, 2SLS
   estimates a complier-weighted average.

## Key References

- Angrist & Pischke (2009). Mostly Harmless Econometrics.
- Stock & Yogo (2005). Testing for weak instruments.
- Andrews, Stock & Sun (2019). Weak instruments in IV regression. Ann Rev Econ.
- Lee, McCrary, Moreira & Porter (2022). Valid t-ratio inference for IV. AER.
- Mogstad, Torgovitsky & Walters (2021). Causal interpretation of 2SLS. AER.
