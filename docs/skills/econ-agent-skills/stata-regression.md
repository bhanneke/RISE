<!-- DO NOT EDIT — auto-copied from skills/econ-agent-skills/details/stata-regression.md -->

# `/stata-regression`

Stata regression workflows on DIME Analytics conventions (ietoolkit, iefolder, a master do-file, ieboilstart, dynamic absolute path globals, iebaltab for balance, esttab for output) with modern estimators as the default: reghdfe for fixed effects, csdid / eventstudyinteract / did_imputation / jwdid for staggered DiD, ivreg2 with `weakid` plus weakivtest for weak instruments, boottest when clusters are few, and rdrobust for RDD. Every table is written to file by code — never copy-pasted from the console.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../econ-agent-skills/">Econ Agent Skills (Jonas Weinert)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> econometrics</div><div><b>License:</b> <code>CC0-1.0 per the repo LICENSE file and README ("CC0 1.0 — public domain"); GitHub's API reports the licence as NOASSERTION / "Other" — record both</code></div><div><b>Updated:</b> 2026-05-05</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code> · <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/JonasWeinert/EconAgentSkills/contents/_skills/analysis/stata-regression/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/econ-agent-skills/stata-regression/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/JonasWeinert/EconAgentSkills/blob/main/_skills/analysis/stata-regression/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/JonasWeinert/EconAgentSkills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Stata Regression

Generate rigorous, reproducible Stata code that follows DIME Analytics impact-evaluation conventions and uses modern econometric estimators. The default style is `ietoolkit` + `reghdfe` + `esttab`, with heterogeneity-robust DiD and weak-IV-robust inference baked in.

### Operating Principles

1. **Reproducibility before convenience.** Every script starts with `ieboilstart`, sets a seed, declares dynamic absolute paths via globals, and writes outputs to a `Results/` folder. Never `cd`, never use relative paths, never commit `.dta` files containing PII.
2. **Modern estimators by default.** Plain `xi: reg y treat##post` under staggered timing is biased; use `csdid`, `eventstudyinteract`, `did_imputation`, or `jwdid`. For weak instruments, use `ivreg2 ... weakid` and `weakivtest`. With few clusters, use `boottest`.
3. **`ietoolkit` is the house standard.** Use `iebaltab` for balance, `ieddtab` for simple two-period DiD, `iefolder` for project setup, `iegraph` for regression-result figures, and `iedropone` for safe drops.
4. **One do-file, one purpose.** Master do-file installs packages and routes to sub-do-files for cleaning, construction, analysis, and output. Each script must run end-to-end from a clean Stata session.
5. **Tables are produced, never copy-pasted.** All tables go through `esttab` to `.tex`, `.csv`, or `.rtf` — no manual editing.

### Decision Policy

This skill follows the repo-wide Agent Policy.

**ASK before proceeding** (blocking):

1. Estimand and identification strategy.
2. Treatment timing (uniform vs staggered) — drives `csdid` / `eventstudyinteract` / `did_imputation` vs plain TWFE.
3. Cluster level for inference (matches assignment level by default).
4. DataWork folder layout: which globals to use, where do tables/figures land.

**DEFAULT + flag** (use this default; tell the user how to override):

- `reghdfe` over `xtreg` / `areg` for high-dim FE.
- `csdid` (Callaway-Sant'Anna) as preferred staggered-DiD estimator; report TWFE as benchmark in `tab_did_estimators`.
- `ivreg2` + `weakivtest` with cluster-robust SEs for IV; switch to `condivreg` when effective F < 100.
- `boottest` wild cluster bootstrap when G < 30 or treatment is concentrated in a few clusters.
- `esttab` for tables; `coefplot` for figures; `iebaltab` for balance.
- Outputs to `${tabs}/` (.tex) and `${figs}/` (.pdf), declared by master do-file globals.

**DOCUMENT and proceed** (write into the decisions log):

- Specific estimator within an approved family.
- The cluster level and the number of clusters G.
- Any sample restriction beyond what the user named.
- Choice of bandwidth in RDD and sensitivity range.

`PROCEED` items: `ieboilstart`, dynamic absolute paths via globals, `isid`, `iedropone`, `assert`, `set seed`, never `cd`, never copy-paste numbers from the Results window.

### Pre-flight Checklist

Before writing code, confirm with the user — and write the answers as a header comment block:

- **Estimand.** ATT, LATE, ITT, sharp/fuzzy RD effect, descriptive, or balance check?
- **Unit of observation and panel keys.** Assert with `isid` (e.g. `isid hhid year`).
- **Treatment timing.** Single shock, simultaneous, staggered, or reversible?
- **Identifying variation.** Which comparison drives the coefficient?
- **Clustering level.** Where is treatment assigned, or where does within-group correlation live?
- **Sample.** Document each filter and report the resulting N.
- **Output target.** Working paper, slides, journal submission, or internal report.

### DIME Project Layout

Every analysis script assumes a `DataWork/` folder created by `iefolder`:

```
ProjectABC/
├── DataWork/
│   ├── MasterDoFile.do            # globals, packages, routes to sub-master files
│   ├── Baseline/
│   │   ├── DataSets/
│   │   │   ├── Raw/
│   │   │   ├── Intermediate/
│   │   │   └── Final/
│   │   ├── Dofiles/
│   │   │   ├── Cleaning/
│   │   │   ├── Construction/
│   │   │   └── Analysis/
│   │   ├── Output/
│   │   │   ├── Tables/
│   │   │   └── Figures/
│   │   └── Documentation/
│   └── Endline/
└── README.md
```

Globals are user-specific and defined only in the master do-file:

```stata
* Master do-file globals
if c(username) == "jonas"      global root "/Users/jonas/Dropbox/ProjectABC"
if c(username) == "coauthor"   global root "C:/Users/coauthor/Dropbox/ProjectABC"

global dataWork  "${root}/DataWork"
global baseline  "${dataWork}/Baseline"
global results   "${baseline}/Output"
```

### Estimator Decision Tree

#### Difference-in-Differences

```
Two periods, two groups, no staggered adoption
└── ieddtab y, t(time) treatment(treated)  // DIME-style two-period DD
    or:    reghdfe y treat_post, absorb(unit time) vce(cluster unit)

Staggered adoption (the realistic case)
└── Do NOT use plain TWFE. Choose one of:
    ├── csdid           → Callaway & Sant'Anna (2021)
    ├── eventstudyinteract → Sun & Abraham (2021)
    ├── did_imputation  → Borusyak, Jaravel & Spiess (2024)
    ├── did_multiplegt_dyn → de Chaisemartin & D'Haultfoeuille
    └── jwdid           → Wooldridge (2021), TWFE re-derivation

Continuous or non-binary treatment
└── did_multiplegt_dyn (de Chaisemartin & D'Haultfoeuille)
```

#### Instrumental Variables

```
Always estimate and report the first stage explicitly.

For 2SLS with diagnostics:
  ivreg2 y x_exog (endog = z), cluster(cluster_var) first

Weak-IV diagnostics:
  - ivreg2 reports Kleibergen-Paap rk Wald F
  - weakivtest after ivreg2 → Olea-Pflueger effective F
  - condivreg or rivtest → Anderson-Rubin / CLR confidence sets

Effective F (Olea-Pflueger):
  - F >= 100 → conventional t is fine
  - 10 <= F < 100 → use AR or tF-adjusted CI
  - F < 10  → instrument is weak; do not interpret 2SLS causally

Panel IV with high-dim FE:
  ivreghdfe y x_exog (endog = z), absorb(unit time) cluster(cluster_var) first
```

#### Regression Discontinuity

```
Sharp RDD:
  rdrobust y x, c(0)                            // Calonico-Cattaneo-Titiunik
  rdplot   y x, c(0) binselect(esmv)
  rddensity x, c(0)                              // density manipulation test

Fuzzy RDD:
  rdrobust y x, c(0) fuzzy(treatment)

Bandwidth sensitivity:
  Loop over h_opt/2, h_opt, 2*h_opt and report the table.
```

#### Inference

```
Number of clusters G:
  G >= 50      → vce(cluster cl) is fine
  30 <= G < 50 → reg2hdfe or boottest with t-statistic correction
  G < 30       → wild cluster bootstrap via boottest, type(rademacher)

Multi-way clustering:
  Use vce2way (or `, vce(cluster cl1 cl2)` in some commands).
  Only when there is real correlation along both dimensions.

Few-cluster small-sample fix in reghdfe:
  reghdfe y x, absorb(unit time) vce(cluster unit, suite(boot))
```

### Output Skeleton

Every analysis do-file should follow this structure:

```stata
*-------------------------------------------------------------*
* Project   : ProjectABC
* Purpose   : Main DiD specification on outcome Y
* Author    : First Last (email)
* Created   : 2026-05-05
* Inputs    : ${baseline}/DataSets/Final/analysis.dta
* Outputs   : ${results}/Tables/table_did_main.tex
*             ${results}/Figures/event_study.pdf
* Estimand  : ATT of program on outcome Y
* Cluster   : at the unit level (treatment assignment)
*-------------------------------------------------------------*

* 0. Settings
ieboilstart, version(17.0)
`r(version)'

* 1. Load and assert structure
use "${baseline}/DataSets/Final/analysis.dta", clear
isid unit_id year

* 2. Sample construction (log every drop)
iedropone if missing(outcome), error  // hard-fail if pattern is unexpected

* 3. Descriptives + balance
iebaltab age gender baseline_y, grpvar(treated) ///
    save("${results}/Tables/balance.xlsx") replace

* 4. Main specification
eststo clear
reghdfe outcome treat_post, absorb(unit_id year) vce(cluster unit_id)
eststo main

* 5. Robustness ladder
reghdfe outcome treat_post, absorb(unit_id year) vce(cluster unit_id year)
eststo twoway

reghdfe outcome treat_post controls, absorb(unit_id year) vce(cluster unit_id)
eststo controls

* 6. Export
esttab main twoway controls using "${results}/Tables/table_did_main.tex", ///
    replace booktabs label se ///
    stats(N r2_within, fmt(%9.0fc %9.3f) labels("Observations" "Within R2")) ///
    star(* 0.10 ** 0.05 *** 0.01) ///
    notes("Cluster-robust SEs in parentheses.")
```

### Common Pitfalls

- Plain `xi: reg y i.treat##i.post` with staggered timing — biased; use `csdid` or `eventstudyinteract`.
- Conditioning on first-stage F > 10 — biased; report Olea-Pflueger F and AR.
- `vce(cluster cl)` with very few clusters — undercoverage; use `boottest`.
- Hardcoded paths and `cd` — break collaboration; use globals from the master do-file.
- Copy-pasting tables into Word — kills reproducibility; always go through `esttab`.
- Quietly dropping observations — every drop should be logged or use `iedropone`.
- Saving `.dta` with PII or running scripts on raw confidential data — see DIME PII guidance.
- `xtreg, fe` for high-dim FE — slow and limited; use `reghdfe`.

### Additional Resources

- `reference.md` — extended code patterns for each estimator family.
- `examples/` — runnable do-files:
  - `examples/master.do` — DIME-style master do-file
  - `examples/reghdfe_baseline.do` — reghdfe + esttab workflow
  - `examples/iebaltab_balance.do` — balance tables with `iebaltab`
  - `examples/csdid_staggered.do` — Callaway-Sant'Anna in Stata
  - `examples/eventstudyinteract_sa.do` — Sun-Abraham event study
  - `examples/did_imputation_bjs.do` — BJS imputation estimator
  - `examples/ivreg2_weak.do` — IV with `weakivtest`
  - `examples/rdrobust_sharp.do` — sharp RDD with `rdrobust`
  - `examples/boottest_few_clusters.do` — wild cluster bootstrap

### Requirements

- Stata >= 16 (Stata 17+ recommended for `frames` and faster matrix ops).
- DIME packages: `ietoolkit`, `iefieldkit`.
- Estimation: `reghdfe`, `ivreg2`, `ivreghdfe`, `weakivtest`.
- Modern DiD: `csdid`, `did_imputation`, `did_multiplegt_dyn`, `eventstudyinteract`, `jwdid`.
- RDD: `rdrobust`, `rddensity`.
- Inference: `boottest`, `vce2way`.
- Tables and figures: `estout` (provides `esttab`), `coefplot`, `outreg2`.

```stata
* Run once, or include with `, replace` in the master do-file.
ssc install ietoolkit,        replace
ssc install iefieldkit,       replace
ssc install reghdfe,          replace
ssc install ftools,           replace        // dependency for reghdfe
ssc install ivreg2,           replace
ssc install ivreghdfe,        replace
ssc install ranktest,         replace        // dependency for ivreg2
ssc install weakivtest,       replace
ssc install csdid,            replace
ssc install drdid,            replace        // dependency for csdid
ssc install did_imputation,   replace
ssc install did_multiplegt_dyn, replace
ssc install eventstudyinteract, replace
ssc install jwdid,            replace
ssc install rdrobust,         replace
ssc install rddensity,        replace
ssc install boottest,         replace
ssc install estout,           replace
ssc install coefplot,         replace
ssc install outreg2,          replace
```

### References

#### DIME Conventions

- DIME Analytics, [Stata Coding Practices](https://dimewiki.worldbank.org/Stata_Coding_Practices)
- DIME Analytics, [Master Do-files](https://dimewiki.worldbank.org/Master_Do-files)
- DIME Analytics, [ietoolkit](https://dimewiki.worldbank.org/ietoolkit)
- DIME Analytics, [Reproducible Research](https://dimewiki.worldbank.org/Reproducible_Research)
- DIME Analytics, [Data Analysis](https://dimewiki.worldbank.org/Data_Analysis)
- DIME Analytics, [Difference-in-Differences](https://dimewiki.worldbank.org/Difference-in-Differences)
- *Development Research in Practice* (DIME Analytics handbook).

#### Methods

- Goodman-Bacon (2021). *DiD with Variation in Treatment Timing*. JoE.
- Callaway & Sant'Anna (2021). *DiD with Multiple Time Periods*. JoE.
- Sun & Abraham (2021). *Estimating Dynamic Treatment Effects in Event Studies*. JoE.
- Borusyak, Jaravel & Spiess (2024). *Revisiting Event Study Designs*. ReStud.
- Olea & Pflueger (2013). *A Robust Test for Weak Instruments*. JBES.
- Lee, McCrary, Moreira & Porter (2022). *Valid t-ratio Inference for IV*. AER.
- Calonico, Cattaneo & Titiunik (2014). *Robust Nonparametric CIs for RDD*. Econometrica.
- MacKinnon & Webb (2018). *Wild Bootstrap for Few (Treated) Clusters*. EJ.
