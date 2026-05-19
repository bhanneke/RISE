<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/revise.md -->

# `revise`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

---
name: revise
description: R&R cycle — classify referee comments and route to appropriate agents. Replaces /respond-to-referee.
argument-hint: "[referee-report file path] [paper path (optional)]"
allowed-tools: Read,Grep,Glob,Write,Edit,Task
---

# Revise

Structure point-by-point referee responses with classification, agent routing per revision protocol, and diplomatic drafting.

**Input:** `$ARGUMENTS` — path to referee report file(s), optionally followed by paper path.

---

## Workflow

### Step 1: Parse Inputs
1. Read referee report(s) from `$ARGUMENTS`
2. Read the paper (paper/main.tex or specified path)
3. Read revision protocol from rules
4. Read existing scripts to know what analyses already exist

### Step 2: Classify Every Comment

| Class | Routing | Action |
|-------|---------|--------|
| **NEW ANALYSIS** | → Coder agent | Flag for user, create analysis task |
| **CLARIFICATION** | → Writer agent | Draft rewritten section |
| **REWRITE** | → Writer agent | Draft structural revision |
| **DISAGREE** | → User (mandatory) | Draft diplomatic pushback, flag for review |
| **MINOR** | → Writer agent | Draft fix directly |

### Step 3: Build Tracking Document
Save to `quality_reports/referee_response_tracker.md` with:
- Summary counts per referee
- Action items by priority (HIGH: new analysis, MEDIUM: clarification, FLAGGED: disagreements, LOW: minor)

### Step 4: Dispatch Agents
- CLARIFICATION/REWRITE → dispatch Writer with specific instructions
- NEW ANALYSIS → flag for user approval before dispatching Coder
- DISAGREE → draft diplomatic response, flag prominently for user

### Step 5: Draft Response Letter
Generate LaTeX response letter with:
- Summary of major changes
- Point-by-point responses with exact referee quotes
- Color-coded responses
- Page/section references for each change

### Step 6: Diplomatic Disagreement Protocol
When DISAGREE: open with acknowledgment, provide evidence, offer partial concession, NEVER say "the referee is wrong." FLAG for user review.

### Step 7: Save Outputs
1. Tracker: `quality_reports/referee_response_tracker.md`
2. Response letter: `quality_reports/referee_response_[journal]_[date].tex`
3. Revised sections: `paper/sections/` (for CLARIFICATION/REWRITE items)

---

## Bundled Resources (Level 3)

| Resource | Path | When |
|----------|------|------|
| Response tracker | `templates/response-tracker.md` | Step 3 — tracking document |
| Response letter | `templates/response-letter.tex` | Step 5 — LaTeX boilerplate |
| Diplomatic disagreement | `templates/diplomatic-disagreement.md` | Step 6 — DISAGREE phrasing |
| Gotchas | `gotchas.md` | Always — known failure points |

---

## Principles
- **The response letter is the user's voice.** Match their tone.
- **Never fabricate results.** Mark NEW ANALYSIS items as TBD.
- **Flag all DISAGREE items.** These need human judgment.
- **Track everything.** Every comment appears in both tracker and response letter.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/revise/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>hugosantanna/clo-author</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../clo-author.md">Clo-Author skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>none declared</dd>
<dt><b>Last update</b></dt><dd>2026-05-11</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/hugosantanna/clo-author">⭐ hugosantanna/clo-author</a><br><img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/hugosantanna/clo-author" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/clo-author/revise/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/clo-author.yml">edit on GitHub</a>.</p>
</div>

</div>
