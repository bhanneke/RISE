<!-- DO NOT EDIT — auto-generated from projects/landscape/bixbench3.yml by scripts/build_indexes.py -->

# BixBench3

`external` · status: `active` · focus: `analysis` · discipline: `biomedical` · started: 2026

**Project page:** <https://github.com/EdisonScientific/BixBench3>

**Source:** [`projects/landscape/bixbench3.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/bixbench3.yml)

## Positioning

Twenty computational-biology tasks at the scale of a whole research study, framed explicitly as *delegation* rather than autonomy: the scientist keeps the research question and the high-level method choice, and the agent implements every analysis step from the raw data of a published study up to a set of exactly specified output artifacts (138 artifacts across the 20 tasks). Grading is two-part — a deterministic grader comparing the agent's artifacts against the published ground truth with per-artifact metrics (F1, CCC, …), plus a PhDval-compatible LLM process judge scoring instruction following, transparency, analytical rigour and run-level failure modes. It is the third generation of the Future-House BixBench line (BixBench, Mitchener et al., arXiv:2503.00096 — 53 scenarios and ~300 open-answer questions, not itself catalogued in RISE) rebuilt by the same core team now at Edison Scientific, and it sits in the RISE evaluation-infrastructure layer next to LifeSciBench and HeurekaBench.

## Distinctive contribution

Honest resource accounting is the contribution the rest of the benchmark field omits: the paper reports an average of 6.8 hours, 102M tokens and $43 per task, with the longest attempts reaching 24 hours, 1.07B tokens and $525 — so the autonomy gap (scores from 0.00 to 0.48 across 13 frontier models, degrading from 0.36 on 1–2-step analyses to 0.24 on 3+ steps) is priced, not just measured. It also runs an LLM-adjudicated network gateway around the agent during the run, logging and policing outbound requests so a task cannot be solved by retrieving the published paper's own answers.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure: it grades delegated analysis work and deliberately excludes question formulation, method choice and write-up, producing no scholarship of its own. |
| Autonomy level | 0 | Static task manifests plus graders; the harness has no agency, although the agents it measures run unattended for 6.8 hours on average per task. |
| Architectural transparency | 3 | The repo publishes the CLI, GCP runner, task manifests, response schemas, the deterministic grader and metrics, and the full 12 KB `judge_prompt.md` with its eight per-artifact rubrics and ten failure-mode tags — code, prompts and configs all visible. |
| Inputs supported | 1 | One input form per task (a prompt plus an exact artifact output contract) with raw study data staged from GCS; no literature-corpus access for the agent and no alternative scaffolds beyond the shipped Inspect harness. |
| Outputs / reproducibility | 2 | Data is pinned to versioned release prefixes (gs://bixbench3-inputs/releases/v1.0.0/) and artifact grading is deterministic, but each run costs ~$43 and needs a GCP VM plus licensed 10x software, and the process-judge score is LLM-generated. |
| Internal evaluation | 2 | Systematic evaluation of 13 frontier models over 20 tasks and 138 artifacts with cost and step-count breakdowns in the companion preprint (arXiv:2608.25286, v1 2026-08-26); no peer review and no third-party replication yet. |
| Openness | 1 | CC BY-SA 4.0 covers Edison-authored code and materials — a share-alike content licence rather than an OSI-permissive software one — mirrored scientific data keeps upstream terms, and the runtime additionally requires separately licensed 10x Cell Ranger binaries the repo will not redistribute. |
| Maturity / traction | 1 | 6 stars, 0 forks, a single commit dated 2026-08-22, no leaderboard, and no external users evident 2.5 weeks after release — a fresh single-team code drop alongside the preprint. |
| Cross-family policy | 1 | The process judge and network adjudicator are pinned to openai/gpt-5.5 while the agent under test can be any provider, so cross-family grading happens by default for non-OpenAI agents but is a fixed judge choice rather than a policy, and collapses to same-family when grading OpenAI models. |
| Runtime assurance | 2 | Two in-pipeline mechanisms: an LLM-adjudicated network gateway that polices the agent's outbound requests live (broker policy plus adjudication logs), and artifact contracts validated at submission before deterministic grading and process judging. |
| Cross-platform portability | 1 | Model side spans OpenAI, Google and Anthropic via `reference_models.yaml` and the UK-AISI Inspect harness, but the runner assumes GCP n2-standard-32 VMs in us-central1-a with GCS buckets and proprietary Cell Ranger images — not portable off Google Cloud. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `code-generation`


**Architectural features:** `tool-use`


**Inputs:** `task-prompt-and-artifact-contract` `raw-study-data` `agent-implementation`


**Outputs:** `graded-artifacts` `evaluation-scores` `process-judge-report` `run-traces`


**Data sources:** `huggingface-task-dataset` `gcs-raw-inputs` `gcs-ground-truth-artifacts`


**Knowledge sources:** `source-papers`


## Limitations

- GitHub holds only the harness and grader: prompts and contracts live on HuggingFace and both the raw inputs and ground-truth artifacts sit in Google Cloud Storage buckets, so the benchmark is not self-contained.
- Running it requires a GCP project, ~$43 of model spend and ~6.8 hours per task on average (up to $525 and 24 hours), plus manually accepting 10x Genomics' EULA to obtain Cell Ranger — far outside commodity-hardware reproducibility.
- One commit, 6 stars, 0 forks and no leaderboard; there is no submission process, so cross-lab comparability depends on the authors' own reported table.
- The process judge is pinned to a single OpenAI model at a fixed effort setting; a judge API or parsing failure is merely recorded, and the judge's own accuracy is not validated against human raters in the repo.
- Deliberately scoped to delegated implementation in computational biology — no question formulation, identification, literature or write-up dimension, and nothing transferable to social-science data without new tasks.
- The predecessor BixBench (arXiv:2503.00096) is not catalogued in RISE, so the lineage's earlier scores are not directly comparable here.

## Related projects in this catalog

- [`lifescibench`](lifescibench.md)
- [`heureka-bench`](heureka-bench.md)
- [`airs-bench`](airs-bench.md)
- [`aarri-bench`](aarri-bench.md)

## Papers describing this project

- **BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks** — Koch, Z., Wassie, A. T., Valdes-Aleman, J., Lee, J., Hinks, M. M., Rodriques, S. G., White, A. D., Laurent, J. M. (2026). *arXiv*. [arXiv:2608.25286](https://arxiv.org/abs/2608.25286)

## Related references (literature catalog)

- Koch, Z. et al. (2026). [*BixBench3: Benchmarking AI agents on research-study-scale computational biology tasks*](../papers/notes/koch2026bixbench3.md) `koch2026bixbench3`
