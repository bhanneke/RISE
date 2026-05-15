<!-- DO NOT EDIT — auto-generated from projects/landscape/tooluniverse.yml by scripts/build_indexes.py -->

# ToolUniverse

`external` · status: `active` · focus: `end-to-end` · discipline: `biomedical` · started: 2025

**Project page:** <https://github.com/mims-harvard/ToolUniverse>

**Source:** [`projects/landscape/tooluniverse.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/tooluniverse.yml)

## Positioning

A curated tool registry and MCP server (arXiv:2509.23426) that packages biomedical, chemical, and general scientific APIs into a uniform agent-callable surface. Distributed as an MCP server, a Python SDK, and an agent-skills bundle; sits in the *infrastructure for RISE pipelines* layer, not as a pipeline itself.

## Distinctive contribution

Reframes the AI-scientist problem as an *interface* problem: scientific tools need to be discoverable, callable, and validable by agents through a uniform protocol. Backed by a Harvard lab and distributed via the MCP registry, making it a natural building block for downstream RISE systems.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Infrastructure layer; supports stages rather than implementing a pipeline itself. |
| Autonomy level | 2 | Supervised: agents invoke tools through the MCP server; user wires it into their pipeline. |
| Architectural transparency | 3 | Open under Apache-2.0; arXiv:2509.23426; full documentation site at zitniklab.hms.harvard.edu/ToolUniverse/. |
| Inputs supported | 3 | Tool catalog spans biomedical, chemical, and general scientific APIs; MCP + Python SDK + skill-bundle distribution. |
| Outputs / reproducibility | 2 | Tool calls are deterministic by the underlying APIs; pipeline-level reproducibility depends on the wrapping agent. |
| Internal evaluation | 2 | ArXiv paper validates the tool registry against scientific-agent benchmarks; broader uptake metrics public. |
| Openness | 3 | Apache-2.0; PyPI; MCP registry listing; community channels (Slack, WeChat). |
| Maturity / traction | 2 | 1.3k+ stars; Harvard institutional backing; recent and active (last push 2026-05). |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-acquisition` `literature-discovery`


**Architectural features:** `tool-use` `rag-knowledge-base`


**Inputs:** `tool-query`


**Outputs:** `tool-results`


**Data sources:** `biomedical-apis` `chemical-apis`


**Knowledge sources:** `biomedical-literature`


## Limitations

- Biomedical orientation; coverage for empirical economics, social sciences thin or absent.
- Infrastructure layer — value depends on the downstream agent system.
- Some tools wrap commercial APIs with rate limits or paid tiers.

## Related projects in this catalog

- [`paper-qa`](paper-qa.md)
- [`aviary`](aviary.md)
- [`robin`](robin.md)

## References

- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
