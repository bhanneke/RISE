<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/freeze.md -->

# `freeze`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../clo-author/">Clo-Author skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>none declared</code></div><div><b>Updated:</b> 2026-05-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/freeze/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/clo-author/freeze/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hugosantanna/clo-author" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Freeze -- Session-Scoped Edit Guard

Blocks Write and Edit operations on files outside the specified directories. Use when reviewing code (freeze everything except notes), when writing (freeze scripts), or when editing data pipelines (freeze paper/).

### Usage

```
/freeze paper/          # Only allow edits in paper/
/freeze scripts/ data/  # Only allow edits in scripts/ and data/
/freeze off             # Deactivate all freeze guards
```

### How It Works

1. Parse the directory arguments from the user's input
2. Write the guard configuration to `.claude/state/session-guards.json`
3. The `session-guard` PreToolUse hook reads this file and blocks Edit/Write operations on files outside the allowed directories
4. Report what's frozen and what's editable

### Activation

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

### Deactivation

When the user invokes `/freeze off`:

1. Read `.claude/state/session-guards.json`
2. Set `freeze.active` to `false`
3. Confirm: "Freeze deactivated. All paths editable."

### Gotchas

- Freeze is session-scoped -- it resets when the conversation ends
- The guard file persists on disk but the hook checks a session flag
- `.claude/` is always editable (can't freeze yourself out of config changes)
- Paths are relative to the project root
