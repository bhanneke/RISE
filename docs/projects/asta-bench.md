<!-- DO NOT EDIT — auto-generated from projects/landscape/asta-bench.yml by scripts/build_indexes.py -->

# AstaBench (AI2)

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2025

**Project page:** <https://github.com/allenai/asta-bench>

**Source:** [`projects/landscape/asta-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/asta-bench.yml)

## Positioning

An evaluation framework from AI2 for measuring scientific-research abilities of AI agents. 2,400+ examples across 11 benchmarks covering literature search, code execution, data analysis, and end-to-end discovery. Built on the InspectAI framework. Sits in the *RISE evaluation infrastructure* layer alongside Aviary and MLGym.

## Distinctive contribution

The most-scoped benchmark suite for scholarly-research agent abilities specifically — not generic agent benchmarks, not domain-specific science tasks (cf. BixBench), but a curated spectrum of *research skills* with standardized tools and execution environments for fair efficiency-comparable runs.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure; does not produce scholarship itself. |
| Autonomy level | 2 | Supervised: user submits an agent; AstaBench scores it across 11 tasks. |
| Architectural transparency | 3 | Open under Apache-2.0; AstaBench paper at allenai.org; built on documented InspectAI framework. |
| Inputs supported | 3 | 11 benchmarks spanning research skills; standardized agent interface; leaderboard submission supported. |
| Outputs / reproducibility | 3 | Docker-based execution; standardized scoring; decoupled solve/score for cross-version comparison. |
| Internal evaluation | 2 | Self-application: AI2 uses AstaBench to evaluate its own agents; broader cross-system results on leaderboard. |
| Openness | 3 | Apache-2.0; AI2 institutional backing; public leaderboard. |
| Maturity / traction | 2 | 104 stars; active development; AI2 institutional backing; recent (2025–2026). |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `data-analysis` `code-generation`


**Architectural features:** `tool-use` `artifact-versioning`


**Inputs:** `task-specification` `agent-implementation`


**Outputs:** `agent-trajectories` `leaderboard-submissions` `efficiency-metrics`


**Data sources:** `benchmark-tasks`


**Knowledge sources:** `paper-corpus`


## Limitations

- Evaluation infrastructure — value depends on downstream agent systems being benchmarked.
- Requires Docker for the recommended path.
- Sub-tasks vary in maturity; the 11-benchmark scope is broad but not exhaustive.

## Related projects in this catalog

- [`aviary`](aviary.md)
- [`mlgym`](mlgym.md)
- [`paper-qa`](paper-qa.md)

## Papers describing this project

- **AstaBench: Rigorous Benchmarking of AI Agents with a Scientific Research Suite** — Bragg, J., D'Arcy, M., Balepur, N., Bareket, D., Dalvi, B., Feldman, S., et al. (2025). *arXiv*. [arXiv:2510.21652](https://arxiv.org/abs/2510.21652)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
