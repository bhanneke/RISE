<!-- DO NOT EDIT — auto-generated from projects/landscape/aarri-bench.yml by scripts/build_indexes.py -->

# AARRI-Bench

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/AARR-bench/AARRI-bench>

**Source:** [`projects/landscape/aarri-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/aarri-bench.yml)

## Positioning

"Act As a Real Research Intern" (arXiv:2606.07462) — 82 containerized scenarios in standardized Harbor task format, each with an assertion-based verifier, probing whether LLM agents show the professionalism of human researchers in *granular* research situations (citation integrity, ablation-completeness audits, dead-end recognition, contradictory-advisor merging) rather than end-to-end execution. Inaugural stage of a planned three-stage AARR series (AARRI intern -> AARRA agent -> AARRS scientist); sits in the RISE evaluation-infrastructure layer alongside AstaBench, MLGym, and AIRS-Bench.

## Distinctive contribution

Isolates the micro-level judgment failures that end-to-end benchmarks average away — context sensitivity, independent judgment, knowing when to quit, collaboration under conflicting guidance — as individually verifiable scenarios. The 11-author paper reports the best configuration (Mini-SWE-Agent with Claude Opus 4.7) at a 68.3% success rate, quantifying a specific gap between frontier agent harnesses and human research interns.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Scenario catalog / evaluation target; does not produce scholarship itself. |
| Autonomy level | 0 | Static containerized scenarios with verifiers; all agency lives in the agents being evaluated. |
| Architectural transparency | 3 | All 82 task definitions with per-task test_outputs.py verifiers public in standardized Harbor format; arXiv paper documents the evaluation setup. |
| Inputs supported | 1 | Single standardized input form (Harbor containerized task); runnable via Harbor Hub registry or local installation. |
| Outputs / reproducibility | 2 | Containerized environments plus deterministic assertion-based verification make scoring rerunnable; agent stochasticity limits exact trajectory reruns. |
| Internal evaluation | 2 | Systematic evaluation of frontier LLMs and agent harnesses in the companion paper (best 68.3%); arXiv-only, no third-party replication yet. |
| Openness | 1 | Public repo, free to run, but no license file at scoring date — reuse terms unclear. |
| Maturity / traction | 1 | Very young (Apr-Jun 2026) and small (8 stars); active single-team development anchored to an 11-author academic paper. |
| Cross-family policy | 0 | Not applicable — model-agnostic evaluation target; paper evaluates multiple families as subjects but the benchmark has no cross-family mechanism of its own. |
| Runtime assurance | 1 | Deterministic per-task pass/fail verification scripts; no in-flight integrity gating beyond final assertions. |
| Cross-platform portability | 2 | Harbor-format tasks run under multiple agent harnesses and any model provider; containerized execution required. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `literature-synthesis` `research-design` `data-analysis` `code-generation` `revision-editing`



**Inputs:** `task-specification` `agent-implementation`


**Outputs:** `pass-fail-verdicts` `evaluation-metrics`


**Data sources:** `benchmark-tasks`


**Knowledge sources:** `task-descriptions`


## Limitations

- No license file at scoring date — reuse terms are unclear.
- Very early traction (8 stars, launched April 2026); single-team maintenance.
- Granular scenarios test judgment in isolation — deliberately does not measure end-to-end research execution, so it complements rather than replaces benchmarks like AIRS-Bench or MLGym.

## Related projects in this catalog

- [`asta-bench`](asta-bench.md)
- [`mlgym`](mlgym.md)
- [`econcs-bench`](econcs-bench.md)

## Papers describing this project

- **Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle** — Wang, J., Lv, W., Fu, B., Fu, J., Song, J., Zhang, L., et al. (2026). *arXiv*. [arXiv:2606.07462](https://arxiv.org/abs/2606.07462)

## Related references (literature catalog)

- Wang, J. et al. (2026). [*Act As a Real Researcher: A Suite of Benchmarks Evaluating Frontier LLMs and Agentic Harnesses in Research Lifecycle*](../papers/notes/wang2026aarribench.md) `wang2026aarribench`
