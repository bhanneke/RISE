<!-- DO NOT EDIT — auto-generated from projects/landscape/ape.yml by scripts/build_indexes.py -->

# APE — Automated Peer Evaluator

`external` · status: `active` · focus: `review` · discipline: `general` · started: 2026

**Project page:** <https://ape.socialcatalystlab.org/>

**Source:** [`projects/landscape/ape.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ape.yml)

## Positioning

A focused tool for automated peer evaluation of submitted papers, sitting at the *referee-simulation* stage of the RISE pipeline. Does not produce papers itself; consumes them and produces structured reviews.

## Distinctive contribution

Treats peer review as a first-class agentic capability with its own product surface, decoupled from upstream authoring. Provides a reusable evaluation interface that other RISE pipelines can route drafts through.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage (referee simulation) only. |
| Autonomy level | 2 | Supervised agent: user submits a paper and receives a structured review. |
| Architectural transparency | 1 | Service homepage describes capability; internals not publicly documented in detail. |
| Inputs supported | 1 | Accepts submitted papers; limited integration with external corpora. |
| Outputs / reproducibility | 1 | Structured reports are persisted; not aimed at reproducibility across runs. |
| Internal evaluation | 1 | Demonstration-level evaluation; no published systematic benchmark to date. |
| Openness | 1 | Hosted service; source not publicly available at time of scoring. |
| Maturity / traction | 1 | Active service; user-base scope unclear from public info. |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base`


**Inputs:** `submitted-paper`


**Outputs:** `referee-report` `structured-scores`


**Knowledge sources:** `prior-reviews` `literature`


## Limitations

- Single-stage coverage limits use as a standalone RISE system.
- Closed implementation hampers reproducibility of the review process.
- Dependence on a hosted service introduces availability risk.

## Related references (literature catalog)

- `gartenberg2026morebetter` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `naddaf2025aipeer` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `neurips2024checklist` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
