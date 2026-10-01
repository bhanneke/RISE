<!-- DO NOT EDIT — auto-generated from projects/landscape/econ-writing-skill.yml by scripts/build_indexes.py -->

# Econ Writing Skill

`external` · status: `active` · focus: `drafting` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/hanlulong/econ-writing-skill>

**Licence:** `MIT`

**Source:** [`projects/landscape/econ-writing-skill.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/econ-writing-skill.yml)

## Positioning

A portable agent skill (`skills/econ-write/`) that packages economics paper-writing craft — section formulas, identification-strategy-aware phrasing, LaTeX conventions, and a pre-submission checklist — distilled from 50+ guides by named economists (Cochrane, McCloskey, Shapiro, Head, Bellemare, Goldin, Kremer). Sits in the RISE drafting/revision layer alongside `research-paper-writing-skills` (the CS/ML analogue) and `academic-writing-agents`, but is economics-discipline-specific and content-first: curated human writing pedagogy packaged as agent-consumable markdown rather than an engineered pipeline.

## Distinctive contribution

The only writing-skill pack in the catalog tuned specifically to empirical-economics conventions: section formulas keyed to 13+ identification strategies (RCT, DiD, IV, RDD, ...), dedicated templates for job-market papers, dissertations, and grant proposals, and a quantified pre-submission gate (24-item checklist, 100-point scoring rubric) rather than generic "write more clearly" guidance.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Four adjacent stages — drafting, revision, a referee-style self-review checklist, and dissemination (AEA replication-package/LaTeX submission conventions) — but no literature, data, or analysis coverage of its own. |
| Autonomy level | 0 | Pure assist content: the host agent rewrites sections under the skill's formulas with the human driving every paragraph; no autonomous pipeline. |
| Architectural transparency | 3 | Fully public markdown/scripts: SKILL.md, sources/ bibliography, identification-strategies.md, latex-tips.md, review-checklist.md, examples/, evals/ and install scripts under .claude/.codex-plugin/.agents/ — nothing hidden, though there is no benchmark harness beyond a single evals/test-cases.md file. |
| Inputs supported | 1 | One input form (draft prose for any section or document type) plus a bundled 50+-guide knowledge base; no live literature search or data access. |
| Outputs / reproducibility | 1 | Revised prose and checklist scores persist only via the host runtime's file edits; the skill itself versions or packages nothing. |
| Internal evaluation | 1 | An evals/test-cases.md file exists, but no published scoring methodology, results, or comparison against an external writing-quality standard was found. |
| Openness | 3 | MIT-licensed plain markdown plus install scripts; reproducing the full artifact is a clone plus directory copy, with no paid dependency beyond the host agent itself. |
| Maturity / traction | 2 | 632 stars, 104 forks, 32 commits, with platform integrations for Claude Code and OpenAI Codex shipped — real external pickup for a sub-5-month-old single-maintainer project, though release cadence beyond the initial commits is unconfirmed. |
| Cross-family policy | 0 | Not applicable — passive model-agnostic markdown content with no executor/reviewer configuration. |
| Runtime assurance | 1 | The 24-item/100-point review-checklist is a mandated self-audit step in the workflow, but it is a prompt-level instruction with nothing enforcing or gating on it. |
| Cross-platform portability | 1 | Ships integrations for Claude Code and OpenAI Codex (2 documented runtimes); no Gemini CLI or broader skills-standard support confirmed, short of the 3+ band. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `paper-drafting` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `single-llm`


**Inputs:** `paper-draft` `section-drafts`


**Outputs:** `revised-paper-sections` `self-review-reports`


**Knowledge sources:** `curated-writing-guides`


## Limitations

- Writing-block only: assumes the analysis is already done — no literature discovery, data access, or identification-strategy execution, only guidance about how to write them up.
- Effectiveness is unevaluated: an evals/test-cases.md file exists but no methodology or results are published against an external writing-quality benchmark.
- Single-maintainer, young project (created 2026, 32 commits); the economics conventions reflect one curator's reading of the cited authorities, not a community consensus process.
- No literature or data access; 'modern standards' content (pre-registration, AEA replication-package requirements) is descriptive guidance, not a verified or enforced check.

## Related projects in this catalog

- [`research-paper-writing-skills`](research-paper-writing-skills.md)
- [`econ-agent-skills`](econ-agent-skills.md)
- [`openecon-data`](openecon-data.md)
- [`academic-writing-agents`](academic-writing-agents.md)
- [`clo-author`](clo-author.md)
