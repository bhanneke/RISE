# Financial Event Studies

## Overview

A financial event study measures the impact of an event (announcement, regulation, shock) on security prices by estimating abnormal returns — the difference between actual returns and expected returns absent the event. The method exploits the assumption that in efficient markets, prices adjust quickly to new information.

Distinct from difference-in-differences event studies: financial event studies use the market model (not parallel trends) as the counterfactual, operate at daily/intraday frequency, and test statistical significance using cross-sectional and time-series variation in abnormal returns.

## Timeline and Windows

```
|-------- Estimation Window --------|-- Gap --|---- Event Window ----|-- Post --|
   T0                            T1   T1+1    T1+g   tau=0   T2        T2+1
   [-250]                      [-31]  [-30]   [-10]   [0]   [+10]
```

**Estimation window**: Typically [-250, -31] or [-200, -21] trading days relative to event day tau=0.
- Used to estimate the market model parameters (alpha, beta).
- Must NOT overlap with the event window.
- Longer is better for precision, but too long risks structural breaks.

**Event window**: The period over which abnormal returns are cumulated.
- Short window: [-1, +1] or [0, +1] — cleanest test, least noise.
- Medium: [-5, +5] or [-10, +10] — captures slow price adjustment or information leakage.
- Long window: [-30, +30] or months — problematic (joint hypothesis, confounding events, model misspecification accumulates).

**Gap**: Optional buffer between estimation and event window to prevent event contamination.

## Expected Return Models

### Market Model (Standard)

R_it = alpha_i + beta_i * R_mt + epsilon_it

- Estimated over the estimation window using OLS.
- R_mt: market return (CRSP value-weighted or S&P 500).
- Abnormal return: AR_it = R_it - (alpha_hat_i + beta_hat_i * R_mt)

### Market-Adjusted Model (Simpler)

AR_it = R_it - R_mt

- Assumes alpha=0, beta=1 for all firms.
- Less precise but avoids estimation error in alpha/beta.
- Appropriate when estimation window is unavailable.

### Fama-French Three-Factor

R_it = alpha_i + beta_i * MKT_t + s_i * SMB_t + h_i * HML_t + epsilon_it

- Controls for size and value exposures.
- Reduces cross-sectional variation in abnormal returns.
- Use when the sample has systematic size/value tilts.

### Four-Factor (Carhart)

Adds momentum factor UMD (Up Minus Down) to FF3.

### Buy-and-Hold Abnormal Returns (BHAR)

For long-horizon studies:

BHAR_i = Product(1 + R_it) - Product(1 + E[R_it])   over event window

- Compounds actual and expected returns over the window.
- Better captures investor experience than CARs for long horizons.
- But: skewed distribution, cross-sectional dependence, rebalancing bias.

## Abnormal Returns and Aggregation

### Cumulative Abnormal Return (CAR)

For firm i over event window [t1, t2]:

CAR_i(t1, t2) = Sum(AR_it) for t = t1 to t2

### Cross-Sectional Aggregation

Average CAR across N events:

CAAR(t1, t2) = (1/N) * Sum(CAR_i(t1, t2)) for i = 1 to N

## Test Statistics

### Parametric Tests

**Patell (1976) test** (standardized residual test):
- Standardize each AR by its estimation-window standard error (adjusted for prediction error).
- SAR_it = AR_it / S_i * sqrt(adjustment factor)
- Test statistic: sum of SARs divided by sqrt(N), distributed N(0,1) under H0.
- Assumes cross-sectional independence.

**BMP (Boehmer-Musumeci-Poulsen, 1991)** (standardized cross-sectional test):
- Standardizes ARs as in Patell, then uses the cross-sectional variance of SARs.
- Robust to event-induced variance (the main problem with Patell).
- Recommended as the default parametric test.

```
t_BMP = (1/N) * Sum(SAR_i) / sqrt((1/(N*(N-1))) * Sum((SAR_i - SAR_bar)^2))
```

**Kolari-Pynnonen (2010)**:
- Adjusts BMP for cross-sectional correlation.
- Multiplies BMP by sqrt((1 - r_bar) / (1 + (N-1)*r_bar)) where r_bar is average pairwise correlation of ARs.
- Essential when events cluster in calendar time.

### Non-Parametric Tests

**Sign test**: Under H0, fraction of positive CARs = 0.5. Binomial test.
- Robust to non-normality.
- Requires CARs to be symmetric under H0.

**Rank test (Corrado, 1989)**:
- Rank abnormal returns across estimation and event windows.
- Test whether event-window ranks are systematically high or low.
- Robust to non-normality and thin trading.

**Generalized sign test**: Adjusts expected fraction of positive CARs using estimation-window data.

### Which Test to Use
- **Default**: BMP (robust to event-induced variance).
- **Clustered events**: Kolari-Pynnonen or calendar-time portfolio.
- **Small samples / non-normal returns**: Rank test or sign test.
- **Always report** at least one parametric and one non-parametric test.

## Cross-Sectional Regression of CARs

After computing CARs, explain variation across events:

CAR_i = gamma_0 + gamma_1 * X_1i + gamma_2 * X_2i + ... + eta_i

- X variables: firm characteristics, event characteristics, treatment intensity.
- Use heteroskedasticity-robust (White) standard errors.
- If events cluster in time: cluster standard errors by event date or use Fama-MacBeth.

## Calendar-Time Portfolio Approach

Alternative to cross-sectional aggregation when events cluster:

1. Each calendar month, form a portfolio of all firms currently in their event window.
2. Compute the portfolio's excess return.
3. Regress on factor model (FF3 or FF4).
4. The intercept (alpha) is the abnormal return.

Advantages: naturally accounts for cross-sectional correlation. Standard errors are time-series based.
Disadvantages: portfolio composition changes monthly; low power when few events per month.

```python
# Pseudo-code
for each month t:
    portfolio_return_t = equal_weighted average of returns of firms in event window at t

# Regress portfolio excess returns on factors
alpha = intercept from FF3 regression
```

## Implementation in Python

```python
import pandas as pd
import numpy as np
import statsmodels.api as sm

def compute_abnormal_returns(returns, market_returns, event_date_idx,
                              est_start=-250, est_end=-31,
                              evt_start=-1, evt_end=1):
    """
    Compute CARs using the market model.

    Parameters
    ----------
    returns : pd.Series — firm daily returns
    market_returns : pd.Series — market daily returns (aligned index)
    event_date_idx : int — index position of event date
    """
    # Estimation window
    est_ret = returns.iloc[event_date_idx + est_start : event_date_idx + est_end + 1]
    est_mkt = market_returns.iloc[event_date_idx + est_start : event_date_idx + est_end + 1]

    # Estimate market model
    X = sm.add_constant(est_mkt)
    model = sm.OLS(est_ret, X).fit()
    alpha, beta = model.params
    sigma = model.resid.std()

    # Event window
    evt_ret = returns.iloc[event_date_idx + evt_start : event_date_idx + evt_end + 1]
    evt_mkt = market_returns.iloc[event_date_idx + evt_start : event_date_idx + evt_end + 1]

    # Abnormal returns
    expected = alpha + beta * evt_mkt
    AR = evt_ret - expected
    CAR = AR.sum()

    return AR, CAR, sigma, model


def bmp_test(CARs, sigmas):
    """Boehmer-Musumeci-Poulsen test statistic."""
    SARs = CARs / sigmas
    N = len(SARs)
    mean_SAR = SARs.mean()
    var_SAR = ((SARs - mean_SAR) ** 2).sum() / (N * (N - 1))
    t_stat = mean_SAR / np.sqrt(var_SAR)
    return t_stat
```

## Common Pitfalls

1. **Overlapping event windows**: If multiple events affect the same firm within the event window, CARs are confounded. Drop overlapping events or use shortest feasible window.
2. **Event date uncertainty**: If the exact announcement date is unclear (e.g., rumors preceded the announcement), use [-5, +5] and plot daily CARs to identify information leakage.
3. **Thin trading**: Illiquid stocks have zero-return days that bias beta estimates toward zero. Use Dimson (1979) adjustment (include lead and lag market returns) or Scholes-Williams (1977).
4. **Survivorship bias**: If firms delist during the event window, use delisting returns (CRSP provides these).
5. **Cross-sectional dependence**: Clustered events (e.g., regulatory announcements affecting all firms on the same day) inflate standard test statistics. Use Kolari-Pynnonen or calendar-time portfolios.
6. **Confounding events**: Firm-specific confounding events (earnings, M&A) during the event window. Check for concurrent announcements.
7. **Long-horizon issues**: CARs over months are unreliable — model misspecification accumulates, results are sensitive to benchmark choice. Prefer short windows.

## Practical Checklist

1. Define event precisely. Identify the exact announcement date from news archives / SEC filings / press releases.
2. Choose event window length based on hypothesis. Default: [-1, +1] for clean identification.
3. Estimate market model over [-250, -31]. Verify sufficient non-missing returns (require >= 100 trading days).
4. Compute ARs and CARs. Plot average daily CARs over [-10, +10] to visualize dynamics.
5. Test significance with BMP (parametric) and rank test (non-parametric).
6. If events cluster in calendar time, use Kolari-Pynnonen adjustment or calendar-time portfolio.
7. Run cross-sectional regression of CARs on event/firm characteristics with robust SEs.
8. Robustness: vary event window length, use market-adjusted model, FF3 model, drop outliers.
9. Report: N events, mean/median CAR, test statistics, event window, estimation window.
10. Plot cumulative average abnormal returns over the event window with confidence bands.

## Key References

- MacKinlay, A.C. (1997). Event studies in economics and finance. Journal of Economic Literature.
- Campbell, J.Y., Lo, A.W., and MacKinlay, A.C. (1997). The Econometrics of Financial Markets. Princeton.
- Boehmer, E., Musumeci, J., and Poulsen, A.B. (1991). Event-study methodology under conditions of event-induced variance. Journal of Financial Economics.
- Kolari, J.W. and Pynnonen, S. (2010). Event study testing with cross-sectional correlation of abnormal returns. Review of Financial Studies.
- Kothari, S.P. and Warner, J.B. (2007). Econometrics of event studies. In Handbook of Corporate Finance: Empirical Corporate Finance.
- Corrado, C.J. (1989). A nonparametric test for abnormal security-price performance in event studies. Journal of Financial Economics.
- Fama, E.F. (1998). Market efficiency, long-term returns, and behavioral finance. Journal of Financial Economics.
