<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/rt-journal-match.md -->

# `rt-journal-match`

Answers "which journal should I send this to?" — profiles the paper, shortlists candidate venues across 185+ packs, and ranks them into reach/match/safe with a resubmission ladder, reading live venue facts from each pack's source-map.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>submission</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Research-Toolkit-Skills/skills/rt-journal-match/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/rt-journal-match/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Research-Toolkit-Skills/skills/rt-journal-match/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Journal-Match (rt-journal-match)

The missing front-door question — *which venue?* — across the whole repository. Full
methodology + the stable venue index live in
`shared-resources/journal-selection/journal-match.md`
and `venue-index.tsv`.

### When to trigger

- The author has a result/draft and no settled target.
- A paper was rejected and needs the best next venue.
- A "not a fit" signal means the scope/venue needs rethinking.

### What it does

1. **Profile the paper** — discipline + subfield, method/design, contribution type,
   setting/data/region, ambition (be honest).
2. **Shortlist** from `venue-index.tsv` by discipline / lane / region (long-tail venues →
   the discipline breadth bundle).
3. **Score** each candidate on **Fit × acceptance-odds × turnaround × cost/policy ×
   audience**, reading the live facts from each candidate's `resources/official-source-map.md`.
4. **Return reach / match / safe** (≈2–3 each) with one-line rationales + the live facts,
   then a **submit order and resubmission ladder**.

### Hard rules

- **Live facts from the source-map, never from memory** (fees, acceptance, turnaround, page
  limits, data policy).
- **Fit judgment defers** to the venue's `*-topic-selection` / `*-contribution-framing`.
- **Be honest about odds**; don't inflate a paper into a reach it can't clear.
- **Coverage honesty**: if a plausible venue is outside the index and its bundle, say so.

### Output format

```
【Paper profile】discipline / method / contribution / setting / ambition
【Reach】V — why; key live facts (desk-reject, turnaround, fee)
【Match】V — …
【Safe】V — …
【Submit order & ladder】V_top → if reject → V_next (what to change) → …
【Open questions】facts to re-verify in the source-map before submitting
```

### Anti-patterns

- Recommending only reaches (wastes the timeline) or only safes (undersells the paper).
- Ignoring `lane` — sending a qualitative/theory paper to an empirical-only venue.
- Treating the `tier` column as a precise ranking (it is an indicative bucket).

Next: once a target is chosen, `rt-execution-bridge` to run the analysis and
`rt-submission-readiness` to check the bar.
