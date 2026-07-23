<!-- DO NOT EDIT — auto-generated from projects/landscape/airs-bench.yml by scripts/build_indexes.py -->

# AIRS-Bench (Meta FAIR)

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/facebookresearch/airs-bench>

**Source:** [`projects/landscape/airs-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/airs-bench.yml)

## Positioning

A benchmark (arXiv:2602.06855) quantifying the end-to-end AI research abilities of LLM agents: 20 tasks sourced from 17 state-of-the-art ML papers across language modeling, code generation, mathematics, biochemical modeling, and time-series forecasting. Each task is a <problem, dataset, metric> triplet with a published SOTA anchor that agents must match or exceed — spanning idea, experiment, and refinement work — with no baseline code provided. Sits in the RISE evaluation-infrastructure layer alongside AstaBench, MLGym, and Aviary.

## Distinctive contribution

Anchors agent performance to *published human SOTA* rather than synthetic targets: a normalized score (0 = worst observed, 1 = SOTA) plus Elo ratings and valid-submission rates, computed over 14 agent configurations at 10-20 seeds each. The companion paper reports agents exceeding human SOTA on four tasks while failing to match it on sixteen — an explicitly unsaturated target set for end-to-end ML research agents.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure; quantifies the research ability of other systems, does not produce scholarship itself. |
| Autonomy level | 0 | Static task specs plus a scoring harness; all agency lives in the LLM agents being evaluated. |
| Architectural transparency | 3 | Public code, YAML task definitions, HuggingFace-hosted datasets, scoring notebooks, and a 36-author arXiv paper documenting the full evaluation setup. |
| Inputs supported | 2 | 20 standardized task specs across five ML domains, runnable under two documented scaffolding frameworks (aira-dojo and MLGym). |
| Outputs / reproducibility | 2 | Fixed <problem, dataset, metric> triplets with SOTA anchors and seeded multi-run reporting; agent-run stochasticity limits exact reruns. |
| Internal evaluation | 2 | Systematic evaluation of 14 agent configurations at 10-20 seeds in the companion arXiv paper; not yet peer-reviewed or third-party replicated. |
| Openness | 1 | Fully public but CC BY-NC 4.0 — non-permissive, research-only reuse (stricter reading of the rubric than mlgym's earlier score). |
| Maturity / traction | 2 | 104 stars, Meta institutional backing, active development Jan-May 2026, companion paper with headline cross-model results. |
| Cross-family policy | 0 | Not applicable — model-agnostic evaluation target; baselines span families (GPT-4o, o3-mini, gpt-oss, Devstral, CWM) but there is no executor/reviewer pairing of its own. |
| Runtime assurance | 1 | Automated metric scoring plus valid-submission checks; no in-flight integrity gating during agent runs. |
| Cross-platform portability | 2 | YAML task specs consumable by two agent runtimes (aira-dojo, MLGym) and any model provider; Python 3.12 + conda required. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation`



**Inputs:** `task-specification` `agent-implementation`


**Outputs:** `evaluation-metrics` `agent-trajectories`


**Data sources:** `benchmark-datasets`


**Knowledge sources:** `source-papers`


## Limitations

- CC BY-NC 4.0 license restricts commercial reuse of tasks and code.
- Evaluation infrastructure — value depends on downstream agent systems being benchmarked.
- SOTA anchors are snapshots: normalized scores will drift in meaning as human state of the art advances; matching them requires substantial GPU budgets.

## Related projects in this catalog

- [`mlgym`](mlgym.md)
- [`asta-bench`](asta-bench.md)
- [`aviary`](aviary.md)
- [`econcs-bench`](econcs-bench.md)

## Papers describing this project

- **AIRS-Bench: a Suite of Tasks for Frontier AI Research Science Agents** — Lupidi, A., Gauri, B., Foster, T. S., Al Omari, B., Magka, D., Pepe, A., et al. (2026). *arXiv*. [arXiv:2602.06855](https://arxiv.org/abs/2602.06855)
