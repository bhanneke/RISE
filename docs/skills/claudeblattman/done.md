<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/done.md -->

# `/done`

Mark work complete + update tracking

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

# Session Capture

*v2.4.2 — Patch 0: structured cost-logging format for Step 6's performance log line — `mode:MODE session:SESSION files:FILES rule:RULE [optional description]` — so post-hoc cost analysis can group runs without parsing free-text NOTES. Patch 1 (private only): Step 0.5 Python extracted to a helper script; the public version keeps the Python inline.*
*v2.4.1 — OSC-0 terminal-title escape wrapped in a brace-group `{ ... } 2>/dev/null` instead of `>/dev/tty 2>/dev/null`. The plain pattern leaks the open-error past `2>/dev/null` when the bash subprocess has no controlling terminal (any harness-spawned subshell), producing visible "device not configured: /dev/tty" noise. Brace-group silences it cleanly.*
*v2.4 — Step 4's natural-language pruning logic is replaced with a single Bash call to a deterministic prune helper script. Closes the silent-skip gap where Brief / auto-quick runs let the model bypass pruning. Adds tiered cutoffs (>10k lines → 7d, >6k → 14d, >3k → 30d, >1.5k → 60d) so pruning actually fires under high-volume workflows. Background: the session log had drifted from ~3,000 to ~9,700 lines because /done's auto-quick path was implicitly treating Step 4 as skippable. Calling a single script replaces "the model decides whether to prune" with "the harness runs the prune unconditionally."*
*v2.3 — Step 6 summary emits an OSC-0 terminal-title escape via `/dev/tty` after the captured-confirmation block. Editor tab title becomes `[<task-short>] done` (or `[no-anchor] done` for unanchored sessions). Phase 0 of a multi-terminal collision fix. Reaches the terminal via `/dev/tty` (controlling terminal); silent no-op when unavailable.*
*v2.2 — Routing-audit row gains `state_set_by_user` and `state_set_on_hostname` columns (sourced from `active-subproject.json`). Step 0.5 forwards them; Step 5a routing-audit echo includes them. Schema bumps from 8-field to 10-field; readers tolerant of 7/8/10 by positional parse. Pure additive — no routing-logic change. Diagnostic for multi-terminal collision diagnosis.*
*v2.1 — Rule 2 divergence guard. The guard tokenizes state.task_name + session topic, drops stopwords, and falls through to Step 5a.5 if the token intersection is empty — preserving the state folder's HANDOFF and surfacing a breadcrumb to the user. Audit label for the divergent case is `2-fresh-state-divergent` (distinct from `2-fresh-state`) so telemetry can measure how often the guard fires. Routing-audit CSV gains a trailing `hostname` field; readers tolerate 7-field and 8-field rows.*
*v2.0 — Routing rewritten to CWD-precedence. Core change: Step 5a checks whether CWD is inside a HANDOFF-bearing sub-folder BEFORE consulting `active-subproject.json`. This prevents stale state from a prior session (`/start-task` set to folder A, current CWD under folder B with its own HANDOFF.md) from misrouting handoffs. State-file freshness check switched from a 14-day `set_at` field (which can be LLM-fabricated) to a 24-hour filesystem mtime (can't be faked). Routing-audit CSV at `~/.claude-assistant/logs/routing-audit.csv` captures each decision for telemetry.*
*v1.12 — Step 5a.5 made non-destructive. When no `active-subproject.json` is set, `/done` NO LONGER overwrites a project-root `HANDOFF.md`. Instead it appends a dated entry to a project-root `SESSION_LOG.md` (creates if needed) and falls through to Step 5b's global handoff. Scoped project-root HANDOFF.md requires explicit `/start-task`. All scoped writes (HANDOFF.md, SESSION_LOG.md entries) gain hostname+timestamp metadata via an atomic-write helper.*
*v1.11 — Atomic-write discipline added. All writes to session-log.md, HANDOFF.md, SESSION_LOG.md, handoff.md, watch-list.md, and skill-performance.csv MUST route through the atomic-write helper (tmp-file + `os.replace()`). Prevents corruption from sync race conditions and process interruption.*
*v1.10 — Step 2.7 body extracted to a separate reference and now runs ONLY on `retro` flag. Steps 0.5/3.5/5a/5a.5 CWD walks consolidated into a single Step 0.5 pass — downstream steps reuse cached values. Quick-default added for Brief sessions. 40-call soft-cap (prompt-level) added before optional steps. Effort-steering preamble added.*

Captures key decisions, open questions, follow-ups, and working artifacts from the current session. Writes a structured entry to a session log and persists unsaved artifacts for cross-session continuity.

## Arguments

`$ARGUMENTS` can include:
- *(none)* — full capture (decisions + questions + follow-ups + context)
- `quick` — abbreviated capture (decisions + follow-ups only, no context summary)
- `project` — also write a project-level `HANDOFF.md` to the project root
- `project:name` — tag the entry with a specific project name
- `retro` — additionally run a watch-list check (looks for unresolved hypotheses, failed approaches, and patterns repeated across sessions). Opt-in only — no auto-fire on Extended sessions.

## How Routing Works (v2.0+)

`/done` decides where to write the handoff using two rules in priority order. Both prevent the most common misroute: stale state from a prior `/start-task` overrides the current working directory.

**Rule 1 — CWD precedence.** If you're working inside a sub-folder that has its own `HANDOFF.md`, route there regardless of any state file. The actual workspace beats whatever state was set days ago.

**Rule 2 — Fresh active state.** If no sub-folder HANDOFF, but there's an `active-subproject.json` file modified within the last 24 hours (or marked `permanent: true`), route to its folder — but only if the session topic actually overlaps with the state's task name. The divergence guard prevents silent misroutes when state is stale or pointing somewhere irrelevant.

**Neither rule fires.** Falls through to a non-destructive path: writes a project-root `SESSION_LOG.md` (append-only) and a global handoff. **Never overwrites a project-root `HANDOFF.md` you maintain by hand** — that requires explicit `/start-task` first.

## Instructions

**Effort-steering preamble:** This skill is structured and templated — extract facts from the conversation into slots and write outputs. Prioritize responding quickly over thinking deeply. Do not re-analyze the session. This is a low-judgment skill; high-effort reasoning is overkill and wastes tokens.

**File-write discipline:** Every write to a synced file in this skill MUST use an atomic-write helper. Direct `Write` tool or `>>` appends are forbidden for: `session-log.md`, `HANDOFF.md`, `SESSION_LOG.md`, `handoff.md`, `watch-list.md`, `skill-performance.csv`. Working-notes artifact files (new files in `working-notes/`) may use direct `Write` — they are not subject to concurrent sync collisions because each file is named per-session.

**Post-hoc budget audit:** Log the final tool-call count in Step 6's performance log line. If this run exceeded 40 calls, also write a one-line anomaly record to a rate-limit-shadow CSV. This is an audit trail, not a pre-emptive cap — the model cannot reliably count its own tool calls mid-execution.

### Step 0.5: Consolidated CWD Walk

All path resolution happens once, in a single Python subprocess. Downstream steps reference the cached values — they MUST NOT re-walk the filesystem.

```python
import os, sys, json, time

d = os.getcwd()
now = time.time()
result = {
    "SUBPROJECT_NAME": "",
    "SUBPROJECT_FOLDER": "",
    "ACTIVE_SUBPROJECT_JSON": "",
    "ACTIVE_SUBPROJECT_DATA": None,
    "STATE_MTIME_EPOCH": 0,
    "STATE_AGE_HOURS": -1,
    "STATE_SET_BY_USER": "",       # v2.2: from active-subproject.json
    "STATE_SET_ON_HOSTNAME": "",   # v2.2: from active-subproject.json
    "PROJECT_ROOT": "",
    "PROJECT_CLAUDE_MD": "",
    "CWD_HANDOFF_PATH": "",
}

cwd = d
for _ in range(7):
    asp = os.path.join(cwd, '.claude', 'active-subproject.json')
    if os.path.exists(asp) and not result["ACTIVE_SUBPROJECT_JSON"]:
        try:
            data = json.load(open(asp))
            sv = data.get('schema_version')
            if sv != 3:
                sys.stderr.write(f"⚠ active-subproject.json schema mismatch at {asp}: expected v3, got {sv!r}. Ignoring.
")
            else:
                result["ACTIVE_SUBPROJECT_JSON"] = asp
                result["ACTIVE_SUBPROJECT_DATA"] = data
                result["SUBPROJECT_NAME"] = data.get('task_name', '')
                result["SUBPROJECT_FOLDER"] = data.get('folder_relative', '')
                result["STATE_SET_BY_USER"] = data.get('set_by_user', '')
                result["STATE_SET_ON_HOSTNAME"] = data.get('set_on_hostname', '')
                mtime = os.path.getmtime(asp)
                result["STATE_MTIME_EPOCH"] = mtime
                result["STATE_AGE_HOURS"] = (now - mtime) / 3600.0
        except Exception:
            pass

    cmd = os.path.join(cwd, '.claude', 'CLAUDE.md')
    if os.path.exists(cmd) and not result["PROJECT_ROOT"]:
        result["PROJECT_ROOT"] = cwd
        result["PROJECT_CLAUDE_MD"] = cmd

    h = os.path.join(cwd, 'HANDOFF.md')
    if os.path.exists(h) and not result["CWD_HANDOFF_PATH"] and not result["PROJECT_ROOT"]:
        result["CWD_HANDOFF_PATH"] = h

    parent = os.path.dirname(cwd)
    if parent == cwd:
        break
    cwd = parent

print(json.dumps(result))
```

Parse the JSON. Cache the values. Subsequent steps reference:
- `SUBPROJECT_NAME`, `SUBPROJECT_FOLDER`, `ACTIVE_SUBPROJECT_DATA`, `STATE_AGE_HOURS` → Steps 3, 5a
- `STATE_SET_BY_USER`, `STATE_SET_ON_HOSTNAME` → Step 5a routing-audit row (v2.2)
- `PROJECT_ROOT`, `PROJECT_CLAUDE_MD` → Steps 5a, 5a.5
- `CWD_HANDOFF_PATH` → Step 5a Rule 1

If `SUBPROJECT_NAME` is empty: Step 3 omits the sub-project tag.
If `PROJECT_ROOT` is empty: Step 5a.5 falls through to Step 5b's global path.
If `CWD_HANDOFF_PATH` is empty: Step 5a Rule 1 doesn't fire; check Rule 2.

### Step 1: Identify Session Scope

Review the conversation history and determine:
- **Session topic(s):** What was worked on? (1-2 line summary)
- **Project(s) touched:** Match against known projects
- **Duration indicator:** Brief (< 10 exchanges), Medium (10-30), Extended (30+)

**Auto-quick for Brief sessions:** If duration is Brief AND no `project`, `retro`, or explicit flags were passed, apply `quick` mode semantics automatically. Saves 3-6 tool calls per Brief invocation. Do NOT auto-apply quick for Medium or Extended sessions.

### Step 2: Extract Session Content

Scan the conversation for:

**Decisions made** — configuration changes, skill edits, policy updates, approach selections, commitments.

**Approaches rejected** *(optional — only if the session pivoted away from a started approach):* `[Approach] — [why rejected]`

**Open questions** — unresolved items that need future attention, deferred items, blockers.

**Follow-ups** — concrete next steps for future sessions.

**Key artifacts created** — files written or modified.

### Step 2.7: Watch-list Check (opt-in)

Run only when the `retro` arg is present. Otherwise skip entirely. Procedure: scan for unresolved hypotheses, failed approaches, and behavioral patterns repeated across sessions. Append observations to a watch-list file (e.g., `~/.claude-assistant/working-notes/watch-list.md`).

### Step 2.5: Working Artifacts

**Skip if** ALL of: ≤5 exchanges, no files created/modified, no decisions logged, no agents spawned. Also skip in `quick` mode.

Scan for substantial working content not already saved to a file — restructuring plans, agent review outputs, draft content, detailed decision rationale. Do NOT save reproducible outputs.

For each artifact: save to `<project-root>/working-notes/` (if `project` arg and project root found) or `~/Documents/working-notes/`. Use `YYYY-MM-DD_description.md` naming.

Budget: consolidate to 1-3 files max.

### Step 3: Write Session Entry

Append to your global session log (e.g., `~/Documents/session-log.md`):

```markdown
---

## [YYYY-MM-DD HH:MM] — [SUBPROJECT_NAME] [Session topic summary]
SESSLOG:[YYYY-MM-DD HH:MM]

**Project(s):** [project names or "General"]
**Duration:** [Brief/Medium/Extended]

### Decisions
- [Decision 1]

### Open Questions
- [Question 1]

### Follow-ups
- [ ] [Action item 1]

### Artifacts
- [Created/Modified] `path/to/file` — [what changed]

[If not `quick`:]
### Context
[2-4 sentence summary of key context for the next session.]
```

If the file doesn't exist, create with header `# Session Log` + a brief description. **New entries go at the TOP** (reverse chronological).

**Sub-project tagging:** If `SUBPROJECT_NAME` was found in Step 0.5, include it in brackets before the topic. Otherwise omit the brackets entirely.

### Step 3.5: Project SESSION_LOG.md Append (opt-in)

**Skip if** the current project's `.claude/CLAUDE.md` does not contain `session_log: true`, or if no project root is found.

If `session_log: true` is set: append a session entry to `<PROJECT_ROOT>/SESSION_LOG.md` (chronological, oldest first — opposite of the global log).

### Step 4: Prune and Cleanup

**Session log pruning (v2.4 — deterministic helper):**

Call the deterministic Python prune helper. It implements tiered cutoffs (file-size → cutoff-days), so it actually fires under high-volume workflows where the old fixed 30-day cutoff produced false-negative no-ops:

```bash
python3 ~/.claude-assistant/scripts/session-log-prune.py
```

The helper reads your global session log, archives entries older than the tier's cutoff to a sibling `session-log-archive.md`, and prints a one-line summary on stdout that you copy into Step 6's summary block. Tiers (most-aggressive first):

| File size | Cutoff |
|-----------|--------|
| > 10,000 lines | 7 days (emergency) |
| > 6,000 lines | 14 days (busy) |
| > 3,000 lines | 30 days (hard) |
| > 1,500 lines | 60 days (soft) |
| ≤ 1,500 lines | no-op |

Why deterministic: when this step was natural-language, the model silently skipped it under Brief / auto-quick effort routing, and the file drifted from ~3,000 to ~9,700 lines before it was caught. Calling a single script replaces "the model decides whether to prune" with "the harness runs the prune unconditionally."

If the helper is missing or errors out: surface the error in Step 6 summary and continue with the rest of /done — pruning is non-blocking.

**Working-notes cleanup:** Delete files in `working-notes/` older than 30 days (by mtime). Skip if no `working-notes/` directory exists.

### Step 5: Write Handoff Note

#### 5a. Sub-folder routing (CWD precedence)

Two rules in priority order. Use cached values from Step 0.5.

**Rule 1 — CWD precedence.** If `CWD_HANDOFF_PATH` is non-empty, route there regardless of `active-subproject.json`.

1. `folder_path = os.path.dirname(CWD_HANDOFF_PATH)`.
2. Derive `task_name`: read the first non-empty H1 of `CWD_HANDOFF_PATH`. If it matches `^# Handoff — (.+)$`, use the capture group; else use folder basename title-cased.
3. **Overwrite logging:** Read first non-empty line of existing `CWD_HANDOFF_PATH`, append to global session log: `*Sub-folder handoff overwritten (cwd-precedence): [first-line]*`
4. Write `folder_path/HANDOFF.md` using the project-level template.
5. **Routing audit** (see "Routing audit log" below). `RULE_FIRED="1-cwd-precedence"`, `CHOSEN=folder_path`.
6. **Global handoff:** write to your global handoff file ONLY if infrastructure files were modified (skill files, agent files, config files). Otherwise skip.
7. **Return** — skip Rule 2.

**Rule 2 — Fresh active state.** If Rule 1 did NOT fire AND `ACTIVE_SUBPROJECT_DATA` is non-empty AND `STATE_AGE_HOURS` is between 0 and 24 (or `permanent: true` in state), route to the state's folder.

*Why 24h not 14 days:* `set_at` fields can be LLM-fabricated; v2 uses filesystem `mtime` (computed in Step 0.5) with a tighter window. 24h matches typical "I set it today" intent; anything older probably isn't the current session's topic.

**Rule 2 divergence guard (v2.1).** Before committing to route to state folder, check for topic divergence.

1. Tokenize `ACTIVE_SUBPROJECT_DATA.task_name` and the session's Step 1 topic summary: lowercase, split on whitespace/hyphens/underscores/slashes, drop stopwords (`the`, `a`, `an`, `and`, `of`, `for`, `to`, `in`, `on`, `project`, `task`, `trip`, `session`, `management`, `integration`, `skill`, `skills`).
2. If the intersection of the two token sets is **empty** → divergent session. Execute the divergent path. If the intersection is non-empty → proceed with the normal Rule 2 steps.

**Divergent path (token intersection empty):**

a. Do NOT overwrite `folder_path/HANDOFF.md`. Leave the state folder's HANDOFF untouched.
b. **Routing audit.** `RULE_FIRED="2-fresh-state-divergent"`, `CHOSEN="-"`, `STATE_FOLDER=<state.folder_relative>`.
c. Fall through to Step 5a.5 — the project-root SESSION_LOG.md append path. Session content is still captured there.
d. **Step 6 breadcrumb (mandatory surface in summary):**
   ```
   ⚠ State/session divergence detected
     Active sub-project: [state.task_name] ([state.folder_relative])
     Session topic:      [Step 1 topic summary]
     State HANDOFF preserved; session captured in <PROJECT_ROOT>/SESSION_LOG.md.
     To route to a different folder, run: /start-task folder:<target> && /done
   ```

**Normal Rule 2 path (token intersection non-empty):**

1. Read: `folder_path`, `task_name`, `folder_relative` from `ACTIVE_SUBPROJECT_DATA`.
2. **Overwrite logging:** If `folder_path/HANDOFF.md` exists and is non-empty, read first non-empty line, append to session-log.md: `*Sub-project handoff overwritten: [first-line]*`
3. **Write** `folder_path/HANDOFF.md` tagged `*Project: [task_name]*` + `SESSLOG:[timestamp]`.
4. **Routing audit.** `RULE_FIRED="2-fresh-state"`, `CHOSEN=folder_path`.
5. **Global handoff:** same infrastructure-only rule as Rule 1.
6. Step 6 summary: `Handoff (scoped): [folder_relative]/HANDOFF.md [via: fresh-state, age=[N]h] [written]`.
7. **Return** — skip Step 5a.5 and Step 5b scoped write.

**Neither rule fired:**
- No CWD HANDOFF AND no state file → fresh session, no context → fall through.
- State exists but stale (>24h, not permanent) → fall through. Write routing-audit row with `RULE_FIRED="0-stale-state-fallthrough"` before falling through.

**Routing-audit log (required after ANY routing decision):**

Location: `~/.claude-assistant/logs/routing-audit.csv`
Schema (v2.2): `timestamp,session_id,cwd,rule_fired,chosen_folder,state_folder,state_age_hours,hostname,state_set_by_user,state_set_on_hostname`

Schema-version notes:
- Pre-2.1 rows: 7 fields (no `hostname`).
- v2.1 rows: 8 fields (no `state_set_by_user`/`state_set_on_hostname`).
- v2.2+ rows: 10 fields. The two new fields originate from `active-subproject.json`'s `set_by_user` and `set_on_hostname`; empty strings if the state file is older.

Readers should tolerate 7-field, 8-field, OR 10-field rows (positional parse).

One row per `/done` invocation. Append-only. v2.2 row size ~110 bytes.

#### 5a.5. CWD-fallback routing (no active sub-project) — non-destructive

When neither Rule 1 nor Rule 2 fires:

1. **Do NOT touch project-root `HANDOFF.md`** — leave any existing file at `CWD_HANDOFF_PATH` exactly as-is. A project-root HANDOFF.md the user maintains by hand is theirs to manage; `/done` will not overwrite it without an explicit `/start-task`.

2. **Capture session content in project-root `SESSION_LOG.md` instead** (append-only, reverse-chronological). Target: `<PROJECT_ROOT>/SESSION_LOG.md`. If `PROJECT_ROOT` is empty, skip and fall through to Step 5b.

3. If `SESSION_LOG.md` doesn't exist, create with the canonical header.

4. **Prepend the session entry** using the same block format as Step 3. The atomic-write helper inserts a `<!-- written by: HOSTNAME at ISO8601 -->` line so cross-machine origin is visible.

5. **Routing-audit row.** Write a row with `RULE_FIRED="3-project-log"`, `CHOSEN="<PROJECT_ROOT>/SESSION_LOG.md"`.

6. **Fall through to Step 5b** — the global handoff still gets written. Do NOT `return` early.

7. **Step 6 summary:** show `Handoff (scoped): <PROJECT_ROOT>/SESSION_LOG.md [via: cwd-project-log] [appended]` and `Project HANDOFF.md: preserved (no active sub-project — run /start-task to write a scoped HANDOFF)`.

**Why this design:** the destructive code path (silently overwriting project-root HANDOFF.md) is removed, not guarded. No prompt-dismissal or transcription error can restore the failure mode. Cross-session context is still captured via append-only SESSION_LOG.md.

#### 5b. Standard handoff (all other cases)

**Overwrite logging:** Before overwriting your global handoff file, if the existing file is non-empty, append to session-log.md: `*Previous handoff overwritten: [topic from old handoff]*`.

Generate the handoff note (≤30 lines) and overwrite `~/.claude/handoff.md` (or your equivalent) for SessionStart-hook resumption.

**Routing-audit row:** After writing, append a row with `RULE_FIRED="4-global-handoff"`, `CHOSEN="~/.claude/handoff.md"`.

**Key rules:**
- Max 30 lines (Working Artifacts lines don't count — they're pointers)
- Working Artifacts section only appears when artifacts were saved
- Use **absolute paths** in Key Files; **checkboxes** for Next Steps
- In `quick` mode: omit the Context section
- Active Decisions: only decisions constraining the *next* session
- Include `SESSLOG:[YYYY-MM-DD HH:MM]` cross-reference

```markdown
# Handoff — [YYYY-MM-DD]
SESSLOG:[YYYY-MM-DD HH:MM]

## Session Topic
[1-line summary]

## Active Decisions
- [Decision constraining next session]

## Key Files
- [absolute path to important file]

## Next Steps
- [ ] [Most important next step]
- [ ] [Other follow-ups]

## Working Artifacts
- [path/to/artifact] — [what it contains]

## Context
[1-2 sentences for the next session to pick up seamlessly]
```

### Step 6: Summary

Display a brief confirmation:

```
────────────────────
SESSION CAPTURED
────────────────────
Topic: [summary]
Decisions: [N] | Questions: [N] | Follow-ups: [N] | Artifacts: [N]
[If working artifacts saved:] Working artifacts saved: [N] files → [directory path]
[If pruning ran:] Pruned: [N] entries → session-log-archive.md
[If retro flag fired:] Watch-list: [M new, K incremented]
Logged to: session-log.md
Handoff (scoped): [path]  [via: sub-project / cwd-project-log / global]  [written / appended / skipped]
Handoff (global): [path] [written / skipped]
[If v1.12 cwd-fallback path fired:] Project HANDOFF.md: preserved (no active sub-project — run /start-task to write a scoped HANDOFF)

[If divergence detected:]
⚠ State/session divergence — see breadcrumb above

[If open questions exist:]
⚠ [N] open questions — pick these up next session

[If Duration is Extended and retro flag was NOT used:]
ℹ Extended session — if hypotheses or patterns repeated across sessions, re-run with: /done retro

[If follow-ups exist:]
Next time: [most important follow-up item]
────────────────────
```

**v2.3 — Phase 0 affordance.** After printing the summary, emit an OSC-0 terminal-title escape via `/dev/tty` so the editor tab strip shows `[<task-short>] done`. Source the task name from `SUBPROJECT_NAME` (Step 0.5 cache). Falls silently to no-op if `/dev/tty` is unwritable or not the controlling terminal.

```bash
# v2.4.1: brace-group + outer 2>/dev/null silences "device not configured: /dev/tty" when the bash
# subprocess has no controlling terminal (any harness-spawned subshell). The plain
# `>/dev/tty 2>/dev/null` pattern leaks the open-error past 2>/dev/null.
if [ -n "$SUBPROJECT_NAME" ]; then
  SHORT_NAME=$(echo "$SUBPROJECT_NAME" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | cut -c1-20)
  { printf ']0;[%s] done' "$SHORT_NAME" >/dev/tty; } 2>/dev/null || true
else
  { printf ']0;[no-anchor] done' >/dev/tty; } 2>/dev/null || true
fi
```

## Customization Points

- **Log file location:** Default `~/Documents/session-log.md`. Adjust to your preferred location.
- **Handoff file location:** Default `~/.claude/handoff.md` (read by SessionStart hook). Adjust if your hook reads from elsewhere.
- **Working-notes directory:** Default `~/Documents/working-notes/`. Adjust as needed.
- **Archive retention:** Tiered cutoffs in the prune helper (7d / 14d / 30d / 60d depending on file size). Adjust thresholds in the helper script to your tolerance.
- **Sub-project routing:** Requires the optional `/start-task` skill to populate `.claude/active-subproject.json`. Without it, only Rule 1 (CWD precedence) and Step 5a.5 (project-root SESSION_LOG.md) fire — both work fine without state files.
- **Routing-audit CSV:** Default `~/.claude-assistant/logs/routing-audit.csv`. Adjust to wherever you keep skill telemetry.
- **Prune helper:** Default `~/.claude-assistant/scripts/session-log-prune.py`. A standalone Python script that reads the global session log, archives by tier, and prints a one-line summary. Easy to swap for any equivalent script of your own.

## Error Handling

- **No substantive content:** "Nothing to capture — session was too brief." Exit.
- **Session log write fails:** Display the entry in the terminal so you can manually save it.
- **Prune helper missing or errors:** Surface the error in Step 6 summary; pruning is non-blocking — the rest of /done continues.

## Design Notes

- **Complements session-closing patterns** — those suggest *improvements* (new skills, rules, agents). This skill captures *artifacts* (decisions, questions, follow-ups).
- **No MCP tools needed** — pure filesystem operation.
- **Skip-gate audit:** When working artifact scan is skipped, the reason is logged. Grep for `SKIPPED artifact scan` to detect over-firing.
- **SESSLOG cross-references:** Both session log entries and handoff notes include `SESSLOG:[YYYY-MM-DD HH:MM]` for grep-able traceability.

## Log Performance

```bash
echo "$(date +%Y-%m-%d),done,TOOL_CALLS,NOTES" >> ~/.claude-assistant/logs/skill-performance.csv
```

Replace TOOL_CALLS with best estimate. **NOTES uses a structured format (v2.4.2) so post-hoc analysis can group runs without parsing free text:**

`mode:MODE session:SESSION files:FILES rule:RULE [optional description]`

| Field | Values |
|-------|--------|
| mode | `full` \| `quick` \| `auto-quick` |
| session | `Brief` \| `Medium` \| `Extended` (from Step 1) |
| files | integer count of files written this run |
| rule | `1-cwd` \| `2-fresh` \| `2-divergent` \| `3-project-log` \| `4-global` \| `none` |

Example: `mode:full session:Extended files:3 rule:1-cwd resolver-migration-deploy`

If this run exceeded the 40-call threshold, also append an anomaly row to a rate-limit-shadow CSV.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/done.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>chrisblattman/claudeblattman</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../claudeblattman.md">claudeblattman (Chris Blattman)</a></dd>
<dt><b>Category</b></dt><dd><code>infra</code></dd>
<dt><b>Field</b></dt><dd>general</dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/chrisblattman/claudeblattman">⭐ chrisblattman/claudeblattman</a><br><img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/done.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/claudeblattman/done/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/claudeblattman.yml">edit on GitHub</a>.</p>
</div>

</div>
