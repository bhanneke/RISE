<!-- DO NOT EDIT — auto-generated from projects/landscape/recast-causal-ai.yml by scripts/build_indexes.py -->

# RECAST (Replication and Extension with Causal AI Statistical Toolkit)

`external` · status: `active` · focus: `replication` · discipline: `econometrics` · started: 2026

**Project page:** <https://github.com/qgallea/recast-showcase>

**Source:** [`projects/landscape/recast-causal-ai.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/recast-causal-ai.yml)

## Positioning

An end-to-end autonomous pipeline for the *replication + extension + peer-review* arc of the RISE concept diagram. Given a published econometrics paper and its replication data, RECAST reproduces the original results, extends them using Double/Debiased Machine Learning (7 ML methods, 20+ sample splits) and Causal Forests, runs the extended findings through a structured three-referee AI review, and emits a final synthesis report.

## Distinctive contribution

Couples *replication* with *methodological extension* — most agentic-replication tools stop at "did we get the same numbers?"; RECAST proposes that the same agentic infrastructure should also push existing papers forward with modern causal-ML estimators and have its own output stress-tested by AI referees before publication.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Spans six pipeline stages (replication, data, analysis, code, peer review, drafting) — broader than pure replication tools. |
| Autonomy level | 2 | Supervised: user supplies target paper + data; system runs the rest autonomously, including the multi-referee review. |
| Architectural transparency | 1 | Was 3 (MIT, skill files as self-documenting architecture); original repo removed/made private mid-2026 — pipeline internals no longer publicly inspectable, only the showcase description. |
| Inputs supported | 2 | Accepts target paper PDF/text + replication dataset; integrates external knowledge via Claude Code tool use. |
| Outputs / reproducibility | 2 | Replicated tables, extension results, code, and referee reports all persisted as durable artifacts. |
| Internal evaluation | 2 | Built-in three-referee AI review acts as runtime quality control on each run; no large external benchmark of replication-success rates yet. |
| Openness | 1 | Was 3 (MIT, public repo); source repo taken private/deleted mid-2026 — only the public successor 'recast-showcase' (under construction, GitHub Pages site) remains. |
| Maturity / traction | 1 | Active early-stage project (single-developer, low star count as of 2026-05). |
| Cross-family policy | 0 | Single-LLM-family pipeline (Claude Code); referees are isolated instances of the same model family. |
| Runtime assurance | 3 | Structured three-isolated-referee review + synthesis loop is the assurance layer; among the most explicit in the catalog. |
| Cross-platform portability | 1 | Claude-Code-specific (skill files); not portable to other agent harnesses without rewriting. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `replication` `data-acquisition` `data-analysis` `code-generation` `peer-review` `drafting`


**Architectural features:** `tool-use` `multi-agent-review` `dag-orchestration` `artifact-versioning` `claude-code-skill-files`


**Inputs:** `target-paper` `target-dataset`


**Outputs:** `replication-report` `extension-results` `referee-reports` `synthesis-report` `code`


**Data sources:** `target-paper-data`


**Knowledge sources:** `target-paper` `doubleml-literature` `causal-forest-literature`


## Limitations

- Original repo (qgallea/recast-causal-ai) was removed or made private around mid-2026; the public successor qgallea/recast-showcase (created 2026-06-17) is explicitly 'under construction' — source access currently unavailable.
- Tied to the Claude Code skill-file orchestration model — porting requires reimplementing the pipeline.
- Replication-success depends on availability of target paper's data and reproducibility of its code.
- Same-family AI referees may share blind spots with the executor; no cross-family review by default.

## Related projects in this catalog

- [`social-science-replicability`](social-science-replicability.md)
- [`e2er`](e2er.md)

## Papers describing this project

- **Double Machine Learning: A Practical Guide** — Baiardi, A., Naghi, A. A. (2024). *The Econometrics Journal*. [doi](https://doi.org/10.1093/ectj/utae004)
- **How to Write an Effective Referee Report and Improve the Scientific Review Process** — Berk, J. B., Harvey, C. R., Hirshleifer, D. (2017). *Journal of Economic Perspectives 31(1):231–244*. [doi](https://doi.org/10.1257/jep.31.1.231)
