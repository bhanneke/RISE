<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/data-public-finance.md -->

# `public-finance`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

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


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/data/public-finance.md</pre>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../hundredx-os.md">100xOS shared skills</a></dd>
<dt><b>Category</b></dt><dd><code>data-handling</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>data-acquisition</code></dd>
<dt><b>License</b></dt><dd>private (curator-owned)</dd>
<dt><b>Last update</b></dt><dd>2026-05-20</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/data-public-finance/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
