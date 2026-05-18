<!-- DO NOT EDIT — auto-generated from projects/landscape/marg.yml by scripts/build_indexes.py -->

# MARG (Multi-Agent Review Generation)

`external` · status: `active` · focus: `review` · discipline: `general` · started: 2024

**Project page:** <https://github.com/allenai/marg-reviewer>

**Source:** [`projects/landscape/marg.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/marg.yml)

## Positioning

A research artifact (arXiv:2401.04259) and reusable demo for generating peer reviews of scientific papers using multiple specialized agents. Ships with a web interface and reproduction scripts for the published user study comparing MARG-S to single-LLM baselines (SARG-B, LiZCa). Sits at the referee-simulation stage of the RISE pipeline.

## Distinctive contribution

Among the earliest peer-reviewed treatments of agentic peer review, with an explicit user study comparing review quality across multiple generation strategies. The repository functions as both a runnable demo and a reproducibility package for the paper.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage (referee simulation). |
| Autonomy level | 2 | Supervised: user submits a paper; multiple review variants generated. |
| Architectural transparency | 3 | Open Apache-2.0; arXiv paper documents method; reproduction configs + GPT cache included. |
| Inputs supported | 1 | Single input form (paper PDF/text). |
| Outputs / reproducibility | 3 | Bundled GPT cache + alignment-metric configs make published-paper experiments reproducible. |
| Internal evaluation | 2 | User study + alignment metrics in the arXiv paper compare three review-generation strategies. |
| Openness | 3 | Apache-2.0; Docker-compose deployment; AI2 backing. |
| Maturity / traction | 1 | 63 stars; cited research artifact rather than a widely-adopted product. |
| Cross-family policy | 0 | Single-LLM-family; uses OpenAI API. |
| Runtime assurance | 1 | Schema validation + alignment-metric scoring of reviews; no in-pipeline claim audit. |
| Cross-platform portability | 0 | Docker-compose deployment; single-LLM tied. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation`


**Architectural features:** `multi-agent` `tool-use`


**Inputs:** `submitted-paper`


**Outputs:** `generated-review` `alignment-metrics`


**Data sources:** `aries-dataset`


**Knowledge sources:** `paper-text`


## Limitations

- Pre-2024 model assumptions; modern frontier models may shift the comparison.
- Single-stage tool; needs to be embedded in a pipeline for end-to-end use.
- Requires OpenAI API access.

## Related projects in this catalog

- [`ape`](ape.md)
- [`reviewer`](reviewer.md)

## Papers describing this project

- **MARG: Multi-Agent Review Generation for Scientific Papers** — D'Arcy, M., Hope, T., Birnbaum, L., Downey, D. (2024). *arXiv*. [arXiv:2401.04259](https://arxiv.org/abs/2401.04259)

## Related references (literature catalog)

- `gartenberg2026morebetter` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `naddaf2025aipeer` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `neurips2024checklist` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
