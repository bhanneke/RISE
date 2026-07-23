<!-- DO NOT EDIT — auto-copied from skills/auto-empirical-research-skills/details/aer-referee-sim.md -->

# `aer-referee-sim`

Adversarial internal review before submission — simulates the AER desk screen plus three referee reports with calibrated severity, scores against the editorial rubric, and produces a prioritized revise list; rerun until the simulated verdict is at least major R&R.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../auto-empirical-research-skills/">Auto-Empirical Research Skills (AERS) — first-party skills</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>CC BY-SA 4.0 (repo default); MIT for the mirrored first-party collections (StatsPAI, AER-skills, Paper-WorkFlow)</code></div><div><b>Updated:</b> 2026-07-22</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Auto-Empirical-Research-Skills/contents/skills/50-brycewang-aer-skills/skills/aer-referee-sim/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/auto-empirical-research-skills/aer-referee-sim/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-referee-sim/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Auto-Empirical-Research-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## AER Referee Simulation

### Overview

Most papers submitted to AER are rejected; the realistic acceptance rate is
6-8 percent, and a large share never reach referees. The cheapest referee
report is the one generated **before** submission — but only if it is as
harsh as the real one. The failure mode of self-review (human or AI) is
leniency: reviewing the paper one hopes was written instead of the one on
the page.

This skill runs the AER editorial process against the draft: a ten-minute
desk screen, then three referee reports written from distinct, adversarial
priors, then an editor's synthesis with a calibrated verdict and a
prioritized revise list. The simulation has one rule that overrides all
others:

> **The simulated reviewers' job is to reject the paper. Every comment must
> survive the question "would this withstand the authors' best rebuttal?" —
> but praise requires the same evidence as criticism.**

### When to Use

- A complete draft exists (body, exhibits, bibliography) and
  `aer-consistency` reports all-pass
- Before every submission and resubmission
- After a real rejection, to test whether the revision would survive the
  same reports
- When coauthors disagree about whether the paper is ready

Do not use on a half-draft — the simulation will correctly report that the
paper is incomplete, which wastes the run. And do not let it replace
`aer-consistency`: typo-hunting referees are wasted referees.

### Stage 1 — The Desk Screen

Simulate the editor's first pass: **ten minutes, first three pages, then the
main tables, then the bibliography**. The editor is deciding only one thing —
is this worth three referees' time?

Work through `docs/desk-rejection-audit.md` items 1-5 plus three scans:

- **Contribution scan.** Can the editor state the contribution in one
  sentence after page 3? Would an economist outside the subfield care?
- **Design scan.** Is the identification strategy named on page 1-2, and is
  it a modern design (`aer-identification` red flags apply on sight)?
- **Craft scan.** Tables in house style, abstract within 100 words, prose
  free of the failure patterns in `docs/style-guide.md`. Editors read craft
  as a proxy for care in the empirics.

Output a desk decision with the editor's two-paragraph letter:

```text
DESK DECISION: <reject | send to referees>
LETTER: <the letter an AER editor would actually send>
```

Calibration: if any Stage 1-2 item in the desk-rejection audit fails, the
decision is **reject** — write the letter and stop. Do not soften a desk
reject into "borderline" to keep the simulation going; fix the draft and
rerun.

### Stage 2 — Three Referee Reports

Three referees, three priors, three reading orders. Each writes
independently — draft all three before reconciling anything, and never let
R2 inherit R1's findings.

#### Referee 1 — The identification specialist

Reads: Empirical Strategy first, then Data, then the robustness appendix.
Prior: "the design is broken until proven otherwise."

Attacks: the identifying assumption's plausibility *in this setting*;
missing diagnostics from the `aer-identification` battery; inference
mismatched to the variation's level; estimand-population gaps (whose effect
is this?); the alternative story the design cannot exclude. R1 re-derives at
least one magnitude from the tables and checks it against the prose.

#### Referee 2 — The field expert

Reads: Introduction, then the antecedents, then Results against the
literature. Prior: "we probably already knew this."

Attacks: novelty against the working-paper frontier (names the closest
papers, including any the draft missed — `aer-literature`'s map is the
checklist); whether magnitudes are plausible next to the literature's;
whether the mechanism evidence distinguishes the favored channel from the
obvious rival; institutional errors a field insider would catch. R2 is the
referee most likely to have written one of the antecedents.

#### Referee 3 — The generalist

Reads: linearly, as an editor-board member from another subfield. Prior:
"why should I care, and can I follow it?"

Attacks: cross-subfield interest (the explicit AER bar); whether the first
three pages are self-contained; under-interpreted results (coefficients
never converted to economic meaning — `aer-paper-body` rules); exhibit
overload or disorder; the conclusion overreaching the evidence; external
validity left unaddressed.

#### Report format (each referee)

```text
SUMMARY: <2-3 sentences — the paper as the referee understood it>
MAJOR COMMENTS: <numbered; each one: quote or cite the page/table,
  state the problem, state what evidence would resolve it>
MINOR COMMENTS: <numbered, brief>
RECOMMENDATION: <reject | major revision | minor revision | accept>
```

Rules of engagement:

- Every major comment is **anchored** — it quotes the manuscript or names
  the exact table/figure. Unanchored vibes ("the paper feels thin") are
  banned.
- Every major comment is **resolvable** — it states what analysis, evidence,
  or rewrite would satisfy the referee. Comments with no resolution path
  are editor material, not referee material.
- Each referee must produce **at least three major comments** or explicitly
  certify, against their own checklist, why fewer exist. An AI reviewer
  that finds nothing major has defaulted to agreeable — restart that report
  with the prior dialed up.
- No praise sandwiches. One sentence of genuine strengths in the summary is
  the cap.

### Stage 3 — Editor Synthesis and Verdict

Score the paper on the rubric in `docs/referee-report-rubric.md`
(contribution, identification, data, robustness, magnitudes, exposition,
integrity — each 0-5 with anchored definitions), then issue the decision the
reports support:

```text
RUBRIC SCORES: <dimension: score, ...>
VERDICT: <desk reject | reject after review | major R&R | minor R&R>
DECISION LETTER: <editor's letter, naming the comments that drove it>
REVISE LIST: <every major comment, deduplicated, ordered by severity:
  blocking → major → minor, each tagged with the skill that fixes it>
```

Calibration anchors (do not inflate):

- Any rubric dimension at 0-1 → reject. Identification ≤ 2 → reject;
  no robustness round fixes a broken design.
- Major R&R requires: contribution ≥ 3, identification ≥ 3, no dimension
  below 2. This is already a top-decile outcome for real submissions.
- Minor R&R from a simulation should be **rare** — if the first run returns
  minor R&R, suspect leniency and rerun Stage 2 with the priors sharpened.

### The Loop

```text
aer-consistency (all PASS)
   → aer-referee-sim
        → verdict reject? → route fixes:
              identification comments → aer-identification / aer-robustness
              novelty comments        → aer-literature / aer-topic-selection
              interpretation comments → aer-paper-body
              framing comments        → aer-introduction
              exhibit comments        → aer-tables-figures
        → revise → aer-consistency → aer-referee-sim (fresh reports)
   → verdict ≥ major R&R on a fresh run → aer-submission
```

Rerun with **fresh** reports each time — re-grading old comments measures
compliance, not quality. Two consecutive runs at major-R&R-or-better, with
no blocking comments, is the exit condition.

### Honesty Constraints for the Simulation

- The reviewers attack the manuscript, not a summary of it. If the draft is
  too long to hold at once, review it section by section against each
  referee's checklist — never from recall.
- Findings of fact (a wrong conversion, a missing diagnostic, a scooped
  contribution) must be verified before they enter a report; a simulated
  referee who hallucinates a flaw costs a revision round.
- Report the verdict to the user **unsoftened**. "The simulation desk-
  rejected the draft for X" is the deliverable, not a diplomatic summary.
- The simulation cannot certify acceptance — only that the draft survives
  the attacks this skill knows how to mount. Say so in the output.

### Common Failure Modes

- Referees that paraphrase the paper's own framing back as praise
- Three reports that are one report with three names — the priors and
  reading orders exist to prevent this
- Major comments that are really minor (citation formatting promoted to
  "major" pads the count without testing the paper)
- Re-running the simulation until it happens to pass, without changing the
  draft — variance is not improvement
- Treating the simulated verdict as a prediction of the real one rather
  than a lower bound on preparedness

### Repository Resources

Bundled with the installed skill, no repository checkout needed --- read it
before the repo resources below:

- `references/scoring-rubric.md` --- anchored 0-5 rubric, verdict mapping, desk-screen and report templates

When working from the AER-skills repository or plugin bundle, load only the
relevant resource:

- Scoring rubric with anchored 0-5 definitions and a calibrated sample
  report: `docs/referee-report-rubric.md`
- Complete worked simulation (two runs, three reports, routed revise
  list): `examples/referee-report-example.md`
- Desk-screen checklist the Stage 1 editor runs: `docs/desk-rejection-audit.md`
- Identification red flags Referee 1 hunts: `skills/aer-identification/SKILL.md`
  and `docs/methods-reference.md`
- Referee-anticipation battery Referee 1 checks for completeness:
  `skills/aer-robustness/SKILL.md`
- Prose failure patterns the desk screen scans: `docs/style-guide.md`
- Response-letter conventions for acting on the revise list:
  `skills/aer-rebuttal/SKILL.md`

### Handoff

```text
DESK DECISION: <reject | sent to referees>
REFEREE RECOMMENDATIONS: <R1 / R2 / R3>
RUBRIC SCORES: <list>
VERDICT: <desk reject | reject | major R&R | minor R&R>
BLOCKING COMMENTS: <n — list>
REVISE LIST: <comment → skill routing>
NEXT SKILL: <routed fix skill | aer-submission if exit condition met>
```

### Anti-Patterns

- Running the simulation as a checklist instead of as three hostile readers
  with different stakes
- Letting the model grade its own prose generously because it recognizes it
- Skipping Stage 1 because "we know it won't desk-reject" — the desk screen
  catches different failures than referees do
- Accepting one lucky major-R&R run as the exit condition
- Using the simulation's praise in the cover letter — its only export is
  the revise list
