<!-- DO NOT EDIT — auto-generated from skills/auto-empirical-research-skills.yml by scripts/build_skills_index.py -->

# Auto-Empirical Research Skills (AERS) — first-party skills

license: `CC BY-SA 4.0 (repo default); MIT for the mirrored first-party collections (StatsPAI, AER-skills, Paper-WorkFlow)` · 22 skills · last update: 2026-07-22

**Source:** <https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills>

**Maintainers:** Bryce Wang (Stanford REAP / CoPaper.AI)

**Related project entry:** [`auto-empirical-research-skills`](../projects/auto-empirical-research-skills.md)

**Compatibility:** `claude-code` `codex` `cursor`

> Repo bundles 1,094 skills across 74 collections, ~90% vendored third-party (clo-author, academic-research-skills, ARIS, awesome-econ-ai-stuff, etc. — cataloged separately in RISE); this manifest catalogs the 22 first-party skills: the root router, the four flagship full-pipeline analysis skills (StatsPAI / Python / Stata / R backends), the chinese-de-aigc editing skill, the 15-skill AER-skills collection (mirror of brycewang-stanford/AER-skills), and the Paper-WorkFlow meta-orchestrator (git submodule of brycewang-stanford/Paper-WorkFlow). First-party status taken from the repo's own catalog/provenance.json origin labels.


**Source YAML:** [`skills/auto-empirical-research-skills.yml`](https://github.com/bhanneke/RISE/blob/main/skills/auto-empirical-research-skills.yml)

## Skills

### `analysis` (6)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-robustness`](auto-empirical-research-skills/aer-robustness.md) | economics | `data-analysis` | Builds the robustness, heterogeneity, mechanism, and placebo battery AER referees demand, once main results exist and before the introduction's value-added paragraph is written. | [view](auto-empirical-research-skills/aer-robustness.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-robustness/SKILL.md) | 2026-07-22 |
| [`aer-statspai`](auto-empirical-research-skills/aer-statspai.md) | economics | `data-analysis` `code-generation` | Runs the AER-track analysis with StatsPAI — the agent-native Python engine and MCP server for causal inference, robustness, sensitivity, and publication-ready table export — after aer-identification fixes the design. | [view](auto-empirical-research-skills/aer-statspai.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-statspai/SKILL.md) | 2026-07-22 |
| [`Full-empirical-analysis-skill`](auto-empirical-research-skills/full-empirical-analysis-python.md) | economics | `data-analysis` `code-generation` | Classical 8-step end-to-end empirical workflow in the traditional Python stack (pandas/statsmodels/linearmodels/pyfixest/econml) — cleaning through publication tables/figures in AER house style, with epidemiology and ML-causal parallel modes; the non-StatsPAI, estimator-explicit counterpart. | [view](auto-empirical-research-skills/full-empirical-analysis-python.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/00.1-Full-empirical-analysis-skill_Python/SKILL.md) | 2026-07-22 |
| [`Full-empirical-analysis-skill-R`](auto-empirical-research-skills/full-empirical-analysis-r.md) | economics | `data-analysis` `code-generation` | Same 8-step empirical pipeline in the tidyverse + fixest R ecosystem — did/HonestDiD/rdrobust/gsynth/MatchIt/grf/DoubleML estimation with modelsummary/gt/ggplot2 publication outputs and Quarto reproducibility; epidemiology and ML-causal modes included. | [view](auto-empirical-research-skills/full-empirical-analysis-r.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/00.3-Full-empirical-analysis-skill_R/SKILL.md) | 2026-07-22 |
| [`Full-empirical-analysis-skill-Stata`](auto-empirical-research-skills/full-empirical-analysis-stata.md) | economics | `data-analysis` `code-generation` | Same 8-step empirical pipeline as a reproducible Stata .do workflow — reghdfe/ivreg2/csdid/did_imputation/sdid/rdrobust/synth/psmatch2 estimation, bacondecomp/honestdid/rwolf/oster robustness, esttab/coefplot outputs; epidemiology and ML-causal modes included. | [view](auto-empirical-research-skills/full-empirical-analysis-stata.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/00.2-Full-empirical-analysis-skill_Stata/SKILL.md) | 2026-07-22 |
| [`StatsPAI_skill`](auto-empirical-research-skills/statspai-skill.md) | economics | `data-analysis` `code-generation` | Full empirical/causal analysis in Python via the StatsPAI vertical engine — AER/QJE-style DID/RD/IV/SCM/DML pipeline with estimating equation + identifying assumption, Table 1/2, event-study figure, robustness gauntlet; plus epidemiology, ML-causal, and Oaxaca-style decomposition modes and Word/Excel/LaTeX table export. | [view](auto-empirical-research-skills/statspai-skill.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/00-Full-empirical-analysis-skill_StatsPAI/SKILL.md) | 2026-07-22 |

### `audit` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-consistency`](auto-empirical-research-skills/aer-consistency.md) | economics | `revision-editing` | Internal-consistency audit of a near-final manuscript: headline numbers across abstract/introduction/results/tables, sample sizes, log-point vs percentage-point conversions, cross-references, and citation-bibliography matching. | [view](auto-empirical-research-skills/aer-consistency.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-consistency/SKILL.md) | 2026-07-22 |

### `design` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-identification`](auto-empirical-research-skills/aer-identification.md) | economics | `research-design` | Selects, implements, or stress-tests the causal identification strategy — DID (incl. staggered), IV (incl. weak-IV-robust inference), RDD, synthetic control, shift-share/Bartik — before introduction or results are written. | [view](auto-empirical-research-skills/aer-identification.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-identification/SKILL.md) | 2026-07-22 |
| [`aer-preregistration`](auto-empirical-research-skills/aer-preregistration.md) | economics | `research-design` | For primary-data and experimental projects, before the intervention: writes the pre-analysis plan, sizes the sample from a power calculation, and registers with the AEA RCT Registry. | [view](auto-empirical-research-skills/aer-preregistration.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-preregistration/SKILL.md) | 2026-07-22 |

### `drafting` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-introduction`](auto-empirical-research-skills/aer-introduction.md) | economics | `paper-drafting` | Drafts or rewrites the introduction to the Keith Head / Bellemare five-paragraph formula with AER-specific conventions, and compresses abstracts to the mandatory 100-word limit. | [view](auto-empirical-research-skills/aer-introduction.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-introduction/SKILL.md) | 2026-07-22 |
| [`aer-paper-body`](auto-empirical-research-skills/aer-paper-body.md) | economics | `paper-drafting` | Drafts and revises the body sections of an AER/AEJ manuscript — background, data, empirical strategy, results, mechanisms, conclusion — including equation conventions, results-paragraph narration, magnitude interpretation, and back-of-envelope policy calculations. | [view](auto-empirical-research-skills/aer-paper-body.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-paper-body/SKILL.md) | 2026-07-22 |

### `editing` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`chinese-de-aigc`](auto-empirical-research-skills/chinese-de-aigc.md) | general | `revision-editing` | Chinese academic de-AIGC rewriting targeting CNKI/Wanfang/VIP/Turnitin-zh detectors — a five-step locate/diagnose/rewrite/self-score/recheck loop over 17 diagnostic rules for the five structural signatures of Chinese LLM prose, with per-section strategies. | [view](auto-empirical-research-skills/chinese-de-aigc.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/48-copaper-ai-chinese-de-aigc/SKILL.md) | 2026-07-22 |

### `figures` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-tables-figures`](auto-empirical-research-skills/aer-tables-figures.md) | economics | `paper-drafting` | Constructs and revises regression tables, descriptive-statistics tables, and figures in AER booktabs house style, with regression-table layout and figure-note conventions. | [view](auto-empirical-research-skills/aer-tables-figures.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-tables-figures/SKILL.md) | 2026-07-22 |

### `ideation` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-topic-selection`](auto-empirical-research-skills/aer-topic-selection.md) | economics | `rq-formulation` | Evaluates whether a research idea clears the AER top-5 bar, routes between AER, AER:Insights, and the AEJ family, and sharpens a fuzzy contribution sentence into one publishable claim. | [view](auto-empirical-research-skills/aer-topic-selection.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-topic-selection/SKILL.md) | 2026-07-22 |

### `infra` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-workflow`](auto-empirical-research-skills/aer-workflow.md) | economics |  | Router for the 15-skill AER-skills collection — sequences manuscript work from topic selection through rebuttal for AER, AER:Insights, and AEJ journals; routes, does not replace, the specialized skills. | [view](auto-empirical-research-skills/aer-workflow.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-workflow/SKILL.md) | 2026-07-22 |
| [`auto-empirical-research-skills`](auto-empirical-research-skills/aers-router.md) | general |  | Root router for whole-repo installs — classifies an empirical-research request by stage/method and dispatches to one of the 1,094 vendored skills via catalog JSON lookups instead of reading the repo wholesale. | [view](auto-empirical-research-skills/aers-router.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/SKILL.md) | 2026-07-22 |
| [`paper-workflow`](auto-empirical-research-skills/paper-workflow.md) | economics | `rq-formulation` `research-design` `data-acquisition` `data-analysis` `paper-drafting` `revision-editing` `referee-simulation` `dissemination` | Meta-orchestrator for a complete empirical paper (econ/social science): Stage 0-9 resumable pipeline from topic selection to submission with two hard human gates (Method Gate after estimation, Draft Quality Gate after polish); routes Python/StatsPAI, Stata, or R analysis backends and invokes existing skills rather than reimplementing them. Git submodule mirroring brycewang-stanford/Paper-WorkFlow. | [view](auto-empirical-research-skills/paper-workflow.md) | [origin](https://github.com/brycewang-stanford/Paper-WorkFlow/blob/main/SKILL.md) | 2026-07-22 |

### `literature` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-literature`](auto-empirical-research-skills/aer-literature.md) | economics | `literature-discovery` `literature-synthesis` | Positions a manuscript against the economics literature — antecedents map for the introduction, cite/no-cite decisions, and verification that every bibliography entry is real, correctly attributed, and cited to the published version. | [view](auto-empirical-research-skills/aer-literature.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-literature/SKILL.md) | 2026-07-22 |

### `replication` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-replication`](auto-empirical-research-skills/aer-replication.md) | economics | `replication` `dissemination` | Assembles the AEA Data and Code Availability deposit — README writing and replication-package audit against the current AEA policy (including the February 2026 Data and Code Availability Policy) before the AEA Data Editor review. | [view](auto-empirical-research-skills/aer-replication.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-replication/SKILL.md) | 2026-07-22 |

### `review` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-referee-sim`](auto-empirical-research-skills/aer-referee-sim.md) | economics | `referee-simulation` | Adversarial internal review before submission — simulates the AER desk screen plus three referee reports with calibrated severity, scores against the editorial rubric, and produces a prioritized revise list; rerun until the simulated verdict is at least major R&R. | [view](auto-empirical-research-skills/aer-referee-sim.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-referee-sim/SKILL.md) | 2026-07-22 |

### `revision` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-rebuttal`](auto-empirical-research-skills/aer-rebuttal.md) | economics | `revision-editing` | Handles a Revise & Resubmit from AER/AEJ journals — triage, the concede/clarify/push-back decision per comment, and the point-by-point response-letter format editors actually read, aligned with manuscript revisions. | [view](auto-empirical-research-skills/aer-rebuttal.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-rebuttal/SKILL.md) | 2026-07-22 |

### `submission` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`aer-submission`](auto-empirical-research-skills/aer-submission.md) | economics | `dissemination` | Final pre-submission audit for AER/AEJ journals — length, format, cover letter, per-author disclosure statements, file packaging, and routing among the AEA journal family. | [view](auto-empirical-research-skills/aer-submission.md) | [origin](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-submission/SKILL.md) | 2026-07-22 |
