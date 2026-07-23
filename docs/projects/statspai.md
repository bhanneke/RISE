<!-- DO NOT EDIT — auto-generated from projects/landscape/statspai.yml by scripts/build_indexes.py -->

# StatsPAI

`external` · status: `active` · focus: `analysis` · discipline: `economics` · started: 2025

**Project page:** <https://github.com/brycewang-stanford/StatsPAI>

**Source:** [`projects/landscape/statspai.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/statspai.yml)

## Positioning

An "agent-native" Python library for causal inference and applied econometrics — a Stata/R-replacement workbench (regress, ivreg, feols, Callaway-Sant'Anna DiD, rdrobust, synthetic control, matching, DML, meta-learners, causal forests, structural estimation; 1,145 registered functions across 87 submodules) whose structured result objects, machine-readable schemas, and MCP server are designed for LLM agents to call. Sits in the infrastructure-for-pipelines layer of RISE, like ToolUniverse, not a research pipeline itself.

## Distinctive contribution

The catalog's clearest case of tooling redesigned *for* agents rather than agents wrapped around tooling: one `import statspai as sp` entry point, `.to_agent_summary()` / `.to_latex()` / serialization on every result object, an MCP server, and a validation-tiered registry that records per-estimator R/Stata reference-parity status separately from API breadth — explicitly so that surface area is not passed off as validation evidence.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Estimation/analysis library touching one stage; all other lifecycle stages are left to the calling agent or companion skill repos (AERS, Paper-WorkFlow). |
| Autonomy level | 0 | Pure tool: every estimation call is driven by a human or an external agent; the library performs no orchestration of its own. |
| Architectural transparency | 3 | Full open source with machine-readable schemas, a function registry with per-estimator validation status, extensive docs, and a very detailed changelog. |
| Inputs supported | 1 | Single input form (dataframe + formula/estimator spec) plus bundled teaching datasets (Card 1995, LaLonde, mpdta, Lee 2008, Prop 99); no literature access. |
| Outputs / reproducibility | 2 | Structured result objects with tidy/LaTeX/DOCX export, plotting, citation, and serialization; deterministic reruns, but no end-to-end paper/data-manifest artifacts. |
| Internal evaluation | 2 | R/Stata reference-parity tests with validation_status tiers and sp.cross_validate, ~200k LOC of tests in CI; JOSS review pending, no external validation yet. |
| Openness | 3 | MIT license, pip-installable from PyPI, examples run offline on commodity hardware after install; Zenodo-archived releases. |
| Maturity / traction | 2 | 282 stars / 58 forks, v1.20.0 with rapid release cadence over ~12 months, PyPI + Zenodo DOI; external adoption still modest and peer review (JOSS) not yet complete. |
| Cross-family policy | 0 | Not applicable — no LLM in the loop; a deterministic library callable from any model family. |
| Runtime assurance | 1 | Schema-validated structured results, validation-tier metadata, and audit methods on result objects; no claim-audit stack (largely inapplicable to a library). |
| Cross-platform portability | 2 | Three integration surfaces — plain Python API, MCP server, and skill packaging — all provider-agnostic, but deployment is confined to Python environments. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis`



**Inputs:** `user-dataset` `model-formula`


**Outputs:** `estimation-results` `publication-tables` `figures`


**Data sources:** `user-provided` `bundled-teaching-datasets`


## Limitations

- A library, not a research system: design choice, specification, and interpretation remain entirely with the calling agent or human.
- Only a subset of the 1,145 registered functions carries certified R/Stata parity — validation_status must be checked per estimator; API breadth outpaces validation depth.
- Very high single-team development velocity (~600 KB changelog, 97 KB migration guide in about a year) raises API-stability concerns; JOSS review still pending.

## Related projects in this catalog

- [`auto-empirical-research-skills`](auto-empirical-research-skills.md)
- [`tooluniverse`](tooluniverse.md)
- [`recast-causal-ai`](recast-causal-ai.md)
