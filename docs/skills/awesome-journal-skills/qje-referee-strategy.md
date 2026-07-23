<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/qje-referee-strategy.md -->

# `qje-referee-strategy`

War-games likely referee objections before submitting, to close gaps pre-emptively given QJE's ~2-week desk screen and ~1-4% acceptance rate; anticipates reports rather than writing the post-decision response.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Quarterly-Journal-of-Economics-Skills/skills/qje-referee-strategy/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/qje-referee-strategy/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Quarterly-Journal-of-Economics-Skills/skills/qje-referee-strategy/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Referee Strategy (qje-referee-strategy)

### When to trigger

- The paper is nearly submission-ready and you want to stress-test it adversarially
- You suspect a specific weakness a referee will seize on
- You are choosing what to put in the body vs. the appendix to forestall objections
- You want to draft suggested/excluded referees and a strategic cover note

### The QJE refereeing reality

QJE is **the fastest top-5 journal at desk** — its five Harvard-based Editors desk-decide in roughly **two weeks** and desk-reject a clear majority (commonly cited around 60%+), with an unconditional acceptance rate of only **~1-4%**. Review is **double-blind**, so you cannot tailor to a known referee; you must satisfy *the toughest plausible expert*. Two consequences: (1) the paper has to survive a fast, skim-level editor screen before any referee sees it, so the big idea and clean identification must be visible up front; (2) for papers that survive, QJE grants few rounds with demanding referees, so you usually get *one* substantive shot. Anticipate the report you would write if you were the toughest expert in your subfield, and answer it in advance.

### Map the three referee archetypes

| Referee type        | What they attack                                          | Pre-empt by...                                            |
|---------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| The identification hawk | The exogeneity claim; pre-trends; exclusion restriction | Falsification + placebo evidence in the body (see qje-identification) |
| The "so what?" skeptic  | Generality; whether the answer matters to all of econ   | A crisp broad-lesson + magnitude benchmarking (qje-topic-selection) |
| The mechanism doubter   | Whether the proposed channel is the real one            | A testable prediction confirmed in data (qje-theory-model) |

### War-gaming protocol

1. **Pass the desk screen first.** Before refereeing even starts, ask: in two pages, is the big question and the clean source of variation obvious? If not, the editor desk-rejects in ~2 weeks regardless of how good the appendix is.
2. **Write the hostile report.** In 5–8 bullets, list the strongest objections a top expert would raise. Be ruthless; this is cheaper now than after a rejection.
3. **Triage.** For each: is it a *fundamental* threat (kills the claim) or a *robustness* request (adds a table)? Fundamentals must be resolved before submission, not deferred to R&R.
4. **Locate the answer.** For each objection, point to where in the paper it is already answered. If nowhere, add it (body for fundamentals, appendix for robustness).
5. **Decide the framing.** Pre-empt the biggest objection explicitly in the text ("A natural concern is X; we address it in three ways ..."). Showing you saw it coming builds referee trust.

### Cover-letter / referee suggestions

- Suggest referees who are expert and fair; avoid close collaborators and advisors (conflicts), consistent with the AEA disclosure norms QJE follows.
- Note genuine conflicts to exclude, briefly and professionally.
- Keep any cover note short: the question, the design, the headline result, and fit for a general-interest journal — the editor reading it has ~2 weeks and many submissions.

### Checklist

- [ ] The two-page editor-skim test passes (big idea + clean variation visible early)
- [ ] A written hostile report exists with the 5–8 strongest objections
- [ ] Every fundamental threat is resolved in the body before submission
- [ ] Each robustness objection has a pre-emptive appendix answer
- [ ] The single biggest concern is addressed explicitly and early in the text
- [ ] Magnitudes benchmarked so the "so what?" referee is satisfied
- [ ] Suggested referees are expert, fair, and conflict-free

### Anti-patterns

- Submitting with a known fundamental hole, hoping referees miss it (the editor desk-screen catches a lot first)
- Deferring identification fixes to "future R&R" — at ~1-4% acceptance, QJE may not grant the round
- Ignoring the obvious objection rather than naming and answering it
- Suggesting collaborators/friends as referees (signals naivety or conflict)
- A long, defensive cover letter that argues instead of stating the contribution

### Output format

```
【Desk-screen test】big idea + variation visible in 2 pages? [Y/N]
【Hostile report】[5–8 strongest objections]
【Fundamentals】[threats that must be fixed pre-submission] — status each
【Robustness asks】[appendix answers] — status each
【Pre-empted in text】the biggest concern, addressed where: ...
【Referee suggestions】[expert, fair, conflict-free]
【Next step】qje-submission
```
