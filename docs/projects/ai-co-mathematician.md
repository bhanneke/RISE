<!-- DO NOT EDIT — auto-generated from projects/landscape/ai-co-mathematician.yml by scripts/build_indexes.py -->

# AI Co-Mathematician (Google DeepMind)

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://arxiv.org/abs/2605.06651>

**Source:** [`projects/landscape/ai-co-mathematician.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ai-co-mathematician.yml)

## Positioning

A closed, agentic multi-agent workbench (arXiv:2605.06651) built on Gemini 3.1 for open-ended *mathematics* research. A hierarchy of specialized agents runs under a top-level project coordinator across asynchronous, parallel workstreams — ideation, literature search, computational exploration, theorem proving, theory building — managing uncertainty, tracking failed hypotheses, and producing LaTeX write-ups with margin annotations and provenance notes. Explicitly modelled on agentic coding environments (e.g. Claude Code), it spans the full pipeline from research intent to a written mathematical result rather than optimizing a single stage.

## Distinctive contribution

One of the first agentic systems to demonstrate open-ended mathematical *discovery* rather than benchmark problem-solving alone: it scored 48% (23/48) on FrontierMath Tier 4 — versus 19% for the Gemini 3.1 Pro base model — and Oxford mathematician Marc Lackenby used it to resolve Problem 21.10 of the Kourovka Notebook, a group-theory question open since 1965. The RISE skills catalog's theorist-toolbox (co-math skills) explicitly emulates this system's coordinator + workstream + reviewer-gate design in an open, skills-as-Markdown form.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Seven stages from refining research intent through proving to LaTeX write-up; no dedicated referee-simulation or dissemination stage. |
| Autonomy level | 2 | Designed as a collaborative workbench (mathematician sets direction and reviews artifacts); async workstreams run without per-step approval, and it solved FrontierMath Tier 4 problems autonomously. |
| Architectural transparency | 1 | Paper describes the hierarchical agent topology and coordinator/workstream design, but no code, prompts, or configs are released. |
| Inputs supported | 2 | Accepts both well-posed open problems and open-ended research directions, with literature search and computational-exploration tooling. |
| Outputs / reproducibility | 2 | Persists LaTeX write-ups plus code from computational exploration with provenance notes; closed system and LLM nondeterminism preclude external end-to-end reproduction. |
| Internal evaluation | 2 | Systematic benchmark result (48% on FrontierMath Tier 4) plus an expert-verified new result (Kourovka Notebook 21.10); still an arXiv preprint, not peer-reviewed. |
| Openness | 0 | Closed research system; no code, weights, or public access at scoring date. |
| Maturity / traction | 1 | DeepMind research prototype (arXiv, May 2026), not a product; demonstrated real use by an external mathematician but no general availability. |
| Cross-family policy | 0 | Single model family — all agents run on Gemini 3.1. |
| Runtime assurance | 2 | In-pipeline review cycles, failed-hypothesis tracking, provenance annotations, and proof/computational verification act as moderate runtime gates. |
| Cross-platform portability | 0 | Closed system locked to DeepMind infrastructure and Gemini; not deployable elsewhere. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `hypothesis-generation` `literature-discovery` `literature-synthesis` `formal-modeling` `code-generation` `paper-drafting`


**Architectural features:** `multi-agent` `human-in-loop` `tool-use` `persistent-memory` `iterative-loop` `artifact-versioning`


**Inputs:** `open-problem` `research-direction`


**Outputs:** `proofs` `latex-writeups` `computational-results` `literature-references`


**Knowledge sources:** `mathematical-literature`


## Limitations

- Closed system: no code, prompts, or public access — architecture is known only from the paper, and the FrontierMath and Kourovka results cannot be independently reproduced.
- Benchmarked and demonstrated in pure mathematics; transfer to empirical or applied research disciplines is unshown.
- Autonomous benchmark performance still leaves the majority of Tier 4 problems unsolved, and headline discoveries required an expert mathematician in the loop.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`alphaevolve`](alphaevolve.md)
- [`econcs-bench`](econcs-bench.md)
- [`google-co-scientist`](google-co-scientist.md)

## Papers describing this project

- **AI co-mathematician: Accelerating mathematicians with agentic AI** — Zheng, D., von Glehn, I., Zwols, Y., Beloshapka, I., Buesing, L., Roy, D. M., et al. (2026). *arXiv (Google DeepMind)*. [arXiv:2605.06651](https://arxiv.org/abs/2605.06651)
