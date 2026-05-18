<!-- DO NOT EDIT — auto-generated from projects/landscape/clo-author.yml by scripts/build_indexes.py -->

# Clo-Author

`external` · status: `active` · focus: `end-to-end` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/hugosantanna/clo-author>

**Source:** [`projects/landscape/clo-author.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/clo-author.yml)

## Positioning

A Claude Code scaffold for empirical economics research, spanning literature review through journal submission. Eighteen agents organized as worker-critic pairs (e.g., Strategist + strategist- critic, Coder + coder-critic) with thirteen named pipeline commands from `/discover` and `/strategize` through `/write`, `/review`, `/revise`, `/talk`, and `/submit`. Targets the full inputs → knowledge production → outputs arc of the RISE diagram with a domain-specific focus on applied economics.

## Distinctive contribution

Worker-critic pair architecture as a first-class design principle: every creator agent has a paired critic that cannot edit files, with 3-round escalation when they disagree. Built-in peer-review simulation with intellectual-disposition reviewers (Structuralist, Credibility, Measurement, Policy, Theory, Skeptic) weighted by journal culture and FATAL / ADDRESSABLE / TASTE classification of comments. Direct sibling to [`e2er`](e2er.md) but distributed as a forkable Claude Code template rather than a Docker stack.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Thirteen stages including dissemination (`/submit`) — broadest coverage in catalog after E2ER. |
| Autonomy level | 2 | Supervised: researcher approves plans before execution; worker-critic disagreements escalate to human after 3 rounds. |
| Architectural transparency | 3 | Skill, agent, and command definitions are plain markdown in `.claude/`; full guide at hugosantanna.github.io/clo-author/. |
| Inputs supported | 2 | Topic / question / referee-report inputs; user provides data; multi-language analysis (R, Python, Julia). |
| Outputs / reproducibility | 2 | Generates replication packages with `/submit`; LaTeX paper is single source of truth; quality gate (>=80/100) before ship. |
| Internal evaluation | 2 | Built-in peer-review simulation with weighted reviewer dispositions; no published external benchmark yet. |
| Openness | 1 | Source is public on GitHub but no declared open-source license — reuse rights are uncertain. |
| Maturity / traction | 1 | Created 2026-02; 193 stars; very active development through May 2026; single-author project at this date. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `hypothesis-generation` `literature-discovery` `literature-synthesis` `research-design` `data-acquisition` `data-analysis` `formal-modeling` `code-generation` `paper-drafting` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `multi-agent` `debate-consensus` `human-in-loop` `tool-use` `persistent-memory` `artifact-versioning`


**Inputs:** `research-topic` `research-question` `referee-report`


**Outputs:** `paper-latex` `code` `slides` `replication-package` `referee-reports`


**Data sources:** `user-provided`


**Knowledge sources:** `literature`


## Limitations

- No declared open-source license; reuse rights uncertain.
- Economics-focused by default; portability to other fields requires customizing domain-profile + journal profiles.
- Depends on Claude Code; not a fully local solution.
- Quality gates and review simulation are internal; no third-party validation reported.

## Related projects in this catalog

- [`e2er`](e2er.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`reviewer`](reviewer.md)
- [`social-science-replicability`](social-science-replicability.md)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- `cunningham2025claudecode` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `eberhardt2025claudecode` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
