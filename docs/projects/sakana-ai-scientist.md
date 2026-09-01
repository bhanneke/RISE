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
| Internal evaluation | 3 | External validation: a v2-generated manuscript passed workshop-level human peer review (ICLR 2025 ICBINB, avg. score 6.33); the underlying research was subsequently peer-reviewed and published in Nature 651, 914-919 (26 Mar 2026). |
| Openness | 1 | Relicensed Dec 2025 from permissive terms to the custom 'AI Scientist Source Code License v1.0' (based on the Responsible AI Source Code License, confirmed in this repo's LICENSE) — a non-permissive, restriction-bearing license (mandatory AI-disclosure clause, use restrictions, termination-on-violation). |
| Maturity / traction | 3 | 7.1k+ stars; multiple iterations (v1 → v2); capstone research published in Nature (Mar 2026), satisfying the 'citations'/production-adoption band. |
| Cross-family policy | 0 | Same-model self-refinement is the canonical failure mode ARIS Table 4 identifies in this lineage. |
| Runtime assurance | 1 | Agentic tree search + self-review pass provide light runtime gating. |
| Cross-platform portability | 0 | Linux + NVIDIA GPU locked; single-template runtime. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

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
- Non-permissive license (AI Scientist Source Code License v1.0, Dec 2025), unlike the permissive license this project shipped under previously.

## Related projects in this catalog

- [`e2er`](e2er.md)
- [`zeropaper`](zeropaper.md)

## Papers describing this project

- **The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search** — Yamada, Y., Lange, R. T., Lu, C., Hu, S., Lu, C., Foerster, J., et al. (2025). *arXiv*. [arXiv:2504.08066](https://arxiv.org/abs/2504.08066)
- **Towards end-to-end automation of AI research** — Lu, C., Lange, R. T., Yamada, Y., Hu, S., Foerster, J., Ha, D., Clune, J. (2026). *Nature*. [arXiv:2606.15497](https://arxiv.org/abs/2606.15497) · [doi](https://doi.org/10.1038/s41586-026-10265-5)

## Also compared in

- **ARIS Table 4** ([`yang2026aris`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Same scoring profile as v1 in Table 4; noted as workshop-level paper produced via agentic tree search.
- **A Survey of AI Scientists** ([`tie2025aiscientistsurvey`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib)) — Covered as the v2 release of the foundational AI-scientist line.

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
- Schick, T. et al. (2023). [*Toolformer: Language Models Can Teach Themselves to Use Tools*](../papers/notes/schick2023toolformer.md) `schick2023toolformer`
