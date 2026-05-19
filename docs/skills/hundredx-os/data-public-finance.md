<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/data-public-finance.md -->

# `public-finance`

*Pack: [100xOS shared skills](../hundredx-os.md) · category `data-handling` · field `economics`*

---

# Public Finance & Macro Data Skill

## FRED API Patterns

The Federal Reserve Economic Data (FRED) API is the standard source for U.S. macro time series. Key series for finance research:

### Interest Rates & Monetary Policy
- `DFF` — Federal funds effective rate (daily)
- `DGS10` — 10-year Treasury constant maturity (daily)
- `DGS2` — 2-year Treasury constant maturity (daily)
- `T10Y2Y` — 10-Year minus 2-Year spread (yield curve)
- `DFEDTARU` — Fed funds target upper limit

### Prices & Inflation
- `CPIAUCSL` — CPI for all urban consumers (monthly, seasonally adjusted)
- `CPILFESL` — Core CPI (ex food & energy)
- `PCEPI` — PCE price index (Fed's preferred measure)
- `BREAKEVEN10` — 10-year breakeven inflation rate

### Output & Activity
- `GDP` — Gross domestic product (quarterly, billions)
- `GDPC1` — Real GDP (chained 2017 dollars)
- `UNRATE` — Unemployment rate (monthly)
- `PAYEMS` — Total nonfarm payrolls (monthly)
- `INDPRO` — Industrial production index

### Financial Conditions
- `VIXCLS` — CBOE VIX (daily)
- `BAMLH0A0HYM2` — ICE BofA high-yield OAS (daily)
- `DTWEXBGS` — Trade-weighted U.S. dollar index (daily)
- `SP500` — S&P 500 (daily, use Yahoo Finance for more granular)

### Money & Credit
- `M2SL` — M2 money supply
- `TOTCI` — Total commercial & industrial loans
- `BUSLOANS` — Commercial & industrial loans

## Yahoo Finance Patterns

Use `yfinance` for market price data:
- Equity indices: `^GSPC` (S&P 500), `^DJI` (Dow), `^IXIC` (Nasdaq)
- Volatility: `^VIX`
- Commodities: `GC=F` (gold), `CL=F` (crude oil), `BTC-USD`
- ETFs as proxies: `SPY`, `QQQ`, `TLT` (long bonds), `HYG` (high yield)
- Individual equities by ticker

## Merge Strategies

When combining macro data with micro-level panel data:

1. **Frequency alignment**: Macro series are daily/monthly/quarterly. Panel data is often at irregular frequencies. Merge on the appropriate time unit.
   - For daily panel data: merge on exact date using FRED daily series
   - For monthly panels: use end-of-month or average macro values
   - For event studies: use the event date to look up the macro variable level

2. **Lags and leads**: In many specifications, you want the macro variable *before* the micro outcome:
   ```
   macro_lag1 = macro_value.shift(1)  # Previous period
   ```

3. **Transformations**:
   - Log differences for growth rates: `np.log(series).diff()`
   - Standardize for cross-variable comparisons: `(x - x.mean()) / x.std()`
   - HP filter for trend/cycle decomposition (use `statsmodels.tsa.filters.hp_filter`)
   - First differences for non-stationary series

4. **Controls vs. instruments**: Macro variables are typically controls in micro regressions (absorb time-varying aggregate shocks). When used as instruments, the exclusion restriction must be argued carefully — macro shocks affect many channels simultaneously.

## Common Pitfalls

- **Vintage effects**: FRED revises macro data. For real-time analysis, use the ALFRED (Archival FRED) real-time dataset.
- **Seasonality**: Prefer seasonally adjusted (SA) series unless studying seasonal patterns. FRED SA series end in `SL` or `SA`.
- **Unit roots**: Most macro series are non-stationary. Test with ADF before running regressions in levels. Use differences or cointegration as appropriate.
- **Generated regressors**: If you construct a macro variable (e.g., residual from a time-series model) and use it as a regressor, standard errors need correction (Murphy-Topel or bootstrap).
