<!-- DO NOT EDIT — auto-generated from projects/landscape/autoresearchclaw.yml by scripts/build_indexes.py -->

# AutoResearchClaw

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/aiming-lab/AutoResearchClaw>

**Source:** [`projects/landscape/autoresearchclaw.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/autoresearchclaw.yml)

## Positioning

An autonomous research pipeline taking a chat-level idea to a full paper via ACP-compatible agent back-ends (Claude Code, Codex CLI, Copilot CLI, Gemini CLI, Kimi CLI). Ships v0.4.0+ with a Human-in-the-Loop Co-Pilot system offering 6 intervention modes (`full-auto` / `gate-only` / `checkpoint` / `step-by-step` / `co-pilot` / `custom`), 19 pre-loaded skills, anti-fabrication VerifiedRegistry, and CLI commands for attaching to / approving / redirecting in-flight pipelines.

## Distinctive contribution

Among the largest user communities in the catalog (12.3k stars, multi-language localizations covering 9 languages + Discord community). The HITL co-pilot system with 6 explicit intervention modes is the most differentiated human-oversight surface among the end-to-end pipelines — and the anti-fabrication system (VerifiedRegistry + experiment diagnosis & repair loop) is a named runtime-assurance component, not an evaluation afterthought.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Nine stages including referee simulation; explicit dissemination support via OpenClaw integration. |
| Autonomy level | 2 | User-selectable: full-auto through co-pilot. After v0.4.0 HITL launch, the design centers on partial autonomy rather than fully autonomous default. |
| Architectural transparency | 2 | Open MIT; v0.4.0 HITL guide documents the 6 intervention modes; some agent internals require source dive. |
| Inputs supported | 3 | Multiple inputs (idea, prior paper, existing results); 5+ ACP-compatible back-ends; messaging-platform integration via OpenClaw bridge. |
| Outputs / reproducibility | 2 | Per-project workspaces; experiment diagnosis & repair loop; 2699 tests passing — but not bitwise-deterministic by design. |
| Internal evaluation | 2 | Anti-fabrication VerifiedRegistry, paper showcase across 8 domains, active testing program; no published peer-reviewed evaluation paper at this scoring date. |
| Openness | 3 | MIT-licensed; multi-language documentation; active Discord community; community-contributed skill ecosystem. |
| Maturity / traction | 3 | 13.8k+ stars; regular releases (v0.5.0 2026-05-20, active through 2026-07); companion paper claims +54.7% over AI Scientist v2 on ARC-Bench. |
| Cross-family policy | 1 | Multiple back-ends (Claude/Codex/Copilot/Gemini/Kimi CLI) make cross-family configurations easy, but no required cross-family review policy in the architecture. |
| Runtime assurance | 3 | Anti-fabrication system (VerifiedRegistry + experiment diagnosis & repair loop), SmartPause (confidence-driven dynamic intervention), ALHF intervention learning, cost budget guardrails. |
| Cross-platform portability | 3 | 5+ CLI back-ends (Claude Code, Codex CLI, Copilot CLI, Gemini CLI, Kimi CLI) + 4 messaging platforms (Discord, Telegram, Lark, WeChat) via OpenClaw bridge. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `literature-discovery` `literature-synthesis` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `human-in-loop` `tool-use` `rag-knowledge-base` `persistent-memory` `iterative-loop` `artifact-versioning`


**Inputs:** `research-idea` `prior-paper` `existing-results`


**Outputs:** `paper` `code` `figures` `experiment-logs`


**Data sources:** `user-provided`


**Knowledge sources:** `arxiv` `literature` `mcp-servers`


## Limitations

- Ethics-and-responsible-use guidelines added 2026-04; the autonomous-default era leaves a legacy of misuse risk.
- No peer-reviewed publication describing the system at this scoring date.
- Heavy aspirational marketing ('Chat an Idea. Get a Paper.') sets a higher bar than the showcase examples meet.
- Single-organization maintenance (Aiming Lab); long-term governance unclear.

## Related projects in this catalog

- [`aris`](aris.md)
- [`evoscientist`](evoscientist.md)
- [`clo-author`](clo-author.md)
- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`academic-research-skills`](academic-research-skills.md)

## Papers describing this project

- **AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration** — Liu, J., Qiu, S., Li, M., Li, B., Ji, H., et al. (2026). *arXiv*. [arXiv:2605.20025](https://arxiv.org/abs/2605.20025)

## Also compared in

- **ARIS Table 4 (footnote 1)** ([`yang2026aris`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Noted as 'very recently' built; no detailed comparison.

## Related references (literature catalog)

- Liu, J. et al. (2026). [*AutoResearchClaw: Self-Reinforcing Autonomous Research with Human-AI Collaboration*](../papers/notes/liu2026autoresearchclaw.md) `liu2026autoresearchclaw`
- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
- Ji, Z. et al. (2023). [*Survey of Hallucination in Natural Language Generation*](../papers/notes/ji2023hallucination.md) `ji2023hallucination`
