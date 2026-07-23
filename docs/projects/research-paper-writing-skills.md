<!-- DO NOT EDIT — auto-generated from projects/landscape/research-paper-writing-skills.yml by scripts/build_indexes.py -->

# Research Paper Writing Skills

`external` · status: `active` · focus: `drafting` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/Master-cai/Research-Paper-Writing-Skills>

**Source:** [`projects/landscape/research-paper-writing-skills.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/research-paper-writing-skills.yml)

## Positioning

A single portable skill package (`research-paper-writing/`) for ML/CV/NLP paper writing: a SKILL.md core workflow plus eight section-specific reference guides (abstract, introduction, related work, method, experiments, conclusion, paper review, paragraph flow) and an example bank, curated and adapted from Prof. Peng Sida's (Zhejiang University) widely used open research-writing notes. Installs by directory copy into Codex, Claude Code, or Gemini CLI. Sits in the skills/knowledge-asset layer alongside Academic Research Skills, but is content-first: distilled human writing pedagogy packaged as agent-consumable markdown rather than an engineered agent pipeline.

## Distinctive contribution

Packages a respected researcher's writing methodology — reverse outlining, one-message-per-paragraph, claim-evidence alignment as a hard constraint, adversarial self-review from a reviewer mindset — into a runtime-portable skill with explicit provenance (MIT, with attribution to Peng's notes and repository). 5.4k stars in under four months is the clearest demonstration in the catalog that expert-curated writing knowledge, not orchestration machinery, is itself a distributable artifact.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three adjacent stages (drafting, revision, reviewer-style self-review); no literature, analysis, or dissemination coverage. |
| Autonomy level | 0 | Pure assist content: the host agent rewrites paragraph-by-paragraph under prescribed human iteration; no autonomous pipeline of its own. |
| Architectural transparency | 3 | The entire artifact is public markdown — SKILL.md workflow, all reference guides, example bank, and agent metadata; nothing is hidden. |
| Inputs supported | 1 | One input form (draft prose for any section) plus a bundled reference/example knowledge base; no live literature or data access. |
| Outputs / reproducibility | 1 | Revised prose persists only via the host runtime's file edits; the skill itself versions or packages nothing. |
| Internal evaluation | 0 | No evaluation of skill effectiveness; credibility rests on the provenance of the source notes. |
| Openness | 3 | MIT-licensed plain markdown; install is a documented directory copy that reproduces the full artifact on any machine. |
| Maturity / traction | 2 | 5,449 stars / 269 forks within ~4 months (created 2026-03-05) show broad adoption, but the repo is a 6-commit content drop with no releases, no issue activity, and a single curator; last push 2026-06-23. |
| Cross-family policy | 0 | Not applicable — passive model-agnostic content with no executor/reviewer configuration. |
| Runtime assurance | 1 | Claim-evidence alignment as a 'hard constraint' and a final adversarial review pass are mandated in the workflow, but purely at prompt level — nothing enforces or gates them. |
| Cross-platform portability | 3 | Deliberately skills-as-Markdown: three officially documented runtimes (Codex, Claude Code, Gemini CLI) and the plain SKILL.md format is consumable by any skills-capable agent runtime. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `single-llm`


**Inputs:** `paper-draft` `section-drafts`


**Outputs:** `revised-paper-sections` `self-review-reports`


**Knowledge sources:** `curated-writing-guides`


## Limitations

- Writing-block only: assumes finished research; no literature, data, or analysis support, and guidance is tuned to ML/CV/NLP conference conventions.
- Effectiveness is unevaluated — value depends entirely on how faithfully the host model follows the prescribed workflow; the mandated claim-evidence checks are unenforced prompt instructions.
- Essentially static since creation (6 commits, no releases, single curator); derivative curation of Peng Sida's notes, so upstream updates do not propagate automatically.

## Related projects in this catalog

- [`academic-research-skills`](academic-research-skills.md)
- [`auto-empirical-research-skills`](auto-empirical-research-skills.md)
- [`clo-author`](clo-author.md)
