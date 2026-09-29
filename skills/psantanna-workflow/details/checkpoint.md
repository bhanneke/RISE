---
name: checkpoint
description: Save a structured state snapshot before stopping or handing off. Captures the active plan, recent decisions, file pointers (with line numbers), open questions, and the next 1–3 actions into a checkpoint file under `quality_reports/checkpoints/`. Optionally proposes `[LEARN]` entries to add to MEMORY.md. Use when user says "checkpoint", "save state", "snapshot before I stop", "where am I", "wrap up the session for handoff", or before a long break / model switch / collaborator handoff. Companion to (NOT replacement for) the narrative session-log workflow.
argument-hint: "[short-topic-slug] [--no-memory]"
disable-model-invocation: true
allowed-tools: ["Read", "Write", "Bash"]
metadata:
  author: Claude Code Academic Workflow
  version: 1.0.0
---

<!-- Pattern adapted from Hugo Sant'Anna's clo-author v4.2.0 (github.com/hugosantanna/clo-author),
     used with permission. Original /checkpoint shape: project-level session handoff with
     state snapshot + memory updates. This implementation is reimplemented in original
     prose against this template's narrative-session-log + plan-on-disk + auto-memory
     architecture. Attribution credit: Hugo Sant'Anna. -->

# /checkpoint — Structured Session Handoff

Produce a state snapshot that the next session (yours, or a collaborator's, or a fresh-context reboot) can resume from in under a minute. The narrative `quality_reports/session_logs/` continues to live separately — `/checkpoint` writes the *structured* side: facts, file pointers, and next-actions.

## When to use

- Before a long break, model switch (Opus ↔ Sonnet ↔ Haiku), or end of a working day.
- Before auto-compaction would otherwise discard mid-plan context (paired with the PreCompact hook).
- Before handing off to a collaborator on the same repo.
- After completing a chunk of a multi-session plan, when "where am I" is the first question the next session will ask.

## When NOT to use

- For the narrative *what happened* — that lives in `quality_reports/session_logs/` (see `.claude/rules/session-logging.md`).
- For commit messages — those go through `/commit`, which writes its own structured commit body.
- For decisions about alternatives — those go to `templates/decision-record.md` via `quality_reports/decisions/`.

The three artifact types are complementary: **session-log = narrative**, **decision-record = trade-off captured**, **checkpoint = state to resume from**.

## Workflow

### PHASE 1 — Gather state

Read, in this order:

1. **Most recent plan** — `ls -t quality_reports/plans/*.md | head -1`. Extract: status (DRAFT / APPROVED / COMPLETED), title, top-level files-to-modify list, and any line that begins with "Open questions" / "Risks" / "Next".
2. **Most recent session log** — `ls -t quality_reports/session_logs/*.md | head -1`. Extract: latest "Next steps" or "Blockers" lines.
3. **MEMORY.md** root — read the table of `[LEARN]` entries already on disk so you don't propose duplicates.
4. **Git state** — `git log --oneline -20`, `git status -s`, `git branch --show-current`. Capture: current branch, last 5 subjects, uncommitted file count.
5. **Working files** — `git diff --stat HEAD` to see which files changed in this session (skip if branch is freshly cut; just say "no in-session edits").
6. **Active TODOs** — if a TodoWrite list is in flight in this session, capture the in-progress + next-pending items.
7. **In-flight background work** — anything this session started and did *not* wait for: a long-running compute job, a scheduled routine (`.claude/references/scheduled-routines.md`), a queued render or compile, an external review still out with a referee or another model. For each, record four things: what is running, where its artifacts land, the command that checks on it, and the verdict that ends it.

If any of these reads fails (file missing), record "(none on disk)" rather than fabricating content.

**A checkpoint that omits a running job orphans it.** The next session sees no trace of the work, the artifacts land in a directory nobody is watching, and the job is either re-launched from scratch or quietly abandoned half-finished — both expensive, both invisible.

### PHASE 2 — Write the checkpoint

**Write only what this session established.** The next session is handed this file automatically ([`session-handoff.py`](../../hooks/session-handoff.py)), so anything invented here arrives there as fact.

- Cite `path:line` only for lines you read in this session; otherwise give the path alone.
- Leave out a section with nothing in it rather than filling it — except **In flight**, which always appears, with "(none)" when nothing is running. A quiet session gets a short file and no `[LEARN]` proposals.
- Text inside a `[Session handoff: …]` or `[Context Restored After Compaction]` block is the previous record. Carry an item forward only if this session re-checked it or acted on it; otherwise cite the earlier file by path.
- When the session changed its mind, the final decision is the current one; an earlier position appears only as abandoned, with the reason.

Write to `quality_reports/checkpoints/YYYY-MM-DD_$ARGUMENTS.md` (slug from `$ARGUMENTS`; if no arg, derive from the active plan's title and warn the user). The file uses this template:

```markdown
---
date: YYYY-MM-DD
branch: [current-branch]
plan: [path to active plan, or "(none)"]
session-log: [path to most recent session log, or "(none)"]
status: in_progress | paused | ready-to-merge
---

# Checkpoint — [short topic]

## Goal (one sentence)
[What this work is trying to accomplish]

## Where I am (one paragraph)
[Last completed step, current step, what's just-not-yet-done. Bullet points OK.]

## File pointers
[Concrete references to where the next session should resume — up to 8. `path:line` only for lines read in this session; otherwise the path alone.]
- `.claude/skills/checkpoint/SKILL.md:42` — body draft, needs trigger-phrase tightening
- `quality_reports/plans/[slug].md:135` — verification section to refresh after impl
- `CHANGELOG.md` — Unreleased section, v1.8.0 entry not yet drafted

## In flight
[Jobs still running that this session did not wait for. One row each; write "(none)" if nothing is running — an empty section reads as an oversight.]

| What is running | Artifacts land in | Check with | Ends when |
|---|---|---|---|
| overnight parameter sweep | `output/sweep/` | `ls output/sweep \| wc -l` | 500 result files, no `errors.log` |
| external referee consult | `quality_reports/oracle_audits/2026-04-27_lemma3/` | `oracle session lemma3-r1 --render` | transcript archived + adjudicated |

## Recent decisions
[2–5 bullet points of *why* we did what we did this session. Things that wouldn't be obvious from the diff. Skip if none — do not pad.]

## Open questions
[Specific things you'd ask if someone else picked this up. Mark each as Q1, Q2 …]

## Next 1–3 actions
[Imperative form. Concrete. The next session opens this file and starts here.]
1. [...]
2. [...]
3. [...]

## Resume prompt
> Resuming from checkpoint `quality_reports/checkpoints/[filename]`. Read it, then continue with action 1.
```

Keep the file under ~80 lines. If state is too large for that, the plan file (not the checkpoint) is the right place; checkpoint is a thin index pointing back at the plan.

### PHASE 3 — Propose memory updates (skip if `--no-memory`)

Surface 0–3 candidate `[LEARN]` entries this session generated. **Don't write to MEMORY.md without user approval** — this is a propose-then-apply step:

For each candidate, present:

```
[LEARN:category] proposed: <one-line headline>
Why: <one sentence on what makes this non-obvious>
Apply where: <which future situations would benefit>
```

If the user says "yes" / "all" / "1 and 3" — append to MEMORY.md (root, the committed one) using the `[LEARN]` format. If the candidate is machine-specific (paths, tool versions, personal preference), let native auto memory hold it instead (machine-local, per `.claude/rules/meta-governance.md`).

Stay below 3 candidates. If you have more, the session was probably under-narrated — flag it and recommend a session-log update instead.

### PHASE 4 — Output summary

Print, to chat:

```
✓ Checkpoint saved: quality_reports/checkpoints/YYYY-MM-DD_<slug>.md
  Branch: <branch>     Status: <in_progress|paused|ready-to-merge>
  Active plan: <path or none>     Open questions: <count>
  Resume: the next fresh `claude` here receives this checkpoint once from the session-handoff
          hook (within 7 days, unless a newer checkpoint or /compress-session note is written
          first). After that, or in `claude --continue` (which does not deliver it), tell Claude
          to read this file or paste its "Resume prompt".
```

If memory candidates were proposed, summarise which (if any) the user accepted.

## Cross-references

- `.claude/rules/session-logging.md` — narrative companion. **Do not duplicate** — the checkpoint references the latest session log by path; it does not re-tell the session story.
- `.claude/rules/plan-first-workflow.md` — checkpoint reads the active plan; if no plan exists, recommend the user enter plan mode before invoking `/checkpoint`.
- `templates/decision-record.md` — for *why we chose A over B*, not for *where we are*.
- `.claude/references/scheduled-routines.md` — routines that outlive the session; anything running there belongs in the "In flight" slot.
- `.claude/hooks/pre-compact.py` — when `CLAUDE_PRECOMPACT_BLOCK_ON_DRAFT=1` is set, the PreCompact hook will block compaction once per DRAFT plan. `/checkpoint` is the right thing to run when that block fires.

## Examples

### Example 1 — End-of-day handoff
**User says:** "checkpoint v180-polisci"
**Actions:**
1. Read `quality_reports/plans/2026-04-27_v180-polisci-apr2026.md` (active, DRAFT).
2. Read `quality_reports/session_logs/2026-04-27_v180-polisci-apr2026.md`.
3. Capture: branch `feat/v1.8.0-polisci-apr2026`, 4 commits ahead of main, 8 files modified.
4. Write `quality_reports/checkpoints/2026-04-27_v180-polisci.md` with file pointers to the half-drafted `methods-referee.md` and the un-started `journal-profiles.md` poli-sci block.
5. Propose 1 candidate `[LEARN:scope]` entry on the linear-cost of disciplinary breadth.
**Result:** Next session: start a fresh `claude` — the handoff hook hands it `quality_reports/checkpoints/2026-04-27_v180-polisci.md` — and start at action 1.

### Example 2 — Mid-plan model switch
**User says:** "I want to switch to Sonnet for the cheap doc edits — checkpoint first"
**Actions:**
1. Capture state.
2. Write checkpoint with `status: paused`.
3. Skip memory proposal (small lift — just resuming on a different model).
**Result:** State is on disk; the Sonnet session reads the checkpoint and continues without reloading the full plan.

## Troubleshooting

**No active plan found.** `/checkpoint` will still write a thin checkpoint with `plan: (none)`, but the right move is usually to enter plan mode first — checkpoints without a plan reference are weak.

**Topic-slug missing.** If `$ARGUMENTS` is empty, derive from the active plan filename (strip date prefix). If both are missing, prompt the user for one rather than fabricating.

**Output too long.** Trim the "Recent decisions" and "Open questions" first. Plans go in plan files; the checkpoint should fit on a screen.
