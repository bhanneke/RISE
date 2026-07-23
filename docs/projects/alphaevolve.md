<!-- DO NOT EDIT — auto-generated from projects/landscape/alphaevolve.yml by scripts/build_indexes.py -->

# AlphaEvolve (Google DeepMind)

`external` · status: `active` · focus: `end-to-end` · discipline: `mathematics` · started: 2025

**Project page:** <https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/>

**Source:** [`projects/landscape/alphaevolve.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/alphaevolve.yml)

## Positioning

A Gemini-powered evolutionary coding agent that combines LLM generative capabilities with automated evaluators in an iterative propose-test-refine loop. Targets the *algorithmic and scientific discovery* arc of the RISE pipeline: given a well-defined evaluator, AlphaEvolve searches the space of programs that improve the metric the evaluator scores. Demonstrated on data-center scheduling, hardware-circuit design, kernel optimization, and — most relevant to RISE — open mathematical problems.

## Distinctive contribution

An evolutionary-search harness over LLM-generated code that decouples *generation* (Gemini Pro / Flash) from *evaluation* (a domain-specific automated scoring function). In Georgiev, Gómez-Serrano, Tao & Wagner (2025) the system rediscovers best-known constructions for 56 of 67 mathematical problems and improves on the best-known result in several, occasionally generalizing finite-case results into closed-form expressions valid for all inputs. Distinctive among RISE-landscape projects because it does not write papers — it discovers algorithmic / mathematical *artifacts*, leaving the scholarly framing to humans.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three stages (hypothesis, code, analysis) bundled into the evolutionary loop; no literature, drafting, or peer-review components. |
| Autonomy level | 3 | Autonomous within the search loop — given problem + evaluator, runs without human intervention until budget exhausted. |
| Architectural transparency | 1 | Whitepaper (Novikov et al., arXiv 2506.13131) describes the architecture; system itself is closed-source. |
| Inputs supported | 1 | Accepts a problem specification + an automated evaluator function; cannot handle problems without a scorable evaluation oracle. |
| Outputs / reproducibility | 2 | Discovered artifacts (programs, mathematical constructions) are durable and verifiable; the discovery *process* requires Google compute and is not externally reproducible. |
| Internal evaluation | 3 | Evaluation is by construction — every candidate is scored by the automated evaluator. 67-problem benchmark in Georgiev et al. provides external validation. |
| Openness | 0 | Closed-source, gated behind Google DeepMind's Early Access Program for selected academic users. |
| Maturity / traction | 2 | Reached general availability on Google Cloud (Gemini Enterprise Agent Platform) 2026-07-19 with enterprise customers (BASF, JetBrains, Klarna); whitepaper + high-profile follow-up papers (including Terence Tao as co-author on Georgiev et al.). |
| Cross-family policy | 0 | Single model family (Gemini Pro/Flash) within Google DeepMind. |
| Runtime assurance | 3 | Automated evaluator runs on every candidate as part of the search loop; this is the assurance layer by construction. |
| Cross-platform portability | 0 | Tightly coupled to Google internal infrastructure and Gemini API; not portable. |

*Scored on 2026-05-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `code-generation` `data-analysis`


**Architectural features:** `evolutionary-search` `tool-use` `iterative-loop` `automated-evaluation`


**Inputs:** `problem-specification` `automated-evaluator`


**Outputs:** `algorithmic-artifacts` `improved-constructions` `closed-form-expressions`


**Data sources:** `none-required`


**Knowledge sources:** `llm-internal`


## Limitations

- Requires a well-defined automated evaluator; not applicable to open-ended discovery without a scorable target.
- Closed-source and gated access — outside users cannot independently reproduce discovery runs.
- Computation-heavy: evolutionary search over LLM-generated programs requires substantial Gemini API budget.
- Does not produce scholarly artifacts (papers, references, methodological discussion) — leaves the writing to human collaborators.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`sakana-ai-scientist-v1`](sakana-ai-scientist-v1.md)

## Papers describing this project

- **AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery** — Novikov, A., Vũ, N., Eisenberger, M., Dupont, E., Huang, P.-S., Wagner, A. Z., et al. (2025). *arXiv*. [arXiv:2506.13131](https://arxiv.org/abs/2506.13131)
- **Mathematical Exploration and Discovery at Scale** — Georgiev, B., Gómez-Serrano, J., Tao, T., Wagner, A. Z. (2025). *arXiv*. [arXiv:2511.02864](https://arxiv.org/abs/2511.02864)

## Related references (literature catalog)

- `novikov2025alphaevolve` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
- `georgiev2025alphaevolvemath` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
