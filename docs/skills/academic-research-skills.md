<!-- DO NOT EDIT — auto-generated from skills/academic-research-skills.yml by scripts/build_skills_index.py -->

# Academic Research Skills (ARS)

license: `CC BY-NC 4.0` · 5 skills · last update: 2026-11-24

**Source:** <https://github.com/Imbad0202/academic-research-skills>

**Maintainers:** Edward Cheng-I Wu

**Related project entry:** [`academic-research-skills`](../projects/academic-research-skills.md)

**Compatibility:** `claude-code` `codex` `vscode` `jetbrains`

> Distributed as a Claude Code plugin. Five top-level skills, each backed by multiple sub-agents (12 for academic-paper, a role-separated 5-seat panel for academic-paper-reviewer, 13 for deep-research). Notable for claim-faithfulness audit pass (ARS_CLAIM_AUDIT) and cross-model verification. Refresh 2026-11-24 (upstream pushed 2026-11-24): re-copied the four existing skills, rewrote their descriptions to match the new SKILL.md texts (new rebuttal-audit mode, an eighth deep-research mode, a 5-seat reviewer panel) and added sr-screener.

**Source YAML:** [`skills/academic-research-skills.yml`](https://github.com/bhanneke/RISE/blob/main/skills/academic-research-skills.yml)

## Skills

### `drafting` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`academic-paper`](academic-research-skills/academic-paper.md) | general | `paper-drafting` `revision-editing` | 12-agent paper writing pipeline with 11 modes (full, plan, outline, revision, revision coaching, abstract, literature review, format conversion, citation check, disclosure, rebuttal audit), style calibration and a writing-quality check. | [view](academic-research-skills/academic-paper.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/academic-paper/SKILL.md) | 2026-08-15 |

### `literature` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`deep-research`](academic-research-skills/deep-research.md) | general | `literature-discovery` `literature-synthesis` | 13-agent research team with 8 modes (full research, quick brief, paper review, literature review, fact-check, three-way literature scan, Socratic dialogue, systematic review with optional meta-analysis). | [view](academic-research-skills/deep-research.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/deep-research/SKILL.md) | 2026-08-15 |
| [`/sr-screener`](academic-research-skills/sr-screener.md) | general | `literature-discovery` `literature-synthesis` | Protocol-driven screening for systematic, scoping and rapid reviews: confirms eligibility rules from a protocol, screens titles/abstracts and full texts with two blinded AI reviewers plus an adjudicator, runs QC checks and PRISMA counts, and hands the corpus to academic-paper. | [view](academic-research-skills/sr-screener.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/sr-screener/SKILL.md) | — |

### `meta` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`academic-pipeline`](academic-research-skills/academic-pipeline.md) | general |  | Orchestrates the 10-stage pipeline from research through writing, integrity checks, two-stage review and revision to finalisation, chaining deep-research, academic-paper and academic-paper-reviewer. | [view](academic-research-skills/academic-pipeline.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/academic-pipeline/SKILL.md) | 2026-11-19 |

### `review` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`academic-paper-reviewer`](academic-research-skills/academic-paper-reviewer.md) | general | `referee-simulation` | Multi-perspective paper review with a role-separated 5-seat panel (journal-fit reviewer, three peer-review roles, devil's advocate); modes for full review, re-review, quick assessment, methodology focus, Socratic guidance and calibration. | [view](academic-research-skills/academic-paper-reviewer.md) | [origin](https://github.com/Imbad0202/academic-research-skills/blob/main/academic-paper-reviewer/SKILL.md) | 2026-08-15 |
