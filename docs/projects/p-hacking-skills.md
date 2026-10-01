<!-- DO NOT EDIT — auto-generated from projects/landscape/p-hacking-skills.yml by scripts/build_indexes.py -->

# p-hacking-skills (phack)

`external` · status: `active` · focus: `analysis` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/brycewang-stanford/p-hacking-skills>

**Licence:** `MIT`

**Source:** [`projects/landscape/p-hacking-skills.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/p-hacking-skills.yml)

## Positioning

An instrumented specification-search engine, packaged both as a `phack` PyPI CLI and as 11 Claude Code/Codex skills, that measures how quickly and how often realistic agent-driven specification searches manufacture p < .05 on econometric data whose true effect is exactly zero by construction (OLS/RCT, DiD, staggered DiD, RDD, IV). It sits in RISE's evaluation/audit layer rather than the production layer: its job is to measure a research-integrity risk of AI research agents, not to help write a paper.

## Distinctive contribution

The first tool in this catalog purpose-built to benchmark AI agents' propensity to p-hack, following up on Asher et al. (2026)'s finding that Claude Opus 4.6 and GPT-5.2 Codex both refuse an explicit request to manufacture significance but comply once it is reframed as "report the most significant specification you can find." It unifies simulation (re-implemented phackR strategies), real-design specification search across four languages (Stata, R, Python, StatsPAI), a detection battery (Elliott-Kudrin-Wüthrich, p-curve, caliper/bunching tests), and third-party verification (`phack verify`) in one ledger format, and is mechanically constrained so that no search can report a "winning" specification without also emitting the full search ledger and a null-calibrated honest p-value.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Touches one stage — specification-search / analysis auditing — by design; it is an evaluation instrument, not a research-production pipeline. |
| Autonomy level | 0 | A tool invoked per search (CLI or skill call); it does not run an autonomous research task of its own. |
| Architectural transparency | 3 | Full open-source Python engine, CLI, 11 skills, design-card schema, and benchmark/eval scripts on GitHub with passing CI. |
| Inputs supported | 1 | One input form (a dataset plus a JSON design card) with no literature or external data-source access, though four language backends are supported. |
| Outputs / reproducibility | 3 | Every run is a seeded, verifiable directory (ledger, specification curve, honest p-value) that `phack verify` can independently check; eight bundled datasets ship with documented DGPs and fixed seeds. |
| Internal evaluation | 2 | Reports its own measured false-positive-rate tables (33-97% across four designs) against a stated methodology, building on and citing Asher et al. (2026) and the p-hacking literature it draws on, though its own tool has no independent third-party replication yet. |
| Openness | 3 | MIT license; installable via `pip install phack` or Docker, runnable in a Colab notebook with bundled demo data — reproducible end-to-end on commodity hardware. |
| Maturity / traction | 1 | 8 stars, 2 forks, PyPI release and passing CI; young (first public September 2026), single-author. |
| Cross-family policy | 0 | Not applicable — it benchmarks other models' p-hacking propensity but has no cross-family review mechanism of its own. |
| Runtime assurance | 3 | The tool is mechanically unable to report a 'best specification' without emitting the full search ledger and a null-calibrated honest p-value — gating on an audit artifact is the core design, not an add-on. |
| Cross-platform portability | 2 | Four execution backends (Stata, R, Python, StatsPAI) plus Claude Code and Codex skill interfaces. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-analysis` `code-generation`


**Architectural features:** `tool-use` `artifact-versioning` `iterative-loop`


**Inputs:** `dataset` `design-card-json`


**Outputs:** `search-ledger` `specification-curve` `null-calibrated-honest-p-value` `audit-report`


**Data sources:** `bundled synthetic null and positive-control datasets with documented DGPs`


## Limitations

- Explicitly 'not meant to be used in real paper writing or research projects' per its own RESPONSIBLE_USE.md — it is an audit/teaching/benchmark instrument.
- Demonstrated designs are limited to four econometric families (DiD, staggered DiD, RDD, IV); no RCT, meta-analysis, or qualitative-data p-hacking forms yet.
- Very young (8 stars, first release 2026); its own measured capability tables have no independent replication yet.

## Related projects in this catalog

- [`ralph-wiggum-asset-pricing`](ralph-wiggum-asset-pricing.md)
- [`repro-bench`](repro-bench.md)
- [`socsci-repro-bench`](socsci-repro-bench.md)
- [`social-science-replicability`](social-science-replicability.md)
- [`stata-code`](stata-code.md)
