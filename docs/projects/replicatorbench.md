<!-- DO NOT EDIT — auto-generated from projects/landscape/replicatorbench.yml by scripts/build_indexes.py -->

# ReplicatorBench / ReplicatorAgent

`external` · status: `active` · focus: `replication` · discipline: `social-sciences` · started: 2026

**Project page:** <https://github.com/CenterForOpenScience/llm-benchmarking>

**Licence:** `Apache-2.0`

**Source:** [`projects/landscape/replicatorbench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/replicatorbench.yml)

## Positioning

A benchmark plus reference agent for evaluating whether LLM agents can replicate empirical findings in the social and behavioral sciences end-to-end: extracting replication-relevant metadata and data from a paper's PDF, designing and generating a replication analysis, executing it in a sandboxed Docker environment, interpreting the statistical results, and validating the verdict against expert-annotated human-coded ground truth. Sits in the RISE evaluation-infrastructure layer alongside core-bench, reprorepo, and repro-bench, but is purpose-built for social/behavioral-science replicability rather than ML-paper or natural-science reproduction.

## Distinctive contribution

Built by the Center for Open Science — the nonprofit behind OSF and the large-scale Reproducibility Projects in psychology and cancer biology — and funded by a Coefficient Giving grant explicitly targeting "Benchmarking LLM Agents on Consequential Real-World Tasks." The benchmark pairs human-verified replicable/non-replicable claims with an LLM-as-judge validator rather than self-reported scores, and the companion paper ("ReplicatorBench: Benchmarking LLM Agents for Replicability in Social and Behavioral Sciences") was accepted to the inaugural AI4Sciences track at KDD 2026.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Covers extraction, research design, code generation, execution/analysis, and the replication verdict itself — five stages, but no literature or paper-drafting component. |
| Autonomy level | 2 | ReplicatorAgent runs extraction-through-validation without per-step human approval on a fixed benchmark task, but the system is operated as a research/benchmarking harness, not a self-directed research agent. |
| Architectural transparency | 3 | Full pipeline published (info_extractor/generator/interpreter/validator), with prompt templates, JSON schemas, and the paper's methodology. |
| Inputs supported | 2 | Two input forms (paper PDF + accompanying dataset/data files) with the paper itself as the knowledge source; no broader literature-corpus or idea/RQ input. |
| Outputs / reproducibility | 2 | Persists replication code, analysis reports, and a verdict per benchmark item, but no versioned end-to-end artifact manifest demonstrated publicly. |
| Internal evaluation | 2 | Core design is a systematic benchmark: agent verdicts scored by an LLM-as-judge against expert-annotated ground truth; companion paper accepted to KDD 2026 AI4Sciences track. |
| Openness | 2 | Apache-2.0, permissive; running it requires Docker sandboxing and LLM API access, so not zero-friction on commodity hardware. |
| Maturity / traction | 1 | 9 stars, 325 commits, young (created 2026); credible institutional backing (COS + three university partners + a dedicated grant) but minimal external community adoption yet. |
| Cross-family policy | 0 | No stated cross-model-family requirement or default; README does not describe a multi-provider review policy. |
| Runtime assurance | 1 | Sandboxed execution catches runtime/syntax failures in generated code; the LLM-as-judge validator is framed as benchmark scoring (post-hoc), not an in-flight integrity gate. |
| Cross-platform portability | 1 | Single benchmark framework targeting one agent implementation (ReplicatorAgent); no stated multi-IDE or multi-runtime support. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `data-acquisition` `research-design` `code-generation` `data-analysis` `replication`


**Architectural features:** `dag-orchestration` `tool-use`


**Inputs:** `paper-pdf` `dataset`


**Outputs:** `replication-code` `replication-report` `replication-verdict`


**Data sources:** `paper-supplied-datasets`


**Knowledge sources:** `paper-pdf-metadata`


## Limitations

- Very young repo (9 stars); KDD 2026 acceptance covers the benchmark paper, not independent third-party use of the released code.
- Benchmark size/coverage statistics are not disclosed in the public README.
- Requires Docker sandboxing and LLM API access to reproduce a run.
- The companion 'robustness' module is explicitly marked as an in-progress scaffold, underdeveloped relative to the replication module.

## Related projects in this catalog

- [`core-bench`](core-bench.md)
- [`reprorepo`](reprorepo.md)
- [`repro-bench`](repro-bench.md)
- [`socsci-repro-bench`](socsci-repro-bench.md)
- [`researchclaw-bench`](researchclaw-bench.md)
- [`mle-bench`](mle-bench.md)

## Papers describing this project

- **ReplicatorBench: Benchmarking LLM Agents for Replicability in Social and Behavioral Sciences** — Nguyen, B., Soós, D., Ma, Q., Obadage, R. R., Ranjan, Z., Koneru, S., Errington, T. M., Nematova, S., Rajtmajer, S., Wu, J., Jiang, M. (2026). *KDD 2026 (AI4Sciences track)*. [arXiv:2602.11354](https://arxiv.org/abs/2602.11354)
