<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/pybondlab-report.md -->

# `/pybondlab-report`

Writes a structured results report after each PyBondLab portfolio-formation run, using a fixed naming convention for strategies.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/pybondlab-report/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/pybondlab-report/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/pybondlab-report/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Results Reporter

Automatically generates a structured report folder after every PyBondLab run.

### When to Apply

After any call to `StrategyFormation.fit()`, `BatchStrategyFormation.fit()`, `BatchWithinFirmSortFormation.fit()`, or `DataUncertaintyAnalysis.fit()` — always invoke the reporter before presenting results.

### Usage

```python
from PyBondLab.report import ResultsReporter

reporter = ResultsReporter(
    result=result,          # FormationResults or BatchResults
    mnemonic='cs_single_5', # short name
    script_text=SCRIPT,     # the Python code that produced result
    output_dir='results',   # root directory (or project scripts/tests/{test}/output/)
)
report_path = reporter.generate()
```

### Mnemonic Convention

| Strategy | Pattern | Example |
|----------|---------|---------|
| SingleSort | `{signal}_single_{nport}` | `cs_single_5` |
| DoubleSort | `{var1}_{var2}_double_{n1}x{n2}` | `rat_cs_double_3x5` |
| WithinFirmSort | `{signal}_wfs` | `cs_wfs` |
| Batch SingleSort | `batch_{n_signals}s` | `batch_3s` |
| Batch WithinFirm | `batchwfs_{n_signals}s` | `batchwfs_3s` |
| FF-style | `ff_{var1}_{var2}_{n1}x{n2}` | `ff_sze_bbtm_2x3` |

### Output Structure

**Single strategy:** `results/{mnemonic}_{YYYY_mm_dd}/` with `meta.json`, `script.py`, `tables/summary_stats.csv`, `figures/portfolio_premia.png`, `figures/factor_bars.png`, `figures/cumret_turnover.png`.

**Batch:** adds per-signal subfolders + `summary/factor_comparison.png`, `summary/summary_stats.csv`, and `summary/factor_panel.parquet` (sign-corrected tidy panel via `extract_panel` with `NamingConfig(sign_correct=True)`).

### Workflow

1. Capture the script text in a `SCRIPT` variable at the top of your code
2. Run the PyBondLab formation as normal
3. Call `ResultsReporter(result, mnemonic, script_text=SCRIPT).generate()`
4. Report the generated path and key statistics to the user
5. Save results under project's `scripts/tests/{test_name}/output/` when working within a project
