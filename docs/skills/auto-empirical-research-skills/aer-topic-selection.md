<!-- DO NOT EDIT — auto-copied from skills/auto-empirical-research-skills/details/aer-topic-selection.md -->

# `aer-topic-selection`

Evaluates whether a research idea clears the AER top-5 bar, routes between AER, AER:Insights, and the AEJ family, and sharpens a fuzzy contribution sentence into one publishable claim.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../auto-empirical-research-skills/">Auto-Empirical Research Skills (AERS) — first-party skills</a></div><div><b>Category:</b> <code>ideation</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>CC BY-SA 4.0 (repo default); MIT for the mirrored first-party collections (StatsPAI, AER-skills, Paper-WorkFlow)</code></div><div><b>Updated:</b> 2026-07-22</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>rq-formulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Auto-Empirical-Research-Skills/contents/skills/50-brycewang-aer-skills/skills/aer-topic-selection/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/auto-empirical-research-skills/aer-topic-selection/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-topic-selection/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Auto-Empirical-Research-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## AER Topic Selection

### Overview

The single most expensive mistake in top-5 economics is writing a polished manuscript around a contribution that was always going to be desk-rejected. This skill is the **pre-mortem**: stress-test the idea, the audience, and the venue *before* the introduction is drafted.

AER accepts only a small share of submissions — on the order of **6–8%** historically (Card and DellaVigna 2013, *Nine Facts about Top Journals*), and recent *Reports of the Editor* put the rate lower still. A large fraction of submissions are desk-rejected before ever reaching a referee; for *AER: Insights*, founding editor Amy Finkelstein has reported desk-rejecting "roughly 45%" of submissions. Either way, much of a paper's survival probability is determined before the first paragraph is written.

### When to Use

- A new project just started and the contribution sentence cannot be written in one line
- The user is undecided between submitting to AER, AER: Insights, or an AEJ
- A prior submission was desk-rejected and the user wants to diagnose whether the topic itself was the problem
- The paper "feels solid" but no senior colleague has agreed to send it to AER

### The Top-5 Bar

A paper clears the top-5 bar if and only if **all four** are true:

1. **Cross-subfield interest.** A labor economist's paper must matter to public, macro, IO, and development economists. Not the median person — the editor. If you cannot name three subfields that would cite it, it is an AEJ paper.
2. **Substantive contribution.** Methodological extension *or* substantive new fact *or* new identification *or* genuinely new data. Competent application of an existing toolkit is desk-rejected.
3. **Self-contained in the first 3 pages.** The editor decides in ten minutes. If understanding the contribution requires the appendix, the paper fails.
4. **Defensible identification or model discipline.** Empirical: design-based, not selection-on-observables. Theory: tractable result with an empirical or policy hook.

If any single test fails, the realistic target is an AEJ or a top field journal, not AER.

### Venue Routing

| Signal                                                            | Target            |
|-------------------------------------------------------------------|-------------------|
| Cross-subfield interest + ≥ 40 pages of substance                 | **AER**           |
| One sharp result, fits the AER: Insights word/exhibit formula, can be told without a long lit review | **AER: Insights** |
| Strong but subfield-bounded contribution; methodologically sound  | **AEJ: Applied / Policy / Macro / Micro** |
| Conventional method, modest extension, useful for one literature  | Top field journal |
| Field experiment with policy hook                                 | AER, AEJ:Applied, or QJE — register in **AEA RCT Registry** *before* submission |

For AER: Insights specifically, the editor (Amy Finkelstein) has stated that a great short paper "makes one point and makes it clearly, concisely, and effectively." If you have a second point, write a second paper.

### The Contribution Sentence Test

Force the contribution into one sentence with this template:

```
We show that X causes Y, identified by Z, using data D, with magnitude M,
which changes the way economists think about Q.
```

If any blank cannot be filled in:

- **X / Y unclear** → the research question is not yet a question
- **Z weak** → return to `aer-identification` before doing anything else
- **D thin** → small-sample, unreplicable, or off-the-shelf data is desk-reject bait
- **M unknown** → results don't exist yet; this is not a topic-selection problem
- **Q absent** → this is an AEJ paper, not an AER paper

### Novelty Audit

Run these five questions (the search protocol and antecedents map live in
`aer-literature` — use it to answer them with evidence, not recall):

1. Has someone in NBER, IZA, CEPR, or SSRN already done this? (Search before writing.)
2. Is the closest published paper in a top-5 within the last 5 years? If yes, what does yours add — new method, new setting, new mechanism, opposite sign?
3. Does the result *change a policy debate*, *flip a stylized fact*, or *unify two strands of literature*?
4. Could a senior referee compress your contribution into "well, we already knew that"?
5. Could a senior referee compress your contribution into "interesting but it's not economics"?

A "yes" to (4) or (5) is fatal at AER.

### Desk Rejection Red Flags

The editor scans for these in the first ten minutes:

- Correlational language masquerading as causal ("our results suggest a relationship between ...")
- An introduction that runs more than 3 pages without naming the data or the identification strategy
- A 14-column table 1 with no headline takeaway
- Spelling, formatting, or LaTeX-bibliography errors visible on the first page
- Abstract over 100 words
- Excessive reliance on the online appendix ("see appendix B for the main result")
- Methodology mismatch — claims causal identification but reports OLS with controls

If any of these are present, fix them before submission.

### Pre-Submission Seminar Sequence

Peer feedback measurably improves journal placement: one SD more comments → 47% higher journal quality. Before sending to AER, target:

1. Internal brown-bag — 2 rounds, separated by ≥ 6 weeks
2. ≥ 2 external seminars at peer or top-tier departments
3. ≥ 1 NBER / CEPR / IZA conference presentation
4. Working paper posted ≥ 3 months before submission

Skip none of these for an AER target. AER: Insights tolerates a shorter cycle because the contribution is sharper and the venue is younger.

### Repository Resources

Bundled with the installed skill, no repository checkout needed --- read it
before the repo resources below:

- `references/venue-router.md` --- AER vs Insights vs AEJ routing tables, novelty audit, and kill criteria

When working from the AER-skills repository or plugin bundle, load only the
relevant resource:

- Recent AER/AEJ exemplars by subfield: `examples/modern-aer-exemplars.md`
- Classic contribution archetypes: `examples/aer-exemplars.md`
- Desk-rejection no-go audit: `docs/desk-rejection-audit.md`
- Workflow routing after the topic decision: `docs/workflow-map.md`

### Go / No-Go Gate

Advance to `aer-identification` / `aer-introduction` only if **all** hold; otherwise route down (AEJ / field journal) or stop:

- [ ] Contribution sentence written in one line with every blank (X, Y, Z, D, M, Q) filled
- [ ] All four Top-5 Bar tests evaluated; AER chosen as target only if all four pass
- [ ] Target venue named explicitly, with a one-sentence reason it is not one tier lower
- [ ] No kill switch live — no "and we also explore", no "we already knew that", no "interesting but not economics"
- [ ] At least three subfields that would plausibly cite the paper can be named

### Handoff

When this skill finishes, emit:

```text
CONTRIBUTION SENTENCE: <one line>
TARGET VENUE: <AER | AER:Insights | AEJ:Applied | AEJ:Policy | AEJ:Macro | AEJ:Micro>
TOP-5 BAR TESTS PASSED: <count>/4
KILL SWITCHES TRIGGERED: <list, or "none">
NEXT SKILL: <aer-literature | aer-identification>
```

### Anti-Patterns

- Choosing the venue based on prestige rather than fit. An AEJ acceptance beats two AER rejections.
- Letting the contribution sentence include "and we also explore ..." — that *and* is where the paper dies.
- Submitting to AER because "the bar is the same as AEJ anyway." It is not. Cross-subfield interest is the explicit filter.
