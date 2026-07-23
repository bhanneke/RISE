<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/rt-simulated-referee.md -->

# `rt-simulated-referee`

Pre-submission peer-review rehearsal — a calibrated Associate Editor desk-screen plus 2-3 distinct-lens referees for the target venue, adversarially verified and synthesized into a report, decision band, and prioritized skill-mapped fix list.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Research-Toolkit-Skills/skills/rt-simulated-referee/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/rt-simulated-referee/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Research-Toolkit-Skills/skills/rt-simulated-referee/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Simulated Referee (rt-simulated-referee)

Run the substantive gauntlet before a real referee does. Full protocol + a worked example:
`shared-resources/submission-readiness/simulated-referee.md`.

### When to trigger

- After `rt-submission-readiness` clears the mechanical bar.
- When the author wants to know the decisive objection before submitting.

### Calibrate first (this is what makes it realistic)

Pull the venue's bar from the target pack, not generic intuition: acceptance/desk-reject
reality + mechanics from `resources/official-source-map.md`; what this venue's referees
attack from `*-referee-strategy` + the shared
`reviewer-objection-checklist`;
the fit/identification/robustness bar from the pack's skills. Set strictness to the
venue's selectivity.

### Protocol

1. **AE desk-screen** — fit, general interest, fatal flaws → desk-reject risk; stop if a clear desk reject.
2. **Independent referees** (distinct lenses: identification skeptic · contribution/fit ·
   robustness/reproducibility) each write a structured report.
3. **Adversarial verification** — every major concern must be **real + specific +
   addressable** or be downgraded.
4. **AE synthesis** — one decision band (reject / major / minor / lean-accept) + the 1–3
   decisive issues.
5. **Skill-mapped fix list** — each decisive issue → the pack skill (and its execution
   bridge) that fixes it.

### Orchestration

Spawn one subagent per role with the same manuscript + the calibrated venue bar; collect
independent reports; a final AE-synthesis agent. Distinct lenses + independence catch more
than a single read.

### Hard rules

1. **Calibrate from the pack + source-map**, never generic.
2. **Verify before reporting** (real / specific / addressable).
3. **Map every decisive issue to a skill + execution bridge.**
4. **It's a rehearsal** — output a decision *band* and the decisive issues, never a fake accept probability.

### Output format

```
【Venue】… (calibrated)
【Desk-screen】send out / desk reject — reason; risk low/med/high
【Decision band】reject / major / minor / lean-accept
【Decisive issues (1–3)】each with owning pack skill + concrete fix
【Author action plan】ordered; tie each to a skill + tool
```

Next: address the decisive issues, then `rt-response-to-referees` for a real R&R.
