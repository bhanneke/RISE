# Panel Data Methods

## Overview

Panel data (longitudinal data) tracks the same units (individuals, firms, countries) across multiple time periods. The repeated observations allow researchers to control for unobserved time-invariant heterogeneity, which is the central advantage of panel methods over cross-sectional analysis.

Notation: Y_it denotes the outcome for unit i in period t. The standard panel model is:

Y_it = X_it * beta + alpha_i + gamma_t + epsilon_it

where alpha_i is unit-specific unobserved heterogeneity, gamma_t captures common time shocks, and epsilon_it is the idiosyncratic error.

## Fixed Effects (FE)

The fixed effects estimator controls for arbitrary time-invariant unobserved heterogeneity (alpha_i) by demeaning all variables within each unit.

**Within transformation**: Subtract unit-specific means from all variables:
(Y_it - Y_i_bar) = (X_it - X_i_bar) * beta + (epsilon_it - epsilon_i_bar)

Key properties:
- Eliminates all time-invariant confounders, observed and unobserved.
- Cannot estimate effects of time-invariant regressors (gender, birth cohort, etc.).
- Equivalent to including a dummy variable for each unit (LSDV), but computationally more efficient.
- Consistent under the assumption E[epsilon_it | X_i1, ..., X_iT, alpha_i] = 0 (strict exogeneity).

**Time fixed effects** (gamma_t) absorb common shocks affecting all units in a given period. Including both unit and time FE gives the "two-way fixed effects" (TWFE) model.

**Strict exogeneity assumption**: Current errors must be uncorrelated with past, present, and future values of X. This rules out feedback effects (where past outcomes affect current X) and lagged dependent variables. Violations lead to inconsistency.

## Random Effects (RE)

The random effects estimator treats alpha_i as a random variable uncorrelated with the regressors. It uses a GLS transformation that partially demeans the data.

Y_it - theta * Y_i_bar = (X_it - theta * X_i_bar) * beta + (1 - theta) * alpha_i + (epsilon_it - theta * epsilon_i_bar)

where theta depends on the variance ratio sigma^2_alpha / sigma^2_epsilon and the number of time periods T.

Key properties:
- More efficient than FE if the RE assumption holds.
- Can estimate effects of time-invariant regressors.
- Inconsistent if alpha_i is correlated with X_it (the typical concern in economics).
- Appropriate when units are randomly sampled from a larger population and there is no reason to expect correlation between unobservables and regressors (rare in observational economics).

## Hausman Test

Tests whether the RE estimator is consistent by comparing FE and RE coefficients:

H = (beta_FE - beta_RE)' * [Var(beta_FE) - Var(beta_RE)]^{-1} * (beta_FE - beta_RE)

Under H0 (RE is consistent), H is chi-squared with K degrees of freedom.

Interpretation:
- Rejection (large H): alpha_i is correlated with regressors. FE is consistent, RE is not. Use FE.
- Failure to reject: Both are consistent; RE is more efficient. Use RE.

Caveats:
- The test assumes correct specification of both models (homoskedasticity, no serial correlation in standard version).
- With clustered or heteroskedasticity-robust standard errors, use the robust version (Wooldridge 2010 or `xtoverid` in Stata).
- Low power in small samples. Failure to reject does not prove RE is valid.

## Correlated Random Effects (CRE)

The Mundlak (1978) / Chamberlain (1982) approach bridges FE and RE:

Y_it = X_it * beta + X_i_bar * gamma + alpha_i + epsilon_it

where X_i_bar is the unit-level mean of X. This is estimated as a RE model with group means added as regressors.

Properties:
- beta is numerically identical to the FE estimator.
- gamma captures the correlation between alpha_i and X_it.
- Can include time-invariant regressors (they go in alongside X_i_bar).
- Hausman test is equivalent to testing gamma = 0.
- Natural framework for combining FE-like within estimation with between variation for time-invariant variables.

## Clustered Standard Errors

With panel data, errors are typically serially correlated within units and heteroskedastic. OLS/GLS standard errors that ignore this are invalid.

**Cluster-robust standard errors** (clustering at the unit level):
- Allow arbitrary within-unit serial correlation and heteroskedasticity.
- Require "large N, small T" asymptotics (many units, few time periods) for consistency.
- The number of clusters must be large enough (typically 50+, though this depends on balance and leverage).

**With few clusters** (< 50 units):
- Cluster-robust SEs are downward biased.
- Use wild cluster bootstrap (Cameron, Gelbach, and Miller 2008).
- Or use bias-corrected cluster-robust variance estimators (Bell-McCaffrey, CR2/CR3).

**Two-way clustering**: When errors are correlated within both unit and time dimensions (e.g., state-year panels with both state and year shocks), use two-way clustering (Cameron, Gelbach, and Miller 2011). Implemented via `cluster2` in Stata or `vcovCL` with two-way clustering in R.

**Driscoll-Kraay standard errors**: Robust to cross-sectional dependence, heteroskedasticity, and serial correlation. Appropriate when the cross-sectional dimension N is large and errors are spatially correlated.

## Dynamic Panels: Arellano-Bond and Extensions

When the model includes a lagged dependent variable:

Y_it = rho * Y_{i,t-1} + X_it * beta + alpha_i + epsilon_it

**The problem**: FE (within transformation) creates correlation between the demeaned lagged dependent variable and the demeaned error term (Nickell bias). The bias is O(1/T), severe when T is small.

**Arellano-Bond (1991) / Difference GMM**:
- First-difference the equation to eliminate alpha_i.
- Use lagged levels (Y_{i,t-2}, Y_{i,t-3}, ...) as instruments for the differenced lagged dependent variable.
- GMM estimation with a growing instrument set.

**Blundell-Bond (1998) / System GMM**:
- Adds level equations to the differenced equations, using lagged differences as instruments for the level equation.
- More efficient than difference GMM, especially when the series is persistent (rho close to 1).
- The level equation requires an additional stationarity assumption on initial conditions.

**Practical issues with GMM panel estimators:**
- **Instrument proliferation**: With many time periods, the instrument count grows quadratically. Too many instruments overfit the endogenous variables, weakening the Hansen test. Collapse the instrument matrix or limit lag depth.
- **Hansen/Sargan test**: Test overidentifying restrictions. Low p-values suggest invalid instruments. But with many instruments, the test is weak (always fails to reject). Report the instrument count.
- **AR(2) test**: Serial correlation test on differenced residuals. AR(1) is expected (by construction); AR(2) indicates serial correlation in levels, which would invalidate instruments.
- **Rule of thumb**: Number of instruments should not exceed number of groups (Roodman 2009).

## Panel Unit Root Tests

With macro panels (long T, potentially non-stationary series):

- **Levin-Lin-Chu (LLC)**: Tests common unit root across all panels. Assumes cross-sectional independence. H0: all panels have a unit root.
- **Im-Pesaran-Shin (IPS)**: Allows heterogeneous autoregressive coefficients across panels. H0: all panels have a unit root. Alternative: some panels are stationary.
- **Fisher-type tests**: Combine p-values from individual ADF tests per panel. Flexible; allows unbalanced panels.
- **Pesaran CADF/CIPS**: Accounts for cross-sectional dependence by augmenting individual ADF regressions with cross-sectional averages.

With non-stationary panels, consider panel cointegration methods (Pedroni, Westerlund) or error correction models.

## First Differencing vs Fixed Effects

Both eliminate time-invariant heterogeneity. FD uses the transformation Y_it - Y_{i,t-1}; FE uses Y_it - Y_i_bar.

- Under strict exogeneity with serially uncorrelated errors: FE is more efficient.
- Under strict exogeneity with random walk errors: FD is more efficient.
- FD requires only sequential exogeneity (weaker than strict exogeneity).
- In practice, compare FE and FD results. Large discrepancies may indicate serial correlation or violations of strict exogeneity.

## Practical Checklist

1. Start with pooled OLS, then FE, then RE. Compare coefficients across specifications.
2. Run the Hausman test (robust version) to guide the FE vs RE choice.
3. Always cluster standard errors at the unit level for panel data. Consider two-way clustering if cross-sectional dependence is likely.
4. With few clusters (< 50), use wild cluster bootstrap.
5. Test for serial correlation in the idiosyncratic error (Wooldridge test).
6. If including a lagged dependent variable with small T, use Arellano-Bond or Blundell-Bond. Report AR(2) test and keep instrument count below number of groups.
7. For CRE: include unit means of time-varying regressors to combine within and between variation.
8. For long T panels: test for unit roots before running regressions in levels.
9. Report within R-squared for FE models (overall R-squared is misleading).
10. Consider the economic meaning of "within" vs "between" variation in your context.

## Key References

- Wooldridge, J. (2010). Econometric Analysis of Cross Section and Panel Data, 2nd ed. MIT Press.
- Arellano, M. and Bond, S. (1991). Some tests of specification for panel data. Review of Economic Studies.
- Blundell, R. and Bond, S. (1998). Initial conditions and moment restrictions in dynamic panel data models. Journal of Econometrics.
- Cameron, A. and Trivedi, P. (2005). Microeconometrics: Methods and Applications. Cambridge.
- Roodman, D. (2009). How to do xtabond2: An introduction to difference and system GMM in Stata. Stata Journal.
- Mundlak, Y. (1978). On the pooling of time series and cross section data. Econometrica.
