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
| Internal evaluation | 2 | Aug 2026 self-published benchmark (150 economics preprints, 1,349 head-to-head matches vs. 9 competitor systems): Refine won 90.4% overall (94.8% vs. single-shot LLM referees, 85.0% vs. scaffolded review systems), broken out by subfield — a systematic internal evaluation, though still self-conducted rather than third-party. |
| Openness | 0 | Closed-source commercial product. |
| Maturity / traction | 3 | 2026-08-06: formal partnership with the American Economic Association and the Econometric Society for technical-verification checks on revise-and-resubmit papers; AEA-journal pilot reported ~90% author approval for incorporating Refine into the editorial process — production-grade deployment inside a major scholarly body's workflow. |
| Cross-family policy | 0 | Closed; single internal stack. |
| Runtime assurance | 1 | ~2-hour parallel compute per review implies multiple internal passes; mechanism not public. |
| Cross-platform portability | 0 | Closed commercial product; single web surface. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation`


**Architectural features:** `multi-agent` `tool-use`


**Inputs:** `submitted-paper-pdf`


**Outputs:** `referee-report` `issue-list`


## Limitations

- Closed-source; cannot be audited, extended, or self-hosted.
- Per-review compute cost passed to user via subscription; pricing not transparent on landing page.
- Its head-to-head benchmark against competitor systems is self-published, not third-party or peer-reviewed.
- Targets the same review niche as coarse.ink and reviewer3.com; differentiation is per-review compute intensity.
- AEA/Econometric Society deployment is scoped to a technical-verification check only — it does not assess contribution, importance, or screen submissions en masse.

## Related projects in this catalog

- [`coarse-ink`](coarse-ink.md)
- [`ape`](ape.md)
- [`marg`](marg.md)
- [`reviewer`](reviewer.md)

## Related references (literature catalog)

- Gartenberg, C. et al. (2026). [*More Versus Better: Artificial Intelligence, Incentives, and the Emerging Crisis in Peer Review*](../papers/notes/gartenberg2026morebetter.md) `gartenberg2026morebetter`
- Naddaf, M. (2025). [*AI Is Transforming Peer Review — and Many Scientists Are Worried*](../papers/notes/naddaf2025aipeer.md) `naddaf2025aipeer`
