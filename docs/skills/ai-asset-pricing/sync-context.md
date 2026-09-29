<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/sync-context.md -->

# `/sync-context`

Detects drift between the code and the agent documentation (docs/ai, AGENTS.md, CLAUDE.md) and proposes updates.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-24</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/sync-context/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/sync-context/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/sync-context/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Context Sync

Detect and fix documentation drift across the repo's AI context layer.

### Examples

- `/sync-context` — scan all mappings and propose updates
- `/sync-context pybondlab` — scan only PyBondLab-related mappings

### Hard Rules

- NEVER auto-commit doc updates. Always show the proposed edit and wait for approval.
- NEVER rewrite entire documents. Propose targeted, minimal edits only.
- Preserve the voice and judgment in existing docs — update facts, not opinions.
- If a doc references a file that no longer exists, flag it but do not remove without asking.
- Do not add new sections or restructure documents unless the drift requires it.

### Workflow

#### 1. Run Drift Detection

```bash
"<PYTHON>" tools/context_drift.py --json
```

Parse the JSON output. Each entry has: `source` (glob), `doc` (file path), `days_stale` (float).

If `$ARGUMENTS` contains a keyword (e.g., `pybondlab`), filter to entries where
either `source` or `doc` contains that keyword. Otherwise process all entries.

#### 2. For Each Stale Mapping

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

#### 3. Summary

After processing all mappings, print a summary table:

```
| Doc                    | Status   | Action                                    |
|------------------------|----------|-------------------------------------------|
| docs/ai/onboarding.md  | Updated  | bootstrap.py uv changes reflected         |
| docs/ai/pybondlab.md   | Current  | no drift detected                         |
| AGENTS.md              | Skipped  | user declined update                      |
```

#### 4. Post-Sync

If any edits were applied, suggest committing with:

```
Sync context: update [list of docs] to reflect recent code changes
```

Do not commit automatically.
