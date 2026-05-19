<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/techdebt.md -->

# `techdebt`

Identifies and resolves code quality issues and maintenance concerns.

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
name: techdebt
description: Find and fix technical debt including duplicated code, dead code, outdated patterns, and code smells. Run at the end of sessions to clean up.
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
  - refactoring
  - code-quality
  - maintenance
---

# Technical Debt Finder

Identify and fix technical debt in the codebase.

## What to Look For

### Code Duplication
- Functions with similar logic that could be consolidated
- Copy-pasted code blocks
- Repeated patterns that should be abstracted

### Dead Code
- Unused imports
- Unused functions or classes
- Commented-out code blocks
- Unreachable code paths

### Outdated Patterns
- Deprecated API usage
- Old-style string formatting (% or .format) vs f-strings
- Type hints using `typing.List` instead of `list`
- Missing type hints on public functions

### Code Smells
- Functions longer than 50 lines
- Too many parameters (more than 5)
- Deep nesting (more than 3 levels)
- Magic numbers without constants
- Overly complex conditionals

### Missing Best Practices
- Missing docstrings on public functions
- Missing error handling
- Hardcoded values that should be config
- Missing tests for critical paths

## Workflow

1. **Scan the Codebase**
   - Look for patterns matching the issues above
   - Prioritize by impact and ease of fix

2. **Report Findings**
   - List issues by category
   - Include file paths and line numbers
   - Estimate severity (high/medium/low)

3. **Fix Issues**
   - Start with high-severity, easy fixes
   - Create atomic commits for each fix
   - Run tests after each change

4. **Verify**
   - Run linter: `ruff check .`
   - Run tests: `pytest`
   - Ensure no new issues introduced

## Arguments

Optionally specify a directory or file to focus on.

Usage:
- `/techdebt` - Scan entire project
- `/techdebt src/` - Scan specific directory
- `/techdebt src/utils.py` - Scan specific file

## Output

Provide a summary of:
- Issues found (by category)
- Issues fixed
- Remaining items for future sessions


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/engineering/techdebt/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>meleantonio/awesome-econ-ai-stuff</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../awesome-econ-ai-stuff.md">awesome-econ-ai-stuff (Antonio Mele)</a></dd>
<dt><b>Category</b></dt><dd><code>code-gen</code></dd>
<dt><b>Field</b></dt><dd>general</dd>
<dt><b>Pipeline stages</b></dt><dd><code>code-generation</code></dd>
<dt><b>License</b></dt><dd>Other (see repo)</dd>
<dt><b>Last update</b></dt><dd>2026</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff">⭐ meleantonio/awesome-econ-ai-stuff</a><br><img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/engineering/techdebt/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/techdebt/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
