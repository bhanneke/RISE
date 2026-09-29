<!-- DO NOT EDIT — auto-copied from skills/daaf/details/creative-verification.md -->

# `/creative-verification`

Turns a researcher's doubt about a finding into competing explanations and pre-specified discriminating tests, drawn from 12 challenge families organised by validity type, with sensitivity statistics, pre-committed interpretation rules and anti-fishing guardrails. The results go into a hypothesis and evidence ledger in place of line-by-line code review.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../daaf/">DAAF — Data Analyst Augmentation Framework (Brian Heseung Kim)</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>LGPL-3.0-or-later (as declared in the README, badge and CITATION.cff; the repo ships the GPL-3.0 text as LICENSE plus COPYING.LESSER)</code></div><div><b>Updated:</b> 2026-08-08</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code> · <code>research-design</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/DAAF-Contribution-Community/daaf/contents/.claude/skills/creative-verification/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/daaf/creative-verification/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/DAAF-Contribution-Community/daaf/blob/main/.claude/skills/creative-verification/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/DAAF-Contribution-Community/daaf?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Creative Verification

Collaborative analytic-triangulation methodology for stress-testing research claims and designing pre-specified challenges. The distinctive loop: elicit the researcher's concern, state the focal claim precisely, generate a bounded set of competing explanations (including data/process explanations), identify what observable result would discriminate among them, prioritize, execute through DAAF's existing file-first/validation/QA machinery, interpret against pre-committed rules, and update a hypothesis/evidence ledger — then stop, iterate, or promote a confirmed change into Revision and Extension. Piloted in **Ad Hoc Collaboration mode only**: the orchestrator loads this skill, runs the loop conversationally, and maintains the ledger per `agent_reference/TRIANGULATION_PROTOCOL.md` in the session workspace. Existing agents (research-executor, code-reviewer, debugger, data-verifier) execute the tests; this skill supplies the challenge taxonomy, the sensitivity-statistic catalog, the interpretation rules, and the interactive-artifact QA contract. It covers both **completed/provisional-results verification** and **pre-analysis challenge design**. It is emphatically not code-change verification (the bundled `verify` skill, `/code-review`), not final delivery adjudication (data-verifier's QA4 verdict), and not re-execution reproducibility checking (Reproducibility Verification mode) — this is prospective, hypothesis-driven challenge design of the *analytic claims themselves*.

### Mission: Calibrated Confidence per Unit of Researcher Attention

The purpose of creative verification is to **reduce the researcher's line-by-line code-review burden by substituting behavioral, output-level verification for granular code spelunking.** Reading every line of a pipeline is expensive and scales poorly; independent re-derivation, reconciliation checks, and discriminating tests on chunks and outputs let a researcher spend attention where it changes their confidence the most.

Three consequences shape everything below:

- **Behavioral verification first.** Prefer tests that check what the code *produced* (does an independent re-derivation of the headline number match? does the total reconcile against the source? does a placebo outcome stay null?) over tests that inspect how it was written. A chunk that passes its behavioral checks does not need line-level review; a chunk that *fails* one does — line-level review is the escalation, not the default.
- **The ledger is a coverage map.** The hypothesis/evidence ledger (schema in `TRIANGULATION_PROTOCOL.md`) is not just a record — it is a map of which facets of the data, process, and results have been triangulated, by what test, with what result. Gaps in the map are the honest statement of what remains unverified. Present it that way to the researcher.
- **Attention is the scarce resource.** When prioritizing tests (rubric below), the implicit denominator is always researcher attention. A cheap test that resolves a high-stakes doubt beats an elegant test that resolves a doubt nobody holds.

This reframing is the skill's reason to exist. If a session drifts into performative skepticism (challenging things nobody doubts) or into exhaustive code review (the thing this skill exists to reduce), stop and re-anchor to the mission.

### The Challenge Loop

```
1. ELICIT      Draw out the researcher's own concern, surprise, or skeptical-
               reviewer question FIRST — before seeding any suggestions.
2. STATE       Write the focal claim precisely (magnitude, population, period,
               conditioning, the decision it informs).
3. GENERATE    Produce a bounded set of competing explanations that could also
               produce the observed result — including data/process explanations
               (missingness, joins, suppression, coding), not only substantive ones.
4. DISCRIMINATE Identify, for each explanation, what OBSERVABLE result would tell
               it apart from the focal claim. No discriminating observable → not
               yet a test, just a worry.
5. PRIORITIZE  Rank candidate tests by the rubric below. Default to a small first
               bundle (~3 complementary tests), then pause.
6. PRE-COMMIT  For each chosen test, record in the ledger what result would SUPPORT
               vs. WEAKEN the focal claim BEFORE running it. The ledger is the arbiter.
7. EXECUTE     Run approved tests through the normal DAAF machinery (file-first
               scripts, inline validation, QA review). Diagnostic artifacts are
               separately planned — never Stage 9 notebooks.
8. INTERPRET   Assign one of six interpretation statuses, update the ledger/coverage
               map, then STOP, ITERATE (new bundle), or PROMOTE a confirmed change
               into Revision and Extension.
```

The loop is collaborative, not adversarial. The aim is **discrimination among explanations**, not treating every difference as a flaw. Researcher and domain knowledge are a source of *hypotheses*, never automatic empirical evidence; DAAF-generated hypotheses are *suggestions* requiring the researcher's judgment and an empirical test.

### Intake Interview

Elicit the researcher's own concerns **before** seeding DAAF suggestions — seeding first anchors them to your framing and suppresses the doubt they actually hold. Open questions:

- What result or decision here feels most consequential?
- What surprised you, or what would a skeptical reviewer say is driving this?
- Which single assumption, if it failed, would most change your confidence?
- **What would you otherwise feel obligated to inspect by hand, line by line?** (Route each such concern to an output-level challenge — this is the mission in action.)
- Which populations, periods, geographies, or definitions might aggregation be hiding?
- What evidence would genuinely change your mind?
- Is the goal exploration, a formal robustness claim, or a decision-support artifact?

Only after these are on the table does DAAF propose challenge families (below). Capture the "inspect by hand" answers explicitly — they are the highest-value targets, because each one is researcher attention the skill can buy back with a behavioral test.

### The 12 Challenge Families

Organized over the four **Shadish-Cook-Campbell validity types** (internal, statistical-conclusion, construct, external). Each family stresses one or more types. Full definitions, when-to-use, concrete Python-first test recipes, and family-specific pitfalls: `references/challenge-families.md`.

| # | Family | Primary validity type(s) |
|---|--------|--------------------------|
| 1 | Population & denominator | statistical-conclusion, construct |
| 2 | Composition & aggregation (Simpson's, weighting) | statistical-conclusion, internal |
| 3 | Missingness & observability (suppression, selective availability) | internal, construct |
| 4 | Measurement & coding (operationalization, proxy validity) | construct |
| 5 | Temporal (windows, cohort vs. period, lag, event alignment) | internal |
| 6 | Model / specification (spec grids, influence, FE/SE choices) | statistical-conclusion, internal |
| 7 | Placebo & falsification (negative outcomes/exposures, timing) | internal |
| 8 | Visual-framing (counts vs. rates, scales, uncertainty shown/hidden) | statistical-conclusion, construct |
| 9 | Data-lineage & implementation (reconciliation, join-loss, duplicate keys) | internal (data-process) |
| 10 | Stakeholder-perspective (skeptical reviewer, domain expert, decision-maker) | external (hypothesis-generating) |
| 11 | Identification-assumption (sensitivity analysis for untestable premises) | internal |
| 12 | Generalizability / transportability | external |

Families 11 and 12 are promoted to first-class because identification assumptions and external validity are challengeable with **named computable statistics**, not just prose — turning "challenge the assumption" into an auditable number. See `references/sensitivity-statistics.md`.

### Prioritization Rubric

Rank each candidate test on these axes; favor tests that are high on the first two and acceptable on the rest. The denominator is always researcher attention.

| Axis | Question |
|------|----------|
| Decision relevance | Does the answer change a decision the researcher actually faces? |
| Discriminatory power | Would the result genuinely separate the focal claim from an alternative? |
| Feasibility | Can current data and the container's tooling answer it? |
| Analytic cost | How much execution and interpretation effort does it demand? |
| Disclosure risk | Does it expose suppressed cells, small counts, or PII? |
| Multiplicity / fishing risk | Does adding it inflate the garden-of-forking-paths problem? Is it pre-specified? |
| Scope impact | Does it change official scope, population, or methodology (which needs approval)? |

Default to a **small first bundle of ~3 complementary tests**, then pause for interpretation before proposing more. Bounded budgets with explicit stopping rules are how the loop resists fishing — see `references/interpretation-and-evidence.md`.

### Routing Concerns to Challenge Families

```
What is the researcher worried about?
├─ "The number itself might be wrong / built wrong"
│   └─ Family 9 (data-lineage): reconcile totals, independent re-derivation,
│      join-loss and duplicate-key checks → references/challenge-families.md
├─ "It might be an artifact of who's in / out of the denominator"
│   └─ Family 1 (population) + Family 2 (composition, Simpson's, weighting)
├─ "Missing or suppressed data might be driving it"
│   └─ Family 3 (missingness & observability)
├─ "The variable might not measure what we think"
│   └─ Family 4 (measurement & coding)
├─ "It might be a fluke of the time window / period"
│   └─ Family 5 (temporal)
├─ "The result might not survive different modeling choices"
│   └─ Family 6 (model/specification) → spec-curve; references/interpretation-and-evidence.md
│      for the summary contract
├─ "It might be spurious / not causal"
│   ├─ Falsification available → Family 7 (placebo & falsification)
│   └─ Rests on an untestable identification assumption
│       └─ Family 11 → named sensitivity statistic (references/sensitivity-statistics.md):
│          unobserved confounding → E-value / Cinelli-Hazlett RV;
│          matched design → Rosenbaum Gamma; proportional selection → Oster delta;
│          DiD pre-trends → event-study + honest-DiD discussion (flag, not naive pre-test);
│          RD → McCrary density (flag) + covariate placebo; IV → overID/placebo, never "test" exclusion
├─ "The chart might be creating the impression"
│   └─ Family 8 (visual-framing) → optional lineup protocol; references/interactive-artifact-qa.md
├─ "It might not generalize beyond this sample/setting"
│   └─ Family 12 (generalizability/transportability)
└─ "A skeptical reviewer / domain expert would ask..."
    └─ Family 10 (stakeholder) — generates hypotheses to route into families 1-12;
       stakeholder questions are not themselves evidence
```

### Guardrails (Anti-Fishing)

Encoded in full in `references/interpretation-and-evidence.md`; the load-bearing set:

- **Label every test** exploratory / pre-specified / confirmatory / post-hoc. Pre-analysis challenge design produces pre-specified tests; interpret post-hoc tests with according caution.
- **Record ALL attempted tests**, including nulls, failures, and results that contradict the researcher's hope. A ledger that only shows supporting tests is a fishing expedition with good PR.
- **Bounded budgets and explicit stopping rules.** Never iterate until a desired finding appears. Default small first bundle, then pause.
- **Pre-commit interpretation before execution** (loop step 6) — the ledger is the arbiter, closing the garden-of-forking-paths gap that hypothesis-only preregistration leaves open.
- **Separate the layers:** researcher concerns vs. DAAF-generated hypotheses vs. test designs vs. executed observations vs. interpretations. `TRIANGULATION_PROTOCOL.md` defines the separation.
- **Preserve the official analysis.** Creative verification runs alongside it and never silently changes it. New data sources, population changes, or methodology changes require explicit user approval; a confirmed change is promoted into Revision and Extension, not slipped in.
- **Diagnostic artifacts are not self-validating evidence.** Plotly HTML / standalone Marimo apps are exploratory interfaces whose every state must trace to audited data — never Stage 9 notebooks. QA contract: `references/interactive-artifact-qa.md`.

### Container Tooling Reality

DAAF prohibits runtime package installs, so the sensitivity-statistic catalog is split into **executable** recipes (dependencies confirmed installed) and **flag-and-describe** methods (no installed package — describe, cite, recommend a Dockerfile addition for the maintainer). Executable: specification-curve (custom statsmodels/pyfixest + Polars + plotnine loop), Cinelli-Hazlett robustness value (closed-form from a t-value and residual df), E-value for risk ratios (closed-form), Oster delta (closed-form benchmark comparison), RD point estimation (`rdrobust`), IV falsification (`linearmodels` overidentification + placebo outcomes), DiD event-study (`pyfixest`), and transportability reweighting (`statsmodels` + `polars`). Flag-and-describe: Rosenbaum bounds, honest DiD (Rambachan-Roth), McCrary/Cattaneo density (`rddensity`). Details, formulas, confidence labels, and citations: `references/sensitivity-statistics.md`.

### Reference Files

Load on demand — thorough by design (Level 3; token cost only when read).

| File | Read when |
|------|-----------|
| `references/challenge-families.md` | Designing a challenge; picking a family; needing a concrete test recipe for a specific concern |
| `references/sensitivity-statistics.md` | A challenge rests on an identification assumption or external validity and needs a named computable statistic (E-value, RV, Gamma, delta, McCrary, honest-DiD) |
| `references/interpretation-and-evidence.md` | Interpreting a completed test; assigning a status; labeling exploratory/confirmatory; setting budgets/stopping rules; summarizing a spec curve; grading evidence |
| `references/interactive-artifact-qa.md` | Planning or reviewing a diagnostic dashboard (Plotly HTML / standalone Marimo app) |

### Companion Protocol

The cross-cutting mechanics — hypothesis/evidence ledger schema, test lifecycle, provenance chain, pre-analysis variant, scope-change approval rules, stopping rules, and the separation of concerns/hypotheses/designs/observations/interpretations — live in `agent_reference/TRIANGULATION_PROTOCOL.md`. This skill is the methodology (what challenges to design and how to interpret them); the protocol is the bookkeeping and provenance substrate (how to record and audit them). Read the protocol when setting up or maintaining the ledger for a session.

### Topic Index

| Topic | Location |
|-------|----------|
| Mission / calibrated-confidence framing | This file, "Mission" |
| The challenge loop (8 steps) | This file, "The Challenge Loop" |
| Intake interview questions | This file, "Intake Interview" |
| 12 challenge families (overview) | This file, "The 12 Challenge Families" |
| Challenge family definitions + recipes | `references/challenge-families.md` |
| Named sensitivity statistics | `references/sensitivity-statistics.md` |
| Six interpretation statuses | `references/interpretation-and-evidence.md` |
| Exploratory/confirmatory labeling, budgets, stopping rules | `references/interpretation-and-evidence.md` |
| Specification-curve summary contract | `references/interpretation-and-evidence.md` |
| Interactive-artifact QA contract | `references/interactive-artifact-qa.md` |
| Ledger schema, lifecycle, provenance | `agent_reference/TRIANGULATION_PROTOCOL.md` |
| Prioritization rubric | This file, "Prioritization Rubric" |
| Anti-fishing guardrails | This file, "Guardrails" |
