<!-- DO NOT EDIT — auto-generated from projects/landscape/open-coscientist.yml by scripts/build_indexes.py -->

# Open CoScientist Agents

`external` · status: `archived` · focus: `ideation` · discipline: `general` · started: 2025

**Project page:** <https://github.com/conradry/open-coscientist-agents>

**Source:** [`projects/landscape/open-coscientist.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/open-coscientist.yml)

## Positioning

An open-source implementation of Google DeepMind's *AI co-scientist* (arXiv:2502.18864), built on LangGraph and GPT Researcher. Realizes the co-scientist's multi-agent design — literature review, generation, reflection, evolution, meta-review, supervisor, and a tournament-style hypothesis competition with ELO ranking.

## Distinctive contribution

Makes a major closed industrial design (DeepMind's co-scientist) inspectable and runnable: every agent role and the ELO tournament loop are present in code, with a Streamlit dashboard for inspecting hypothesis competition transcripts. Useful as a reference implementation against which the original paper's claims can be audited.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Four upstream stages culminating in ranked hypotheses; no execution or drafting. |
| Autonomy level | 3 | Supervisor agent orchestrates the loop without per-step approval. |
| Architectural transparency | 3 | MIT-licensed; every agent role visible in source; references the original DeepMind paper. |
| Inputs supported | 2 | Research-goal inputs; multi-LLM (Gemini 2.5 Pro + Claude Sonnet 4 + o3) collaboration. |
| Outputs / reproducibility | 1 | Tournament transcripts persisted; LLM nondeterminism and live web search limit run-to-run determinism. |
| Internal evaluation | 1 | Demo-quality evaluation; tournament metrics are internal to the loop, not external validation. |
| Openness | 3 | MIT-licensed; reproducible setup with PyPI install path. |
| Maturity / traction | 1 | Confirmed still archived by the owner (archived 2026-04-14, read-only); 69 stars; last push 2025-07 — matches the entry's existing 'archived' status. |
| Cross-family policy | 3 | Requires Gemini 2.5 Pro + Claude Sonnet 4 + o3 in collaboration — explicitly multi-family by design. |
| Runtime assurance | 2 | ELO tournament + meta-review + reflection agents provide debate-based runtime gating. |
| Cross-platform portability | 1 | LangGraph + GPT-Researcher dependency; single Python entry. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `hypothesis-generation` `research-design`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base` `iterative-loop` `debate-consensus`


**Inputs:** `research-goal`


**Outputs:** `ranked-hypotheses` `tournament-transcripts` `research-report`


**Data sources:** `web-search`


**Knowledge sources:** `web-search` `gpt-researcher`


## Limitations

- Requires API keys from multiple commercial providers (Gemini + Anthropic + OpenAI) for the full design.
- Independent implementation; fidelity to the original DeepMind system is the implementer's best effort, not author-verified.
- Last push 2025-07.

## Related projects in this catalog

- [`researchagent`](researchagent.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`gpt-researcher`](gpt-researcher.md)

## Papers describing this project

- **Towards an AI co-scientist** — Gottweis, J., Weng, W.-H., Daryin, A., Tu, T., Palepu, A., Sirkovic, P., et al. (2025). *arXiv (Google DeepMind)*. [arXiv:2502.18864](https://arxiv.org/abs/2502.18864)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Park, J. S. et al. (2023). [*Generative Agents: Interactive Simulacra of Human Behavior*](../papers/notes/park2023generative.md) `park2023generative`
