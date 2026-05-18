<!-- DO NOT EDIT — auto-generated from projects/landscape/aris.yml by scripts/build_indexes.py -->

# ARIS (Auto-Research-In-Sleep)

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep>

**Source:** [`projects/landscape/aris.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/aris.yml)

## Positioning

An open-source research harness for autonomous ML research (arXiv:2605.03042) built around *cross-model adversarial collaboration*: an executor model drives forward progress while a reviewer from a different model family critiques intermediate artifacts and requests revisions. Ships as 74+ Markdown-only `SKILL.md` files plus an optional standalone CLI (ARIS-Code), with the explicit design stance that the harness is a *methodology*, not a platform, portable across Claude Code, Codex CLI, Cursor, Trae, Antigravity, Copilot CLI, OpenClaw, Windsurf, and custom agents.

## Distinctive contribution

Treats *long-running plausible-unsupported-success* as the central failure mode of autonomous research and addresses it by mandating cross-model review as the default (executor and reviewer from different model families, e.g., Claude Code + Codex MCP at GPT-5.4 xhigh, or MiniMax-M2.7 + GLM-5). Three-stage evidence verification, five-pass scientific editing pipeline, mathematical-proof checks, visual PDF inspection, and a persistent *Research Wiki* (papers / ideas / experiments / claims + relationship graph). Notably most- starred (9.8k+) Claude-Code-native research harness in the catalog.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | 11 stages including rebuttal mode (responses to reviewer comments) and conference-talk pipeline. |
| Autonomy level | 3 | 'Wake up to find your paper scored, weaknesses identified, experiments run, and narrative rewritten.' |
| Architectural transparency | 3 | Open under MIT; arXiv technical report (2605.03042); every skill is plain Markdown; AGENT_GUIDE.md for LLM consumption. |
| Inputs supported | 3 | Multiple modes (basic, targeted-improvement with `ref paper` + `base repo`, rebuttal); 5 workflows; broad provider support. |
| Outputs / reproducibility | 2 | Persistent Research Wiki + per-project artifacts; non-determinism intrinsic to LLM execution. |
| Internal evaluation | 3 | Cross-model adversarial review IS the evaluation harness; three-stage evidence verification + claim audit + math-proof checks + visual PDF inspection; 5-round Codex MCP cross-review reported in v0.4.11 release notes. |
| Openness | 3 | MIT-licensed; pure-Markdown skills (no framework lock-in); standalone CLI; multi-IDE adaptations documented; supports free-tier ModelScope path. |
| Maturity / traction | 3 | 9.8k+ stars, Hugging Face Daily Paper #1, featured in awesome-agent-skills, 7-release polish sequence in May 2026; active community. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `hypothesis-generation` `literature-discovery` `literature-synthesis` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `multi-agent` `debate-consensus` `human-in-loop` `tool-use` `rag-knowledge-base` `persistent-memory` `iterative-loop` `artifact-versioning`


**Inputs:** `research-direction` `prior-paper` `base-repo` `reviewer-comments`


**Outputs:** `paper` `code` `figures` `rebuttal` `slides` `research-wiki`


**Data sources:** `user-provided`


**Knowledge sources:** `arxiv` `semantic-scholar` `openalex` `research-wiki`


## Limitations

- ML-research orientation; portability to empirical economics or biomedical research requires skill rewriting.
- Cross-model design requires keys for two model families; single-key fallback exists but degrades the adversarial property.
- Long histories (Research Wiki) can grow large — periodic compaction is the user's responsibility.
- ARIS-Code CLI is Rust-based and binary-distributed; auditing the runtime requires reading non-trivial code.

## Related projects in this catalog

- [`e2er`](e2er.md)
- [`clo-author`](clo-author.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`zeropaper`](zeropaper.md)

## Papers describing this project

- **ARIS: Autonomous Research via Adversarial Multi-Agent Collaboration** — Yang, R., Li, Y., Li, S. (2026). *arXiv*. [arXiv:2605.03042](https://arxiv.org/abs/2605.03042)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
- Ji, Z. et al. (2023). [*Survey of Hallucination in Natural Language Generation*](../papers/notes/ji2023hallucination.md) `ji2023hallucination`
- `matton2025walkthetalk` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
