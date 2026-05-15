<!-- DO NOT EDIT — auto-generated from projects/landscape/gpt-researcher.yml by scripts/build_indexes.py -->

# GPT Researcher

`external` · status: `active` · focus: `literature` · discipline: `general` · started: 2023

**Project page:** <https://github.com/assafelovic/gpt-researcher>

**Source:** [`projects/landscape/gpt-researcher.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/gpt-researcher.yml)

## Positioning

An autonomous "deep research" agent that produces long-form, cited reports on any topic from web and local sources. Uses a planner + parallel execution-agent architecture inspired by Plan-and-Solve and RAG; outputs reports of 2,000+ words with smart image scraping and inline image generation.

## Distinctive contribution

Earliest and most-adopted general-purpose deep-research agent; the planner/executor split with parallelized sub-queries set the reference pattern that several later systems adopted. Distributed as a pip package, Claude Skill, Docker image, and Colab notebook.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Four pre-writing + drafting stages; no analysis, formal modeling, or review. |
| Autonomy level | 3 | Runs end-to-end from a research query; no per-step approval required. |
| Architectural transparency | 3 | Open source under Apache-2.0; planner/executor pattern documented; modular configuration. |
| Inputs supported | 2 | Query + optional local documents; multiple LLM and retrieval back-ends supported. |
| Outputs / reproducibility | 2 | Pip-installable, Docker image, Colab; outputs depend on live web state — not bitwise reproducible. |
| Internal evaluation | 1 | Demonstration-quality evaluation; no rigorous benchmark in the README at this scoring date. |
| Openness | 3 | Apache-2.0; broad distribution; active community. |
| Maturity / traction | 3 | 27k+ stars, regular releases, Claude Skill integration, large Discord community. |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `literature-discovery` `literature-synthesis` `paper-drafting`


**Architectural features:** `multi-agent` `tool-use` `rag-knowledge-base` `iterative-loop`


**Inputs:** `research-query` `local-documents`


**Outputs:** `long-form-report` `citations` `inline-images`


**Data sources:** `web-search` `user-provided-documents`


**Knowledge sources:** `web-search`


## Limitations

- Optimized for general-purpose research; not tuned for academic-rigor outputs (no method/identification awareness).
- Output reproducibility depends on live web state.
- No formal evaluation against academic-quality benchmarks reported.

## Related projects in this catalog

- [`storm`](storm.md)
- [`paper-qa`](paper-qa.md)
- [`open-scholar`](open-scholar.md)

## References

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
