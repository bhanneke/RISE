---
name: tools
description: Utility commands — commit, compile, validate-bib, lint, journal, context-status, deploy, learn.
argument-hint: "[subcommand: commit | compile | validate-bib | lint | journal | context | dashboard | deploy | learn | upgrade] [args]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Agent,Task
---

# Tools

Utility subcommands for project maintenance and infrastructure.

**Input:** `$ARGUMENTS` — subcommand followed by any arguments.

---

## Subcommands

### `/tools dashboard [--open]` — Project Dashboard
Regenerate the project dashboard HTML file.

```bash
python3 scripts/generate_dashboard.py
```

If `--open` is specified (or by default), open the dashboard in the browser:
```bash
open project_dashboard.html
```

The dashboard scans the entire project — paper sections, data, scripts, quality reports, bibliography, plans — and renders an interactive HTML overview. Regenerate it after any significant work.

### `/tools commit [message]` — Git Commit
Stage changes, create commit, optionally create PR and merge.
- Run git status to identify changes
- Stage relevant files (never stage .env or credentials)
- Run `python3 scripts/score.py --gate commit`. If it fails, stop and report which components pull
  the score below 80. On a project nothing has scored yet it passes with a notice; say so and commit.
- Create commit with descriptive message; note the score when there is one
- The git pre-commit hook (`scripts/install-hooks.sh` installs it) runs scaffold integrity and lint
  checks on every commit, including ones made outside this skill

### `/tools compile [file]` — LaTeX Compilation
Automated multi-pass compilation via latexmk.

For papers:
```bash
cd paper && latexmk [file]
```

For talks:
```bash
cd paper/talks && latexmk [file]
```

Note: `paper/latexmkrc` configures XeLaTeX, TEXINPUTS, and BIBINPUTS. Falls back to manual 3-pass if latexmk is unavailable.

### `/tools validate-bib` — Bibliography Validation
Cross-reference all \cite{} keys in paper and talk files against Bibliography_base.bib.
Report: missing entries, unused entries, duplicate keys.

### `/tools lint [file|dir]` — Mechanical Code Linting
Run grep-based checks on R/Python/Julia scripts against the coding standards' prohibited patterns. Catches mechanical violations before the coder-critic's judgment review.

```bash
"$CLAUDE_PROJECT_DIR"/.claude/hooks/lint-scripts.sh [target]
```

- **Single file:** `/tools lint scripts/02_estimate.R`
- **Directory:** `/tools lint scripts/` (recursive)
- **Default:** `/tools lint` (lints `scripts/`)

**What it checks (drawn from `.claude/references/coding-standards-*.md`):**

| Check | R | Python | Julia | Severity |
|-------|---|--------|-------|----------|
| Absolute paths | x | x | x | HIGH |
| `setwd()` / `os.chdir()` / `cd()` | x | x | x | HIGH |
| Missing seed (stochastic code) | x | x | x | HIGH |
| `install.packages()` / `pip install` | x | x | | HIGH |
| `rm(list = ls())` | x | | | MEDIUM |
| `T`/`F` literals | x | | | MEDIUM |
| `sapply()` | x | | | MEDIUM |
| `attach()`/`detach()` | x | | | MEDIUM |
| `<<-` global assignment | x | | | MEDIUM |
| `stargazer` / `plyr` | x | | | MEDIUM |
| `set.seed()` position (after line 30) | x | | | MEDIUM |
| Wildcard imports | | x | | MEDIUM |
| `np.random.seed()` global state | | x | | MEDIUM |
| Bare `except:` | | x | | MEDIUM |
| `eval`/`@eval` runtime | | | x | MEDIUM |
| Late `library()`/`import`/`using` | x | x | x | LOW |
| `print()` for status | x | | | LOW |
| `require()` | x | | | LOW |
| `1:n` patterns | x | | | LOW |

**Output:** Findings by file with severity, line number, and fix suggestion. Always advisory (exit 0).

**When to use:**
- Before `/review --code` — catches mechanical violations instantly
- Before commits — quick sanity check
- The coder-critic focuses on judgment (strategy alignment, numerical plausibility, design); this catches the grep-able stuff

### `/tools journal` — Research Journal
Regenerate the research journal timeline from quality reports and git history.
Shows chronological record of agent actions, phase transitions, scores, decisions.

### `/tools context` — Context Status
Show current context status and session health.
Check context usage, whether auto-compact is approaching, what state will be preserved.

### `/tools deploy` — Deploy Guide Site
Render Quarto guide site and publish to GitHub Pages.
```bash
cd guide && quarto publish gh-pages --no-browser
```

### `/tools learn` — Extract Learnings
Extract reusable knowledge from the current session. Auto-memory handles corrections automatically; this is for multi-step workflows worth turning into a full skill.

### `/tools upgrade` — Upgrade Clo-Author Infrastructure
Upgrade an existing project to the latest clo-author architecture.

The scaffold is more than `.claude/`: the gates run from scripts in `scripts/`, the commit gate from
`.githooks/`. An upgrade that replaces only `.claude/` leaves skills calling scripts that are missing
or out of date. Show the user the plan below and wait for approval before deleting anything.

```
Step 1: DOWNLOAD
  - git clone --depth=1 https://github.com/hugosantanna/clo-author.git into a temp directory

Step 2: PRESERVE USER CUSTOMIZATIONS
  - .claude/references/domain-profile.md if filled in (not just placeholders)
  - custom journal profiles the user added to journal-profiles.md
  - .claude/settings.local.json (personal; restored as is)
  - from the OLD .claude/settings.json, only what the user added: allow entries missing from the
    new settings.json, and hooks whose command is not under .claude/hooks/. Do NOT restore the old
    file over the new one: it would bring back retired hooks (e.g. post-edit-lint.sh) and drop new
    fields such as the guards' "onFailure": "block".

Step 3: REPLACE THE SCAFFOLD
  - .claude/       delete and copy the new one; restore Step 2's files; put the user's added allow
                   entries and hooks into settings.local.json, not settings.json
  - scripts/       copy every top-level file from the release's scripts/ whose first lines carry
                   "clo-author: infrastructure", plus scripts/deepread_prompts/. Overwrite only
                   files that carry the marker in the user's copy too, or do not exist yet
  - .githooks/     copy, then run scripts/install-hooks.sh
  - paper/preambles/header.tex   copy only if the project has none
  - templates/     copy new files; ask before overwriting changed ones

Step 4: DO NOT TOUCH
  - user analysis code: scripts/R/, scripts/python/, any script without the marker
  - paper/ (except a missing header.tex), data/, explorations/, quality_reports/
  - CLAUDE.md, Bibliography_base.bib, README.md, .gitignore

Step 5: VERIFY AND REPORT
  - python3 scripts/check_scaffold.py and python3 scripts/test_hooks.py must pass
  - list what changed (agents, skills, rules, scripts), what was preserved, and where the user's
    old settings entries went; read the release's CHANGELOG.md entries since the old version
  - remove the temp directory
```

**No git merge. No upstream remote.** The user's analysis code is never overwritten: only files that
carry the infrastructure marker are replaced.

---

## Bundled Resources (Level 3)

| Resource | Path | When |
|----------|------|------|
| Gotchas | `gotchas.md` | Always — known failure points |

---

## Principles
- **Each subcommand is lightweight.** No multi-agent orchestration needed.
- **Compile uses latexmk.** Handles multi-pass and biber automatically.
- **validate-bib catches drift.** Run before commits to catch broken citations.
- **Upgrade preserves content.** Infrastructure changes, your paper doesn't.
