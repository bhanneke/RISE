<!-- DO NOT EDIT — auto-generated from projects/landscape/openscience.yml by scripts/build_indexes.py -->

# OpenScience

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/synthetic-sciences/openscience>

**Source:** [`projects/landscape/openscience.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/openscience.yml)

## Positioning

An open-source (Apache-2.0), model-agnostic AI workbench for scientific research, launched 2026-07-03 as an explicit open alternative to Claude Science: a Bun/TypeScript monorepo whose CLI starts a local server hosting a browser workspace, an agent runtime (default `research` agent plus `biology`/`physics`/`ml` specialists with critique and literature-review sub-agents), 292 bundled markdown skills, and ~30 scientific-database connectors (UniProt, PDB, ChEMBL, PubChem, arXiv, OpenAlex, Semantic Scholar). Sits in the big-lab workbench layer alongside Claude Science, Prism, and Google Co-Scientist, but self-hosted and bring-your-own-key.

## Distinctive contribution

The first credible open-source counterweight to the closed research workbenches: per-request model routing across 75+ providers, local-first operation with no account required, and the entire stack — prompts, agents, skills, connectors, SDK, plugin runtime — auditable and editable in one repo, with an optional managed platform (Atlas) kept strictly non-required. Ships an RSI trajectory critic (correctness / efficiency / coverage / reproducibility, 0-100) and an optional blind-reviewer gate at session finalize.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Eight stages from hypothesis through write-up; the peer-review skill and blind-reviewer gate are optional runtime checks, not a declared referee-simulation or dissemination stage. |
| Autonomy level | 2 | Supervised agent: user sets a goal, the agent runs the research loop with tool permissions and a read-only plan mode; user reviews the resulting artifacts. |
| Architectural transparency | 3 | Full code, agent prompts (per-provider prompt files), skills, connectors, config schema, ARCHITECTURE.md and AGENTS.md all public; released builds fetch the skill catalog from the Atlas index, source builds bundle it. |
| Inputs supported | 3 | Goal prompts, existing project directories, and local datasets; literature APIs (arXiv, OpenAlex, Semantic Scholar, Europe PMC) plus ~30 scientific databases, with private local data by construction. |
| Outputs / reproducibility | 2 | Sessions, artifacts, and provenance persist on disk and are shareable as links, and the critic scores reproducibility — but end-to-end re-runnability from declared inputs is not demonstrated. |
| Internal evaluation | 1 | Demo sessions and launch write-ups only; no benchmark results or third-party evaluation of research-output quality published. |
| Openness | 2 | Apache-2.0, npm-installable, BYOK free and non-gated; demo examples need paid provider keys and heavier experiments need cloud compute, so reproducibility on commodity hardware is partial. |
| Maturity / traction | 2 | Now ~2 months past the July launch: 3.4k stars / 455 forks (up from 2,696/374 at last review), sustained past the initial press-cycle spike, with continuous near-daily releases through v2.0.66 (2026-08-31) and an active issue/PR tracker (18 open issues, occasional external contributor PRs alongside the 2-3 person core team) — enough external engagement and release regularity to move past 'too young to call.' |
| Cross-family policy | 1 | Per-request routing across 75+ providers makes cross-family executor/reviewer setups configurable (e.g., critique sub-agent on another family), but cross-family review is neither default nor required. |
| Runtime assurance | 1 | Optional blind-reviewer gate at finalize plus RSI trajectory critic and tool-permission prompts; all optional, with no mandatory claim-audit or citation-verification gating. |
| Cross-platform portability | 2 | 75+ model providers and macOS/Windows/Linux via npm or platform binaries, but a single self-contained runtime — not deployable across other agent frameworks. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `literature-discovery` `literature-synthesis` `data-acquisition` `data-analysis` `code-generation` `paper-drafting` `revision-editing`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `persistent-memory` `artifact-versioning`


**Inputs:** `research-goal-prompt` `project-directory` `user-datasets`


**Outputs:** `analysis-artifacts` `experiment-code` `figures` `manuscript-drafts`


**Data sources:** `scientific-databases` `user-provided`


**Knowledge sources:** `arxiv` `openalex` `semantic-scholar` `curated-skill-library`


## Limitations

- Near-twin disambiguation: ai4s-research/open-science (~900 stars, created the same day, since rebranded 'Open Science Desktop') is not a fork or mirror but an independently built Tauri desktop app on an attributed OpenCode sidecar, from an anonymous org registered 2026-06-27 with bot-named commits and the name-adjacent domain openedscience.com; org identity (Synthetic Sciences, est. 2025, named maintainers), npm distribution (@synsci/openscience), the openscience.sh docs domain, and launch press mark synthetic-sciences/openscience as the canonical OpenScience — but the namespace confusion persists.
- Runtime provenance is under-disclosed: the agent core closely mirrors the MIT-licensed OpenCode CLI (identical provider-prompt file set — anthropic.txt, beast.txt, gemini.txt, qwen.txt — and session-module layout), yet the NOTICE file credits no OpenCode lineage.
- Three weeks old with a 2-3 person team and no published evaluation of output quality; by the project's own security note the agent is not sandboxed — the permission system is not an isolation boundary.

## Related projects in this catalog

- [`claude-science`](claude-science.md)
- [`google-co-scientist`](google-co-scientist.md)
- [`kosmos`](kosmos.md)
- [`tooluniverse`](tooluniverse.md)
