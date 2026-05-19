# Data Visualization Guide for Economics Research

## Chart Selection by Data Relationship

### Scatter Plot — Correlations and Cross-Sectional Relationships

Use when showing the relationship between two continuous variables across units.

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(df["log_gdp_pc"], df["life_expectancy"], s=20, alpha=0.6, edgecolors="none")
ax.set_xlabel("Log GDP per Capita")
ax.set_ylabel("Life Expectancy (years)")
ax.set_title("Income and Health, 2020")

# Add OLS fit line
sns.regplot(x="log_gdp_pc", y="life_expectancy", data=df, ax=ax,
            scatter=False, ci=95, line_kws={"color": "darkred", "linewidth": 1.5})
```

Enhancements: size points by population, color by region, add country labels for notable outliers.

### Line Plot — Time Series

Use for showing trends, cycles, and changes over time.

```python
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(df["date"], df["gdp_growth"], linewidth=1.2, color="#1f77b4")
ax.axhline(y=0, color="gray", linewidth=0.5, linestyle="--")

# Shade recessions (NBER dates)
for start, end in recession_dates:
    ax.axvspan(start, end, alpha=0.15, color="gray")

ax.set_xlabel("")
ax.set_ylabel("Real GDP Growth (%)")
ax.set_title("U.S. Real GDP Growth, 1970-2024")
```

For multiple series, keep the number of lines to 4-5 maximum. Use distinct colors and
add a legend outside the plot area if needed.

### Bar Chart — Comparisons Across Categories

Use for comparing values across discrete groups.

```python
fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.barh(df["country"], df["gini_coefficient"], color="#4c72b0", edgecolor="none")
ax.set_xlabel("Gini Coefficient")
ax.set_title("Income Inequality by Country, 2023")
ax.invert_yaxis()  # Highest value at top
```

Horizontal bars are preferred when category labels are long. Sort bars by value,
not alphabetically, unless there is a natural ordering.

### Coefficient Plot — Regression Results

Use instead of regression tables when the audience is broad or when comparing
many specifications.

```python
import numpy as np

fig, ax = plt.subplots(figsize=(6, 5))

# Assuming results from statsmodels
coefs = results.params[1:]  # Exclude intercept
ci_low = results.conf_int()[0][1:]
ci_high = results.conf_int()[1][1:]
names = coefs.index

y_pos = np.arange(len(names))
ax.errorbar(coefs, y_pos, xerr=[coefs - ci_low, ci_high - coefs],
            fmt="o", color="#333333", ecolor="#999999", capsize=3, markersize=5)
ax.axvline(x=0, color="red", linewidth=0.8, linestyle="--")
ax.set_yticks(y_pos)
ax.set_yticklabels(names)
ax.set_xlabel("Coefficient Estimate (95% CI)")
ax.set_title("OLS Estimates")
```

### Histogram / Density — Distributions

Use to show the shape of a variable's distribution.

```python
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(df["log_income"], bins=50, density=True, alpha=0.7, color="#4c72b0", edgecolor="white")
# Overlay kernel density
df["log_income"].plot.kde(ax=ax, color="darkred", linewidth=1.5)
ax.set_xlabel("Log Income")
ax.set_ylabel("Density")
```

### Heatmap — Correlation Matrices and Two-Dimensional Summaries

```python
corr = df[vars_of_interest].corr()
fig, ax = plt.subplots(figsize=(8, 7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0,
            vmin=-1, vmax=1, square=True, ax=ax,
            linewidths=0.5, cbar_kws={"shrink": 0.8})
```

### Binned Scatter Plot — Nonparametric Relationships

Common in applied economics (Chetty-style). Bins the x-variable and plots mean y within each bin.

```python
df["x_bin"] = pd.qcut(df["x"], q=20, duplicates="drop")
binned = df.groupby("x_bin").agg(x_mean=("x", "mean"), y_mean=("y", "mean")).reset_index()

fig, ax = plt.subplots(figsize=(6, 5))
ax.scatter(binned["x_mean"], binned["y_mean"], s=40, color="#333333", zorder=3)
ax.set_xlabel("X (binned means)")
ax.set_ylabel("Y (conditional mean)")
```

## Accessibility — Colorblind-Safe Palettes

Approximately 8% of men and 0.5% of women have color vision deficiency. Always design
for accessibility.

### Recommended Palettes

```python
# Paul Tol's qualitative palette (up to 7 colors)
tol_bright = ["#4477AA", "#EE6677", "#228833", "#CCBB44", "#66CCEE", "#AA3377", "#BBBBBB"]

# IBM Design Library colorblind-safe
ibm_cb = ["#648FFF", "#785EF0", "#DC267F", "#FE6100", "#FFB000"]

# Seaborn colorblind palette
sns.set_palette("colorblind")

# For sequential data: viridis, cividis, or inferno (perceptually uniform)
plt.cm.viridis
plt.cm.cividis  # Best for colorblind readers

# For diverging data: RdBu (red-blue), PiYG (pink-green)
```

### Additional Accessibility Guidelines

- Use shape and line style in addition to color to distinguish series.
- Ensure sufficient contrast (avoid light colors on white backgrounds).
- Add direct labels to lines rather than relying solely on legends.
- Use patterns or hatching in bar charts if color alone is insufficient.

```python
line_styles = ["-", "--", "-.", ":"]
markers = ["o", "s", "^", "D"]
for i, col in enumerate(columns):
    ax.plot(df["date"], df[col], linestyle=line_styles[i], marker=markers[i],
            markevery=10, label=col)
```

## Publication-Quality Settings

### Global Defaults

```python
import matplotlib as mpl

# Publication defaults
mpl.rcParams.update({
    "figure.figsize": (6.5, 4.5),       # Fits single-column journal width
    "figure.dpi": 150,                    # Screen display
    "savefig.dpi": 300,                   # Print quality
    "savefig.bbox": "tight",
    "savefig.transparent": False,
    "font.family": "serif",               # Or "sans-serif" for some journals
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "axes.linewidth": 0.8,
    "axes.spines.top": False,             # Remove top spine
    "axes.spines.right": False,           # Remove right spine
    "lines.linewidth": 1.2,
    "grid.alpha": 0.3,
    "grid.linewidth": 0.5,
})
```

### Saving for Publication

```python
# Vector formats for journals (scalable, small file size for line art)
fig.savefig("figure1.pdf", format="pdf")
fig.savefig("figure1.eps", format="eps")

# Raster for presentations or web
fig.savefig("figure1.png", format="png", dpi=300)

# For LaTeX integration
fig.savefig("figure1.pgf")  # Native LaTeX rendering of text
```

### Common Journal Requirements

| Journal Type        | Width (inches) | Font         | Format       |
|---------------------|----------------|--------------|--------------|
| Single column       | 3.25-3.5       | Matching journal | PDF/EPS  |
| Double column       | 6.5-7.0        | Matching journal | PDF/EPS  |
| AER / QJE / RES     | 6.5            | Times/Computer Modern | PDF |
| Presentation slides | 10 x 6         | Sans-serif   | PNG (high DPI) |

### Multi-Panel Figures

```python
fig, axes = plt.subplots(2, 2, figsize=(7, 6), constrained_layout=True)

for i, (ax, var) in enumerate(zip(axes.flat, variables)):
    ax.plot(df["date"], df[var])
    ax.set_title(f"({chr(97+i)}) {var_labels[var]}")  # (a), (b), (c), (d)

fig.savefig("figure_panels.pdf")
```

### Annotations and Notes

```python
# Source note below figure
fig.text(0.01, -0.02, "Source: FRED, Federal Reserve Bank of St. Louis.",
         fontsize=8, color="gray", ha="left", transform=fig.transFigure)

# Note about methodology
fig.text(0.01, -0.05, "Note: Shaded areas indicate NBER recession dates.",
         fontsize=8, color="gray", ha="left", transform=fig.transFigure)
```

## Quick Reference — Choosing the Right Chart

| Question                           | Chart Type           |
|------------------------------------|----------------------|
| How does Y relate to X?            | Scatter              |
| How does Y change over time?       | Line                 |
| How does Y differ across groups?   | Bar (horizontal)     |
| What is the distribution of Y?     | Histogram / density  |
| What are my regression estimates?  | Coefficient plot     |
| How do many variables correlate?   | Heatmap              |
| What is the nonparametric shape?   | Binned scatter       |
| How do two distributions compare?  | Overlaid densities   |
| What is the composition over time? | Stacked area         |
| Geographic variation?              | Choropleth map       |
