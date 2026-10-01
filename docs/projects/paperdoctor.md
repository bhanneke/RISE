<!-- DO NOT EDIT — auto-generated from projects/landscape/paperdoctor.yml by scripts/build_indexes.py -->

# PaperDoctor

`external` · status: `active` · focus: `review` · discipline: `general` · started: 2026

**Project page:** <https://github.com/QinghongLin/paperdoctor>

**Licence:** `MIT`

**Source:** [`projects/landscape/paperdoctor.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/paperdoctor.yml)

## Positioning

An agent framework that gives pre-submission papers an evidence-grounded diagnostic rather than a verdict: it checks writing, layout, references, code, theory, prior work, and experiments, and for high-priority claims reruns the paper's own code to verify them. Sits in the RISE referee-simulation / revision-editing layer alongside `reviewer`, `coarse-ink`, and `ai-research-feedback`, but is architected as a three-layer surface/verifier/reproducer stack rather than a panel of generalist reviewer personas.

## Distinctive contribution

Every finding is an auditable triple (observation, evidence pointer — a sentence, equation, or code line — and revision suggestion), and its L3 layer selectively re-executes experiments to confirm or refute specific claims rather than relying on LLM judgment alone. Packaged as 11 Claude Code skills plus Python tooling (PDF parsing via Mathpix/MinerU, code indexing), making the pipeline itself inspectable and installable.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Covers referee-simulation, revision-editing, and selective claim re-execution (a slice of replication); no ideation/design/drafting. |
| Autonomy level | 2 | Runs the full L1-L3 diagnostic pipeline unattended, but human sets up the run (supplies paper+repo) and reviews the final report. |
| Architectural transparency | 3 | Full skill definitions, Python tools, and quick-start pipeline published in the repo; paper documents the 3-layer architecture in detail. |
| Inputs supported | 2 | Two input forms (paper PDF + code repo) with access to the paper's own cited-literature and experiment artifacts. |
| Outputs / reproducibility | 1 | Persists a structured diagnostic report (prose + evidence pointers); no versioned paper+code+data manifest output. |
| Internal evaluation | 2 | Systematically compared against human reviewers and other agentic reviewers in the paper's own study; not yet third-party validated. |
| Openness | 2 | MIT license, pip-installable with documented quick-start; requires paid Mathpix (or MinerU fallback) and LLM API credentials to run. |
| Maturity / traction | 1 | 38 stars / 1 fork as of scoring date; posted September 2026, multi-institution authorship but single public release. |
| Cross-family policy | 0 | Built as Claude Code skills; no documented cross-model-family review requirement or default. |
| Runtime assurance | 2 | L2 typed verifiers route claims to dedicated checkers and L3 selectively reruns experiments — multiple in-pipeline gates before the report is finalized. |
| Cross-platform portability | 0 | Tied to the Claude Code skill format; no evidence of other agent-runtime adapters. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation` `revision-editing` `replication`


**Architectural features:** `multi-agent` `tool-use`


**Inputs:** `paper draft (PDF)` `paper's own code repository`


**Outputs:** `evidence-grounded diagnostic report` `revision suggestions`


**Knowledge sources:** `paper's own cited prior work` `paper's own code/experiments`


## Limitations

- Requires paid Mathpix (or MinerU) and LLM API credentials; not free to run at scale.
- Packaged specifically as Claude Code skills — portability to other agent runtimes is untested.
- Very young (38 stars); evaluated only in its own benchmark study, no independent adoption evidence yet.

## Related projects in this catalog

- [`ai-research-feedback`](ai-research-feedback.md)
- [`reviewer`](reviewer.md)
- [`coarse-ink`](coarse-ink.md)
- [`ai-peer-review-skill`](ai-peer-review-skill.md)

## Papers describing this project

- **PaperDoctor: Evidence-Grounded and Actionable Feedback for Scientific Papers in Progress** — Lin, K.Q., Hu, S., Lu, P., and 14 others (2026). *arxiv*. [arXiv:2609.16995](https://arxiv.org/abs/2609.16995)
