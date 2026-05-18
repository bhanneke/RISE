<!-- DO NOT EDIT — auto-generated from projects/landscape/refine-ink.yml by scripts/build_indexes.py -->

# Refine (refine.ink)

`external` · status: `active` · focus: `review` · discipline: `general` · started: 2026

**Project page:** <https://www.refine.ink/>

**Source:** [`projects/landscape/refine-ink.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/refine-ink.yml)

## Positioning

A commercial AI peer-review service that produces reviewer-grade feedback on academic papers within ~20–40 minutes by running multi-hour parallel compute jobs (~2+ hours per review). Targets four error classes: accuracy (statistical / methodological), mathematical reasoning (proof gaps, edge cases), internal consistency (text↔tables↔citations), and general rigor. Sits in the referee-simulation stage of the RISE pipeline.

## Distinctive contribution

Positions itself as enterprise-grade with explicit security and privacy commitments (SOC 2 + ISO 27001 in progress, zero-retention contracts, papers never used for training). Markets adoption by Oxford / Stanford / Yale / MIT / Caltech / Cambridge / Brown / OpenAI researchers. Closed-source commercial offering; first document free.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage (referee simulation). |
| Autonomy level | 2 | Supervised: user uploads, system returns a structured review. |
| Architectural transparency | 1 | Marketing-level descriptions only; internals not publicly documented. |
| Inputs supported | 1 | PDF inputs; no integration of literature corpora or co-author context. |
| Outputs / reproducibility | 1 | Reports persisted to user account; not designed for byte-level reproducibility. |
| Internal evaluation | 1 | Marketing claims of reviewer-grade quality; no publicly verifiable benchmark. |
| Openness | 0 | Closed-source commercial product. |
| Maturity / traction | 2 | Active commercial offering with named institutional adoption signals; user-base size not disclosed. |
| Cross-family policy | 0 | Closed; single internal stack. |
| Runtime assurance | 1 | ~2-hour parallel compute per review implies multiple internal passes; mechanism not public. |
| Cross-platform portability | 0 | Closed commercial product; single web surface. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation`


**Architectural features:** `multi-agent` `tool-use`


**Inputs:** `submitted-paper-pdf`


**Outputs:** `referee-report` `issue-list`


## Limitations

- Closed-source; cannot be audited, extended, or self-hosted.
- Per-review compute cost passed to user via subscription; pricing not transparent on landing page.
- Marketing-driven adoption claims; no published systematic comparison against alternatives.
- Targets the same review niche as coarse.ink and reviewer3.com; differentiation is per-review compute intensity.

## Related projects in this catalog

- [`coarse-ink`](coarse-ink.md)
- [`ape`](ape.md)
- [`marg`](marg.md)
- [`reviewer`](reviewer.md)

## Related references (literature catalog)

- `gartenberg2026morebetter` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `naddaf2025aipeer` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
