# Figure Specification Format

When producing figures, output a `figure_spec.json` file with actual data values.
The pipeline renders these specs into publication-quality PDFs deterministically.
Do NOT write matplotlib/seaborn code or attempt to generate figures yourself.

## Structure

```json
{
  "figures": [
    {
      "filename": "fig_coefficient_main.pdf",
      "figure_type": "coefficient",
      "label": "fig:main_coefficients",
      "caption_hint": "Main regression coefficients with 95% confidence intervals",
      ...type-specific fields...
    }
  ]
}
```

## Supported Figure Types

### coefficient — Horizontal coefficient plot with CIs
```json
{
  "figure_type": "coefficient",
  "coefficients": [
    {"name": "Treatment", "estimate": 0.15, "ci_lower": 0.08, "ci_upper": 0.22},
    {"name": "Post x Treat", "estimate": -0.03, "ci_lower": -0.10, "ci_upper": 0.04}
  ],
  "reference_line": 0,
  "x_label": "Effect size (percentage points)"
}
```

### event_study — Dynamic treatment effects
```json
{
  "figure_type": "event_study",
  "periods": [-4, -3, -2, -1, 0, 1, 2, 3, 4],
  "estimates": [0.01, -0.02, 0.00, 0.01, 0.15, 0.18, 0.20, 0.19, 0.17],
  "ci_lower": [-0.05, -0.08, -0.06, -0.05, 0.09, 0.12, 0.14, 0.13, 0.11],
  "ci_upper": [0.07, 0.04, 0.06, 0.07, 0.21, 0.24, 0.26, 0.25, 0.23],
  "treatment_period": 0,
  "x_label": "Periods relative to treatment",
  "y_label": "Coefficient estimate"
}
```

### time_series — Multi-series line plot
```json
{
  "figure_type": "time_series",
  "series": [
    {"label": "Treatment", "x": [1, 2, 3, 4, 5], "y": [10, 15, 22, 28, 35]},
    {"label": "Control", "x": [1, 2, 3, 4, 5], "y": [10, 12, 14, 16, 18]}
  ],
  "shaded_regions": [{"x_start": 3, "x_end": 5, "label": "Post-treatment"}],
  "x_label": "Month",
  "y_label": "Outcome variable"
}
```

### bar — Categorical comparison
```json
{
  "figure_type": "bar",
  "categories": ["Q1", "Q2", "Q3", "Q4"],
  "values": [12.5, 18.3, 15.7, 22.1],
  "errors": [2.1, 3.0, 2.5, 3.8],
  "y_label": "Returns (%)"
}
```

### binscatter — Binned scatter plot
```json
{
  "figure_type": "binscatter",
  "x": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
  "y": [2.1, 3.8, 5.2, 7.1, 8.9, 10.5, 12.3, 14.0, 15.8, 17.5],
  "fit_line": {"slope": 1.72, "intercept": 0.35},
  "x_label": "Log market cap",
  "y_label": "Average daily volume"
}
```

### distribution — Histogram with optional KDE
```json
{
  "figure_type": "distribution",
  "values": [0.1, 0.5, 0.8, 1.2, ...],
  "bins": 30,
  "kde_overlay": true,
  "vertical_lines": [{"x": 0.5, "label": "Median"}],
  "x_label": "Returns",
  "y_label": "Count"
}
```

### multi_panel — Grid of sub-figures
```json
{
  "figure_type": "multi_panel",
  "ncols": 2,
  "panels": [
    {"figure_type": "time_series", "title": "Panel A", ...},
    {"figure_type": "bar", "title": "Panel B", ...}
  ]
}
```

## Rules

1. Embed ACTUAL numeric values from estimation results. Never use placeholders.
2. Maximum ~10,000 data points per figure. Pre-bin distributions if needed.
3. Use descriptive filenames: `fig_coefficient_main.pdf`, `fig_event_study.pdf`.
4. Provide a `label` for LaTeX `\ref{}` and a `caption_hint` for the drafter.
5. Skip figure types that don't fit the methodology.
6. All axis labels should include units where applicable.
