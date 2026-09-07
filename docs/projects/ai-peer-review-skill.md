<!-- DO NOT EDIT — auto-generated from projects/landscape/ai-peer-review-skill.yml by scripts/build_indexes.py -->

# ai-peer-review-skill

`external` · status: `dormant` · focus: `review` · discipline: `general` · started: 2026

**Project page:** <https://github.com/AlexWortega/ai-peer-review-skill>

**Source:** [`projects/landscape/ai-peer-review-skill.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/ai-peer-review-skill.yml)

## Positioning

A single-purpose Claude Code skill sitting squarely in the referee-simulation stage: hand it a manuscript (PDF, DOCX, TXT or MD) and it extracts the text, spawns N parallel Claude subagents (default 5, named with NATO codenames alfa through echo) that each return an independent structured review — summary, major concerns, minor concerns, verdict — with one slot optionally given to an AI-Alignment-Forum-style critic red-teaming narrative, novelty, baselines, ablations and reproducibility, then synthesises a meta-review separating shared from unique concerns and issuing a final verdict. It is an explicit adaptation of Russ Poldrack's poldrack/ai-peer-review (MIT, 154 stars, still maintained), whose six proprietary LLMs it replaces with parallel Claude subagents and whose hardcoded neuroscience domain it turns into a parameter — trading cross-model diversity for needing no API keys beyond Claude Code.

## Distinctive contribution

The output shape rather than the review itself. Alongside the per-reviewer markdown and meta_review.md it writes concerns_table.csv — a boolean concerns × reviewers matrix — plus results.json, and it ranks the reviewers by usefulness, so a simulated referee panel becomes something an author can sort and triage instead of read end to end. Among the catalog's review tools it is the cheapest thing that produces a machine-readable disagreement map across reviewers.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 0 | Single stage: referee simulation on a finished manuscript. |
| Autonomy level | 2 | One invocation yields the whole bundle — the human supplies the paper and optional parameters (num_reviewers 3-8, domain, output_dir) and reads the meta-review, with no intermediate approval. |
| Architectural transparency | 3 | MIT, and the system is essentially prompts plus glue: the reviewer templates and the meta-review prompt ship as files under prompts/, with scripts/ and a SKILL.md documenting the workflow and a comparison table against upstream. Nothing is hidden — there is simply no evaluation harness to publish. |
| Inputs supported | 0 | Four file formats but one input form (a manuscript) plus a domain string, with no literature corpus or data access — a stricter reading of the rubric than the earlier `reviewer` entry, which scored 1 for the same paper-only input. |
| Outputs / reproducibility | 2 | Four durable artifacts per paper under papers/<paper-stem>/ including a machine-readable concerns matrix and a JSON bundle; no seeding or model pinning, so two runs on the same PDF give different panels. |
| Internal evaluation | 0 | None reported: no agreement statistics against human referee reports, no comparison against the upstream six-model panel it replaces, and no worked example in the repository. |
| Openness | 2 | MIT (for the skill adaptation) and installation is a clone plus a symlink into ~/.claude/skills, but every run needs a paid Claude Code subscription and review quality tracks whichever frontier model is behind it — not free-tier reproducible. |
| Maturity / traction | 1 | 61 stars and 5 forks on 11 commits, every one pushed on 2026-05-08 with nothing since and no releases; upstream poldrack/ai-peer-review is larger (154 stars, 24 forks) and still being pushed as of 2026-07-05. |
| Cross-family policy | 0 | This is the port's defining trade-off: upstream ran six different proprietary LLMs to buy reviewer diversity, whereas this runs N instances of one Claude model, so disagreement between reviewers reflects sampling and prompt variation within a single family. |
| Runtime assurance | 1 | Single-pass structured review plus a meta-review synthesis; nothing checks a reviewer's assertion back against the manuscript or the literature, and no gate blocks a confabulated concern from reaching the CSV. |
| Cross-platform portability | 0 | Claude Code only — installed by symlink into ~/.claude/skills, and the parallel-reviewer mechanism is Claude Code's own subagent spawning; no other runtime or provider is supported. |

*Scored on 2026-09-08. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `referee-simulation`


**Architectural features:** `multi-agent` `tool-use`


**Inputs:** `manuscript-pdf` `manuscript-docx` `manuscript-text` `domain-parameter`


**Outputs:** `reviewer-reports` `meta-review` `concerns-matrix-csv` `results-json`


## Limitations

- Reviewer diversity is simulated inside one model family. The upstream tool used six different proprietary LLMs on purpose; N Claude subagents share priors and blind spots, so a concern all five miss is a concern the panel structurally cannot surface — and the usefulness ranking is produced by the same family it is ranking.
- No evaluation. Nothing compares its reviews to real referee reports or to the upstream panel, so there is no evidence the concerns matrix is calibrated rather than merely tidy.
- No literature access: reviewers cannot check a novelty or prior-work claim against anything, so novelty verdicts rest on model memory — the failure mode most likely to mislead an author.
- Frozen: 11 commits, all on 2026-05-08. The upstream poldrack/ai-peer-review is still maintained and is the better target for anyone who wants the multi-model panel.
- Claude Code and a paid subscription are hard requirements, and cost scales with num_reviewers (3-8) times paper length; domain adaptation is a prompt parameter, so field-specific standards (identification, institutional detail) are only as good as the model's priors.

## Related projects in this catalog

- [`reviewer`](reviewer.md)
- [`marg`](marg.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`ai-research-feedback`](ai-research-feedback.md)
