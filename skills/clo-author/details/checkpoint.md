---
name: checkpoint
description: >
  Session handoff — persists what happened in the current session to memory,
  SESSION_REPORT.md, and the research journal. Use when wrapping up a work session,
  before `/compact`, or when the user says "checkpoint", "save progress", "sync",
  "wrap up", "log this", or "handoff". Optionally pushes to Obsidian if the user
  has configured `.claude/state/obsidian-config.md`. Does NOT run briefings,
  calendar, or mail. Just gather, confirm, save.
argument-hint: "[--auto | --memory-only | --scaffold-only | --dry-run]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash
---

# Checkpoint: Session Handoff

Captures what happened in the current session and pushes it to three places (plus optionally a fourth):

1. **Claude Code auto-memory** (`~/.claude/projects/.../memory/`) — learnings for future conversations
2. **`SESSION_REPORT.md`** (project root) — append-only session log per `.claude/rules/logging.md`
3. **`quality_reports/research_journal.md`** — agent-invocation trail
4. **Obsidian vault** (optional, gated) — project-note journal, dashboard, daily journal

You are fast and minimal. One confirmation prompt, then save.

---

## Flow

### Step 1: Gather Context

Run these in parallel (single message, multiple Bash calls):

```bash
basename "$(pwd)"
git log --oneline -10
git diff --stat
git diff --cached --stat
```

Then scan:
- `CLAUDE.md` header for the project name
- `quality_reports/plans/` for files modified today
- `quality_reports/session_logs/` for files modified today (if the project uses session logs)
- The conversation context for key decisions, corrections, or learnings that qualify for auto-memory

### Step 2: Detect Obsidian Configuration

Check for `.claude/state/obsidian-config.md`:

```bash
test -f .claude/state/obsidian-config.md && echo "OBSIDIAN: configured" || echo "OBSIDIAN: not configured"
```

If the file exists, read it to extract:
- Vault path
- Project-name mapping (working directory → Obsidian project note)

If the file does not exist, Obsidian integration is inactive for this session. Proceed without it — do not ask the user to set it up unless they invoke `/checkpoint --setup-obsidian` (see below).

### Step 3: Draft Updates (present to user for confirmation)

Present a compact summary:

```
## Checkpoint Summary

**Project:** [name] | **Branch:** [current branch]
**Session:** [date, ~duration if inferrable]
**Obsidian:** [configured: path | not configured]

### What happened
- [bullets from git log + conversation context]

### Memory updates
- [new learnings to save — or "None"]

### Scaffold updates
- **SESSION_REPORT.md:** [entry to append]
- **quality_reports/research_journal.md:** [entry to append — if any agent work happened]

### Obsidian updates
- [if configured: project note journal entry, dashboard row, daily journal]
- [if not configured: "Skipped — no .claude/state/obsidian-config.md"]
```

**Ask the user:** "Look right? I'll save all of this." Wait for confirmation or edits.

Skip confirmation if invoked with `--auto` or the user said "just do it".

### Step 4: Save Everything

Execute all saves. Each section is independent — if one fails, the others still run.

#### 4a. Claude Code Auto-Memory

Check existing memory files first — update rather than duplicate.

**Qualifies for memory:**
- User corrections or preferences (`feedback` type)
- Project state that isn't in git (`project` type)
- External references discovered (`reference` type)
- User profile updates (`user` type)

**Does NOT go in memory** (per auto-memory rules):
- Code patterns, file paths, architecture
- Git history (derivable from `git log`)
- Debugging solutions (the fix is in the code)
- Ephemeral task details

Write/update memory files with the standard frontmatter, then update `MEMORY.md` index.

#### 4b. SESSION_REPORT.md

Append-only. If the file doesn't exist, create it with header `# Session Report — [Project Name]`.

Entry format (per `.claude/rules/logging.md`):

```markdown
## YYYY-MM-DD HH:MM — [Brief Title]

**Operations:**
- [Scripts run, files created/modified/deleted]

**Decisions:**
- [Choice made] — [rationale]

**Results:**
- [Key findings, outputs produced]

**Commits:**
- `[hash]` [commit message]

**Status:**
- Done: [what's complete]
- Pending: [what remains]
```

#### 4c. quality_reports/research_journal.md

Append only if agent work happened this session (writer, coder, strategist, etc.). Entry format per `logging.md`:

```markdown
### YYYY-MM-DD HH:MM — [Agent Name]
**Phase:** [Discovery/Strategy/Execution/Peer Review/Presentation]
**Target:** [file or topic]
**Score:** [XX/100 or PASS/FAIL or N/A]
**Verdict:** [one line — key finding or decision]
**Report:** [path to full report]
```

#### 4d. Obsidian (optional, only if `.claude/state/obsidian-config.md` exists)

Follow the project's `obsidian-config.md` for vault path and project mapping. Then:

1. Add journal entry to the matched project note via Obsidian MCP (`obsidian_get_file_contents` → modify → `obsidian_delete_file` + `obsidian_append_content`). Reverse chronological — newest first, after `## Journal` heading.
2. Update the dashboard (`Home.md`) only if something changed (stage transition, status update, Next Action change, Days in Stage recalc). Sync General Kanban if the project is research-tracked.
3. Append to today's daily journal (`Journal/YYYY-MM-DD.md`). Create from template if it doesn't exist.

Entry format for project note journal:

```markdown
### YYYY-MM-DD

**Done:**
- [concrete accomplishments from this session]

**Next:**
- [concrete next steps]
```

Keep it tight — 3–5 bullets per section max.

### Step 4e. Refresh Project Dashboard

Regenerate the project dashboard to capture latest session state:
```bash
python3 scripts/generate_dashboard.py
```

### Step 5: Confirm

Report what was saved:

```
Checkpoint saved:
- Memory: [updated/created N files | no changes]
- SESSION_REPORT.md: [entry added]
- research_journal.md: [entry added | skipped — no agent work]
- Dashboard: [refreshed]
- Obsidian: [entry added to Project Name | not configured]
```

---

## Flags

| Flag | Effect |
|------|--------|
| `--auto` | Skip user confirmation, just save |
| `--memory-only` | Only update Claude Code memory |
| `--scaffold-only` | Update memory + SESSION_REPORT + research_journal, skip Obsidian |
| `--dry-run` | Show what would be saved, don't save |
| `--setup-obsidian` | Walk the user through creating `.claude/state/obsidian-config.md` from the example template |

---

## Obsidian Config Setup (on demand)

When invoked with `--setup-obsidian`:

1. Check if `.claude/state/obsidian-config.md.example` exists; if not, flag and stop.
2. Copy the example to `.claude/state/obsidian-config.md`.
3. Walk the user through filling in: vault path, project-name mapping for the current working directory.
4. Verify Obsidian MCP is connected; if not, point the user to the Obsidian REST API plugin setup.
5. Confirm `.claude/state/` is in `.gitignore`.

Do NOT run this on every checkpoint — only when the user explicitly opts in.

---

## Bundled Resources

| Resource | Path | What It Contains |
|----------|------|-----------------|
| Session report entry | `checkpoint/templates/session-report-entry.md` | Append format for SESSION_REPORT.md |
| Research journal entry | `checkpoint/templates/research-journal-entry.md` | Append format for research_journal.md |
| Memory entry types | `checkpoint/templates/memory-entry-types.md` | 4 memory types with when-to-save guidance |
| Gotchas | `checkpoint/gotchas.md` | Known failure points and edge cases |

---

## Rules

- **Never invent progress.** Only log what actually happened — from git, conversation, or user confirmation.
- **Be fast.** The whole checkpoint should take under 60 seconds including user confirmation.
- **Don't duplicate.** Check existing memory files before creating new ones. Check if today's journal entry already covers this project.
- **Respect meta-governance.** Fork users get memory + SESSION_REPORT + research_journal out of the box. Obsidian integration is opt-in and gated behind local config.
- **`.claude/state/obsidian-config.md` is local-only.** It contains user-specific paths and mappings; `.gitignore` keeps it out of commits.
- **Dashboard is source of truth** for Obsidian project stages (when Obsidian is active). Don't contradict it.
- **Memory is for future conversations.** Don't save things only useful right now.
- **Minimal user friction.** One confirmation prompt, not five. Default to "looks right? saving."

---

## Precedence

If the user has a user-level `checkpoint` skill at `~/.claude/skills/checkpoint/`, this project-level skill takes precedence when invoked from within clo-author. The user-level skill continues to work for projects that don't have this file.
