<!-- DO NOT EDIT — auto-generated from projects/landscape/pai-econ-claude.yml by scripts/build_indexes.py -->

# pAI-Econ-claude

`external` · status: `active` · focus: `end-to-end` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/maxwell2732/pAI-Econ-claude>

**Source:** [`projects/landscape/pai-econ-claude.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/pai-econ-claude.yml)

## Positioning

A gated, human-in-the-loop multi-agent Claude Code Skill for AI-assisted economic THEORY development: a 10-stage sequential pipeline (research intake → puzzle refinement → literature → canonical-model matching → model primitives → assumption audit → propositions → proof sketches → counterexample search → economic interpretation → manuscript generation) with an optional numerical- simulation stage, 8 quality gates, and 6+ mandatory human decision points. Sits alongside theorist-toolbox (morankor) in the RISE formal-modeling layer, as an independent, differently-architected attempt at the same "trustable AI help on economic theory" problem.

## Distinctive contribution

A 40+ template "model_library" of canonical economic-theory models (micro/labor/trade/IO) used for novelty-risk and canonical-fit gating — a structured prior that theorist-toolbox does not have — plus a companion arXiv paper (2607.21268) reporting a controlled before/after evaluation on 5 matched theory tasks against an ungated baseline: mean failure severity fell 1.58→1.16 and reported usefulness rose 2.60→3.10, the closest thing to a quantitative ablation in the catalog's economic-theory-agent niche.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five declared stages (RQ/puzzle refinement, literature, formal modeling, optional code generation, manuscript drafting) with gaps — no dedicated literature-synthesis or referee-simulation stage as such (review lives inside internal gates, not as a pipeline stage). |
| Autonomy level | 1 | 6+ mandatory human decision points across 8 gated stages — closer to copilot (human approves each significant step) than a supervised-and-review-only agent. |
| Architectural transparency | 3 | MIT license; 20+ stage-specific prompt files, SKILL.md routing logic, the model_library templates, and gate logic all published in the repo. |
| Inputs supported | 1 | Primary input is a free-text research idea/puzzle; an 'Empirical Companion' mode exists for applied-research inputs but no external literature-corpus or data-source connector is documented. |
| Outputs / reproducibility | 2 | Each stage persists a versioned intermediate record (propositions, proof sketches, optional simulation code/figures, manuscript files) gated by human checkpoints; no demonstrated end-to-end reproducibility across arbitrary runs. |
| Internal evaluation | 2 | Companion arXiv preprint (2607.21268) evaluates the gated pipeline against an ungated baseline on 5 matched economic-theory tasks with severity/usefulness scoring; not yet externally peer-reviewed or replicated by a third party. |
| Openness | 2 | MIT license, example inputs in examples/ for quickstart, but running the full pipeline requires a paid Claude Code/API subscription — not free-tier reproducible. |
| Maturity / traction | 2 | 168 stars / 58 forks, tagged v1.4.0, 38 commits, active as of August 2026 — beta-stage with growing external adoption but single-team origin. |
| Cross-family policy | 0 | Single-model by design — built specifically as a Claude Code Skill (name and commands are Claude-specific); no cross-family review mechanism. |
| Runtime assurance | 3 | 8 in-pipeline gates (novelty risk, canonical-model fit, model coherence, proof integrity, economic meaning, mathematical review) that diagnose failure modes and trigger loopbacks before a stage can advance — a full runtime audit stack with gating on failure. |
| Cross-platform portability | 0 | Locked to Claude Code as a Claude Code Skill; no documented support for other IDEs, runtimes, or model providers. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `literature-discovery` `formal-modeling` `code-generation` `paper-drafting`


**Architectural features:** `multi-agent` `human-in-loop` `dag-orchestration` `iterative-loop`


**Inputs:** `research-idea` `user-dataset`


**Outputs:** `propositions` `proofs` `paper-draft` `figures`


**Data sources:** `user-provided`


**Knowledge sources:** `model-library-templates`


## Limitations

- Locked to a single platform (Claude Code) and a single model family, unlike theorist-toolbox's Codex-adversarial-pair option.
- Evaluation is a preprint self-reported on 5 matched tasks by the same team that built the system — no external replication yet.
- Requires a paid Claude Code/API subscription to run; not reproducible on free infrastructure.

## Related projects in this catalog

- [`econcs-bench`](econcs-bench.md)
- [`ai-co-mathematician`](ai-co-mathematician.md)

## Papers describing this project

- **pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assisted Economic Theory Development** — Zhu, C., Wang, X., Zhang, W. (2026). *arXiv*. [arXiv:2607.21268](https://arxiv.org/abs/2607.21268)
