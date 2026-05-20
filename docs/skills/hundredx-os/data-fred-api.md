<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/data-fred-api.md -->

# `fred-api`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>data-handling</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-acquisition</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/data/fred-api.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## FRED API — Federal Reserve Economic Data

### Overview

FRED (Federal Reserve Economic Data) is maintained by the Federal Reserve Bank of St. Louis.
It provides over 800,000 time series from 100+ sources. The API is free with a key from
https://fred.stlouisfed.org/docs/api/api_key.html.

### Base URL and Authentication

```
Base URL: https://api.stlouisfed.org/fred/
API key: passed as query parameter `api_key=YOUR_KEY`
Response formats: json, xml (use `file_type=json`)
```

Rate limit: 120 requests per 60 seconds per API key.

### Common Macro Series IDs

#### National Accounts
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| GDPC1        | Real GDP (chained 2017 dollars, SA)        | Quarterly  |
| GDP          | Nominal GDP                                | Quarterly  |
| A191RL1Q225SBEA | Real GDP growth rate (annualized)      | Quarterly  |
| PCEC96       | Real personal consumption expenditures     | Monthly    |
| GPDI         | Gross private domestic investment          | Quarterly  |

#### Prices and Inflation
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| CPIAUCSL     | CPI for All Urban Consumers (SA)           | Monthly    |
| CPILFESL     | Core CPI (less food and energy, SA)        | Monthly    |
| PCEPI        | PCE Price Index                            | Monthly    |
| PCEPILFE     | Core PCE Price Index                       | Monthly    |
| T10YIE       | 10-Year Breakeven Inflation Rate           | Daily      |

#### Labor Market
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| UNRATE       | Civilian Unemployment Rate (SA)            | Monthly    |
| PAYEMS       | Total Nonfarm Payrolls (SA)                | Monthly    |
| CIVPART      | Labor Force Participation Rate             | Monthly    |
| AWHAETP      | Average Weekly Hours (private, SA)         | Monthly    |
| CES0500000003 | Average Hourly Earnings (private, SA)    | Monthly    |
| ICSA         | Initial Jobless Claims (SA)                | Weekly     |
| JTSJOL       | Job Openings (JOLTS, SA)                   | Monthly    |

#### Interest Rates and Monetary Policy
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| FEDFUNDS     | Effective Federal Funds Rate               | Monthly    |
| DFF          | Effective Federal Funds Rate               | Daily      |
| DGS10        | 10-Year Treasury Constant Maturity Rate    | Daily      |
| DGS2         | 2-Year Treasury Constant Maturity Rate     | Daily      |
| T10Y2Y       | 10Y-2Y Treasury Spread                    | Daily      |
| MORTGAGE30US | 30-Year Fixed Mortgage Rate                | Weekly     |
| WALCL        | Fed Total Assets (balance sheet)           | Weekly     |

#### Financial Conditions
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| SP500        | S&P 500 Index                              | Daily      |
| VIXCLS       | CBOE Volatility Index (VIX)               | Daily      |
| BAMLH0A0HYM2 | ICE BofA US High Yield Option-Adj Spread  | Daily      |
| DTWEXBGS     | Trade-Weighted US Dollar Index (Broad)     | Daily      |

#### Housing and Real Estate
| Series ID    | Description                                | Frequency  |
|--------------|--------------------------------------------|------------|
| MSPUS        | Median Sales Price of Houses Sold          | Quarterly  |
| HOUST        | Housing Starts (SA, annual rate)           | Monthly    |
| CSUSHPINSA   | Case-Shiller US Home Price Index (NSA)     | Monthly    |

### Python fredapi Library

Install: `pip install fredapi`

#### Basic Usage

```python
from fredapi import Fred

fred = Fred(api_key="YOUR_API_KEY")

## Fetch a single series
gdp = fred.get_series("GDPC1")  # Returns pandas Series with DatetimeIndex

## Fetch with date range
cpi = fred.get_series("CPIAUCSL", observation_start="2000-01-01", observation_end="2024-12-31")

## Get series metadata
info = fred.get_series_info("UNRATE")
print(info["title"], info["frequency"], info["units"])
```

#### Frequency Conversion

FRED supports server-side frequency aggregation. Use the `frequency` parameter:

```python
## Convert daily to monthly (aggregation_method defaults to average)
fed_funds_monthly = fred.get_series("DFF", frequency="m")

## Quarterly GDP as annual
gdp_annual = fred.get_series("GDPC1", frequency="a", aggregation_method="eop")  # end of period
```

Frequency codes: `d` (daily), `w` (weekly), `bw` (biweekly), `m` (monthly),
`q` (quarterly), `sa` (semiannual), `a` (annual).

Aggregation methods: `avg` (average, default), `sum`, `eop` (end of period).

#### Vintage Dates (Real-Time Data)

FRED stores every historical revision. This matters for replication and
avoiding look-ahead bias in forecasting studies.

```python
## Get data as it was known on a specific date
gdp_vintage = fred.get_series("GDPC1", realtime_start="2020-01-01", realtime_end="2020-01-01")

## Get all vintages for a date range
all_vintages = fred.get_series_all_releases("GDPC1")

## First release vs. latest for a specific observation
first = fred.get_series_first_release("GDPC1")
latest = fred.get_series_latest_release("GDPC1")
```

Vintage data is essential for:
- Nowcasting and forecasting evaluations (use only data available at the time)
- Studying data revisions (how much does GDP get revised?)
- Replicating papers that used real-time data vintages

#### Searching for Series

```python
results = fred.search("consumer price index")  # Returns DataFrame
results = fred.search_by_release(10)           # CPI release ID
results = fred.search_by_category(32073)       # Category: prices
```

#### Building a Panel Dataset

```python
import pandas as pd

series_ids = ["GDPC1", "UNRATE", "CPIAUCSL", "FEDFUNDS"]
frames = {}
for sid in series_ids:
    frames[sid] = fred.get_series(sid, observation_start="1990-01-01", frequency="q")

panel = pd.DataFrame(frames)
panel.index.name = "date"
```

#### Direct API Calls (without fredapi)

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

### Key API Endpoints

| Endpoint                          | Purpose                              |
|-----------------------------------|--------------------------------------|
| `/fred/series/observations`       | Get data for a series                |
| `/fred/series`                    | Get series metadata                  |
| `/fred/series/search`             | Search series by keywords            |
| `/fred/series/categories`         | Get categories for a series          |
| `/fred/series/vintagedates`       | Get all vintage dates for a series   |
| `/fred/releases`                  | List data releases                   |
| `/fred/release/series`            | Get series in a release              |

### Tips for Academic Use

- Always cite the original data source (e.g., BLS for CPI, BEA for GDP), not just FRED.
- Record the vintage date or download date for reproducibility.
- For seasonally adjusted vs. not: FRED series ending in `SA` or `SL` are typically SA.
  NSA variants often end in `NS`. Check metadata.
- FRED GeoFRED provides state and MSA level data for regional analysis.
- The FRED Excel add-in and FRED mobile app are useful for quick exploration.
