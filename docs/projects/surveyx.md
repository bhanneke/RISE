<!-- DO NOT EDIT — auto-generated from projects/landscape/surveyx.yml by scripts/build_indexes.py -->

# SurveyX

`external` · status: `active` · focus: `literature` · discipline: `general` · started: 2025

**Project page:** <https://github.com/IAAR-Shanghai/SurveyX>

**Source:** [`projects/landscape/surveyx.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/surveyx.yml)

## Positioning

An academic survey-automation system (arXiv:2502.14776) that generates domain-specific surveys from a paper title plus retrieval keywords. Open-source repository ships only the offline processing path; full-version capabilities (real-time online search, multimodal parsing) are gated behind the hosted surveyx.cn service.

## Distinctive contribution

Two-tier deployment — an open offline pipeline plus a commercial online service — making the field's tension between research reproducibility and product gating explicit. The offline release is usable as a methodological baseline.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three stages around literature synthesis and drafting. |
| Autonomy level | 3 | Runs from title + keywords to survey; offline version is autonomous given the reference set. |
| Architectural transparency | 2 | arXiv:2502.14776 documents the method; offline code is public; online crawler + paper-DB system are closed. |
| Inputs supported | 1 | Open version: user-uploaded Markdown references only. Full feature set requires the hosted service. |
| Outputs / reproducibility | 1 | Open path is reproducible given user-supplied references; hosted-service runs are not. |
| Internal evaluation | 2 | ArXiv paper reports comparative evaluation; the hosted-service variant has not been independently audited. |
| Openness | 1 | No declared license in repository metadata; substantial functionality reserved for the commercial service. |
| Maturity / traction | 2 | 970 stars; active development; live hosted service at surveyx.cn. |

*Scored on 2026-05-15. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `paper-drafting`


**Architectural features:** `multi-agent` `rag-knowledge-base` `iterative-loop`


**Inputs:** `survey-title` `keywords` `reference-markdown`


**Outputs:** `long-form-survey` `citations`


**Data sources:** `user-provided-markdown`


**Knowledge sources:** `user-provided`


## Limitations

- Open-source release deliberately omits the most capability-relevant components (crawler, paper DB, multimodal parser).
- No declared open-source license.
- Output quality on the open path depends entirely on the references the user supplies.

## Related projects in this catalog

- [`autosurvey`](autosurvey.md)
- [`storm`](storm.md)
- [`open-scholar`](open-scholar.md)

## Papers describing this project

- **SurveyX: Academic Survey Automation via Large Language Models** — Liang, X., Yang, J., Wang, Y., Tang, C., Zheng, Z., Song, S., et al. (2025). *arXiv*. [arXiv:2502.14776](https://arxiv.org/abs/2502.14776)

## Related references (literature catalog)

- Wu, J. et al. (2025). [*Agentic Reasoning: A Streamlined Framework for Enhancing LLM Reasoning with Agentic Tools*](../papers/notes/wu2025agenticreasoning.md) `wu2025agenticreasoning`
