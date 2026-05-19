# Paper Revision Workflow

## Purpose

Guide the systematic revision of a manuscript in response to reviewer reports
and an editor's decision letter. This skill covers the full workflow from
reading reports to producing a revised manuscript with point-by-point responses.

For formatting the response letter itself, see `writing/referee-response`.

---

## Revision Phases

### Phase 1: Triage the Reports

Read all reviewer reports and the editor's letter. Classify every comment:

| Category | Description | Priority |
|----------|-------------|----------|
| **Fundamental** | Challenges identification, causality, core contribution | Must address first |
| **Methodological** | Estimation issues, robustness, alternative specs | High |
| **Data/measurement** | Variable definitions, sample selection, data quality | High |
| **Exposition** | Clarity, structure, writing, notation | Medium |
| **Bibliography** | Missing citations, DOI, reference formatting | Medium |
| **Minor** | Typos, formatting, cosmetic | Low |

**Key rule:** Do not start writing until you have read ALL reports and mapped
every comment to a paper section. Some comments interact — a causality concern
from Referee 1 may be addressed by the robustness check requested by Referee 2.

### Phase 2: Address Causality and Identification First

Reviewers' concerns about causal identification are the single most common
reason for rejection in empirical papers. Address these before anything else.

**Checklist for estimation / causality concerns:**

- [ ] Is the identification strategy clearly stated? (source of variation,
      exclusion restriction, parallel trends assumption)
- [ ] Are threats to identification listed and addressed?
- [ ] Are standard errors correct? (clustering level, heteroskedasticity)
- [ ] Is the estimator appropriate? (OLS when you need IV? DiD without pre-trends?)
- [ ] Are the key coefficients causally interpretable or merely correlational?
      If correlational, is this stated clearly?
- [ ] Do robustness checks address the specific concerns raised, not generic ones?
- [ ] Are placebo tests, falsification tests, or pre-trend analyses included
      where applicable?

**When the reviewer says "this is not causal":** Do not just add caveats.
Either (a) strengthen the identification strategy with additional analysis, or
(b) reframe the contribution around the descriptive/correlational finding and
explain why it is valuable on its own terms. Half-measures ("we acknowledge
this is correlational" while still making causal claims) will be rejected.

### Phase 3: Systematic Section-by-Section Revision

Map each reviewer comment to the specific section(s) it affects. Then revise
section by section, addressing all mapped comments for that section in one pass.

| Paper section | Common reviewer concerns |
|---------------|-------------------------|
| Introduction | Contribution unclear, overpromising, missing related work |
| Literature review | Missing key references, shallow engagement, no DOI |
| Model/Theory | Assumptions not justified, notation inconsistent |
| Data | Sample selection unclear, variable definitions missing |
| Estimation/Results | Causality, robustness, alternative specifications |
| Discussion | Over-interpreting, ignoring limitations |
| Conclusion | Repeating results without insight |
| References | Missing DOI, inconsistent formatting, orphan citations |

### Phase 4: Bibliography and DOI Enforcement

**Every reference MUST have a DOI.** This is a hard requirement, not a suggestion.

1. Run a DOI completeness check on the `.bib` file.
2. For each entry missing a DOI, look it up via CrossRef Simple Text Query.
3. Use `\usepackage{doi}` in the preamble so DOIs render as clickable links.
4. Use `plainnat` bibliography style (or another DOI-displaying style).
5. Only exceptions: pre-DOI publications, unpublished manuscripts, datasets.

### Phase 5: Draft the Response Letter

Use the `writing/referee-response` skill for formatting. Key principles:

- Quote every comment verbatim.
- Address every comment — never skip one.
- Provide page/line references for all changes.
- For causality concerns, explain the specific analysis added (not just "we
  revised the section").
- Cross-reference when multiple referees raise the same issue.

### Phase 6: Verification

Before submitting:

- [ ] Every reviewer comment has a response
- [ ] All new tables/figures are numbered and referenced
- [ ] DOI present for all references (run reference checker)
- [ ] `\usepackage{doi}` in preamble, `plainnat` or DOI-enabled `.bst`
- [ ] Track changes or marked-up manuscript prepared
- [ ] No orphan citations or orphan references
- [ ] Causality/identification section has been strengthened (not just caveated)
- [ ] Response letter has page/line references for all changes

---

## Integration with Workers

| Task | Worker | Key skills |
|------|--------|-----------|
| Read & triage reviewer reports | `virtual_coauthor` | This skill + `reasoning/argument-audit` |
| Revise estimation/causality | `econometrics_worker`, `causal_inference` | `econometrics/*`, `causal-inference/*` |
| Revise prose sections | `paper_drafter` | `writing/paper-structure`, this skill |
| Draft LaTeX response letter | `latex_drafter` (section: referee-response) | `writing/referee-response` |
| Check bibliography DOIs | `reference_checker` | `review/reference-check`, `latex/bibtex` |
| Full quality review of revision | `deep_review` | `review/*` |

---

## Anti-Patterns

- **Defensive revisions.** Adding caveats ("we acknowledge this limitation")
  without substantive changes. Reviewers see through this.
- **Cosmetic robustness.** Adding 10 robustness tables that all use the same
  flawed identification strategy. Fix the strategy, then show robustness.
- **Ignoring the editor.** The editor's letter prioritizes concerns. Address
  the editor's specific requests first.
- **Scope creep.** Adding new analyses not requested by reviewers. Stick to
  what was asked unless a new analysis directly addresses a concern.
- **Missing DOI in the revision.** Reviewers specifically check for this.
  It signals carelessness.
