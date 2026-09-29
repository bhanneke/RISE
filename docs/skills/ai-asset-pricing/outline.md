<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/outline.md -->

# `/outline`

Analyses paper structure, reporting section balance, word counts and compliance with Cochrane's writing principles.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/outline/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/outline/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/outline/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Outline Skill

Review the current paper structure: section balance, word counts, Cochrane-principle compliance, and structural integrity.

### Examples
- `/outline` — full structural analysis of main.tex
- `/outline balance` — check section length balance only
- `/outline cochrane` — Cochrane-principle compliance check only

### Workflow

#### Step 1: Read Current Structure

1. Read `main.tex`
2. Extract all `\section{}`, `\subsection{}`, `\subsubsection{}` commands
3. Count lines and estimate words per section (between `%% BEGIN/END` markers)
4. Verify `%% BEGIN/END` markers are present and match registered keys

**Registered section keys**: Check the project's `CLAUDE.md` or `guidance/paper-context.md` for the section key registry. If neither exists, discover keys by scanning for `%% BEGIN:` markers in `main.tex`.

#### Step 2: Structural Analysis

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

#### Step 3: Project-Specific Structural Checks

If `guidance/paper-context.md` exists, run its registered structural checks. Common checks include:
- Are key figures/tables referenced in the introduction?
- Does the introduction enumerate all main contributions?
- Does the conclusion mention stated deliverables (data, code, packages)?
- Is the paper's terminology used consistently in section headers?

If no paper-context file exists, skip this step and note it in the output.

#### Step 4: Output

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
