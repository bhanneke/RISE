<!-- DO NOT EDIT — auto-generated from projects/landscape/reclaim.yml by scripts/build_indexes.py -->

# RECLAIM

`external` · status: `active` · focus: `replication` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/mithils3/reclaim>

**Licence:** `MIT (code); CC BY 4.0 (datasets/run records)`

**Source:** [`projects/landscape/reclaim.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/reclaim.yml)

## Positioning

A reproducibility benchmark of 100 NeurIPS 2025 papers that asks whether autonomous agents can recover a paper's pinned central empirical result under a fixed GPU-hour budget. Papers are stratified into three tiers by what the authors actually released — Run (code+data+weights), Retrain (no weights), Reimplement (no code) — so difficulty tracks artifact completeness rather than topic. Sits alongside `core-bench`, `paperbench`, and `repro-bench` in the RISE replication/evaluation-infrastructure layer, but is explicitly tiered and designed to be rebuilt yearly from each new conference cycle.

## Distinctive contribution

Unlike pass/fail replication leaderboards, RECLAIM ships full execution traces for all 372 graded runs (audit data, not just scores), is built to regenerate itself annually from new conference releases, and quantifies how reproduction rate collapses with release completeness (41% at Run tier down to 15% at Reimplement tier across four agents).

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Declared stages are replication and code-generation (retrain/reimplement tiers); no ideation, design, or write-up coverage. |
| Autonomy level | 3 | Reference agents run end-to-end within a 96 H100-hour GPU budget to recover the pinned target metric, without per-step human approval. |
| Architectural transparency | 3 | Full agent codebase (reclaim_repro, reclaim_claude), cluster scripts, and 372 run transcripts published. |
| Inputs supported | 1 | Single bundled input form (paper + its own released artifacts); no external literature or data-source access beyond that. |
| Outputs / reproducibility | 3 | Versioned run records with full transcripts and audit data, reproducible via provided Slurm/Apptainer cluster scripts. |
| Internal evaluation | 2 | Systematic evaluation across 4 agents x 100 papers (400 agent-paper cells); paper is under review, not yet externally validated. |
| Openness | 2 | Permissive licensing (MIT code / CC BY 4.0 data), but the declared 96 H100-hour-per-paper budget is far from commodity hardware. |
| Maturity / traction | 1 | 0 stars, repo marked 'anonymized ... under review' as of scoring date; brand-new (Sept 2026), single-team artifact. |
| Cross-family policy | 0 | Benchmarks separate agent runs for comparison, not a cross-family executor/reviewer design; each run uses one agent/model. |
| Runtime assurance | 2 | Grading is verified through execution traces matched against pinned target metrics — a runtime audit gate, not just a final score. |
| Cross-platform portability | 2 | Evaluates multiple agents/backbones (reference agent package plus 3 others) and ships Slurm/Apptainer cluster portability. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `replication` `code-generation`


**Architectural features:** `tool-use` `iterative-loop`


**Inputs:** `ML paper + whatever artifacts (code/data/weights) its authors released`


**Outputs:** `reproduction success/fail verdict per paper` `execution traces` `leaderboard`


**Data sources:** `NeurIPS 2025 paper release artifacts`


**Knowledge sources:** `HuggingFace dataset (Mithilss/reclaim)`


## Limitations

- Requires a 96 H100-hour GPU budget per paper — not reproducible on commodity hardware.
- Repository is explicitly an 'anonymized ... under review' release; long-term maintenance/governance is unclear.
- ML/NeurIPS-specific; no economics or social-science papers in the benchmark.

## Related projects in this catalog

- [`core-bench`](core-bench.md)
- [`paperbench`](paperbench.md)
- [`repro-bench`](repro-bench.md)
- [`reprorepo`](reprorepo.md)
- [`researchclaw-bench`](researchclaw-bench.md)

## Papers describing this project

- **RECLAIM: Can Agents Reproduce the Claims of Machine Learning Papers?** — Salunkhe, M., Ding, H., Verma, S., Kindratenko, V. (2026). *arxiv*. [arXiv:2609.28850](https://arxiv.org/abs/2609.28850)
