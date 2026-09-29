---
name: outline
description: Analyze paper structure — section balance, word counts, Cochrane-principle compliance
user_invocable: true
---

# Outline Skill

Review the current paper structure: section balance, word counts, Cochrane-principle compliance, and structural integrity.

## Examples
- `/outline` — full structural analysis of main.tex
- `/outline balance` — check section length balance only
- `/outline cochrane` — Cochrane-principle compliance check only

## Workflow

### Step 1: Read Current Structure

1. Read `main.tex`
2. Extract all `\section{}`, `\subsection{}`, `\subsubsection{}` commands
3. Count lines and estimate words per section (between `%% BEGIN/END` markers)
4. Verify `%% BEGIN/END` markers are present and match registered keys

**Registered section keys**: Check the project's `CLAUDE.md` or `guidance/paper-context.md` for the section key registry. If neither exists, discover keys by scanning for `%% BEGIN:` markers in `main.tex`.

### Step 2: Structural Analysis

**Section Presence**:
- Verify all expected body sections are present (based on registered keys or discovered markers)
- Verify appendices are present if referenced in the body
- Flag any sections that appear in `main.tex` but are not in the registered key list

**Section Balance**:
- Flag sections that are >2x the average body-section length
- Flag sections that are <0.25x the average body-section length
- Introduction target: ~3 pages (Cochrane)
- Conclusion target: ~1--2 paragraphs

**Organization (Cochrane Principles)**:
- Is the main result presented as early as possible?
- Is there anything before the main result that a reader doesn't need?
- Are robustness checks in the appendix (not cluttering the body)?
- Is the literature review AFTER the contribution (not before)?

### Step 3: Project-Specific Structural Checks

If `guidance/paper-context.md` exists, run its registered structural checks. Common checks include:
- Are key figures/tables referenced in the introduction?
- Does the introduction enumerate all main contributions?
- Does the conclusion mention stated deliverables (data, code, packages)?
- Is the paper's terminology used consistently in section headers?

If no paper-context file exists, skip this step and note it in the output.

### Step 4: Output

```
PAPER OUTLINE
=============

Title: [from \title{} command in main.tex]

Current Structure:
  1. [Section name] (key: [key]) — N lines, ~M words
  2. [Section name] (key: [key]) — N lines, ~M words
  ...
  ---
  A. [Appendix name] (key: [key]) — N lines, ~M words
  ...

Total body: ~W words (~P pages at 250 words/page)
Total with appendices: ~W' words

Section Balance:
  Average body section: ~N words
  Longest: [section] (M words, Xx average)
  Shortest: [section] (M words, Xx average)

Cochrane Check:
  [x] Main result in first half of paper
  [x] Literature review after contribution
  [x] Robustness in appendix
  [ ] Introduction exceeds 3-page target (currently ~P pages)

Project-Specific Checks:
  [x] [check description]
  [ ] [any issues found]
  (or: "No paper-context.md found — skipping project-specific checks")

Section Markers:
  N/N sections have valid %% BEGIN/END markers
  [any marker issues]
```
