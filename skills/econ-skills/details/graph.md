---
name: graph
description: Create, edit, fix, or style graphs, figures, choropleths, and regression tables for academic presentations. Use when asked to make, fix, or improve any visualization — including matplotlib plots, Lorenz curves, maps, scatter plots, binscatters, and LaTeX regression tables compiled to PDF.
argument-hint: <task: create|fix|style> [--path <script_or_notebook>] [--output <graph_folder>]
---

# Graph & Figure Manager

Create, edit, fix, and style publication-quality graphs and tables for academic presentations.

## Trigger conditions

Invoke this skill when the user asks to:
- Create / make / plot / draw a graph, figure, chart, or map
- Fix / debug a graph that looks wrong (colors, labels, overflow, blank colorbar, etc.)
- Style / improve / clean up an existing figure
- Create a regression table as a standalone LaTeX PDF
- Any task involving matplotlib, choropleth maps, Lorenz curves, binscatters, or similar

## Before starting

Read `graph_preferences.md` in this skill directory for all style rules, known bugs, and hard preferences. The preferences file is authoritative — follow it exactly.

## General principles

- **Always change source code, never outputs.** Edit the notebook/script that generates the figure. Never create side scripts to modify output PDFs/PNGs.
- **Compile and verify.** After any change, re-run the relevant cell(s) and check the output visually.
- **Save to the configured graphs directory.** Output path pattern: `<GRAPHS_OUTPUT_DIR>/{update_dir}/{topic}/`
- **PDF is default.** Save as `format='pdf', dpi=300`. Also save PNG if the user asks.
- **Square figures by default.** Use `(12, 12)` unless the content demands otherwise (e.g., choropleths use `(12, 7)`).

## Style quick reference

Refer to `graph_preferences.md` for full details. Key rules:

| Element | Setting |
|---------|---------|
| Colormap | `viridis` (default) |
| Title color | `rgb(43/255, 63/255, 94/255)` (navy) |
| Title fontsize | 24 |
| Subtitle fontsize | 14, gray |
| Axis labels | fontsize 20 |
| Tick labels | fontsize 16 |
| Legend | fontsize 15 |
| Lines | Solid only (no dashes except 45° equality line) |
| Figure size | `(12, 12)` square default, `(12, 7)` for maps |

## Hard rules

- **Square figures preferred.** Don't make rectangular unless asked.
- **No dashed/dotted lines.** Solid only. Dashed OK only for 45° equality line.
- **No Gini in legend.** Don't clutter legend labels with statistics.
- **Large fonts.** Presentations must be readable from the back of the room.
- **Never `bbox_inches='tight'` with inset axes** — breaks colorbar gradient in PDF (matplotlib bug).

## Task 1: Create

### Graphs / Figures
1. Identify the data source and what the figure should show.
2. Read `graph_preferences.md` for the relevant graph type (Lorenz, choropleth, scatter, etc.).
3. Write clean matplotlib code following all style rules.
4. Save PDF to the appropriate output path under `<GRAPHS_OUTPUT_DIR>`.
5. Verify output visually.

### Choropleth maps
Follow the detailed specs in `graph_preferences.md`:
- County background in light gray, MSA polygons with white edges
- Alaska and Hawaii insets at specified positions/sizes
- Colorbar via `fig.add_axes()` + `cax=` (never `ax=` with `shrink`)
- Dollar-formatted tick labels for monetary values
- `fig.subplots_adjust()` for margins (never `bbox_inches='tight'`)

### Regression tables (LaTeX → PDF)
Follow the pipeline in `graph_preferences.md`:
1. Run regressions with `pyfixest`
2. Build LaTeX string programmatically
3. Use `standalone` document class with `border=10pt`, `booktabs`
4. Use savebox pattern for table notes (critical — `\textwidth` doesn't work in standalone)
5. Stars: `$^{***}$` p<0.01, `$^{**}$` p<0.05, `$^{*}$` p<0.1
6. Negative sign: `$-$` (LaTeX math minus)
7. Compile with `pdflatex -interaction=nonstopmode`
8. Clean up `.aux`, `.log` files

## Task 2: Fix

1. Read the current code that generates the figure.
2. Identify the root cause (don't trial-and-error).
3. Common issues and fixes:
   - **Blank colorbar in PDF**: Using `bbox_inches='tight'` with insets. Switch to `fig.subplots_adjust()`.
   - **Colorbar whitespace**: `vmin`/`vmax` don't match tick boundaries. Snap to `floor`/`ceil`.
   - **Misaligned colorbar**: Using `ax=` instead of `cax=`. Switch to `fig.add_axes()`.
   - **Table notes too narrow**: Using `p{\textwidth}` in standalone. Use savebox pattern.
   - **Fonts too small**: Check against fontsize specs in preferences.
4. Fix in the source notebook/script, re-run, verify.

## Task 3: Style

1. Read the current figure and the preferences file.
2. Audit against every applicable rule (colors, fonts, line styles, figure size, etc.).
3. Apply changes to the source code.
4. Re-run and verify.
