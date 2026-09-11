<!-- DO NOT EDIT — auto-generated from projects/landscape/karpathy-autoresearch.yml by scripts/build_indexes.py -->

# autoresearch (Karpathy)

`external` · status: `dormant` · focus: `analysis` · discipline: `computer-science` · started: 2026

**Project page:** <https://github.com/karpathy/autoresearch>

**Source:** [`projects/landscape/karpathy-autoresearch.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/karpathy-autoresearch.yml)

## Positioning

The origin point of the "autoresearch" category rather than a research tool: a ten-file scaffold in which an AI coding agent repeatedly edits train.py, trains a single-GPU nanochat language model for exactly five minutes, scores the result by validation bits-per-byte, and keeps or discards the change. It touches only the hypothesis → code → measure loop; there is no literature stage, no write-up, and no orchestration code — the agent is whatever harness you point at program.md. Listed here for lineage: autoresearchclaw, aris and faros all descend from this repo, and the awesome-autoresearch lists treat it as the category's reference point.

## Distinctive contribution

It fixed the template the whole downstream family inherited — a frozen data/eval harness (prepare.py) the agent may not touch, one mutable artifact (train.py), a plain-markdown instruction file (program.md) that any agent runtime can consume, and a single cheap objective metric with a hard five-minute budget so an unsupervised loop cannot win by spending more compute. At 95,362 stars and 13,405 forks it is by a wide margin the highest-traction artifact in the RISE landscape, and the forks are the mechanism by which the pattern spread.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 1 | Three adjacent stages only — propose a change, implement it in train.py, measure val_bpb; no literature, no research design, no drafting, no review. |
| Autonomy level | 2 | The modify/train/evaluate loop is meant to run unsupervised, but the repo ships no orchestrator: a human writes and maintains program.md, chooses the agent harness, and reads the resulting curve, so effective autonomy is set by the harness you bring. |
| Architectural transparency | 2 | Everything in the repo is public and readable (train.py, prepare.py, program.md, analysis.ipynb), and program.md is the agent instruction in plain markdown — but there is no agent implementation, topology, or evaluation harness here to document, so the orchestration layer is undocumented by construction. |
| Inputs supported | 0 | One narrow input form — the fixed nanochat data prepared by prepare.py — with no literature access, no external data sources, and no way to point it at a different research object. |
| Outputs / reproducibility | 1 | Persists code diffs, val_bpb numbers and progress.png but no prose artifact of any kind; the fixed five-minute budget and single metric make successive runs comparable, though nothing is packaged for replay. |
| Internal evaluation | 1 | Every candidate change is scored on val_bpb against the baseline, and the author's own progress.png shows one run's trajectory — but no aggregate study of whether the loop reliably discovers improvements, no benchmark, and no paper. |
| Openness | 1 | No LICENSE, LICENSE.md or COPYING file at the repository root and the GitHub API reports no licence, so despite 13,405 forks the code is source-available but legally unlicensed; it also needs a single NVIDIA GPU (tested on H100), so it is not commodity-hardware reproducible. |
| Maturity / traction | 2 | Score carried entirely by traction, not maturity: 95,362 stars and 13,405 forks with a whole downstream category descending from it, against 36 commits, no releases, no packaging, and nothing pushed since 2026-03-26. |
| Cross-family policy | 0 | No reviewer role exists — the only judge is the val_bpb metric — so there is nothing for a cross-family policy to apply to. |
| Runtime assurance | 1 | Exactly one in-flight gate: a change is kept only if it improves validation bits-per-byte on a fixed five-minute run; no claim checking, no code audit, no second opinion. |
| Cross-platform portability | 2 | Agent-runtime-agnostic by design — program.md is a plain markdown instruction file with no framework coupling, so any coding agent can drive it — but the execution environment is hardware-locked to one NVIDIA GPU (H100-tested), with community forks required for other accelerators. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `hypothesis-generation` `code-generation` `data-analysis`


**Architectural features:** `iterative-loop` `tool-use`


**Inputs:** `baseline-training-script` `agent-instruction-file`


**Outputs:** `modified-training-code` `validation-metrics` `progress-chart`


**Data sources:** `fixed-nanochat-corpus`


## Limitations

- Unlicensed: no LICENSE file in the repo and GitHub reports none, so the 13,405 forks and every derivative rest on unclear reuse terms. (The README carries an MIT badge-style claim that no licence file substantiates.)
- Quiet since 2026-03-26 with 36 commits total and 194 open issues — a demonstration that was released and left, not a maintained project.
- The research domain is LLM training on a single GPU, not science: there is no literature stage, no manuscript, and no transfer to empirical social-science work. This is a lineage entry, not a usable tool for economics research.
- Requires a single NVIDIA GPU (H100-tested), no distributed training, and platform-specific code.
- No paper and no systematic evaluation of the agent loop itself — only one author-run progress curve.

## Related projects in this catalog

- [`autoresearchclaw`](autoresearchclaw.md)
- [`aris`](aris.md)
- [`faros`](faros.md)
- [`deepscientist`](deepscientist.md)
