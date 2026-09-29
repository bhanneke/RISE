<!-- DO NOT EDIT — auto-copied from skills/barrios-skills/details/econ-writing-plus.md -->

# `econ-writing-plus`

Method-specific writing conventions for identification sections, covering 13 designs (RCT, DiD, IV, RDD, synthetic control and synthetic DiD, structural, descriptive, bunching, shift-share, event studies, causal ML, multi-strategy), with modern DiD reporting guidance (Goodman-Bacon, Callaway-Sant'Anna, Sun-Abraham, de Chaisemartin-D'Haultfoeuille). Also covers AEA replication-package standards, AI-use disclosure, ERC grant structure, macro/trade/finance conventions, title evaluation, and turning significance into economic magnitudes. It is written as a supplement to writing skills that the repo does not ship.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../barrios-skills/">Barrios Skills (John Manuel Barrios)</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2026 John Barrios"). The vendored third-party skills keep their own terms: the Anthropic document skills say "Proprietary. LICENSE.txt has complete terms", and the K-Dense skills carry per-library licence lines.</code></div><div><b>Updated:</b> 2026-05-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code> · <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Barrios88/barrios-skills/contents/skills/writing-and-review/econ-writing-plus/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/barrios-skills/econ-writing-plus/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Barrios88/barrios-skills/blob/main/skills/writing-and-review/econ-writing-plus/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Barrios88/barrios-skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Barrios Skills** — John Barrios's curated workflow for economists and accountants. Prioritize reproducible empirical work, clear identification language, and journal-ready output.

## Econ Writing Plus

Advanced, method-specific additions to the existing economic-writing skill set. **Use alongside** `economic-writing`, `econ-humanizer`, `research-grants`, `pre-submission-review`, and `referee-report` — not instead of them.

**When in doubt:** default to the broader econ skills for general structure (abstract, intro, conclusion, review). Invoke this skill for:
- Writing or reviewing an identification section — see `identification-strategies.md`
- Preparing AEA / Econometrica / EJ submission compliance
- ERC grant proposals (the existing research-grants skill only covers NSF/NIH/DOE/DARPA)
- Field-specific conventions in macro, trade, or finance
- Title evaluation
- Translating statistical significance into economic magnitudes

---

### 1. IDENTIFICATION STRATEGIES (Primary Reference)

See identification-strategies.md for detailed writing conventions for each of the following:

- **Randomized Controlled Trials (RCTs)** — ITT vs. LATE, attrition, spillovers, take-up
- **Difference-in-Differences (DiD)** — parallel trends, event study, modern estimators
- **Instrumental Variables (IV)** — instrument relevance, exclusion restriction, complier population, Anderson-Rubin CIs
- **Regression Discontinuity (RDD)** — running variable, McCrary density test, bandwidth sensitivity, LOCAL interpretation
- **Synthetic Control** — donor pool, pre-treatment fit, placebo inference
- **Synthetic DiD** (Arkhangelsky et al.) — doubly robust, unit + time weights
- **Structural Estimation** — identifying vs. functional-form assumptions, model fit, counterfactuals as payoff
- **Descriptive / Measurement** — explicitly disclaim causality, data construction as contribution
- **Bunching Estimation** (Saez, Kleven) — counterfactual distribution, optimization frictions
- **Shift-Share / Bartik** — share vs. shift exogeneity (Goldsmith-Pinkham et al.; Borusyak-Hull-Jaravel), leave-one-out
- **Event Studies** — pre-period coefficients, normalization, staggered-event estimators
- **ML for Causal Inference** — Causal Forests, double/debiased ML, cross-fitting
- **Multi-strategy papers** — name a primary, frame others as complementary

#### Modern DiD estimator guidance (critical for current submissions)

If a DiD paper uses staggered treatment adoption, do NOT present only two-way fixed effects. Use:

- **Goodman-Bacon (2021) decomposition** to show which 2×2 comparisons drive the TWFE estimate (exposes negative-weight problem)
- **Callaway & Sant'Anna (2021)** for heterogeneous treatment effects over time
- **Sun & Abraham (2021)** for event-study specifications under staggered adoption
- **de Chaisemartin & D'Haultfoeuille (2020)** for the no-sign-reversal assumption

Present results from BOTH traditional TWFE and a robust estimator. If they differ, explain why (negative weights, treatment effect heterogeneity). The event-study plot should come from the robust estimator, not the TWFE version.

#### Adapting the introduction by paper type

| Paper Type | Hook Strategy | Paragraphs 4-6 | Key Threat |
|-----------|--------------|----------------|-----------|
| RCT | Policy relevance of intervention | ITT and LATE estimates | Attrition, spillovers, external validity |
| DiD | Policy change / natural experiment | Main DiD + event study | Parallel trends, anticipation |
| IV | The instrument and why it's clever | OLS vs. IV comparison | Exclusion restriction, weak instruments |
| RDD | The cutoff and its stakes | RD estimate + bandwidth sensitivity | Manipulation, other discontinuities |
| Synthetic Control | Treated unit + event | Synthetic vs. actual trajectory | Pre-treatment fit, donor pool |
| Synthetic DiD | Policy change + few treated units | Synth-DiD vs. DiD vs. SC | Parallel trends, synth-control fit |
| Structural | Question requiring a model | Counterfactual results | Model assumptions, external validity |
| Theory | Puzzle the model resolves | Main proposition + intuition | Robustness to assumptions |
| Descriptive | Why the fact matters | Key patterns with magnitudes | Measurement validity, sample selection |
| Bunching | Policy kink/notch + affected group | Elasticity + bunching plot | Optimization frictions, manipulation |
| Shift-Share | Shock + local exposure | Main estimate + leave-one-out | Share exogeneity, shock exogeneity |
| Event Study | Event + stakes | Plot + key coefficients | Pre-trends, anticipation |
| ML/Causal | Prediction or heterogeneity question | ML vs. parametric comparison | Overfitting, interpretability |

---

### 2. AEA REPLICATION PACKAGE STANDARDS

Every empirical paper submitted to AEA journals (and increasingly Econometrica, EJ, field journals) must include a replication package meeting the Data Editor standards.

**README structure (Social Science Data Editors template):**
1. Data Availability & Provenance — who owns the data, how to access
2. Dataset List — every file, source, description
3. Computational Requirements — software, packages, runtime, hardware
4. Programs Description — what each script does, execution order
5. Replicator Instructions — step-by-step, reproducible without manual intervention

**Directory structure:**
```
data/raw/        <- original downloaded data, never modified
data/analysis/   <- cleaned analysis-ready datasets
code/            <- all scripts, numbered in execution order
results/         <- generated tables and figures
```

**Rules:**
- Cite every dataset in the References section with standard in-text citations
- Code must reproduce all results without manual intervention (one config file for paths is the only exception)
- Map every table and figure to a specific program file
- For restricted-access data: include a Data Availability Statement explaining the application procedure, wait times, and monetary costs
- Include `LICENSE.txt` (default: CC-BY 4.0)

---

### 3. AI-USE DISCLOSURE

**AEA policy:** AI cannot be listed as an author. Disclose AI use during submission.
**Econometric Society:** Co-authors must sign a responsibility statement accepting responsibility for all content.

**What to disclose:** drafting assistance, code generation, literature search, data analysis suggestions.
**Typically no disclosure needed:** spell-check, grammar tools, LaTeX formatting.

**Core rule:** If AI drafted a paragraph, read it as if a careless RA wrote it — verify every fact, citation, and number. You are responsible for all AI-generated content.

---

### 4. ERC GRANT STRUCTURE

(Complements `research-grants`, which covers NSF/NIH/DOE/DARPA.)

**ERC reviewer priorities differ from NSF:**
- **PI track record** is weighted heavily — foreground publication record, citation impact, career trajectory
- **"High-risk, high-gain"** framing is mandatory — ERC explicitly funds frontier risk-taking, not incremental extensions
- **Societal relevance** section should connect to real policy questions, not abstract "advancing knowledge"

**Proposal structure:**
1. Extended synopsis (5 pages): question, approach, expected impact — written for a smart non-specialist
2. Scientific proposal (14 pages for StG/CoG, 15 for AdG): detailed research plan, methodology, feasibility
3. CV + track record (2 + 2 pages): highlight *your* contributions, not co-authors'
4. Budget justification: link every cost to a specific research activity

**Common mistake:** writing like a finished paper. A proposal sells the *plan*, not findings. Emphasize what you WILL learn.

---

### 5. FIELD-SPECIFIC CONVENTIONS

#### Macroeconomics
- Papers are longer (40–60 pages normal); the "under 40 pages" rule does not apply
- Calibration tables are standard: parameter | value | source/target moment
- Impulse response functions (IRFs) are the primary visualization, not regression tables
- "Model Fit" section comparing model moments to data moments is expected
- DSGE papers: describe steady state, log-linearization or solution method, shock specification
- Phrase results as "the model generates X" rather than "I find X"

#### Trade
- Gravity estimation: use PPML, multilateral resistance controls, explicit fixed-effects structure
- General equilibrium counterfactuals are expected in structural trade papers
- Use 3-year or 5-year panel intervals (not annual) with specific justification

#### Finance
- Abstract limit is often **100 words** (not 150) — check target journal
- Fama-MacBeth regressions and portfolio-sort presentation are standard
- Variable winsorization at 1%/99% is expected and must be reported
- Chicago Manual of Style citation at some journals (differs from AEA)

#### Development / Applied Micro with RCTs
- Pre-registration is nearly mandatory
- Include a CONSORT-style flow diagram (enrollment → randomization → attrition → analysis)
- Report cost-effectiveness alongside treatment effects
- Balance tables belong prominently in the paper, not the appendix

---

### 6. TITLE EVALUATION FRAMEWORK

Score any candidate title 1–10 on each dimension:

1. **Clarity** — Can a non-specialist understand the topic in one reading?
2. **Specificity** — Are treatment/cause and outcome/effect both named?
3. **Length** — Under 12 words is ideal; under 15 is acceptable
4. **Memorability** — Would someone remember it at a conference?
5. **No methodology** — Does it emphasize the finding, not the method? (Exception: you invented the method.)

**Good:**
- "The Oregon Health Insurance Experiment: Evidence from the First Year"
- "The China Syndrome: Local Labor Market Effects of Import Competition"
- "Pollution and Mortality: Evidence from the 1952 London Fog"

**Bad:**
- "A Difference-in-Differences Analysis of Education Policy" (methodology, not finding)
- "On the Relationship Between Various Factors and Economic Outcomes" (says nothing)
- "Essays on Labor Economics" (acceptable for dissertation, never for a paper)

**Formulas that work:**
- "The Impact of [D] on [Y]: Evidence from [Context]"
- "[D] and [Y]" (shorter, acceptable)
- Theory: name the key mechanism, not the technique
- Structural: "[Counterfactual Question]: Evidence from [Context]"

---

### 7. ECONOMIC SIGNIFICANCE (Not Just Statistical)

Never report a coefficient without translating it. Rules:

- **Translate to meaningful units:** dollars, percentage points, standard deviations, policy benchmarks
- **Compare effect size** to at least one of:
  - Mean of the dependent variable
  - A well-known intervention (e.g., "equivalent to 60% of the Moving to Opportunity effect")
  - A policy-relevant threshold (e.g., the poverty line)
- **For elasticities**, state whether computed at the mean, median, or arc
- **Back-of-envelope calculations are encouraged** — show the reader what the number means in aggregate
- **Null results:** distinguish "precisely estimated zero" (report CI and rule out effects above X) from "imprecisely estimated" (wide CI). Discuss statistical power. If pre-registered, emphasize that.

---

### 8. MULTIPLE TESTING

When testing multiple outcomes or subgroups:
- Acknowledge the problem explicitly
- Report family-wise error rate (Bonferroni, Holm) **or** false discovery rate (Benjamini-Hochberg) corrections
- At minimum, flag results surviving the correction
- For heterogeneity: pre-specify subgroups based on theory, not data mining; report the number of subgroups tested

---

### 9. HOW TO USE THIS SKILL ALONGSIDE OTHERS

| Task | Primary skill | Add from this skill |
|------|---------------|---------------------|
| Draft an intro | `economic-writing` | Paper-type hook table (§1), title eval (§6) |
| Write identification section | `economic-writing` | Full identification-strategies.md |
| Rewrite for voice | `econ-humanizer` | — (no overlap) |
| Pre-submission audit | `pre-submission-review` | AEA replication check (§2), AI disclosure (§3) |
| Referee response | `referee-report` | — (no overlap) |
| NSF/NIH grant | `research-grants` | — |
| **ERC grant** | `research-grants` + **this skill** (§4) | §4 is the delta |
| Finance paper | `economic-writing` | §5 (100-word abstract, FM regressions) |
| Macro paper | `economic-writing` | §5 (IRFs, calibration tables) |
| Staggered DiD | `economic-writing` | §1 modern-estimator guidance |

---

*Synthesized from the hanlulong/econ-writing-skill corpus (50+ sources: Cochrane, McCloskey, Head, Bellemare, Shapiro, Goldin & Katz, Glaeser, Kremer, Nikolov, Schwabish, Evans, Dudenhefer) plus the modern DiD and shift-share literatures.*
