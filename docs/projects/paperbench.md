<!-- DO NOT EDIT — auto-generated from projects/landscape/paperbench.yml by scripts/build_indexes.py -->

# PaperBench (OpenAI)

`external` · status: `dormant` · focus: `replication` · discipline: `computer-science` · started: 2025

**Project page:** <https://github.com/openai/frontier-evals/tree/main/project/paperbench>

**Source:** [`projects/landscape/paperbench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/paperbench.yml)

## Positioning

The reference replication benchmark for AI research: agents must reproduce 20 ICML 2024 Spotlight and Oral papers from scratch — understanding the contribution, writing the codebase, and executing the experiments — with no starter code. Each sample pairs the paper (PDF and Markdown) with a hierarchical rubric co-developed with that paper's own authors, decomposing replication into 8,316 individually gradable leaves across three requirement types (Code Development, Execution, Result Match). The harness runs three containers per attempt: agent rollout, then re-execution of the submitted codebase in a fresh GPU container, then LLM grading against the rubric. Sits at the replication block of the RISE pipeline as the target that `paper2code` and the replication agents are measured against, and as the AI-research counterpart to `mle-bench`'s Kaggle framing.

## Distinctive contribution

Author-co-developed hierarchical rubrics are the mechanism nothing else in the catalog has: replication stops being a binary pass and becomes 8,316 graded claims, which is what makes partial credit meaningful and lets Code-Dev (code only, no GPUs, ~85% cheaper grading) exist as a lighter variant of the same target. It also benchmarks its own grader — JudgeEval is a separate evaluation of judge accuracy — and anchors agents against recruited top ML PhDs, reporting that the best agent (Claude 3.5 Sonnet with open-source scaffolding, 21.0%) still did not beat the human baseline.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Evaluation infrastructure: the declared stages are what it grades in other systems; PaperBench itself produces scores, not scholarship. |
| Autonomy level | 0 | Fixed papers, rubrics and a three-stage grading harness; all agency belongs to the evaluated agents, which the baselines ran unattended for 12–36 hours. |
| Architectural transparency | 3 | The monorepo publishes the 20 papers with their `rubric.json` trees and judge addenda, the DummySolver and BasicAgent/IterativeAgent scaffolds, the SimpleJudge implementation, the Dockerfiles, a rubric-viewing GUI, and JudgeEval. |
| Inputs supported | 2 | Each sample carries multiple input forms (paper PDF, Markdown, rubric, optional judge addendum) over three splits (debug/dev/all), with a documented interface for plugging in any agent — plus the papers themselves as literature. |
| Outputs / reproducibility | 2 | Papers and rubrics are pinned in Git-LFS and the reproduction container re-executes submissions deterministically, but final scores come from an LLM judge and expensive stochastic agent rollouts, so exact reruns are not guaranteed. |
| Internal evaluation | 2 | Systematic multi-model evaluation with 3 runs per configuration, a human baseline of recruited ML PhDs, and JudgeEval validating the grader — but the arXiv page carries no venue in its comments field, and no peer-reviewed publication or third-party replication could be verified on 2026-09-08. |
| Openness | 2 | MIT licence at the root of openai/frontier-evals with the full harness public, but running it needs Docker with NVIDIA GPU containers and an OpenAI-keyed judge (`GRADER_OPENAI_API_KEY`), and some JudgeEval tarballs cannot be redistributed — permissive, not commodity-reproducible. |
| Maturity / traction | 2 | Hosted in a 1,291-star / 176-fork OpenAI eval monorepo and widely used as a frontier replication eval, but the README leaderboard contains only the authors' own baselines dated 2025-04-02, there is no submission process, and no commit has touched project/paperbench since 2025-12-06. |
| Cross-family policy | 1 | The judge's completer is configurable and the reported runs graded Claude, DeepSeek and Gemini agents with an OpenAI judge, but nothing requires or defaults to cross-family pairing — grading an OpenAI agent uses a same-family judge. |
| Runtime assurance | 1 | The harness re-executes each submission in a clean GPU container before grading and JudgeEval bounds the grader's accuracy, but these are grading-time checks on a finished submission rather than in-flight gates during the agent's run. |
| Cross-platform portability | 1 | Depends on OpenAI's own nanoeval + alcatraz runtime (a custom `ComputerRuntime` is a documented extension point) and on an OpenAI-compatible completer for the judge; agents themselves can come from any provider. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `code-generation` `data-analysis` `replication`


**Architectural features:** `tool-use`


**Inputs:** `paper-pdf-and-markdown` `replication-rubric` `agent-implementation`


**Outputs:** `replication-scores` `graded-rubric-trees` `executed-submissions`


**Data sources:** `git-lfs-paper-dataset`


**Knowledge sources:** `icml-2024-papers` `author-co-developed-rubrics`


## Limitations

- The code URL printed in the paper (github.com/openai/preparedness) now redirects: PaperBench lives at project/paperbench inside openai/frontier-evals, and that subtree has had no commit since 2025-12-06.
- The leaderboard is a static README table of the authors' own April 2025 baseline runs — no external submission process, so no independent scores exist to compare against.
- Grading is LLM-based and costly: the Code-Dev variant exists chiefly because it cuts roughly 85% of judge spend, and every score inherits the judge's error rate as measured by JudgeEval.
- Twenty ICML 2024 papers is a frozen and narrowing target — those papers' own code and derivative discussion are now in model training data, so scores drift upward for reasons unrelated to replication ability.
- The papers dataset is Git-LFS-gated and some JudgeEval tarballs must be regenerated locally rather than downloaded.
- Requires Docker plus NVIDIA GPU containers for the reproduction stage; the full split is out of reach on commodity hardware.
- Scope is machine-learning papers only: nothing about identification, data acquisition from the field, or empirical social-science replication.

## Related projects in this catalog

- [`mle-bench`](mle-bench.md)
- [`core-bench`](core-bench.md)
- [`repro-bench`](repro-bench.md)
- [`paper2code`](paper2code.md)
- [`social-science-replicability`](social-science-replicability.md)

## Papers describing this project

- **PaperBench: Evaluating AI's Ability to Replicate AI Research** — Starace, G., Jaffe, O., Sherburn, D., Aung, J., Chan, J. S., Maksin, L., Dias, R., Mays, E., Kinsella, B., Thompson, W., Heidecke, J., Glaese, A., Patwardhan, T. (2025). *arXiv*. [arXiv:2504.01848](https://arxiv.org/abs/2504.01848)

## Related references (literature catalog)

- Starace, G. et al. (2025). [*PaperBench: Evaluating AI's Ability to Replicate AI Research*](../papers/notes/starace2025paperbench.md) `starace2025paperbench`
