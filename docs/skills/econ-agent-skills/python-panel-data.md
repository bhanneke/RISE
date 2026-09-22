<!-- DO NOT EDIT — auto-copied from skills/econ-agent-skills/details/python-panel-data.md -->

# `/python-panel-data`

Panel and causal-inference code in Python via pyfixest, linearmodels.PanelOLS, and statsmodels, with correct fixed effects, two-way clustering, IV2SLS, event studies through `sunab`, weak-IV diagnostics, and the wildboottest package below 30 clusters. Unusually candid about the ecosystem gap: for Callaway-Sant'Anna, Borusyak-Jaravel-Spiess, or de Chaisemartin-D'Haultfoeuille it routes the user to the R or Stata skill (or rpy2) rather than improvising, and documents the cross-language jump in the decisions log.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../econ-agent-skills/">Econ Agent Skills (Jonas Weinert)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> econometrics</div><div><b>License:</b> <code>CC0-1.0 per the repo LICENSE file and README ("CC0 1.0 — public domain"); GitHub's API reports the licence as NOASSERTION / "Other" — record both</code></div><div><b>Updated:</b> 2026-05-05</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code> · <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/JonasWeinert/EconAgentSkills/contents/_skills/analysis/python-panel-data/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/econ-agent-skills/python-panel-data/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/JonasWeinert/EconAgentSkills/blob/main/_skills/analysis/python-panel-data/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/JonasWeinert/EconAgentSkills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Python Panel Data

Generate rigorous panel and causal-inference code in Python. The modern Python ecosystem is `pyfixest` for `fixest`-style speed and syntax, `linearmodels.PanelOLS` for textbook panel models, and `statsmodels` for general purpose. Where Python's modern-DiD support is incomplete, point the user to R.

### Operating Principles

1. **Identification before code.** State the estimand, the source of identifying variation, and the threats to identification before writing any model.
2. **Use `pyfixest` first when speed and modern syntax matter.** Fall back to `linearmodels.PanelOLS` for textbook panel models, `statsmodels` for general regression and IV with simple specs.
3. **Be honest about ecosystem gaps.** Python's heterogeneity-robust DiD support is weaker than R or Stata. For Callaway-Sant'Anna, BJS, or de Chaisemartin-D'Haultfoeuille, use the corresponding R or Stata skill, or call R via `rpy2`.
4. **Reproducibility discipline.** Pin versions in `pyproject.toml` or `requirements.txt`. Use `pathlib` for paths, `pd.read_*` with `dtype=` arguments, and seed every random call.
5. **Tables are produced, never copy-pasted.** Use `pyfixest.etable`, `linearmodels` LaTeX export, or `stargazer` for `statsmodels`.

### Decision Policy

This skill follows the repo-wide Agent Policy.

**ASK before proceeding** (blocking):

1. Estimand and identification strategy.
2. Library choice when both apply: `pyfixest` for speed and modern syntax vs `linearmodels.PanelOLS` for textbook panel API.
3. Cluster level for inference.
4. Whether to switch language (R / Stata) for parts where Python's ecosystem is weaker (Callaway-Sant'Anna, BJS, AR weak-IV CIs).

**DEFAULT + flag** (use this default; tell the user how to override):

- `pyfixest.feols` for panel TWFE, event studies (`sunab`), and IV with FE.
- `linearmodels.PanelOLS` when the user wants explicit `EntityEffects` / `TimeEffects` / RandomEffects / FirstDifferenceOLS.
- `statsmodels` only for cross-section logit/probit/GLM/simple OLS.
- `wildboottest` package when G < 30; otherwise `vcov = {"CRV1": "unit"}`.
- Outputs as parquet in `data/processed/`; tables to `paper/tabs/` via `pyfixest.etable`.

**DOCUMENT and proceed** (write into the decisions log):

- Library choice and the reason if non-default.
- Panel structure (balanced / unbalanced / rotating) inferred from the data.
- Cross-language jumps (e.g. "Used R `did` package via subprocess for Callaway-Sant'Anna because no mature Python equivalent").

`PROCEED` items: `pyproject.toml` + lockfile, `Path(__file__).resolve().parents[N]`, `numpy.random.default_rng(20240101)`, `assert df.duplicated([keys]).sum() == 0` after every load.

### Pre-flight Checklist

Before writing code, confirm with the user — and write the answers as a header docstring:

- **Estimand.** ATT, LATE, ITT, descriptive?
- **Unit of observation and panel keys.** Assert with `df.duplicated(["unit", "time"]).sum() == 0`.
- **Treatment timing.** Single shock, simultaneous, staggered, or reversible?
- **Identifying variation.** Which comparison drives the coefficient?
- **Clustering level.** Where is treatment assigned, or where does within-group correlation live?
- **Sample.** Document each filter with sample sizes.
- **Output target.** Working paper, slides, journal submission, or exploratory.

### Library Choice

| Need | Library | Notes |
|------|---------|-------|
| Panel TWFE, event studies, IV with FE | `pyfixest` | Fastest; mirrors R `fixest`; `feols`, `fepois`, `iplot` |
| Textbook panel: PanelOLS, RandomEffects, FirstDifferenceOLS, BetweenOLS | `linearmodels` | Rich panel API; explicit `EntityEffects`, `TimeEffects` |
| Cross-section IV2SLS, GMM | `linearmodels` | `IV2SLS`, `IVGMM` |
| Logit/probit, GLM, simple OLS | `statsmodels` | Standard, well-documented |
| Tables (multiple models) | `pyfixest.etable`, `stargazer`, `linearmodels` `compare()` | Pick one and stick with it |

Install:

```bash
pip install pyfixest linearmodels statsmodels pandas pyarrow stargazer
```

### Estimator Decision Tree

#### Difference-in-Differences

```
Single shock, two groups, uniform timing
└── pyfixest.feols("y ~ treat_post | unit + time", data=df,
                   vcov={"CRV1": "unit"})

Staggered adoption (the realistic case)
├── Sun-Abraham via pyfixest:
│     pyfixest.feols("y ~ sunab(cohort, time) | unit + time",
│                    data=df, vcov={"CRV1": "unit"})
├── BJS imputation: not yet a polished package; implement manually
│   or use the `differences` package (limited).
└── Callaway-Sant'Anna: use R `did` via rpy2, or switch to the
    R or Stata skill for that estimator.

Continuous or non-binary treatment
└── No mature Python implementation. Use Stata
    `did_multiplegt_dyn` or R `DIDmultiplegt`.
```

#### Instrumental Variables

```
Cross-section 2SLS:
  from linearmodels import IV2SLS
  IV2SLS.from_formula("y ~ 1 + x_exog + [endog ~ z]", data=df).fit(
      cov_type="clustered", clusters=df.cluster
  )

Panel IV with high-dim FE:
  pyfixest.feols("y ~ x_exog | unit + time | endog ~ z",
                 data=df, vcov={"CRV1": "unit"})

Weak-IV diagnostics:
  - linearmodels reports Kleibergen-Paap rk Wald F.
  - For Olea-Pflueger effective F or AR sets, use R `ivDiag`,
    Stata `weakivtest`, or implement AR by hand.

Effective F:
  - F >= 100 → conventional 2SLS is fine.
  - 10 <= F < 100 → use AR or tF; do not rely on conventional t.
  - F < 10  → instrument is weak; do not interpret 2SLS causally.
```

#### Inference

```
Number of clusters G:
  G >= 50      → cluster-robust SE is fine
  30 <= G < 50 → consider HC3-style small-sample correction
  G < 30       → use wild cluster bootstrap (`pyfixest` supports
                 `wildboottest` via the `wildboottest` package)
                 or call Stata `boottest` / R `fwildclusterboot`.

Multi-way clustering:
  pyfixest:    vcov={"CRV1": ["unit", "year"]}
  linearmodels: cov_type="clustered", clusters=df[["unit", "year"]]
```

### Output Skeleton

Every analysis script should follow:

```python
"""
analysis_main.py
Project: ProjectABC
Purpose: Main DiD specification on outcome Y
Inputs : data/processed/analysis.parquet
Outputs: results/tables/table_did_main.tex
         results/figures/event_study.pdf
Estimand: ATT of program on Y
Cluster : at the unit level (treatment assignment)
"""
from pathlib import Path
import pandas as pd
import pyfixest as pf

PROJECT = Path(__file__).resolve().parents[2]
DATA_FINAL = PROJECT / "data" / "processed"
RESULTS    = PROJECT / "results"
RESULTS.joinpath("tables").mkdir(parents=True, exist_ok=True)
RESULTS.joinpath("figures").mkdir(parents=True, exist_ok=True)

## 1. Load and assert structure
df = pd.read_parquet(DATA_FINAL / "analysis.parquet")
assert df.duplicated(["unit_id", "year"]).sum() == 0

## 2. Sample construction
df = df.dropna(subset=["outcome"])  # log this filter

## 3. Main and robustness specs
m_main = pf.feols("outcome ~ treat_post | unit_id + year",
                  data=df, vcov={"CRV1": "unit_id"})
m_two  = pf.feols("outcome ~ treat_post | unit_id + year",
                  data=df, vcov={"CRV1": ["unit_id", "year"]})

## 4. Export
pf.etable([m_main, m_two],
          type="tex",
          file_name=str(RESULTS / "tables" / "table_did_main.tex"))
```

### Common Pitfalls

- Plain TWFE on staggered timing in `pyfixest` is just as biased as in `fixest`. Use `sunab` or switch language.
- Forgetting to set the panel index in `linearmodels`. Always `df.set_index(["unit", "time"])` before `PanelOLS.from_formula`.
- Cluster-robust SE with very few clusters — undercoverage; use wild bootstrap.
- Mixing `pyfixest` and `linearmodels` results in the same table — they sometimes treat absorbed FE differently. Stay within one framework per table.
- Hardcoded paths — use `pathlib.Path(__file__).resolve().parents[N]`.
- `df["x"] = ...` after a chained operation losing `.copy()` — use `df = df.assign(...)` or explicit `.copy()`.

### Additional Resources

- `reference.md` — extended code patterns for each estimator family.
- `examples/` — runnable scripts:
  - `examples/twfe_pyfixest.py` — TWFE with pyfixest
  - `examples/twfe_linearmodels.py` — TWFE with linearmodels.PanelOLS
  - `examples/event_study_sun_abraham.py` — Sun-Abraham via pyfixest
  - `examples/iv_panel_pyfixest.py` — panel IV with diagnostics
  - `examples/clustered_inference.py` — multi-way clustering and CR2
  - `examples/balance_table.py` — pandas + scipy balance tables

### Requirements

- Python >= 3.10
- Core: `pandas`, `pyarrow`, `numpy`, `scipy`
- Econometrics: `pyfixest`, `linearmodels`, `statsmodels`
- Tables and plots: `stargazer`, `matplotlib`

```bash
pip install pandas pyarrow numpy scipy pyfixest linearmodels statsmodels stargazer matplotlib
```

### References

- Berge (2018), `fixest`: Fast Fixed Effects Estimation. Original reference for the `fixest`/`pyfixest` family.
- Sun & Abraham (2021). *Estimating Dynamic Treatment Effects in Event Studies*. JoE.
- Borusyak, Jaravel & Spiess (2024). *Revisiting Event Study Designs*. ReStud.
- Olea & Pflueger (2013). *A Robust Test for Weak Instruments*. JBES.
- Wooldridge (2010). *Econometric Analysis of Cross Section and Panel Data*.
- DIME Analytics, [Reproducible Research](https://dimewiki.worldbank.org/Reproducible_Research).
- DIME Analytics, [Data Analysis](https://dimewiki.worldbank.org/Data_Analysis).
- pyfixest documentation: https://py-econometrics.github.io/pyfixest/
- linearmodels documentation: https://bashtage.github.io/linearmodels/
