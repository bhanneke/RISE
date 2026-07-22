<!-- DO NOT EDIT — auto-generated from projects/landscape/econcs-bench.yml by scripts/build_indexes.py -->

# EconCS Bench

`external` · status: `active` · focus: `end-to-end` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/aieconcs/econcs-bench>

**Source:** [`projects/landscape/econcs-bench.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/econcs-bench.yml)

## Positioning

A benchmark suite of open research challenges in Economics and Computation (EconCS), associated with the AI-Driven Research in EconCS workshop at EC 2026. 24 open problems — mechanism design, fair division (EFX, MMS, PMMS), prophet inequalities, information design, complexity of equilibria — each a markdown PROBLEM.md with YAML metadata, contributor attribution, known results, and an optional difficulty rating (Approachable / Challenging / Hard). Sits in the RISE evaluation-infrastructure layer alongside AstaBench, Aviary, and MLGym, but targets formal *theory* research rather than empirical, coding, or literature tasks.

## Distinctive contribution

The first community-curated open-problem benchmark aimed at AI-driven theory research: problems are contributed via pull requests by many of the field's leading researchers (Nisan, Papadimitriou, Procaccia, Conitzer, Feldman, Mirrokni, Weinberg, Dobzinski, Chen, Babaioff, Rubinstein, Duetting, Lucier, Branzei, Paes Leme), making it both a live registry of what experts consider genuinely open and a difficulty-graded target set for proof-capable research agents. Success has no harness: a solved benchmark problem is a publishable research result.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Problem catalog / evaluation target; does not produce scholarship itself. |
| Autonomy level | 0 | Static problem statements curated by humans via PR review; any agency lives in the systems attempting the problems. |
| Architectural transparency | 3 | Fully public markdown problem statements with YAML metadata, contributor attribution, and a documented difficulty rubric; contribution process is PR-based and transparent. |
| Inputs supported | 1 | Single input form (PROBLEM.md with name/contributor/rating metadata); no execution harness or standardized agent interface. |
| Outputs / reproducibility | 0 | No system outputs; solutions arrive as ordinary research papers outside the repo. |
| Internal evaluation | 1 | Expert curation and optional contributor-assigned difficulty ratings; no scoring harness, baselines, or leaderboard yet. |
| Openness | 1 | Public repo with open PR-based contribution, but no license file at scoring date. |
| Maturity / traction | 1 | Young (June 2026) and small (9 stars), but anchored to the EC 2026 workshop with problems from many of the field's most prominent researchers. |
| Cross-family policy | 0 | Not applicable — model-agnostic problem statements with no runtime; no policy on solving systems. |
| Runtime assurance | 0 | No runtime; problem statements only. |
| Cross-platform portability | 3 | Plain markdown + YAML, consumable by any agent framework or by humans; deliberately format-minimal. |

*Scored on 2026-07-22. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `formal-modeling`



**Inputs:** `open-problem-submissions`


**Outputs:** `problem-statements` `difficulty-ratings`


**Knowledge sources:** `contributor-expertise`


## Limitations

- No license file at scoring date — reuse terms are unclear.
- Problem statements only: no execution harness, automated scoring, or leaderboard; verifying a claimed solution requires expert peer review.
- Coverage reflects contributor interests — heavily weighted toward mechanism design and fair division.

## Related projects in this catalog

- [`asta-bench`](asta-bench.md)
- [`aviary`](aviary.md)
- [`mlgym`](mlgym.md)
