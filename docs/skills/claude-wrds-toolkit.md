<!-- DO NOT EDIT — auto-generated from skills/claude-wrds-toolkit.yml by scripts/build_skills_index.py -->

# Claude Code WRDS Toolkit (Piotr Orłowski)

license: `none` · 8 skills · last update: 2026-05-06

**Source:** <https://github.com/piotrek-orlowski/claude-wrds-public>

**Maintainers:** Piotr Orłowski (piotrek-orlowski on GitHub)

**Compatibility:** `claude-code`

!!! warning "No licence declared"
    The source repository declares no licence, so its skill texts are not
    reproduced here. The skills are listed by name with RISE's own short
    descriptions, and each links to its file in the source repository.
    Ask the maintainer before reusing or adapting the material.

> A Claude Code setup for pulling empirical-finance data from WRDS: five subagents (database specialists for CRSP with CCM/Compustat linking, OptionMetrics and TAQ, a multi-database orchestrator, and a general academic-paper reader) plus three connection and schema skills, shipped with a permissions file that pre-approves the psql, ssh and scp calls. Its distinctive design choice is routing TAQ work through SAS batch jobs on the WRDS grid over SSH while everything else goes through a static psql service entry, which keeps the agents from tripping approval prompts. Requires a WRDS account with SSH-key access and Duo MFA. No licence declared: skill texts are not reproduced here; each skill links to its source.


**Source YAML:** [`skills/claude-wrds-toolkit.yml`](https://github.com/bhanneke/RISE/blob/main/skills/claude-wrds-toolkit.yml)

## Skills

### `data-handling` (5)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`crsp-wrds-expert`](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/crsp-wrds-expert.md){ target=_blank rel=noopener } | finance | `data-acquisition` | Subagent specialised in the CRSP stock files on WRDS, covering returns, price and share adjustments, delisting returns, identifiers, and linking CRSP to Compustat fundamentals through the CCM table, all via PostgreSQL. | — | [origin](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/crsp-wrds-expert.md) | 2026-05-06 |
| [`optionmetrics-wrds-expert`](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/optionmetrics-wrds-expert.md){ target=_blank rel=noopener } | finance | `data-acquisition` | Subagent for OptionMetrics IvyDB extraction on WRDS: option prices, implied volatilities, Greeks, volatility surfaces and standardised options, plus mapping option security IDs to CRSP PERMNOs. | — | [origin](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/optionmetrics-wrds-expert.md) | 2026-02-27 |
| [`taq-wrds-expert`](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/taq-wrds-expert.md){ target=_blank rel=noopener } | finance | `data-acquisition` `data-analysis` | Subagent for NYSE TAQ tick data that writes SAS programs, submits them as batch jobs on the WRDS cloud over SSH, and retrieves results, aimed at tasks such as NBBO spreads, trade filtering and realized variance. | — | [origin](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/taq-wrds-expert.md) | 2026-02-27 |
| [`/wrds-psql`](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/skills/wrds-psql/SKILL.md){ target=_blank rel=noopener } | finance | `data-acquisition` | Connection and query conventions for hitting WRDS PostgreSQL from the local machine with stored credentials, including how to shape commands so they run without approval prompts and how to export large extracts. | — | [origin](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/skills/wrds-psql/SKILL.md) | 2026-02-27 |
| [`/wrds-schema`](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/skills/wrds-schema/SKILL.md){ target=_blank rel=noopener } | finance | `data-acquisition` | Session-start helper that has the specialist agents query table and column metadata for the chosen WRDS databases and return a compact reference card, so later queries need fewer exploratory round-trips. | — | [origin](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/skills/wrds-schema/SKILL.md) | 2026-02-27 |

### `infra` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`wrds-query-orchestrator`](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/wrds-query-orchestrator.md){ target=_blank rel=noopener } | finance | `data-acquisition` | Coordinating subagent for requests that span several WRDS databases; it dispatches the specialist agents, assembles the merged query via the appropriate link tables, and keeps query files organised and version-controlled. | — | [origin](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/wrds-query-orchestrator.md) | 2026-02-27 |
| [`/wrds-ssh`](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/skills/wrds-ssh/SKILL.md){ target=_blank rel=noopener } | finance | `data-acquisition` | Patterns for working on the WRDS servers over SSH: running SAS, submitting and monitoring batch jobs, and moving files between the local machine and WRDS scratch space. | — | [origin](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/skills/wrds-ssh/SKILL.md) | 2026-02-27 |

### `literature` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`paper-reader`](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/paper-reader.md){ target=_blank rel=noopener } | finance | `literature-synthesis` | General-purpose subagent that reads academic papers in finance, economics, statistics and related fields and writes structured summaries of their contributions, methods and findings; not WRDS-specific. | — | [origin](https://github.com/piotrek-orlowski/claude-wrds-public/blob/main/agents/paper-reader.md) | 2026-02-27 |
