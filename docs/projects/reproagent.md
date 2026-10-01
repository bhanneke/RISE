<!-- DO NOT EDIT — auto-generated from projects/landscape/reproagent.yml by scripts/build_indexes.py -->

# ReproAgent

`external` · status: `active` · focus: `replication` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/kernel-14/ReproAgent>

**Licence:** `MIT`

**Source:** [`projects/landscape/reproagent.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/reproagent.yml)

## Positioning

A contract-guided paper-to-code reproduction agent: given a research paper, a four-stage Prepare-Plan-Generate-Repair pipeline extracts implementation requirements, binds them to evidence from related repositories, and generates a dependency-ordered, repair-validated codebase. Sits in the RISE code-generation/replication layer alongside `paper2code`, `repro-bench`, and `core-bench`, evaluated directly on PaperBench Code-Dev.

## Distinctive contribution

Maintains a persistent "implementation contract" with two channels — an implementation-requirement channel (paper snippets to code obligations) and a reference-evidence channel (retrieved structure/content from related repos) — both projected into file-level contracts that are carried through generation and repair. On PaperBench Code-Dev it beats same-backbone baselines (BasicAgent, IterAgent, an AI-Scientist-style scaffold) under both Claude-Sonnet-4.5 and Gemini-3-Flash.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Declared stages are code-generation and replication only; no ideation, design, data-analysis, or write-up coverage. |
| Autonomy level | 3 | Runs the full Prepare-Plan-Generate-Repair pipeline end-to-end to produce a complete repository without per-step approval. |
| Architectural transparency | 3 | Full pipeline code, dual-channel contract implementation, and ablation-study runners published under MIT. |
| Inputs supported | 1 | Single input form (the paper itself); related-repo retrieval is an internal knowledge source, not a separate user-facing input. |
| Outputs / reproducibility | 2 | Produces a versioned generated repository with a coverage report; no accompanying data manifest or claim about full paper+data reproducibility. |
| Internal evaluation | 3 | Evaluated on the established external PaperBench Code-Dev benchmark and accepted to Findings of EMNLP 2026 — peer-reviewed external validation. |
| Openness | 2 | MIT license, pip-installable with documented quick-start; requires Gemini or Claude API credentials to run. |
| Maturity / traction | 1 | 2 stars / 0 forks, 7 commits as of scoring date; posted August 2026, single public evaluation study. |
| Cross-family policy | 1 | Demonstrated under two different model families (Claude-Sonnet-4.5 and Gemini-3-Flash) as interchangeable backbones, but not required by design. |
| Runtime assurance | 2 | Repair stage validates contract coverage and fixes gaps before completion — an in-pipeline gate beyond a single-pass generation. |
| Cross-platform portability | 1 | Supports at least two LLM backbones (Claude, Gemini); no evidence of broader runtime/IDE portability. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `code-generation` `replication`


**Architectural features:** `dag-orchestration` `iterative-loop` `tool-use`


**Inputs:** `research paper (PDF/text)`


**Outputs:** `executable code repository` `coverage/validation report`


**Knowledge sources:** `related code repositories (reference-evidence channel)`


## Limitations

- Generates code only; does not address missing data or model weights (untested on fully artifact-absent 'Reimplement'-style cases).
- Very young repository (2 stars, 7 commits); evaluated in a single published study (PaperBench Code-Dev) so far.
- ML/CS-specific; untested on economics/social-science replication workflows (e.g., Stata/R-based pipelines).

## Related projects in this catalog

- [`paper2code`](paper2code.md)
- [`repro-bench`](repro-bench.md)
- [`core-bench`](core-bench.md)
- [`reprorepo`](reprorepo.md)
- [`reclaim`](reclaim.md)
- [`researchclaw-bench`](researchclaw-bench.md)

## Papers describing this project

- **ReproAgent: Contract-Guided Paper-to-Code Reproduction** — Hu, X., Pan, Z., Wang, Z., Liu, Z., Su, Z., Zhang, W. (2026). *EMNLP 2026 Findings / arxiv*. [arXiv:2608.24291](https://arxiv.org/abs/2608.24291)
