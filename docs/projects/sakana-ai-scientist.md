<!-- DO NOT EDIT — auto-generated from projects/landscape/sakana-ai-scientist.yml by scripts/build_indexes.py -->

# Sakana AI Scientist v2

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2024

**Project page:** <https://github.com/SakanaAI/AI-Scientist-v2>

**Source:** [`projects/landscape/sakana-ai-scientist.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/sakana-ai-scientist.yml)

## Positioning

An autonomous "AI scientist" pipeline that ideates, runs experiments (primarily ML), drafts a paper, and self-reviews. Targets the full RISE arc end-to-end with minimal human oversight per task.

## Distinctive contribution

Among the earliest publicly released systems to demonstrate a single agentic pipeline producing complete machine-learning papers (idea → experiments → write-up → self-review) without per-step human intervention.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Covers ~7 stages; weak on literature discovery/synthesis and external dissemination. |
| Autonomy level | 3 | Runs end-to-end without per-task human approval. |
| Architectural transparency | 3 | Code, prompts, and configurations publicly released. |
| Inputs supported | 1 | Narrow input form (research area + template); limited external data integration. |
| Outputs / reproducibility | 2 | Persists papers + code + experiment logs; reproducibility depends on the seeded template. |
| Internal evaluation | 2 | Self-review pass and reported metrics on generated papers; external validation contested. |
| Openness | 3 | Open source under permissive license. |
| Maturity / traction | 2 | Released, widely discussed, multiple iterations (v1 → v2). |

*Scored on 2026-05-14. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `artifact-versioning`


**Inputs:** `research-area` `seed-template`


**Outputs:** `paper-draft` `code` `experiment-logs` `self-review`


**Data sources:** `benchmark-datasets`


**Knowledge sources:** `semantic-scholar` `openreview`


## Limitations

- ML-paper focus; portability to non-CS domains unclear.
- Quality of produced papers strongly dependent on seed templates.
- Self-review is not a substitute for external peer review.

## Related projects in this catalog

- [`e2er`](e2er.md)
- [`zeropaper`](zeropaper.md)

## References

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
