<!-- DO NOT EDIT — auto-generated from projects/landscape/ai-peer-review.yml by scripts/build_indexes.py -->

# AI Peer Review (poldrack)

`external` · status: `active` · focus: `review` · discipline: `general` · started: 2026

**Project page:** <https://github.com/poldrack/ai-peer-review>

**Licence:** `MIT`

**Source:** [`projects/landscape/ai-peer-review.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ai-peer-review.yml)

## Positioning

A CLI tool for AI-assisted meta-review of scientific papers: submits a manuscript to up to six proprietary LLMs (GPT-4o, GPT-4o-mini, Claude 3.7 Sonnet, Gemini 2.5 Pro, DeepSeek R1, Llama 4 Maverick) for independent review, then synthesizes a meta-review plus a concerns-by-reviewer matrix. Sits in the RISE referee-simulation lane alongside `reviewer` and `marg`; it is the upstream original of the catalogued `ai-peer-review-skill`, which replaces the six-provider panel with parallel Claude subagents.

## Distinctive contribution

A genuine cross-model-family review panel (six different providers by default) rather than N instances of one model family — the exact trade-off its Claude-only fork gives up for convenience — plus a "scientific-validity-only" review profile that screens out presentation nitpicks to focus on substantive concerns.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage: referee simulation on a finished manuscript. |
| Autonomy level | 2 | One invocation submits the manuscript to all configured models and returns reviews plus a synthesized meta-review; the human supplies the paper and API keys and reads the final bundle, with no intermediate approval step. |
| Architectural transparency | 3 | MIT; the CLI, per-model review prompts, meta-review synthesis logic, and configuration profiles (including a neuroscience-tuned default and a scientific-validity-only mode) are all in the repo. No evaluation harness exists to publish. |
| Inputs supported | 0 | One input form (a manuscript) with no literature corpus or data access of any kind. |
| Outputs / reproducibility | 2 | Four durable artifacts per paper (per-model markdown reviews, a markdown meta-review, a CSV concerns matrix, and a JSON results bundle) organized by paper name; no seeding or model-version pinning, so reruns on the same manuscript can differ. |
| Internal evaluation | 0 | No agreement statistics against human referee reports, and no comparison of review quality across the six supported models, reported in the repository. |
| Openness | 2 | MIT license and a documented pip install -e . setup, but running the full six-model panel requires paid API keys across up to four providers (OpenAI, Anthropic, Google, Together AI) — not free-tier reproducible. |
| Maturity / traction | 2 | 154 stars, 25 forks, and commits as recent as 2026-07 — actively maintained, with enough external pickup to have spawned at least one derivative skill (`ai-peer-review-skill`, 61 stars). |
| Cross-family policy | 2 | Running independent reviewers across six different proprietary model families is the out-of-the-box default configuration, not an opt-in — the opposite trade-off from the single-family Claude fork. |
| Runtime assurance | 1 | Each model produces a single-pass structured review, synthesized once into a meta-review; nothing checks a reviewer's claim back against the manuscript text or flags a likely confabulated concern. |
| Cross-platform portability | 1 | A standalone Python CLI callable from any environment with API keys configured — not locked to one agent runtime like its Claude-Code-only fork — but it is a single tool, not a multi-IDE or multi-runtime skill package. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation`


**Architectural features:** `multi-agent` `tool-use`


**Inputs:** `manuscript-pdf`


**Outputs:** `reviewer-reports` `meta-review` `concerns-matrix-csv` `results-json`


## Limitations

- Requires paid API keys across up to four providers (OpenAI, Anthropic, Google, Together AI) to run the full six-model panel — the most expensive single review tool in the catalog's review lane.
- No evaluation of review quality or agreement against human referee reports or ground truth.
- Default review profile and prompts were built for neuroscience/biomedical papers; adapting to other fields means editing prompts directly rather than passing a parameter (contrast the catalogued fork, which turns this into a config option).
- The README discloses that all code was AI-generated via Claude Code, with no independent code review reported.
- No seeding or model-version pinning, so two runs on the same manuscript can yield materially different panels.

## Related projects in this catalog

- [`ai-peer-review-skill`](ai-peer-review-skill.md)
- [`reviewer`](reviewer.md)
- [`marg`](marg.md)
- [`ai-research-feedback`](ai-research-feedback.md)
