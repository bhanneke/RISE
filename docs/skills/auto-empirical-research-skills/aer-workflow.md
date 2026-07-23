<!-- DO NOT EDIT — auto-copied from skills/auto-empirical-research-skills/details/aer-workflow.md -->

# `aer-workflow`

Router for the 15-skill AER-skills collection — sequences manuscript work from topic selection through rebuttal for AER, AER:Insights, and AEJ journals; routes, does not replace, the specialized skills.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../auto-empirical-research-skills/">Auto-Empirical Research Skills (AERS) — first-party skills</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>CC BY-SA 4.0 (repo default); MIT for the mirrored first-party collections (StatsPAI, AER-skills, Paper-WorkFlow)</code></div><div><b>Updated:</b> 2026-07-22</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Auto-Empirical-Research-Skills/contents/skills/50-brycewang-aer-skills/skills/aer-workflow/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/auto-empirical-research-skills/aer-workflow/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills/blob/main/skills/50-brycewang-aer-skills/skills/aer-workflow/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Auto-Empirical-Research-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## AER Workflow

### Overview

This is the router. It does not replace any specialized skill. It tells you which one to use next, and in what order.

Default assumption: unless the user names a different venue, the manuscript targets **AER**, **AER: Insights**, or an **AEJ** journal — not a finance journal, not a generic economics field journal, and not a working-paper repository.

### When to Use

- The user asks "what should I work on next?"
- The user dumps a draft and you must decide where the bottleneck is
- The user asks for a full paper to be drafted end-to-end and you need the gate sequence
- The user is rotating between writing, empirics, and revision and loses track of which stage they are in
- A new reviewer report has arrived and the work mode must switch from drafting to rebuttal

### Routing Map

Use:

- `aer-topic-selection` when the project is new, when the user is undecided between AER / Insights / an AEJ, or when the contribution sentence cannot be written in one line
- `aer-literature` when the closest papers must be mapped (novelty scan, antecedents paragraph) or when any citation needs verifying — for AI-drafted manuscripts, every citation
- `aer-identification` when the empirical design is the bottleneck — DiD, IV, RDD, SCM, shift-share, event study, RCT analysis
- `aer-preregistration` when the study runs a field/lab/survey experiment or collects primary data — write the pre-analysis plan, size the sample from a power/MDE calculation, and register with the AEA RCT Registry *before* the intervention
- `aer-robustness` when the main results exist but referee-anticipating checks (placebo, heterogeneity, mechanism, alternative samples) are missing or weak
- `aer-paper-body` when drafting or repairing the body sections — background, data, empirical strategy, results narration, magnitude interpretation, mechanisms, conclusion
- `aer-introduction` when drafting or rewriting the introduction, or when the abstract is over 100 words
- `aer-tables-figures` when regression tables are inconsistent, oversized, footnote-bloated, or do not match AER house style
- `aer-consistency` when the assembled manuscript needs the integrity audit — numbers vs. tables, sample sizes, conversions, cross-references, citation two-way match
- `aer-referee-sim` when a complete draft needs the adversarial desk screen and three simulated referee reports before submission
- `aer-replication` when preparing the AEA Data and Code Availability deposit, writing the README, or auditing reproducibility before acceptance
- `aer-submission` when running the final preflight before clicking submit — length, format, cover letter, conflicts
- `aer-rebuttal` when reviewer comments exist and a point-by-point response letter plus aligned manuscript edits are needed
- `aer-statspai` (optional engine) when the design is already fixed and the user wants to *run* the empirics from the agent — a unified Python API / MCP server covering DiD, IV, RDD, SCM, robustness, and table export. It executes what `aer-identification` chose; it does not replace that choice.

### Default Sequence

For most empirical AER-track manuscripts, prefer this order:

1. `aer-topic-selection` — fix the contribution sentence and the target venue *before* anything else
2. `aer-literature` — map the 3-6 closest papers; kill the project now if it is scooped
3. `aer-identification` — stress-test the design; if it fails here, no later skill saves the paper
   - *Experimental / primary-data branch:* if the design randomizes treatment or collects new data, detour to `aer-preregistration` **before** the intervention — pre-analysis plan, power/MDE-justified sample size, AEA RCT Registry timestamp. Skip this branch for observational data already realized.
4. `aer-robustness` — anticipate the three robustness checks the median referee will demand (run the empirics via `templates/` or `aer-statspai`)
5. `aer-paper-body` — draft background, data, strategy, results, mechanisms, conclusion
6. `aer-introduction` — only now write the five-paragraph intro and the 100-word abstract, summarizing a body that exists
7. `aer-tables-figures` — finalize the main exhibits in AER house style
8. `aer-consistency` — the integrity audit; every number, reference, and citation must reconcile
9. `aer-referee-sim` — adversarial internal review; loop back to the routed fix skill until the verdict is at least major R&R on a fresh run
10. `aer-replication` — assemble the deposit package while results are still fresh in code
11. `aer-submission` — final preflight: length, format, cover letter, COI
12. `aer-rebuttal` — after external review, revise manuscript first, then write the letter against the revised version

### Quality Gates for End-to-End Drafting

When the user asks the agent to **write the paper**, the sequence above is a
set of gates, not suggestions. Do not advance past a gate that fails:

- Gate A (after step 3): contribution sentence written, venue chosen, design survives `aer-identification` red flags
- Gate B (after step 5): every claim in the draft body traces to an exhibit or a verified citation
- Gate C (after step 8): `aer-consistency` reports all-pass; `aer-literature` citation ledger fully closed
- Gate D (after step 9): `aer-referee-sim` verdict ≥ major R&R on two consecutive fresh runs
- Gate E (after step 11): `aer-submission` preflight all green

### Decision Cues

If the user says...

- *"I have an idea but I don't know if it's AER-worthy"* → `aer-topic-selection`
- *"Has someone already done this?"* / *"Are these references real?"* → `aer-literature`
- *"My DiD has staggered treatment"* → `aer-identification`
- *"My first stage F is 8"* → `aer-identification` (weak-IV branch)
- *"I'm about to run a field experiment"* / *"What sample size do I need?"* / *"Where do I register the RCT?"* → `aer-preregistration`
- *"The referee said the result might be driven by X"* → `aer-robustness`
- *"My results section just walks through the tables"* → `aer-paper-body`
- *"What does a 0.042 coefficient on log wages mean?"* → `aer-paper-body` (magnitude rules)
- *"My intro is 4 pages and the editor hated it"* → `aer-introduction`
- *"My table 3 has 14 columns"* → `aer-tables-figures`
- *"Do the numbers in my abstract match my tables?"* → `aer-consistency`
- *"Tear this draft apart before I submit"* → `aer-referee-sim`
- *"The Data Editor flagged my README"* → `aer-replication`
- *"I'm submitting tomorrow"* → `aer-submission`
- *"I got an R&R with three reports"* → `aer-rebuttal`
- *"Just run my staggered DiD / IV / RDD for me"* → `aer-statspai` (after the design is settled in `aer-identification`)

### Common Mistakes

- polishing the introduction before the identification strategy is stable
- drafting the body before the empirics exist, then bending results prose to fit promises
- writing the abstract before deciding AER vs AER:Insights (the 100-word limit is the same but the *framing* differs sharply)
- treating tables and figures as a final-week task; AER tables drive how reviewers read results
- submitting without the consistency audit — text-table mismatches are the cheapest rejection trigger there is
- skipping the referee simulation because the deadline is close; the real referees are slower and harsher
- writing the rebuttal letter against the old draft instead of the revised manuscript
- assembling the replication package only after acceptance — the AEA Data Editor's report is now part of the production timeline and can delay publication by weeks
- defaulting to the OLS + cluster-by-state recipe; modern AER demands design-based identification

### Anti-Patterns

- Using a generic "scientific writing" skill in place of `aer-introduction` or `aer-paper-body` — the conventions (no intro heading, five-paragraph Head formula, finding-first results paragraphs, magnitude discipline) are economics-specific
- Using a generic "data availability" skill in place of `aer-replication` — the AEA policy is *unusually* strict and the openICPSR workflow is specific
- Skipping `aer-topic-selection` because "I already know this is an AER paper" — desk rejection across the AER family is high, and the top-5 bar is *cross-subfield interest*, not technical competence
- Letting any skill write citations from memory — `aer-literature`'s verification protocol is mandatory for machine-drafted text
- Treating `aer-referee-sim` praise as evidence of quality; its only export is the revise list

### Repository Resources

Bundled with the installed skill, no repository checkout needed --- read it
before the repo resources below:

- `references/gate-map.md` --- the 12-step lifecycle with entry criteria, gates, and artifacts per step

When working from the AER-skills repository or plugin bundle, load only the
relevant resource:

- Full workflow diagram: `docs/workflow-map.md`
- Editor/referee no-go checklist: `docs/desk-rejection-audit.md`
- Estimator and diagnostic defaults: `docs/methods-reference.md`
- Prose rules shared by the writing skills: `docs/style-guide.md`
- Scoring rubric for the internal review gate: `docs/referee-report-rubric.md`
- Policy source register: `docs/source-register.md`
- SkillOpt-style improvement protocol: `docs/skillopt-evaluation-protocol.md`
- Held-out routing scenarios: `examples/skillopt-routing-scenarios.json`

### Skill Optimization Loop

When improving this skill stack, treat `aer-workflow` as the router under
test. Use `docs/skillopt-evaluation-protocol.md` to collect failures, keep each
patch bounded, and accept routing or gate changes only after
`python3 scripts/run_skillopt_gate.py` and `make preflight` pass. Do not tune the
router by naming only the expected skill; use user-like manuscript prompts from
`examples/skillopt-routing-scenarios.json` or add a new scenario first.

### Handoff Contract

Whenever this skill is invoked, end with:

```text
NEXT SKILL: <aer-skill-name>
REASON: <one sentence>
INPUTS NEEDED: <list of artifacts the next skill needs>
GATE STATUS: <which quality gates are passed / open>
```

This keeps the agent loop tight when the user runs multiple skills in sequence.
