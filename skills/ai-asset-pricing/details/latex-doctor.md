---
name: latex-doctor
description: Clean and fix .tex files -- strip comments, fix compilation errors, verify section markers
---

# LaTeX Doctor Skill

The "clean room" skill. Run to get a `.tex` file into a consistent, compilable state with verified section markers.

## Examples
- `/latex-doctor` -- full cleanup of the main .tex file
- `/latex-doctor comments` -- only strip comments
- `/latex-doctor markers` -- only verify section markers
- `/latex-doctor compile` -- only fix compilation issues
- `/latex-doctor path/to/file.tex` -- clean a specific file

## Workflow

### Step 1: Initial Compile

1. Run the compile command (use pdflatex/bibtex paths from canonical local state reported by `tools/bootstrap.py audit`, or a repo-root compatibility shim if present):
   ```bash
   cd {latex_dir} && pdflatex -interaction=nonstopmode {file} && bibtex {stem} && pdflatex -interaction=nonstopmode {file} && pdflatex -interaction=nonstopmode {file}
   ```
2. Parse the log for:
   - **Errors**: count and categorize (missing packages, undefined commands, etc.)
   - **Warnings**: overfull/underfull hbox, missing references, font warnings
3. Report: "Current state: N errors, M warnings"

### Step 2: Comment Cleanup

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

### Step 3: Verify Section Markers

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

### Step 4: Compilation Fixes

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

### Step 5: Warning Reduction

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

### Step 6: Recompile and Report

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
