<!-- DO NOT EDIT — auto-generated from projects/landscape/deepscientist.yml by scripts/build_indexes.py -->

# DeepScientist

`external` · status: `active` · focus: `end-to-end` · discipline: `computer-science` · started: 2025

**Project page:** <https://github.com/ResearAI/DeepScientist>

**Source:** [`projects/landscape/deepscientist.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/deepscientist.yml)

## Positioning

A local-first autonomous research studio for ML/AI work: you hand it a paper, a repository, or a bare research objective, and it reproduces a baseline, then runs long-horizon hypothesise → verify → analyse cycles under Bayesian optimisation, accumulating findings across sessions and ending in figures, reports and a LaTeX/PDF draft. Unlike the run-once pipelines elsewhere in the RISE end-to-end layer (aris, agent-laboratory, luxas), state is the architecture: one Git repository per research quest, branches expressing competing research routes, failed branches retained rather than discarded, and a "Findings Memory" that survives between runs.

## Distinctive contribution

The only catalogued end-to-end system whose persistence layer is ordinary version control — quest-as-Git-repo with per-route branches and preserved failures — combined with the field's most honest published funnel: an ICLR 2026 paper reporting roughly 5,000 autonomously generated ideas, 1,100 taken to experimental validation and 21 that became scientific findings, over ~20,000 GPU hours, with gains of 183.7% (accuracy), 1.9% (tokens/second) and 7.9% (AUROC) over human-designed state of the art on three AI tasks. It is also runner-agnostic (Codex, Claude Code, Kimi Code, OpenCode) and supports human takeover at any point, which fits a human-approval-by-default workflow better than the unattended systems it competes with.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Seven stages — baseline reproduction, hypothesis generation from prior results, experiment loops, ablations, analysis and figures, paper drafting, LaTeX/PDF compilation — with real gaps: no literature-discovery or literature-synthesis stage, and no referee-simulation stage inside the pipeline. |
| Autonomy level | 3 | Designed for unattended long-horizon runs — the paper's headline campaign ran roughly a month on 16 H800 GPUs generating ~5,000 ideas — with human takeover offered as an option, not a required gate. |
| Architectural transparency | 2 | Apache-2.0 with 341 commits and an ICLR 2026 paper describing the Bayesian-optimisation loop, findings memory and quest structure; but the shipped repo is the npm-distributed TypeScript studio and I could not confirm from the repo page that per-agent prompts are published as inspectable files, nor is an evaluation harness included. |
| Inputs supported | 2 | Three input forms (a research objective, a paper, or an existing code repository) plus the user's own local code and data as the working substrate; no external literature-corpus connector or dataset catalogue is documented. |
| Outputs / reproducibility | 2 | Every quest is a Git repository holding code, experiment branches, figures, report and LaTeX/PDF in-tree, with failed routes retained — strong artifact versioning — but no run manifest, seed policy or replication script is published, so end-to-end reproducibility from declared inputs is not demonstrated. |
| Internal evaluation | 3 | Peer-reviewed: published as a conference paper at ICLR 2026 (arXiv 2509.26603), reporting measured gains over human SOTA on three AI tasks with the full idea → validation → finding funnel, plus automated-reviewer scoring of the generated manuscripts. |
| Openness | 2 | Apache-2.0 and installable in one line (`npm install -g @researai/deepscientist`), but the demonstrated results required 16 H800 GPUs and ~20,000 GPU hours plus a paid agent runner, so nothing shown is reproducible on commodity hardware. |
| Maturity / traction | 2 | 3,317 stars, 330 forks, 341 commits, tagged releases through v1.6.0 and an npm distribution — beta with real external users — but single-lab origin and last pushed 2026-06-28, so momentum has slowed. |
| Cross-family policy | 1 | Four interchangeable runners (Codex, Claude Code, Kimi Code, OpenCode) plus Ollama/Gemini backends make cross-family setups easy to configure, but nothing requires or defaults to an executor and a reviewer drawn from different model families. |
| Runtime assurance | 1 | The in-flight check is empirical rather than editorial — each hypothesis must survive a real experiment against a reproduced baseline, and failed branches are kept rather than hidden — but no claim-faithfulness, citation-grounding, math-verification or figure-audit gate is documented. |
| Cross-platform portability | 2 | Top of the band: four built-in agent runners plus local backends (Ollama, Gemini) via wrappers, and local-first execution on macOS/Linux — but native Windows is experimental (WSL2 recommended) and it is one studio runtime, not a library embeddable elsewhere. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `research-design` `code-generation` `data-analysis` `replication` `paper-drafting` `dissemination`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `persistent-memory` `artifact-versioning`


**Inputs:** `research-objective` `paper` `code-repository`


**Outputs:** `experiment-results` `ablation-studies` `figures` `paper-draft` `compiled-pdf` `quest-git-history`


**Data sources:** `user-provided` `self-generated-experiments`


**Knowledge sources:** `user-supplied-papers` `findings-memory`


## Limitations

- Domain is ML/AI research — the reported targets are AI tasks (accuracy, tokens/second, AUROC) — with no evidence in economics, finance or the social sciences; the identification-and-robustness half of empirical social science has no analogue here.
- The discovery funnel is brutally thin: ~5,000 ideas → 1,100 validated → 21 findings (≈0.4%), at ~20,000 GPU hours on 16 H800s, so the cost per usable result is very high.
- Manuscript quality was assessed by an automated AI reviewer (reported as on par with average ICLR 2025 submissions, ~60% simulated acceptance), not by human referees.
- Last pushed 2026-06-28 — active by the three-month rule, but slowing; native Windows support is experimental.
- Requires a paid agent runner (Codex/Claude Code/Kimi/OpenCode) and serious GPU compute; the local-first design deliberately rules out cloud handoff of unpublished ideas.
- I could not open the OpenReview forum page directly (browser verification) — the ICLR 2026 acceptance is confirmed via the search-indexed OpenReview PDF header and the repo README's OpenReview link, not by fetching the page myself.

## Related projects in this catalog

- [`agent-laboratory`](agent-laboratory.md)
- [`aris`](aris.md)
- [`evoscientist`](evoscientist.md)
- [`luxas`](luxas.md)

## Papers describing this project

- **DeepScientist: Advancing Frontier-Pushing Scientific Findings Progressively** — Weng, Y., Zhu, M., Xie, Q., Sun, Q., Lin, Z., Liu, S., Zhang, Y. (2026). *ICLR 2026*. [arXiv:2509.26603](https://arxiv.org/abs/2509.26603)

## Related references (literature catalog)

- `weng2025deepscientist` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
