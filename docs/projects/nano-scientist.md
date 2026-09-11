<!-- DO NOT EDIT — auto-generated from projects/landscape/nano-scientist.yml by scripts/build_indexes.py -->

# nano-scientist

`external` · status: `dormant` · focus: `end-to-end` · discipline: `general` · started: 2024

**Project page:** <https://github.com/AI4Scientist/nano-scientist>

**Source:** [`projects/landscape/nano-scientist.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/nano-scientist.yml)

## Positioning

A budget-first autonomous report generator: `python main.py "topic" --budget 2.00` runs four self-terminating loops — literature, experimentation, writing with an internal peer-review pass, and compilation — and lands a LaTeX source, a deduplicated CrossRef-checked BibTeX file and a compiled PDF in `outputs/<uuid>/` alongside `cost_log.json`, `history.json` and `summary.json`. Internally it is 87 lazy-loaded SKILL.md files rather than a fixed agent graph, so it sits between the end-to-end pipelines (zeropaper, agent-laboratory) and the skill packs in the RISE catalog.

## Distinctive contribution

Cost is a first-class input rather than an afterthought: the dollar budget is a command-line argument, investigation depth adapts to the funds remaining, each loop exits when the estimated cost of further LLM calls crosses a threshold, and every run ships a cost log — no other catalogued system treats spend as a controllable parameter, and the four showcase reports were all produced at a $1 budget so the price/quality trade-off is inspectable. Its "zero-drop" citation handling is also unusually careful: entries that fail CrossRef lookup are recovered by title search or retained as `@misc` stubs so the bibliography never silently loses a reference.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Nine declared stages across four loops — ideation, paper discovery and review, experimentation or synthesis, section drafting, an internal peer-review pass with feedback handling, and pdflatex/bibtex compilation — though the four published showcases exercise the literature-and-writing path far more than the experimental one. |
| Autonomy level | 3 | A single command produces a compiled PDF with no approval points; loops self-terminate on quality gates or remaining budget rather than on human sign-off. |
| Architectural transparency | 2 | All 87 skills are plain SKILL.md files with YAML frontmatter under skills/, alongside src/, main.py and a CLAUDE.md, so the routing logic and prompts are readable — but there is no evaluation harness and no LICENSE clarifying reuse of any of it. |
| Inputs supported | 1 | One input form — a topic string, plus a budget parameter — with literature access through paper-discovery skills and CrossRef; no dataset input, no private-corpus connector. |
| Outputs / reproducibility | 2 | Each run persists report.tex, report.pdf, references.bib, figures/, data/, scripts/ and per-run cost/history/summary JSON under outputs/<uuid>/; but depth is budget-adaptive and no seed or manifest is emitted, so a run cannot be reproduced from its inputs. |
| Internal evaluation | 1 | Four $1 showcase reports with cost logs (small-LM bug fixing, a Lean 4 theorem-prover taxonomy, coding agents across 933k pull requests, on-policy distillation) — anecdotal demos; no benchmark, no paper, no external review. |
| Openness | 1 | Verified: the README carries an MIT badge but there is no LICENSE, LICENSE.md or COPYING file at the repository root and the GitHub API reports license null, so reuse terms are unconfirmed; a run also requires a paid OPENROUTER_API_KEY. |
| Maturity / traction | 1 | Research prototype: 127 stars, 20 forks, 120 commits, no releases, and nothing pushed since 2026-06-03. |
| Cross-family policy | 1 | All inference routes through OpenRouter and a separate REVIEWER_MODEL can be pointed at a different family from the writer, so cross-family review is configurable — but it is not the documented default. |
| Runtime assurance | 2 | Multiple in-pipeline gates: independent quality gates per loop, an optional distinct reviewer model, an internal peer-review pass whose feedback the writing loop must address, zero-drop CrossRef citation verification, and bounded pdflatex error correction (two attempts) — moderate rather than heavy, since none of these hard-fail the run. |
| Cross-platform portability | 2 | A single Python CLI, but OpenRouter plus a configurable OpenAI-compatible INFERENCE_BASE_URL puts many model providers behind one adapter, and the 87 markdown skills are portable in principle to other harnesses. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `literature-discovery` `literature-synthesis` `code-generation` `data-analysis` `paper-drafting` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `tool-use` `iterative-loop` `dag-orchestration`


**Inputs:** `research-topic` `dollar-budget`


**Outputs:** `paper-draft` `compiled-pdf` `bibtex` `figures` `analysis-scripts` `cost-log`


**Data sources:** `self-generated-experiments`


**Knowledge sources:** `crossref` `paper-discovery-skills`


## Limitations

- Licence unconfirmed — verified absent: the README shows an MIT badge, but the repo root holds only .env.example, .gitignore, CLAUDE.md, README.md, main.py and requirements.txt plus showcases/, skills/ and src/, with no LICENSE file, and the GitHub API reports license null. Treat as unlicensed until a LICENSE lands.
- Repo created_at is 2024-12-02 while every shipped artifact is 2026-vintage (87 SKILL.md files, OpenRouter, Claude-style skill frontmatter), so the repository was almost certainly repurposed; year_started is dated from GitHub metadata, and the effective project start looks like 2026.
- Nothing pushed since 2026-06-03 — dormant by the three-month rule.
- All four showcases are $1 runs on CS/ML topics, so both quality at real research depth and behaviour outside computer science are unevidenced despite the domain-agnostic framing.
- 'Peer-reviewed technical report' means the system reviewed its own draft — there is no external review, benchmark or reported evaluation of output quality.
- Requires a paid OpenRouter key; the repo is ~115 MB, largely showcase artifacts.

## Related projects in this catalog

- [`zeropaper`](zeropaper.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`luxas`](luxas.md)
