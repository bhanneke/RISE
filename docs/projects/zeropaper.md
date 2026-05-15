<!-- DO NOT EDIT — auto-generated from projects/landscape/zeropaper.yml by scripts/build_indexes.py -->

# zeropaper

`external` · status: `active` · focus: `drafting` · discipline: `general` · started: 2025

**Project page:** <https://github.com/alejandroll10/zeropaper>

**Source:** [`projects/landscape/zeropaper.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/zeropaper.yml)

## Positioning

An autonomous paper-writing pipeline that takes a research topic and produces a written paper with minimal user input. Sits firmly in the paper-drafting / revision portion of the RISE pipeline with light upstream ideation.

## Distinctive contribution

Lightweight, accessible single-developer implementation of the autonomous-paper-writing idea, with a focus on minimizing per-paper human input rather than on multi-agent sophistication.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Covers ~4 stages; no formal data analysis, modeling, or referee simulation. |
| Autonomy level | 2 | Supervised agent — user provides topic and reviews output. |
| Architectural transparency | 2 | Open-source code; prompts visible; architecture documentation modest. |
| Inputs supported | 1 | Single input form (topic); no integration of private corpora or datasets. |
| Outputs / reproducibility | 1 | Persists drafts; not aimed at reproducibility of generated content. |
| Internal evaluation | 0 | No reported systematic evaluation of output quality. |
| Openness | 3 | Open source on GitHub; reproducible setup. |
| Maturity / traction | 1 | Single-developer research prototype. |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `literature-discovery` `paper-drafting` `revision-editing`


**Architectural features:** `single-llm` `tool-use` `iterative-loop`


**Inputs:** `research-topic`


**Outputs:** `paper-draft`


**Knowledge sources:** `web-search`


## Limitations

- Output quality unevaluated against external standards.
- No data-analysis or empirical-modeling stages.
- Limited literature integration.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`e2er`](e2er.md)

## Papers describing this project

- **zeropaper companion: Autonomous research paper generation at scale** — Aldea, A. (2026). *SSRN working paper*. [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6687378)
