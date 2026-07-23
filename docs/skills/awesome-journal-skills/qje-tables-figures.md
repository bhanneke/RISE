<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-tables-figures.md -->

# `qje-tables-figures`

Finalizes main exhibits for a figure-forward QJE manuscript — clean tables and self-contained notes that read well in QJE's single-PDF, author-date format.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>figures</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-tables-figures/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-tables-figures/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-tables-figures/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Tables & Figures (qje-tables-figures)

### When to trigger

- The main result is a dense table with too many columns
- The paper is "table-heavy" when the design would land better as a figure
- Table notes are incomplete (sample, units, clustering, significance unclear)
- An event-study / RDD / binscatter result is hidden in a table instead of plotted

### QJE aesthetic: figure-forward, self-contained exhibits

QJE has moved firmly toward **figure-forward presentation** — the Opportunity Insights / Chetty-style QJE paper makes its central result legible in one well-designed graph (e.g., the binned mobility maps and exposure-effect plots of the QJE 2014/2018 neighborhoods papers). Identification designs are inherently visual: event-study plots, RDD discontinuity plots, and binned scatters communicate credibility better than a coefficient buried in a regression column. Tables remain essential for estimates and robustness, but the *headline* should often be a figure a reader grasps in five seconds. Practical QJE constraints: at initial submission **everything is one PDF with figures embedded** (no separate figure files), exhibits are numbered and called out in order, and in-text references are **author-date (Chicago)**.

### The headline-figure decision

| Design          | Headline figure                                              |
|-----------------|--------------------------------------------------------------|
| DID / event std | Event-study plot: leads ≈ 0, clean post-treatment dynamics   |
| RDD             | Discontinuity plot: binned means + local polynomial fit      |
| IV              | First-stage and reduced-form scatter / binscatter            |
| RCT             | Treatment-vs-control outcome distributions or effect-by-arm  |
| Descriptive     | The new fact, plotted with the data doing the talking        |

### Table craft

- **Width discipline.** Main results table should be readable; if it sprawls past a handful of columns, split it or move variants to the appendix (no page limit means you can — but readability still wins).
- **Self-contained notes.** Every table/figure note states: sample and time span, unit of observation, what each column is, fixed effects included, standard-error clustering level, and how significance is denoted.
- **Standard errors in parentheses**, clustering level named in the note; report N and relevant fit statistics.
- **Coefficients with meaning.** Report units so the magnitude is interpretable (effect in SDs, in dollars, in percentage points), not just a bare number.
- Author-date (Chicago) in-text references; figures and tables numbered and called out in order.

### Figure craft

- Show the data: binned scatters, confidence bands, and raw-ish patterns build credibility.
- Avoid chartjunk: no 3D, no needless color, legible axis labels with units; figures must remain legible embedded in the single submission PDF and at print resolution.
- Confidence intervals shown, not just point estimates; bandwidth/bin choices noted.
- A figure should be interpretable from its caption alone.

### Checklist

- [ ] The central result has a headline figure a reader grasps quickly
- [ ] Main table is readable; sprawling variants moved to the appendix
- [ ] Every exhibit note is self-contained (sample, units, FE, clustering, significance)
- [ ] Magnitudes are interpretable (units stated), not bare coefficients
- [ ] Event-study / RDD / first-stage results are plotted, not only tabulated
- [ ] Confidence intervals / bands shown on figures
- [ ] Figures embedded and legible in the single submission PDF; numbered, author-date citations

### Execution bridge (StatsPAI / Stata MCP)

Generate exhibits from the fitted result rather than retyping numbers (the usual source
of body-vs-appendix drift). Full map:
`shared-resources/empirical-methods/execution-with-mcp.md`.

- **Tables:** `etable` (multi-column) or `did_summary_to_latex` straight from the
  `result_id` — one definition, one set of numbers, body and appendix in sync.
- **Event-study / coefficient figures:** `plot_from_result`, `enhanced_event_study_plot`,
  `event_study_table` — axis units and the SE/clustering note baked in.
- **Every note** names the estimator + clustering (from the result's diagnostics) and
  states the magnitude in interpretable units. See a full fitted-result → exhibit chain
  in the JF execution walkthrough.

### Anti-patterns

- A 9-column main table when a single event-study figure would carry the result
- Table notes that omit the clustering level or the sample definition
- Reporting coefficients with no units, so magnitude is uninterpretable
- Decorative 3D/colored charts that add no information
- Burying the cleanest evidence (the discontinuity, the leads) in an appendix table

### Output format

```
【Headline exhibit】figure type chosen + why
【Main table】column count + what moved to appendix
【Notes audit】sample / units / FE / clustering / significance present? [Y/N each]
【Magnitude legibility】units stated? [Y/N]
【Figures plotted】[event study / RDD / first stage / ...]
【Next step】qje-writing-style
```
