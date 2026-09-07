<!-- DO NOT EDIT — auto-generated from projects/landscape/agon.yml by scripts/build_indexes.py -->

# Agon

`external` · status: `active` · focus: `end-to-end` · discipline: `general` · started: 2026

**Project page:** <https://github.com/AutoResearch-Factory/Agon>

**Source:** [`projects/landscape/agon.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/agon.yml)

## Positioning

A Claude Code plugin that drives a research project from a one-line topic through idea → proposal → running experiments with no human-written experimental code. Twelve role-scoped subagents (idea creator/refiner/reviewer, proposal refiner/reviewer, experiment scientist/coder/auditor/reviewer/screener, deep-lit reader, env-validator) hand off work exclusively through files on disk in a separate "artifacts" workspace, so a run is recoverable, auditable, and resumable across sessions. Sits at the literature → ideation → research-design → code/analysis slice of the pipeline; the project's own rules explicitly forbid the scientist role from ever drafting the paper, so paper-writing and dissemination are out of scope for the public plugin.

## Distinctive contribution

"Prompt Economy" (arXiv:2606.08878) applied concretely: rather than one big autonomous loop, Agon decomposes research into tick-based commands (/idea-tick, /proposal-tick, /experiment-tick, /deep-lit-tick) run unattended for hours via `--dangerously-skip-permissions`, with adversarial auditor/reviewer subagents that re-read raw result files (not the author's summarized claims) to catch drift, downgraded claims, or numbers that don't match logs before a round can be marked reviewed. Built on top of ARIS's skill and the AutoResearch- SibylSystem (both credited, not reimplemented), and reports deployment across 10+ research domains in its arXiv paper (2606.24177).

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Six stages (literature discovery/synthesis, hypothesis generation, research design, code generation, data analysis); explicitly excludes paper-drafting and dissemination by design ('scientist agent never writes the paper'). |
| Autonomy level | 3 | README states loops 'run unattended... for hours with nobody at the keyboard'; requires --dangerously-skip-permissions and recommends giving Agon its own machine/container. |
| Architectural transparency | 3 | All 12 agent prompts, 5 skills, hooks, and templates are public Markdown/Python in the repo; arXiv paper documents the Prompt Economy design principles. |
| Inputs supported | 2 | Single input form (a topic or vague idea in text) but multi-source literature access (arXiv, Semantic Scholar, OpenAlex, Google Scholar via arxiv-tools skill); no external structured-data-source integration observed. |
| Outputs / reproducibility | 2 | Every handoff persists to disk (idea/proposal/STATE/experiment-log files, code, results) and is explicitly designed to be resumable/auditable, but there is no packaged reproducibility manifest and no final paper artifact. |
| Internal evaluation | 1 | Paper describes narrative deployment across 10+ research domains; no reported benchmark scores, leaderboard, or third-party replication in the repo or abstract. |
| Openness | 2 | MIT license, public repo, runnable by anyone with a Claude Code (or DeepSeek/Grok/Codex-proxied) subscription; not fully commodity-hardware-free since it depends on a paid LLM backend. |
| Maturity / traction | 1 | Young (paper June 2026, repo active through Aug 2026), ~44 stars / 4 forks at time of review; single-team research prototype, pre-1.0. |
| Cross-family policy | 1 | Optional — README documents a claude-ds wrapper (DeepSeek) and notes the same pattern works for Codex and Grok via CLIProxyAPI, but the default path is Claude models throughout. |
| Runtime assurance | 2 | Multiple in-pipeline gates: experiment-auditor checks result files for sanity/timestamp/contradiction before claims stand, experiment-reviewer independently re-reads code/logs against claims with full repo access, and a separate novelty-check skill runs multi-source literature verification on proposals. |
| Cross-platform portability | 2 | Ships as a Claude Code plugin, but the documented backend-swap pattern (claude-ds, claude-codex, claude-grok via CLIProxyAPI) gives it 3+ effective LLM providers; still a single agent runtime (Claude Code CLI). |

*Scored on 2026-09-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-discovery` `literature-synthesis` `hypothesis-generation` `research-design` `code-generation` `data-analysis`


**Architectural features:** `multi-agent` `tool-use` `iterative-loop` `persistent-memory` `artifact-versioning`


**Inputs:** `one-line-topic` `vague-idea-description`


**Outputs:** `idea-files` `proposal-files` `experiment-code` `experiment-logs-and-results`


**Data sources:** `user-provided`


**Knowledge sources:** `arxiv` `semantic-scholar` `openalex` `google-scholar`


## Limitations

- No paper-writing or dissemination stage in the public plugin — the design explicitly forbids the scientist role from drafting manuscripts, so output is code + results + logs, not a submittable paper.
- Heavily Chinese-language agent prompts and internal docs; English-only users get the README/commands but not the full prompt text without translation.
- No reported benchmark evaluation — claims of effectiveness rest on narrative deployment description in the arXiv paper, not a scored comparison.
- Requires --dangerously-skip-permissions and hours of unattended tool/code execution; safe only in an isolated machine/container as the README itself warns.

## Related projects in this catalog

- [`aris`](aris.md)
- [`reprorepo`](reprorepo.md)
- [`autoresearchclaw`](autoresearchclaw.md)
- [`open-coscientist`](open-coscientist.md)

## Papers describing this project

- **Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy** — Sun, Youran, Ren, Xingyu, Yi, Chugang, Guo, Jiaxuan, Zhang, Kejia, Du, Jianda, Yang, Haizhao (2026). *arXiv preprint*. [arXiv:2606.24177](https://arxiv.org/abs/2606.24177)
