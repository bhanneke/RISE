<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/careful.md -->

# `careful`



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
name: careful
description: Block destructive bash commands for this session. Prevents rm -rf, git reset --hard, git push --force, and similar dangerous operations. Activate with /careful, deactivate with /careful off.
user-invocable: true
---

# Careful -- Session-Scoped Destructive Command Guard

Blocks Bash commands matching destructive patterns. Use when working on critical branches, before a deadline, or whenever you want an extra safety net.

## Usage

```
/careful       # Activate destructive command blocking
/careful off   # Deactivate
```

## Blocked Patterns

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

## Activation

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

## Deactivation

When `/careful off`:
1. Set `careful.active` to `false`
2. Confirm: "Careful mode deactivated."

## Gotchas

- Session-scoped -- resets when conversation ends
- Only blocks Bash tool calls -- doesn't affect user's terminal
- Can be overridden if the user explicitly approves the blocked command
- `rm` without `-rf` is still allowed (single file deletion)


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/careful/ --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/clo-author/careful/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/clo-author.yml">edit on GitHub</a>.</p>
</div>

</div>
