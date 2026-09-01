<!-- DO NOT EDIT — auto-generated from projects/landscape/stata-mcp.yml by scripts/build_indexes.py -->

# Stata MCP

`external` · status: `active` · focus: `analysis` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/hanlulong/stata-mcp>

**Source:** [`projects/landscape/stata-mcp.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/stata-mcp.yml)

## Positioning

An MCP server plus VS Code / Cursor / Antigravity IDE extension that lets AI coding assistants (GitHub Copilot, Claude Code, Claude Desktop, Cline, Cursor AI) run Stata .do-file selections, view results and graphs, and interact with datasets directly inside the editor. Sits in the data-analysis / code-generation layer of RISE, alongside StatsPAI and Auto-Empirical-Research-Skills' Stata backend, but as an IDE-integration bridge rather than a Python causal-inference library or skill collection.

## Distinctive contribution

The only Stata-to-modern-IDE MCP bridge in the catalog: dual transport (streamable HTTP + SSE), isolated per-session Stata instances with multi-session support, a persistent-daemon-free direct execution model, syntax highlighting for .do/.ado/.mata/.doh files, and an in-editor data viewer — published as an installable VS Code Marketplace extension (DeepEcon.stata-mcp) rather than a source-only repo.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Touches two adjacent stages (data-analysis, code-generation) via Stata execution; no literature, drafting, or review stages. |
| Autonomy level | 0 | Pure tool: every run/stop action is a human- or calling-agent-issued command against a live Stata session; no independent task planning. |
| Architectural transparency | 2 | Full MIT-licensed extension and MCP-server source published with a documented dual-endpoint architecture; no 'prompts' concept since the server is invoked by external AI assistants rather than running its own agent loop. |
| Inputs supported | 1 | One input form (Stata code/selection) plus direct dataset access via the bundled data viewer; no literature or external-corpus access. |
| Outputs / reproducibility | 2 | Persists Stata output logs, tables, and graphs in the editor/webview; deterministic re-runs depend on the user's Stata license and data, no bundled data manifest. |
| Internal evaluation | 1 | Video demo and PDF report examples only; no benchmark or systematic evaluation of correctness reported. |
| Openness | 2 | MIT-licensed extension code, but requires a paid Stata 17+ license to run — not reproducible on a free/commodity stack end-to-end. |
| Maturity / traction | 2 | 491 stars / 85 forks / 218 commits, published on the VS Code Marketplace with per-client (Copilot, Claude, Cline, Cursor) configuration docs — beta-stage external adoption. |
| Cross-family policy | 0 | Not applicable — a tool invoked by whichever AI assistant the user has configured; no cross-model review mechanism of its own. |
| Runtime assurance | 1 | Structured real-time output/error display in the editor; no claim-audit or verification gates beyond surfacing Stata's own error messages. |
| Cross-platform portability | 2 | Three IDEs (VS Code, Cursor, Antigravity) and multiple AI-assistant integrations (Copilot, Claude, Cline) via a protocol-based MCP server. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `code-generation`


**Architectural features:** `tool-use`


**Inputs:** `stata-do-files` `user-dataset`


**Outputs:** `execution-results` `figures` `analysis-code`


**Data sources:** `user-provided`


## Limitations

- Requires a paid Stata 17+ installation (17+ preferred for the pystata backend); not usable without proprietary software.
- No accuracy or correctness evaluation reported beyond demo videos — the tool executes Stata faithfully but does not audit results.
- Single-maintainer project (Lu Han / OpenEcon.ai); only 2 open issues tracked, limited external contribution history.

## Related projects in this catalog

- [`stata-code`](stata-code.md)
- [`statspai`](statspai.md)
- [`openecon-data`](openecon-data.md)
