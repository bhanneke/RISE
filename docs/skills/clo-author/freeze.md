<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/freeze.md -->

# `freeze`



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
name: freeze
description: Block edits outside specified directories for this session. Protects files from accidental changes during focused work. Activate with /freeze [dirs], deactivate with /freeze off.
user-invocable: true
---

# Freeze -- Session-Scoped Edit Guard

Blocks Write and Edit operations on files outside the specified directories. Use when reviewing code (freeze everything except notes), when writing (freeze scripts), or when editing data pipelines (freeze paper/).

## Usage

```
/freeze paper/          # Only allow edits in paper/
/freeze scripts/ data/  # Only allow edits in scripts/ and data/
/freeze off             # Deactivate all freeze guards
```

## How It Works

1. Parse the directory arguments from the user's input
2. Write the guard configuration to `.claude/state/session-guards.json`
3. The `session-guard` PreToolUse hook reads this file and blocks Edit/Write operations on files outside the allowed directories
4. Report what's frozen and what's editable

## Activation

When the user invokes `/freeze [dirs]`:

1. Read the current `.claude/state/session-guards.json` (create if it doesn't exist)
2. Set the `freeze` guard:
```json
{
  "freeze": {
    "active": true,
    "allowed_paths": ["paper/", "scripts/"],
    "activated_at": "2026-05-09T14:30:00",
    "reason": "User invoked /freeze"
  }
}
```
3. Confirm: "Freeze active. Edits allowed only in: [dirs]. Run `/freeze off` to deactivate."

## Deactivation

When the user invokes `/freeze off`:

1. Read `.claude/state/session-guards.json`
2. Set `freeze.active` to `false`
3. Confirm: "Freeze deactivated. All paths editable."

## Gotchas

- Freeze is session-scoped -- it resets when the conversation ends
- The guard file persists on disk but the hook checks a session flag
- `.claude/` is always editable (can't freeze yourself out of config changes)
- Paths are relative to the project root


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/freeze/ --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/clo-author/freeze/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/clo-author.yml">edit on GitHub</a>.</p>
</div>

</div>
