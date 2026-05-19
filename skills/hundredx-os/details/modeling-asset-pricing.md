# Asset Pricing and Factor Models

## Overview

Asset pricing studies why different securities earn different average returns. The central question: are return differences compensation for risk, or evidence of mispricing? The field operates through two main empirical approaches: cross-sectional regressions (Fama-MacBeth) and portfolio sorts.

## Theoretical Foundations

### Stochastic Discount Factor (SDF) Framework

All asset pricing models can be written as:

E[M * R_i] = 1  (for gross returns)
E[M * R_i^e] = 0  (for excess returns)

where M is the stochastic discount factor (pricing kernel). Different models correspond to different specifications of M.

- CAPM: M = a - b * R_m
- ICAPM: M = function of state variables
- Consumption CAPM: M = beta * (C_{t+1}/C_t)^(-gamma)

### Risk Premia

For any factor f:
E[R_i^e] = beta_i * lambda_f

- beta_i: exposure of asset i to factor f (from time-series regression)
- lambda_f: price of risk for factor f (estimated cross-sectionally)

## Factor Models

### CAPM (Sharpe 1964, Lintner 1965)

E[R_i] - R_f = beta_i * (E[R_m] - R_f)

- Single factor: the market portfolio.
- beta_i = Cov(R_i, R_m) / Var(R_m).
- Empirically rejected: the security market line is too flat (low-beta stocks earn more than predicted, high-beta stocks earn less).

### Fama-French Three-Factor (1993)

R_it - R_ft = alpha_i + beta_i * MKT_t + s_i * SMB_t + h_i * HML_t + epsilon_it

- MKT: market excess return.
- SMB (Small Minus Big): return spread between small-cap and large-cap portfolios.
- HML (High Minus Low): return spread between high book-to-market (value) and low book-to-market (growth) portfolios.

### Carhart Four-Factor (1997)

Adds UMD (Up Minus Down) momentum factor:

R_it - R_ft = alpha_i + beta_i * MKT_t + s_i * SMB_t + h_i * HML_t + u_i * UMD_t + epsilon_it

### Fama-French Five-Factor (2015)

Adds profitability and investment:

R_it - R_ft = alpha_i + b_i*MKT + s_i*SMB + h_i*HML + r_i*RMW + c_i*CMA + epsilon_it

- RMW (Robust Minus Weak): profitability factor.
- CMA (Conservative Minus Aggressive): investment factor.
- HML becomes redundant in many tests when RMW and CMA are included.

### q-Factor Model (Hou-Xue-Zhang, 2015)

R_it - R_ft = alpha_i + beta_i*MKT + s_i*ME + r_i*ROE + c_i*IA + epsilon_it

- ME: size factor.
- ROE: return on equity factor (profitability).
- IA: investment-to-assets factor.
- Motivated by q-theory of investment.

### Other Notable Models
- **Stambaugh-Yuan (2017)**: mispricing factors (management + performance).
- **Daniel-Hirshleifer-Sun (2020)**: behavioral factors (PEAD + financing).
- **Barillas-Shanken (2018)**: model comparison framework using Bayesian methods.

## Factor Data Sources

- **Ken French Data Library**: kenfrencharialibrary (Fama-French factors, industry portfolios, anomaly sorts). Free, updated monthly.
- **AQR Data Library**: additional factors (BAB, QMJ, time-series momentum).
- **WRDS**: CRSP for stock returns, Compustat for accounting data.

```python
import pandas_datareader.data as web

# Fama-French factors from Ken French library
ff3 = web.DataReader('F-F_Research_Data_Factors_daily', 'famafrench', start='2000-01-01')[0]
ff5 = web.DataReader('F-F_Research_Data_5_Factors_2x3_daily', 'famafrench', start='2000-01-01')[0]
mom = web.DataReader('F-F_Momentum_Factor_daily', 'famafrench', start='2000-01-01')[0]
```

## Fama-MacBeth Regressions

Two-pass procedure to estimate factor risk premia:

### Pass 1: Time-Series Regressions
For each asset i, regress excess returns on factors to get beta estimates:

R_it^e = alpha_i + beta_i' * F_t + epsilon_it

### Pass 2: Cross-Sectional Regressions
Each period t, regress cross-section of returns on estimated betas:

R_it^e = gamma_0t + gamma_1t * beta_hat_i + eta_it

### Inference
- lambda_hat = (1/T) * Sum(gamma_t) — time-series average of cross-sectional slopes.
- Standard error: s.e.(lambda_hat) = std(gamma_t) / sqrt(T).
- This automatically accounts for cross-sectional correlation in returns.

### Shanken (1992) Correction
Betas are estimated with error. The errors-in-variables problem biases Fama-MacBeth standard errors downward.

Corrected variance: Var(lambda_hat)_corrected = Var(lambda_hat)_FM * (1 + lambda' * Sigma_f^{-1} * lambda) + Sigma_f / T

where Sigma_f is the factor covariance matrix.

```python
from linearmodels.asset_pricing import TradedFactorModel, LinearFactorModel

# Using linearmodels
model = TradedFactorModel(portfolios=portfolio_returns, factors=factor_returns)
result = model.fit()
print(result.summary)

# Or manual Fama-MacBeth
import statsmodels.api as sm

# Pass 1: estimate betas (rolling or full-sample)
betas = {}
for asset in assets:
    reg = sm.OLS(returns[asset], sm.add_constant(factors)).fit()
    betas[asset] = reg.params[1:]  # exclude intercept

beta_df = pd.DataFrame(betas).T

# Pass 2: cross-sectional regressions each period
gammas = []
for t in returns.index:
    y = returns.loc[t]
    X = sm.add_constant(beta_df)
    reg = sm.OLS(y, X).fit()
    gammas.append(reg.params)

gammas = pd.DataFrame(gammas)
lambda_hat = gammas.mean()
lambda_se = gammas.std() / np.sqrt(len(gammas))
t_stats = lambda_hat / lambda_se
```

## Portfolio Sorts

### Single Sorts
1. At the end of each month (or June for annual sorts), sort stocks into quantile portfolios based on a characteristic (e.g., size, B/M, momentum).
2. Compute value-weighted or equal-weighted returns for each portfolio over the next month (or year).
3. Form a long-short portfolio: top quantile minus bottom quantile.
4. Test whether the long-short portfolio earns a significant alpha after controlling for known factors.

### Double Sorts (Independent)
1. Sort stocks independently by two characteristics into quantiles.
2. Intersect to form NxM portfolios.
3. Compute average returns for each cell.
4. Controls for the second characteristic when examining the first.

### Double Sorts (Dependent/Sequential)
1. First sort by the control variable into quantiles.
2. Within each quantile, sort by the variable of interest.
3. Average across the first sort to get returns conditional on the variable of interest, controlling for the first.

### Breakpoints
- **NYSE breakpoints**: Use only NYSE stocks for breakpoint computation. This avoids micro-cap stocks (which dominate CRSP by count) from skewing the sort.
- **Decile vs quintile**: Quintiles are standard. Deciles provide more granularity but may have too few stocks per portfolio in small samples.

## Alpha Tests

### GRS Test (Gibbons-Ross-Shanken, 1989)

Tests whether all intercepts (alphas) in a set of time-series regressions are jointly zero:

GRS = (T/N) * ((T-N-K)/(T-K-1)) * alpha' * Sigma^{-1} * alpha / (1 + mu_f' * Omega_f^{-1} * mu_f)

where:
- T: number of time periods
- N: number of test assets
- K: number of factors
- Sigma: residual covariance matrix
- mu_f, Omega_f: factor means and covariance

Under H0 (all alphas = 0), GRS ~ F(N, T-N-K).

**Interpretation**: A significant GRS test means the factor model fails to price the test assets. But GRS has low power with many test assets or short samples.

```python
from linearmodels.asset_pricing import TradedFactorModel

model = TradedFactorModel(portfolios=test_portfolios, factors=factors)
result = model.fit()
print(f"GRS statistic: {result.grs_statistic:.3f}")
print(f"GRS p-value: {result.grs_pvalue:.4f}")
```

### Spanning Tests

Test whether adding new factors improves the pricing of test assets beyond existing factors. Regress candidate factor on existing factors; if the intercept is significant, the new factor spans risks not captured by the existing model.

## GMM Estimation of Asset Pricing Models

For non-traded factor models (consumption, macro factors):

### Moment Conditions
E[M * R_i^e] = 0 for all test assets i

where M = 1 - b' * (f - E[f]) is linear in factors.

### GMM Procedure
1. Stack N moment conditions: g_T(b) = (1/T) * Sum(M_t * R_t^e).
2. First-stage GMM: W = I (identity weighting).
3. Optimal GMM: W = S^{-1} where S is the long-run covariance of moment conditions.
4. J-test (Hansen, 1982): T * g_T' * W * g_T ~ chi^2(N - K) tests overidentifying restrictions.

### Hansen-Jagannathan Distance

HJ = min_b sqrt(g_T' * E[R * R']^{-1} * g_T)

Measures the maximum pricing error of the model, scaled by the second moment matrix of returns. Allows comparison across models with different numbers of factors.

## Cross-Sectional Predictability

### Return Predictors (Anomalies)
Characteristics that predict the cross-section of returns:
- Size, value (B/M), momentum, profitability, investment, accruals, asset growth, idiosyncratic volatility, betting-against-beta, quality, etc.
- Harvey-Liu-Zhu (2016): over 300 factors documented. Multiple testing is a serious concern.

### Multiple Testing Corrections
- Bonferroni: divide significance level by number of tests (conservative).
- Holm-Bonferroni: step-down procedure (less conservative).
- Benjamini-Hochberg: controls false discovery rate (FDR).
- Harvey-Liu-Zhu (2016): t-stat threshold of ~3.0 (not 2.0) for new anomalies.
- Bootstrapped critical values: account for cross-correlation among anomalies.

### Fama-MacBeth with Characteristics
Instead of estimated betas, use firm characteristics directly:

R_{i,t+1}^e = gamma_0t + gamma_1t * Char_it + eta_it

This is essentially a cross-sectional regression of next-period returns on current characteristics. Avoids the errors-in-variables problem of estimated betas.

## Practical Checklist

1. **Define test assets**: 25 FF portfolios (5x5 size/value), industry portfolios, or individual stocks. Choice matters for power.
2. **Factor construction**: Follow standard methodology (Fama-French conventions, NYSE breakpoints, value-weighted).
3. **Sample period**: At least 30 years for monthly data. Check subperiod stability.
4. **Time-series regressions**: Use OLS with Newey-West standard errors (or simple OLS if factors are well-behaved). Report alpha, betas, R^2.
5. **Fama-MacBeth**: Report time-series average of cross-sectional slopes with Newey-West (or Shanken-corrected) standard errors.
6. **GRS test**: Report GRS statistic, p-value, and average absolute alpha.
7. **Portfolio sorts**: Use NYSE breakpoints, value-weighted returns, and report both VW and EW for robustness.
8. **Long-short portfolio**: Report mean return, alpha (FF3/FF5), Sharpe ratio, and max drawdown.
9. **Multiple testing**: If testing multiple anomalies, apply FDR correction or use t-stat > 3.0 threshold.
10. **Economic magnitude**: Report in basis points per month or percent per year. Discuss transaction costs and capacity.
11. **Out-of-sample**: Test in holdout period, international markets, or pre-discovery sample.
12. **Robustness**: Micro-cap exclusion (NYSE price > $5 or ME > 20th percentile), winsorization (1%/99%), subperiods, alternative factor models.

## Key References

- Fama, E.F. and French, K.R. (1993). Common risk factors in the returns on stocks and bonds. Journal of Financial Economics.
- Fama, E.F. and French, K.R. (2015). A five-factor asset pricing model. Journal of Financial Economics.
- Fama, E.F. and MacBeth, J.D. (1973). Risk, return, and equilibrium: Empirical tests. Journal of Political Economy.
- Carhart, M.M. (1997). On persistence in mutual fund performance. Journal of Finance.
- Hou, K., Xue, C., and Zhang, L. (2015). Digesting anomalies: An investment approach. Review of Financial Studies.
- Gibbons, M.R., Ross, S.A., and Shanken, J. (1989). A test of the efficiency of a given portfolio. Econometrica.
- Shanken, J. (1992). On the estimation of beta-pricing models. Review of Financial Studies.
- Cochrane, J.H. (2005). Asset Pricing, revised ed. Princeton University Press.
- Harvey, C.R., Liu, Y., and Zhu, H. (2016). ... and the cross-section of expected returns. Review of Financial Studies.
