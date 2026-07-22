<!-- DO NOT EDIT — auto-copied from skills/theorist-toolbox/details/co-math-status.md -->

# `/co-math-status`

Renders a compact status view of a co-math project — goals, active workstreams, blocked items, pending reviews, recent decisions — as an ASCII diagram.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../theorist-toolbox/">Theorist Toolbox</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/morankor/theorist-toolbox/contents/skills/co-math-status/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/theorist-toolbox/co-math-status/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/morankor/theorist-toolbox/blob/main/skills/co-math-status/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/morankor/theorist-toolbox?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

> **Author:** Moran Koren, Ben-Gurion University of the Negev (korenmor@bgu.ac.il). Part of the [Theorist Toolbox](https://github.com/morankor/theorist-toolbox).


## co-math-status

Render a compact, human-readable status view of the current AI co-mathematician project.

### When to invoke

- `/co-math-status`
- "show project status"
- "what's the state of this project"
- "what's blocked"
- "which workstreams are running"

### What it does

Runs `python3 ~/.claude/co-math/tools/render_status.py` from the current directory. The script walks up from the cwd to find a `co-math-config.json`; if there is no co-math project in the ancestry, it prints "not inside a co-math project" and exits cleanly.

When inside a project, the output looks like:

```
Project: ambidextrous-sofa
Created: 2026-05-10  |  Strict mode: ON  |  Paper format: latex

Research question:
  Prove an upper bound on the ambidextrous sofa problem area.

Goals (approved: YES)
  G1 Literature review of prior sofa bounds
  G2 Computational framework for branch-and-bound search
  G3 Execute the search

Workstreams                         status      agent              last update
  W001-prior-bounds          [G1]   COMPLETE    literature-reviewer 2026-05-10
  W002-comp-framework        [G2]   RUNNING     coder              2026-05-11
  W003-pruning-heuristic     [G2]   BLOCKED     prover             2026-05-12  <-- needs attention
  W004-search                [G3]   PLANNED     -                  -

Pending reviews
  W002-comp-framework  -- in review by paper-reviewer (round 1)

Open obligations in paper.tex
  3 \unproven blocks (see appendix A)

Recent decisions (last 3)
  2026-05-12  Pruning heuristic blocked; user steering needed (per W003 report.md)
  2026-05-11  Approved goals G1-G3
  2026-05-10  Project initialized

Failed explorations: 1 (see failed-explorations/)
```

### Output

Output is printed directly. The script does not modify any files. After printing, **briefly summarise** the most important item for the user — typically "X workstreams running, Y blocked" — rather than re-explaining what the user just saw.

### When to do more than render

If the user follows up with "open the blocked workstream" or "show me W003's log", read the relevant file with the Read tool and surface the contents.
