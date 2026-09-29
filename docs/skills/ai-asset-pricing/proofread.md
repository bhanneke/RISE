<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/proofread.md -->

# `/proofread`

Mechanical scan for typos, LaTeX formatting slips, punctuation and spacing.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>editing</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-11</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/proofread/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/proofread/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/proofread/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Proofread Skill

Scan for mechanical errors that `/style-check` does not cover: typos, LaTeX formatting issues, punctuation around equations, and spacing problems.

### Examples
- `/proofread` -- proofread the main .tex file
- `/proofread introduction` -- proofread only the introduction section
- `/proofread path/to/file.tex` -- proofread a specific file

### Input

The user provides an optional section key, file path, or line range. If omitted, scan the project's main `.tex` file.

### Workflow

#### Step 1: Extract Target Text
- If a section key is given, extract that section using `%% BEGIN/END` markers
- If a file path is given, read that file
- If no argument, read the main `.tex` file
- Note line numbers for all findings

#### Step 2: Spelling & Typo Scan
Search for common typos in prose and math-adjacent text:
- Misspelled words (e.g., "componet", "assigment", "misraking")
- Doubled words ("the the", "is is")
- Common academic misspellings ("accomodate", "occurence", "seperate", "consistant")
- Wrong word usage ("it's" for possessive, "affect/effect" confusion)

#### Step 3: LaTeX Formatting
Check for formatting issues:
- `\ref{eq:...}` where `\eqref{eq:...}` should be used (equation references)
- Missing non-breaking space: `Eq.\eqref` should be `Eq.~\eqref`
- Same for: `Table\ref` -> `Table~\ref`, `Figure\ref` -> `Figure~\ref`, `Section\ref` -> `Section~\ref`
- `Eq,~` instead of `Eq.~` (comma vs period)
- Inconsistent `\citet` vs `\cite` usage
- Unclosed braces or environments

#### Step 4: Spacing Issues
- Double spaces in prose (outside of LaTeX commands)
- Missing space after period (except in abbreviations like "e.g." or "i.e.")
- Tab/space mixing in indentation
- Trailing whitespace on lines

#### Step 5: Equation Punctuation
For displayed equations (`\[...\]`, `equation`, `align`):
- Check trailing punctuation: equations ending sentences need a period, mid-sentence need a comma
- Consistent punctuation style across the paper

#### Step 6: Capitalization
- Section/subsection titles: check for consistent capitalization style
- "Theorem", "Lemma", "Proposition" capitalized when used as proper nouns with numbers
- "equation" lowercase when used generically, but "Eq." when followed by a reference

#### Step 7: Output

```
PROOFREAD REPORT
================

File: [filename]
Scope: [section or full file]
Lines scanned: [count]

TYPOS: [N found]
- Line 109: "componet" -> "component"

LATEX FORMATTING: [N found]
- Line 153: "Eq,~\eqref" -> "Eq.~\eqref" (comma should be period)
- Line 245: "\ref{eq:delay}" -> "\eqref{eq:delay}" (equation reference)

SPACING: [N found]
- Line X: double space between "the  signal"

EQUATION PUNCTUATION: [N found]
- Line X: displayed equation ends sentence but has no period

CAPITALIZATION: [N found]
- Line X: "theorem 1" -> "Theorem 1"

SUMMARY:
- Total mechanical errors: N
- Typos: A
- LaTeX formatting: B
- Spacing: C
- Punctuation: D
- Capitalization: E
```
