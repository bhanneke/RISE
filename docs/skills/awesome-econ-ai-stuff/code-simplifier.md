<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/code-simplifier.md -->

# `code-simplifier`

Streamlines and improves code clarity and consistency.

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
name: code-simplifier
description: Simplify and clean up code after changes are complete. Reduces complexity, improves readability, and ensures consistency.
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
  - python
  - readability
---

# Code Simplifier

Clean up and simplify code after making changes.

## When to Use

Run this skill after completing a feature or fix to ensure the code is clean, readable, and maintainable.

## Simplification Goals

### Reduce Complexity
- Break long functions into smaller, focused ones
- Reduce nesting depth (max 3 levels)
- Simplify complex conditionals
- Extract magic numbers to named constants

### Improve Readability
- Use descriptive variable and function names
- Add clarifying comments for non-obvious logic
- Ensure consistent formatting
- Remove unnecessary comments

### Apply Pythonic Patterns
- Use list/dict/set comprehensions where appropriate
- Use `with` statements for resource management
- Use `enumerate()` instead of manual indexing
- Use `zip()` for parallel iteration
- Use f-strings for formatting
- Use `pathlib` for file paths

### Clean Up
- Remove unused imports
- Remove unused variables
- Remove commented-out code
- Remove redundant code paths
- Consolidate duplicate logic

## Workflow

1. **Identify Changed Files**
   - Focus on files modified in the current session
   - Or specify files/directories as arguments

2. **Analyze Each File**
   - Check for simplification opportunities
   - Prioritize high-impact improvements

3. **Apply Simplifications**
   - Make incremental changes
   - Preserve original behavior
   - Run tests after each change

4. **Format and Lint**
   - Run `ruff format .`
   - Run `ruff check --fix .`

5. **Verify**
   - Run tests: `pytest`
   - Ensure behavior unchanged

## Arguments

Optionally specify files or directories to simplify.

Usage:
- `/code-simplifier` - Simplify recently changed files
- `/code-simplifier src/module.py` - Simplify specific file
- `/code-simplifier src/` - Simplify entire directory

## Example Transformations

Before:
```python
result = []
for i in range(len(items)):
    if items[i].is_valid == True:
        result.append(items[i].value)
```

After:
```python
result = [item.value for item in items if item.is_valid]
```

Before:
```python
if x != None:
    if y != None:
        if z != None:
            process(x, y, z)
```

After:
```python
if all(v is not None for v in (x, y, z)):
    process(x, y, z)
```


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/engineering/code-simplifier/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/engineering/code-simplifier/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/code-simplifier/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
