<!-- DO NOT EDIT — auto-generated from projects/landscape/open-scholar.yml by scripts/build_indexes.py -->

# OpenScholar (AI2)

`external` · status: `dormant` · focus: `literature` · discipline: `general` · started: 2024

**Project page:** <https://github.com/AkariAsai/OpenScholar>

**Source:** [`projects/landscape/open-scholar.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/open-scholar.yml)

## Positioning

A retrieval-augmented LM designed to answer scientific queries by searching the literature and generating responses grounded in sources. Releases include training code, an 8B fine-tuned Llama checkpoint, an offline retrieval index, and the ScholarQABench evaluation suite. Sits in the literature block of the RISE diagram with strong evaluation tooling.

## Distinctive contribution

Pairs the inference system with two purpose-built evaluation artifacts — ScholarQABench (automatic) and OpenScholar_ExpertEval (human) — addressing the under-developed *evaluation* axis of scholarly-synthesis systems. Open weights make it usable as a research baseline.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Two stages (discovery + synthesis); a literature-QA building block. |
| Autonomy level | 2 | Supervised: user submits a query, system returns a cited answer. |
| Architectural transparency | 3 | Open under Apache-2.0; arXiv:2411.14199 documents method; training + retrieval code published. |
| Inputs supported | 2 | Scientific queries with optional retrieval-result inputs; supports both open and proprietary LMs. |
| Outputs / reproducibility | 2 | Released retrieval results, model checkpoints, and inference scripts make pipeline runs reproducible. |
| Internal evaluation | 3 | ScholarQABench + expert evaluation interfaces; both quantitative and human evaluation reported. |
| Openness | 3 | Apache-2.0; open weights for Llama-3.1_OpenScholar-8B; data and benchmark publicly released. |
| Maturity / traction | 2 | 1.5k+ stars; cited as a baseline; demo at open-scholar.allen.ai; backed by AI2. |
| Cross-family policy | 1 | 8B open-weight model + optional commercial LLMs; cross-family configurable. |
| Runtime assurance | 1 | ScholarQABench evaluation set + retrieval verification; runtime gating is light. |
| Cross-platform portability | 1 | HuggingFace + Semantic Scholar API + You.com; not multi-IDE. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis`


**Architectural features:** `rag-knowledge-base` `tool-use` `iterative-loop`


**Inputs:** `research-question`


**Outputs:** `cited-response` `citations`


**Data sources:** `semantic-scholar-api` `you-search`


**Knowledge sources:** `semantic-scholar` `web-search`


## Limitations

- Single-stage focus (literature synthesis), not an end-to-end pipeline.
- Quality depends on retrieval coverage; Semantic Scholar API required.
- Last commit slightly older than the most-active projects in this catalog.

## Related projects in this catalog

- [`storm`](storm.md)
- [`paper-qa`](paper-qa.md)
- [`gpt-researcher`](gpt-researcher.md)

## Papers describing this project

- **OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs** — Asai, A., He, J., Shao, R., Shi, W., Singh, A., Chang, J. C., et al. (2024). *arXiv*. [arXiv:2411.14199](https://arxiv.org/abs/2411.14199)

## Also compared in

- **Agentic AI for Scientific Discovery: A Survey** ([`gridach2025agenticsurvey`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Covered as a retrieval-augmented LM for scholarly literature.

## Related references (literature catalog)

- Asai, A. et al. (2024). [*OpenScholar: Synthesizing Scientific Literature with Retrieval-augmented LMs*](../papers/notes/asai2024openscholar.md) `asai2024openscholar`
- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Ji, Z. et al. (2023). [*Survey of Hallucination in Natural Language Generation*](../papers/notes/ji2023hallucination.md) `ji2023hallucination`
