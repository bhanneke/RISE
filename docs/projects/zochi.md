<!-- DO NOT EDIT — auto-generated from projects/landscape/zochi.yml by scripts/build_indexes.py -->

# Zochi (Intology)

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2025

**Project page:** <https://github.com/IntologyAI/Zochi>

**Source:** [`projects/landscape/zochi.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/zochi.yml)

## Positioning

An end-to-end "artificial scientist" system from Intology, claimed to span hypothesis generation through to peer-reviewed publication. Differentiates itself from earlier AI-scientist releases by publishing the *outputs* — accepted ACL 2025 and ICLR 2025 workshop papers (CS-ReFT, Tempest/Siege) with reported state-of-the-art results — rather than only the pipeline.

## Distinctive contribution

The strongest *external-validation* claim in the AI-scientist landscape: peer-reviewed acceptances of papers produced by the system, including ACL 2025 main proceedings. The repository releases code and a technical report covering an earlier version of the system.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Seven stages from hypothesis through review; full lifecycle in claimed scope. |
| Autonomy level | 3 | Autonomous end-to-end discovery is the stated design target. |
| Architectural transparency | 2 | Public repository covers earlier version; current capabilities described in blog posts; full current pipeline not open. |
| Inputs supported | 2 | Research-area inputs with optional dataset; commercial back-end at intology.ai. |
| Outputs / reproducibility | 2 | Published papers + benchmark code; full system reproduction depends on current closed components. |
| Internal evaluation | 3 | External peer review at ACL 2025 + ICLR 2025 workshops — strongest external validation in the catalog. |
| Openness | 2 | MIT-licensed code for earlier version; current system features are commercial. |
| Maturity / traction | 2 | 305 stars; commercial backing (Intology); credible publication trajectory. |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `artifact-versioning`


**Inputs:** `research-area`


**Outputs:** `paper-draft` `code` `experiment-results`


**Data sources:** `benchmark-datasets`


**Knowledge sources:** `literature`


## Limitations

- Public code lags the current capabilities described in marketing — current pipeline is not fully open.
- Validation is via specific peer-reviewed papers; cross-domain generality is asserted but not separately tested.
- Last push 2025-11; the open repository may not reflect the live system.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`sakana-ai-scientist-v1`](sakana-ai-scientist-v1.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`e2er`](e2er.md)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- `gartenberg2026morebetter` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
