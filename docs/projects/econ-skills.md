<!-- DO NOT EDIT — auto-generated from projects/landscape/econ-skills.yml by scripts/build_indexes.py -->

# econ-skills (zbsaygin)

`external` · status: `active` · focus: `analysis` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/zbsaygin/econ-skills>

**Licence:** `MIT`

**Source:** [`projects/landscape/econ-skills.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/econ-skills.yml)

## Positioning

A personal Claude Code skill pack for academic economics research workflows: reading papers by citekey, multi-agent literature review with novelty assessment, a Delphi-consensus correctness audit of math and econometrics, Econometrica-style notation cleanup, and LaTeX document/Beamer-slide/figure production. Spans literature discovery through paper-drafting and presentation output.

## Distinctive contribution

notation-clean is a narrow, unusual skill not found in any other cataloged pack: it audits and simplifies mathematical notation against an explicit "Econometrica publication standard" (Greek-for-parameters vs. Latin-for-variables, a 5-use threshold for introducing new symbols, reserved-symbol collision checks), triggered specifically on notation-focused requests rather than general correctness review. audit-econ pairs this with a Delphi-consensus multi-agent audit of derivations, econometrics, code, and data.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five stages (literature discovery/synthesis, notation/math revision, drafting, presentation output) but no data-analysis, research-design, or referee-simulation skill. |
| Autonomy level | 1 | audit-econ presents severity-sorted findings for the user to triage and 'manages fix workflow' rather than auto-committing fixes; lit-review stress-tests via an adversarial referee but surfaces the gap for the user. |
| Architectural transparency | 3 | All seven skills are public Markdown with explicit sub-agent and consensus-mechanism descriptions; no closed components. |
| Inputs supported | 2 | Multiple input forms (citekey, pasted PDF, LaTeX document, .bib file) plus a literature-access pathway via lit-review's multi-agent search; no private data-source access. |
| Outputs / reproducibility | 2 | Persists compiled LaTeX documents, Beamer decks, and standalone-PDF figures/tables, but requires per-user placeholder setup (paths, Zotero/Better BibTeX) and has no cross-skill artifact manifest. |
| Internal evaluation | 0 | No test fixtures, benchmark, or reported evaluation for any of the seven skills at scoring date. |
| Openness | 2 | MIT license; functional use requires replacing ~10 user-specific placeholders and a Zotero + Better BibTeX bibliography pipeline, so not zero-setup. |
| Maturity / traction | 1 | 7 stars, 1 fork, single commit on record at scoring date — a young, single-maintainer personal tool. |
| Cross-family policy | 0 | No cross-model-family mechanism described; audit-econ's 'consensus' is among same-family Opus sub-agents, not across model families. |
| Runtime assurance | 2 | audit-econ dispatches independent sub-agents to a Delphi consensus before reporting findings; lit-review stress-tests its own novelty claim with an adversarial referee pass until convergence. |
| Cross-platform portability | 0 | Claude Code only; no stated support for other agent runtimes. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `revision-editing` `paper-drafting` `dissemination`


**Architectural features:** `multi-agent` `debate-consensus` `tool-use`


**Inputs:** `paper-pdf` `citekey` `latex-document` `bibtex-file`


**Outputs:** `paper-summary` `literature-review` `audit-report` `latex-document` `beamer-slides` `figures`


**Knowledge sources:** `zotero-bibtex-library`


## Limitations

- Very young (1 commit, 7 stars); unproven beyond the maintainer's own use.
- Heavy placeholder setup required (project paths, bibliography path, Zotero + Better BibTeX workflow) before any skill runs correctly.
- No reported evaluation or test fixtures for any skill.
- No license file beyond the README's one-line MIT statement.

## Related projects in this catalog

- [`academic-research-skills`](academic-research-skills.md)
- [`econ-paper-review-skill`](econ-paper-review-skill.md)
- [`econtools`](econtools.md)
- [`econ-agent-skills`](econ-agent-skills.md)
