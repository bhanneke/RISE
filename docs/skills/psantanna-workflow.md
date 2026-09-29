<!-- DO NOT EDIT — auto-generated from skills/psantanna-workflow.yml by scripts/build_skills_index.py -->

# Pedro Sant'Anna's Claude Code Workflow

license: `MIT` · 79 skills · last update: 2026-09-27

**Source:** <https://github.com/pedrohcgs/claude-code-my-workflow>

**Maintainers:** Pedro H. C. Sant'Anna (Emory University, Economics)

**Compatibility:** `claude-code`

> A ready-to-fork Claude Code template for academics using LaTeX/Beamer + R. 61 skills + 18 agents. Calibrated peer-review pipeline against AER, QJE, JPE, Econometrica, ReStud. Adopted by 15+ research groups. Refresh 2026-09-29 (upstream at 2026-09-27, previously catalogued at 2026-04-27 with 30 skills + 14 agents): added 31 skills (replication packaging, environment capture, disclosure and submission checks, grant/DMP/power-analysis design aids, teaching tools, audit and verification primitives such as vaccinate, differential-audit, verify-artifact, oracle-review) and 4 agents (humanize-auditor, promote-memory-council, r-package-reviewer, sim-reviewer); 43 existing skill texts changed upstream and were re-copied (notably /commit no longer merges, /deep-audit became a general adversarial audit); nothing was removed.

**Source YAML:** [`skills/psantanna-workflow.yml`](https://github.com/bhanneke/RISE/blob/main/skills/psantanna-workflow.yml)

## Skills

### `analysis` (4)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/challenge`](psantanna-workflow/challenge.md) | economics | `data-analysis` | Stress-tests a finding against the analysis forks not taken (measures, sample filters, controls, clustering, weighting, functional form) by running and reporting the specification grid. | [view](psantanna-workflow/challenge.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/challenge/SKILL.md) | 2026-08-23 |
| [`/data-analysis`](psantanna-workflow/data-analysis.md) | economics | `data-analysis` | — | [view](psantanna-workflow/data-analysis.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/data-analysis/SKILL.md) | 2026-09-26 |
| [`/diagnose`](psantanna-workflow/diagnose.md) | economics | `data-analysis` `code-generation` | Root-causes a failing or wrong empirical result with a reproduce, minimise, hypothesise, instrument, fix loop tuned for R, Stata and Python research code. | [view](psantanna-workflow/diagnose.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/diagnose/SKILL.md) | 2026-09-26 |
| [`/simulation-study`](psantanna-workflow/simulation-study.md) | economics | `formal-modeling` `code-generation` | Scaffolds and runs a reproducible Monte Carlo simulation study in R (DGP, estimator grid, seeded replications), reporting bias, RMSE, coverage and size/power with Monte Carlo standard errors. | [view](psantanna-workflow/simulation-study.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/simulation-study/SKILL.md) | 2026-09-26 |

### `audit` (14)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/blast-radius`](psantanna-workflow/blast-radius.md) | economics | `code-generation` | Before and after changing anything shared (a function, signature, schema, config default or constant), finds every consumer and runs it to catch silent downstream breakage. | [view](psantanna-workflow/blast-radius.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/blast-radius/SKILL.md) | 2026-08-23 |
| [`agent:claim-verifier`](psantanna-workflow/claim-verifier.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/claim-verifier.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/claim-verifier.md) | 2026-09-26 |
| [`/credible-claims`](psantanna-workflow/credible-claims.md) | economics | `research-design` | Research-brief and claim-record discipline for AI-assisted research: write the brief before a long run, and back every reported result with a claim record. | [view](psantanna-workflow/credible-claims.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/credible-claims/SKILL.md) | 2026-08-21 |
| [`/deep-audit`](psantanna-workflow/deep-audit.md) | economics | `referee-simulation` | Adversarial audit of a theory, proof, paper, codebase or set of claims: independent skeptics must return concrete defects, a separate judge adjudicates each, confirmed defects are fixed and re-verified. | [view](psantanna-workflow/deep-audit.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/deep-audit/SKILL.md) | 2026-09-27 |
| [`/differential-audit`](psantanna-workflow/differential-audit.md) | economics | `replication` | Compares two implementations of the same thing (a port, reimplementation, replication package or refactor) with frozen inputs and a full output inventory so agreement is meaningful. | [view](psantanna-workflow/differential-audit.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/differential-audit/SKILL.md) | 2026-08-21 |
| [`/disclosure-check`](psantanna-workflow/disclosure-check.md) | economics | `dissemination` | Pre-screens tables, figures and logs built on restricted data for statistical-disclosure problems (small cells, suppression gaps, dominance, re-identification risk) before release. | [view](psantanna-workflow/disclosure-check.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/disclosure-check/SKILL.md) | 2026-09-26 |
| [`/qa-quarto`](psantanna-workflow/qa-quarto.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/qa-quarto.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/qa-quarto/SKILL.md) | 2026-09-26 |
| [`agent:quarto-critic`](psantanna-workflow/quarto-critic.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/quarto-critic.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/quarto-critic.md) | 2026-09-26 |
| [`/r-package-check`](psantanna-workflow/r-package-check.md) | economics | `code-generation` | Runs the full R package release gate (docs, tests, R CMD check --as-cran) and triages every ERROR, WARNING and NOTE against CRAN policy. | [view](psantanna-workflow/r-package-check.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/r-package-check/SKILL.md) | 2026-09-26 |
| [`/vaccinate`](psantanna-workflow/vaccinate.md) | economics |  | Qualifies a checker before trusting it: seeds known defects into a copy of a real artifact plus a clean control and reports recall and false-positive rate. | [view](psantanna-workflow/vaccinate.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/vaccinate/SKILL.md) | 2026-09-26 |
| [`/validate-bib`](psantanna-workflow/validate-bib.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/validate-bib.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/validate-bib/SKILL.md) | 2026-06-09 |
| [`agent:verifier`](psantanna-workflow/verifier.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/verifier.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/verifier.md) | 2026-09-26 |
| [`/verify-artifact`](psantanna-workflow/verify-artifact.md) | economics | `dissemination` | Proves a file about to be sent or published is the intended one: rebuild from source, integrity check, diff against source, and recipient echo-back. | [view](psantanna-workflow/verify-artifact.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/verify-artifact/SKILL.md) | 2026-08-21 |
| [`/verify-claims`](psantanna-workflow/verify-claims.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/verify-claims.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/verify-claims/SKILL.md) | 2026-09-26 |

### `code-gen` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/stata-replication`](psantanna-workflow/stata-replication.md) | economics | `code-generation` `data-analysis` | End-to-end Stata pipeline: numbered .do files run through the stata-mcp server, logged outputs, and publication-ready esttab tables and exported figures. | [view](psantanna-workflow/stata-replication.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/stata-replication/SKILL.md) | 2026-09-26 |

### `design` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/data-management-plan`](psantanna-workflow/data-management-plan.md) | economics | `research-design` | Drafts a funder-compliant Data Management Plan (NSF, NIH, ERC, Horizon Europe) covering data description, storage, access, sharing and preservation. | [view](psantanna-workflow/data-management-plan.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/data-management-plan/SKILL.md) | 2026-09-26 |
| [`/power-analysis`](psantanna-workflow/power-analysis.md) | economics | `research-design` | Computes power, required sample size and minimum detectable effect for a study design (clustered RCTs, multiple arms, simulation-based) and writes a registry-ready power section. | [view](psantanna-workflow/power-analysis.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/power-analysis/SKILL.md) | 2026-09-26 |
| [`/preregister`](psantanna-workflow/preregister.md) | economics | `research-design` | — | [view](psantanna-workflow/preregister.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/preregister/SKILL.md) | 2026-09-26 |

### `drafting` (6)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`agent:beamer-translator`](psantanna-workflow/beamer-translator.md) | economics | `paper-drafting` | — | [view](psantanna-workflow/beamer-translator.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/beamer-translator.md) | 2026-09-26 |
| [`/compile-latex`](psantanna-workflow/compile-latex.md) | economics | `paper-drafting` | — | [view](psantanna-workflow/compile-latex.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/compile-latex/SKILL.md) | 2026-04 |
| [`/grant-proposal`](psantanna-workflow/grant-proposal.md) | economics | `research-design` | Scaffolds a research grant proposal (NSF, NIH, ERC or foundation) by composing the interview spec, data-management-plan and environment-capture skills. | [view](psantanna-workflow/grant-proposal.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/grant-proposal/SKILL.md) | 2026-09-27 |
| [`/scaffold-exercises`](psantanna-workflow/scaffold-exercises.md) | economics |  | Scaffolds a graded problem set with worked solutions and short why-this-matters explainers across analytical, empirical and coding problem types. | [view](psantanna-workflow/scaffold-exercises.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/scaffold-exercises/SKILL.md) | 2026-09-26 |
| [`/syllabus`](psantanna-workflow/syllabus.md) | economics |  | Builds or restructures a course syllabus: description and prerequisites, week-by-week schedule, measurable learning objectives, assessment scheme with rubric, and standard policies. | [view](psantanna-workflow/syllabus.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/syllabus/SKILL.md) | 2026-09-26 |
| [`/translate-to-quarto`](psantanna-workflow/translate-to-quarto.md) | economics | `paper-drafting` | — | [view](psantanna-workflow/translate-to-quarto.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/translate-to-quarto/SKILL.md) | 2026-09-26 |

### `editing` (8)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/humanize`](psantanna-workflow/humanize.md) | economics | `revision-editing` | Read-only audit of .tex, .qmd or .md prose for AI-voice tells: boilerplate transitions, cliche lexicon, em-dash overuse, symmetric paragraph shapes and hedging. | [view](psantanna-workflow/humanize.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/humanize/SKILL.md) | 2026-09-26 |
| [`agent:humanize-auditor`](psantanna-workflow/humanize-auditor.md) | economics | `revision-editing` | Read-only auditor for AI-voice tells in academic prose across the ten detection categories defined by /humanize. | [view](psantanna-workflow/humanize-auditor.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/humanize-auditor.md) | 2026-09-26 |
| [`/pedagogy-review`](psantanna-workflow/pedagogy-review.md) | economics | `revision-editing` | — | [view](psantanna-workflow/pedagogy-review.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/pedagogy-review/SKILL.md) | 2026-09-26 |
| [`agent:pedagogy-reviewer`](psantanna-workflow/pedagogy-reviewer.md) | economics | `revision-editing` | — | [view](psantanna-workflow/pedagogy-reviewer.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/pedagogy-reviewer.md) | 2026-09-26 |
| [`/proofread`](psantanna-workflow/proofread.md) | economics | `revision-editing` | — | [view](psantanna-workflow/proofread.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/proofread/SKILL.md) | 2026-09-26 |
| [`agent:proofreader`](psantanna-workflow/proofreader.md) | economics | `revision-editing` | — | [view](psantanna-workflow/proofreader.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/proofreader.md) | 2026-09-26 |
| [`agent:quarto-fixer`](psantanna-workflow/quarto-fixer.md) | economics | `revision-editing` | — | [view](psantanna-workflow/quarto-fixer.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/quarto-fixer.md) | 2026-06-09 |
| [`/voice-profile`](psantanna-workflow/voice-profile.md) | economics | `revision-editing` | Extracts a written voice profile from your own prior papers and uses it to keep new drafts sounding like you. | [view](psantanna-workflow/voice-profile.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/voice-profile/SKILL.md) | 2026-09-26 |

### `figures` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/extract-tikz`](psantanna-workflow/extract-tikz.md) | economics | `paper-drafting` | — | [view](psantanna-workflow/extract-tikz.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/extract-tikz/SKILL.md) | 2026-08-21 |
| [`/new-diagram`](psantanna-workflow/new-diagram.md) | economics | `paper-drafting` | — | [view](psantanna-workflow/new-diagram.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/new-diagram/SKILL.md) | 2026-09-26 |
| [`/visual-audit`](psantanna-workflow/visual-audit.md) | economics | `paper-drafting` | — | [view](psantanna-workflow/visual-audit.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/visual-audit/SKILL.md) | 2026-09-26 |

### `ideation` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/interview-me`](psantanna-workflow/interview-me.md) | economics | `rq-formulation` `hypothesis-generation` | — | [view](psantanna-workflow/interview-me.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/interview-me/SKILL.md) | 2026-09-26 |
| [`/research-ideation`](psantanna-workflow/research-ideation.md) | economics | `rq-formulation` `hypothesis-generation` | — | [view](psantanna-workflow/research-ideation.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/research-ideation/SKILL.md) | 2026-09-26 |

### `infra` (11)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/checkpoint`](psantanna-workflow/checkpoint.md) | economics |  | — | [view](psantanna-workflow/checkpoint.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/checkpoint/SKILL.md) | 2026-09-27 |
| [`/coauthor-brief`](psantanna-workflow/coauthor-brief.md) | economics |  | Generates a co-author handoff brief: git delta since the last brief, state of manuscript, analysis and slides, open questions, and how to reproduce locally. | [view](psantanna-workflow/coauthor-brief.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/coauthor-brief/SKILL.md) | 2026-09-26 |
| [`/commit`](psantanna-workflow/commit.md) | economics |  | Runs the quality and consistency gates, then commits with a subject that states what is now true; pushes and opens a PR only on request and never merges without an explicit instruction. | [view](psantanna-workflow/commit.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/commit/SKILL.md) | 2026-09-26 |
| [`/compress-session`](psantanna-workflow/compress-session.md) | economics |  | Distills the current conversation into a structured session note (decisions, open questions, file pointers, next actions) before auto-compression. | [view](psantanna-workflow/compress-session.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/compress-session/SKILL.md) | 2026-09-26 |
| [`/context-status`](psantanna-workflow/context-status.md) | economics |  | — | [view](psantanna-workflow/context-status.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/context-status/SKILL.md) | 2026-09-26 |
| [`/issues`](psantanna-workflow/issues.md) | economics |  | Keeps the project to-do list and memory in GitHub issues: files findings without duplicates, lists issues relevant to the current work, and closes them with a record of the fix. | [view](psantanna-workflow/issues.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/issues/SKILL.md) | 2026-09-26 |
| [`/learn`](psantanna-workflow/learn.md) | economics |  | — | [view](psantanna-workflow/learn.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/learn/SKILL.md) | 2026-09-26 |
| [`/permission-check`](psantanna-workflow/permission-check.md) | economics |  | — | [view](psantanna-workflow/permission-check.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/permission-check/SKILL.md) | 2026-09-26 |
| [`/promote-memory`](psantanna-workflow/promote-memory.md) | economics |  | Reviews candidate learnings in Claude Code auto memory through a five-critic council and promotes majority-approved entries to the committed MEMORY.md. | [view](psantanna-workflow/promote-memory.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/promote-memory/SKILL.md) | 2026-09-26 |
| [`agent:promote-memory-council`](psantanna-workflow/promote-memory-council.md) | economics |  | Five-critic council (generality, staleness, redundancy, evidence, format) that votes on promoting candidate learnings from local memory to the committed MEMORY.md; invoked by /promote-memory. | [view](psantanna-workflow/promote-memory-council.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/promote-memory-council.md) | 2026-09-26 |
| [`/triage-inbox`](psantanna-workflow/triage-inbox.md) | economics |  | Triages academic email and calendar into a prioritized digest plus a referee-obligations tracker (referee requests, R&R correspondence, co-author threads, invitations). | [view](psantanna-workflow/triage-inbox.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/triage-inbox/SKILL.md) | 2026-09-27 |

### `literature` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/lit-review`](psantanna-workflow/lit-review.md) | economics | `literature-discovery` `literature-synthesis` | — | [view](psantanna-workflow/lit-review.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/lit-review/SKILL.md) | 2026-09-27 |

### `meta` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/new-skill`](psantanna-workflow/new-skill.md) | economics |  | Scaffolds a new skill in the repo conventions: interviews for purpose, trigger phrases and tool needs, then writes a SKILL.md that passes the integrity gates. | [view](psantanna-workflow/new-skill.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/new-skill/SKILL.md) | 2026-09-27 |

### `replication` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/audit-reproducibility`](psantanna-workflow/audit-reproducibility.md) | economics | `replication` | — | [view](psantanna-workflow/audit-reproducibility.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/audit-reproducibility/SKILL.md) | 2026-09-26 |
| [`/capture-environment`](psantanna-workflow/capture-environment.md) | economics | `replication` | Snapshots the computational environment (R, Stata or Python) for a replication package and writes the matching lockfiles and version records. | [view](psantanna-workflow/capture-environment.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/capture-environment/SKILL.md) | 2026-09-26 |
| [`/replication-package`](psantanna-workflow/replication-package.md) | economics | `replication` `dissemination` | Assembles a submission-ready replication package to the AEA Data and Code Availability Standard: README, dataset manifest, computational requirements, table and figure map. | [view](psantanna-workflow/replication-package.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/replication-package/SKILL.md) | 2026-09-26 |

### `review` (14)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/devils-advocate`](psantanna-workflow/devils-advocate.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/devils-advocate.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/devils-advocate/SKILL.md) | 2026-08-21 |
| [`agent:domain-referee`](psantanna-workflow/domain-referee.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/domain-referee.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/domain-referee.md) | 2026-09-26 |
| [`agent:domain-reviewer`](psantanna-workflow/domain-reviewer.md) | economics | `referee-simulation` | Template agent for substantive domain review of a lecture deck or manuscript section: derivation correctness, assumption sufficiency, citation fidelity, code-theory alignment, logical consistency. | [view](psantanna-workflow/domain-reviewer.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/domain-reviewer.md) | 2026-09-26 |
| [`agent:editor`](psantanna-workflow/editor.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/editor.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/editor.md) | 2026-09-26 |
| [`agent:methods-referee`](psantanna-workflow/methods-referee.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/methods-referee.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/methods-referee.md) | 2026-09-26 |
| [`/oracle-review`](psantanna-workflow/oracle-review.md) | economics | `referee-simulation` | Runs an external frontier-model referee from a different vendor (via the Oracle CLI) on a paper, proof, estimator or replication package, then triages each finding as confirmed, refuted or downgraded. | [view](psantanna-workflow/oracle-review.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/oracle-review/SKILL.md) | 2026-09-27 |
| [`agent:r-package-reviewer`](psantanna-workflow/r-package-reviewer.md) | economics | `code-generation` | R package source reviewer for CRAN readiness: DESCRIPTION and dependency hygiene, NAMESPACE, roxygen completeness, testthat coverage and CRAN-policy red flags. | [view](psantanna-workflow/r-package-reviewer.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/r-package-reviewer.md) | 2026-09-26 |
| [`agent:r-reviewer`](psantanna-workflow/r-reviewer.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/r-reviewer.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/r-reviewer.md) | 2026-09-26 |
| [`/review-paper`](psantanna-workflow/review-paper.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/review-paper.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/review-paper/SKILL.md) | 2026-09-26 |
| [`/review-r`](psantanna-workflow/review-r.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/review-r.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/review-r/SKILL.md) | 2026-09-26 |
| [`/seven-pass-review`](psantanna-workflow/seven-pass-review.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/seven-pass-review.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/seven-pass-review/SKILL.md) | 2026-09-27 |
| [`agent:sim-reviewer`](psantanna-workflow/sim-reviewer.md) | economics | `formal-modeling` | Monte Carlo simulation reviewer: assumption regime, DGP and estimand alignment, replication budget and Monte Carlo SE, coverage against the truth, and parallel-seed discipline. | [view](psantanna-workflow/sim-reviewer.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/sim-reviewer.md) | 2026-09-26 |
| [`agent:slide-auditor`](psantanna-workflow/slide-auditor.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/slide-auditor.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/slide-auditor.md) | 2026-09-26 |
| [`agent:tikz-reviewer`](psantanna-workflow/tikz-reviewer.md) | economics | `referee-simulation` | — | [view](psantanna-workflow/tikz-reviewer.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/agents/tikz-reviewer.md) | 2026-09-26 |

### `revision` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/adjudicate-review`](psantanna-workflow/adjudicate-review.md) | economics | `revision-editing` | Treats every incoming review finding (referee, AI reviewer, linter, second model) as a candidate, checks it against the source, and applies only verified fixes. | [view](psantanna-workflow/adjudicate-review.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/adjudicate-review/SKILL.md) | 2026-09-26 |
| [`/respond-to-eval`](psantanna-workflow/respond-to-eval.md) | economics |  | Turns student course evaluations into a teaching-improvement plan: clusters comments into themes and classifies each as Keep, Change or Investigate. | [view](psantanna-workflow/respond-to-eval.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/respond-to-eval/SKILL.md) | 2026-09-27 |
| [`/respond-to-referees`](psantanna-workflow/respond-to-referees.md) | economics | `revision-editing` | — | [view](psantanna-workflow/respond-to-referees.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/respond-to-referees/SKILL.md) | 2026-09-27 |

### `slides` (3)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/create-lecture`](psantanna-workflow/create-lecture.md) | economics | `dissemination` | — | [view](psantanna-workflow/create-lecture.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/create-lecture/SKILL.md) | 2026-09-26 |
| [`/slide-excellence`](psantanna-workflow/slide-excellence.md) | economics | `dissemination` | — | [view](psantanna-workflow/slide-excellence.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/slide-excellence/SKILL.md) | 2026-09-26 |
| [`/teach-from-paper`](psantanna-workflow/teach-from-paper.md) | economics |  | Turns a research paper into teaching materials: lecture outline, the key results with intuition, a slide skeleton for /create-lecture, discussion questions and a problem-set brief. | [view](psantanna-workflow/teach-from-paper.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/teach-from-paper/SKILL.md) | 2026-09-27 |

### `submission` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/deploy`](psantanna-workflow/deploy.md) | economics | `dissemination` | — | [view](psantanna-workflow/deploy.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/deploy/SKILL.md) | 2026-08-22 |
| [`/submission-disclosures`](psantanna-workflow/submission-disclosures.md) | economics | `dissemination` | Generates the submission-time disclosure block: AI-use statement matched to the target journal policy, CRediT roles, conflict-of-interest and data-availability statements. | [view](psantanna-workflow/submission-disclosures.md) | [origin](https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/submission-disclosures/SKILL.md) | 2026-06-10 |
