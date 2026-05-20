<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/econ-visualization.md -->

# `econ-visualization`

Publication-quality charts and graphs for economics papers.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>figures</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/communication/econ-visualization/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/econ-visualization/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/communication/econ-visualization/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Econ Visualization

### Purpose

This skill creates publication-quality figures for economics papers, using clean styling, consistent scales, and export-ready formats.

### When to Use

- Building figures for empirical results and descriptive analysis
- Standardizing chart style across a paper or presentation
- Exporting figures to PDF or PNG at journal quality

### Instructions

Follow these steps to complete the task:

#### Step 1: Understand the Context

Before generating any code, ask the user:

- What is the dataset and key variables?
- What chart type is needed (line, bar, scatter, event study)?
- What output format and size are required?

#### Step 2: Generate the Output

Based on the context, generate code that:

1. **Uses a consistent theme** for academic styling
2. **Labels axes and legends clearly**
3. **Exports figures** at high resolution
4. **Includes reproducible steps** for data preparation

#### Step 3: Verify and Explain

After generating output:

- Explain how to regenerate or update the plot
- Suggest alternatives (log scales, faceting, smoothing)
- Note any data transformations used

### Example Prompts

- "Create an event study plot with confidence intervals"
- "Plot GDP per capita over time for three countries"
- "Build a scatter plot with fitted regression line"

### Example Output

```r
## ============================================
## Publication-Quality Figure in R
## ============================================
library(tidyverse)

df <- read_csv("data.csv")

ggplot(df, aes(x = year, y = gdp_per_capita, color = country)) +
  geom_line(size = 1) +
  scale_y_continuous(labels = scales::comma) +
  labs(
    title = "GDP per Capita Over Time",
    x = "Year",
    y = "GDP per Capita (USD)",
    color = "Country"
  ) +
  theme_minimal(base_size = 12) +
  theme(
    legend.position = "bottom",
    panel.grid.minor = element_blank()
  )

ggsave("figures/gdp_per_capita.pdf", width = 7, height = 4, dpi = 300)
```

### Requirements

#### Software

- R 4.0+ or Python 3.10+

#### Packages

- For R: `ggplot2`, `scales`, `dplyr`
- For Python: `matplotlib`, `seaborn` (optional alternative)

### Best Practices

1. **Use vector formats** (PDF, SVG) for publication
2. **Keep labels concise** and readable
3. **Document data filters** used in the figure

### Common Pitfalls

- Overcrowded plots without clear labeling
- Inconsistent scales across figures
- Exporting low-resolution images

### References

- [ggplot2 documentation](https://ggplot2.tidyverse.org/)
- [Tufte (2001) The Visual Display of Quantitative Information](https://www.edwardtufte.com/tufte/books_vdqi)

### Changelog

#### v1.0.0

- Initial release
