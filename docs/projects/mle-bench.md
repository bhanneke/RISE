<!-- DO NOT EDIT — auto-generated from projects/landscape/mle-bench.yml by scripts/build_indexes.py -->

# MLE-bench (OpenAI)

`external` · status: `dormant` · focus: `analysis` · discipline: `computer-science` · started: 2024

**Project page:** <https://github.com/openai/mle-bench>

**Source:** [`projects/landscape/mle-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/mle-bench.yml)

## Positioning

Seventy-five Kaggle competitions repackaged as an offline agent benchmark: an agent gets the competition description and data and must produce a submission CSV, graded deterministically against the held-out test set and scored against the *human* medal thresholds from that competition's original leaderboard. Splits by complexity (Low == Lite, 22 competitions and 158 GB; the full set is 3.3 TB), with a canonical protocol of at least three seeds reported as mean ± SEM, a Docker environment image, a grading server, and three open-source agent scaffolds (AIDE, MLAB, OpenHands) wired in as baselines. It measures the data-work leg of the RISE pipeline — the empirical execution that `analysis` entries automate — and is the sibling benchmark to `paperbench`'s replication framing.

## Distinctive contribution

Human medal thresholds as the yardstick: performance is reported as the share of competitions in which an agent would have won any Kaggle medal, so the scale is anchored to what thousands of human competitors actually achieved rather than to a synthetic metric. It is also the catalog's clearest longitudinal record of the autonomy curve — the same deterministic grader now carries roughly two years of third-party submissions with published grading reports, from the paper's AIDE + o1-preview at 17.1% Any-Medal on the full set to external agents from Baidu, Google, Microsoft, Meta, SJTU and several startups above 60%, with Lite-split scores now over 80%.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure: it grades ML-engineering execution and produces scores, not scholarship — no question formulation, literature or write-up stage exists. |
| Autonomy level | 0 | Fixed competition tasks plus a deterministic grader; the harness is explicitly agent-agnostic and all agency sits in the evaluated scaffolds. |
| Architectural transparency | 3 | Public dataset-construction code, per-competition prepare/grade logic, split files, the `mlebench-env` Docker image, the grading server, the aggregation scripts, and the three baseline agents — plus a paper documenting the rules. |
| Inputs supported | 2 | 75 standardized competition tasks in Low/Medium/High and Lite splits, each with description and local data, runnable by any agent and demonstrated across three scaffolds. |
| Outputs / reproducibility | 2 | Task and grading are explicitly deterministic, splits are versioned files, and every leaderboard row ships a grading report — but agent runs are high-variance (hence the ≥3-seed protocol) and 3.3 TB with ~2 days of Kaggle-API prep stands between a reader and a rerun. |
| Internal evaluation | 3 | Peer-reviewed at ICLR 2025 as an Oral (verified on iclr.cc), and externally validated in practice by ~28 leaderboard rows of third-party agent submissions with published grading reports through early 2026. |
| Openness | 2 | MIT licence, but explicitly scoped — 'this license applies to the code in this repository, but not the external datasets and files that may be downloaded' — so the data arrives under Kaggle's own competition terms and needs an accepted-rules Kaggle account. |
| Maturity / traction | 3 | 1,739 stars, 257 forks, an ICLR 2025 Oral, and sustained external adoption: leaderboard submissions from Baidu, Google Cloud AI Research, Microsoft (R&D-Agent), Meta (AIRA-dojo), SJTU, Fractal AI and startups, running from 2024-10 to 2026-03. |
| Cross-family policy | 0 | Not applicable — grading is deterministic CSV scoring with no LLM in the evaluation path, so there is no executor/reviewer pairing to make cross-family. |
| Runtime assurance | 1 | Deterministic grading plus optional extras (a rule-violation detector and a plagiarism detector) and obfuscated competition descriptions; these are post-submission checks with no in-flight gating of an agent's run. |
| Cross-platform portability | 2 | Deliberately agent-agnostic — three open-source scaffolds demonstrated and leaderboard entrants have run it with OpenAI, Anthropic, Google and DeepSeek models — but the harness itself needs Linux, Docker and the Kaggle API. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `code-generation`


**Architectural features:** `tool-use`


**Inputs:** `kaggle-competition-tasks` `agent-implementation`


**Outputs:** `submission-csv` `medal-scores` `grading-reports`


**Data sources:** `kaggle-competition-datasets`


**Knowledge sources:** `kaggle-human-leaderboards`


## Limitations

- Leaderboard submissions have been paused since 2026-04-24 'while we develop an improved process for ensuring submissions are fair and comparable', so the ranking is frozen mid-race.
- Most top submissions publish grading reports but not source code (the leaderboard's 'Source Code Available' column reads X for the leaders), so the highest scores cannot be independently reproduced.
- Known contamination and leakage problems are catalogued rather than fixed — including test-label leakage in some competitions — and deferred to a prospective v2.
- Costly at scale: 3.3 TB for the full set (158 GB for Lite), roughly two days of dataset preparation, and a canonical setup of 24 hours on 36 vCPUs / 440 GB RAM / one A10 GPU per run, at three seeds.
- Kaggle competitions measure ML engineering, not research: no hypothesis, identification, literature or write-up dimension, and medal thresholds are frozen snapshots of human leaderboards that no longer move.
- Increasingly saturated at the easy end — Lite-split scores above 80% leave little headroom — and the code has not been touched since 2026-04-24.
- The MIT licence covers only the harness; redistributing the competition data is not permitted, which complicates archival replication.

## Related projects in this catalog

- [`paperbench`](paperbench.md)
- [`mlgym`](mlgym.md)
- [`airs-bench`](airs-bench.md)
- [`rd-agent`](rd-agent.md)
- [`asta-bench`](asta-bench.md)

## Papers describing this project

- **MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering** — Chan, J. S., Chowdhury, N., Jaffe, O., Aung, J., Sherburn, D., Mays, E., Starace, G., Liu, K., Maksin, L., Patwardhan, T., Weng, L., Mądry, A. (2024). *ICLR 2025 (Oral); arXiv:2410.07095*. [arXiv:2410.07095](https://arxiv.org/abs/2410.07095)

## Related references (literature catalog)

- Chan, J. S. et al. (2024). [*MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering*](../papers/notes/chan2024mlebench.md) `chan2024mlebench`
