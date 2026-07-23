<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/rt-response-to-referees.md -->

# `rt-response-to-referees`

Turns a referee report into a point-by-point response letter plus revision plan — editor first, every comment answered, each empirical fix backed by a real re-run via the target pack's skill and the execution bridge.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>revision</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Research-Toolkit-Skills/skills/rt-response-to-referees/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/rt-response-to-referees/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Research-Toolkit-Skills/skills/rt-response-to-referees/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Response-to-Referees (rt-response-to-referees)

Draft the reply that decides the second round. Full method:
`shared-resources/submission-readiness/response-to-referees.md`.

### When to trigger

- An R&R letter has arrived and needs a point-by-point response + revision.
- You want to convert `rt-simulated-referee` output into a rehearsed reply.

### What it does

1. **Inventory every comment** (per referee + AE), tag major/minor, substantive/clarification.
2. **Editor first** — lead with the AE's decisive concerns.
3. **Classify each response** honestly: concede & fix / address partially / push back with
   evidence (rarely, and only when right).
4. **Back substantive fixes with a real re-run** — map each empirical comment to the pack
   skill + `rt-execution-bridge`; the number in the reply must be one you actually computed.
5. **Write the letter** — quote each comment, respond beneath it, point to the exact change.
6. **Summarize the changes** in a scannable table.

### Hard rules

1. **Editor first**, then referees.
2. **Every claimed fix corresponds to a real change/re-run**; empirical claims cite a number
   produced via the execution bridge.
3. **Answer every comment** — none silently dropped.
4. **Venue response format from the pack + source-map** (some cap length / want a structure).
5. It drafts a *reply*; the author owns final scientific sign-off.

### Output format

```
【Cover note to editor】how the decisive concerns were addressed
【Referee 1】R1.1 (quote) → concede&fix / partial / push-back · what changed · where · new number
【Referee 2】… 【AE】(decisive points first)
【Summary of changes】comment → change → location
【Open/declined】comments not fully addressed, with the honest reason
```

### Anti-patterns

- Silent omission; defensive tone / blanket push-back; "we addressed this" with no real
  edit; burying the AE's load-bearing concern.

Next: regenerate affected outputs in `rt-replication-package` so the package matches the revision.
