<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/rt-workflow.md -->

# `rt-workflow`

Sequences a manuscript across venues — which cross-journal toolkit skill to invoke next, from picking a target journal through execution, submission-readiness, simulated review, rebuttal, and the replication package.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Research-Toolkit-Skills/skills/rt-workflow/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/rt-workflow/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Research-Toolkit-Skills/skills/rt-workflow/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Cross-Journal Workflow Router (rt-workflow)

The author-side loop that runs *across* journals, complementing the per-journal depth
packs (which answer "how do I clear THIS venue's bar?"). Each step is backed by a
canonical capability doc in `shared-resources/`.

### When to trigger

- You have a result/draft and don't yet know the venue, or just got a reject and need the next target.
- You are mid-project and want the next cross-journal step.
- You want the end-to-end sequence: pick → execute → ready → rehearse → submit → rebut → replicate.

### The loop (and the skill that owns each step)

1. **`rt-journal-match`** — profile the paper → ranked reach/match/safe shortlist + resubmission ladder.
2. **`rt-execution-bridge`** — run the analysis through the StatsPAI / Stata MCP tools (estimate + audit), not just advise it.
3. **`rt-submission-readiness`** — go/no-go scorecard on the manuscript against the target venue's bar.
4. **`rt-simulated-referee`** — rehearse a calibrated AE + referee panel; surface the decisive objections before a real referee does.
5. **(fix)** — route each objection back to the target pack's skill + the execution bridge.
6. **`rt-response-to-referees`** — after an R&R, draft the point-by-point reply + revision plan (editor first).
7. **`rt-replication-package`** — assemble + validate the Data-Editor package against the venue's data-and-code policy.

### Routing table

| Symptom | Go to |
|---|---|
| "Where should I send this?" / "Rejected — what next?" | `rt-journal-match` |
| "I need to actually run the DiD/IV/RDD/SCM/DML, not just plan it" | `rt-execution-bridge` |
| "Is it ready to submit?" | `rt-submission-readiness` |
| "What will referees attack?" | `rt-simulated-referee` |
| "I have an R&R to answer" | `rt-response-to-referees` |
| "The Data Editor needs a replication package" | `rt-replication-package` |

### How it relates to the per-journal packs

This router sequences the *cross-journal* steps; the **venue bar and all live facts**
(fees, limits, acceptance, data policy, house style) come from the chosen pack's own
skills and `resources/official-source-map.md`. Always defer venue-specific judgment to
that pack — this toolkit picks the venue, runs the analysis, and rehearses the gauntlet.

### Anti-patterns

- Submitting before `rt-submission-readiness` clears the mechanical bar.
- Picking a venue without reading its live source-map facts (`rt-journal-match` hard rule).
- Treating the simulated referee as a verdict rather than a rehearsal.

### Output format

```
【Current step】pick / execute / ready / rehearse / respond / replicate
【Next skill】rt-...
【Why】one line
【Venue bar source】<target pack>/resources/official-source-map.md + skills
```
