---
name: context-status
description: |
  Show current context status and session health.
  Use to check how much context has been used, whether auto-compact is
  approaching, and what state will be preserved.
allowed-tools: ["Read", "Bash", "Glob"]
disallowed-tools: ["Edit", "MultiEdit"]
metadata:
  author: Claude Code Academic Workflow
  version: 1.0.0
---

# /context-status — Check Session Health

Show the current session status including context usage estimate, active plan,
and preservation state.

## What This Skill Shows

1. **Context usage estimate** — Approximate % of context window used
2. **Active plan** — Current plan file and status
3. **Session log** — Most recent session log
4. **Preservation state** — What will survive compaction

## Workflow

### Step 1: Check the Context Estimate

The context-monitor hook writes its estimate to `context-pct.txt` (and its counters and threshold flags to `context-monitor-cache.json`) in this project's session directory:

```bash
d=~/.claude/sessions/$(printf '%s' "${CLAUDE_PROJECT_DIR:-$PWD}" | python3 -c 'import sys,hashlib;print(hashlib.md5(sys.stdin.read().encode()).hexdigest()[:8])')
cat "$d/context-pct.txt" 2>/dev/null; cat "$d/context-monitor-cache.json" 2>/dev/null | head -20
```

### Step 2: Find Active Plan

```bash
ls -lt quality_reports/plans/*.md 2>/dev/null | head -3
```

### Step 3: Find Session Log

```bash
ls -lt quality_reports/session_logs/*.md 2>/dev/null | head -1
```

### Step 4: Report Status

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

## Notes

- Context % comes from Claude Code's own `context_window.used_percentage` where the status line shows it; the hook's `context-pct.txt` holds an estimate from transcript size (falling back to a tool-call count). The built-in `/context` shows exact usage
- Actual compaction is triggered by Claude Code automatically
- All important state is saved to disk (plans, logs, MEMORY.md)
