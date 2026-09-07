<!-- DO NOT EDIT — auto-generated from projects/landscape/stata-code.yml by scripts/build_indexes.py -->

# stata-code

`external` · status: `active` · focus: `analysis` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/brycewang-stanford/stata-code>

**Source:** [`projects/landscape/stata-code.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/stata-code.yml)

## Positioning

An agent-native Python bridge to Stata offering four parallel interfaces onto one core — an MCP server (21 tools), a Jupyter kernel, a VS Code extension, and a CLI — for running econometric analyses (DiD, IV, RDD) and producing publication-ready tables with token-efficient, structured output. Sits in the data-analysis / code-generation layer of RISE alongside StatsPAI (same maintainer ecosystem) and stata-mcp (hanlulong), as a Stata-execution bridge rather than a Python-native re-implementation of Stata's estimators.

## Distinctive contribution

The only Stata bridge in the catalog offering four simultaneous frontends (MCP/Jupyter/VS Code/CLI) over one core, a persistent daemon mode for cross-call data retention via Unix socket, 34 typed error categories with suggested fixes, command-safety guardrails that block shell escapes and destructive file operations, and built-in cross-validation against StatsPAI for result-parity auditing between the two independent tools.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Touches two adjacent stages (data-analysis, code-generation); no literature, drafting, or review coverage. |
| Autonomy level | 0 | Tool: every MCP call, kernel cell, or CLI command is issued by a human or calling agent; the daemon persists data but does not plan or execute tasks independently. |
| Architectural transparency | 3 | MIT-licensed, full source for all four frontends, comprehensive CI-covered test suite (schema, runner, console parser, MCP, kernel, VS Code integration) and a documented 34-category error taxonomy. |
| Inputs supported | 1 | One input form (Stata code) plus direct dataset access via pystata/console backends; no literature or external-corpus access. |
| Outputs / reproducibility | 2 | Persists structured code/log/graph references and publication-ready tables; token-efficient by design (refs over inline content) but no end-to-end paper/data-manifest bundle. |
| Internal evaluation | 2 | Systematic internal test suite across all interfaces plus StatsPAI cross-validation for numeric result-parity auditing between two independently built tools — no external/third-party validation yet. |
| Openness | 2 | MIT license (explicitly chosen over AGPL to avoid copyleft transmission), pip-installable; still requires a paid Stata 13+ (17+ preferred) license to actually execute analyses. |
| Maturity / traction | 1 | 42 stars, 161 commits, v0.12 (July 2026) — active single-maintainer research prototype, pre-1.0. |
| Cross-family policy | 0 | Not applicable — an execution tool invoked by whichever AI assistant (Claude Code, Cursor, etc.) the user configures; no cross-model review of its own. |
| Runtime assurance | 2 | Multiple in-pipeline gates: typed 34-category error handling with suggested fixes, pre-execution command-safety guardrails (blocks shell escapes/file deletion), and StatsPAI cross-validation for result parity. |
| Cross-platform portability | 2 | Four execution surfaces (MCP, Jupyter kernel, VS Code extension, CLI) over one core, usable from Claude Code, Cursor, Claude Desktop, and plain Jupyter/VS Code. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `code-generation`


**Architectural features:** `tool-use` `persistent-memory`


**Inputs:** `stata-do-files` `user-dataset`


**Outputs:** `analysis-code` `publication-tables` `execution-logs`


**Data sources:** `user-provided`


## Limitations

- Requires a paid Stata 13+ installation (17+ preferred for the pystata in-memory backend); not runnable end-to-end on free/commodity software alone.
- Single-maintainer, pre-1.0 (v0.12); API and error-taxonomy surface may still shift release to release.
- Cross-validation against StatsPAI checks numeric parity between two tools from the same maintainer ecosystem, not against an independent ground truth.

## Related projects in this catalog

- [`stata-mcp`](stata-mcp.md)
- [`statspai`](statspai.md)
- [`auto-empirical-research-skills`](auto-empirical-research-skills.md)
