<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/revise.md -->

# `revise`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../clo-author/">Clo-Author skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>none declared</code></div><div><b>Updated:</b> 2026-05-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/revise/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/clo-author/revise/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hugosantanna/clo-author" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Revise

Structure point-by-point referee responses with classification, agent routing per revision protocol, and diplomatic drafting.

**Input:** `$ARGUMENTS` — path to referee report file(s), optionally followed by paper path.

---

### Workflow

#### Step 1: Parse Inputs
1. Read referee report(s) from `$ARGUMENTS`
2. Read the paper (paper/main.tex or specified path)
3. Read revision protocol from rules
4. Read existing scripts to know what analyses already exist

#### Step 2: Classify Every Comment

| Class | Routing | Action |
|-------|---------|--------|
| **NEW ANALYSIS** | → Coder agent | Flag for user, create analysis task |
| **CLARIFICATION** | → Writer agent | Draft rewritten section |
| **REWRITE** | → Writer agent | Draft structural revision |
| **DISAGREE** | → User (mandatory) | Draft diplomatic pushback, flag for review |
| **MINOR** | → Writer agent | Draft fix directly |

#### Step 3: Build Tracking Document
Save to `quality_reports/referee_response_tracker.md` with:
- Summary counts per referee
- Action items by priority (HIGH: new analysis, MEDIUM: clarification, FLAGGED: disagreements, LOW: minor)

#### Step 4: Dispatch Agents
- CLARIFICATION/REWRITE → dispatch Writer with specific instructions
- NEW ANALYSIS → flag for user approval before dispatching Coder
- DISAGREE → draft diplomatic response, flag prominently for user

#### Step 5: Draft Response Letter
Generate LaTeX response letter with:
- Summary of major changes
- Point-by-point responses with exact referee quotes
- Color-coded responses
- Page/section references for each change

#### Step 6: Diplomatic Disagreement Protocol
When DISAGREE: open with acknowledgment, provide evidence, offer partial concession, NEVER say "the referee is wrong." FLAG for user review.

#### Step 7: Save Outputs
1. Tracker: `quality_reports/referee_response_tracker.md`
2. Response letter: `quality_reports/referee_response_[journal]_[date].tex`
3. Revised sections: `paper/sections/` (for CLARIFICATION/REWRITE items)

---

### Bundled Resources (Level 3)

| Resource | Path | When |
|----------|------|------|
| Response tracker | `templates/response-tracker.md` | Step 3 — tracking document |
| Response letter | `templates/response-letter.tex` | Step 5 — LaTeX boilerplate |
| Diplomatic disagreement | `templates/diplomatic-disagreement.md` | Step 6 — DISAGREE phrasing |
| Gotchas | `gotchas.md` | Always — known failure points |

---

### Principles
- **The response letter is the user's voice.** Match their tone.
- **Never fabricate results.** Mark NEW ANALYSIS items as TBD.
- **Flag all DISAGREE items.** These need human judgment.
- **Track everything.** Every comment appears in both tracker and response letter.
