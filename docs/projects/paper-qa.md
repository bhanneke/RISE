<!-- DO NOT EDIT — auto-generated from projects/landscape/paper-qa.yml by scripts/build_indexes.py -->

# PaperQA2 (FutureHouse)

`external` · status: `active` · focus: `literature` · discipline: `general` · started: 2023

**Project page:** <https://github.com/Future-House/paper-qa>

**Source:** [`projects/landscape/paper-qa.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/paper-qa.yml)

## Positioning

A high-accuracy retrieval-augmented generation package focused on scientific PDFs (and Office docs, source code). PaperQA2 combines agentic document retrieval with metadata enrichment (incl. retraction checks) to answer questions over scientific corpora with citations. Sits in the knowledge-layer block of the RISE diagram as a building block, not a full pipeline.

## Distinctive contribution

Reports superhuman performance on scientific QA, summarization, and contradiction-detection tasks in the accompanying 2024 paper, with particular attention to citation accuracy and retraction awareness. Distributed as a battle-tested library that other RISE projects can embed.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Two adjacent stages (discovery + synthesis); a building-block, not a pipeline. |
| Autonomy level | 2 | Supervised: user supplies corpus and question, agent retrieves and answers. |
| Architectural transparency | 3 | Open under Apache-2.0; PaperQA2 paper documents algorithm; PyPI package with rich settings cheatsheet. |
| Inputs supported | 2 | Multiple input formats (PDFs, Office, code); embedding + LLM back-ends configurable. |
| Outputs / reproducibility | 2 | Caching + index reuse make outputs reproducible given fixed inputs and model. |
| Internal evaluation | 3 | Published 2024 paper with comparative benchmarks; widely cited as a reference RAG baseline. |
| Openness | 3 | Apache-2.0; PyPI; documented API; permissive license; reproducibility scripts in repo. |
| Maturity / traction | 3 | 8.5k+ stars, production-grade releases, embedded in downstream FutureHouse systems. |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base` `artifact-versioning`


**Inputs:** `question` `pdf-corpus`


**Outputs:** `answer` `citations` `summary`


**Data sources:** `user-pdfs` `office-documents` `source-code`


**Knowledge sources:** `semantic-scholar` `crossref` `retraction-watch`


## Limitations

- Building block (literature Q&A) — not an end-to-end research pipeline.
- Quality depends on PDF parsing and embedding configuration.
- Best results require access to commercial LLMs.

## Related projects in this catalog

- [`storm`](storm.md)
- [`open-scholar`](open-scholar.md)
- [`gpt-researcher`](gpt-researcher.md)
- [`aviary`](aviary.md)
- [`robin`](robin.md)

## Papers describing this project

- **PaperQA: Retrieval-Augmented Generative Agent for Scientific Research** — Lála, J., O'Donoghue, O., Shtedritski, A., Cox, S., Rodriques, S. G., White, A. D. (2023). *arXiv (PaperQA1)*. [arXiv:2312.07559](https://arxiv.org/abs/2312.07559)
- **Language agents achieve superhuman synthesis of scientific knowledge** — Skarlinski, M. D., Cox, S., Laurent, J. M., Braza, J. D., Hinks, M., Hammerling, M. J., et al. (2024). *arXiv (PaperQA2)*. [arXiv:2409.13740](https://arxiv.org/abs/2409.13740)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Ji, Z. et al. (2023). [*Survey of Hallucination in Natural Language Generation*](../papers/notes/ji2023hallucination.md) `ji2023hallucination`
