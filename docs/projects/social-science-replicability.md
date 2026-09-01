<!-- DO NOT EDIT — auto-generated from projects/landscape/social-science-replicability.yml by scripts/build_indexes.py -->

# Social Science Replicability Infrastructure

`external` · status: `active` · focus: `replication` · discipline: `social-sciences` · started: 2025

**Project page:** <https://github.com/benjamin-kohler/social_science_replicability>

**Source:** [`projects/landscape/social-science-replicability.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/social-science-replicability.yml)

## Positioning

Infrastructure aimed at the replication stage of the RISE pipeline: given a published paper, attempt to reproduce its empirical results in an automated or semi-automated fashion. Sits squarely in the replication block of the RISE diagram.

## Distinctive contribution

Focuses the agentic-research conversation on *replication of existing papers* rather than generation of new ones — a complementary axis to the AI-scientist line.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Four stages, all in the replication arc; does not cover ideation/drafting. |
| Autonomy level | 2 | Supervised: user supplies target, system attempts replication. |
| Architectural transparency | 2 | Open source; architecture documented in README; prompts visible. |
| Inputs supported | 2 | Accepts target paper + target dataset; integrates external sources. |
| Outputs / reproducibility | 2 | Reports + code persisted; reproducibility-by-design as a stated goal. |
| Internal evaluation | 1 | Demonstrated on example papers; no broad benchmark of replication success rates. |
| Openness | 3 | Open source under permissive license. |
| Maturity / traction | 1 | Active prototype; single-developer-led; 30 stars but repo remains actively committed to (42 commits, most recent 2026-08-31). |
| Cross-family policy | 0 | Single-LLM-family pipeline; methodology extractor + replicator within one family. |
| Runtime assurance | 2 | Code-execution + output-match comparison against target paper is the runtime assurance. |
| Cross-platform portability | 1 | Python-CLI tool; back-end LLM swappable but not multi-IDE. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `replication` `data-acquisition` `data-analysis` `code-generation`


**Architectural features:** `tool-use` `dag-orchestration` `artifact-versioning`


**Inputs:** `target-paper` `target-dataset`


**Outputs:** `replication-report` `code` `comparison-tables`


**Data sources:** `target-paper-data`


**Knowledge sources:** `target-paper`


## Limitations

- Success rate depends heavily on availability of target paper's data + code.
- Limited published benchmarks of replication accuracy.

## Related projects in this catalog

- [`e2er`](e2er.md)

## Papers describing this project

- **Read the Paper, Write the Code: Agentic Reproduction of Social-Science Results** — Köhler, B., Zollikofer, D., Einsiedler, A., Hoyle, A., Ash, E. (2026). *arXiv*. [arXiv:2604.21965](https://arxiv.org/abs/2604.21965)
