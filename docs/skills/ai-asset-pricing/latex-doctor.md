<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/latex-doctor.md -->

# `/latex-doctor`

Cleans .tex files by stripping comments, fixing compile errors and checking section markers.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-24</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>dissemination</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/latex-doctor/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/latex-doctor/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/latex-doctor/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## LaTeX Doctor Skill

The "clean room" skill. Run to get a `.tex` file into a consistent, compilable state with verified section markers.

### Examples
- `/latex-doctor` -- full cleanup of the main .tex file
- `/latex-doctor comments` -- only strip comments
- `/latex-doctor markers` -- only verify section markers
- `/latex-doctor compile` -- only fix compilation issues
- `/latex-doctor path/to/file.tex` -- clean a specific file

### Workflow

#### Step 1: Initial Compile

1. Run the compile command (use pdflatex/bibtex paths from canonical local state reported by `tools/bootstrap.py audit`, or a repo-root compatibility shim if present):
   ```bash
   cd {latex_dir} && pdflatex -interaction=nonstopmode {file} && bibtex {stem} && pdflatex -interaction=nonstopmode {file} && pdflatex -interaction=nonstopmode {file}
   ```
2. Parse the log for:
   - **Errors**: count and categorize (missing packages, undefined commands, etc.)
   - **Warnings**: overfull/underfull hbox, missing references, font warnings
3. Report: "Current state: N errors, M warnings"

#### Step 2: Comment Cleanup

Scan the `.tex` file and remove unnecessary comments:

**REMOVE**:
- Lines that are 100% LaTeX comments (`% some old note`)
- Trailing inline comments (keep the code, strip the `% comment` part)
- Blocks of commented-out code (`% \begin{table}...% \end{table}`)

**PRESERVE** (never touch):
- `%% BEGIN key` and `%% END key` section markers
- `% !TeX` directives
- `%` inside `\url{}`, `\verb||`, or verbatim environments
- Comments that are clearly documentation (start with `%% NOTE:` or similar)

Report: "Removed N comment lines (K characters saved)"

#### Step 3: Verify Section Markers

Verify `%% BEGIN/END` markers for consistency.

1. Scan the `.tex` file for all `%% BEGIN key` and `%% END key` markers
2. If the project's `CLAUDE.md` defines registered section keys, cross-reference against them
3. Check for:
   - **Missing markers**: `\section{}` commands without `%% BEGIN/END` pairs
   - **Orphaned markers**: `%% BEGIN key` without matching `%% END key` (or vice versa)
   - **Unknown keys**: Markers with keys not in the registered list (if one exists)
   - **Ordering**: `%% END key` appears before the next `%% BEGIN key`
4. Fix any issues found, or flag for human review if ambiguous

Report: "Verified N markers. M issues found."

#### Step 4: Compilation Fixes

Address common compilation errors:

**Missing packages**:
- If `\usepackage{X}` is missing but commands from package X are used, add the `\usepackage` to the preamble
- Ask user before adding non-standard packages

**Undefined references**:
- List all `\ref{label}` where `\label{label}` does not exist
- Flag with line numbers but do NOT auto-fix

**Missing bibliography**:
- Check that the `.bib` file exists and is referenced
- Flag missing BibTeX keys (keys in `\cite{}` not in `.bib`)

**Orphaned labels**:
- Labels that exist (`\label{...}`) but are never referenced (`\ref{...}`)
- Note but do NOT auto-remove

#### Step 5: Warning Reduction

Address common warnings:

**Overfull \hbox**:
- Identify the offending lines from the log
- Suggest specific fix (reword, `\allowbreak`, adjust column width, `\resizebox`)
- Apply safe fixes automatically; flag complex cases for human review

**Underfull \hbox**:
- Usually less serious; identify and suggest fixes

**Missing references**:
- List with line numbers
- Note: "Run full compile cycle to resolve, or check for typos in label names"

Report: "Addressed N warnings. Reduced from M to K remaining."

#### Step 6: Recompile and Report

1. Run full compile cycle
2. Parse the new log
3. Generate final report:

```
LATEX DOCTOR REPORT
====================

File: [filename]

COMMENTS:
  Removed: N lines (K characters)
  Preserved: M marker/directive lines

SECTION MARKERS:
  Verified: N markers
  Issues: M issues found [list if any]

COMPILATION:
  Before: E errors, W warnings
  After:  E' errors, W' warnings
  Fixed:  [list of fixes applied]

REMAINING ISSUES:
  - [list of issues that need human attention]

STATUS: [CLEAN COMPILE / N ISSUES REMAINING]
```
