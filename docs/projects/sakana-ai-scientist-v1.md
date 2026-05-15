<!-- DO NOT EDIT — auto-generated from projects/landscape/sakana-ai-scientist-v1.yml by scripts/build_indexes.py -->

# Sakana AI Scientist (v1)

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2024

**Project page:** <https://github.com/SakanaAI/AI-Scientist>

**Source:** [`projects/landscape/sakana-ai-scientist-v1.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/sakana-ai-scientist-v1.yml)

## Positioning

The original AI Scientist release (arXiv:2408.06292): an end-to-end agentic pipeline that ideates, runs experiments, and writes a paper with self-review on a fixed set of CS templates (NanoGPT, 2D Diffusion, Grokking). Foundational reference for the AI-scientist line and direct predecessor to v2.

## Distinctive contribution

First widely-noticed system to demonstrate a complete machine-learning paper produced autonomously by an LLM pipeline, including in-pipeline reviewer simulation. Released with example papers and per-template scaffolds, making the line of work concrete and inspectable.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Seven stages from ideation through self-review; no literature-synthesis or external dissemination stage. |
| Autonomy level | 3 | Runs end-to-end without per-step human approval; user supplies a template and topic. |
| Architectural transparency | 3 | Code, prompts, templates, and example outputs publicly released; arXiv paper documents the design. |
| Inputs supported | 1 | Narrow input form (area + curated template); limited external data integration. |
| Outputs / reproducibility | 2 | Papers + code + logs persisted; reproducibility tied to the seeded template. |
| Internal evaluation | 2 | Self-review pass and qualitative evaluation in the arXiv paper; external evaluations of output quality are mixed. |
| Openness | 2 | Open source under a non-OSI 'Other' license (verify terms before reuse); requires Linux + NVIDIA GPU. |
| Maturity / traction | 3 | 13k+ stars, peer attention, basis for follow-up systems and the v2 release. |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `artifact-versioning`


**Inputs:** `research-area` `template`


**Outputs:** `paper-pdf` `code` `experiment-logs` `llm-generated-review`


**Data sources:** `template-datasets`


**Knowledge sources:** `semantic-scholar`


## Limitations

- Locked to three CS templates; portability to other domains community-maintained.
- Self-review correlates weakly with external peer-review judgments.
- Non-permissive license; requires Linux + NVIDIA GPU + texlive-full.
- Executes LLM-written code; security/containment is the user's responsibility.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`zeropaper`](zeropaper.md)
- [`e2er`](e2er.md)

## References

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
