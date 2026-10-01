<!-- DO NOT EDIT — auto-generated from projects/landscape/kosmos.yml by scripts/build_indexes.py -->

# Kosmos (jimmc414 implementation)

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2025

**Project page:** <https://github.com/jimmc414/Kosmos>

**Licence:** `MIT (stated in README; no licence file)`

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
| Openness | 1 | Source public; the README states MIT, but there is no LICENSE file and the GitHub API reports none (checked 2026-09-29), so the grant rests on the README alone. |
| Maturity / traction | 2 | ~590 stars (up from 511); alpha-stage release (0.2.0-alpha); active community uptake post-Kosmos paper, with continued commits and open issue engagement into Q4 2026. |
| Cross-family policy | 1 | Anthropic or OpenAI API back-ends — cross-family possible by config. |
| Runtime assurance | 2 | Built-in 8-dimension quality framework + knowledge-graph consistency checks + sandboxed Docker execution. |
| Cross-platform portability | 1 | Anthropic or OpenAI; single agent framework. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

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

## Also compared in

- **A Survey of AI Scientists** ([`tie2025aiscientistsurvey`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Covered as an autonomous-discovery system.

## Related references (literature catalog)

- Mitchener, L. et al. (2025). [*Kosmos: An AI Scientist for Autonomous Discovery*](../papers/notes/mitchener2025kosmos.md) `mitchener2025kosmos`
- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Park, J. S. et al. (2023). [*Generative Agents: Interactive Simulacra of Human Behavior*](../papers/notes/park2023generative.md) `park2023generative`
