<!-- DO NOT EDIT — auto-generated from skills/academic-research-skills.yml by scripts/build_skills_index.py -->

# Academic Research Skills (ARS)

license: `CC BY-NC 4.0` · 4 skills · last update: 2026-05-17

**Source:** <https://github.com/Imbad0202/academic-research-skills>

**Maintainers:** Edward Cheng-I Wu

**Related project entry:** [`academic-research-skills`](../projects/academic-research-skills.md)

**Compatibility:** `claude-code` `codex` `vscode` `jetbrains`

> Distributed as a Claude Code plugin. Four top-level skills, each backed by multiple sub-agents (7–13 each). Notable for claim-faithfulness audit pass (ARS_CLAIM_AUDIT) and cross-model verification.

**Source YAML:** [`skills/academic-research-skills.yml`](https://github.com/bhanneke/RISE/blob/main/skills/academic-research-skills.yml)

## Skills

### `drafting` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`academic-paper`](academic-research-skills/academic-paper.md) | general | `paper-drafting` `revision-editing` | 12-agent paper writing skill with Style Calibration, Writing Quality Check, LaTeX hardening, visualization, revision coaching, citation conversion, anti-leakage protocol, and VLM figure verification. | [view](academic-research-skills/academic-paper.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/academic-paper/SKILL.md) | 2026-05 |

### `literature` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`deep-research`](academic-research-skills/deep-research.md) | general | `literature-discovery` `literature-synthesis` | 13-agent research team with Socratic guided mode, PRISMA systematic review, intent detection, dialogue health monitoring, optional cross-model DA, Semantic Scholar API verification. | [view](academic-research-skills/deep-research.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/deep-research/SKILL.md) | 2026-05 |

### `meta` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`academic-pipeline`](academic-research-skills/academic-pipeline.md) | general |  | Pipeline orchestrator that chains deep-research → academic-paper → academic-paper-reviewer with quality gates between stages. | [view](academic-research-skills/academic-pipeline.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/academic-pipeline/SKILL.md) | 2026-05 |

### `review` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`academic-paper-reviewer`](academic-research-skills/academic-paper-reviewer.md) | general | `referee-simulation` | 7-agent multi-perspective peer review with 0–100 quality rubrics (EIC + 3 dynamic reviewers + Devil's Advocate), concession threshold protocol, attack intensity preservation, optional cross-model DA critique/calibration, R&R traceability matrix. | [view](academic-research-skills/academic-paper-reviewer.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/academic-paper-reviewer/SKILL.md) | 2026-05 |
