<!-- DO NOT EDIT — auto-generated from projects/landscape/mcp-stata.yml by scripts/build_indexes.py -->

# mcp-stata (Stata agentic toolkit)

`external` · status: `dormant` · focus: `analysis` · discipline: `economics` · started: 2025

**Project page:** <https://github.com/tmonk/mcp-stata>

**Licence:** `AGPL-3.0`

**Source:** [`projects/landscape/mcp-stata.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/mcp-stata.yml)

## Positioning

A stdio MCP server, distributed on PyPI and run through uvx, that gives an AI agent control of a local licensed Stata 17+ installation: run commands or .do files (including background jobs), inspect and lint data and code, read r()/e()/s() stored results as structured JSON, export graphs, and diff session state. It ships with a catalog of 20 Markdown skills (replication and robustness, data audit, data provenance, publication QA, referee response, causal inference, power analysis, legacy-code modernization) that tell the agent how to use those tools. Sits in the data-analysis / code-generation layer next to stata-mcp (hanlulong); the two are independent projects, and the IDE front end here is a separate companion repo, Stata Workbench (tmonk/stata-workbench, a VS Code extension, also AGPL-3.0).

## Distinctive contribution

Where stata-mcp (hanlulong) is an MIT-licensed VS Code extension that bundles an HTTP/SSE MCP server, mcp-stata is agent-first: a client-agnostic stdio server with one-line installers for Claude Code, Codex, Gemini, Cursor, Windsurf and VS Code, structured stored-results retrieval intended for programmatic checking of estimates, a command-history diff of variables and macros, and a research-workflow skill layer (replication, publication QA, referee response) that stata-mcp does not have. Its Stata News "Community corner" feature is the only vendor-side recognition of a Stata agent bridge in the catalog.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Tools cover Stata execution and code work (data-analysis, code-generation) and the skills add rerun-based replication and robustness; referee-response and publication-QA skills organise reruns and table checks but do not draft or review a paper. |
| Autonomy level | 0 | A tool the host agent calls command by command; the server has no planning loop of its own, and the skills are instructions for the calling agent, not an autonomous pipeline. |
| Architectural transparency | 3 | AGPL-3.0 source for the Python server and Rust sorter, all 20 SKILL.md files, MCP config examples, a pytest suite with CI, and a benchmark harness are public in the repo. |
| Inputs supported | 1 | Stata code or .do files plus direct dataset loading (sysuse/webuse/path/URL); no literature corpus or external data-source connector. |
| Outputs / reproducibility | 2 | Every run writes a log file and returns structured results and exported graphs, and session history diffs give an audit trail; no bundled manifest ties outputs to data versions for end-to-end regeneration. |
| Internal evaluation | 1 | Unit/integration tests and a speed benchmark (about 0.4 s per test on a 20-test suite) check the software, not the correctness of agent-produced analyses; no output-quality evaluation reported. |
| Openness | 1 | Source available under AGPL-3.0, a copyleft rather than permissive licence, and every run requires a paid Stata 17+ licence plus a paid agent client. |
| Maturity / traction | 2 | 86 stars / 20 forks, 30 tagged releases up to v3.3.0 on PyPI, featured in Stata News; external users but single maintainer, and no push since 2026-05-12. |
| Cross-family policy | 0 | Not applicable: an MCP tool driven by whichever agent the user runs, with no reviewer role of its own. |
| Runtime assurance | 1 | Structured error envelopes (return codes, parsed r(XXX) errors, trace mode), a static .do/.ado linter and server-side safety enforcement on submitted code; nothing checks whether the estimates or claims built on them are right. |
| Cross-platform portability | 3 | Protocol-based stdio server with documented installers or configs for Claude Code, Claude Desktop, Codex, Gemini, Cursor, Windsurf, VS Code and Antigravity, plus Claude and Codex plugin manifests; runs on macOS, Linux and Windows. |

*Scored on 2026-09-29. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `code-generation` `replication`


**Architectural features:** `tool-use`


**Inputs:** `stata-do-files` `stata-commands` `user-dataset`


**Outputs:** `execution-results` `stored-results-json` `figures` `log-files`


**Data sources:** `user-provided` `stata-sysuse-webuse`


**Knowledge sources:** `stata-help-files`


## Limitations

- Requires a licensed local Stata 17+ (MP, SE or BE) and uses Stata's proprietary pystata module; unusable without proprietary software.
- AGPL-3.0 copyleft: modified versions offered as a network service must publish their source, which restricts embedding in closed tools.
- No push since 2026-05-12 (dormant by the three-month rule) after a fast release cadence to v3.3.0; 13 open issues.
- The skills organise replication, QA and referee-response work but nothing validates the agent's econometric choices; correctness rests on the user.
- Single maintainer (a PhD candidate); the recommended install path pipes a remote script into the shell (curl | bash, irm | iex).

## Related projects in this catalog

- [`stata-mcp`](stata-mcp.md)
- [`stata-code`](stata-code.md)
- [`statspai`](statspai.md)
- [`econ-agent-skills`](econ-agent-skills.md)
- [`auto-empirical-research-skills`](auto-empirical-research-skills.md)
