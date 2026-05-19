<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/commit-push-pr.md -->

# `commit-push-pr`

Manages git workflows: commits, pushes, and pull request creation.

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
name: commit-push-pr
description: Commit changes, push to remote, and create a pull request. Use for completing features or fixes ready for review.
workflow_stage: engineering
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
author: Awesome Econ AI Community
version: 1.0.0
disable-model-invocation: true
tags:
  - git
  - github
  - pull-request
---

# Commit, Push, and Create PR

Automate the git workflow for completing a feature or fix.

## Pre-computed Context

Before proceeding, gather this information:
- Current branch: `!git branch --show-current`
- Git status: `!git status --short`
- Recent commits on this branch: `!git log --oneline -5`
- Diff summary: `!git diff --stat`

## Workflow

1. **Review Changes**
   - Check `git status` for all modified/added files
   - Review the diff to understand what's being committed
   - Ensure no sensitive files are staged (.env, credentials, etc.)

2. **Run Pre-commit Checks**
   - Format code: `ruff format .` (if Python files changed)
   - Lint code: `ruff check .` (if Python files changed)
   - Run tests: `pytest` (if tests exist)

3. **Stage and Commit**
   - Stage relevant files: `git add <files>`
   - Create a commit with Conventional Commits format:
     - `feat:` for new features
     - `fix:` for bug fixes
     - `docs:` for documentation
     - `refactor:` for refactoring
     - `test:` for tests
     - `chore:` for maintenance
   - Write a clear, concise commit message focusing on "why"

4. **Push to Remote**
   - Push the branch: `git push -u origin HEAD`
   - If branch doesn't exist on remote, create it

5. **Create Pull Request**
   - Use GitHub CLI: `gh pr create`
   - Include:
     - Clear title summarizing the change
     - Description with summary and context
     - Reference any related issues
   - Add appropriate labels if applicable

## Arguments

Pass a commit message or leave empty for auto-generated message based on changes.

Usage: `/commit-push-pr [optional commit message]`

Example: `/commit-push-pr feat: add user authentication`

## Output

Return the PR URL when complete.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/engineering/commit-push-pr/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>meleantonio/awesome-econ-ai-stuff</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../awesome-econ-ai-stuff.md">awesome-econ-ai-stuff (Antonio Mele)</a></dd>
<dt><b>Category</b></dt><dd><code>infra</code></dd>
<dt><b>Field</b></dt><dd>general</dd>
<dt><b>License</b></dt><dd>Other (see repo)</dd>
<dt><b>Last update</b></dt><dd>2026</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff">⭐ meleantonio/awesome-econ-ai-stuff</a><br><img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/engineering/commit-push-pr/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/commit-push-pr/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
