---
name: pybondlab-report
description: "Generates structured results reports after PyBondLab portfolio formation runs. Auto-apply when running StrategyFormation, BatchStrategyFormation, BatchWithinFirmSortFormation, or any portfolio sorting with PyBondLab."
---

# Results Reporter

Automatically generates a structured report folder after every PyBondLab run.

## When to Apply

After any call to `StrategyFormation.fit()`, `BatchStrategyFormation.fit()`, `BatchWithinFirmSortFormation.fit()`, or `DataUncertaintyAnalysis.fit()` — always invoke the reporter before presenting results.

## Usage

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

## Mnemonic Convention

| Strategy | Pattern | Example |
|----------|---------|---------|
| SingleSort | `{signal}_single_{nport}` | `cs_single_5` |
| DoubleSort | `{var1}_{var2}_double_{n1}x{n2}` | `rat_cs_double_3x5` |
| WithinFirmSort | `{signal}_wfs` | `cs_wfs` |
| Batch SingleSort | `batch_{n_signals}s` | `batch_3s` |
| Batch WithinFirm | `batchwfs_{n_signals}s` | `batchwfs_3s` |
| FF-style | `ff_{var1}_{var2}_{n1}x{n2}` | `ff_sze_bbtm_2x3` |

## Output Structure

**Single strategy:** `results/{mnemonic}_{YYYY_mm_dd}/` with `meta.json`, `script.py`, `tables/summary_stats.csv`, `figures/portfolio_premia.png`, `figures/factor_bars.png`, `figures/cumret_turnover.png`.

**Batch:** adds per-signal subfolders + `summary/factor_comparison.png`, `summary/summary_stats.csv`, and `summary/factor_panel.parquet` (sign-corrected tidy panel via `extract_panel` with `NamingConfig(sign_correct=True)`).

## Workflow

1. Capture the script text in a `SCRIPT` variable at the top of your code
2. Run the PyBondLab formation as normal
3. Call `ResultsReporter(result, mnemonic, script_text=SCRIPT).generate()`
4. Report the generated path and key statistics to the user
5. Save results under project's `scripts/tests/{test_name}/output/` when working within a project
