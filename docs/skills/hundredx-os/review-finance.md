<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/review-finance.md -->

# `finance`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/review/finance.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Finance Paper Review Checklist

### Overview

Quality checklist for reviewing empirical finance papers. Covers methodology, data, presentation, and common pitfalls specific to financial economics research.

### Data Quality

#### Sample Construction
- [ ] Sample selection criteria clearly stated and justified.
- [ ] Universe defined (CRSP, Compustat, specific exchange, country).
- [ ] Filters documented: minimum price, minimum market cap, exclusion of financials/utilities, share type (ordinary common equity only).
- [ ] Sample period justified. Long enough for reliable inference (typically 20+ years for asset pricing, 5+ years for corporate finance).
- [ ] Number of observations, firms, and time periods reported.

#### Survivorship Bias
- [ ] Includes delisted firms (not just survivors).
- [ ] Uses delisting returns from CRSP (not just dropping firms at delisting).
- [ ] If using a database that only covers survivors (e.g., some international databases), acknowledge the bias.

#### Look-Ahead Bias
- [ ] Accounting data available to investors at portfolio formation (use lagged data: e.g., fiscal year-end data available 6 months later — June sorting convention).
- [ ] No future information used in variable construction.
- [ ] Real-time data vintages used for macro variables if relevant.

#### Data Cleaning
- [ ] Outlier treatment documented (winsorization at 1/99% or trimming). Consistent across all variables.
- [ ] Penny stocks excluded or results shown with and without (price > $1 or $5).
- [ ] Micro-caps addressed (NYSE size breakpoints, or explicit exclusion of bottom quintile by ME).
- [ ] Missing data handling explained (how are missing returns, missing accounting data treated?).

### Methodology

#### Standard Errors
- [ ] Appropriate standard errors for the setting:
  - Time-series regressions: Newey-West HAC (specify lag length).
  - Panel regressions: clustered by firm and/or time (Petersen 2009).
  - Fama-MacBeth: Newey-West on the time series of cross-sectional slopes (or Shanken correction).
  - Event studies: BMP or Kolari-Pynnonen.
- [ ] Justification for clustering choice. Petersen (2009) guidance: cluster on the dimension with fewer clusters.
- [ ] NOT using simple OLS standard errors for panel data with firm or time effects.

#### Return Computation
- [ ] Log returns vs simple returns: stated and consistent. Log returns for time-series analysis; simple returns for portfolio aggregation.
- [ ] Compounding method for multi-period returns: buy-and-hold (BHAR) vs cumulative abnormal (CAR). State which and why.
- [ ] Excess returns: clearly defined (in excess of risk-free rate, typically 1-month T-bill).
- [ ] Currency: returns in local currency or USD, and how currency effects are handled.

#### Factor Model Specification
- [ ] Factor model choice justified (CAPM, FF3, FF5, q-factor, etc.).
- [ ] Factor data source cited (Ken French library, AQR, self-constructed).
- [ ] Results robust to alternative factor models (show at least two).
- [ ] If self-constructed factors: construction methodology detailed and matches standard conventions.

#### Portfolio Construction
- [ ] Sorting variable, breakpoints, and rebalancing frequency documented.
- [ ] NYSE breakpoints used for CRSP sorts (avoids micro-cap domination).
- [ ] Value-weighted returns as primary (equal-weighted as robustness — EW overweights micro-caps).
- [ ] Holding period and skip-month convention for momentum documented.

#### Endogeneity and Identification
- [ ] Potential endogeneity concerns discussed.
- [ ] If causal claims made: identification strategy clearly stated (IV, DiD, RDD, natural experiment).
- [ ] Instruments validated: relevance (first-stage F > 10) and exclusion restriction argued.
- [ ] Reverse causality addressed.

### Statistical Issues

#### Multiple Testing
- [ ] If testing multiple hypotheses: acknowledge the problem.
- [ ] Apply appropriate corrections (Bonferroni, Holm, FDR/Benjamini-Hochberg).
- [ ] For new anomalies: use t > 3.0 threshold (Harvey-Liu-Zhu 2016) or bootstrap.
- [ ] Pre-registration or holdout sample if feasible.

#### Economic vs Statistical Significance
- [ ] Report economic magnitudes (basis points per month, percent per year, dollar amounts).
- [ ] Discuss whether the effect is large enough to matter after transaction costs.
- [ ] For trading strategies: account for bid-ask spreads, market impact, short-selling costs, and capacity constraints.
- [ ] Sharpe ratio or information ratio for strategy performance.

#### Small Sample / Power
- [ ] Is the sample large enough for the tests used?
- [ ] For GRS tests: N (test assets) should be much less than T (time periods).
- [ ] For Fama-MacBeth: at least 200+ months for reliable inference.
- [ ] For event studies: sufficient events for cross-sectional tests (N > 30 minimum, ideally 100+).

#### Non-Stationarity
- [ ] Unit root tests performed if using price levels, valuation ratios, or macro variables.
- [ ] Stambaugh (1999) bias addressed if using persistent regressors in predictive regressions.
- [ ] Regime changes or structural breaks considered (pre/post crisis, regulatory changes).

### Presentation

#### Tables
- [ ] Summary statistics table: N, mean, median, SD, min, max, percentiles for all key variables.
- [ ] Correlation matrix for main variables.
- [ ] Regression tables: coefficients, t-statistics (or standard errors), R^2, N, fixed effects indicators.
- [ ] Portfolio sort tables: mean return, alpha, t-statistics, monotonicity pattern, high-minus-low spread.
- [ ] Standard errors in parentheses, t-statistics in brackets — be consistent.
- [ ] Significance stars: * p<0.10, ** p<0.05, *** p<0.01 (state convention).

#### Figures
- [ ] Time series of key variables or cumulative returns.
- [ ] Event study: cumulative average abnormal returns with confidence bands.
- [ ] Portfolio performance: cumulative wealth plot.
- [ ] Coefficient stability across subperiods or specifications (coefficient plot).

#### Reporting Conventions
- [ ] Returns in percent (not decimals). State frequency (daily, monthly, annual).
- [ ] Report annualized returns and volatilities where appropriate (multiply monthly by 12 and sqrt(12)).
- [ ] Market cap in millions or billions. State currency and date for nominal values.
- [ ] Book-to-market, not market-to-book (Fama-French convention).
- [ ] Basis points (bps) for small return differentials (1 bp = 0.01%).

### Common Pitfalls in Finance Papers

1. **Cross-sectional correlation**: Fama-MacBeth addresses this, but pooled OLS with firm-clustered SEs does not account for time effects. Use double-clustering (Petersen 2009) or Fama-MacBeth.

2. **Microstructure noise**: Using daily closing prices for high-frequency analysis introduces bid-ask bounce. Use midpoint prices or apply appropriate filters.

3. **Rebalancing assumptions**: Monthly rebalanced portfolios assume zero transaction costs. Discuss turnover and implementation costs.

4. **Short-selling constraints**: Long-short strategies assume costless shorting. Discuss short interest, lending fees, and institutional constraints.

5. **Data snooping**: The finance "factor zoo" problem. New anomalies must clear a high bar. Pre-specify hypotheses.

6. **Stale prices**: Illiquid stocks have stale prices that induce spurious predictability and autocorrelation. Use the Dimson (1979) beta correction.

7. **Penny stock bias**: Many anomalies concentrate in micro-cap and penny stocks. Results should survive exclusion of stocks below $5 or below the 20th NYSE size percentile.

8. **Backfill bias**: Databases may backfill historical data when a firm is added, creating upward bias in performance.

9. **Index inclusion effects**: S&P 500 additions/deletions have well-documented price effects. Control for or exclude these events if they contaminate the sample.

10. **Seasonality**: January effect, turn-of-month, day-of-week effects. Check if results are driven by calendar regularities.

### Key References

- Petersen, M.A. (2009). Estimating standard errors in finance panel data sets: Comparing approaches. Review of Financial Studies.
- Harvey, C.R., Liu, Y., and Zhu, H. (2016). ... and the cross-section of expected returns. Review of Financial Studies.
- Stambaugh, R.F. (1999). Predictive regressions. Journal of Financial Economics.
- Hou, K., Xue, C., and Zhang, L. (2020). Replicating anomalies. Review of Financial Studies.
- Fama, E.F. and French, K.R. (2008). Dissecting anomalies. Journal of Finance.
- Cochrane, J.H. (2011). Presidential address: Discount rates. Journal of Finance.
- McLean, R.D. and Pontiff, J. (2016). Does academic research destroy stock return predictability? Journal of Finance.
