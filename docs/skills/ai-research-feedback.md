<!-- DO NOT EDIT — auto-generated from skills/ai-research-feedback.yml by scripts/build_skills_index.py -->

# AI Research Feedback (Claes Bäckman)

license: `MIT` · 10 skills · last update: 2026-08-27

**Source:** <https://github.com/claesbackman/AI-research-feedback>

**Maintainers:** Claes Bäckman (claesbackman.com)

**Related project entry:** [`ai-research-feedback`](../projects/ai-research-feedback.md)

**Compatibility:** `claude-code`

> Ten Claude Code skills for getting critical feedback on economics and finance research — the most-starred single-author econ skill pack in this catalog (~477 stars at curation). The review tier is deliberately graduated by cost, so a draft can be iterated cheaply and audited expensively: `review-paper` runs eight parallel referee agents against a named journal persona (top-5 economics, finance, macro), `review-paper-light` runs two for contribution and overclaiming, and `review-paper-checks` runs three that hunt only mechanical errors and issue no editorial judgment at all. Two skills are not reviews: `explain-diff` builds an offline HTML explainer with a five-question quiz (the idea taken from Geoffrey Litt's "Understanding is the new bottleneck"), and `audit-analysis` hands changed analysis code to an isolated subagent — the clean context is the point, so that whoever wrote the code, including the Claude session that helped, cannot steer the findings. Every review skill sets `disable-model-invocation: true`, so Claude never launches a multi-agent review on its own; `pdf-to-markdown` is the deliberate exception and may be auto-invoked when reading a PDF. A notable design detail: the review skills pass agents exactly the main .tex file plus its include-graph and explicitly exclude prior review reports, response letters, and old drafts — the fix for review-on-review contamination, which is the standard failure mode of running these tools repeatedly in one folder. All skills except `explain-diff` and `pdf-to-markdown` require access to the `general-purpose` subagent. Reports are written into a `reviews/` subfolder with date-versioned filenames.


**Source YAML:** [`skills/ai-research-feedback.yml`](https://github.com/bhanneke/RISE/blob/main/skills/ai-research-feedback.yml)

## Skills

### `audit` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/audit-analysis`](ai-research-feedback/audit-analysis.md) | economics | `code-generation` `data-analysis` | Hands a diff of changed empirical code to an isolated subagent instructed to break it: N before and after every filter, merge, and collapse taken from logs; merge keys, uniqueness, and the fate of unmatched observations; variable units, logs versus levels, deflation, lag alignment; silent failures such as missings coerced to zero, `destring ... force`, and `fillna(0)`; and the clustering level and what the fixed effects absorb. Every finding must quote a file and line and is tagged CONFIRMED or SUSPECTED; nothing is written to the repository. | [view](ai-research-feedback/audit-analysis.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/audit-analysis/SKILL.md) | 2026-08-26 |
| [`/review-paper-checks`](ai-research-feedback/review-paper-checks.md) | economics | `revision-editing` | Three-agent check for what is wrong rather than what is debatable: misspellings and grammar, numbers in the text that disagree with the tables, terminology and sample drift, cross-references and citations that point to nothing, and claims the design does not license. Issues no contribution or publication judgment, and afterwards offers to apply only the unambiguous fixes to the .tex files. | [view](ai-research-feedback/review-paper-checks.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper-checks/SKILL.md) | 2026-08-27 |

### `drafting` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/paper-version`](ai-research-feedback/paper-version.md) | economics | `dissemination` | Turns a LaTeX paper into a policy brief, one-page, or five-page lay summary through four sequential agents — a reader that extracts claims and numbers verbatim, a writer, a reviewer that checks every number and causal claim in the draft against the extraction, and a page builder — then emits a standalone HTML page ready for GitHub Pages. Pauses after the review so the author can edit before the page is built. | [view](ai-research-feedback/paper-version.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/paper-version/SKILL.md) | 2026-08-26 |

### `infra` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/explain-diff`](ai-research-feedback/explain-diff.md) | economics | `code-generation` | Writes one self-contained offline HTML page explaining a code change well enough that someone who did not write it could defend it: what the code did before, what changed in prose with no code, the verified consequences for sample and coefficients, a walkthrough grouped by purpose, and a five-question quiz of which at least two must test empirical consequences. Re-reads the diff and surrounding code from scratch — ignoring any account already in the conversation — and saves the page outside the repository under a dated, ref-tagged filename. | [view](ai-research-feedback/explain-diff.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/explain-diff/SKILL.md) | 2026-08-02 |
| [`/pdf-to-markdown`](ai-research-feedback/pdf-to-markdown.md) | general | `literature-discovery` | Converts a PDF to markdown beside the original with page markers every twenty pages and the text trimmed at the references or appendix, so only the main text enters the context window. Uses `pdftotext` when poppler is installed — orders of magnitude faster and free of model context cost — and falls back to chunked reading otherwise. | [view](ai-research-feedback/pdf-to-markdown.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/pdf-to-markdown/SKILL.md) | 2026-08-26 |

### `replication` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/review-paper-code`](ai-research-feedback/review-paper-code.md) | economics | `replication` | Reviews an empirical project's LaTeX paper against its Stata, R, or Python code on three fronts: reproducibility (paths, seeds, outputs, dependencies, run order, documentation), code quality, and paper-to-code alignment of tables, variables, sample restrictions, methods, clustering, and fixed effects. Calibrated to treat gaps as items to verify rather than accusations. | [view](ai-research-feedback/review-paper-code.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper-code/SKILL.md) | 2026-07-05 |

### `review` (4)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/review-grant`](ai-research-feedback/review-grant.md) | general | `research-design` | Six-agent panel review of a grant proposal against a target funder (NSF, NIH, ERC, Horizon Europe) or general standards, judging clarity and compliance signals, internal consistency and deliverables, significance and innovation, research design and feasibility, and the budget, timeline, team, and management plan. Inspects budgets, biosketches, data-management plans, and letters of support alongside the narrative. | [view](ai-research-feedback/review-grant.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-grant/SKILL.md) | 2026-07-05 |
| [`/review-pap`](ai-research-feedback/review-pap.md) | economics | `research-design` | Six-agent review of a pre-analysis plan against a chosen trial registry (AEA, EGAP, OSF, ClinicalTrials, ISRCTN) or journal standard, covering pre-specification completeness, hypothesis and outcome coverage, identification and causal claims, the statistical analysis plan including power and multiple testing, data and implementation feasibility, and registry fit. Pulls in power calculations, survey instruments, randomization protocols, and mock tables when it finds them. | [view](ai-research-feedback/review-pap.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-pap/SKILL.md) | 2026-07-05 |
| [`/review-paper`](ai-research-feedback/review-paper.md) | economics | `referee-simulation` | Eight parallel referee agents produce a pre-submission report against a named journal persona: spelling and style, internal consistency and cross-references, unsupported claims and identification integrity, mathematics and notation, tables and figures, referee assessment, plus a contribution advocate and a contribution skeptic whose opposing ratings are reconciled in a synthesis section. Novelty claims that cannot be verified from the paper's own bibliography are flagged rather than asserted. | [view](ai-research-feedback/review-paper.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper/SKILL.md) | 2026-07-05 |
| [`/review-paper-light`](ai-research-feedback/review-paper-light.md) | economics | `referee-simulation` | Fast two-agent pre-submission check on contribution, identification, and causal overclaiming — one agent plays a demanding associate editor who rates the contribution and names identification threats, the other hunts causal overclaiming, mechanisms asserted as facts, and missing caveats. Runs in about a minute, for iteration between full reviews. | [view](ai-research-feedback/review-paper-light.md) | [origin](https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper-light/SKILL.md) | 2026-07-05 |
