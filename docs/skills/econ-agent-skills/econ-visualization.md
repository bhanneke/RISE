<!-- DO NOT EDIT — auto-copied from skills/econ-agent-skills/details/econ-visualization.md -->

# `/econ-visualization`

Code-produced publication figures in ggplot2, matplotlib/seaborn, or Stata twoway/coefplot, exported as vector PDF straight into the paper's `figs/` folder, with a chart-type decision tree (event-study coefficient plots, balance plots, recession-shaded time series, binscatters, density plots, choropleths) and colourblind-safe Okabe-Ito or viridis palettes — never red-green for treatment versus control. Follows DIME's Reviewing Graphs checklist and separates caption-dependent paper figures from standalone visuals that need an in-figure title and a source line.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../econ-agent-skills/">Econ Agent Skills (Jonas Weinert)</a></div><div><b>Category:</b> <code>figures</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>CC0-1.0 per the repo LICENSE file and README ("CC0 1.0 — public domain"); GitHub's API reports the licence as NOASSERTION / "Other" — record both</code></div><div><b>Updated:</b> 2026-05-05</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code> · <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/JonasWeinert/EconAgentSkills/contents/_skills/communication/econ-visualization/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/econ-agent-skills/econ-visualization/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/JonasWeinert/EconAgentSkills/blob/main/_skills/communication/econ-visualization/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/JonasWeinert/EconAgentSkills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Economics Visualization

Generate publication-quality figures that come out of code and `\includegraphics{}` cleanly into the paper or `\frame{}` into the slides. The default style follows DIME's [Data Visualization](https://dimewiki.worldbank.org/Data_visualization) and [Reviewing Graphs checklist](https://dimewiki.worldbank.org/Checklist:_Reviewing_Graphs) guidance.

### Operating Principles

1. **Figures are produced, never screenshotted.** Same DIME [four-tier replicability](https://dimewiki.worldbank.org/Exporting_Analysis) as tables: full replicability means the script writes a vector file (`.pdf`/`.eps`/`.svg`) directly to `paper/figs/`.
2. **Vector first.** Save as PDF (or EPS for some journals; SVG for web). PNG only for raster content (maps, photos, screenshots).
3. **Color discipline.** Use a colorblind-safe palette by default (Okabe-Ito, viridis); reserve color for information; ensure the figure still reads in grayscale; never red-green for treatment-vs-control.
4. **Audience-aware annotation.** A figure embedded in a paper relies on the caption; a standalone figure (slide, dashboard, blog) needs an in-figure title, takeaway annotation, and source citation.
5. **Same dimensions everywhere.** Define one figure-size convention per project (e.g. `width = 6.5 in, height = 4 in` for paper figures; `width = 10 in, height = 5 in` for 16:9 slides) so every figure aligns visually.

### Decision Policy

This skill follows the repo-wide Agent Policy.

**ASK before proceeding** (blocking):

1. The single point the figure makes. (One figure, one claim.)
2. Audience: paper figure (rely on caption) vs standalone (needs in-figure title + source).
3. Chart type when more than one would work (e.g. event-study coefficient plot vs forest plot).
4. Color encoding — does color carry information, or is it decorative.

**DEFAULT + flag** (use this default; tell the user how to override):

- Okabe-Ito colorblind-safe palette; never red-green for treatment/control.
- Vector PDF (`device = cairo_pdf` in R; default in matplotlib) for paper figures.
- Paper figure dimensions `width = 6.5 in, height = 4 in`; slide figures `width = 10 in, height = 5.5 in`.
- `theme_paper()` in R / paper-wide rcParams in matplotlib / `scheme(white_tableau)` in Stata.
- Output to `paper/figs/<name>.pdf`; the paper `\includegraphics{}` directly.

**DOCUMENT and proceed** (write into the figure script header):

- Sample / filter applied for this specific figure (when different from the main estimation sample).
- Source of any external macro variable (e.g. NBER recession dates).
- Color and shape encoding choices for any non-default series.

`PROCEED` items: figures produced by code (never screenshotted); save vector format; `here::here()` / `pathlib` for paths; one script per figure; rebuild path runs figure scripts before LaTeX.

### Pre-flight Checklist

Before generating code, confirm with the user — and write the answers in the script header:

- **Question the figure answers.** A figure should make exactly one point.
- **Chart type.** Line / bar / scatter / coefficient plot / event study / binscatter / map / density / heatmap?
- **Data source and sample.** Where does the data come from; what filters apply?
- **Audience.** Paper figure (rely on caption) or standalone (needs title + source)?
- **Output target.** PDF for paper; PDF or PNG for slides; SVG for web.
- **Dimensions.** Width/height in inches; affects font sizing.
- **Color encoding.** Is color carrying information (yes → palette choice matters) or is it decorative (no → use a single accent color)?

### Decision Tree (chart type by question)

```
Comparing two groups over time
└── Two-line plot with vertical reference line at the event.
    Add a shaded confidence band if you have one.

Treatment effect dynamics (event study)
└── Coefficient plot: x = relative period, y = coefficient,
    error bars = 95% CI, vertical line at -1 (omitted period).

Magnitude of one effect across many specifications
└── Coefficient plot: y axis lists specifications, x axis shows
    point estimate + 95% CI; vertical line at 0.

Distribution of a variable in two groups
└── Overlapping density plots, or a violin plot if N is large.

Continuous-X relationship (with many obs)
└── Binscatter (binsreg in Stata; binsreg / binscatter in R).

Heterogeneity across categories
└── Forest plot (coefplot per category, sorted by point estimate).

Geographic variation
└── Choropleth (sf + ggplot2 in R; geopandas in Python; spmap in Stata).

Cross-section relationship
└── Scatter + line of best fit; consider log scales for skewed vars.

Time series with macro events
└── Line plot with shaded recession bars (NBER dates) and
    annotated key events.
```

### Project Layout

```
paper/
├── paper.tex
├── figs/                       # all .pdf figures; never hand-edited
│   ├── fig_event_study.pdf
│   ├── fig_balance.pdf
│   └── fig_time_series.pdf
└── code/
    ├── r/
    │   └── make_figures.R
    └── stata/
        └── make_figures.do
```

In the paper:

```latex
\begin{figure}[htbp]\centering
  \includegraphics[width=0.85\textwidth]{figs/fig_event_study.pdf}
  \caption{Event study of treatment effect on outcome Y.}
  \label{fig:event}
\end{figure}
```

### Color Palettes (colorblind-safe defaults)

```
R, ggplot2:
  scale_color_manual(values = c("#0072B2", "#D55E00", "#009E73",
                                "#F0E442", "#CC79A7", "#56B4E9"))
  # Okabe-Ito, used by default in scientific publishing.

Python, matplotlib:
  plt.rcParams["axes.prop_cycle"] = cycler(
      color = ["#0072B2", "#D55E00", "#009E73", "#F0E442",
               "#CC79A7", "#56B4E9"])

Sequential numeric (viridis):
  ggplot2: scale_*_viridis_c()
  matplotlib: cmap = "viridis"
  Stata: graph twoway, ... scheme(white_tableau)
```

Never use a red-green encoding for treatment/control — fails for ~8% of male readers.

### Output Skeleton (R, ggplot2)

```r
## make_figures.R header
## Project: ProjectABC
## Inputs : data/processed/analysis.parquet
## Outputs: paper/figs/fig_event_study.pdf
## Author : First Last
## Notes  : One figure per script section. Run as a whole.

library(ggplot2)
library(arrow)
library(here)

FIGS <- here("paper", "figs")
dir.create(FIGS, recursive = TRUE, showWarnings = FALSE)

theme_paper <- function(base_size = 11) {
  theme_minimal(base_size = base_size) +
    theme(panel.grid.minor = element_blank(),
          plot.title       = element_text(face = "plain"),
          plot.title.position = "plot",
          legend.position  = "bottom")
}

## (figure code)

ggsave(file.path(FIGS, "fig_event_study.pdf"),
       width = 6.5, height = 4, units = "in", device = cairo_pdf)
```

### Common Pitfalls

- Default ggplot/matplotlib themes for journal figures (gray panels, busy gridlines). Strip them.
- 3D bar charts and pie charts. Almost never the right choice.
- Two y-axes encoding different units. Hard to interpret; consider faceting instead.
- Tiny axis text on a paper figure that becomes unreadable when the page is printed.
- Inconsistent axis ranges between related figures. Force shared limits.
- Using "rainbow" colormaps (`jet`) — perceptually misleading. Use viridis/cividis.
- Forgetting to label units (`Percent`, `USD`, `Log GDP`).
- Including a legend with one entry. Use a direct title instead.
- Saving as PNG for a paper figure. Use PDF/EPS so the figure scales without pixelation.
- Pasting a figure that requires the audience to read tiny coefficient labels — replace with a coefficient plot.

### Additional Resources

- `reference.md` — extended patterns: event-study coefplot recipes, binscatter, recession-shaded time series, balance plot, choropleth maps, faceting.
- `examples/` — runnable scripts:
  - `examples/event_study_ggplot.R` — coefficient plot from `fixest::iplot` data
  - `examples/balance_plot_ggplot.R` — standardized differences plot
  - `examples/time_series_recessions.R` — line plot with shaded NBER recessions
  - `examples/binscatter_ggplot.R` — binsreg-style scatter
  - `examples/event_study_matplotlib.py` — same in Python
  - `examples/coefplot_stata.do` — Stata `coefplot` from `eststo` output
  - `examples/twoway_stata.do` — Stata `twoway` chart with shaded periods
  - `examples/theme_paper.R` — paper-wide ggplot2 theme

### Requirements

- R: `ggplot2`, `arrow`, `dplyr`, `here`, `viridis`, `sf`, `binsreg` (optional).
- Python: `matplotlib`, `seaborn`, `pandas`, `pyarrow`, `geopandas` (for maps).
- Stata: `coefplot`, `binsreg`, `spmap`, `colorpalette` (in `palettes` package).
- LaTeX: `graphicx`, `caption`, `subcaption`.

### References

#### DIME

- DIME Analytics, [Data Visualization](https://dimewiki.worldbank.org/Data_visualization).
- DIME Analytics, [Checklist: Reviewing Graphs](https://dimewiki.worldbank.org/Checklist:_Reviewing_Graphs).
- DIME Analytics, [Exporting Analysis](https://dimewiki.worldbank.org/Exporting_Analysis).
- DIME Analytics, [Stata Visual Library for Impact Evaluation](https://worldbank.github.io/Stata-IE-Visual-Library/).

#### Style and Theory

- Tufte (2001), *The Visual Display of Quantitative Information*.
- Cleveland (1993), *Visualizing Data*.
- Wilke (2019), *Fundamentals of Data Visualization* — https://clauswilke.com/dataviz/.
- Healy (2018), *Data Visualization: A Practical Introduction* — https://socviz.co/.
- Datawrapper, [What to Consider When Choosing Colors for Data Visualization](https://blog.datawrapper.de/colors/).
- Okabe & Ito, [Color Universal Design palette](https://jfly.uni-koeln.de/color/).

#### Tools

- ggplot2 — https://ggplot2.tidyverse.org/.
- matplotlib gallery — https://matplotlib.org/stable/gallery/.
- Stata `coefplot` (Jann) — https://repec.sowi.unibe.ch/stata/coefplot/.
