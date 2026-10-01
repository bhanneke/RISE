<!-- DO NOT EDIT — auto-generated from projects/landscape/dare.yml by scripts/build_indexes.py -->

# DARE (De-Anthropocentric Research Engine)

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/yogsoth-ai/de-anthropocentric-research-engine>

**Licence:** `Apache-2.0`

**Source:** [`projects/landscape/dare.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/dare.yml)

## Positioning

A pure-markdown research-skill corpus, substantially rearchitected in a "v4" rewrite merged 2026-09-23: what had been a four-layer hierarchy of 900+ skills (Campaign -> Strategy -> Tactic -> SOP) grouped into ten packages is now a two-layer research graph of 267 nodes — 51 Tactics (complete research transformations) composed from 216 SOPs (single-purpose steps) — reached through four product shells (entry, catalog, write-spec, execute-spec); the old `cli/` and `dsh-plugin/` components were dropped in the same merge. It now lists 11 MCP servers as optional retrieval back-ends (Semantic Scholar, alphaXiv, PubMed, bioRxiv, medRxiv, Perplexity, Brave, Tavily, keenable, You.com, Apify, plus a local wiki-vault knowledge graph) but is explicitly "decoupled from retrieval" — none is required. It still covers direction-setting through experiment execution and stops there: no drafting, referee-simulation or submission stage exists, and an automated paper-writing pipeline is listed only as a roadmap item. There is no application code at all — the runtime is Codex or Claude Code and the framework is the instruction set.

## Distinctive contribution

Orchestration is deliberately non-linear: rather than a fixed pipeline, the Executable Research Spec (machine-readable, checkbox-tracked, quantified completion criteria, +/-10% deviation bounds) commits to a tactic sequence drawn from the 51-tactic catalog and records the conditions under which that sequence is abandoned, with backtracking as a first-class mechanism bridging human direction and autonomous execution. The skill files carry machine-checkable discipline rather than prose advice — the sampled assumption-audit SOP declares its tactic and SOP dependencies in YAML frontmatter, budgets tokens per sub-task with +/-10% ranges, and hard-gates exit at >=80% budget use. The v4 rewrite (merged 2026-09-23) replaced the earlier 900+-skill / 2,476-edge claim with a much smaller, precisely countable graph — 267 nodes and roughly 485 edges (339 mandatory calls + 146 soft jumps) — resolving the previous self-reported count inconsistency by shrinking and simplifying the graph rather than by auditing the old one.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Six stages — direction crystallisation, multi-pass literature acquisition, gap detection/synthesis, hypothesis formation with falsifiability audits, experiment design, and factor-level/sensitivity analysis — with clear gaps: no paper-drafting, referee-simulation or dissemination coverage, and execution depends on whatever tools the host runtime provides since DARE ships no code. |
| Autonomy level | 3 | Stated stance is 'The AI is the researcher — you set the direction'; after the Research Spec is approved the engine selects and sequences campaigns itself, backtracks on its own conditions, and recovers sessions from checkpoints without per-step approval. |
| Architectural transparency | 3 | Apache-2.0 with every skill published as plain markdown with dependencies declared inline in frontmatter and no hidden runtime component; the sampled assumption-audit/SKILL.md is a real SOP with a token-budget table and an exit gate, not a placeholder. |
| Inputs supported | 2 | Multiple input forms (cold/warm/hot-start free-text direction, plus ara-from-context ingestion of existing material) with literature access via Semantic Scholar/alphaXiv/web-search MCP servers and a local wiki-vault corpus; no structured dataset or database connector is documented. |
| Outputs / reproducibility | 2 | Persists durable markdown artifacts — Executable Research Specs with checkbox tracking, context checkpoints, gap and audit reports, wiki-vault entries — but nothing versions a run or makes the non-linear campaign path replayable. |
| Internal evaluation | 0 | No paper, no benchmark, no reported demo outcomes at scoring date; the only citation in the README is external (Park et al. 2023 on declining scientific disruptiveness) and motivates the design rather than testing it. |
| Openness | 2 | Apache-2.0 and self-contained (a single clone carries all 900+ skills), but running it requires a paid Codex or Claude Code subscription plus API keys for the Brave/Tavily/Apify MCP servers — not free-tier reproducible. |
| Maturity / traction | 2 | 503 stars / 42 forks (up from 442/34), including a major v4 architecture rewrite merged 2026-09-23 that replaced the four-layer/900-skill design with the two-layer graph — sustained real external interest and continued active development, but still no releases or version tags verified, no named maintainer, and no reported downstream use. |
| Cross-family policy | 0 | The Codex and Claude Code installers are alternatives, not a pairing: adversarial-debate and stress-test skills run inside whichever single runtime is installed, and nothing requires or recommends a reviewer from a second model family. |
| Runtime assurance | 2 | Multiple in-pipeline gates — per-SOP token budgets with a >=80%-use exit gate, falsifiability audits, load-bearing x likely-false assumption classification, adversarial stress-testing and sacred-cow hunting, backtrack conditions, +/-10% spec-deviation bounds requiring human authorisation — but no evidence-verification, citation-grounding or proof-checking layer, and the gates are instructions to the model rather than enforced checks. |
| Cross-platform portability | 2 | Two documented runtimes (Codex via install/codex.sh or .ps1, Claude Code via manual .claude/skills plus .mcp.json) over a deliberately portable substrate of markdown skills and MCP servers; short of framework-agnostic because only these two paths are documented and only Codex has an installer. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `hypothesis-generation` `literature-discovery` `literature-synthesis` `research-design` `data-analysis`


**Architectural features:** `tool-use` `rag-knowledge-base` `persistent-memory` `iterative-loop` `human-in-loop`


**Inputs:** `research-direction` `existing-context`


**Outputs:** `research-specs` `hypothesis-sets` `literature-maps` `gap-analyses` `experiment-designs` `wiki-vault-entries`


**Data sources:** `semantic-scholar-api` `alphaxiv` `web-search-apis` `apify-scraping`


**Knowledge sources:** `wiki-vault-knowledge-graph` `semantic-scholar`


## Limitations

- The stance is the inverse of this catalog's human-approval-by-default rule: the README frames the human as 'oracle' and 'guardian' while asserting 'The AI is the researcher — you set the direction' and 'Science is dying because the human is in the way'. Read DARE as a source of methods to borrow (assumption audits, adversarial debate protocols, abstraction laddering, falsifiability audits) rather than a harness to adopt whole; its single approval point sits at the spec boundary, not inside the work.
- No evaluation of any kind — no paper, no benchmark, no reported outcomes — so all claims about the value of the 900+ skills are architectural assertions.
- The gates are instruction-level, not enforced: token budgets, +/-10% bounds and the >=80%-budget exit gate are asked of the model in markdown; nothing outside the model verifies compliance.
- Anonymous provenance: the repo sits under a pseudonymous organisation (Yogsoth-AI, created 2026-05-12, no institutional affiliation) with no named maintainers, which makes accountability and long-term maintenance unassessable.
- A v4 rewrite merged 2026-09-23 replaced the earlier four-layer, 900+-skill, 10-package design (whose self-reported package/skill/edge counts were internally inconsistent) with a two-layer, 267-node graph (51 tactics, 216 SOPs) and dropped the CLI and `dsh-plugin/` components entirely — a major, recent architecture change; the new, smaller counts are precise but, like the old ones, are self-reported and not independently audited here.
- The rewrite is only days old at scoring date (2026-10-01): it is unclear whether the simplification has been exercised end-to-end by external users, and the previous roadmap item of automated redundancy pruning ('skill ablation') may or may not still apply to the new graph.
- No drafting, review or dissemination coverage — output stops at specs, designs and analyses; the Claude Code install path is manual.

## Related projects in this catalog

- [`auto-empirical-research-skills`](auto-empirical-research-skills.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`sakana-ai-scientist`](sakana-ai-scientist.md)
