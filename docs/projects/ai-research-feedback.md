<!-- DO NOT EDIT — auto-generated from projects/landscape/ai-research-feedback.yml by scripts/build_indexes.py -->

# AI Research Feedback

`external` · status: `active` · focus: `review` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/claesbackman/AI-research-feedback>

**Source:** [`projects/landscape/ai-research-feedback.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ai-research-feedback.yml)

## Positioning

Ten Claude Code skills that referee economics and finance research artifacts before they leave the author's hands. The core is `review-paper`, an 8-subagent referee panel (grammar, internal consistency, claims, mathematics, figures, contribution, plus an opposing-perspective agent) writing a consolidated `reviews/PRE_SUBMISSION_REVIEW_[date].md`, with `review-paper-light` (2 agents) and `review-paper-checks` (3 agents, mechanical only) as cheaper tiers. Sits in the RISE referee-simulation layer alongside reviewer and the review half of academic-research-skills, but is calibrated to a named top-journal set (AER, QJE, JPE, Econometrica, REStud, JF, JFE, RFS, JFQA, AEJ:Macro, JME, RED) rather than to generic academic quality.

## Distinctive contribution

It is the only pack in the catalog that extends referee simulation beyond the manuscript to three neighbouring artifacts: `review-pap` runs a 6-agent panel over pre-analysis plans against AEA/EGAP/OSF registry conventions, `review-grant` a 6-agent panel over NSF / NIH / ERC / Horizon Europe proposals, and `review-paper-code` maps each empirical claim in a draft back to the line of analysis code that produced it. `audit-analysis` runs an adversarial audit of changed analysis code in a deliberately isolated subagent context so the auditor cannot see the author's own justification.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three stages only (research-design via pre-analysis-plan review, revision-editing, referee-simulation); every skill is a critique pass over a document the human already wrote — the README states analysis code is never executed, so `replication` is not claimed even though `review-paper-code` reads code. |
| Autonomy level | 2 | Supervised agent: the human types `/review-paper` once, the skill fans out to 8 parallel general-purpose subagents and writes one consolidated dated report that the human then reads — no per-agent approval gate in between. |
| Architectural transparency | 3 | MIT license with every SKILL.md prompt published, subagent counts and roles enumerated per skill, and the output path of each report documented in the README; no separate evaluation harness is shipped. |
| Inputs supported | 1 | Four document input forms (draft, pre-analysis plan, grant proposal, code diff) but no external literature-corpus or data-source connector — reference checking is done from the draft's own bibliography, so the band-2 requirement of literature *or* data access is not met. |
| Outputs / reproducibility | 1 | Persists prose only: date-stamped markdown reports under `reviews/` plus standalone HTML for `paper-version` and `explain-diff`. No code, figures, or data artifacts are produced, and subagent panels are LLM-stochastic so two runs on the same draft differ. |
| Internal evaluation | 0 | No validation, testing, accuracy, or agreement-with-human-referee claims appear anywhere in the repo documentation (verified by reading the README on 2026-09-08); the 477 stars are adoption signal, not evaluation. |
| Openness | 2 | MIT license and the skills are plain markdown, but running any multi-agent skill requires a paid Claude Code subscription with `general-purpose` subagent access — not reproducible on free infrastructure. |
| Maturity / traction | 2 | 477 stars / 84 forks / 0 open issues, pushed 2026-08-27, created 2026-03-01 — real external adoption, but only 24 commits, no tagged releases or versioning, and a single maintainer. |
| Cross-family policy | 0 | Single-family by design: every subagent in every panel is a Claude Code `general-purpose` subagent, so the 8-agent referee panel is eight views from one model family. No config option for an outside-family reviewer. |
| Runtime assurance | 1 | The review *is* the deliverable, not a gate on a pipeline: nothing blocks or loops back on failure. The only genuine integrity mechanisms are the opposing-perspective agent inside `review-paper` and the isolated subagent context used by `audit-analysis` to prevent the auditor from seeing the author's rationale. |
| Cross-platform portability | 0 | Locked to Claude Code: the README's global requirement is 'Claude Code with access to the general-purpose subagent', and the fan-out design depends on that runtime primitive. No Cursor / Codex / Gemini CLI install path documented. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `research-design` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `debate-consensus` `human-in-loop`


**Inputs:** `paper-draft` `pre-analysis-plan` `grant-proposal` `analysis-code-diff`


**Outputs:** `reviewer-report` `prioritized-fix-list` `code-review-report` `policy-brief-html`


**Knowledge sources:** `target-journal-conventions` `preregistration-registry-conventions`


## Limitations

- Zero reported evaluation — no measured agreement with human referees, no false-positive/false-negative calibration, nothing to indicate whether the 8-agent panel finds real problems or plausible-sounding ones.
- `review-paper-code` and `audit-analysis` reason about code statically; the README states analysis code is never run, so a claim that a table 'matches the code' is an inference, not a re-execution.
- Journal calibration is explicitly top-five economics and top-three finance; feedback may be systematically mis-scaled for field journals or IS venues.
- All eight referee views come from one model family, so correlated blind spots are structurally unaddressed.
- 24 commits, no releases, single maintainer, no license-independent guarantee of continuity.
- Requires a paid Claude Code subscription and cannot be run on any other agent runtime.

## Related projects in this catalog

- [`reviewer`](reviewer.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`econ-agent-skills`](econ-agent-skills.md)
- [`pai-econ-claude`](pai-econ-claude.md)
- [`auto-empirical-research-skills`](auto-empirical-research-skills.md)
