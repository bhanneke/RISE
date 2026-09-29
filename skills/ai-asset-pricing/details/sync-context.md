---
name: sync-context
description: "Detect documentation drift and propose updates to docs/ai/, AGENTS.md, and CLAUDE.md. Use when session-start warnings flag stale docs, after significant code changes, or periodically to keep context current."
---

# Context Sync

Detect and fix documentation drift across the repo's AI context layer.

## Examples

- `/sync-context` — scan all mappings and propose updates
- `/sync-context pybondlab` — scan only PyBondLab-related mappings

## Hard Rules

- NEVER auto-commit doc updates. Always show the proposed edit and wait for approval.
- NEVER rewrite entire documents. Propose targeted, minimal edits only.
- Preserve the voice and judgment in existing docs — update facts, not opinions.
- If a doc references a file that no longer exists, flag it but do not remove without asking.
- Do not add new sections or restructure documents unless the drift requires it.

## Workflow

### 1. Run Drift Detection

```bash
"<PYTHON>" tools/context_drift.py --json
```

Parse the JSON output. Each entry has: `source` (glob), `doc` (file path), `days_stale` (float).

If `$ARGUMENTS` contains a keyword (e.g., `pybondlab`), filter to entries where
either `source` or `doc` contains that keyword. Otherwise process all entries.

### 2. For Each Stale Mapping

For each drift warning, in order:

1. **Read the current doc** using the Read tool.

2. **Identify what changed** in the source since the doc was last updated:
   ```bash
   git log --oneline --since="<days_stale> days ago" -- <source_files>
   ```
   Then read the relevant source files to understand the current state.

3. **Compare** what the doc says against the current source state. Identify
   specific lines in the doc that are now inaccurate, incomplete, or misleading.

4. **Propose a targeted edit** — show the old text and the proposed replacement.
   Use the Edit tool format (old_string → new_string). Explain the reason for
   each change in one sentence.

5. **Wait for user approval** before applying each edit.

### 3. Summary

After processing all mappings, print a summary table:

```
| Doc                    | Status   | Action                                    |
|------------------------|----------|-------------------------------------------|
| docs/ai/onboarding.md  | Updated  | bootstrap.py uv changes reflected         |
| docs/ai/pybondlab.md   | Current  | no drift detected                         |
| AGENTS.md              | Skipped  | user declined update                      |
```

### 4. Post-Sync

If any edits were applied, suggest committing with:

```
Sync context: update [list of docs] to reflect recent code changes
```

Do not commit automatically.
