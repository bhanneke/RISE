<!-- DO NOT EDIT — auto-generated from projects/landscape/researchagent.yml by scripts/build_indexes.py -->

# ResearchAgent (NAACL 2025)

`external` · status: `dormant` · focus: `ideation` · discipline: `general` · started: 2025

**Project page:** <https://github.com/JinheonBaek/ResearchAgent>

**Source:** [`projects/landscape/researchagent.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/researchagent.yml)

## Positioning

The NAACL 2025 reference implementation (arXiv:2404.07738) of *iterative research idea generation over scientific literature*. Starting from a core paper, the system retrieves related work and entities, proposes a research problem, and refines it via parallel multi-criteria reviews from LLM reviewer agents.

## Distinctive contribution

Among the earliest peer-reviewed treatments of agentic ideation *grounded in literature*, with an explicit multi-reviewer feedback loop and a paper+entity knowledge store. Useful as a methodological reference for the catalog's ideation-focused projects rather than as a turnkey product.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Four upstream stages (lit discovery → research design); no analysis, drafting, or review of papers. |
| Autonomy level | 2 | Supervised: user supplies seed paper IDs and knowledge store; system iterates autonomously. |
| Architectural transparency | 3 | NAACL 2025 paper; code structure documented in README; per-agent prompts visible in source. |
| Inputs supported | 2 | Semantic Scholar paper IDs + a knowledge store mined offline; relies on S2 Graph API. |
| Outputs / reproducibility | 2 | Code + paper experiments runnable; LLM nondeterminism affects byte-level reproducibility. |
| Internal evaluation | 2 | Multi-criteria reviewer evaluation built into the loop; broader external evaluation reported in the NAACL paper. |
| Openness | 1 | Code is public but no declared open-source license — reuse rights are uncertain. |
| Maturity / traction | 1 | 37 stars; published-paper artifact with limited community uptake; last push 2025-08. |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `rq-formulation` `hypothesis-generation` `research-design`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base` `iterative-loop`


**Inputs:** `seed-paper-ids` `knowledge-store`


**Outputs:** `research-problem` `method-proposal` `experiment-design` `review-scores`


**Data sources:** `semantic-scholar`


**Knowledge sources:** `semantic-scholar` `extracted-entities`


## Limitations

- No declared open-source license.
- Single-developer maintenance; semi-active.
- Knowledge store must be pre-mined offline — not a turnkey deployment.

## Related projects in this catalog

- [`agent-laboratory`](agent-laboratory.md)
- [`open-coscientist`](open-coscientist.md)
- [`e2er`](e2er.md)

## Papers describing this project

- **ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models** — Baek, J., Jauhar, S. K., Cucerzan, S., Hwang, S. J. (2024). *NAACL 2025 (arXiv)*. [arXiv:2404.07738](https://arxiv.org/abs/2404.07738)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
