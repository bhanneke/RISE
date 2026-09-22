<!-- DO NOT EDIT — auto-generated from projects/landscape/scholar-loop.yml by scripts/build_indexes.py -->

# Scholar Loop

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/renee-jia/scholar-loop>

**Source:** [`projects/landscape/scholar-loop.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/scholar-loop.yml)

## Positioning

A single-maintainer "autonomous AI scientist" that runs the full PhD loop on a single-GPU budget: literature scouting (arXiv + OpenAlex, citation-ranked), grounded hypothesis generation, debate-gated real PyTorch experiments in a smoke -> verify -> full funnel, reflection into a time-decaying skill library, and a number-grounded write-up with self-review — all under a self-stopping budget governor. Sits with the AI-scientist family (Sakana, Agent Laboratory) but leads with deterministic anti-reward-hacking guards rather than scale.

## Distinctive contribution

Treats the outer loop and its integrity guards as the product: two-phase frozen scoring the experiment code cannot fake, an edit allowlist, a VerifiedRegistry that grounds every number in the draft, and universal predict-then-verify calibration that scores each agent's checkable claims against ground truth — with a bundled adversarial "cheater" engine to prove the guards hold, and the whole eight-agent loop testable deterministically without an API key or GPU.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Seven stages from literature through drafting and self-review; domains are pre-defined YAML profiles with fixed metrics, so no open research-question formulation. |
| Autonomy level | 3 | Runs unattended under a self-stopping governor (dollar budget, round cap, convergence); the user supplies only the domain profile and budget up front. |
| Architectural transparency | 3 | MIT-licensed full code with typed JSON-schema agent I/O, 108 tests, CI, and captured end-to-end runs publishing paper, run log, and raw ledger. |
| Inputs supported | 1 | One input form (a domain profile plus engine pair; two shipped) with live literature access via arXiv and OpenAlex. |
| Outputs / reproducibility | 2 | Persists drafts, run ledgers, and logs — every reported number traces to a frozen-metric measurement in the jsonl — but exact re-runs are deterministic only under the MockLLM. |
| Internal evaluation | 1 | Two captured live Opus runs on toy tasks (digits 5.0%->3.82% err, diabetes RMSE 56.5->55.24) plus a reward-hacking stress test; no benchmark evaluation or external validation. |
| Openness | 3 | MIT; pip-installable; the entire loop runs deterministically in under a second on CPU with no API key via the bundled MockLLM. |
| Maturity / traction | 1 | 468 stars and 35 forks — essentially flat since last review (462/36) — confirming the single-maintainer research preview has had no pushes since 2026-06-23, now over two months idle at scoring; growth has stalled along with development. |
| Cross-family policy | 0 | Single family — the optional [llm] extra ships only an Anthropic client, and writer and reviewer share the same model; the optimization loop deliberately uses no LLM-as-judge. |
| Runtime assurance | 3 | Heavy deterministic guard stack with gating: frozen two-phase scoring, edit allowlist, VerifiedRegistry number-grounding, schema validate-retry, per-agent predict-then-verify calibration, and tiered promotion gates — adversarially tested via the cheater engine. |
| Cross-platform portability | 0 | Pure-Python package runs anywhere, but live runs support only the Anthropic backend; the MockLLM is a test double, not a deployment target. |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `hypothesis-generation` `code-generation` `data-analysis` `paper-drafting` `referee-simulation`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `persistent-memory` `debate-consensus`


**Inputs:** `domain-profile` `budget-config`


**Outputs:** `paper-draft` `review-report` `run-ledger` `skill-library`


**Data sources:** `bundled-datasets`


**Knowledge sources:** `arxiv` `openalex` `skill-library`


## Limitations

- No commits since 2026-06-23 (over two months idle at this review) and star/fork counts have plateaued (468/35, up from 462/36) — the single-maintainer 'research preview' looks stalled rather than merely quiet; status here assumes <3 months idle still counts as active.
- Shipped domains are toy sklearn/PyTorch tasks with weak baselines, and the system's own reviewer rejects both captured papers as too marginal (the README concedes it is not wrong).
- Anthropic-only live backend and no container sandboxing yet — the author names sandboxing as the open residual boundary.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`agent-laboratory`](agent-laboratory.md)
- [`data-to-paper`](data-to-paper.md)
