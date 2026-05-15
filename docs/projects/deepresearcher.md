<!-- DO NOT EDIT — auto-generated from projects/landscape/deepresearcher.yml by scripts/build_indexes.py -->

# DeepResearcher (GAIR-NLP)

`external` · status: `active` · focus: `literature` · discipline: `general` · started: 2025

**Project page:** <https://github.com/GAIR-NLP/DeepResearcher>

**Source:** [`projects/landscape/deepresearcher.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/deepresearcher.yml)

## Positioning

An end-to-end RL-trained deep-research agent (arXiv:2504.03160) that learns to plan, retrieve, cross-validate, and self-reflect via reinforcement learning in real-world web environments rather than in simulated retrieval. Ships a 7B HuggingFace checkpoint (DeepResearcher-7b) trained via this pipeline.

## Distinctive contribution

Argues that *end-to-end RL on real web environments* — not prompt engineering and not RL on retrieval simulators — is what unlocks emergent cognitive behaviors in research agents (planning, multi- source cross-validation, self-reflection, honest non-answer when evidence is missing). Reports +28.9 points over prompt baselines and +7.2 over RAG-RL baselines.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three deep-research stages. |
| Autonomy level | 3 | Designed for autonomous multi-turn research without per-step approval. |
| Architectural transparency | 3 | Open under Apache-2.0; arXiv:2504.03160 documents training; checkpoint released; code public. |
| Inputs supported | 2 | Research-question inputs; trained for real-world web environments rather than simulated retrieval. |
| Outputs / reproducibility | 2 | Released checkpoint enables reproducible inference; full RL training pipeline released. |
| Internal evaluation | 3 | Quantitative gains vs. prompt-engineering and RAG-RL baselines reported in the arXiv paper. |
| Openness | 3 | Apache-2.0; open weights on HuggingFace; permissive license. |
| Maturity / traction | 2 | 751 stars; active; recent academic release (2025-04). |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `literature-discovery` `literature-synthesis`


**Architectural features:** `tool-use` `iterative-loop` `rag-knowledge-base`


**Inputs:** `research-question`


**Outputs:** `research-report` `citations`


**Data sources:** `web-search`


**Knowledge sources:** `web-search`


## Limitations

- 7B parameter scale limits ceiling on the hardest benchmarks.
- RL training is compute-intensive and not trivially reproducible end-to-end.
- Live-web inference is non-deterministic by design.

## Related projects in this catalog

- [`tongyi-deepresearch`](tongyi-deepresearch.md)
- [`gpt-researcher`](gpt-researcher.md)
- [`storm`](storm.md)

## References

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
