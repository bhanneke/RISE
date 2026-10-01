<!-- DO NOT EDIT — auto-generated from projects/landscape/research-harness-workflow.yml by scripts/build_indexes.py -->

# Claude Code Research Harness Workflow

`external` · status: `active` · focus: `analysis` · discipline: `social-sciences` · started: 2026

**Project page:** <https://github.com/maxwell2732/claudecode-research-harness-workflow>

**Licence:** `MIT (badge in README; no LICENSE file found in the repository)`

**Source:** [`projects/landscape/research-harness-workflow.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/research-harness-workflow.yml)

## Positioning

A seven-stage controlled-execution framework (setup -> audit -> clean -> plan -> work -> review -> release) that constrains Claude Code to produce auditable, reproducible empirical research rather than general-purpose "vibe coding." Raw data is read-only, every cleaning and merge decision must leave a script and a log, every analysis task needs a script/log/output triple before it can be marked complete, and causal claims are checked against the declared identification strategy before a replication package is released. A separate standalone mode extracts paper-matched, analysis-ready subsamples and codebooks from raw multi-wave survey panels, for reproducing a published paper's sample construction before extending or re-estimating it.

## Distinctive contribution

Targets the data-cleaning/merging stage as the primary locus of silent failure (undocumented edits, broken merge keys reported as "done," causal language outrunning the identification design) rather than treating drafting or ideation as the hard part. The paper-subsample mode is concrete and checkable: a three-script pipeline (discover_vars -> subsample -> codebook) produces a codebook that flags each reconstructed variable CLOSE / MODERATE / DIFFERS against the published paper's own descriptive-statistics table, with required notes on any DIFFERS entry before it counts as ready.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Covers audit, cleaning, planning, execution, review and release — roughly 5 adjacent stages — but no literature, ideation or drafting stage. |
| Autonomy level | 2 | Supervised agent: a human writes/approves the research contract and analysis plan, then the agent executes within pre-approved bounds and halts when evidence breaks. |
| Architectural transparency | 3 | Full rules, checkpoints and agent/skill configuration (CLAUDE.md and seven /research-harness-* commands) are published in the repo. |
| Inputs supported | 2 | Multiple input forms — raw survey data, a written research specification, and (in the subsample mode) a published paper to reproduce — though no literature-corpus or external data-source connector. |
| Outputs / reproducibility | 3 | Produces a versioned replication package (scripts + logs + outputs + report) and is itself archived with a Zenodo DOI. |
| Internal evaluation | 2 | Systematic internal check: the subsample codebook quantitatively compares reconstructed variable means against a published paper's own descriptive-statistics table and flags mismatches. |
| Openness | 1 | README displays an MIT license badge, but no LICENSE file is present in the repository at scoring date — terms are not formally confirmed. |
| Maturity / traction | 1 | 40 stars and 49 forks with a Zenodo archival DOI, but single-author, pre-1.0, and documented primarily in Chinese. |
| Cross-family policy | 0 | Single-model (Claude Code) by design; no cross-family review mechanism. |
| Runtime assurance | 2 | Multiple in-pipeline gates: read-only raw-data protection, mandatory merge diagnostics, and an identification/causal-language review stage before release. |
| Cross-platform portability | 0 | Built specifically around Claude Code's slash-command/skill mechanism; not documented for other agent runtimes. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-acquisition` `data-analysis` `code-generation` `revision-editing` `replication`


**Architectural features:** `human-in-loop` `tool-use` `dag-orchestration` `iterative-loop`


**Inputs:** `raw-survey-data` `research-specification` `published-paper-for-reproduction`


**Outputs:** `cleaned-panel-data` `codebook` `cleaning-and-merge-logs` `analysis-scripts` `tables-figures` `replication-package`


**Data sources:** `multi-wave household/social survey panels (user-supplied, not a named API)`


## Limitations

- No LICENSE file found in the repository despite an MIT badge in the README — licensing terms are unconfirmed.
- Documentation is primarily in Chinese and the workflow is tightly coupled to Claude Code's command mechanism, limiting portability.
- Internal validation (the CLOSE/MODERATE/DIFFERS codebook check) covers the cleaning/subsample-extraction stage only; there is no broader benchmark or third-party audit of the full seven-stage pipeline.

## Related projects in this catalog

- [`clo-author`](clo-author.md)
- [`repro-bench`](repro-bench.md)
- [`reprorepo`](reprorepo.md)
- [`core-bench`](core-bench.md)
