<!-- DO NOT EDIT — auto-generated from projects/landscape/coarse-ink.yml by scripts/build_indexes.py -->

# Coarse (coarse.ink)

`external` · status: `active` · focus: `review` · discipline: `general` · started: 2026

**Project page:** <https://coarse.ink/>

**Source:** [`projects/landscape/coarse-ink.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/coarse-ink.yml)

## Positioning

A web-based AI peer-review service: users upload academic papers (up to 50 MB) and receive AI-generated referee reports with 20+ detailed comments. Operates in two modes — web-based using user-supplied OpenRouter API keys, or local processing via Claude Code / Codex / Gemini CLI subscriptions. Sits squarely in the referee-simulation stage of the RISE pipeline.

## Distinctive contribution

Open-source (MIT) and explicitly anti-commercial in framing — "Academic peer review runs on unpaid academic labor. Others decided to make a business out of that. We didn't like that." The site reports a blind self-evaluation against refine.ink, Stanford Agentic Reviewer, and reviewer3.com claiming higher coverage, specificity, and depth. Privacy-by-design: API keys remain in the user's browser tab and clear on close.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage (referee simulation). |
| Autonomy level | 2 | Supervised: user uploads paper and receives a report; optional 'reviewer focus' notes steer emphasis. |
| Architectural transparency | 2 | Open source under MIT; multiple back-end models exposed (Claude, GPT-5, Gemini, DeepSeek). Internal orchestration not deeply documented in marketing. |
| Inputs supported | 1 | PDF + optional focus note; no integration of literature corpora or prior reviews. |
| Outputs / reproducibility | 1 | Reports are persisted client-side; not deterministic across runs by design (different model choices). |
| Internal evaluation | 1 | Self-reported blind evaluation vs. refine.ink, Stanford Agentic Reviewer, reviewer3.com; no third-party benchmark. |
| Openness | 3 | MIT-licensed; BYOK (bring-your-own-key) model; transparent pricing (~under $2/review with OpenRouter). |
| Maturity / traction | 1 | Active hosted service in 2026; user-base scope not publicly disclosed. |
| Cross-family policy | 1 | BYOK OpenRouter exposes Claude / GPT-5 / Gemini / DeepSeek as user-selectable executor — cross-family by user choice. |
| Runtime assurance | 1 | Single-pass review with focus-note steering; no published claim-audit harness. |
| Cross-platform portability | 2 | Multi-provider via OpenRouter + local Claude Code/Codex/Gemini CLI fallback. |

*Scored on 2026-05-18. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation`


**Architectural features:** `tool-use` `human-in-loop`


**Inputs:** `submitted-paper-pdf` `reviewer-focus-note`


**Outputs:** `referee-report`


## Limitations

- Single-stage tool; needs upstream paper provenance.
- Quality varies with chosen back-end model.
- Self-evaluation against competitors not independently audited.

## Related projects in this catalog

- [`refine-ink`](refine-ink.md)
- [`ape`](ape.md)
- [`marg`](marg.md)
- [`reviewer`](reviewer.md)

## Related references (literature catalog)

- `gartenberg2026morebetter` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `naddaf2025aipeer` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
