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
