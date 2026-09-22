<!-- DO NOT EDIT — auto-generated from projects/landscape/dare.yml by scripts/build_indexes.py -->

# DARE (De-Anthropocentric Research Engine)

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/yogsoth-ai/de-anthropocentric-research-engine>

**Source:** [`projects/landscape/dare.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/dare.yml)

## Positioning

The largest pure-markdown research-skill corpus in the catalog: 900+ skills over a four-layer hierarchy — Campaign (45+) -> Strategy (200+) -> Tactic (120+) -> SOP (500+), each layer holding one concern and calling only the layer below — grouped into ten composable packages (north-star-crystallization, knowledge-acquisition, hypothesis-formation, creative-ideation, convergence, deep-insight, stress-test, experiment-execution, knowledge-structuring, ara-from-context) and wired to seven MCP servers (Semantic Scholar, alphaXiv, Brave, Tavily, keenable, Apify, plus a local wiki-vault knowledge graph). It covers direction-setting through experiment execution and stops there: no drafting, referee-simulation or submission stage exists, and an automated paper-writing pipeline is listed only as a roadmap item. There is no application code at all — the runtime is Codex or Claude Code and the framework is the instruction set.

## Distinctive contribution

Orchestration is deliberately non-linear: rather than a fixed pipeline the agent is handed an "arsenal" and selects campaign sequences from the current research state, with backtrack conditions as first-class objects and an Executable Research Spec (machine-readable, checkbox-tracked, quantified completion criteria, +/-10% deviation bounds) as the contract between human direction and autonomous execution. The skill files carry machine-checkable discipline rather than prose advice — the sampled assumption-audit SOP declares its tactic and SOP dependencies in YAML frontmatter, budgets tokens per sub-task with +/-10% ranges, and hard-gates exit at >=80% budget use — and the repo claims a closed dependency graph across all 2,476 skill-to-skill edges.

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
| Maturity / traction | 2 | 442 stars / 34 forks in seven months, pushed 2026-09-03, 3 open issues — real external interest, but no releases or version tags verified, no named maintainer, and no reported downstream use. |
| Cross-family policy | 0 | The Codex and Claude Code installers are alternatives, not a pairing: adversarial-debate and stress-test skills run inside whichever single runtime is installed, and nothing requires or recommends a reviewer from a second model family. |
| Runtime assurance | 2 | Multiple in-pipeline gates — per-SOP token budgets with a >=80%-use exit gate, falsifiability audits, load-bearing x likely-false assumption classification, adversarial stress-testing and sacred-cow hunting, backtrack conditions, +/-10% spec-deviation bounds requiring human authorisation — but no evidence-verification, citation-grounding or proof-checking layer, and the gates are instructions to the model rather than enforced checks. |
| Cross-platform portability | 2 | Two documented runtimes (Codex via install/codex.sh or .ps1, Claude Code via manual .claude/skills plus .mcp.json) over a deliberately portable substrate of markdown skills and MCP servers; short of framework-agnostic because only these two paths are documented and only Codex has an installer. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

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
- Counts are self-reported and inconsistent: the GitHub description says 9 packages while the README lists 10 with per-package counts, and the '900+ skills' / '2,476 edges' figures were not recounted at scoring.
- Sheer size is a cost as well as a feature: 900+ skills over four layers is a large surface to audit before trusting any single campaign, and the roadmap itself lists automated redundancy pruning ('skill ablation') as an open task.
- No drafting, review or dissemination coverage — output stops at specs, designs and analyses; the Claude Code install path is manual.

## Related projects in this catalog

- [`auto-empirical-research-skills`](auto-empirical-research-skills.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`sakana-ai-scientist`](sakana-ai-scientist.md)
