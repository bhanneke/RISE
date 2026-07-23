<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/rt-submission-readiness.md -->

# `rt-submission-readiness`

Venue-parameterized go/no-go scorecard on the actual manuscript — fit, identification, robustness, exhibits, exposition, venue mechanics, data/code, pre-empted objections — returning PASS/FLAG/FAIL per dimension plus desk-reject risk.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>submission</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Research-Toolkit-Skills/skills/rt-submission-readiness/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/rt-submission-readiness/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Research-Toolkit-Skills/skills/rt-submission-readiness/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Submission-Readiness Self-Check (rt-submission-readiness)

The mechanical/structural go/no-go that catches avoidable desk rejects before you hit
submit. Full rubric:
`shared-resources/submission-readiness/readiness-checklist.md`.
It is the outward-facing analogue of the repo's internal `tools/quality_scorecard.py`.

### When to trigger

- The draft is "done" and the author is about to submit to a named venue.
- Before paying a submission fee / starting the portal.
- After `rt-journal-match` selects the target and after `rt-execution-bridge` has run any
  empirical checks the paper depends on.

### Inputs to load

1. The manuscript or submission packet, including front matter, main text, exhibits,
   appendix, data/code statement, and cover letter if drafted.
2. The target journal pack's `README.md`, relevant skills, and
   `resources/official-source-map.md`.
3. Any executed analysis artifacts from `rt-execution-bridge`: result handles, audit gaps,
   robustness outputs, and replication/package notes.

### What it does

Reads the target pack's skills + `resources/official-source-map.md`, inspects the actual
manuscript (cite §/table for every flag), and scores nine dimensions PASS / FLAG / FAIL:

1. Fit & general interest · 2. Contribution clarity · 3. Identification / method ·
4. Robustness & inference · 5. Exhibits self-contained · 6. Exposition (magnitude up front)
· 7. Venue mechanics (page limit / anonymization / fee / cover letter) · 8. Data & code /
reproducibility · 9. Pre-empted referee objections.

**Go/no-go:** any FAIL on Fit, Identification, or Venue-mechanics is a no-go (the classic
desk-reject triggers).

### Decision contract

| Result | Meaning | Required next action |
|---|---|---|
| `GO` | No blocking FAIL and all venue mechanics are verified. | Run `rt-simulated-referee` for the substantive attack surface before submission. |
| `CONDITIONAL GO` | No fatal desk-reject trigger, but one or more FLAG items will draw reviewer pressure. | Fix or explicitly justify each FLAG; rerun this check on the changed sections. |
| `NO-GO` | Any FAIL on fit, identification/method, or venue mechanics, or an unverifiable required venue rule. | Route each blocking item to the owning target-pack skill and rerun before opening the portal. |

For `UNKNOWN`, name the missing evidence and the smallest artifact needed to resolve it. Do
not silently upgrade `UNKNOWN` to PASS.

### Hard rules

1. **Read the manuscript; cite locations** — no status without a §/table/page reference.
2. **Venue facts live from the source-map**, never from memory.
3. **No false green** — unverifiable dimension → `UNKNOWN`, not PASS.
4. **Map every FAIL/FLAG to the owning skill** (and its execution bridge) so the author
   knows exactly where to fix it.
5. **Separate mechanics from judgment** — this skill catches preventable desk-reject risk;
   use `rt-simulated-referee` for the substantive probability of surviving peer review.

### Output format

```
【Venue】… (bar: pack skills + source-map, read live)
【Scorecard】1 Fit … PASS/FLAG/FAIL — note (§ cited) · … (dims 2–9)
【Go / No-go】GO / NO-GO — deciding dimension(s)
【Blocking gaps (FAIL)】ranked; each with the fix + owning skill
【Will-be-pushed (FLAG)】referee-anticipation list
【Unknowns】missing evidence required before a green light
【Desk-reject risk】low / medium / high — why
```

Next: if readiness passes, `rt-simulated-referee` for the substantive adversarial review.
