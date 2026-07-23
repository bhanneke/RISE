<!-- DO NOT EDIT — auto-generated from projects/landscape/evoscientist.yml by scripts/build_indexes.py -->

# EvoScientist

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/EvoScientist/EvoScientist>

**Source:** [`projects/landscape/evoscientist.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/evoscientist.yml)

## Positioning

A self-evolving AI scientist system (arXiv:2603.08127) built on the DeepAgents framework. Six sub-agents (plan, research, code, debug, analyze, write) co-evolve with persistent memory, adaptive per-turn tool selection, dynamic system-prompt rewriting, and installable skill / knowledge packs (EvoSkills). Positioned around "vibe research" — a human-on-the-loop paradigm where the AI acts as a co-evolving research buddy that internalizes scholarly taste.

## Distinctive contribution

Strongest external-benchmark trajectory in the catalog: #1 on DeepResearch Bench, #1 on DeepResearch Bench II, #1 on AstaBench Code & Execution, #1 on AstaBench Data Analysis (all at submission time), plus 6/6 papers accepted at ICAIS 2025 with Best Paper + Appraisal awards. Skills + memory architecture is engineered for *evolution* over sessions, not just task completion.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Nine stages from RQ formulation through revision; six-agent team covers plan/research/code/debug/analyze/write. |
| Autonomy level | 3 | 'Human-on-the-loop' (not in-the-loop): AI acts as a research buddy that internalizes scholarly taste; runs autonomously by default. |
| Architectural transparency | 3 | Open Apache-2.0; technical report arXiv:2603.08127; project site at EvoScientist.github.io. |
| Inputs supported | 2 | Multiple input forms (direction, prior context); skill-pack and MCP-server extensibility. |
| Outputs / reproducibility | 2 | Persistent memory enables session-to-session continuity; benchmark submissions have reproducible runs. |
| Internal evaluation | 3 | External validation: top-ranked on four agentic-research benchmarks; ICAIS 2025 peer-reviewed acceptance with multiple awards. |
| Openness | 3 | Apache-2.0; PyPI package; companion EvoSkills repo; multi-provider configuration. |
| Maturity / traction | 3 | 4.3k+ stars; 13 releases 2026-05→07 (v0.2.3, incl. v0.2.0 'Autonomy milestone'); PyPI package + evoscientist.ai site; sustained leaderboard performance; ICAIS 2025 recognition. |
| Cross-family policy | 1 | Multi-provider configuration (Anthropic, OpenAI, Google, MiniMax, NVIDIA) supports cross-family setups but no required policy. |
| Runtime assurance | 2 | Per-turn adaptive tool selection + context editing + 'More Effort' code-generation refinement loop provide moderate runtime gating; no published claim-audit harness comparable to ARIS or ARS. |
| Cross-platform portability | 3 | Framework-agnostic by design: CLI hub + Telegram + Slack + Feishu + WeChat + mobile; multi-provider config. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `hypothesis-generation` `literature-discovery` `literature-synthesis` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing`


**Architectural features:** `multi-agent` `human-in-loop` `tool-use` `rag-knowledge-base` `persistent-memory` `iterative-loop` `artifact-versioning`


**Inputs:** `research-direction` `prior-context`


**Outputs:** `research-report` `code` `paper-draft` `evolved-skills`


**Data sources:** `user-provided`


**Knowledge sources:** `mcp-servers` `evoskills`


## Limitations

- Benchmark dominance does not directly demonstrate methodological novelty of papers produced.
- Built on DeepAgents framework — architecture is layered, requires reading DeepAgents to fully audit.
- Skill quality varies across EvoSkills packs (community-contributed).

## Related projects in this catalog

- [`aris`](aris.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`autoresearchclaw`](autoresearchclaw.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`paper-qa`](paper-qa.md)

## Papers describing this project

- **EvoScientist Technical Report** — EvoScientist team (2026). *arXiv*. [arXiv:2603.08127](https://arxiv.org/abs/2603.08127)

## Also compared in

- **ARIS Table 4 (footnote 1)** ([`yang2026aris`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Noted as 'very recently' built; no detailed comparison.
- **AstaBench leaderboard** — Held #1 on Code & Execution + Data Analysis tracks at submission time.
- **DeepResearch Bench II leaderboard** — Held #1 at multiple submission windows.

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Park, J. S. et al. (2023). [*Generative Agents: Interactive Simulacra of Human Behavior*](../papers/notes/park2023generative.md) `park2023generative`
