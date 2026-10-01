<!-- DO NOT EDIT — auto-generated from projects/landscape/paper-workflow.yml by scripts/build_indexes.py -->

# Paper-WorkFlow

`external` · status: `active` · focus: `end-to-end` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/brycewang-stanford/Paper-WorkFlow>

**Licence:** `MIT`

**Source:** [`projects/landscape/paper-workflow.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/paper-workflow.yml)

## Positioning

A meta-orchestrator for the empirical-economics paper pipeline: Stage 0-9 take a project from topic selection through literature grounding, data, identification/estimation, exhibits, drafting, structural and sentence-level polish, simulated referee review, and journal shortlisting/submission packaging. Entry is flexible — a user can join with a bare idea, existing clean data, existing results, or an existing draft/referee report, and the orchestrator routes to the matching stage rather than restarting the pipeline. It does not reimplement research skills itself; it routes to 47 skills in a companion "mother" repository (Auto-Empirical-Research-Skills, already catalogued) plus optional per-journal skills from Awesome Journal Skills at the submission stage.

## Distinctive contribution

Two hard quality gates — a method gate after Stage 3 (design register + evidence bundle, blocking identification flaws) and a 7-dimension quality-scorecard gate after Stage 7 (blocking manuscript defects, with automatic rollback to the weakest prior stage on failure) — plus a maintainer-facing acceptance-test harness (`evals/run_acceptance.py`) that runs the whole pipeline on synthetic raw data and checks for stale files, broken citations, and improper retrospective-disclosure/placeholder behavior. The README is explicit that this validates software plumbing, not paper quality or acceptance odds.

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 3 | 10-stage (0-9) protocol spans topic selection through submission, including paper-drafting and a two-gate validation stage. |
| Autonomy level | 2 | Recommended mode is stage-gated: title, journal choice, identification strategy and final submission require explicit human authorization; a fully-autonomous mode exists but is not the default. |
| Architectural transparency | 2 | Stage/gate logic, state schema (workflow_state.json v14) and rollback rules are public, but the 47 routed skills live in a separate companion repo, not bundled here. |
| Inputs supported | 2 | Multiple entry forms (idea, raw data, results, draft, referee comments) plus literature access via a routed web-research/arxiv skill; no dedicated proprietary-data connector of its own. |
| Outputs / reproducibility | 3 | Resumable, versioned workspace (workflow_state.json) producing a full replication package; an acceptance-test suite runs the pipeline end-to-end from synthetic raw data to a checked DOCX/main.tex. |
| Internal evaluation | 1 | 42/42 executable-gate CI badge and acceptance tests validate the software pipeline only; the README explicitly disclaims this as evidence of paper quality or acceptance rate. |
| Openness | 2 | MIT license with passing CI, but full operation needs the separate 47-skill mother repo plus licensed analysis backends (Stata/R); not self-contained end-to-end. |
| Maturity / traction | 1 | 39 stars, 186 commits, active CI; single-team (Stanford REAP x CoPaper.AI), first public in 2026. |
| Cross-family policy | 0 | No cross-model-family review requirement; runs on whichever single agent backend the user has (Claude, Codex, Cursor or Gemini). |
| Runtime assurance | 2 | Method gate (identification) and 7-dimension quality-scorecard gate with automatic rollback, plus a reference-verification and zero-numeric-drift check during the polish stage. |
| Cross-platform portability | 2 | Documented to run on 4 agent backends (Claude, Codex, Cursor, Gemini), each via its own skill/command mechanism. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `literature-discovery` `literature-synthesis` `research-design` `data-acquisition` `data-analysis` `code-generation` `paper-drafting` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `multi-agent` `dag-orchestration` `human-in-loop` `tool-use` `iterative-loop`


**Inputs:** `idea` `raw-data` `existing-results` `draft-manuscript` `referee-comments`


**Outputs:** `proposal` `cleaned-data` `design-register` `analysis-code` `tables-figures` `main.tex` `response-letters` `journal-shortlist` `replication-package` `final-report`


**Knowledge sources:** `arxiv` `web-research`


## Limitations

- 'End-to-end' describes pipeline coverage, not a guarantee of data availability, significant results, or passing either gate; failures are recorded as audit artifacts rather than silently hidden, but they are still failures.
- Full capability depends on a separate companion repository (Auto-Empirical-Research-Skills, 47 skills) and on licensed analysis backends (Stata/R) that are not bundled.
- Acceptance testing covers software plumbing (stale files, broken citations, retrospective-disclosure handling); there is no independent evidence yet of output quality or journal-acceptance outcomes.

## Related projects in this catalog

- [`auto-empirical-research-skills`](auto-empirical-research-skills.md)
- [`clo-author`](clo-author.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`writing-driven-autoresearch`](writing-driven-autoresearch.md)
