<!-- DO NOT EDIT — auto-generated from projects/landscape/robin.yml by scripts/build_indexes.py -->

# Robin (FutureHouse)

`external` · status: `active` · focus: `end-to-end` · discipline: `biomedical` · started: 2025

**Project page:** <https://github.com/Future-House/robin>

**Source:** [`projects/landscape/robin.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/robin.yml)

## Positioning

A multi-agent system for automating scientific discovery (arXiv:2505.13400), with explicit support for hypothesis generation, experiment design, and data analysis. The hypothesis and experiment modules are usable standalone; the full data-analysis path requires FutureHouse's commercial Edison platform.

## Distinctive contribution

One of the few openly-documented RISE systems that explicitly separates *hypothesis generation* and *experiment design* as modular, runnable components rather than bundling them into a monolithic ideation step. FutureHouse-blog write-up demonstrates a full end-to-end scientific-discovery run.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Four stages spanning ideation through analysis; no drafting or review. |
| Autonomy level | 2 | Supervised: human researcher provides RQ; agents execute the discovery loop. |
| Architectural transparency | 3 | Open under Apache-2.0; arXiv paper + FutureHouse blog post; Docker setup published. |
| Inputs supported | 2 | Research-question inputs; integrated retrieval; multiple LLM providers via LiteLLM. |
| Outputs / reproducibility | 1 | Hypothesis/experiment paths runnable offline; full analysis path requires paid Edison API. |
| Internal evaluation | 2 | Demonstrated end-to-end run on a biological discovery task in the arXiv paper. |
| Openness | 2 | Source open under Apache-2.0, but full functionality gated behind commercial API credits. |
| Maturity / traction | 2 | 301 stars; FutureHouse backing; recent (April 2026). |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-acquisition` `data-analysis`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base` `iterative-loop`


**Inputs:** `research-question`


**Outputs:** `hypotheses` `experiment-design` `analysis-results`


**Data sources:** `edison-platform` `literature`


**Knowledge sources:** `literature` `paper-qa`


## Limitations

- Data-analysis path requires paid Edison API credits.
- Biomedical orientation; portability to other empirical disciplines untested.
- Quality depends on access to recent commercial LLMs.

## Related projects in this catalog

- [`paper-qa`](paper-qa.md)
- [`aviary`](aviary.md)
- [`agent-laboratory`](agent-laboratory.md)

## Papers describing this project

- **Robin: A multi-agent system for automating scientific discovery** — Ghareeb, A. E., Chang, B., Mitchener, L., Yiu, A., Szostkiewicz, C. J., Laurent, J. M., et al. (2025). *arXiv*. [arXiv:2505.13400](https://arxiv.org/abs/2505.13400)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
