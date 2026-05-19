<!-- DO NOT EDIT — auto-copied from skills/clo-author/details/tools.md -->

# `tools`



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
name: tools
description: Utility commands — commit, compile, validate-bib, lint, journal, context-status, deploy, learn. Replaces individual utility skills.
argument-hint: "[subcommand: commit | compile | validate-bib | lint | journal | context | deploy | learn | upgrade] [args]"
allowed-tools: Read,Grep,Glob,Write,Edit,Bash,Task
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
- Create commit with descriptive message
- If quality score available and >= 80, note in commit

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

**What it does:**
1. Clone the latest clo-author release into a temp directory
2. Save the user's filled-in domain-profile.md and any custom journal profiles
3. Delete the old `.claude/` directory
4. Copy the new `.claude/` in
5. Restore the user's domain-profile.md and custom journal profiles
6. Optionally copy new `templates/`
7. Report what changed

**Workflow:**
```
Step 1: DOWNLOAD
  - Clone latest clo-author into /tmp/clo-author-upgrade
  - Or: gh release download --repo hugosantanna/clo-author

Step 2: PRESERVE USER CUSTOMIZATIONS
  - Save .claude/references/domain-profile.md if filled in (not just placeholders)
  - Save any custom journal profiles the user added to journal-profiles.md
  - Save .claude/settings.json (user's permissions and hooks)
  - Save .claude/settings.local.json if it exists

Step 3: REPLACE
  - Delete old .claude/ entirely
  - Copy new .claude/ from the downloaded release
  - Restore saved customizations from Step 2

Step 4: DO NOT TOUCH
  - paper/, scripts/, data/, explorations/, quality_reports/
  - CLAUDE.md, Bibliography_base.bib, README.md, .gitignore
  - Any other user content

Step 5: REPORT
  - List what was updated (new agents, skills, rules)
  - List what was preserved (domain profile, settings, custom profiles)
  - Clean up temp directory
```

**No git merge. No upstream remote. No conflicts.** Just delete and replace `.claude/`.

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


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/hugosantanna/clo-author/contents/.claude/skills/tools/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>hugosantanna/clo-author</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../clo-author.md">Clo-Author skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>none declared</dd>
<dt><b>Last update</b></dt><dd>2026-05-11</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/hugosantanna/clo-author">⭐ hugosantanna/clo-author</a><br><img src="https://img.shields.io/github/stars/hugosantanna/clo-author?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/hugosantanna/clo-author" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/clo-author/tools/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/clo-author.yml">edit on GitHub</a>.</p>
</div>

</div>
