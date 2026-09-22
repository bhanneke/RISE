<!-- DO NOT EDIT — auto-generated from projects/landscape/swarmresearch.yml by scripts/build_indexes.py -->

# SwarmResearch

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/SwarmResearch/SwarmResearch>

**Source:** [`projects/landscape/swarmresearch.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/swarmresearch.yml)

## Positioning

An orchestrator-subagent harness for open-ended discovery, from a four-author group at UIUC. A Shepherd Agent holds the global picture and spawns waves of Search Agents by launching non-interactive Codex or Claude Code sessions: Explorers start from a fresh context and attack a new approach, Optimizers fork a parent's conversation history and refine an existing solution, and the Shepherd steers the population through three levers — parent selection, agent type and prompt. Every major edit lands on its own git branch. Sits beside AlphaEvolve and CORAL in the discovery-not-drafting corner of the landscape: it produces algorithms and solutions, not manuscripts.

## Distinctive contribution

It ships as agent skills, not as a framework — three Markdown skills (swarmresearch, swarmresearch-explorer, swarmresearch-optimizer) in `.claude/skills` and `.codex/skills`, with the README noting that other coding agents are supported by changing the spawn commands, so the prompts *are* the implementation. The architectural claim is about breadth over depth: a single long-running agent converges on one high-level approach and then grinds on low-level edits, whereas branch-isolated waves keep competing approaches alive and scale parallelism adaptively with search depth. Reported to match or beat SOTA LLM-guided evolution and multi-agent baselines on 13 of 15 tasks at a $50-per-task budget.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three adjacent stages — propose an approach, implement it, score it against the evaluator. No literature access, no write-up, no review of scholarship. |
| Autonomy level | 3 | The Shepherd spawns non-interactive Codex/Claude Code sessions and steers them without human gates; the paper's reference run put 50 agents through ~3 hours unattended on a $50 budget. |
| Architectural transparency | 2 | The three skills are plain Markdown in .claude/skills and .codex/skills, so the orchestration prompts and spawn logic are fully readable — but the repo holds only those plus assets/ and one spec_dec_example, has no license, and the paper's experiment harness lives in a separate reproduction repo. |
| Inputs supported | 0 | One narrow input form — a working directory holding prompt.md, an executable evaluator and an optional baseline — with no literature retrieval and no dataset connectors of any kind. |
| Outputs / reproducibility | 2 | Competing approaches persist as first-class git branches, so the search history is inspectable rather than collapsed; but there is no run manifest or seed control, and the reported 13/15 result is not reproducible from this repository. |
| Internal evaluation | 2 | The paper evaluates 15 tasks across three families — 5 math (circle packing, Erdős min overlap, signal processing, MMD-14-3, 3rd autocorrelation), 5 ADRS systems tasks (EPLB, LLM-SQL, txn scheduling, Cloudcast, PRISM) and 5 ALE-Bench-Lite AtCoder heuristics — against CORAL, EvoX and fixed-scaling baselines; arXiv preprint, not peer-reviewed or third-party replicated. |
| Openness | 1 | No LICENSE file and the GitHub API reports license: null (verified 2026-09-08), so the skills are readable but not legally reusable; a run also needs a paid Codex or Claude Code subscription, budgeted at $50 per task in the paper. |
| Maturity / traction | 1 | 16 stars, 3 forks, 13 commits, nothing pushed since 2026-07-07; a single-team research prototype attached to one preprint, with no release or packaging. |
| Cross-family policy | 1 | Skills ship for two runtimes and the paper's own configurations mix families across roles (Claude Code for the swarm, Opus 4.6 for EvoX, Minimax-M2.5 subagents under a Sonnet-4.6 orchestrator), so cross-family setups are supported — but nothing requires one, and there is no LLM reviewer role to pair, because scoring is delegated to a deterministic external evaluator. |
| Runtime assurance | 1 | One in-flight check: every candidate is scored by the user-supplied external evaluator, which the README frames as reward-hacking prevention, and branch isolation stops a failed approach contaminating others. No second integrity gate, and no manuscript to audit. |
| Cross-platform portability | 2 | Skills-as-Markdown for two agent runtimes (Claude Code and Codex) with a documented path to others by changing spawn commands, and the paper exercises several model families; only two runtimes actually ship, so short of the framework-agnostic band. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `code-generation` `data-analysis`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `artifact-versioning`


**Inputs:** `problem-description` `external-evaluator` `baseline-solution`


**Outputs:** `solution-implementations` `git-branch-history` `evaluator-scores`


**Knowledge sources:** `user-supplied-evaluator`


## Limitations

- No LICENSE file (verified 2026-09-08 via the GitHub API and a root directory listing) — the skills are readable but reuse terms are undeclared.
- Requires the user to supply an executable evaluator, which confines it to problems with a cheap machine-checkable objective. Most empirical economics questions have no such scorer: the quantity of interest is an identified effect, not a number a script can rank.
- Scope is algorithm and heuristic design, not scholarship — no literature access, no citation handling, no write-up stage, so nothing here produces or checks a paper.
- The reported 13/15 result cannot be reproduced from this repository: it holds the skills and one speculative-decoding example, while the paper's experiment code sits in a separate reproduction repo.
- Expensive and slow at the demonstrated scale: $50 per task in the benchmark, and the speculative-decoding case study ran roughly 11 hours per phase on Claude Code Opus 4.8.
- 16 stars, 3 forks, 13 commits, unchanged since 2026-07-07 — the adaptive-parallelism claim rests entirely on the authors' own runs.

## Related projects in this catalog

- [`alphaevolve`](alphaevolve.md)
- [`coral`](coral.md)
- [`agon`](agon.md)
- [`deepscientist`](deepscientist.md)

## Papers describing this project

- **SwarmResearch: Orchestrating Coding Agents for Open-Ended Discovery** — Virk, Y., Edds, Z., Xia, C. S., Zhang, L. (2026). *arXiv*. [arXiv:2607.02807](https://arxiv.org/abs/2607.02807)

## Related references (literature catalog)

- `virk2026swarmresearch` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
