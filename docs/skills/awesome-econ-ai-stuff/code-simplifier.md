<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/code-simplifier.md -->

# `code-simplifier`

Streamlines and improves code clarity and consistency.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>code-gen</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/engineering/code-simplifier/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/code-simplifier/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/engineering/code-simplifier/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Code Simplifier

Clean up and simplify code after making changes.

### When to Use

Run this skill after completing a feature or fix to ensure the code is clean, readable, and maintainable.

### Simplification Goals

#### Reduce Complexity
- Break long functions into smaller, focused ones
- Reduce nesting depth (max 3 levels)
- Simplify complex conditionals
- Extract magic numbers to named constants

#### Improve Readability
- Use descriptive variable and function names
- Add clarifying comments for non-obvious logic
- Ensure consistent formatting
- Remove unnecessary comments

#### Apply Pythonic Patterns
- Use list/dict/set comprehensions where appropriate
- Use `with` statements for resource management
- Use `enumerate()` instead of manual indexing
- Use `zip()` for parallel iteration
- Use f-strings for formatting
- Use `pathlib` for file paths

#### Clean Up
- Remove unused imports
- Remove unused variables
- Remove commented-out code
- Remove redundant code paths
- Consolidate duplicate logic

### Workflow

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

### Arguments

Optionally specify files or directories to simplify.

Usage:
- `/code-simplifier` - Simplify recently changed files
- `/code-simplifier src/module.py` - Simplify specific file
- `/code-simplifier src/` - Simplify entire directory

### Example Transformations

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
