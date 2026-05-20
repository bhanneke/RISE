<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/careful.md -->

# `careful`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../clo-author/">Clo-Author skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>none declared</code></div><div><b>Updated:</b> 2026-05-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/careful/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/clo-author/careful/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/hugosantanna/clo-author" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Careful -- Session-Scoped Destructive Command Guard

Blocks Bash commands matching destructive patterns. Use when working on critical branches, before a deadline, or whenever you want an extra safety net.

### Usage

```
/careful       # Activate destructive command blocking
/careful off   # Deactivate
```

### Blocked Patterns

When active, the following Bash command patterns are blocked:

| Pattern | What It Catches |
|---------|----------------|
| `rm -rf` | Recursive force delete |
| `rm -r` without explicit path | Broad recursive delete |
| `git reset --hard` | Discard all uncommitted changes |
| `git push --force` | Force push (overwrites remote history) |
| `git push -f` | Same |
| `git clean -f` | Delete untracked files |
| `git checkout -- .` | Discard all working tree changes |
| `git branch -D` | Force delete branch |
| `DROP TABLE` | SQL table deletion |
| `DROP DATABASE` | SQL database deletion |
| `> /dev/null` at start | Overwriting with null |
| `chmod 777` | Overly permissive permissions |

### Activation

When the user invokes `/careful`:

1. Read `.claude/state/session-guards.json` (create if needed)
2. Set the `careful` guard:
```json
{
  "careful": {
    "active": true,
    "activated_at": "2026-05-09T14:30:00",
    "reason": "User invoked /careful"
  }
}
```
3. Confirm: "Careful mode active. Destructive bash commands are blocked. Run `/careful off` to deactivate."

### Deactivation

When `/careful off`:
1. Set `careful.active` to `false`
2. Confirm: "Careful mode deactivated."

### Gotchas

- Session-scoped -- resets when conversation ends
- Only blocks Bash tool calls -- doesn't affect user's terminal
- Can be overridden if the user explicitly approves the blocked command
- `rm` without `-rf` is still allowed (single file deletion)
