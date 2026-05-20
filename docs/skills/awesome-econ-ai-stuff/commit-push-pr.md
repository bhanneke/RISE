<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/commit-push-pr.md -->

# `commit-push-pr`

Manages git workflows: commits, pushes, and pull request creation.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/engineering/commit-push-pr/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/commit-push-pr/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/engineering/commit-push-pr/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Commit, Push, and Create PR

Automate the git workflow for completing a feature or fix.

### Pre-computed Context

Before proceeding, gather this information:
- Current branch: `!git branch --show-current`
- Git status: `!git status --short`
- Recent commits on this branch: `!git log --oneline -5`
- Diff summary: `!git diff --stat`

### Workflow

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

### Arguments

Pass a commit message or leave empty for auto-generated message based on changes.

Usage: `/commit-push-pr [optional commit message]`

Example: `/commit-push-pr feat: add user authentication`

### Output

Return the PR URL when complete.
