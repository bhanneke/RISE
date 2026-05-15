<!-- DO NOT EDIT — auto-generated from projects/landscape/kosmos.yml by scripts/build_indexes.py -->

# Kosmos (jimmc414 implementation)

`external` · status: `research-prototype` · focus: `end-to-end` · discipline: `general` · started: 2025

**Project page:** <https://github.com/jimmc414/Kosmos>

**Source:** [`projects/landscape/kosmos.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/kosmos.yml)

## Positioning

An open-source implementation of the Kosmos AI scientist architecture (Lu et al., arXiv:2511.02824), adapted to run via Claude Code or the Anthropic / OpenAI APIs. Runs autonomous research cycles: hypothesis generation, experiment design, code execution in sandboxed Docker, validation against an 8-dimension quality framework, and knowledge-graph construction.

## Distinctive contribution

Operationalizes the Kosmos architecture as a runnable system on commodity infrastructure, including a built-in 8-dimension validation harness and an explicit knowledge-graph layer that tracks concept relationships across cycles. The validation framework is independently reusable as a methodological scaffold.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Four stages from ideation through analysis; no paper drafting or review. |
| Autonomy level | 3 | Autonomous research cycles by design. |
| Architectural transparency | 3 | Open implementation; references the source paper (arXiv:2511.02824); 3700+ tests reported in repo. |
| Inputs supported | 2 | Research-area + data inputs; Anthropic or OpenAI back-ends; Docker-sandboxed execution. |
| Outputs / reproducibility | 2 | Knowledge graph + validated-discovery artifacts persisted; cycle outputs deterministic given fixed inputs and model. |
| Internal evaluation | 2 | Built-in 8-dimension quality framework; broader external evaluation pending. |
| Openness | 1 | Source public but no declared license in repo metadata — reuse rights uncertain. |
| Maturity / traction | 2 | 511 stars; alpha-stage release; active community uptake post-Kosmos paper. |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base` `persistent-memory` `iterative-loop` `artifact-versioning`


**Inputs:** `research-area` `data`


**Outputs:** `hypotheses` `experiment-results` `knowledge-graph` `validated-discoveries`


**Data sources:** `user-provided`


**Knowledge sources:** `literature` `knowledge-graph`


## Limitations

- No declared open-source license.
- Alpha-stage; expect breaking changes.
- Code-execution without Docker falls back to `exec()` with static validation — security caveat in README.
- Implements an architecture from a third-party paper; not a primary research artifact.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`sakana-ai-scientist-v1`](sakana-ai-scientist-v1.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`robin`](robin.md)

## Papers describing this project

- **Kosmos: An AI Scientist for Autonomous Discovery** — Mitchener, L., Yiu, A., Chang, B., Bourdenx, M., Nadolski, T., Sulovari, A., et al. (2025). *arXiv*. [arXiv:2511.02824](https://arxiv.org/abs/2511.02824)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Park, J. S. et al. (2023). [*Generative Agents: Interactive Simulacra of Human Behavior*](../papers/notes/park2023generative.md) `park2023generative`
