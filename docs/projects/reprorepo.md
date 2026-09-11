<!-- DO NOT EDIT — auto-generated from projects/landscape/reprorepo.yml by scripts/build_indexes.py -->

# ReproRepo

`external` · status: `active` · focus: `replication` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/LithiumDA/ReproRepo>

**Source:** [`projects/landscape/reprorepo.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/reprorepo.yml)

## Positioning

A framework (arXiv:2606.18237) for building issue-grounded reproducibility-audit benchmarks from paper-repository pairs: it collects conference paper metadata and repo links, curates reproducibility-related GitHub issues via LLM review, pins fixed paper/repository snapshots, runs blind static-audit agents, and scores whether agent findings match hidden human-reported reproduction blockers. Evaluated at scale on 1,149 ML papers. Sits in the RISE evaluation-infrastructure layer and speaks directly to the replication-infrastructure interest.

## Distinctive contribution

Uses human-raised GitHub issues as naturally occurring ground truth for reproducibility auditing — sidestepping both expensive expert annotation and full re-execution — under a blind protocol in which agents audit paper + repo snapshots without ever seeing the hidden issues. The best baseline (Codex with GPT-5.5) surfaces at least one semantically related human-reported blocker for roughly 90% of papers; the CMU team includes Shah, Talwalkar, Dettmers, and Yang.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Audit / benchmark infrastructure targeting the replication stage; does not produce scholarship itself. |
| Autonomy level | 0 | Scripted benchmark-construction pipeline; the audit agents (Codex, Claude Code) are baselines under evaluation, not the system's own agency. |
| Architectural transparency | 3 | Full pipeline code, prompt and repository-text ablation variants, runner wrappers with Dockerfiles, and step-by-step pipeline documentation. |
| Inputs supported | 1 | One composite input form (paper PDF + pinned repository snapshot) plus GitHub-issue and OpenReview/Paper-Copilot metadata access. |
| Outputs / reproducibility | 1 | Only lightweight aggregate CSVs are released; benchmark cases, snapshots, and agent outputs must be regenerated with credentials and nondeterministic LLM stages. |
| Internal evaluation | 2 | Systematic evaluation across 1,149 papers with ablations and run-variance analysis; arXiv preprint, not yet peer-reviewed. |
| Openness | 2 | MIT-licensed, uv-managed, with an API-free smoke test; full pipeline requires GitHub plus model API credentials and data regeneration. |
| Maturity / traction | 1 | Weeks old (June 2026), 6 stars, single-team use; prominent CMU authorship (Shah, Talwalkar, Dettmers, Yang). |
| Cross-family policy | 1 | Audit runners (Codex CLI, Claude Code, DeepSeek-backed) and the LLM issue-review/alignment stages are separately configurable — cross-family judging is possible but not a stated policy. |
| Runtime assurance | 1 | Structured issue-case schema, LLM accept/reject case filtering, and the blind-snapshot protocol gate benchmark construction; no runtime audit stack. |
| Cross-platform portability | 2 | Three runner back-ends (Codex CLI, Claude Code, Claude Code with DeepSeek) with Dockerfiles — three model providers. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `replication`


**Architectural features:** `tool-use`


**Inputs:** `paper-repository-pairs` `github-issues`


**Outputs:** `benchmark-case-sets` `audit-findings` `alignment-scores`


**Data sources:** `github-issues` `openreview-metadata`


**Knowledge sources:** `human-reported-issues`


## Limitations

- Ground truth covers only blockers users chose to report as GitHub issues; silent or unreported reproducibility failures are invisible to the benchmark.
- Static audits only — agents read paper and repository without executing code, so failures that surface only at runtime are out of scope.
- Released artifacts are aggregate result tables; rebuilding the full benchmark depends on live GitHub state, API credentials, and nondeterministic LLM curation stages.

## Related projects in this catalog

- [`social-science-replicability`](social-science-replicability.md)
- [`paper2code`](paper2code.md)
- [`asta-bench`](asta-bench.md)
- [`mlgym`](mlgym.md)

## Papers describing this project

- **ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues** — Li, S., Wei, Q. A., Tang, J., Chen, V., Shah, N. B., Dettmers, T., Yang, Y., Talwalkar, A. (2026). *arXiv*. [arXiv:2606.18237](https://arxiv.org/abs/2606.18237)

## Related references (literature catalog)

- Li, S. et al. (2026). [*ReproRepo: Scaling Reproducibility Audits with GitHub Repository Issues*](../papers/notes/li2026reprorepo.md) `li2026reprorepo`
