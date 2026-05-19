<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/permission-check.md -->

# `/permission-check`



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
name: permission-check
description: Diagnose why Claude Code is (or isn't) prompting for permission. By default reads only repo-local layers (CLI project, CLI project-local, VSCode workspace). Host-global layers (CLI user `~/.claude/`, VSCode user settings) are read ONLY when the user explicitly confirms — those files may contain unrelated paths or secrets. Use when user says "why is it asking me to approve?", "permission check", "why am I getting prompts?", "bypass isn't working", "check my permissions". Read-only diagnostic.
argument-hint: "(no arguments)"
allowed-tools: ["Read", "Bash", "Glob"]
---

# Permission Check

## Purpose

Surface the full permission-mode picture across every layer Claude Code honors, so the user can see at a glance why prompts are (or aren't) firing. Claude Code resolves permission mode from a 6-tier stack; a single misconfigured layer produces silent overrides that are hard to debug by eye.

## The 6 layers (precedence: bottom wins)

1. **VSCode user settings** — `~/Library/Application Support/Code/User/settings.json` (macOS), `%APPDATA%/Code/User/settings.json` (Windows), `~/.config/Code/User/settings.json` (Linux). Key: `claudeCode.initialPermissionMode`.
2. **VSCode workspace settings** — `<repo>/.vscode/settings.json`. Same key. Wins over user.
3. **CLI user settings** — `~/.claude/settings.json`. Key: `permissions.defaultMode`.
4. **CLI project settings** — `<repo>/.claude/settings.json`. Same key. Wins over user.
5. **CLI project-local settings** — `<repo>/.claude/settings.local.json`. Same key. Wins over project.
6. **In-session mode** — set at session start from layers 1-5, then mutable via `Shift+Tab` or `/permission-mode`. Authoritative until session ends.

**Key insight:** `initialPermissionMode` only fires at session start. If you toggled mid-session (or the session started before a settings change), the file-level settings are correct but the *runtime* mode differs. That's the #1 source of "bypass isn't working" confusion.

## Privacy contract

Host-global settings files (`~/.claude/settings.json`, VSCode user settings) may contain:
- Paths to unrelated projects and secrets
- API keys, tokens, or provider credentials added outside this repo
- Permission policies set by the user's org or employer

This skill is designed for defense-in-depth: **Phase A runs automatically and reads only repo-local files.** Phase B reads host-global files **only after the user explicitly confirms** — never silently. When reporting host-global layers, redact any key that is not directly relevant to `permissions.*` or `claudeCode.*`.

## Protocol

### Phase A: Repo-local layers (auto-runs)

Read these immediately — they are checked into (or gitignored inside) the repo and do not cross the trust boundary:

```bash
VSCODE_WS="${CLAUDE_PROJECT_DIR}/.vscode/settings.json"
CLI_PROJECT="${CLAUDE_PROJECT_DIR}/.claude/settings.json"
CLI_LOCAL="${CLAUDE_PROJECT_DIR}/.claude/settings.local.json"
```

For each file that exists, extract:
- **VSCode workspace:** `claudeCode.initialPermissionMode`, `claudeCode.allowDangerouslySkipPermissions`
- **CLI project / project-local:** `permissions.defaultMode`, `permissions.allow`, `permissions.deny`

Missing files are fine — report "not present" rather than erroring.

Print the resolved defaultMode from these three layers alone. If that already explains the prompt behavior (e.g., CLI project-local has `defaultMode: "default"` while project has `bypassPermissions`), stop here and surface the diagnosis.

### Phase B: Host-global layers (requires explicit user confirmation)

If Phase A is inconclusive — e.g., all repo-local layers agree on bypass but the user is still being prompted — ask the user:

> "To complete the diagnosis, I need to read two files outside this repo:
> - `~/.claude/settings.json` (CLI user-level)
> - your VSCode user settings (`~/Library/Application Support/Code/User/settings.json` on macOS; Linux/Windows vary)
>
> These may contain unrelated paths or secrets. I will redact any key that isn't in `permissions.*` or `claudeCode.*`. Proceed?"

Only after the user confirms, read:

```bash
# VSCode user (platform-dependent path; try all three)
case "$(uname -s)" in
    Darwin)  VSCODE_USER="${HOME}/Library/Application Support/Code/User/settings.json" ;;
    Linux)   VSCODE_USER="${HOME}/.config/Code/User/settings.json" ;;
    MINGW*|MSYS*|CYGWIN*) VSCODE_USER="${APPDATA}/Code/User/settings.json" ;;
    *)       VSCODE_USER="" ;;
esac

CLI_USER="${HOME}/.claude/settings.json"
```

When reporting their contents, **extract only the relevant keys**:
- CLI user: `permissions.defaultMode`, `permissions.allow`, `permissions.deny`
- VSCode user: any key starting with `claudeCode.`

Never print the full file. Redact everything else to `(other keys redacted)`.

### Step 2: Compute resolved state

The resolved `defaultMode` is the value from the highest-precedence layer that sets it. Report:

- Which layer won the `defaultMode` contest.
- Merged `allow` list (union across CLI tiers).
- Merged `deny` list (union; any `deny` blocks the action even if allowed elsewhere).
- Whether VSCode says `bypass` but CLI says otherwise (or vice versa) — this is a legitimate conflict to flag.

### Step 3: Report runtime mode

The live in-session mode is exposed via the status line (see `.claude/scripts/statusline.sh`). Tell the user:

> "Your status line shows the current in-session mode in the top-right of the Claude Code panel. If that disagrees with the resolved `defaultMode` above, you (or Shift+Tab) overrode it mid-session. Press Shift+Tab to cycle back."

If the status line isn't configured, emit a warning and point at `.claude/scripts/statusline.sh`.

### Step 4: Flag common failure modes

Check for and explicitly call out:

1. **Layer drift:** CLI project says bypass but CLI local says default → local wins, explains the prompts.
2. **VSCode-only bypass:** VSCode layers say bypass but no CLI layer does → terminal Claude Code will still prompt; extension may or may not.
3. **Empty allowlist + default mode:** `defaultMode: "default"` with empty `allow` → every tool prompts, as designed.
4. **Stale session:** settings are correct but user reports prompts → almost always a session that pre-dates the fix. Advise "Cmd+Shift+P → Developer: Reload Window, then new Claude Code session."
5. **`deny` wins:** any match in a `deny` list blocks the tool regardless of `allow`. Rare but deadly.

## Output format

```
=== PERMISSION STATE ===

Layer 1 — VSCode user:       bypassPermissions      (allowDangerouslySkipPermissions: true)
Layer 2 — VSCode workspace:  bypassPermissions
Layer 3 — CLI user:          bypassPermissions      (allow: ["*"])
Layer 4 — CLI project:       bypassPermissions      (allow: ["Edit(**)", "Bash(*)", ...])
Layer 5 — CLI project-local: bypassPermissions      (allow: [...], deny: [])

Resolved defaultMode: bypassPermissions (set by Layer 5)
Merged allow:         Edit(**), Write(**), Bash(*), ...
Merged deny:          (none)

=== RUNTIME ===

Check the status line at the top of the Claude Code panel. Expected: [BYPASS].
If it shows [PROMPT], [AUTO-EDIT], or [PLAN] — that's an in-session override. Press Shift+Tab to cycle.

=== DIAGNOSIS ===

No layer drift detected. If you are still seeing prompts:
  1. Session is stale (started before settings were applied) — reload window + new session.
  2. VSCode extension bug — check extension version and file an issue.
  3. Tool was previously denied in this session — that denial is remembered. New session clears it.
```

If any layer disagrees, replace the "No layer drift detected" line with a specific flagged issue.

## Notes

- This skill is read-only. It never modifies settings.
- If `$CLAUDE_PROJECT_DIR` is unset, fall back to `git rev-parse --show-toplevel`.
- Platform-aware: detect macOS vs Linux vs Windows for the VSCode user path.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/permission-check/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>infra</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/permission-check/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/permission-check/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
