<!-- DO NOT EDIT — auto-generated from projects/landscape/aviary.yml by scripts/build_indexes.py -->

# Aviary (FutureHouse)

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2024

**Project page:** <https://github.com/Future-House/aviary>

**Source:** [`projects/landscape/aviary.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/aviary.yml)

## Positioning

A gymnasium for defining custom language-agent environments (arXiv:2412.21154), with pre-built environments for math, general knowledge, biological sequences, scientific literature search, and protein stability. Aviary is **evaluation infrastructure** for RISE systems, not a RISE pipeline itself — but it is directly relevant because it defines tasks against which RISE pipelines can be measured.

## Distinctive contribution

Provides a standardized environment-and-agent abstraction (paired with the LDP language-decision-process library) for benchmarking agentic systems on scientific tasks. Lowers the cost of producing comparable evaluations across pipelines.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Cross-cutting evaluation infrastructure; does not produce scholarly artifacts itself. |
| Autonomy level | 2 | Supervised: user defines environments; agents act within them. |
| Architectural transparency | 3 | Open under Apache-2.0; arXiv paper; tutorials; full documentation site. |
| Inputs supported | 2 | Multiple environment definitions ship with the library; user-defined environments supported. |
| Outputs / reproducibility | 3 | Pip-installable; deterministic given fixed model + environment; designed for benchmark reproducibility. |
| Internal evaluation | 2 | Used by FutureHouse to evaluate their own agents (Robin, PaperQA); benchmarks published in the arXiv paper. |
| Openness | 3 | Apache-2.0; PyPI as `fhaviary`; sister library LDP also open. |
| Maturity / traction | 2 | 278 stars (up from 261); active development through at least 2026-07-20 (new Jupyter-notebook environment added); embedded in FutureHouse evaluation stack. |
| Cross-family policy | 1 | Environment-agnostic; cross-family possible by user setup. |
| Runtime assurance | 1 | Trajectory logging + environment-level scoring; not a runtime claim-audit harness. |
| Cross-platform portability | 2 | Pip-installable; pairs with LDP; multi-environment by design. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `literature-discovery`


**Architectural features:** `tool-use` `artifact-versioning`


**Inputs:** `task-specification`


**Outputs:** `agent-trajectories` `evaluation-metrics`


**Data sources:** `benchmark-datasets` `scientific-literature`


**Knowledge sources:** `paper-qa`


## Limitations

- Evaluation infrastructure, not a RISE pipeline — included here for completeness, scored conservatively on lifecycle coverage.
- Benchmarks reflect the environments included; coverage of social-science tasks limited.

## Related projects in this catalog

- [`paper-qa`](paper-qa.md)
- [`robin`](robin.md)

## Papers describing this project

- **Aviary: training language agents on challenging scientific tasks** — Narayanan, S., Braza, J. D., Griffiths, R., Ponnapati, M., Bou, A., Laurent, J., et al. (2024). *arXiv*. [arXiv:2412.21154](https://arxiv.org/abs/2412.21154)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
