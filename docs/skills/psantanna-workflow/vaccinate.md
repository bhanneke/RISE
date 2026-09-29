<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/vaccinate.md -->

# `/vaccinate`

Qualifies a checker before trusting it: seeds known defects into a copy of a real artifact plus a clean control and reports recall and false-positive rate.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/vaccinate/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/vaccinate/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/vaccinate/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Vaccinate — grade the grader

Twenty bugs were once planted in a working codebase and the review agents were asked to check
it again. They reported everything was fine. **Recall: 0/20.**

A vaccine is a small, controlled dose of error that strengthens the whole system. This skill
administers one.

**The rule it enforces: an unqualified check is not weak evidence — it is none.**

### When to run it

- Before a referee simulation, reproducibility gate, or review agent is used to make a
  decision that matters (a submission, a release, a deposit).
- After changing a checker — a modified gate is unqualified until re-measured.
- On a schedule for gates that guard load-bearing claims. Detection decays as artifacts drift.

### Protocol

#### 1. Name the failure

State the defect **class** the check is supposed to catch. "Catches problems" is not a class.
"Detects a coefficient in the text that no longer matches its table" is.

#### 2. Build the seeded set + a clean control

Work on a **copy**, never the live artifact. Produce:

- **N seeded variants**, one defect each, drawn from `references/defect-library.md`.
- **At least one clean control** — an unmodified copy.

The control is not optional. Without it you measure recall and call it accuracy.

**Verify each seed actually violates something.** A seed that the artifact already permits
creates no defect, and the checker correctly reporting "pass" will look like a broken gate.
This is the most common way a qualification run produces a false alarm about itself.

#### 3. Run the checker blind

Run the check or agent against each variant **in a fresh context**, one variant per run. It
must not know which variant it has, how many defects exist, or that a qualification is
underway. For an AI reviewer, spawn a fresh-context `Agent` call (not a conversation fork, which would carry the seeded answer key).

#### 4. Score

| Metric | Definition |
|---|---|
| **Recall** | seeded defects correctly identified / seeded defects planted |
| **False-positive rate** | findings on the **clean control** that are *factually false* / total findings on the control |
| **Localization** | did it name the right location, or just report unease? |
| **Baseline delta** | recall of a **simpler alternative** (a grep, a diff, a one-line assertion) |

A finding on the clean control counts as a false positive only when it is **factually
wrong** — not merely unwelcome. A reviewer prompted to find gaps will report some in sound
work; that is expected behaviour, not a failure.

**The baseline is load-bearing.** A five-agent panel that scores no better than `grep -n` has
not earned its cost.

#### 5. Write the ledger row

Append to `quality_reports/qualification/LEDGER.md`:

```
| date | target | artifact | defect classes | N | recall | FPR | baseline | verdict |
```

Verdicts: **PASS** (detects its named class at an agreed threshold) · **FAIL** (misses it) ·
**BLOCKED** (could not be run — say why; do not record as PASS).

#### 6. Act on the result

- **FAIL** → the check does not license its claim. Fix the check or stop citing it. Do **not**
  weaken the seed until it passes.
- **PASS** → record the threshold. A PASS at one difficulty is not a PASS at another.
- Either way, a checker with no ledger row is **unqualified**, and its green light means
  nothing.

### Worked example

```
/vaccinate check-model-versions.sh
```

1. Failure class: "a superseded model presented as current".
2. Seed: append `The newest model is Opus 4.8 and it is the default.` to `README.md`.
   Control: unmodified `README.md`.
3. Run: `bash scripts/check-model-versions.sh; echo $?`
4. Score: seeded → exit **1** (detected). Control → exit **0** (no false alarm).
   Recall 1/1, FPR 0/0. Baseline: `grep -c "Opus 4.8" README.md` also detects — so the gate's
   value is its *allow-marker logic*, not raw detection.
5. Ledger: `PASS`.
6. Restore the artifact and re-run to confirm you are back to green.

### Anti-patterns

- **Seeding into an artifact that already permits the seed** — measures nothing, looks like a
  broken gate.
- **Telling the reviewer it is a test** — it will look harder than it does in production.
- **Counting any finding as a hit** — a finding at the wrong location is not detection.
- **One seed, one run** — a single trial does not distinguish detection from luck. Use ≥2
  replicates per class where cost allows.
- **Weakening the seed until it passes** — that is fitting the test to the checker.
- **Skipping the clean control** — the most common omission, and it hides the cost.

### Reference files

| File | Read when |
|---|---|
| `references/defect-library.md` | choosing what to seed — defect classes by artifact type |
| `evals/README.md` | the complementary question: does the *skill* produce better output than not having it? |


---

## Doctrine: what qualification means

### Do not assume more machinery is better

A second model, more agents, or a longer debate is **not** presumed to verify better. Before an elaborate procedure earns extra weight, show it outperforms a simpler check on the same prespecified seeded failures and valid cases, reporting both detection and false alarms. Complexity that has not beaten a baseline is cost, not assurance.

### Treat AI verdicts as predictions, not facts

When a model grades, triages, or reviews at scale:
- keep a **sampled set for qualified human review**, and record how it was sampled (retain coverage of hard subgroups — do not sample only the easy middle);
- keep fitting/prompt-tuning cases **separate** from evaluation cases;
- report where AI and expert judgments diverge;
- remember a well-calibrated *average* score certifies no individual verdict;
- **agreement between models is not independent evidence** — they share failure modes and converge on the same wrong answer at a meaningful rate.

Any material change to the model, prompt, rubric, or target population requires fresh human labels and recalibration.

### Requalify after material change

A check qualified against an old interface, schema, or scale may silently stop testing anything. Re-run the seeded-defect proof after material changes to the object under test or to the check itself.

### Distinguish qualified checks from scientific judgments

- **Qualified checks** have a defensible reference answer: unique keys, units convert, a table
  regenerates, an estimator recovers an analytic special case, a seeded fault triggers a
  failure. These can be automated and rerun forever.
- **Scientific judgments** — whether a field measures the intended construct, whether an
  identifying assumption is plausible, whether a result deserves causal language — cannot be
  automated, and **no volume of qualified checks substitutes for one.**

### Confirm the check actually ran

A missing, substituted, or degraded check is **missing evidence**, not a pass. Verify the run
happened (log, exit status, artifact timestamp — not an assumption); that it ran on the
**current** object, not a cached one; that nothing was skipped, filtered, or swallowed into a
default; and that the tolerance was fixed **before** the comparison. *A tolerance loosened
after a failed comparison converts evidence into decoration.* If it must be loosened, record
it as an approved divergence with a reason.

### Cross-references

- `verification-ladder.md` — rung 0; why this comes before everything
- Merged with the former `/qualify-checks` (2026-08-21): same goal — one skill, not two
- `external-oracle-process.md` — qualifying an external referee
