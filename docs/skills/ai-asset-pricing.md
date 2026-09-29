<!-- DO NOT EDIT — auto-generated from skills/ai-asset-pricing.yml by scripts/build_skills_index.py -->

# ai-asset-pricing (Alex Dickerson)

license: `MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")` · 37 skills · last update: 2026-04-19

**Source:** <https://github.com/Alexander-M-Dickerson/ai-asset-pricing>

**Maintainers:** Alex Dickerson (Alexander-M-Dickerson on GitHub)

**Compatibility:** `claude-code` `codex` `gemini-cli`

> An empirical asset pricing research repo built around WRDS data, the author's PyBondLab corporate-bond portfolio package and a LaTeX paper workflow, with shared entry points for Claude Code (CLAUDE.md), Codex (AGENTS.md) and Gemini CLI (GEMINI.md). Besides 38 skills it ships 11 agents (WRDS query experts for CRSP, Compustat, OptionMetrics, TAQ, JKP global factors and the Dickerson bond data, a PyBondLab orchestrator and a paper reader), 12 rule files, hooks, a LaTeX paper boilerplate and a Python bootstrap engine. The skills cover five areas: WRDS and bond data access, factor and panel construction rules against look-ahead bias, PyBondLab runs and reports, paper writing and auditing section by section (write, edit, audit, captions, maths, consistency, citations, style, submission to JF, RFS or JFE, referee replies), and repo maintenance (onboarding, context sync, skill, agent and rule authoring). A provenance audit (md5 plus difflib word-sequence ratio, 2026-09-29) against every details copy RISE already holds, the named upstreams (K-Dense, anthropics, meleantonio, hanlulong, EconAgentSkills), the Auto-Empirical-Research-Skills bundle, and the full git histories of the two projects the README acknowledges finds 34 first-party skills, 3 adapted skills and 1 vendored copy. The vendored copy, `wrds-ssh`, is Piotr Orlowski's claude-wrds-public skill (0.957; only an Examples block and a note preferring local psql were added) and is not catalogued. The adapted skills are catalogued with their origin named in the entry: `wrds-schema` (0.857, Orlowski's text kept whole and extended with JKP and Dickerson bond schemas), `wrds-psql` (0.470, also from Orlowski) and `split-pdf` (0.474, from Scott Cunningham's MixtapeTools, reworked for adaptive chunking and finance extraction notes). The README acknowledges both sources in general terms but the skill files do not credit them, and claude-wrds-public carries no licence file, so the MIT grant of this repo cannot extend to the Orlowski-derived text. RISE therefore links to those three adapted skills rather than reproducing them, the same treatment it gives their unlicensed sources; the other 34 are reproduced under MIT. Several skills assume tools a user must supply: `idea`, `research` and `verify-citations` search through a Perplexity MCP server, and the WRDS skills need the user's own WRDS account. The repo has been unchanged since 2026-04-19.


**Source YAML:** [`skills/ai-asset-pricing.yml`](https://github.com/bhanneke/RISE/blob/main/skills/ai-asset-pricing.yml)

## Skills

### `analysis` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/factor-construction`](ai-asset-pricing/factor-construction.md) | finance | `data-analysis` `research-design` | Rules against look-ahead bias when building cross-sectional factors: signal timing, lead-return alignment, monthly and annual (Fama-French style) rebalancing, breakpoint choices to ask the user about, and post-construction diagnostics. | [view](ai-asset-pricing/factor-construction.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/factor-construction/SKILL.md) | 2026-03-11 |
| [`/pybondlab-report`](ai-asset-pricing/pybondlab-report.md) | finance | `data-analysis` | Writes a structured results report after each PyBondLab portfolio-formation run, using a fixed naming convention for strategies. | [view](ai-asset-pricing/pybondlab-report.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/pybondlab-report/SKILL.md) | 2026-03-11 |
| [`/run`](ai-asset-pricing/run.md) | finance | `data-analysis` `code-generation` | Shortcut that runs single or batch PyBondLab portfolio sorts on the Dickerson bond data straight from Bash, bypassing the orchestrator agent, with templates for single sorts and within-firm sorts. | [view](ai-asset-pricing/run.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/run/SKILL.md) | 2026-03-24 |

### `audit` (6)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/audit-captions`](ai-asset-pricing/audit-captions.md) | finance | `revision-editing` | Checks every table and figure caption in a paper for consistent language, notation and formatting and reports findings by severity. | [view](ai-asset-pricing/audit-captions.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/audit-captions/SKILL.md) | 2026-03-12 |
| [`/audit-math`](ai-asset-pricing/audit-math.md) | finance | `formal-modeling` `referee-simulation` | Adversarial pass over the proofs, derivations and formal environments of a paper, reporting errors and gaps by severity. | [view](ai-asset-pricing/audit-math.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/audit-math/SKILL.md) | 2026-03-12 |
| [`/audit-section`](ai-asset-pricing/audit-section.md) | finance | `revision-editing` | Deep audit of one section of a paper for style, factual accuracy, citations and logical flow. | [view](ai-asset-pricing/audit-section.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/audit-section/SKILL.md) | 2026-03-12 |
| [`/check-consistency`](ai-asset-pricing/check-consistency.md) | finance | `revision-editing` | Fast scan across sections for inconsistent numbers, terminology and cross-references. | [view](ai-asset-pricing/check-consistency.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/check-consistency/SKILL.md) | 2026-03-12 |
| [`/full-paper-audit`](ai-asset-pricing/full-paper-audit.md) | finance | `referee-simulation` `revision-editing` | Runs the section audits across the whole paper, checking cross-section consistency, every citation and all style issues. | [view](ai-asset-pricing/full-paper-audit.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/full-paper-audit/SKILL.md) | 2026-03-12 |
| [`/verify-citations`](ai-asset-pricing/verify-citations.md) | finance | `literature-discovery` `revision-editing` | Checks that every citation key in the LaTeX files exists in the .bib file and verifies the references through Perplexity. | [view](ai-asset-pricing/verify-citations.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/verify-citations/SKILL.md) | 2026-03-12 |

### `data-handling` (4)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/bond-data`](ai-asset-pricing/bond-data.md) | finance | `data-acquisition` `data-analysis` | Reference for the Dickerson corporate bond dataset as used with PyBondLab: WRDS-to-PyBondLab column mapping, alternative return columns, value-weight choices, the 1-22 rating encoding, signal clusters and known data traps. | [view](ai-asset-pricing/bond-data.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/bond-data/SKILL.md) | 2026-03-11 |
| [`/panel-data-rules`](ai-asset-pricing/panel-data-rules.md) | finance | `data-analysis` `code-generation` | Eight rules for CRSP and Compustat panels: gap-checked lags and leads, accounting-data timing, CCM linking, universe filters and winsorisation to confirm with the user, Compustat missing values, book-equity hierarchies and quarterly-data traps. | [view](ai-asset-pricing/panel-data-rules.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/panel-data-rules/SKILL.md) | 2026-03-12 |
| [`/wrds-psql`](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/wrds-psql/SKILL.md){ target=_blank rel=noopener } | finance | `data-acquisition` | Querying WRDS PostgreSQL from the local machine with psql and a .pgpass file: single-line command rule, query patterns, CSV and Parquet export, schema discovery and large extractions. Adapted from Piotr Orlowski's claude-wrds-public wrds-psql skill (0.470 word-sequence similarity). | — | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/wrds-psql/SKILL.md) | 2026-03-24 |
| [`/wrds-schema`](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/wrds-schema/SKILL.md){ target=_blank rel=noopener } | finance | `data-acquisition` | Preloads WRDS schema knowledge (tables, columns, join keys, known traps) for CRSP, Compustat, OptionMetrics and TAQ. Piotr Orlowski's claude-wrds-public wrds-schema skill (0.857 word-sequence similarity) extended with JKP global factor and Dickerson bond schemas. | — | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/wrds-schema/SKILL.md) | 2026-03-11 |

### `drafting` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/setup-paper`](ai-asset-pricing/setup-paper.md) | finance | `paper-drafting` | Starts a new paper from the repo's LaTeX boilerplate, filling title, authors and affiliations, inserting tagged placeholder text and compiling a test PDF. | [view](ai-asset-pricing/setup-paper.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/setup-paper/SKILL.md) | 2026-03-24 |
| [`/write-section`](ai-asset-pricing/write-section.md) | finance | `paper-drafting` | Writes a new section or subsection of an empirical finance paper under the repo's academic writing rules. | [view](ai-asset-pricing/write-section.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/write-section/SKILL.md) | 2026-03-24 |

### `editing` (4)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/compare-versions`](ai-asset-pricing/compare-versions.md) | general | `revision-editing` | Shows the diff between current and proposed text together with the reason for each change. | [view](ai-asset-pricing/compare-versions.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/compare-versions/SKILL.md) | 2026-03-12 |
| [`/edit-section`](ai-asset-pricing/edit-section.md) | finance | `revision-editing` | Revises an existing paper section for style, clarity and correctness under the repo's writing rules. | [view](ai-asset-pricing/edit-section.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/edit-section/SKILL.md) | 2026-03-12 |
| [`/proofread`](ai-asset-pricing/proofread.md) | general | `revision-editing` | Mechanical scan for typos, LaTeX formatting slips, punctuation and spacing. | [view](ai-asset-pricing/proofread.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/proofread/SKILL.md) | 2026-03-11 |
| [`/style-check`](ai-asset-pricing/style-check.md) | finance | `revision-editing` | Checks LaTeX prose against the repo's academic writing standards and reports violations by category and severity. | [view](ai-asset-pricing/style-check.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/style-check/SKILL.md) | 2026-03-11 |

### `figures` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/publication-figures`](ai-asset-pricing/publication-figures.md) | finance | `data-analysis` `dissemination` | Figure conventions for empirical finance and economics: matplotlib styling, palettes, sizes, export settings, journal overrides and templates for time series, decile bars, coefficient plots and event studies. | [view](ai-asset-pricing/publication-figures.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/publication-figures/SKILL.md) | 2026-04-19 |

### `ideation` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/idea`](ai-asset-pricing/idea.md) | finance | `hypothesis-generation` `literature-discovery` `research-design` | Adversarial idea generator for empirical asset pricing that surveys the literature through Perplexity, attacks each hypothesis in a loop, checks WRDS data feasibility and compiles a research-plan skeleton. | [view](ai-asset-pricing/idea.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/idea/SKILL.md) | 2026-03-12 |

### `infra` (7)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/build-context`](ai-asset-pricing/build-context.md) | finance | `paper-drafting` | Builds a paper-context file from the user's .tex, .md or .pdf drafts, recording abstract, key results, terminology, sample, section structure, labels and key citations for later writing and audit skills. | [view](ai-asset-pricing/build-context.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/build-context/SKILL.md) | 2026-03-12 |
| [`/build-paper`](ai-asset-pricing/build-paper.md) | general | `dissemination` | Compiles the LaTeX paper to PDF through the pdflatex and bibtex cycle and lists common compilation failures. | [view](ai-asset-pricing/build-paper.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/build-paper/SKILL.md) | 2026-03-24 |
| [`/extract-section`](ai-asset-pricing/extract-section.md) | general | `revision-editing` | Pulls one section out of main.tex by its key so later skills can work on it in isolation. | [view](ai-asset-pricing/extract-section.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/extract-section/SKILL.md) | 2026-03-12 |
| [`/latex-doctor`](ai-asset-pricing/latex-doctor.md) | general | `dissemination` | Cleans .tex files by stripping comments, fixing compile errors and checking section markers. | [view](ai-asset-pricing/latex-doctor.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/latex-doctor/SKILL.md) | 2026-03-24 |
| [`/new-project`](ai-asset-pricing/new-project.md) | finance |  | Scaffolds a new empirical project folder with LaTeX, code, scripts, results, literature and guidance subfolders plus a README and a project-level CLAUDE.md. | [view](ai-asset-pricing/new-project.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/new-project/SKILL.md) | 2026-04-19 |
| [`/onboard`](ai-asset-pricing/onboard.md) | finance |  | Agent-driven cold start for the repo: finds or installs Python 3.11 or later, runs the shared bootstrap audit, plan and apply cycle, and sets up WRDS only if the user has an account. | [view](ai-asset-pricing/onboard.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/onboard/SKILL.md) | 2026-04-05 |
| [`/sync-context`](ai-asset-pricing/sync-context.md) | general |  | Detects drift between the code and the agent documentation (docs/ai, AGENTS.md, CLAUDE.md) and proposes updates. | [view](ai-asset-pricing/sync-context.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/sync-context/SKILL.md) | 2026-03-24 |

### `literature` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/research`](ai-asset-pricing/research.md) | finance | `literature-discovery` | Searches for papers, references and methodology literature through the Perplexity MCP tools and returns them in a fixed format. | [view](ai-asset-pricing/research.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/research/SKILL.md) | 2026-03-12 |
| [`/split-pdf`](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/split-pdf/SKILL.md){ target=_blank rel=noopener } | finance | `literature-synthesis` | Downloads a paper, splits the PDF into chunks sized to its length, reads them in controlled batches and writes structured notes on question, data, method, results and factor definitions. Adapted, without credit in the file, from Scott Cunningham's MixtapeTools split-pdf skill (0.474 word-sequence similarity). | — | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/split-pdf/SKILL.md) | 2026-03-12 |

### `meta` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/create-audit-agent`](ai-asset-pricing/create-audit-agent.md) | general | `code-generation` | Creates new Claude Code agent files or audits existing ones against a 17-point checklist covering frontmatter, routing keywords, body-frontmatter alignment and consistency across agents. | [view](ai-asset-pricing/create-audit-agent.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/create-audit-agent/SKILL.md) | 2026-03-11 |
| [`/create-skill`](ai-asset-pricing/create-skill.md) | general | `code-generation` | Creates new Claude Code skills, auto-apply skills or trigger rules, or audits existing ones, walking through type choice, structural pattern, generation, validation and registration. | [view](ai-asset-pricing/create-skill.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/create-skill/SKILL.md) | 2026-03-24 |
| [`/rule-create`](ai-asset-pricing/rule-create.md) | general | `code-generation` | Creates new .claude/rules files or audits existing ones for quality and effectiveness. | [view](ai-asset-pricing/rule-create.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/rule-create/SKILL.md) | 2026-03-11 |

### `review` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/outline`](ai-asset-pricing/outline.md) | finance | `revision-editing` | Analyses paper structure, reporting section balance, word counts and compliance with Cochrane's writing principles. | [view](ai-asset-pricing/outline.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/outline/SKILL.md) | 2026-03-12 |

### `revision` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/respond-to-referee`](ai-asset-pricing/respond-to-referee.md) | finance | `revision-editing` | Drafts response-letter text and matching LaTeX edits for a single referee point, or a complete reply document from a LaTeX template. | [view](ai-asset-pricing/respond-to-referee.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/respond-to-referee/SKILL.md) | 2026-03-24 |

### `slides` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/build-deck`](ai-asset-pricing/build-deck.md) | finance | `dissemination` | Builds and compiles Beamer seminar or conference decks following a Rhetoric of Decks philosophy, with narrative templates, a compile loop and a self-review step. | [view](ai-asset-pricing/build-deck.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/build-deck/SKILL.md) | 2026-03-24 |

### `submission` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/submission-prep`](ai-asset-pricing/submission-prep.md) | finance | `dissemination` | Pre-submission checklist for the Journal of Finance, Review of Financial Studies, Journal of Financial Economics or another target journal. | [view](ai-asset-pricing/submission-prep.md) | [origin](https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/submission-prep/SKILL.md) | 2026-03-11 |
