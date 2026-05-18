<!-- DO NOT EDIT — auto-generated from projects/landscape/data-to-paper.yml by scripts/build_indexes.py -->

# data-to-paper

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2023

**Project page:** <https://github.com/Technion-Kishony-lab/data-to-paper>

**Source:** [`projects/landscape/data-to-paper.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/data-to-paper.yml)

## Positioning

An end-to-end framework that takes annotated data and produces *backward-traceable* scientific manuscripts: every numeric value in the output can be click-traced to the specific code line that generated it. Navigates interacting LLM and rule-based agents through data exploration, literature search, hypothesis raising, code-debugging, interpretation, and step-by-step paper writing. Released alongside an NEJM AI peer-reviewed paper (Ifargan et al., 2024 — DOI:10.1056/AIoa2400555).

## Distinctive contribution

The "data-chained" provenance design is unique in the catalog: the manuscript is constructed so that traceability is intrinsic, not a reporting add-on — any reported number resolves backward through the data analysis steps. Ships both Autopilot and Copilot modes (oversee / inspect / guide / rewind / replay) and overrides standard statistical packages with coding guardrails to minimize common LLM coding errors.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Seven stages from hypothesis through revision; explicitly skips referee simulation and dissemination. |
| Autonomy level | 3 | Autopilot mode runs end-to-end from data; Copilot mode adds human oversight on demand. |
| Architectural transparency | 3 | Open under MIT; NEJM AI paper + arXiv:2404.17605 document the method; agent prompts visible. |
| Inputs supported | 2 | Accepts annotated datasets with optional research-goal specification; open-goal and fixed-goal modes. |
| Outputs / reproducibility | 3 | Backward-traceable manuscripts where any numeric value resolves to its generating code line — strongest reproducibility design in the catalog. |
| Internal evaluation | 3 | Peer-reviewed publication in NEJM AI demonstrating the framework; example papers across diabetes, social-network, and clinical datasets. |
| Openness | 3 | MIT-licensed; pip-installable; example datasets + example papers all public. |
| Maturity / traction | 2 | 793 stars; NEJM AI publication; last push 2025-07 — slower cadence but stable mature release. |
| Cross-family policy | 0 | Single-LLM design with rule-based agents alongside; no cross-family review architecture. |
| Runtime assurance | 2 | Coding guardrails (overridden statistical packages), data-chaining provenance checks, and AI-review-on-demand in Copilot mode. |
| Cross-platform portability | 1 | Pip package; works with multiple LLM back-ends, but no native multi-IDE adaptation layer. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `literature-discovery` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing`


**Architectural features:** `multi-agent` `human-in-loop` `tool-use` `artifact-versioning` `dag-orchestration`


**Inputs:** `annotated-dataset` `research-goal`


**Outputs:** `traceable-manuscript` `data-chained-paper` `code`


**Data sources:** `user-provided`


**Knowledge sources:** `literature`


## Limitations

- Designed for 'relatively simple research goals and simple datasets' per the authors — does not yet target deep theoretical or large-scale studies.
- Last push 2025-07; cadence has slowed since the NEJM publication.
- No referee-simulation or dissemination-packaging stages.

## Related projects in this catalog

- [`e2er`](e2er.md)
- [`ape`](ape.md)
- [`clo-author`](clo-author.md)
- [`sakana-ai-scientist`](sakana-ai-scientist.md)

## Papers describing this project

- **Autonomous LLM-Driven Research — from Data to Human-Verifiable Research Papers** — Ifargan, T., Hafner, L., Kern, M., Alcalay, O., Kishony, R. (2024). *NEJM AI*. [doi](https://doi.org/10.1056/AIoa2400555)
- **Autonomous LLM-driven research from data to human-verifiable research papers** — Ifargan, T., Hafner, L., Kern, M., Alcalay, O., Kishony, R. (2024). *arXiv preprint*. [arXiv:2404.17605](https://arxiv.org/abs/2404.17605)

## Also compared in

- **ARIS Table 4** ([`yang2026aris`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Listed as 'data-driven (not open-ended idea-to-paper)' with narrower research state retention.

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
