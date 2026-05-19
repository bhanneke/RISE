<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/econ-visualization.md -->

# `econ-visualization`

Publication-quality charts and graphs for economics papers.

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

---
name: econ-visualization
description: Create publication-quality charts and graphs for economics papers.
workflow_stage: communication
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
author: Awesome Econ AI Community
version: 1.0.0
tags:
  - visualization
  - ggplot2
  - charts
  - publication
---

# Econ Visualization

## Purpose

This skill creates publication-quality figures for economics papers, using clean styling, consistent scales, and export-ready formats.

## When to Use

- Building figures for empirical results and descriptive analysis
- Standardizing chart style across a paper or presentation
- Exporting figures to PDF or PNG at journal quality

## Instructions

Follow these steps to complete the task:

### Step 1: Understand the Context

Before generating any code, ask the user:

- What is the dataset and key variables?
- What chart type is needed (line, bar, scatter, event study)?
- What output format and size are required?

### Step 2: Generate the Output

Based on the context, generate code that:

1. **Uses a consistent theme** for academic styling
2. **Labels axes and legends clearly**
3. **Exports figures** at high resolution
4. **Includes reproducible steps** for data preparation

### Step 3: Verify and Explain

After generating output:

- Explain how to regenerate or update the plot
- Suggest alternatives (log scales, faceting, smoothing)
- Note any data transformations used

## Example Prompts

- "Create an event study plot with confidence intervals"
- "Plot GDP per capita over time for three countries"
- "Build a scatter plot with fitted regression line"

## Example Output

```r
# ============================================
# Publication-Quality Figure in R
# ============================================
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

## Requirements

### Software

- R 4.0+ or Python 3.10+

### Packages

- For R: `ggplot2`, `scales`, `dplyr`
- For Python: `matplotlib`, `seaborn` (optional alternative)

## Best Practices

1. **Use vector formats** (PDF, SVG) for publication
2. **Keep labels concise** and readable
3. **Document data filters** used in the figure

## Common Pitfalls

- Overcrowded plots without clear labeling
- Inconsistent scales across figures
- Exporting low-resolution images

## References

- [ggplot2 documentation](https://ggplot2.tidyverse.org/)
- [Tufte (2001) The Visual Display of Quantitative Information](https://www.edwardtufte.com/tufte/books_vdqi)

## Changelog

### v1.0.0

- Initial release


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/communication/econ-visualization/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>meleantonio/awesome-econ-ai-stuff</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../awesome-econ-ai-stuff.md">awesome-econ-ai-stuff (Antonio Mele)</a></dd>
<dt><b>Category</b></dt><dd><code>figures</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>Other (see repo)</dd>
<dt><b>Last update</b></dt><dd>2026</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff">⭐ meleantonio/awesome-econ-ai-stuff</a><br><img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/communication/econ-visualization/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/econ-visualization/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
