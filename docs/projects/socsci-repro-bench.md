<!-- DO NOT EDIT — auto-generated from projects/landscape/socsci-repro-bench.yml by scripts/build_indexes.py -->

# SocSci-Repro-Bench

`external` · status: `dormant` · focus: `replication` · discipline: `social-sciences` · started: 2026

**Project page:** <https://github.com/malizad/SocSci-Repro-Bench>

**Source:** [`projects/landscape/socsci-repro-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/socsci-repro-bench.yml)

## Positioning

A benchmark of 221 reproduction tasks drawn from 54 published social-science papers across four disciplines (political science, sociology, economics, psychology) and roughly a dozen substantive domains, where an agent must execute the authors' own analysis code in R, Python or Stata and extract the target quantitative result. The repo holds the gold answers (`SocSci_Repro_Bench.json`), the research questions (`SocSci_Repro_Bench_RQ.json`) and paper metadata (`SocSci_Repro_Bench_Metadata.json`); the anonymised replication materials for all 54 papers live on Harvard Dataverse. Sits in the RISE evaluation-infrastructure layer next to social-science-replicability and reprorepo, and is the only entry there that scores computational reproducibility on social-science papers with Stata in the loop.

## Distinctive contribution

Two design choices make it a real test rather than a pass-rate exercise. First, the task set deliberately includes papers that are *not* reproducible because materials are missing, marked "No Data" or "No Code or Data", so an agent can be wrong by succeeding — a hallucinated result on an infeasible task is scored as failure. Second, it reports a paper-level metric alongside the task-level one: the repo README gives Claude Code 93.4% task-level but only 78.0% paper-level, and Codex 62.1% and 35.8%, exposing how much task-level accuracy overstates whether a paper actually reproduces.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage: a task set targeting replication. It produces no scholarship itself — the coverage lives entirely in the agents being measured. |
| Autonomy level | 0 | Static JSON task set curated by the authors; all agency belongs to the coding agents attempting the tasks. |
| Architectural transparency | 2 | Gold answers, research questions and paper metadata are published as three documented JSON files, and the paper describes the task construction — but the repo ships no scoring harness, no agent prompts and no run configs, so the measured pipeline cannot be inspected. |
| Inputs supported | 1 | One input form (a reproduction task = paper metadata + research question + the authors' code and data), with data access supplied off-repo via the anonymised Harvard Dataverse deposit; no standardized agent interface. |
| Outputs / reproducibility | 0 | No system outputs. The gold-answer JSON is a durable artifact, but with no runner or scoring script in the repo the reported Claude Code and Codex accuracies cannot be regenerated from what is published here. |
| Internal evaluation | 2 | Systematic evaluation of two frontier coding agents across all 221 tasks, reported at both task and paper level in a companion arXiv preprint (2606.11447, submitted 2026-06-09); not peer-reviewed at scoring date and no third-party replication of the measurement. |
| Openness | 1 | The repo page states CC BY 4.0 but the GitHub API reports 'Other (NOASSERTION)', so terms are ambiguous; the materials themselves are gated behind an off-repo anonymised Dataverse deposit, some tasks require a commercial Stata license, and no harness is provided — reproducing the headline numbers is not possible from the repo alone. |
| Maturity / traction | 1 | 13 stars, 1 fork, 7 commits, all on 2026-03-06 — created and last pushed the same day, untouched since. Credible author team (Zurich / NYU) and a widely-noticed preprint, but no external users or releases. |
| Cross-family policy | 0 | Not applicable — a static task set with no runtime and no policy on solving systems. The paper does compare across families (Claude Code vs Codex), but that is the object of measurement, not a cross-family review requirement. |
| Runtime assurance | 0 | No runtime, so no in-flight checks. The 'No Data' / 'No Code or Data' traps are an integrity property of the *benchmark design*, catching agent overclaiming after the fact rather than gating a pipeline as it runs. |
| Cross-platform portability | 3 | Plain JSON gold answers plus a Dataverse deposit, agent-agnostic and format-minimal; already exercised against two entirely different agent stacks, and the tasks span three analysis languages, so nothing in the artifact assumes a runtime. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `replication`



**Inputs:** `published-paper-with-author-materials`


**Outputs:** `gold-answer-set` `research-questions` `paper-metadata`


**Data sources:** `harvard-dataverse`


**Knowledge sources:** `published-social-science-corpus`


## Limitations

- No evaluation harness, scoring script or leaderboard in the repo, so the reported 93.4% / 78.0% and 62.1% / 35.8% figures are not independently reproducible from what is published.
- License ambiguity: repo page says CC BY 4.0, GitHub API reports NOASSERTION.
- Untouched since its creation day (2026-03-06), so the task set will not track newer agents or newly deposited papers.
- Gold answers are published in plain JSON in a public repo — a standing training-contamination risk for any agent evaluated after the release date.
- Measures the easier reproduction task: reproducing a result *from the authors' own code*, not rebuilding the analysis from methods and data as social-science-replicability does.
- Replication materials are anonymised and hosted off-repo on Dataverse; some tasks additionally require a commercial Stata license.
- The arXiv abstract does not state the headline percentages — the accuracy figures come from the repo README, so the two sources should be cited distinctly.

## Related projects in this catalog

- [`social-science-replicability`](social-science-replicability.md)
- [`reprorepo`](reprorepo.md)
- [`repro-bench`](repro-bench.md)
- [`core-bench`](core-bench.md)
- [`paperbench`](paperbench.md)

## Papers describing this project

- **AI Coding Agents Can Reproduce Social Science Findings** — Alizadeh, M., Mosleh, M., Gilardi, F., Kasirzadeh, A., Tucker, J. (2026). *arXiv*. [arXiv:2606.11447](https://arxiv.org/abs/2606.11447)

## Related references (literature catalog)

- `alizadeh2026coding` ([BibTeX](https://github.com/bhanneke/RISE/blob/main/papers/references.bib))
