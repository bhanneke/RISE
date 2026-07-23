<!-- DO NOT EDIT — auto-generated from projects/landscape/tongyi-deepresearch.yml by scripts/build_indexes.py -->

# Tongyi DeepResearch

`external` · status: `active` · focus: `literature` · discipline: `general` · started: 2025

**Project page:** <https://github.com/Alibaba-NLP/DeepResearch>

**Source:** [`projects/landscape/tongyi-deepresearch.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/tongyi-deepresearch.yml)

## Positioning

An agentic large language model purpose-built for long-horizon deep-information-seeking tasks (arXiv:2510.24701), shipped both as open weights (30.5B total / 3.3B active) and as inference code with ReAct and 'Heavy' (IterResearch) modes. Sits in the literature/ synthesis block of the RISE diagram, with state-of-the-art reported results on agentic-search benchmarks (BrowseComp, FRAMES, Humanity's Last Exam).

## Distinctive contribution

Treats agentic-research capability as a *model-training* problem, not just an orchestration problem: continual agentic pre-training, fully automated synthetic data generation, and end-to-end on-policy RL with GRPO. Distinguishes itself from prompt-engineering pipelines by shipping a model purpose-trained for research-style tool use.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three deep-research stages; not an end-to-end paper-writing pipeline. |
| Autonomy level | 3 | Runs end-to-end without per-step approval; long-horizon trajectories are the design target. |
| Architectural transparency | 3 | Open under Apache-2.0; arXiv:2510.24701 + technical blog document training and inference. |
| Inputs supported | 2 | Research-query inputs; ReAct and Heavy inference paradigms; HuggingFace + ModelScope deployment. |
| Outputs / reproducibility | 2 | Open weights and inference scripts; full training pipeline partially released. |
| Internal evaluation | 3 | Extensive benchmark results reported on BrowseComp, FRAMES, HLE, SimpleQA; state-of-the-art on several. |
| Openness | 3 | Apache-2.0; HuggingFace + ModelScope checkpoints; commercial deployment via Bailian. |
| Maturity / traction | 3 | 19.7k+ stars; production deployment via Aliyun Bailian; technical report revised (arXiv 2510.24701 v3, 2026-05-19); repo itself quiet since 2026-02. |
| Cross-family policy | 0 | Self-trained model; no architectural cross-family policy. |
| Runtime assurance | 1 | IterResearch 'Heavy' mode adds test-time deliberation; no published claim-audit harness. |
| Cross-platform portability | 2 | HuggingFace + ModelScope + Bailian deployment; ReAct + IterResearch inference modes. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `literature-discovery` `literature-synthesis`


**Architectural features:** `tool-use` `rag-knowledge-base` `iterative-loop`


**Inputs:** `research-question`


**Outputs:** `cited-response` `research-report`


**Data sources:** `web-search`


**Knowledge sources:** `web-search`


## Limitations

- Specialized for deep-information-seeking; does not produce papers, code, or replication packages directly.
- Heavy mode is compute-expensive; quality–cost trade-off non-trivial.
- Real-world agentic search depends on live web state — outputs not bitwise reproducible.

## Related projects in this catalog

- [`gpt-researcher`](gpt-researcher.md)
- [`deepresearcher`](deepresearcher.md)
- [`storm`](storm.md)
- [`paper-qa`](paper-qa.md)

## Papers describing this project

- **Tongyi DeepResearch Technical Report** — Tongyi DeepResearch Team (2025). *arXiv (Alibaba)*. [arXiv:2510.24701](https://arxiv.org/abs/2510.24701)

## Also compared in

- **Agentic AI for Scientific Discovery: A Survey** ([`gridach2025agenticsurvey`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Covered as a deep-research agent trained via RL.

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
