<!-- DO NOT EDIT — auto-generated from projects/landscape/sakana-ai-scientist-v3.yml by scripts/build_indexes.py -->

# Sakana AI Agentic Scientist (AI-Scientist-v3)

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/SakanaAI/AI-Scientist-v3>

**Licence:** `Apache-2.0`

**Source:** [`projects/landscape/sakana-ai-scientist-v3.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/sakana-ai-scientist-v3.yml)

## Positioning

Third generation of Sakana AI's "AI Scientist" lineage, reframed as an orchestrator that drives off-the-shelf coding-agent CLIs (Claude Code, Codex, Cursor, OpenCode, Gemini, Pi) through a six-phase pipeline — task drafting, investigation, ablations, sealed final evaluation, post-hoc analysis, and paper writing — against a human-authored task.md plus an evaluator, rather than hand-rolling its own agent.

## Distinctive contribution

Replaces v1/v2's single built-in agent with a harness-agnostic design that can run the same task through six different commercial/open coding-agent backends for comparison, and adds a "sealed" final evaluation phase (each phase runs in its own container reading only a run-local snapshot) specifically to prevent the pipeline from grading its own held-out test. Flagship case studies were run across 9 frontier model/harness combinations.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Covers ~7 stages (ideation through paper + optional review/revision); no dedicated literature-discovery or dissemination stage — task.md is human-authored. |
| Autonomy level | 2 | Runs each phase to completion without per-step approval, but a human still writes the task.md brief and evaluator up front; task drafting from a bare prompt is labelled experimental and 'not yet robust' per the README, so full autonomy on novel tasks is unproven. |
| Architectural transparency | 3 | Full code, Hydra configs, phase definitions, and container/evaluation harness publicly released under Apache-2.0; README documents the six-phase design and sealed-evaluation mechanism in detail. |
| Inputs supported | 1 | Single input form (task.md + evaluator + optional GPU preset); no literature-corpus or external-data-source integration described. |
| Outputs / reproducibility | 2 | Persists a per-run directory (results/<task>/<agent>/<run_id>/) with phase subfolders, compiled paper.pdf, and a manifest; reproducibility depends on the task's evaluator and chosen coding-agent backend, which the repo does not pin to exact versions. |
| Internal evaluation | 1 | Flagship claim is a development version that produced one paper accepted at ALIFE 2026, but neither the README nor the arXiv abstract names that paper or gives a benchmark/baseline comparison against prior AI-Scientist versions or other systems — anecdotal at this scoring date. |
| Openness | 2 | Apache-2.0 (reverting from v2's non-permissive 'AI Scientist Source Code License'); examples ship with evaluators so are partially reproducible, but several require Docker + multi-GPU presets, short of fully commodity-hardware reproduction. |
| Maturity / traction | 1 | Released 2026-10-15 (arXiv paper arXiv:2610.18933 submitted 2026-10-13); 575 stars / 81 forks as of 2026-11-01, days after launch — research-prototype stage, too young for an external-adoption claim beyond the single ALIFE acceptance. |
| Cross-family policy | 1 | Supports driving 6 different coding-agent CLIs (Claude, Codex, Cursor, OpenCode, Gemini, Pi) for the same task, but cross-family comparison is a configurable choice, not the default or required path. |
| Runtime assurance | 2 | Sealed final-evaluation containers (phase reads only a run-local snapshot, preventing self-grading) plus rubric-based evaluation during investigation and an optional external AI-reviewer pass — multiple in-pipeline gates, short of a full claim/citation/figure audit stack. |
| Cross-platform portability | 1 | Docker-first runtime with 6 supported coding-agent backends, but README warns agents run with full tool permissions (--allow yolo) and GPU presets assume CUDA; no CPU-only or browser path documented. |

*Scored on 2026-11-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `tool-use` `dag-orchestration` `iterative-loop` `artifact-versioning`


**Inputs:** `research-area` `seed-template`


**Outputs:** `paper-draft` `code` `experiment-logs` `self-review`


**Data sources:** `benchmark-datasets`


## Limitations

- Task definition (task.md + evaluator) is human-authored; bare-prompt task drafting is explicitly flagged experimental and not yet robust.
- No quantitative benchmark or head-to-head comparison against v1/v2 or other AI-scientist systems reported at launch.
- README warns agents run with full tool permissions and inherit whatever API keys they are given — a real operational-security caveat for unattended runs.
- Only one concretely named external validation claim (an ALIFE 2026 acceptance), and the paper itself does not identify that accepted paper.
- Released 10 days before this scoring date — all traction figures are early and may move quickly.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`sakana-ai-scientist-v1`](sakana-ai-scientist-v1.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`zeropaper`](zeropaper.md)

## Papers describing this project

- **The Agentic Scientist: Orchestrating Coding Agents for Automated Scientific (Co-)Discovery** — Lange, R. T., Grillotti, L., Yamada, Y., Charakorn, R., Ha, D. (2026). *arXiv*. [arXiv:2610.18933](https://arxiv.org/abs/2610.18933)
