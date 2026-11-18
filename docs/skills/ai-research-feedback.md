<!-- DO NOT EDIT — auto-generated from skills/ai-research-feedback.yml by scripts/build_skills_index.py -->

# AI Research Feedback (Claes Bäckman)

license: `MIT` · 12 skills · last update: 2026-11-15

**Source:** <https://github.com/claesbackman/AI-research-feedback>

**Maintainers:** Claes Bäckman (claesbackman.com)

**Related project entry:** [`ai-research-feedback`](../projects/ai-research-feedback.md)

**Compatibility:** `claude-code`

> Twelve Claude Code skills for getting critical feedback on economics and finance research and for presenting it — the most-starred single-author econ skill pack in this catalog (566 stars on 2026-11-18). The review tier is deliberately graduated by cost, so a draft can be iterated cheaply and audited expensively: `review-paper` runs seven parallel agents against a named target journal, the last of which rates the contribution against six questions, and then a verification pass that drops wrong and marginal findings, `review-paper-light` runs two for contribution and overclaiming, and `review-paper-checks` runs three that hunt only mechanical errors and issue no editorial judgment at all. `explain-diff` builds an offline HTML explainer with a five-question quiz (the idea taken from Geoffrey Litt's "Understanding is the new bottleneck"). Four skills turn a finished paper into other formats: `paper-version` writes a policy brief or lay summary, `explorable-deck` and `explorable-beamer` build talks in the explorable-explanation style (Quarto reveal.js or LaTeX beamer), and `paper-website` builds a static digital edition from the LaTeX source. The three newest ship a template and helper scripts next to their SKILL.md; RISE copies only the SKILL.md, so install them from the source repository. `audit-analysis`, catalogued here until 2026-11, was removed upstream on 2026-11-15. Every review skill sets `disable-model-invocation: true`, so Claude never launches a multi-agent review on its own; `pdf-to-markdown` is the deliberate exception and may be auto-invoked when reading a PDF. A notable design detail: the review skills pass agents exactly the main .tex file plus its include-graph and explicitly exclude prior review reports, response letters, and old drafts — the fix for review-on-review contamination, which is the standard failure mode of running these tools repeatedly in one folder. The review skills and `paper-version` require the `general-purpose` subagent; the two deck skills use it only for optional review passes; `explain-diff`, `pdf-to-markdown` and `paper-website` run without subagents. Reports are written into a `reviews/` subfolder with date-versioned filenames.


**Source YAML:** [`skills/ai-research-feedback.yml`](https://github.com/bhanneke/RISE/blob/main/skills/ai-research-feedback.yml)

## Skills

### `audit` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/review-paper-checks`](ai-research-feedback/review-paper-checks.md) | economics | `revision-editing` | Three-agent check for what is wrong rather than what is debatable: misspellings and grammar, numbers in the text that disagree with the tables, terminology and sample drift, cross-references and citations that point to nothing, and claims the design does not license. Issues no contribution or publication judgment, and afterwards offers to apply only the unambiguous fixes to the .tex files. | [view](ai-research-feedback/review-paper-checks.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper-checks/SKILL.md) | 2026-11-13 |

### `drafting` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/paper-version`](ai-research-feedback/paper-version.md) | economics | `dissemination` | Turns a LaTeX paper into a policy brief, one-page, or five-page lay summary through four sequential agents — a reader that extracts claims and numbers verbatim, a writer, a reviewer that checks every number and causal claim in the draft against the extraction, and a page builder — then emits a standalone HTML page ready for GitHub Pages. Pauses after the review so the author can edit before the page is built. | [view](ai-research-feedback/paper-version.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/paper-version/SKILL.md) | 2026-11-13 |
| [`/paper-website`](ai-research-feedback/paper-website.md) | economics | `dissemination` | Turns a LaTeX paper into a static website edition built with pandoc and three Python scripts that the skill copies into the project, so the author can rebuild it after each revision. The site keeps the PDF's own section, figure, table and equation numbers and adds footnotes that open in place, linked citations, full-text search, a cite box and CSV download of every table; the author chooses whether it also carries figures redrawn from aggregate data or a results explorer. The template and scripts live next to the SKILL.md in the source repository. | [view](ai-research-feedback/paper-website.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/paper-website/SKILL.md) | 2026-11-15 |

### `infra` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/explain-diff`](ai-research-feedback/explain-diff.md) | economics | `code-generation` | Writes one self-contained offline HTML page explaining a code change well enough that someone who did not write it could defend it: what the code did before, what changed in prose with no code, the verified consequences for sample and coefficients, a walkthrough grouped by purpose, and a five-question quiz of which at least two must test empirical consequences. Re-reads the diff and surrounding code from scratch — ignoring any account already in the conversation — and saves the page outside the repository under a dated, ref-tagged filename. | [view](ai-research-feedback/explain-diff.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/explain-diff/SKILL.md) | 2026-08-02 |
| [`/pdf-to-markdown`](ai-research-feedback/pdf-to-markdown.md) | general | `literature-discovery` | Converts a PDF to markdown beside the original with page markers every twenty pages and the text trimmed at the references or appendix, so only the main text enters the context window. Uses `pdftotext` when poppler is installed — orders of magnitude faster and free of model context cost — and falls back to chunked reading otherwise. | [view](ai-research-feedback/pdf-to-markdown.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/pdf-to-markdown/SKILL.md) | 2026-11-13 |

### `replication` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/review-paper-code`](ai-research-feedback/review-paper-code.md) | economics | `replication` | Reviews an empirical project's LaTeX paper against its Stata, R, or Python code on three fronts: reproducibility (paths, seeds, outputs, dependencies, run order, documentation), code quality, and paper-to-code alignment of tables, variables, sample restrictions, methods, clustering, and fixed effects. Calibrated to treat gaps as items to verify rather than accusations. | [view](ai-research-feedback/review-paper-code.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper-code/SKILL.md) | 2026-11-13 |

### `review` (4)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/review-grant`](ai-research-feedback/review-grant.md) | general | `research-design` | Six-agent panel review of a grant proposal against a target funder (NSF, NIH, ERC, Horizon Europe) or general standards, judging clarity and compliance signals, internal consistency and deliverables, significance and innovation, research design and feasibility, and the budget, timeline, team, and management plan. Inspects budgets, biosketches, data-management plans, and letters of support alongside the narrative. | [view](ai-research-feedback/review-grant.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-grant/SKILL.md) | 2026-11-13 |
| [`/review-pap`](ai-research-feedback/review-pap.md) | economics | `research-design` | Six-agent review of a pre-analysis plan against a chosen trial registry (AEA, EGAP, OSF, ClinicalTrials, ISRCTN) or journal standard, covering pre-specification completeness, hypothesis and outcome coverage, identification and causal claims, the statistical analysis plan including power and multiple testing, data and implementation feasibility, and registry fit. Pulls in power calculations, survey instruments, randomization protocols, and mock tables when it finds them. | [view](ai-research-feedback/review-pap.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-pap/SKILL.md) | 2026-11-13 |
| [`/review-paper`](ai-research-feedback/review-paper.md) | economics | `referee-simulation` | Seven parallel agents produce a pre-submission referee report against a named target journal: spelling and style, internal consistency and cross-references, unsupported claims and identification integrity, mathematics and notation, tables and figures, a referee assessment of identification, analyses, positioning and fit, and a contribution assessment that answers six questions taken from Jason Fletcher with a Strong, Adequate or Weak verdict relative to the journal. A verification pass then drops wrong and marginal findings. The skill does not judge novelty against the prior literature, because the agents cannot verify what other papers have shown. | [view](ai-research-feedback/review-paper.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper/SKILL.md) | 2026-11-15 |
| [`/review-paper-light`](ai-research-feedback/review-paper-light.md) | economics | `referee-simulation` | Fast two-agent pre-submission check on contribution, identification, and causal overclaiming — one agent plays a demanding associate editor who rates the contribution and names identification threats, the other hunts causal overclaiming, mechanisms asserted as facts, and missing caveats. Runs in about a minute, for iteration between full reviews. | [view](ai-research-feedback/review-paper-light.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper-light/SKILL.md) | 2026-11-13 |

### `slides` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/explorable-beamer`](ai-research-feedback/explorable-beamer.md) | economics | `dissemination` | Builds the same explorable-style talk as explorable-deck in LaTeX beamer: one idea per frame, TikZ and pgfplots stages the presenter steps through, a notes build and a handout build, and a screenshot-and-log check of every page. All numbers used in charts and sentences sit in one data file. The template and build scripts ship next to the SKILL.md in the source repository. | [view](ai-research-feedback/explorable-beamer.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/explorable-beamer/SKILL.md) | 2026-11-15 |
| [`/explorable-deck`](ai-research-feedback/explorable-deck.md) | economics | `dissemination` | Builds a Quarto reveal.js talk in the explorable-explanation style: one idea per slide under an assertion title, a concrete running example, run-time SVG figures the presenter steps through live, the source's own figures recoloured into the deck palette, speaker notes on every slide and an appendix for side questions. All chart numbers sit in one data file. The deck template ships next to the SKILL.md in the source repository. | [view](ai-research-feedback/explorable-deck.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/explorable-deck/SKILL.md) | 2026-11-15 |
