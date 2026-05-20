<!-- DO NOT EDIT — auto-generated from projects/landscape/reviewer.yml by scripts/build_indexes.py -->

# Reviewer (Ingar30)

`external` · status: `active` · focus: `review` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/Ingar30/reviewer>

**Source:** [`projects/landscape/reviewer.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/reviewer.yml)

## Positioning

A reproducible multi-agent reviewer for academic economics papers. Takes a PDF as input, runs a fixed set of mandatory reviewers plus dynamically-selected optional reviewers, validates their JSON output against schemas, deduplicates findings, and assembles a final editor report. Sits firmly in the referee-simulation stage of the RISE pipeline.

## Distinctive contribution

Treats peer review as a structured engineering problem with explicit schemas, validation, parser-quality preflight, and editor-bundle assembly — distinguishing itself from chat-style review assistants. Reviewer prompts and orchestration are open and reproducible; review outputs are kept private by default.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage (referee simulation). |
| Autonomy level | 2 | Supervised: user provides a PDF and receives a final editor report. |
| Architectural transparency | 3 | Open source under MIT; reviewer prompts, schemas, validation, and orchestration all in the repo. |
| Inputs supported | 1 | Accepts paper PDFs; no integration of external literature corpora at present. |
| Outputs / reproducibility | 2 | Schema-validated reviewer JSON and structured editor report persisted; deterministic given fixed model + prompts. |
| Internal evaluation | 1 | Smoke checks on report structure and traceability; no published systematic benchmark yet. |
| Openness | 3 | MIT-licensed; setup scripts for Windows and macOS/Linux; reproducible workflow. |
| Maturity / traction | 1 | Very new (initialized 2026-05-14); single-developer research prototype. |
| Cross-family policy | 0 | Single-family (Codex CLI); reviewer agents within one model family. |
| Runtime assurance | 2 | Parser-quality preflight + schema validation + smoke checks gate the editor report; no claim-audit pass. |
| Cross-platform portability | 0 | Codex-CLI-locked; Windows + macOS/Linux setup scripts but single agent framework. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation`


**Architectural features:** `multi-agent` `dag-orchestration` `tool-use` `artifact-versioning`


**Inputs:** `submitted-paper-pdf`


**Outputs:** `editor-report` `reviewer-json` `parser-artifacts`


## Limitations

- Single-stage tool (review only); requires upstream paper provenance.
- Economics-paper focused; portability to other disciplines untested.
- Depends on Codex CLI; not a fully local solution.
- Source PDFs and review outputs are private by design; no shared evaluation corpus.

## Related projects in this catalog

- [`ape`](ape.md)
- [`e2er`](e2er.md)

## Related references (literature catalog)

- Gartenberg, C. et al. (2026). [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](../papers/notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`
- Naddaf, M. (2025). [*AI Is Transforming Peer Review — and Many Scientists Are Worried*](../papers/notes/naddaf2025aipeer.md) `naddaf2025aipeer`
- Goldberg, A. et al. (2024). [*Usefulness of LLMs as an Author Checklist Assistant for Scientific Papers: NeurIPS'24 Experiment*](../papers/notes/neurips2024checklist.md) `neurips2024checklist`
