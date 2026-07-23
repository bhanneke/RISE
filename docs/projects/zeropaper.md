<!-- DO NOT EDIT — auto-generated from projects/landscape/zeropaper.yml by scripts/build_indexes.py -->

# zeropaper (Auto AI Research Template)

`external` · status: `active` · focus: `end-to-end` · discipline: `finance` · started: 2025

**Project page:** <https://github.com/alejandroll10/zeropaper>

**Source:** [`projects/landscape/zeropaper.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/zeropaper.yml)

## Positioning

An autonomous research-paper pipeline that uses Claude Code, Codex, or Gemini CLI as the subagent dispatcher. From a chosen variant (finance theory, macro theory, finance + empirical with CRSP / Compustat / FRED, finance + theory_llm, or seed / manual / faithful / light modes) it runs problem discovery → idea generation → theory development → math verification → paper writing → referee simulation, producing watermarked PDF drafts under a restrictive academic-use license.

## Distinctive contribution

Treats subscription-tier coding-agent CLIs (Claude Code / Codex / Gemini CLI) as the dispatch substrate for an autonomous-paper pipeline with adversarial gates (math-auditor, novelty-checker, simulated referees), per-project git-isolated workspaces, and sandboxed execution (bubblewrap on Linux, Seatbelt on macOS). Notable for its license-coded responsible-use protocol: §2 requires prior notice before submission, §3 requires AI-disclosure, §4 forbids watermark removal, §5 prohibits commercial use without separate license.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | Covers ~10 stages including formal modeling, empirical analysis (--ext empirical), and referee simulation. |
| Autonomy level | 3 | 'Set up a project, launch Claude Code, Codex, or Gemini CLI, walk away.' Autonomous by design. |
| Architectural transparency | 2 | Pipeline stages documented in README; full agent-prompt internals require reading the template. |
| Inputs supported | 2 | Multiple variants (finance, macro), modes (--seed, --faithful, --manual, --light, empirical-first); empirical extension integrates external financial corpora. |
| Outputs / reproducibility | 2 | Per-project git repositories isolate outputs; sandboxed execution; watermarked PDF provenance. |
| Internal evaluation | 2 | In-pipeline adversarial gates (math-auditor, novelty-checker, simulated referees); companion benchmarks paper referenced. |
| Openness | 1 | Source on GitHub but under the custom 'Research Use License v1.1' (adopted 2026-07-07) — prior notice, AI-disclosure, watermark-preservation, non-commercial clauses all encumber reuse; not OSI open source. |
| Maturity / traction | 1 | Very active development (100+ commits since May 2026, last push 2026-07-23) but single-developer / Institute for Automated Research; ~60 stars. |
| Cross-family policy | 1 | Optional cross-family setup (Claude Code / Codex / Gemini CLI as dispatcher); not required. |
| Runtime assurance | 3 | Math-auditor + novelty-checker + simulated referees as adversarial gates; sandboxed execution (bubblewrap/Seatbelt); watermarking. |
| Cross-platform portability | 1 | Three dispatcher CLIs (Claude Code, Codex, Gemini CLI); finance/macro variants but single template runtime. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `hypothesis-generation` `literature-discovery` `research-design` `formal-modeling` `data-acquisition` `data-analysis` `paper-drafting` `revision-editing` `referee-simulation`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `debate-consensus` `artifact-versioning`


**Inputs:** `research-area` `seed-idea` `prior-paper`


**Outputs:** `watermarked-pdf` `code` `replication-data`


**Data sources:** `crsp` `compustat` `fred` `user-provided`


**Knowledge sources:** `web-search` `prior-literature`


## Limitations

- Restrictive license (Research Use License v1.1, 2026-07-07): submission requires prior written notice; AI-disclosure mandatory; watermark removal terminates license; commercial use prohibited; 'Assisted Output' exemption for human-led work.
- Designed for finance/macro/empirical-finance papers — portability to other empirical disciplines requires variant authoring.
- Watermarking is non-cosmetic; detection methodology shared only with journal editors.
- Subscription path (~$200/mo, ~$2/paper) recommended; pay-per-token path is ~$2,000/paper.
- Sandbox depends on bubblewrap (Linux) or Seatbelt (macOS); Windows untested.

## Related projects in this catalog

- [`sakana-ai-scientist`](sakana-ai-scientist.md)
- [`e2er`](e2er.md)
- [`clo-author`](clo-author.md)
- [`ape`](ape.md)

## Papers describing this project

- **IAR-M-001: zeropaper companion paper** — Aldea, A. (2026). *Institute for Automated Research working paper series*. [link](https://instituteforautomatedresearch.org/papers/iar-m/iar-m-001)
