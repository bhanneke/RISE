<!-- DO NOT EDIT — auto-generated from projects/landscape/mlgym.yml by scripts/build_indexes.py -->

# MLGym (Meta)

`external` · status: `dormant` · focus: `end-to-end` · discipline: `computer-science` · started: 2025

**Project page:** <https://github.com/facebookresearch/MLGym>

**Source:** [`projects/landscape/mlgym.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/mlgym.yml)

## Positioning

A gym-style framework and benchmark (MLGym-Bench, arXiv:2502.14499) for advancing AI research agents on 13 diverse ML research tasks (CV, NLP, RL, game theory). Like [`aviary`](aviary.md), MLGym is **evaluation infrastructure** for RISE-style systems rather than a RISE pipeline itself.

## Distinctive contribution

First gym environment specifically for *ML research tasks* — not general QA or knowledge work — covering idea generation, data processing, method implementation, training, and result analysis as a unified RL training surface. Distinct from Aviary in that it targets the *training* of research agents via RL, not only their evaluation.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Cross-cutting evaluation/training infrastructure; not a pipeline producing scholarship. |
| Autonomy level | 2 | Supervised: user defines tasks; agents act within them; RL training is a separate pipeline. |
| Architectural transparency | 3 | Open source; arXiv:2502.14499; benchmark task definitions public. |
| Inputs supported | 2 | 13 task definitions across CV, NLP, RL, game theory; extensible to user-defined tasks. |
| Outputs / reproducibility | 3 | Reproducible by design — gym-style task specs + trajectory artifacts. |
| Internal evaluation | 2 | Used to benchmark AI research agents in the arXiv paper; framework described as experimental. |
| Openness | 2 | CC BY-NC 4.0 license — open for research and non-commercial use; not permissive for commercial deployment. |
| Maturity / traction | 2 | 599 stars; Meta institutional backing; last push 2025-08; flagged as 'experimental, under heavy development'. |
| Cross-family policy | 0 | Single-family in published baselines; framework agnostic but no policy. |
| Runtime assurance | 1 | Task-level trajectory + leaderboard scoring; runtime gating minimal. |
| Cross-platform portability | 1 | Open framework, multiple agents pluggable; not multi-IDE. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation`


**Architectural features:** `tool-use` `artifact-versioning` `iterative-loop`


**Inputs:** `task-specification`


**Outputs:** `agent-trajectories` `evaluation-metrics` `training-data`


**Data sources:** `benchmark-datasets`


**Knowledge sources:** `task-descriptions`


## Limitations

- Non-commercial license restricts deployment options.
- Evaluation infrastructure — value depends on downstream agent systems being benchmarked.
- ML-research orientation; not designed for empirical-social-science or biomedical tasks.
- Author flag: 'Please expect major changes to the design.'

## Related projects in this catalog

- [`aviary`](aviary.md)
- [`paper2code`](paper2code.md)
- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`sakana-ai-scientist-v1`](sakana-ai-scientist-v1.md)

## Papers describing this project

- **MLGym: A New Framework and Benchmark for Advancing AI Research Agents** — Nathani, D., Madaan, L., Roberts, N., Bashlykov, N., Menon, A., Moens, V., et al. (2025). *arXiv*. [arXiv:2502.14499](https://arxiv.org/abs/2502.14499)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
