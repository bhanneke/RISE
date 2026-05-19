<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/data-fred-api.md -->

# `fred-api`



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

# FRED API — Federal Reserve Economic Data

## Overview

FRED (Federal Reserve Economic Data) is maintained by the Federal Reserve Bank of St. Louis.
It provides over 800,000 time series from 100+ sources. The API is free with a key from
https://fred.stlouisfed.org/docs/api/api_key.html.

## Base URL and Authentication

```
Base URL: https://api.stlouisfed.org/fred/
API key: passed as query parameter `api_key=YOUR_KEY`
Response formats: json, xml (use `file_type=json`)
```

Rate limit: 120 requests per 60 seconds per API key.

## Common Macro Series IDs

### National Accounts
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| GDPC1        | Real GDP (chained 2017 dollars, SA)        | Quarterly  |
| GDP          | Nominal GDP                                | Quarterly  |
| A191RL1Q225SBEA | Real GDP growth rate (annualized)      | Quarterly  |
| PCEC96       | Real personal consumption expenditures     | Monthly    |
| GPDI         | Gross private domestic investment          | Quarterly  |

### Prices and Inflation
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| CPIAUCSL     | CPI for All Urban Consumers (SA)           | Monthly    |
| CPILFESL     | Core CPI (less food and energy, SA)        | Monthly    |
| PCEPI        | PCE Price Index                            | Monthly    |
| PCEPILFE     | Core PCE Price Index                       | Monthly    |
| T10YIE       | 10-Year Breakeven Inflation Rate           | Daily      |

### Labor Market
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| UNRATE       | Civilian Unemployment Rate (SA)            | Monthly    |
| PAYEMS       | Total Nonfarm Payrolls (SA)                | Monthly    |
| CIVPART      | Labor Force Participation Rate             | Monthly    |
| AWHAETP      | Average Weekly Hours (private, SA)         | Monthly    |
| CES0500000003 | Average Hourly Earnings (private, SA)    | Monthly    |
| ICSA         | Initial Jobless Claims (SA)                | Weekly     |
| JTSJOL       | Job Openings (JOLTS, SA)                   | Monthly    |

### Interest Rates and Monetary Policy
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| FEDFUNDS     | Effective Federal Funds Rate               | Monthly    |
| DFF          | Effective Federal Funds Rate               | Daily      |
| DGS10        | 10-Year Treasury Constant Maturity Rate    | Daily      |
| DGS2         | 2-Year Treasury Constant Maturity Rate     | Daily      |
| T10Y2Y       | 10Y-2Y Treasury Spread                    | Daily      |
| MORTGAGE30US | 30-Year Fixed Mortgage Rate                | Weekly     |
| WALCL        | Fed Total Assets (balance sheet)           | Weekly     |

### Financial Conditions
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| SP500        | S&P 500 Index                              | Daily      |
| VIXCLS       | CBOE Volatility Index (VIX)               | Daily      |
| BAMLH0A0HYM2 | ICE BofA US High Yield Option-Adj Spread  | Daily      |
| DTWEXBGS     | Trade-Weighted US Dollar Index (Broad)     | Daily      |

### Housing and Real Estate
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| MSPUS        | Median Sales Price of Houses Sold          | Quarterly  |
| HOUST        | Housing Starts (SA, annual rate)           | Monthly    |
| CSUSHPINSA   | Case-Shiller US Home Price Index (NSA)     | Monthly    |

## Python fredapi Library

Install: `pip install fredapi`

### Basic Usage

```python
from fredapi import Fred

fred = Fred(api_key="YOUR_API_KEY")

# Fetch a single series
gdp = fred.get_series("GDPC1")  # Returns pandas Series with DatetimeIndex

# Fetch with date range
cpi = fred.get_series("CPIAUCSL", observation_start="2000-01-01", observation_end="2024-12-31")

# Get series metadata
info = fred.get_series_info("UNRATE")
print(info["title"], info["frequency"], info["units"])
```

### Frequency Conversion

FRED supports server-side frequency aggregation. Use the `frequency` parameter:

```python
# Convert daily to monthly (aggregation_method defaults to average)
fed_funds_monthly = fred.get_series("DFF", frequency="m")

# Quarterly GDP as annual
gdp_annual = fred.get_series("GDPC1", frequency="a", aggregation_method="eop")  # end of period
```

Frequency codes: `d` (daily), `w` (weekly), `bw` (biweekly), `m` (monthly),
`q` (quarterly), `sa` (semiannual), `a` (annual).

Aggregation methods: `avg` (average, default), `sum`, `eop` (end of period).

### Vintage Dates (Real-Time Data)

FRED stores every historical revision. This matters for replication and
avoiding look-ahead bias in forecasting studies.

```python
# Get data as it was known on a specific date
gdp_vintage = fred.get_series("GDPC1", realtime_start="2020-01-01", realtime_end="2020-01-01")

# Get all vintages for a date range
all_vintages = fred.get_series_all_releases("GDPC1")

# First release vs. latest for a specific observation
first = fred.get_series_first_release("GDPC1")
latest = fred.get_series_latest_release("GDPC1")
```

Vintage data is essential for:
- Nowcasting and forecasting evaluations (use only data available at the time)
- Studying data revisions (how much does GDP get revised?)
- Replicating papers that used real-time data vintages

### Searching for Series

```python
results = fred.search("consumer price index")  # Returns DataFrame
results = fred.search_by_release(10)           # CPI release ID
results = fred.search_by_category(32073)       # Category: prices
```

### Building a Panel Dataset

```python
import pandas as pd

series_ids = ["GDPC1", "UNRATE", "CPIAUCSL", "FEDFUNDS"]
frames = {}
for sid in series_ids:
    frames[sid] = fred.get_series(sid, observation_start="1990-01-01", frequency="q")

panel = pd.DataFrame(frames)
panel.index.name = "date"
```

### Direct API Calls (without fredapi)

```python
import requests

params = {
    "series_id": "GDPC1",
    "api_key": "YOUR_KEY",
    "file_type": "json",
    "observation_start": "2000-01-01",
    "frequency": "q",
}
resp = requests.get("https://api.stlouisfed.org/fred/series/observations", params=params)
data = resp.json()["observations"]  # List of {"date": ..., "value": ...}
```

## Key API Endpoints

| Endpoint                          | Purpose                              |
|-----------------------------------|--------------------------------------|
| `/fred/series/observations`       | Get data for a series                |
| `/fred/series`                    | Get series metadata                  |
| `/fred/series/search`             | Search series by keywords            |
| `/fred/series/categories`         | Get categories for a series          |
| `/fred/series/vintagedates`       | Get all vintage dates for a series   |
| `/fred/releases`                  | List data releases                   |
| `/fred/release/series`            | Get series in a release              |

## Tips for Academic Use

- Always cite the original data source (e.g., BLS for CPI, BEA for GDP), not just FRED.
- Record the vintage date or download date for reproducibility.
- For seasonally adjusted vs. not: FRED series ending in `SA` or `SL` are typically SA.
  NSA variants often end in `NS`. Check metadata.
- FRED GeoFRED provides state and MSA level data for regional analysis.
- The FRED Excel add-in and FRED mobile app are useful for quick exploration.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<pre style="white-space:pre-wrap;"># curator-private; copy text from
# /Users/hanneke/Documents/Projects/100xOS/shared/skills/data/fred-api.md</pre>
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/hundredx-os/data-fred-api/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/hundredx-os.yml">edit on GitHub</a>.</p>
</div>

</div>
