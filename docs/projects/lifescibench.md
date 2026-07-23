<!-- DO NOT EDIT — auto-generated from projects/landscape/lifescibench.yml by scripts/build_indexes.py -->

# LifeSciBench

`external` · status: `active` · focus: `end-to-end` · discipline: `biomedical` · started: 2026

**Project page:** <https://openai.com/index/introducing-life-sci-bench/>

**Source:** [`projects/landscape/lifescibench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/lifescibench.yml)

## Positioning

OpenAI's expert-authored benchmark (announced 2026-06-17) for measuring how well AI models support real-world life-science research. 750 free-response tasks span seven workflows — evidence handling, analysis, design/optimization, scientific reasoning, validation/operations, translation, and scientific communication — across seven biological domains, each pairing a scientific prompt, supporting artifacts, and an expert-written grading rubric. Sits in the RISE evaluation-infrastructure layer alongside AstaBench and EconCS Bench, but targets biomedical research capability.

## Distinctive contribution

Grades models against ~19,020 rubric criteria (~25 per task) decomposing each expected answer into individual claims, calculations, decisions, justifications, and caveats — authored by 173 PhD-level biotech/pharma scientists and validated by 453 independent expert reviewers (97% doctorate-holding, >96% agreement). Roughly 53% of tasks attach real scientific artifacts (genomic sequences, chemical structures, figures, tables, PDFs), and the best model (GPT-Rosalind) clears only 36.1% of tasks — with a sharp drop from text-only to artifact-bearing tasks.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Benchmark spans evidence handling through communication, but is an evaluation target — it does not itself produce scholarship. |
| Autonomy level | 0 | Static, human-authored task/rubric set; any agency lives in the models being scored. |
| Architectural transparency | 1 | Preprint and blog document task authoring, rubric construction, and validation methodology, but no tasks, rubrics, prompts, or grading code are released. |
| Inputs supported | 2 | Multiple input forms — text prompts plus 1,062 multimodal artifacts (genomic sequences, chemical structures, figures, tables, PDFs). |
| Outputs / reproducibility | 0 | No public artifact; reported scores cannot be reproduced without the withheld tasks, rubrics, and grader. |
| Internal evaluation | 2 | Systematic evaluation of five models across families with rubric-based scoring and 453 independent validators, but OpenAI selected tasks and ran the scoring — no third-party replication. |
| Openness | 0 | Benchmark not publicly downloadable at scoring date — no verifiable Hugging Face or GitHub release of tasks, rubrics, or harness; only a preprint describing it. |
| Maturity / traction | 1 | New (June 2026), professionally constructed and widely covered, but a one-off OpenAI release with no public leaderboard or external adoption yet. |
| Cross-family policy | 0 | Not applicable — model-agnostic benchmark with no runtime or reviewer role. |
| Runtime assurance | 0 | No runtime; task set and rubrics only. |
| Cross-platform portability | 1 | Internally model-agnostic (evaluated GPT, Gemini, and Grok families), but the harness is not distributed, so it cannot be deployed externally. |

*Scored on 2026-07-23. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `literature-synthesis` `research-design` `data-analysis` `paper-drafting`



**Inputs:** `task-prompts` `scientific-artifacts`


**Outputs:** `rubric-scores` `model-pass-rates`


**Knowledge sources:** `expert-authored-rubrics`


## Limitations

- Neither the dataset nor the grading harness is publicly released, so scores cannot be independently reproduced or audited.
- Single-turn evaluation only; real research is iterative and multi-turn.
- OpenAI authored the tasks, ran the scoring, and chose the comparison set (which omits Claude), inviting self-evaluation bias.

## Related projects in this catalog

- [`econcs-bench`](econcs-bench.md)
- [`asta-bench`](asta-bench.md)
- [`naturebench`](naturebench.md)
- [`robin`](robin.md)
