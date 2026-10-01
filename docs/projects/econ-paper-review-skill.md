<!-- DO NOT EDIT — auto-generated from projects/landscape/econ-paper-review-skill.yml by scripts/build_indexes.py -->

# Econ Paper Review Skill (econ-review)

`external` · status: `active` · focus: `review` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/hanlulong/econ-paper-review-skill>

**Licence:** `PolyForm Noncommercial 1.0.0 (source-available; free for academic/nonprofit use, commercial use requires separate terms)`

**Source:** [`projects/landscape/econ-paper-review-skill.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/econ-paper-review-skill.yml)

## Positioning

A referee-simulation Claude Code/Codex skill for economics (and adjacent social-science) manuscripts: it reads a paper, reconstructs its argument and evidence chain, checks quotations, calculations and citations against the source and against live literature, and produces a typeset referee report plus a prioritized, agent-ready revision plan. It is one of three sibling tools from the same author (alongside the already-catalogued openecon-data and stata-mcp) and is named as the self-refereeing component inside the author's own envisioned econ-auto-research pipeline (not yet released — see watch-list).

## Distinctive contribution

Verification-first design: every comment either quotes the manuscript directly or names the specific checked comparison or calculation it rests on, and claims of novelty or missing citations trigger a live literature search before being included, rather than being asserted from the model's own training knowledge. This distinguishes it from the catalog's more generic, model-ensemble referee tools (ai-peer-review-skill, Reviewer) by making per-comment evidentiary grounding the core trust mechanism, and by being deliberately economics/social-science-specific (identification strategy, proofs, reproducibility standards) rather than domain-agnostic.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Covers referee-simulation plus a structured revision-editing handoff (the revision plan); no literature-discovery, data, or drafting stages of its own. |
| Autonomy level | 1 | Copilot: a full review runs unattended for 30+ minutes, but the author must read the report and decide what to implement before any revision proceeds. |
| Architectural transparency | 2 | Source-available (PolyForm Noncommercial) with the review methodology (reconstruct -> verify -> report) documented in the README; the verification engine's internals are not fully walked through as prompts. |
| Inputs supported | 1 | A single input form (the manuscript) plus live literature-verification access; no structured data or multi-format research input. |
| Outputs / reproducibility | 1 | Persists a referee report and revision plan (prose/structured text); output can vary run to run and is not itself a versioned analysis artifact. |
| Internal evaluation | 1 | Demonstrated via one bundled sample review (25 comments) on a demo manuscript with intentionally inserted errors; no external benchmark or human-referee comparison reported. |
| Openness | 1 | Source-available under PolyForm Noncommercial 1.0.0 — free for academic/nonprofit use but not an OSI-permissive license; commercial use requires a separate agreement. |
| Maturity / traction | 1 | 25 stars, 5 forks, 36 commits; young (first public ~2026), single-author. |
| Cross-family policy | 0 | Single-agent by design (one Claude Code or Codex session); no cross-model-family review step. |
| Runtime assurance | 2 | Built-in verification passes (quotation/calculation checks, live literature verification for novelty/citation claims) run before comments are finalized, described as happening 'late in the run' specifically to keep comments trustworthy. |
| Cross-platform portability | 1 | Supports two agent runtimes (Claude Code and Codex) via a standalone-skill or plugin install. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation` `revision-editing`


**Architectural features:** `tool-use` `human-in-loop`


**Inputs:** `manuscript-pdf-latex-markdown`


**Outputs:** `referee-report-pdf` `markdown-reports` `prioritized-revision-plan`


**Knowledge sources:** `live web/literature verification (sources not fully documented)`


## Limitations

- PolyForm Noncommercial license restricts commercial use — source-available, not open-source by the OSI definition.
- A full review can take 30+ minutes and depends on live literature verification whose source coverage is not fully documented.
- Young (25 stars); no independent evaluation yet of report quality or calibration against human referees.

## Related projects in this catalog

- [`ai-peer-review-skill`](ai-peer-review-skill.md)
- [`reviewer`](reviewer.md)
- [`clo-author`](clo-author.md)
- [`openecon-data`](openecon-data.md)
