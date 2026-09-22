<!-- DO NOT EDIT — auto-generated from projects/landscape/repro-bench.yml by scripts/build_indexes.py -->

# REPRO-Bench

`external` · status: `dormant` · focus: `replication` · discipline: `social-sciences` · started: 2024

**Project page:** <https://github.com/uiuc-kang-lab/REPRO-Bench>

**Source:** [`projects/landscape/repro-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/repro-bench.yml)

## Positioning

A benchmark of 112 task instances, each a published social-science paper paired with its author-supplied reproduction package and a public reproduction report, where the agent must return a *verdict* on whether the paper reproduces rather than merely re-run its code. Given only the paper PDF and the package, the agent has to locate the reported claims, execute heterogeneous code across several languages and data formats, and judge whether the output is consistent with what the paper says. Sits in the RISE evaluation-infrastructure layer beside core-bench, socsci-repro-bench and reprorepo, and occupies the assessment-judgment end of that layer rather than the code-execution end.

## Distinctive contribution

The gold labels come from real published reproduction reports, so the target is the human reproducibility *decision* — does this paper reproduce? — instead of a numerical match against a known answer, and the tasks deliberately keep real-world complexity (mixed languages, mixed data formats, full packages) rather than pre-simplified capsules. The headline result is the catalog's strongest published evidence that agents cannot yet stand in for a reproducibility referee: the best of three off-the-shelf agents (SWE-agent, AutoGPT, CORE-Agent) reaches only 21.4% accuracy, and the authors' own REPRO-Agent improves that best figure by 71% relative — published at ACL 2025 Findings.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage (replication): a task set for reproducibility-assessment agents, not a system that produces scholarship. |
| Autonomy level | 2 | Each baseline runs unattended over the task set via a run_all.sh script once the 183 GB dataset is in place; no per-task human approval, but no automated grading step is published either. |
| Architectural transparency | 1 | The ACL paper documents the benchmark design and REPRO-Agent at a high level, but the repo holds only three vendored third-party agent frameworks with run_all.sh wrappers, a 819-byte README and ground_truth.json — REPRO-Agent itself, its prompts, and any grading code are not identifiable in the repo. |
| Inputs supported | 2 | Two input forms per task (original paper PDF plus the full reproduction package) with deliberate diversity of data formats and programming languages; no literature-corpus or external data-source connector. |
| Outputs / reproducibility | 1 | Agent verdicts are checkable against a 1.7 KB ground_truth.json in the repo, but no grading script, run logs, or result artifacts are published, so the reported accuracies cannot be regenerated from the repo alone. |
| Internal evaluation | 3 | Peer-reviewed at ACL 2025 Findings (DOI 10.18653/v1/2025.findings-acl.1210) with three agents evaluated end-to-end and an ablation-driven follow-on agent; 23 citations on Semantic Scholar. |
| Openness | 1 | Code and data are publicly downloadable, but there is no license file in the repo and none on the Hugging Face dataset card at scoring date — reuse terms are undefined. |
| Maturity / traction | 2 | ACL Findings publication, 23 citations and 4,737 Hugging Face dataset downloads in the last month indicate real external use, but the repo is minimal (3 commits, 11 stars, 2 forks) and has not been pushed since 2025-11-03. |
| Cross-family policy | 0 | No cross-family mechanism or recommendation; the three evaluated baselines are single-agent scaffolds run against one model each. |
| Runtime assurance | 0 | No in-flight integrity mechanisms of REPRO-Bench's own design — whatever logging exists is inherited from the vendored SWE-agent/AutoGPT scaffolds, and correctness is decided post-hoc against ground_truth.json. |
| Cross-platform portability | 1 | Three vendored agent frameworks are supported, but through a single execution path (bash run_all.sh scripts against a git-lfs dataset) with no documented provider or runtime abstraction. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `replication`


**Architectural features:** `tool-use`


**Inputs:** `paper-pdf` `reproduction-package`


**Outputs:** `reproducibility-verdicts` `accuracy-scores`


**Data sources:** `reproduction-packages`


**Knowledge sources:** `public-reproduction-reports`


## Limitations

- The repo exists (github.com/uiuc-kang-lab/REPRO-Bench) but carries no license file, and the Hugging Face dataset card (chuxuan/REPRO-Bench) shows no license either — reuse terms are unclear, which caps the openness score at 1.
- REPRO-Agent, the paper's own contribution and the source of the headline 71% improvement, is not identifiable as a separate component in the repo; only the three vendored baselines with run_all.sh wrappers are present, so the improvement cannot be reproduced from what is published.
- The dataset is 183 GB behind git-lfs — not runnable on commodity hardware without substantial storage and bandwidth, and the Hugging Face viewer reports inconsistent formats across splits.
- Dormant and thin: 3 commits total, last push 2025-11-03, no setup documentation beyond three run commands, no grading script.
- Instances are restricted to papers that already have a public reproduction report, which skews the sample toward journals and services running mandatory verification; results need not transfer to fields without that infrastructure.
- The repo README titles the paper '...Social Science Papers?' while the arXiv and ACL versions read '...Social Science Research?' — a minor metadata inconsistency.

## Related projects in this catalog

- [`core-bench`](core-bench.md)
- [`socsci-repro-bench`](socsci-repro-bench.md)
- [`social-science-replicability`](social-science-replicability.md)
- [`reprorepo`](reprorepo.md)

## Papers describing this project

- **REPRO-Bench: Can Agentic AI Systems Assess the Reproducibility of Social Science Research?** — Hu, C., Zhang, L., Lim, Y., Wadhwani, A., Peters, A., Kang, D. (2025). *Findings of the Association for Computational Linguistics: ACL 2025*. [arXiv:2507.18901](https://arxiv.org/abs/2507.18901) · [doi](https://doi.org/10.18653/v1/2025.findings-acl.1210)

## Related references (literature catalog)

- Hu, C. et al. (2025). [*REPRO-Bench: Can Agentic AI Systems Assess the Reproducibility of Social Science Research?*](../papers/notes/hu2025reprobench.md) `hu2025reprobench`
