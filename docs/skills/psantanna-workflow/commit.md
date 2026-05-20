<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/commit.md -->

# `/commit`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/commit/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/commit/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/commit/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Commit, PR, and Merge

Stage changes, verify quality gates, commit with a descriptive message, create a PR, and merge to main.

### Steps

#### Step 0: Quality Gate (Pre-Commit)

**Run before branching.** For every changed `.qmd`, `.tex`, or `.R` file that has quality rubrics, run:

```bash
python3 scripts/quality_score.py <changed-file-paths>
```

- If any file scores below **80**, halt and report the findings. The user must either fix the issues or explicitly override with phrases like *"commit anyway"* or *"skip quality gate"*.
- If all files score 80+, continue.

Spawn the **verifier** agent (via `Task` with `subagent_type=verifier`) to run compilation/render checks on the changed files. Report pass/fail before committing.

#### Step 0b: Surface-Sync Gate (Pre-Commit)

**Runs unconditionally.** Enforces that count claims (`"14 agents, 28 skills, 24 rules, 6 hooks"` and siblings) across README.md, CLAUDE.md, the guide source + rendered HTML, the landing page, and the skill template all agree with the on-disk counts of `.claude/{skills,agents,rules,hooks}`:

```bash
./scripts/check-surface-sync.sh
```

- **Exit 0:** all counts consistent — continue.
- **Exit 1:** drift detected — print the diff and halt. Fix the stale counts, then re-run. Do NOT proceed past this gate on drift, even with "commit anyway" — the purpose is to catch the exact class of issue that produced PRs #70, #76, and #78.
- **Exit 2:** script error (missing surface file, unreadable directory) — investigate before proceeding.

#### Step 1: Check current state

```bash
git status
git diff --stat
git log --oneline -5
```

#### Step 2: Create a branch

```bash
git checkout -b <short-descriptive-branch-name>
```

#### Step 3: Stage files

Add specific files (never use `git add -A`):

```bash
git add <file1> <file2> ...
```

Do NOT stage `.claude/settings.local.json` or any files containing secrets.

#### Step 4: Commit with a descriptive message

If `$ARGUMENTS` is provided, use it as the commit message. Otherwise, analyze the staged changes and write a message that explains *why*, not just *what*.

```bash
git commit -m "$(cat <<'EOF'
<commit message here>
EOF
)"
```

#### Step 5: Push and create PR

```bash
git push -u origin <branch-name>
gh pr create --title "<short title>" --body "$(cat <<'EOF'
### Summary
<1-3 bullet points>

### Test plan
<checklist>

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

#### Step 6: Merge and clean up

```bash
gh pr merge <pr-number> --merge --delete-branch
git checkout main
git pull
```

#### Step 7: Report

Report the PR URL and what was merged.

### Important

- **Never skip Step 0.** Quality gates catch broken compilation, bad citations, and hardcoded paths before they reach `main`. If the user insists on skipping, record their override reason in the commit message.
- Always create a NEW branch — never commit directly to main.
- Exclude `settings.local.json` and sensitive files from staging.
- Use `--merge` (not `--squash` or `--rebase`) unless asked otherwise.
- If the commit message from `$ARGUMENTS` is provided, use it exactly.
