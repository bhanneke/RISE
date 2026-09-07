<!-- DO NOT EDIT — auto-generated from projects/landscape/openecon-data.yml by scripts/build_indexes.py -->

# OpenEcon Data

`external` · status: `active` · focus: `analysis` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/hanlulong/openecon-data>

**Source:** [`projects/landscape/openecon-data.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/openecon-data.yml)

## Positioning

An MCP server plus web app giving AI agents natural-language access to 330K+ economic indicators indexed across 11 providers (FRED, World Bank, IMF, Eurostat, UN Comtrade, BIS, Statistics Canada, OECD, ExchangeRate-API, CoinGecko, ChinaMacro). Sits in the data-acquisition layer of RISE, complementary to StatsPAI/stata-code (which analyze data the agent already has) rather than overlapping with them.

## Distinctive contribution

The only economic-data-acquisition MCP tool in the catalog: an LLM-parser → semantic-provider-routing → fetch-with-fallback pipeline that resolves natural-language requests (including multi-language queries and automatic regional-group expansion like G7/BRICS/EU) into indicator series, with conversational follow-ups and multi-format export (CSV/JSON/Stata/Python code) carrying source attribution.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Touches one stage only (data-acquisition); no analysis, drafting, or review functionality. |
| Autonomy level | 0 | Tool: every query is human- or agent-issued; conversational follow-ups persist context but do not amount to independent task execution. |
| Architectural transparency | 2 | Three-stage pipeline (LLM parser → semantic routing → fetch-with-fallback) documented and open-sourced (FastAPI/React/Redis stack); no published prompts for the LLM-parser stage. |
| Inputs supported | 1 | One input form (natural-language query) plus data-source access across 11 providers; no literature-corpus access. |
| Outputs / reproducibility | 1 | Persists structured data exports (CSV/JSON/Stata/Python) with source attribution and cached deterministic re-fetch; no paper/code/data-manifest bundle — it is a data tool, not a paper-producing pipeline. |
| Internal evaluation | 0 | Only latency metrics reported (~0.1s cached, several seconds first query); no evaluation of query-to-indicator mapping accuracy. |
| Openness | 1 | AGPL-3.0 (copyleft, source-sharing required for hosted service); free hosted demo gated at 20 queries before signup. |
| Maturity / traction | 2 | 69 stars, 885 commits, live production demo (data.openecon.ai/chat) — active beta with external users, single-maintainer team. |
| Cross-family policy | 0 | Not applicable — a data-fetching tool with no cross-model review process. |
| Runtime assurance | 1 | Automatic fallback mechanisms when a preferred data provider fails; no claim-verification or citation-audit layer. |
| Cross-platform portability | 2 | MCP server usable from Claude Code, Codex, and any compatible MCP client, plus a self-hostable stack and a browser demo. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-acquisition`


**Architectural features:** `tool-use` `persistent-memory`


**Inputs:** `natural-language-query`


**Outputs:** `datasets` `csv-json-stata-python-exports`


**Data sources:** `fred` `world-bank` `imf` `eurostat` `un-comtrade` `bis` `statistics-canada` `oecd` `exchangerate-api` `coingecko` `chinamacro`


## Limitations

- AGPL-3.0 license requires source-sharing for hosted deployments, a heavier obligation than the catalog's typical MIT/Apache entries.
- No reported evaluation of whether natural-language queries are correctly mapped to the intended indicator series across providers.
- Free demo capped at 20 queries; self-hosting requires OpenRouter API credentials and infrastructure (Redis, Node.js, Python).

## Related projects in this catalog

- [`stata-mcp`](stata-mcp.md)
- [`statspai`](statspai.md)
- [`stata-code`](stata-code.md)
