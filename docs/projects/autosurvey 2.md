<!-- DO NOT EDIT — auto-generated from projects/landscape/autosurvey.yml by scripts/build_indexes.py -->

# AutoSurvey

`external` · status: `dormant` · focus: `literature` · discipline: `general` · started: 2024

**Project page:** <https://github.com/AutoSurveys/AutoSurvey>

**Source:** [`projects/landscape/autosurvey.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/autosurvey.yml)

## Positioning

A NeurIPS 2024 framework (arXiv:2406.10252) for automatically generating comprehensive literature surveys from a topic and a paper database. Demonstrated on survey lengths of 8k–64k tokens with reported citation-quality and content-quality scores. Sits squarely in the literature-synthesis stage of the RISE diagram.

## Distinctive contribution

Among the first systems to treat *long-form survey writing* (not short-form QA or summarization) as the target task, with explicit evaluation of citation quality at scale. Ships with a 530K-abstract arXiv-CS database used in the published experiments.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three stages clustered around literature synthesis and drafting. |
| Autonomy level | 3 | Runs end-to-end from a topic to a survey; no per-step approval. |
| Architectural transparency | 2 | NeurIPS 2024 paper documents the framework; code and database public; prompts visible. |
| Inputs supported | 1 | Topic input only; database is fixed (CS-arXiv abstracts in the public release). |
| Outputs / reproducibility | 2 | Code + database + commands published for paper experiments. |
| Internal evaluation | 3 | Systematic evaluation across multiple survey lengths in the NeurIPS paper. |
| Openness | 1 | No license declared in repository metadata — defaults to all rights reserved; database access via OneDrive link from maintainers. |
| Maturity / traction | 1 | 468 stars; activity slowed sharply after the NeurIPS publication (last push 2025-02). |
| Cross-family policy | 0 | Single LLM per run. |
| Runtime assurance | 1 | Citation-quality and content-quality scoring in NeurIPS paper; no in-pipeline claim audit harness. |
| Cross-platform portability | 1 | Code + paper-DB available; single back-end. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `paper-drafting`


**Architectural features:** `multi-agent` `rag-knowledge-base` `iterative-loop`


**Inputs:** `survey-topic`


**Outputs:** `long-form-survey` `citations`


**Data sources:** `arxiv-cs-abstracts`


**Knowledge sources:** `arxiv`


## Limitations

- No declared open-source license — reuse rights are uncertain.
- Database limited to CS-arXiv abstracts in the public release; full-text version requires contacting authors.
- Last commit ~2025-02; appears semi-maintained.

## Related projects in this catalog

- [`surveyx`](surveyx.md)
- [`storm`](storm.md)
- [`open-scholar`](open-scholar.md)

## Papers describing this project

- **AutoSurvey: Large Language Models Can Automatically Write Surveys** — Wang, Y., Guo, Q., Yao, W., Zhang, H., Zhang, X., Wu, Z., et al. (2024). *NeurIPS 2024*. [arXiv:2406.10252](https://arxiv.org/abs/2406.10252)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
