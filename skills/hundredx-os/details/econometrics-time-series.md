# Time Series Econometrics

## Overview

Time series methods model the temporal dependence structure in financial and economic data. The core challenge is distinguishing genuine predictability from spurious correlation induced by persistence, non-stationarity, or structural breaks.

## Stationarity and Unit Root Tests

A time series is (weakly) stationary if its mean, variance, and autocovariances are constant over time. Most financial prices are non-stationary (unit root); returns are typically stationary.

### Testing for Unit Roots

**Augmented Dickey-Fuller (ADF)**:
- H0: Unit root (non-stationary). H1: Stationary.
- Include sufficient lags to whiten residuals (use AIC/BIC for lag selection).
- Include intercept; add trend only if the series has a visible trend under the alternative.
- Low power against near-unit-root alternatives.

**Phillips-Perron (PP)**:
- Non-parametric correction for serial correlation (Newey-West).
- Same null as ADF but more robust to heteroskedasticity.
- Can over-reject in small samples with negative MA components.

**KPSS (Kwiatkowski-Phillips-Schmidt-Shin)**:
- H0: Stationary. H1: Unit root.
- Use jointly with ADF: if ADF rejects and KPSS does not reject, conclude stationarity. If both reject or neither rejects, the series may be fractionally integrated.

**Zivot-Andrews / Lee-Strazicich**:
- Unit root tests allowing for structural breaks.
- Use when you suspect a regime change (policy shift, crisis).

### Practical Rules
- Always plot the series first. Visual inspection catches most issues.
- Test in levels and first differences.
- For financial prices: work in log returns (continuously compounded).
- For macro series: test whether first-differencing or detrending is appropriate.

## ARIMA Models

ARIMA(p, d, q): AutoRegressive Integrated Moving Average.
- p: AR order (number of lagged values of y)
- d: Integration order (number of differences to achieve stationarity)
- q: MA order (number of lagged error terms)

### Identification
1. Check stationarity (unit root tests). Set d accordingly (usually d=0 for returns, d=1 for prices).
2. Examine ACF and PACF of the stationary series:
   - ACF cuts off at lag q, PACF decays → MA(q)
   - PACF cuts off at lag p, ACF decays → AR(p)
   - Both decay → ARMA(p,q)
3. Use information criteria (AIC, BIC) to select p, q. BIC penalizes complexity more.

### Estimation
```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(y, order=(p, d, q))
results = model.fit()
print(results.summary())
```

### Diagnostics
- Ljung-Box test on residuals (H0: no autocorrelation). Test at multiple lag lengths.
- Jarque-Bera test for normality of residuals.
- Plot residual ACF — should show no significant spikes.
- Check for ARCH effects in residuals (Engle's LM test) → if present, use GARCH.

## GARCH Models

Generalized Autoregressive Conditional Heteroskedasticity. Models time-varying volatility — the defining feature of financial return series (volatility clustering).

### GARCH(1,1)

The workhorse model:

r_t = mu + epsilon_t
epsilon_t = sigma_t * z_t,  z_t ~ N(0,1) or t-distributed
sigma_t^2 = omega + alpha * epsilon_{t-1}^2 + beta * sigma_{t-1}^2

- omega > 0, alpha >= 0, beta >= 0
- alpha + beta < 1 for stationarity (unconditional variance = omega / (1 - alpha - beta))
- alpha captures shock impact; beta captures persistence
- Typical financial data: alpha ~ 0.05-0.10, beta ~ 0.85-0.95

```python
from arch import arch_model

model = arch_model(returns, vol='Garch', p=1, q=1, dist='t')
results = model.fit(disp='off')
print(results.summary())

# Conditional volatility
vol = results.conditional_volatility

# Standardized residuals
std_resid = results.std_resid
```

### Extensions

**EGARCH (Nelson, 1991)**: Captures leverage effect (negative returns increase volatility more than positive returns of equal magnitude).

log(sigma_t^2) = omega + alpha * (|z_{t-1}| - E|z_{t-1}|) + gamma * z_{t-1} + beta * log(sigma_{t-1}^2)

- gamma < 0 indicates leverage effect.
- Log specification ensures sigma^2 > 0 without parameter constraints.

**GJR-GARCH (Glosten-Jagannathan-Runkle, 1993)**: Alternative leverage specification.

sigma_t^2 = omega + (alpha + gamma * I_{t-1}) * epsilon_{t-1}^2 + beta * sigma_{t-1}^2

- I_{t-1} = 1 if epsilon_{t-1} < 0. gamma > 0 implies leverage.

**GARCH-in-Mean**: Adds conditional variance to the mean equation.

r_t = mu + delta * sigma_t^2 + epsilon_t

- Tests risk-return tradeoff. delta > 0 means higher volatility commands higher expected return.

```python
# EGARCH
model = arch_model(returns, vol='EGARCH', p=1, q=1)

# GJR-GARCH
model = arch_model(returns, vol='Garch', p=1, o=1, q=1)  # o=1 adds asymmetry
```

### Distribution Assumptions
- Normal: default, but financial returns have fat tails.
- Student-t: `dist='t'` — recommended default for financial data.
- Skewed-t: `dist='skewt'` — captures both fat tails and asymmetry.
- GED: `dist='ged'` — Generalized Error Distribution.

### GARCH Diagnostics
- Ljung-Box on squared standardized residuals (should show no remaining ARCH effects).
- QQ-plot of standardized residuals against assumed distribution.
- News impact curve (plot sigma^2 as function of epsilon_{t-1}).
- Compare AIC/BIC across GARCH variants.

## VAR Models

Vector Autoregression: models multiple time series jointly. Each variable is regressed on its own lags and lags of all other variables.

Y_t = c + A_1 * Y_{t-1} + ... + A_p * Y_{t-p} + u_t

where Y_t is a K-dimensional vector.

### Identification and Estimation
1. Test each series for unit roots. If I(1), consider VECM instead.
2. Select lag order p using AIC/BIC/HQ on the VAR in levels (or differences if non-stationary).
3. Estimate by OLS equation-by-equation (equivalent to SUR when all equations have the same regressors).

```python
from statsmodels.tsa.api import VAR

model = VAR(data[['y1', 'y2', 'y3']])
results = model.fit(maxlags=8, ic='bic')
print(results.summary())
```

### Granger Causality
- X Granger-causes Y if past values of X improve prediction of Y beyond Y's own past.
- Test via F-test on excluded lags in the Y equation.
- NOT causal in the structural sense — purely predictive.

```python
results.test_causality('y1', causing='y2', kind='f')
```

### Impulse Response Functions (IRFs)
- Trace the dynamic response of each variable to a one-unit shock in another.
- **Ordering matters** for Cholesky decomposition: variable ordered first is assumed contemporaneously exogenous.
- Report confidence bands (bootstrap or asymptotic).

```python
irf = results.irf(periods=20)
irf.plot(orth=True)  # Orthogonalized (Cholesky) IRFs
```

### Structural VAR (SVAR)
- Imposes economic restrictions on the contemporaneous impact matrix.
- Short-run restrictions (Cholesky or custom zero restrictions).
- Long-run restrictions (Blanchard-Quah: permanent vs transitory shocks).
- Sign restrictions (Uhlig): identify shocks by the sign of responses.

### Forecast Error Variance Decomposition (FEVD)
- Decomposes the forecast error variance of each variable into contributions from each shock.
- Complements IRFs: shows relative importance of shocks.

## Cointegration

Two or more I(1) series are cointegrated if a linear combination is I(0). The series share a common stochastic trend and cannot drift apart indefinitely.

### Engle-Granger Two-Step
1. Estimate cointegrating regression: y_t = alpha + beta * x_t + u_t (OLS)
2. Test residuals u_t for unit root (ADF with Engle-Granger critical values, NOT standard ADF tables)
3. If cointegrated, estimate ECM: Delta(y_t) = gamma * u_{t-1} + lagged differences + e_t
4. gamma < 0 is the error correction speed.

Limitations: only finds one cointegrating relationship; normalization matters; poor small-sample properties.

### Johansen Test
- Tests for number of cointegrating vectors among K variables.
- Trace test and maximum eigenvalue test.
- Can find 0, 1, ..., K-1 cointegrating relationships.
- Specify deterministic components (intercept/trend in cointegrating equation vs short-run).

```python
from statsmodels.tsa.vector_ar.vecm import coint_johansen

result = coint_johansen(data, det_order=0, k_ar_diff=2)
print(result.trace_stat)
print(result.trace_stat_crit_vals)  # 90%, 95%, 99%
```

### VECM (Vector Error Correction Model)

If cointegration exists, estimate VECM rather than VAR in differences:

Delta(Y_t) = alpha * beta' * Y_{t-1} + Gamma_1 * Delta(Y_{t-1}) + ... + u_t

- beta: cointegrating vectors (long-run equilibrium)
- alpha: adjustment coefficients (speed of correction)
- Gamma: short-run dynamics

```python
from statsmodels.tsa.vector_ar.vecm import VECM

model = VECM(data, k_ar_diff=2, coint_rank=1)
results = model.fit()
```

## HAC Standard Errors

With time series data, OLS standard errors are inconsistent under heteroskedasticity and autocorrelation. Use Heteroskedasticity and Autocorrelation Consistent (HAC) estimators.

**Newey-West**: The standard choice for time series regressions.

```python
import statsmodels.api as sm

model = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': L})
```

**Bandwidth selection**: Newey-West with automatic bandwidth (Andrews 1991) or fixed rule L = floor(4 * (T/100)^(2/9)).

**When to use**: Always in time series regressions unless you have strong reasons to believe errors are homoskedastic and serially uncorrelated (rare in finance).

## Forecast Evaluation

### In-Sample vs Out-of-Sample
- In-sample fit (R^2, AIC) overstates predictive ability.
- Use expanding or rolling window out-of-sample forecasts.
- Compare against a benchmark (random walk, historical mean).

### Metrics
- RMSE, MAE, MAPE for point forecasts.
- Diebold-Mariano test: H0 equal predictive accuracy between two models.
- Clark-West test: for nested model comparisons (adjusts for the fact that the null imposes restrictions).
- Mincer-Zarnowitz regression: regress realized on forecast. Test alpha=0, beta=1 jointly.

### Density Forecasts
- Probability integral transform (PIT): if model is correct, PIT values are U(0,1).
- Log predictive score for comparing density forecasts.

## Structural Breaks and Regime Switching

**Chow test**: Known break date. F-test for parameter stability.

**CUSUM / CUSUM-of-squares**: Sequential tests for parameter instability.

**Bai-Perron**: Multiple unknown structural breaks. Estimates break dates and tests for number of breaks.

**Markov-switching models**: Regime-dependent parameters with transition probabilities.

```python
from statsmodels.tsa.regime_switching.markov_regression import MarkovRegression

model = MarkovRegression(y, k_regimes=2, trend='c', switching_variance=True)
results = model.fit()
```

## Practical Checklist

1. Plot the series. Check for trends, breaks, volatility clustering, outliers.
2. Test for unit roots (ADF + KPSS). Transform to stationarity if needed (log returns, first differences).
3. Choose model class: univariate (ARIMA/GARCH) vs multivariate (VAR/VECM).
4. Select lag order via information criteria.
5. Estimate and check residual diagnostics (Ljung-Box, ARCH-LM, normality).
6. For GARCH: use Student-t or skewed-t distribution. Test for leverage (EGARCH/GJR).
7. For VAR: test Granger causality, compute IRFs with confidence bands, report FEVD.
8. For cointegrated systems: use VECM, not VAR in differences.
9. Always use HAC (Newey-West) standard errors for time series regressions.
10. Evaluate forecasts out-of-sample against a naive benchmark. Use Diebold-Mariano or Clark-West.
11. Test for structural breaks if the sample spans crises or policy changes.
12. Report unconditional and conditional moments, persistence measures (half-life), and economic interpretation.

## Key References

- Hamilton, J.D. (1994). Time Series Analysis. Princeton University Press.
- Luetkepohl, H. (2005). New Introduction to Multiple Time Series Analysis. Springer.
- Tsay, R.S. (2010). Analysis of Financial Time Series, 3rd ed. Wiley.
- Engle, R.F. (1982). Autoregressive conditional heteroscedasticity with estimates of the variance of UK inflation. Econometrica.
- Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. Journal of Econometrics.
- Johansen, S. (1991). Estimation and hypothesis testing of cointegration vectors. Econometrica.
- Newey, W.K. and West, K.D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica.
- Diebold, F.X. and Mariano, R.S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics.
