# Judge and Examiner Designs

## Core Idea

Judge (or examiner) designs exploit the quasi-random assignment of cases to decision-makers who vary in their treatment propensity. When cases are assigned to judges, patent examiners, disability adjudicators, or caseworkers through a process that is as-if random (conditional on time and location), the decision-maker's leniency serves as an instrument for the treatment they impose.

The instrument captures exogenous variation in treatment that arises not from the defendant's or applicant's characteristics but from the idiosyncratic preferences of the assigned decision-maker.

## Setup and Notation

- Unit i is assigned to decision-maker j
- Treatment D_i (e.g., incarceration, patent grant, disability award)
- Outcome Y_i (e.g., recidivism, firm innovation, labor supply)
- Decision-maker leniency: Z_j = propensity of judge j to assign treatment

The instrument is Z_j, measuring how much more or less likely judge j is to treat, relative to other judges handling similar cases.

## Instrument Construction

### Leave-Out Mean (Jackknife IV)

The standard instrument is the leave-out mean treatment rate of judge j:

Z_{ij} = (1 / (n_j - 1)) * sum_{i' != i, j(i') = j} D_{i'}

This excludes individual i's own treatment status to avoid mechanical correlation between the instrument and the endogenous variable.

**Why leave-out**: Including the own observation creates a mechanical first stage even with random assignment. The leave-out construction ensures the instrument reflects the judge's general tendency, not the specific case outcome.

### Residualized Leniency

When assignment is random conditional on covariates (court-by-time FE, case characteristics):

1. Regress D_i on case-level controls and court-by-time FE. Obtain residuals.
2. Compute the leave-out mean of these residuals for each judge.

This removes variation in judge treatment rates that reflects differences in case composition rather than true leniency differences.

### Handling Unbalanced Panels

Judges with few cases produce noisy leniency measures. Options:
- Exclude judges with fewer than a minimum number of cases (e.g., 50).
- Shrinkage estimators: Empirical Bayes estimates of judge leniency pull extreme estimates toward the overall mean.
- Weight by the number of cases per judge.

## Identification Assumptions

### 1. Conditional Random Assignment

Cases must be assigned to judges as-if randomly, conditional on observable case characteristics and court-by-time fixed effects.

**Testable implication**: Pre-determined case characteristics should be balanced across judges. Regress each covariate on judge fixed effects (conditional on court-by-time FE) and test for joint significance.

**Common assignment mechanisms**:
- Strict random rotation (e.g., cases assigned in sequence).
- Random draw from the pool of available judges that day.
- Alphabetical by defendant surname with rotating judge schedules.
- Within a court-year, assignment is effectively random even if the mechanism is not literally a lottery.

**Violations**:
- Specialization: some judges handle specific case types (drug cases, financial crimes).
- Judge shopping: attorneys select or manipulate which judge hears their case.
- Administrative overrides: complex cases assigned to senior judges.
- Transfers: cases reassigned after initial assignment.

### 2. Exclusion Restriction

The judge affects the outcome only through the treatment decision, not through any other channel.

**Potential violations**:
- Sentencing type and length: a strict judge may impose different sentence types (prison vs probation), not just more or less treatment.
- Deterrence: being assigned to a harsh judge may change behavior through fear, independent of the actual sentence.
- Bundled treatments: the judge's decision may affect multiple margins simultaneously (bail, conviction, sentencing, conditions).
- Ancillary orders: judges may impose complementary requirements (treatment programs, monitoring) correlated with their leniency.

**Mitigation**: Carefully define the treatment. If the instrument captures variation in multiple treatment margins, the IV estimate reflects a combination of effects. Use multi-valued treatment frameworks or focus on a specific margin.

### 3. Monotonicity

A stricter judge must be stricter for all types of cases, not just on average. Formally: if judge j is more likely to incarcerate than judge j' on average, then for every defendant type, P(D = 1 | j) >= P(D = 1 | j').

**Why it matters**: Without monotonicity, there are "defiers" (individuals who would be treated by the lenient judge but not the strict judge). With defiers, the standard LATE interpretation breaks down.

**Plausibility**: Monotonicity is more plausible when the treatment is binary and judges face the same decision (incarcerate or not) for all cases. It is less plausible when judges face multidimensional decisions or when the instrument conflates different treatment margins.

## Testing for Validity

### Covariate Balance

Regress pre-determined covariates on judge leniency (the leave-out instrument). No significant relationship should exist after conditioning on court-by-time FE.

Standard test: regress each covariate on the instrument and report coefficients. Joint F-test for all covariates.

### Frandsen, Lefgren, and Leslie (2023) Monotonicity Test

A formal test for the monotonicity assumption in judge designs.

**Intuition**: Under monotonicity, the distribution of potential outcomes conditional on the judge instrument should satisfy certain stochastic dominance conditions. Violations of these conditions imply the existence of defiers.

**Implementation**:
- Test whether the distribution of outcomes varies monotonically with judge strictness.
- The test examines whether complier potential outcome distributions cross, which would violate monotonicity.
- Available in Stata and R packages.

**Limitations**: The test has power against specific monotonicity violations but cannot detect all forms of non-monotonicity. Passing the test is necessary but not sufficient for monotonicity.

### First-Stage Heterogeneity

Estimate first-stage coefficients for different subgroups (by case type, defendant characteristics, severity). If leniency predicts treatment strongly for all subgroups with the same sign, this supports (but does not prove) monotonicity.

### Specification Tests

- **Overidentification**: With many judges, the model is heavily overidentified. The Sargan/Hansen J-test can detect some forms of instrument invalidity, though it has low power.
- **Leave-one-judge-out**: Re-estimate excluding each judge. Sensitivity of results to individual judges.
- **Split-sample**: Estimate leniency in one random half of each judge's cases; apply it as an instrument in the other half.

## Applications

### Criminal Justice

**Incarceration effects on recidivism**:
- Kling (2006): longer sentences increase post-release earnings for some groups.
- Mueller-Smith (2015): incarceration increases recidivism, with large effects for marginal defendants.
- Bhuller et al. (2020): incarceration reduces recidivism in Norway, where prison focuses on rehabilitation.

**Pre-trial detention**:
- Dobbie, Goldin, and Yang (2018): pre-trial detention increases guilty pleas and conviction rates, reduces future employment.
- Gupta, Hansman, and Frenchman (2016): cash bail assignment affects detention and downstream outcomes.

### Patent Examination

**Patent grant effects on innovation and firm outcomes**:
- Sampat and Williams (2019): gene patents do not reduce follow-on innovation.
- Farre-Mensa, Hegde, and Ljungqvist (2020): patent grants help startups raise funding and grow.

**Instrument**: Examiner grant rate (leave-out) instruments for whether a specific application is granted.

### Disability Insurance

**Effect of disability insurance receipt on labor supply**:
- Maestas, Mullen, and Strand (2013): DI allowance reduces labor force participation substantially.
- French and Song (2014): DI receipt effects on earnings and employment.

**Instrument**: Examiner or ALJ (Administrative Law Judge) allowance rate.

### Social Services and Child Welfare

**Foster care and child removal**:
- Doyle (2007, 2008): children on the margin of foster care placement have worse outcomes in foster care (delinquency, teen motherhood).

**Instrument**: Caseworker removal propensity.

### Asylum and Immigration

**Asylum grant decisions**:
- Judges vary substantially in asylum grant rates; assignment is quasi-random within courts.
- Used to study effects of legal status on economic integration.

## Many Judges and Weak Instruments

Judge designs typically have many instruments (one per judge or a continuous leniency measure). This creates specific econometric issues:

- **Many-instruments bias**: With hundreds of judges, 2SLS is biased. LIML, JIVE, or regularized estimators are preferred.
- **Leave-out estimation already addresses one source of many-instrument bias**, but does not fully resolve it when the number of judges is large relative to the sample.
- **UJIVE (Kolesar 2013)**: Unbiased jackknife IV estimator, particularly suitable for judge designs.
- **Post-LASSO IV**: Select a subset of judges with the strongest first stages using LASSO, then use them as instruments.

## Practical Checklist

1. Document the assignment mechanism. Explain why it is quasi-random.
2. Show covariate balance on pre-determined characteristics conditional on court-by-time FE.
3. Construct the leave-out instrument (residualized if needed).
4. Report the first-stage F-statistic. With many judges, use the effective F or judge-level regression.
5. Discuss and test monotonicity (Frandsen et al. test, subgroup first stages).
6. Discuss the exclusion restriction: through what channels does the judge affect outcomes?
7. Report both 2SLS and LIML/JIVE given the many-instruments setting.
8. Show robustness to dropping individual judges, especially outlier judges.
9. Report the complier characteristics (who are the marginal individuals affected by judge assignment).
10. Consider the specific LATE being estimated: effects for marginal cases, not infra-marginal.

## Key References

- Kling, J. (2006). Incarceration length, employment, and earnings. American Economic Review.
- Dobbie, W., Goldin, J., and Yang, C. (2018). The effects of pre-trial detention on conviction, future crime, and employment. American Economic Review.
- Maestas, N., Mullen, K., and Strand, A. (2013). Does disability insurance receipt discourage work? American Economic Review.
- Frandsen, B., Lefgren, L., and Leslie, E. (2023). Judging judge fixed effects. American Economic Review.
- Mogstad, M., Torgovitsky, A., and Walters, C. (2021). The causal interpretation of two-stage least squares with multiple instruments. American Economic Review.
- Kolesar, M. (2013). Estimation in an instrumental variables model with treatment effect heterogeneity. Working paper.
- Sampat, B. and Williams, H. (2019). How do patents affect follow-on innovation? Evidence from the human genome. American Economic Review.
