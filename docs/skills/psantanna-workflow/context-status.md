<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/context-status.md -->

# `/context-status`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/context-status/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/context-status/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/context-status/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## /context-status — Check Session Health

Show the current session status including context usage estimate, active plan,
and preservation state.

### What This Skill Shows

1. **Context usage estimate** — Approximate % of context window used
2. **Active plan** — Current plan file and status
3. **Session log** — Most recent session log
4. **Preservation state** — What will survive compaction

### Workflow

#### Step 1: Check the Context Estimate

The context-monitor hook writes its estimate to `context-pct.txt` (and its counters and threshold flags to `context-monitor-cache.json`) in this project's session directory:

```bash
d=~/.claude/sessions/$(printf '%s' "${CLAUDE_PROJECT_DIR:-$PWD}" | python3 -c 'import sys,hashlib;print(hashlib.md5(sys.stdin.read().encode()).hexdigest()[:8])')
cat "$d/context-pct.txt" 2>/dev/null; cat "$d/context-monitor-cache.json" 2>/dev/null | head -20
```

#### Step 2: Find Active Plan

```bash
ls -lt quality_reports/plans/*.md 2>/dev/null | head -3
```

#### Step 3: Find Session Log

```bash
ls -lt quality_reports/session_logs/*.md 2>/dev/null | head -1
```

#### Step 4: Report Status

Format the output:

```
📊 Session Status
─────────────────────────────────
Context Usage:  ~XX% (estimated)
Auto-compact:   [approaching | not imminent]

📋 Active Plan
File:   quality_reports/plans/YYYY-MM-DD_description.md
Status: [draft | approved | in_progress | completed]
Task:   [current unchecked task or "none"]

📝 Session Log
File:   quality_reports/session_logs/YYYY-MM-DD_description.md

✓ Preservation Check
  • Pre-compact hook: [configured | missing]
  • Post-compact restore: [configured | missing]
  • Session state will be saved before compaction
```

### Notes

- Context % comes from Claude Code's own `context_window.used_percentage` where the status line shows it; the hook's `context-pct.txt` holds an estimate from transcript size (falling back to a tool-call count). The built-in `/context` shows exact usage
- Actual compaction is triggered by Claude Code automatically
- All important state is saved to disk (plans, logs, MEMORY.md)
