<!-- DO NOT EDIT — auto-generated from skills/thinkingwithagents-skills.yml by scripts/build_skills_index.py -->

# Thinking with Agents econ skills (Emily Beam and Erkmen Aslim)

license: `CC-BY-4.0 (repo LICENSE, "Creative Commons Attribution 4.0 International, Copyright (c) 2026 Emily Beam")` · 9 skills · last update: 2026-04-26

**Source:** <https://github.com/thinkingwithagents/skills>

**Maintainers:** Emily Beam (eabeam on GitHub, University of Vermont), Erkmen Aslim (University of Vermont), co-lead of the Thinking with Agents project

**Compatibility:** `claude-code` `cursor` `agnostic`

> Nine skills for empirical economics from Thinking with Agents, the resource collection Emily Beam and Erkmen Aslim built around the UVM Economics AI Bootcamp (Spring 2026). The repo is a GitHub fork of eabeam/econ-skills, which holds the first three skills (econ-audit, data-dictionary, lit-review, 2026-04-20); the fork adds code-review, review-paper, pipeline-audit, find-data, research-brainstorm and academic-beamer-deck (2026-04-26). All commits are by Emily Beam, and the README still credits her alone and gives install commands for the parent repo. The skills are plain SKILL.md files and the README names Claude Code, Cursor and Cline. Four of them are adversarial checks of applied-micro work: econ-audit (specification, clustering and bad-control errors in Stata, R or Python), code-review (DIME, Gentzkow-Shapiro, AEA and IPA code standards), pipeline-audit (variable construction and sample restrictions against a pre-analysis plan) and review-paper (skeptical referee plus devil's advocate). The rest support ideation, data search, codebooks, multi-session literature reviews and Beamer decks. A provenance audit (md5 plus difflib word-sequence ratio, 2026-09-29) against every details copy RISE already holds, the named upstreams and the Auto-Empirical-Research-Skills bundle finds all nine first-party (best external match 0.243, review-paper against a Felpix Studios review skill, a shared genre and no shared text); there are no vendored copies. The details copies are verbatim and are redistributed under CC-BY-4.0 with attribution to Emily Beam, the copyright holder, and the Thinking with Agents project (Emily Beam and Erkmen Aslim).


**Source YAML:** [`skills/thinkingwithagents-skills.yml`](https://github.com/bhanneke/RISE/blob/main/skills/thinkingwithagents-skills.yml)

## Skills

### `audit` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/econ-audit`](thinkingwithagents-skills/econ-audit.md) | econometrics | `data-analysis` `referee-simulation` | Adversarial review of analysis code in Stata, R or Python that looks for errors which run cleanly but give wrong answers: misspecification, wrong clustering, bad controls and silent failures, together with an identification and design assessment and a specification table. | [view](thinkingwithagents-skills/econ-audit.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/econ-audit/SKILL.md) | 2026-04-20 |
| [`/pipeline-audit`](thinkingwithagents-skills/pipeline-audit.md) | economics | `data-analysis` `replication` | Adversarial audit of a data pipeline that checks variable construction, sample restrictions and analytical choices against the pre-analysis plan and grades findings as red, orange or yellow flags. | [view](thinkingwithagents-skills/pipeline-audit.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/pipeline-audit/SKILL.md) | 2026-04-26 |

### `data-handling` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/data-dictionary`](thinkingwithagents-skills/data-dictionary.md) | economics | `data-analysis` | Generates a codebook from a Stata .dta file in summary, full or analysis-ready mode: variable list, summary statistics, value labels, string variables and high-missingness flags. | [view](thinkingwithagents-skills/data-dictionary.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/data-dictionary/SKILL.md) | 2026-04-20 |
| [`/find-data`](thinkingwithagents-skills/find-data.md) | economics | `data-acquisition` `research-design` | Searches systematically across source categories for datasets that fit a research question, verifies them, and sorts them into public, needs-processing and restricted-access tiers, with a summary table, suggested combinations and help with download, scraping or access applications. | [view](thinkingwithagents-skills/find-data.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/find-data/SKILL.md) | 2026-04-26 |

### `ideation` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/research-brainstorm`](thinkingwithagents-skills/research-brainstorm.md) | economics | `rq-formulation` `literature-discovery` `research-design` | Senior-colleague brainstorming dialogue that sharpens or generates a research question, runs a parallel literature scan, attacks the question, offers alternative framings, checks feasibility through find-data and writes a research brief. | [view](thinkingwithagents-skills/research-brainstorm.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/research-brainstorm/SKILL.md) | 2026-04-26 |

### `literature` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/lit-review`](thinkingwithagents-skills/lit-review.md) | economics | `literature-discovery` `literature-synthesis` | Multi-session literature review workflow that scaffolds a review folder, tracks papers across sessions, shows a status dashboard, produces Beamer, Quarto or Markdown summaries, and runs referee passes to catch missing canonical papers. | [view](thinkingwithagents-skills/lit-review.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/lit-review/SKILL.md) | 2026-04-20 |

### `review` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/code-review`](thinkingwithagents-skills/code-review.md) | economics | `code-generation` `replication` | Structured review of Stata, R or Python research code against DIME, Gentzkow-Shapiro, AEA and IPA standards, reporting silent failures, reproducibility risks and style problems by severity, with a replication-package checklist mode. | [view](thinkingwithagents-skills/code-review.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/code-review/SKILL.md) | 2026-04-26 |
| [`/review-paper`](thinkingwithagents-skills/review-paper.md) | economics | `referee-simulation` | Simulates a skeptical referee on a paper, checking identification, statistical claims, robustness and presentation, and returns a referee report, a devil's-advocate report and an editorial synthesis. | [view](thinkingwithagents-skills/review-paper.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/review-paper/SKILL.md) | 2026-04-26 |

### `slides` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/academic-beamer-deck`](thinkingwithagents-skills/academic-beamer-deck.md) | economics | `dissemination` | Builds or redesigns academic Beamer decks from .tex sources, figures and talk context, with a narrative structure, a design system, strict layout and TikZ rules, and a compile check, and returns a compile-ready deck with an organised figures folder. | [view](thinkingwithagents-skills/academic-beamer-deck.md) | [origin](https://github.com/thinkingwithagents/skills/blob/main/academic-beamer-deck/SKILL.md) | 2026-04-26 |
