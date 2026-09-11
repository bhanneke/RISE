<!-- DO NOT EDIT — auto-copied from skills/econ-agent-skills/details/latex-tables.md -->

# `/latex-tables`

Produces publication-ready LaTeX tables from code — esttab/outreg2 in Stata, modelsummary or fixest::etable in R, stargazer or pyfixest.etable in Python — written directly into the paper's `tabs/` folder at DIME's "full replicability" tier, with booktabs three-line styling, threeparttable notes carrying SE type and cluster level, siunitx decimal alignment, and `Cref`-friendly labels. The .tex file is never hand-edited; the script is re-run instead.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../econ-agent-skills/">Econ Agent Skills (Jonas Weinert)</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>CC0-1.0 per the repo LICENSE file and README ("CC0 1.0 — public domain"); GitHub's API reports the licence as NOASSERTION / "Other" — record both</code></div><div><b>Updated:</b> 2026-05-05</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/JonasWeinert/EconAgentSkills/contents/_skills/writing/latex-tables/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/econ-agent-skills/latex-tables/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/JonasWeinert/EconAgentSkills/blob/main/_skills/writing/latex-tables/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/JonasWeinert/EconAgentSkills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## LaTeX Tables

Generate publication-ready LaTeX tables that come out of code (`esttab`, `modelsummary`, `pyfixest.etable`, `stargazer`) and `\input{}` cleanly into the paper. The default style follows DIME's "full replicability" tier: no manual editing between code and PDF.

### Operating Principles

1. **Tables are produced, never typed.** DIME identifies four [levels of replicability](https://dimewiki.worldbank.org/Exporting_Analysis): full, good, basic, and none. "None" (copy-paste from a console window) is unacceptable for any output that leaves the analyst. Default to **full**: code writes a `.tex` file that the paper `\input{}`s directly.
2. **One source of truth per table.** Every numeric cell, star, sample size, and footnote comes from the same script that ran the regression. Never edit the `.tex` file by hand — re-run the script and rebuild the paper.
3. **`booktabs` styling.** Three horizontal rules (`\toprule`, `\midrule`, `\bottomrule`), no vertical lines, consistent decimal alignment via `siunitx` `S` columns when precision matters.
4. **Notes via `threeparttable`.** Significance levels, standard-error type, sample restrictions, and clustering belong in a single notes block at the bottom — not in the caption.
5. **Cross-reference with `\Cref{}`.** `\label{tab:main}` + `\Cref{tab:main}` reads "Table 2" in body text and behaves correctly at sentence start.

### Decision Policy

This skill follows the repo-wide Agent Policy.

**ASK before proceeding** (blocking):

1. Source language of the regression (Stata / R / Python) — determines the canonical table package.
2. Table type (regression / summary stats / balance / multi-panel / DiD-estimator comparison).
3. Standard-error type and cluster level (these belong in the table notes).
4. Output target (LaTeX `.tex`, Word `.rtf`, Excel `.xlsx`).

**DEFAULT + flag** (use this default; tell the user how to override):

- `esttab` (Stata), `modelsummary` or `fixest::etable` (R), `pyfixest.etable` or `stargazer` (Python).
- `booktabs` styling: `\toprule`, `\midrule`, `\bottomrule`; no vertical lines.
- Three-star convention `* 0.10 ** 0.05 *** 0.01`; pin once per paper.
- `threeparttable` for the notes block.
- Output path `paper/tabs/<name>.tex`; the paper `\input{}`s it.
- Within-R² (`r2_within`) reported instead of overall R² for FE models.

**DOCUMENT and proceed** (write into the decisions log of the table-generating script):

- The estimating equation, sample, cluster level, and FE included for each column.
- Variable label mapping (`coef_map` / `coeflabels`).
- Any subsample restriction shown in a column.

`PROCEED` items: tables produced by code (never copy-paste); generated `.tex` never hand-edited; rebuild path runs the table script before LaTeX.

### Pre-flight Checklist

Before generating code, confirm with the user — and write the answers in the script header:

- **Source language.** Stata, R, or Python? (Each has its own canonical table package.)
- **Table type.** Regression (multi-spec), summary statistics, balance / difference-in-means, descriptive cross-tabs, or model-comparison panel?
- **Sample.** Single or stratified? If panel, which fixed effects are on/off across columns?
- **Standard errors.** Cluster-robust at which level? Wild-bootstrap p-values?
- **Stars and notes.** Conventional `*** ** *` cutoffs (1/5/10), or journal-specific (some require none)?
- **Output path.** Almost always `paper/tabs/{name}.tex`; the paper `\input{}`s that file.
- **Compile target.** `\begin{table}` floating environment in body, or naked `tabular` snippet to be included from a parent macro?

### Decision Tree (which table package to use)

```
Source = Stata
└── esttab (from estout) is canonical.
    eststo store; esttab using "tabs/x.tex", booktabs label se ...

Source = R
├── fixest models (most common in 2024-26): use fixest::etable
└── Mixed model classes: use modelsummary (works across lm, glm,
    PanelOLS, fixest, brms, ...). modelsummary writes .tex via
    `output = "tabs/x.tex"`.

Source = Python
├── pyfixest models: use pyfixest.etable
├── linearmodels models: use compare(...) + manual to_latex(), or
    pass models through stargazer
└── statsmodels OLS / GLM: use stargazer (Python port).

Output for Word
└── Same packages with .rtf or .docx output (esttab supports rtf;
    modelsummary supports docx via flextable).
```

### Output Path Convention

```
paper/
├── paper.tex
├── tabs/                       # all .tex tables; never hand-edited
│   ├── table_main.tex
│   ├── table_balance.tex
│   ├── table_summary.tex
│   └── table_robustness.tex
├── figs/
└── code/
    ├── stata/
    │   └── make_tables.do
    └── r/
        └── make_tables.R
```

Body text:

```latex
\Cref{tab:main} reports our preferred specification.
\input{tabs/table_main.tex}
```

The `.tex` file should produce the entire `\begin{table} ... \end{table}` environment so you only have one `\input{}` per table in the paper.

### Common Pitfalls

- Hand-editing the `.tex` file after generation. The next run will overwrite or diverge from the published numbers.
- Mixing significance-star conventions across tables (`*` at 0.05 in one, at 0.10 in another).
- Using `\hline` everywhere; readers expect three-line `booktabs` tables.
- Vertical lines in regression tables — never necessary, always ugly.
- Putting key information in the caption (e.g. "Standard errors clustered by firm") instead of in the notes block, where it can be longer and less awkward.
- Using `_` in variable labels without `\_` escaping; LaTeX silently interprets them as subscripts.
- Including raw column names like `treat_post` instead of human-readable labels.
- Numbers with inconsistent decimal precision across columns.
- Missing N row at the bottom of regression tables; reviewers will ask.
- Not exporting at all — running the regression in interactive mode and screenshotting the result. (This is "no replicability" in DIME's framework.)

### Additional Resources

- `reference.md` — extended patterns: balance tables, summary stats, panel tables, threeparttable notes, siunitx S-column alignment, multi-panel tables, journal-specific deviations.
- `examples/` — runnable scripts that produce real `.tex` files:
  - `examples/make_tables_esttab.do` — Stata regression + summary + balance via `esttab`
  - `examples/make_tables_modelsummary.R` — R via `modelsummary` + `fixest::etable`
  - `examples/make_tables_pyfixest.py` — Python via `pyfixest.etable`
  - `examples/make_tables_stargazer.py` — Python `statsmodels` via `stargazer`
  - `examples/table_main_template.tex` — minimal copy-paste-able tabular for "good replicability" cases
  - `examples/table_balance_template.tex` — DIME-style balance table layout

### Requirements

- LaTeX: TeX Live 2022+ or MacTeX 2022+; packages `booktabs`, `threeparttable`, `siunitx`, `caption`, `cleveref`.
- Stata: `ssc install estout` (provides `esttab`, `eststo`, `estadd`, `estpost`).
- R: `install.packages(c("modelsummary", "fixest", "kableExtra"))`.
- Python: `pip install stargazer pyfixest pandas`.

### References

#### DIME

- DIME Analytics, [Exporting Analysis](https://dimewiki.worldbank.org/Exporting_Analysis) — four levels of replicability.
- DIME Analytics, [Checklist: Submit Table](https://dimewiki.worldbank.org/Checklist:_Submit_Table).
- DIME Analytics, [Stata Coding Practices](https://dimewiki.worldbank.org/Stata_Coding_Practices) — `estout` family.

#### Style

- AEA, [Manuscript Style Guide](https://www.aeaweb.org/journals/aer/submissions/accepted-articles/styleguide).
- Jansen & Persson, *Nice and fast tables in Stata for LaTeX and Excel* — https://osf.io/78nuc/.
- Lukas Püttmann, [`esttab` cheat sheet](https://lukaspuettmann.com/esttab/).
- `booktabs` documentation — https://ctan.org/pkg/booktabs.
- `siunitx` — https://ctan.org/pkg/siunitx (S columns for decimal alignment).
