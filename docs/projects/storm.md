<!-- DO NOT EDIT — auto-generated from projects/landscape/storm.yml by scripts/build_indexes.py -->

# STORM / Co-STORM

`external` · status: `active` · focus: `literature` · discipline: `general` · started: 2024

**Project page:** <https://github.com/stanford-oval/storm>

**Source:** [`projects/landscape/storm.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/storm.yml)

## Positioning

An LLM-powered knowledge-curation system that writes Wikipedia-style long-form articles from web search. STORM uses perspective-guided question asking and simulated conversations between a writer and a topic expert; Co-STORM (EMNLP 2024) adds a collaborative discourse protocol with human-in-the-loop and a dynamic mind map.

## Distinctive contribution

Treats the *pre-writing* problem (deciding what questions to ask) as the central bottleneck of automated long-form writing, and operationalizes it via perspective discovery and simulated expert dialogue. Co-STORM further makes the human–LLM curation loop a first-class architectural element.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three stages clustered around the pre-writing + drafting block; no analysis, modeling, or review. |
| Autonomy level | 2 | Supervised in STORM (topic → article); Co-STORM adds collaborative human steering. |
| Architectural transparency | 3 | Open under MIT; modular interfaces; two arXiv papers (NAACL 2024 + EMNLP 2024) document the design. |
| Inputs supported | 2 | Single input form (topic) but multiple retrieval back-ends: Bing, You.com, custom vector store. |
| Outputs / reproducibility | 2 | Pip-installable `knowledge-storm` package; outputs are deterministic given the retrieval back-end and model. |
| Internal evaluation | 2 | Both papers report systematic evaluations against baselines and Wikipedia editors. |
| Openness | 3 | MIT-licensed, pip-installable, demo site, public papers. |
| Maturity / traction | 3 | 28k+ stars, live research preview with 70k+ users, integrated into multiple downstream projects. |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `paper-drafting`


**Architectural features:** `multi-agent` `human-in-loop` `tool-use` `rag-knowledge-base` `iterative-loop`


**Inputs:** `topic`


**Outputs:** `long-form-article` `citations` `mind-map`


**Data sources:** `web-search` `user-provided-documents`


**Knowledge sources:** `bing-search` `you-search` `vector-rm`


## Limitations

- Stated explicitly by authors: output is not publication-ready and requires significant editing.
- Focused on Wikipedia-style synthesis; not designed to generate novel research.
- Quality dependent on search back-end coverage.

## Related projects in this catalog

- [`gpt-researcher`](gpt-researcher.md)
- [`open-scholar`](open-scholar.md)
- [`paper-qa`](paper-qa.md)

## References

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
