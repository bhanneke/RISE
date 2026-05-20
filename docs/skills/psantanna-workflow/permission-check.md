<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/permission-check.md -->

# `/permission-check`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/permission-check/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/permission-check/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/permission-check/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Permission Check

### Purpose

Surface the full permission-mode picture across every layer Claude Code honors, so the user can see at a glance why prompts are (or aren't) firing. Claude Code resolves permission mode from a 6-tier stack; a single misconfigured layer produces silent overrides that are hard to debug by eye.

### The 6 layers (precedence: bottom wins)

1. **VSCode user settings** — `~/Library/Application Support/Code/User/settings.json` (macOS), `%APPDATA%/Code/User/settings.json` (Windows), `~/.config/Code/User/settings.json` (Linux). Key: `claudeCode.initialPermissionMode`.
2. **VSCode workspace settings** — `<repo>/.vscode/settings.json`. Same key. Wins over user.
3. **CLI user settings** — `~/.claude/settings.json`. Key: `permissions.defaultMode`.
4. **CLI project settings** — `<repo>/.claude/settings.json`. Same key. Wins over user.
5. **CLI project-local settings** — `<repo>/.claude/settings.local.json`. Same key. Wins over project.
6. **In-session mode** — set at session start from layers 1-5, then mutable via `Shift+Tab` or `/permission-mode`. Authoritative until session ends.

**Key insight:** `initialPermissionMode` only fires at session start. If you toggled mid-session (or the session started before a settings change), the file-level settings are correct but the *runtime* mode differs. That's the #1 source of "bypass isn't working" confusion.

### Privacy contract

Host-global settings files (`~/.claude/settings.json`, VSCode user settings) may contain:
- Paths to unrelated projects and secrets
- API keys, tokens, or provider credentials added outside this repo
- Permission policies set by the user's org or employer

This skill is designed for defense-in-depth: **Phase A runs automatically and reads only repo-local files.** Phase B reads host-global files **only after the user explicitly confirms** — never silently. When reporting host-global layers, redact any key that is not directly relevant to `permissions.*` or `claudeCode.*`.

### Protocol

#### Phase A: Repo-local layers (auto-runs)

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

#### Phase B: Host-global layers (requires explicit user confirmation)

If Phase A is inconclusive — e.g., all repo-local layers agree on bypass but the user is still being prompted — ask the user:

> "To complete the diagnosis, I need to read two files outside this repo:
> - `~/.claude/settings.json` (CLI user-level)
> - your VSCode user settings (`~/Library/Application Support/Code/User/settings.json` on macOS; Linux/Windows vary)
>
> These may contain unrelated paths or secrets. I will redact any key that isn't in `permissions.*` or `claudeCode.*`. Proceed?"

Only after the user confirms, read:

```bash
## VSCode user (platform-dependent path; try all three)
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

#### Step 2: Compute resolved state

The resolved `defaultMode` is the value from the highest-precedence layer that sets it. Report:

- Which layer won the `defaultMode` contest.
- Merged `allow` list (union across CLI tiers).
- Merged `deny` list (union; any `deny` blocks the action even if allowed elsewhere).
- Whether VSCode says `bypass` but CLI says otherwise (or vice versa) — this is a legitimate conflict to flag.

#### Step 3: Report runtime mode

The live in-session mode is exposed via the status line (see `.claude/scripts/statusline.sh`). Tell the user:

> "Your status line shows the current in-session mode in the top-right of the Claude Code panel. If that disagrees with the resolved `defaultMode` above, you (or Shift+Tab) overrode it mid-session. Press Shift+Tab to cycle back."

If the status line isn't configured, emit a warning and point at `.claude/scripts/statusline.sh`.

#### Step 4: Flag common failure modes

Check for and explicitly call out:

1. **Layer drift:** CLI project says bypass but CLI local says default → local wins, explains the prompts.
2. **VSCode-only bypass:** VSCode layers say bypass but no CLI layer does → terminal Claude Code will still prompt; extension may or may not.
3. **Empty allowlist + default mode:** `defaultMode: "default"` with empty `allow` → every tool prompts, as designed.
4. **Stale session:** settings are correct but user reports prompts → almost always a session that pre-dates the fix. Advise "Cmd+Shift+P → Developer: Reload Window, then new Claude Code session."
5. **`deny` wins:** any match in a `deny` list blocks the tool regardless of `allow`. Rare but deadly.

### Output format

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

### Notes

- This skill is read-only. It never modifies settings.
- If `$CLAUDE_PROJECT_DIR` is unset, fall back to `git rev-parse --show-toplevel`.
- Platform-aware: detect macOS vs Linux vs Windows for the VSCode user path.
