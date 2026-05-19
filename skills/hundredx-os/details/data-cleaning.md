# Data Cleaning Best Practices for Economics Research

## Overview

Clean data is the foundation of credible empirical work. This guide covers systematic
approaches to data cleaning for economic datasets, with emphasis on panel data, survey
data, and administrative records commonly used in applied economics.

## Handling Missing Values

### Diagnosis First

Before imputing or dropping, understand the missing data mechanism:

- **MCAR** (Missing Completely at Random): Missingness is unrelated to any variable.
  Safe to drop, but imputation improves efficiency.
- **MAR** (Missing at Random): Missingness depends on observed variables.
  Multiple imputation is appropriate; dropping introduces bias.
- **MNAR** (Missing Not at Random): Missingness depends on the unobserved value itself
  (e.g., high earners not reporting income). No simple fix; requires modeling the
  selection process (Heckman correction, bounds analysis).

```python
import pandas as pd
import numpy as np

# Profile missingness
df.isnull().sum().sort_values(ascending=False)
df.isnull().mean()  # Fraction missing per column

# Check if missingness correlates with observables
df["income_missing"] = df["income"].isnull().astype(int)
df.groupby("income_missing")[["education", "age", "gender"]].mean()
```

### Strategies

| Strategy             | When to use                                    | Risk                        |
|----------------------|------------------------------------------------|-----------------------------|
| Listwise deletion    | MCAR, small fraction missing (<5%)             | Loss of power               |
| Mean/median impute   | Quick exploration only                         | Attenuates variance         |
| Regression impute    | MAR, continuous variable                       | Understates uncertainty     |
| Multiple imputation  | MAR, need valid inference                      | Computationally heavier     |
| Indicator method     | Add dummy for "missing" + impute constant      | Biased if MNAR              |
| Last obs carry fwd   | Panel data, slow-moving variables              | Stale data                  |
| Interpolation        | Time series with small gaps                    | Assumes smooth process      |

```python
# Multiple imputation with sklearn
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

imputer = IterativeImputer(max_iter=10, random_state=42)
df_imputed = pd.DataFrame(imputer.fit_transform(df_numeric), columns=df_numeric.columns)
```

## Outlier Detection and Treatment

### Detection Methods

```python
# Z-score method (assumes normality)
from scipy import stats
z_scores = np.abs(stats.zscore(df["income"].dropna()))
outliers_z = z_scores > 3

# IQR method (robust to non-normality)
Q1, Q3 = df["income"].quantile([0.25, 0.75])
IQR = Q3 - Q1
lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
outliers_iqr = (df["income"] < lower) | (df["income"] > upper)

# Mahalanobis distance (multivariate)
from scipy.spatial.distance import mahalanobis
cov_inv = np.linalg.inv(df[["x1", "x2"]].cov().values)
center = df[["x1", "x2"]].mean().values
df["mahal"] = df[["x1", "x2"]].apply(lambda row: mahalanobis(row, center, cov_inv), axis=1)
```

### Treatment Methods

**Winsorizing** — cap extreme values at a percentile threshold. Preferred in economics
because it retains all observations.

```python
from scipy.stats.mstats import winsorize

# Winsorize at 1st and 99th percentile
df["income_w"] = winsorize(df["income"], limits=[0.01, 0.01])

# Manual winsorizing (more control)
p01, p99 = df["income"].quantile([0.01, 0.99])
df["income_w"] = df["income"].clip(lower=p01, upper=p99)
```

**Trimming** — drop extreme observations entirely. Loses data but avoids influence.

```python
# Trim top and bottom 1%
p01, p99 = df["income"].quantile([0.01, 0.99])
df_trimmed = df[(df["income"] >= p01) & (df["income"] <= p99)]
```

**Best practice**: Report results with and without outlier treatment.
If results change substantially, discuss why.

## Merge and Join Strategies

### Pre-merge Checks

```python
# Check key uniqueness
assert df_left["id"].is_unique, "Left key not unique — will duplicate rows"
assert df_right["id"].is_unique, "Right key not unique — will duplicate rows"

# Check key overlap
left_keys = set(df_left["id"])
right_keys = set(df_right["id"])
print(f"Left only: {len(left_keys - right_keys)}")
print(f"Right only: {len(right_keys - left_keys)}")
print(f"Both: {len(left_keys & right_keys)}")
```

### Merge with Validation

```python
# Use validate parameter to catch unexpected many-to-many
merged = pd.merge(df_left, df_right, on="id", how="left", validate="m:1", indicator=True)

# Always inspect the indicator
print(merged["_merge"].value_counts())
# left_only   — unmatched left rows (check if expected)
# right_only  — unmatched right rows (only with how="outer")
# both        — matched rows
```

### Fuzzy Matching

For entity matching where keys are not exact (company names, addresses):

```python
from fuzzywuzzy import fuzz, process

# Find best match for each name in a reference list
df["best_match"] = df["company_name"].apply(
    lambda x: process.extractOne(x, reference_names, scorer=fuzz.token_sort_ratio)
)
```

### Time-Based Merges

For merging datasets at different frequencies (e.g., monthly macro data with quarterly firm data):

```python
# Merge-as-of: for each row in left, find the most recent matching row in right
merged = pd.merge_asof(
    df_daily.sort_values("date"),
    df_monthly.sort_values("date"),
    on="date",
    direction="backward"  # Use most recent available observation
)
```

## Panel Data Balancing

### Diagnosing Panel Structure

```python
# Check panel balance
panel_counts = df.groupby("entity_id")["year"].count()
print(f"Min periods: {panel_counts.min()}, Max: {panel_counts.max()}")
print(f"Balanced: {panel_counts.nunique() == 1}")

# Identify gaps
def find_gaps(group):
    years = group["year"].sort_values()
    expected = range(years.min(), years.max() + 1)
    return set(expected) - set(years)

gaps = df.groupby("entity_id").apply(find_gaps)
```

### Balancing Strategies

```python
# Create balanced panel (keep only entities observed in all periods)
all_periods = set(df["year"].unique())
entity_periods = df.groupby("entity_id")["year"].apply(set)
balanced_entities = entity_periods[entity_periods == all_periods].index
df_balanced = df[df["entity_id"].isin(balanced_entities)]

# Create fully balanced panel with explicit missing values
idx = pd.MultiIndex.from_product(
    [df["entity_id"].unique(), df["year"].unique()],
    names=["entity_id", "year"]
)
df_balanced = df.set_index(["entity_id", "year"]).reindex(idx).reset_index()
```

**Warning**: Restricting to a balanced panel introduces survivorship bias. Report how many
entities you drop and test sensitivity.

## Encoding Categorical Variables

### Ordered Categories

```python
education_order = ["less_than_hs", "high_school", "some_college", "bachelors", "graduate"]
df["education"] = pd.Categorical(df["education"], categories=education_order, ordered=True)
df["education_numeric"] = df["education"].cat.codes
```

### Dummy Variables

```python
# For regression: drop one category to avoid multicollinearity
dummies = pd.get_dummies(df["industry"], prefix="ind", drop_first=True, dtype=int)
df = pd.concat([df, dummies], axis=1)
```

### High-Cardinality Categoricals

For variables with many levels (e.g., occupation codes, ZIP codes):
- Use fixed effects rather than dummies when the number of categories is large
- Consider grouping into broader categories (e.g., 2-digit industry from 4-digit NAICS)
- Target encoding is useful for prediction but introduces leakage risk

## Date Parsing and Time Alignment

```python
# Parse dates robustly
df["date"] = pd.to_datetime(df["date_str"], format="mixed", dayfirst=False)

# Create fiscal year, quarter
df["year"] = df["date"].dt.year
df["quarter"] = df["date"].dt.quarter
df["fiscal_year"] = df["date"].dt.year + (df["date"].dt.month >= 7).astype(int)

# Align to period end (for merging quarterly data)
df["quarter_end"] = df["date"] + pd.offsets.QuarterEnd(0)

# Handle mixed date formats in messy administrative data
def parse_flexible(date_str):
    for fmt in ["%Y-%m-%d", "%m/%d/%Y", "%d-%b-%Y", "%Y%m%d"]:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT
```

## General Workflow

1. **Load and inspect**: `df.shape`, `df.dtypes`, `df.describe()`, `df.head(20)`
2. **Check duplicates**: `df.duplicated(subset=key_cols).sum()`
3. **Profile missingness**: pattern, mechanism, fraction
4. **Validate ranges**: income > 0, age in [0, 120], percentages in [0, 100]
5. **Standardize strings**: `.str.strip().str.lower()`, fix encoding issues
6. **Parse dates**: consistent format, handle time zones
7. **Handle outliers**: document rule, report sensitivity
8. **Merge carefully**: validate, inspect indicator, check row count
9. **Document everything**: keep a cleaning log or script with comments
10. **Save cleaned data**: separate file from raw data, never overwrite originals
