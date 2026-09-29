<!-- DO NOT EDIT — auto-generated from skills/idea-evaluation-pipeline.yml by scripts/build_skills_index.py -->

# Research Idea Evaluation Pipeline (Alejandro Lopez-Lira)

license: `none` · 8 skills · last update: 2026-03-12

**Source:** <https://github.com/alejandroll10/idea-evaluation-pipeline>

**Maintainers:** Alejandro Lopez-Lira (alejandroll10 on GitHub)

**Compatibility:** `agnostic` `claude-code` `cursor` `codex` `windsurf`

!!! warning "No licence declared"
    The source repository declares no licence, so its skill texts are not
    reproduced here. The skills are listed by name with RISE's own short
    descriptions, and each links to its file in the source repository.
    Ask the maintainer before reusing or adapting the material.

> A prompt-based loop for stress-testing a finance or economics research idea against the bar of the top finance and economics journals: evaluate, have the evaluation reviewed for fairness, pivot and re-evaluate until the score clears a threshold, then run a threat-focused literature search, verify every citation, and issue and review a final verdict. The prompts are plain text files driven by an AGENTS.md runner, so any coding agent or a manual copy-paste workflow can use them; the explicit citation-verification step against hallucinated references is what stands out. No licence declared: skill texts are not reproduced here; each skill links to its source.


**Source YAML:** [`skills/idea-evaluation-pipeline.yml`](https://github.com/bhanneke/RISE/blob/main/skills/idea-evaluation-pipeline.yml)

## Skills

### `audit` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`verify_lit_review_prompt.txt`](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/verify_lit_review_prompt.txt){ target=_blank rel=noopener } | finance | `literature-discovery` | Checks each citation in the generated literature review against the web, correcting wrong bibliographic details and removing papers that cannot be found. | — | [origin](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/verify_lit_review_prompt.txt) | 2026-03-12 |

### `ideation` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`prompt_ideas.txt`](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/prompt_ideas.txt){ target=_blank rel=noopener } | finance | `hypothesis-generation` | Scores a research idea against its three closest papers on marginal contribution, method, impact, feasibility and related criteria; used both for the first evaluation and for each pivot. | — | [origin](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/prompt_ideas.txt) | 2026-03-12 |
| [`pivot_prompt.txt`](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/pivot_prompt.txt){ target=_blank rel=noopener } | finance | `rq-formulation` `hypothesis-generation` | Reshapes an idea that scored below the threshold, using the full evaluation history to fix its weak points while staying on the same topic. | — | [origin](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/pivot_prompt.txt) | 2026-03-12 |

### `infra` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`AGENTS.md`](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/AGENTS.md){ target=_blank rel=noopener } | finance | `hypothesis-generation` `literature-discovery` | Agent-facing instructions that run the eight evaluation steps in order, name the input and output files for each step, and control the loop back to pivoting whenever a score falls short. | — | [origin](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/AGENTS.md) | 2026-03-12 |

### `literature` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`lit_review_prompt.txt`](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/lit_review_prompt.txt){ target=_blank rel=noopener } | finance | `literature-discovery` | Web-search step that looks for papers the author did not cite which undermine the novelty claim, requiring a link for every paper it names. | — | [origin](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/lit_review_prompt.txt) | 2026-03-12 |

### `review` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`final_verdict_prompt.txt`](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/final_verdict_prompt.txt){ target=_blank rel=noopener } | finance | `hypothesis-generation` | Synthesises the whole evaluation history into a final score with justification and a recommendation on whether the idea is ready to pursue. | — | [origin](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/final_verdict_prompt.txt) | 2026-03-12 |
| [`review_eval_prompt.txt`](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/review_eval_prompt.txt){ target=_blank rel=noopener } | finance | `hypothesis-generation` | Second-opinion check on an idea evaluation, judging whether the critique and its score are fair and well reasoned before the pipeline acts on them. | — | [origin](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/review_eval_prompt.txt) | 2026-03-12 |
| [`review_final_verdict_prompt.txt`](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/review_final_verdict_prompt.txt){ target=_blank rel=noopener } | finance | `hypothesis-generation` | Audits the final verdict for consistency with the evidence gathered earlier in the pipeline and decides whether the idea passes or goes back for another pivot. | — | [origin](https://github.com/alejandroll10/idea-evaluation-pipeline/blob/main/review_final_verdict_prompt.txt) | 2026-03-12 |
