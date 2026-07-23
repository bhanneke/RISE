<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/rt-replication-package.md -->

# `rt-replication-package`

Assembles and validates the Data-Editor replication package against the target venue's data-and-code policy — master script, pinned environment, README/roadmap, restricted-data plan, script-to-exhibit output map, and a Data-Editor-grade checklist.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code> · <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Research-Toolkit-Skills/skills/rt-replication-package/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/rt-replication-package/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Research-Toolkit-Skills/skills/rt-replication-package/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Replication Package (rt-replication-package)

The step that now blocks acceptance at the top (AEA / JF / Management Science Data Editors
re-run your code and check every number). Full manifest + validation checklist:
`shared-resources/empirical-methods/replication-package.md`.

### When to trigger

- Approaching final submission, or a conditional accept with a data-and-code requirement.
- A Data Editor / verification service needs the package.

### What it does

1. **Read the venue policy** from the target pack's `resources/official-source-map.md`
   (code at submission vs. acceptance? Data Editor? AsCollected page? restricted-data rule?
   hosting?). **Match it exactly.**
2. **Assemble the manifest**: master script (raw → all exhibits), ordered steps
   (clean → construct → estimate → robustness → tables), pinned environment, README/roadmap,
   data (or pseudo/synthetic data for restricted access + access instructions), the
   script→exhibit output map, and the disclosure statement.
3. **Validate** with the checklist: runs clean end-to-end on a fresh machine; every reported
   number reproduced (body + appendix); seeded/deterministic; restricted-data plan; output
   map complete; venue policy satisfied.

### Hard rules

1. **Every reported number traces to a script step** (body and appendix).
2. **Deterministic** — pin versions, seed RNGs.
3. **Restricted data → pseudo/synthetic data + access instructions**, never confidential data committed.
4. **Match the venue's exact policy** from the source-map; re-verify before submission.
5. **Keep it in sync with the execution bridge** — when a revision re-runs an estimate,
   regenerate the affected outputs.

### Output format

```
【Venue policy】(code timing, Data Editor, restricted-data rule, hosting)
【Manifest】master · steps · env · README · data · output-map · disclosure — status each
【Validation】end-to-end ✓/✗ · all numbers reproduced ✓/✗ · seeded ✓/✗ · restricted-data plan ✓/✗
【Blocking gaps】what would fail a Data-Editor check, ranked
【Ready?】GO / NOT-YET — deciding items
```

### Anti-patterns

- "Works on my machine" (absolute paths, unpinned versions, manual steps); reported numbers
  the script doesn't reproduce; committing confidential data; leaving assembly to post-accept crunch.
