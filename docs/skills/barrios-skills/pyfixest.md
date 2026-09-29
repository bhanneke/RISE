<!-- DO NOT EDIT — auto-copied from skills/barrios-skills/details/pyfixest.md -->

# `pyfixest`

High-dimensional fixed-effects estimation in Python with pyfixest (fixest/reghdfe grammar) for firm-year and firm-quarter panels: multi-way FE with firm clustering, fixest-style multiple specifications, IV with FE, and staggered DiD through did2s and Sun-Abraham instead of naive TWFE. Its iron law is to fix the clustering level and the FE structure before estimating. It adds accounting and finance defaults and `pf.etable` output for journal tables, and routes simple two-way FE work to `python-panel-data` and R/Stata users to the sibling skills.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../barrios-skills/">Barrios Skills (John Manuel Barrios)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> econometrics</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2026 John Barrios"). The vendored third-party skills keep their own terms: the Anthropic document skills say "Proprietary. LICENSE.txt has complete terms", and the K-Dense skills carry per-library licence lines.</code></div><div><b>Updated:</b> 2026-07-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code> · <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Barrios88/barrios-skills/contents/skills/econometrics/pyfixest/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/barrios-skills/pyfixest/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Barrios88/barrios-skills/blob/main/skills/econometrics/pyfixest/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Barrios88/barrios-skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Barrios Skills** — John Barrios's curated workflow for economists and accountants. Prioritize reproducible empirical work, clear identification language, and journal-ready output.

## PyFixest for empirical accounting & finance

### When to use

- Firm–year / firm–quarter panels with firm and year (or industry×year) fixed effects
- High-dimensional FE that are slow in `linearmodels` or plain `statsmodels`
- IV with FE, Poisson/PPML with FE, or modern DiD helpers in Python
- You already know Stata `reghdfe` / R `fixest` and want the same grammar in Python

**Prefer** `python-panel-data` when the design is a simple two-way FE / RE with `linearmodels` and you want textbook panel diagnostics. **Prefer** `r-econometrics` / Stata skills when the paper's replication package is R/Stata-first.

### Install

```bash
python -m pip install pyfixest
## optional: python -m pip install "pyfixest[plots]"
```

Docs: [pyfixest.org](https://pyfixest.org/pyfixest.html)

### Iron law: specify clustering and FE before estimating

1. State the **unit of treatment / residual correlation** (usually firm, sometimes industry or CEO)
2. State **fixed effects** that absorb the design (firm + year; firm + industry×year; etc.)
3. Estimate with matching `vcov` / cluster
4. Inspect N, absorbed FE counts, and a coefficient sample before writing results into a paper

### Quick patterns

#### OLS with multi-way FE + firm clustering

```python
import pyfixest as pf

fit = pf.feols(
    "roa ~ treat + size + mb | gvkey + fyear",
    data=df,
    vcov={"CRV1": "gvkey"},
)
fit.summary()
```

#### Multiple specs (fixest-style)

```python
fit = pf.feols(
    "roa ~ treat + size | gvkey + fyear",
    data=df,
    vcov={"CRV1": "gvkey"},
)
## Compare specs with pf.etable([...]) for paper tables
```

#### IV with FE

```python
fit = pf.feols(
    "y ~ 1 | gvkey + fyear | endog ~ instrument",
    data=df,
    vcov={"CRV1": "gvkey"},
)
```

#### Staggered DiD / event study

Prefer package DiD helpers (`did2s`, Sun-Abraham / local projections as documented upstream) over naive TWFE when adoption is staggered. Report an event-study plot from a robust estimator, not only TWFE — see `econ-writing-plus` for narrative conventions.

### Accounting / finance defaults

| Design | Typical FE | Cluster |
|--------|------------|---------|
| Firm–year treatment | `gvkey + fyear` | firm (`gvkey`) |
| Industry shock | `gvkey + fyear` or `gvkey + industry^fyear` | firm; sometimes industry |
| CEO / executive panel | exec + year or firm + year | firm or exec (justify) |
| State policy | firm + year | firm; often state×year FE debate in text |

### Journal-ready output

- Export LaTeX via pyfixest / maketables helpers; pair with `latex-tables` for house style
- Report within R² / FE set / cluster level in table notes
- Never paste coefficients without SE and N

### Checklist before claiming results

- [ ] Sample filters documented (Compustat `indfmt/datafmt/popsrc/consol` if from WRDS)
- [ ] FE and cluster match the identification story
- [ ] Staggered timing → not only TWFE
- [ ] One exhibit inspected (sign, magnitude, N) against a raw crosstab
