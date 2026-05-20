<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/techdebt.md -->

# `techdebt`

Identifies and resolves code quality issues and maintenance concerns.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-econ-ai-stuff/">awesome-econ-ai-stuff (Antonio Mele)</a></div><div><b>Category:</b> <code>code-gen</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>Other (see repo)</code></div><div><b>Updated:</b> 2026</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/engineering/techdebt/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/techdebt/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/engineering/techdebt/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Technical Debt Finder

Identify and fix technical debt in the codebase.

### What to Look For

#### Code Duplication
- Functions with similar logic that could be consolidated
- Copy-pasted code blocks
- Repeated patterns that should be abstracted

#### Dead Code
- Unused imports
- Unused functions or classes
- Commented-out code blocks
- Unreachable code paths

#### Outdated Patterns
- Deprecated API usage
- Old-style string formatting (% or .format) vs f-strings
- Type hints using `typing.List` instead of `list`
- Missing type hints on public functions

#### Code Smells
- Functions longer than 50 lines
- Too many parameters (more than 5)
- Deep nesting (more than 3 levels)
- Magic numbers without constants
- Overly complex conditionals

#### Missing Best Practices
- Missing docstrings on public functions
- Missing error handling
- Hardcoded values that should be config
- Missing tests for critical paths

### Workflow

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

### Arguments

Optionally specify a directory or file to focus on.

Usage:
- `/techdebt` - Scan entire project
- `/techdebt src/` - Scan specific directory
- `/techdebt src/utils.py` - Scan specific file

### Output

Provide a summary of:
- Issues found (by category)
- Issues fixed
- Remaining items for future sessions
