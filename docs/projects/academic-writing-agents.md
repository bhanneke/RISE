<!-- DO NOT EDIT — auto-generated from projects/landscape/academic-writing-agents.yml by scripts/build_indexes.py -->

# academic-writing-agents

`external` · status: `dormant` · focus: `revision` · discipline: `general` · started: 2026

**Project page:** <https://github.com/andrehuang/academic-writing-agents>

**Source:** [`projects/landscape/academic-writing-agents.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/academic-writing-agents.yml)

## Positioning

A Claude Code plugin that puts a manuscript-audit orchestrator over twelve specialist agents: five read-only reviewers (consistency-checker, logic-reviewer, technical-reviewer, writing-reviewer, latex-layout-auditor), a bibliography-auditor, two web-enabled research agents (research-analyst for related work, novelty and positioning; brainstormer for alternative framings), a paper-crawler over the DBLP and OpenAlex APIs, and three agents that modify the source (prose-polisher, section-drafter, latex-figure-specialist). Invoked as `/academic <task>` or auto-triggered on `.tex` files, it fans the independent reviewers out in parallel, synthesises one report prioritised Critical / Important / Minor, then runs a sequential fix-and-verify pass. Sits in the drafting/revision band of RISE next to research-paper-writing-skills and Academic Research Skills, but is narrower and manuscript-first.

## Distinctive contribution

Review persistence. Findings are written to `.review/YYYY-MM-DD-<scope>.md`; a later pass compares file timestamps and re-reviews only sections that changed, and the action agents read the stored findings so each edit is traceable to the reviewer concern that motivated it — incremental review state that the larger skill catalogs in this band do not carry. Behaviour is pinned to a codified 30 Principles document (18.8 KB, six categories from structure and narrative through process and meta), and agent files declare their own tool set and model in frontmatter — the sampled consistency-checker declares `tools: Read, Glob, Grep` and `model: opus`, so the read-only reviewers structurally cannot edit the manuscript they are auditing.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five stages — literature collection (paper-crawler), related-work/gap synthesis (research-analyst), section drafting, prose and layout revision, and pre-submission review — with no research design, data analysis, estimation or replication anywhere in scope. |
| Autonomy level | 1 | Copilot: the orchestrator names the agents it will deploy and 'proceed[s] with deployment unless the user objects', findings are surfaced as a prioritised report and proposed fixes are presented for approval before the action agents write to the manuscript. |
| Architectural transparency | 3 | Everything the system consists of is inspectable in-repo despite not rendering on the repo landing page: all 12 agent definitions under agents/ (1.6–4.4 KB each, with YAML frontmatter declaring tools and model), the 14.8 KB orchestrator skills/academic/SKILL.md, the 18.8 KB principles/academic-writing.md, and marketplace.json — under MIT. No evaluation harness exists to publish. |
| Inputs supported | 1 | One input form (a LaTeX manuscript / project directory) plus literature access through DBLP, OpenAlex and WebSearch/WebFetch; no dataset, database or private-corpus connector. |
| Outputs / reproducibility | 2 | Persists dated review reports under .review/ and writes prose, LaTeX sections and TikZ figures directly into the source tree, but versioning is whatever the user's git provides and no run is reproducible from a declared input set. |
| Internal evaluation | 0 | No benchmark, no paper, no example outputs or transcripts in the repo; the design is grounded in Michael Black's 'Writing a Good Scientific Paper' and the author's thesis-supervision experience. |
| Openness | 2 | MIT license, whole plugin is markdown, one-command install from the Claude plugin marketplace or the GitHub URL, but it requires a paid Claude Code subscription and the agents pin model: opus — not free-tier reproducible. |
| Maturity / traction | 1 | 190 stars / 19 forks and marketplace-installable with a v2.1 feature set, but 5 commits total, 93 KB, one author, and no push since 2026-05-11 — a research prototype in single-team use. |
| Cross-family policy | 0 | Claude Code plugin with model: opus pinned in agent frontmatter; no reviewer from a second model family is supported or suggested. |
| Runtime assurance | 2 | Several in-pipeline integrity mechanisms: bibliography-auditor checks entry completeness and arXiv updates against external records, consistency-checker resolves cross-references and detects orphan floats, latex-layout-auditor inspects the compiled PDF, findings must cite file:line, and a verification stage re-runs the checkers after edits — but the checks are advisory, not blocking. |
| Cross-platform portability | 0 | Single platform: .claude-plugin/ marketplace layout, /academic slash command, Claude Code agent-spawning semantics and an opus model pin; no other IDE, runtime or provider path is documented. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `human-in-loop` `tool-use` `persistent-memory` `iterative-loop`


**Inputs:** `latex-manuscript` `project-directory`


**Outputs:** `review-reports` `revised-prose` `latex-sections` `tikz-figures`


**Data sources:** `dblp-api` `openalex-api`


**Knowledge sources:** `thirty-principles-document`


## Limitations

- Dormant at scoring date: 5 commits total, last push 2026-05-11, and the repo description still advertises '10 specialist agents' while 12 agent definition files are present.
- No evaluation of any kind — no benchmark, no paper, no worked examples in the repo — so the 30 Principles are asserted pedagogy, not measured effect.
- Approval is opt-out rather than opt-in: the orchestrator proceeds unless the user objects, and the action agents apply fixes in place to the LaTeX source, so it is only safe under version control.
- Reviewer output is LLM judgement, not verification: only the bibliography-auditor (external records) and latex-layout-auditor (compiled PDF) check anything outside the model, and no finding blocks a subsequent step.
- Locked to Claude Code — marketplace plugin layout, /academic command, model: opus in frontmatter — so nothing here ports to another runtime without a rewrite.
- Scope is LaTeX and ML-paper-shaped: no data acquisition, estimation or replication stage, and tasks without a matching specialist fall back to general-purpose agents.
- Agent files are substantive but small (1.6–4.4 KB each); the depth of each specialist is thin relative to the orchestrator (14.8 KB) and the principles document (18.8 KB) that carry most of the behaviour.

## Related projects in this catalog

- [`research-paper-writing-skills`](research-paper-writing-skills.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`clo-author`](clo-author.md)
- [`reviewer`](reviewer.md)
