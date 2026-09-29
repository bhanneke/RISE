<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/build-context.md -->

# `/build-context`

Builds a paper-context file from the user's .tex, .md or .pdf drafts, recording abstract, key results, terminology, sample, section structure, labels and key citations for later writing and audit skills.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/build-context/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/build-context/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/build-context/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Build Context Skill

Generate a structured `guidance/paper-context.md` file that captures everything Claude needs to know about a paper before writing, editing, or auditing it. This file is consumed by `/audit-section`, `/check-consistency`, `/edit-section`, `/full-paper-audit`, `/audit-captions`, and other writing skills.

### Examples
- `/build-context main.tex` -- build context from the paper's LaTeX source
- `/build-context draft.pdf` -- build context from a PDF of the paper
- `/build-context notes.md main.tex` -- combine author notes with LaTeX source
- `/build-context related_paper.pdf` -- extract context from a related paper for reference
- `/build-context` -- scan for main.tex or .pdf files in the current project and ask which to use

### Input

One or more file paths. Supported formats:
- `.tex` -- LaTeX source (richest; extracts section structure, labels, equations, citations)
- `.pdf` -- PDF file (read with the Read tool; extracts prose content and structure)
- `.md` -- Markdown notes (author's own description of the paper, key results, terminology)

If no arguments are provided, scan the current project directory for `main.tex` or `*.pdf` files and prompt the user to select.

### Workflow

#### Step 1: Read Source Files
1. Read each provided file
2. For `.tex`: extract the full document
3. For `.pdf`: read the PDF (use pages parameter for large files; start with first 10 pages, then continue if needed)
4. For `.md`: read as-is (these are usually the author's own notes)

#### Step 2: Extract Paper Identity
From the source material, identify:
- **Title**: from `\title{}` or document header
- **Authors**: from `\author{}` or byline
- **Abstract**: from `\begin{abstract}` or first section
- **Core contribution**: 1-3 sentences summarizing what the paper does that is new

#### Step 3: Extract Key Results
Identify the paper's main quantitative and qualitative findings:
- **Primary results**: the headline findings (with specific numbers if available)
- **Secondary results**: supporting findings
- **Robustness**: what robustness checks are performed
- **Null results**: any important non-findings

For each result, record:
- The claim as stated in the paper
- The specific numbers (magnitudes, t-statistics, confidence intervals)
- Which table/figure reports it

#### Step 4: Extract Terminology
Build a terminology table:
- **Preferred terms**: the paper's canonical names for its concepts, methods, variables
- **Deprecated terms**: informal or older names that should not be used
- **Abbreviations**: all abbreviations and their definitions

Format as:

```markdown
| Preferred | Avoid | Notes |
|-----------|-------|-------|
| [correct term] | [incorrect/informal term] | [context] |
```

#### Step 5: Extract Structure
If working from `.tex`, record:
- **Section keys**: all `%% BEGIN:<key>` / `%% END:<key>` markers found
- **Key labels**: important `\label{}`s for tables, figures, equations, theorems
- **Section summaries**: 1-sentence summary of each section's content

#### Step 6: Extract Sample Description
- Date range of the sample
- Number of observations (cross-sectional units, time periods)
- Data sources
- Key filters or sample construction choices

#### Step 7: Extract Citation Context
Identify the paper's most important citations:
- Papers it builds directly on
- Papers it contrasts with
- Methodological references

#### Step 8: Write paper-context.md

Write the file to `guidance/paper-context.md` (creating the `guidance/` directory if needed). Use this template:

```markdown
## Paper Context

Generated by `/build-context` on [date]. Source files: [list].

### Identity

- **Title**: [title]
- **Authors**: [authors]
- **Core contribution**: [1-3 sentences]

### Abstract

[abstract text]

### Key Results

#### Primary
1. [Result]: [magnitude] ([table/figure reference])
2. ...

#### Secondary
1. ...

#### Null Results
1. ...

### Terminology

| Preferred | Avoid | Notes |
|-----------|-------|-------|
| ... | ... | ... |

### Abbreviations

| Abbreviation | Definition |
|-------------|------------|
| ... | ... |

### Sample

- **Period**: [start] to [end]
- **Observations**: [count] ([unit])
- **Sources**: [data sources]
- **Key filters**: [any important sample restrictions]

### Section Structure

| Key | Section Title | Summary |
|-----|--------------|---------|
| `introduction` | Introduction | ... |
| ... | ... | ... |

### Key Labels

- Tables: [list of table labels]
- Figures: [list of figure labels]
- Equations: [list of key equation labels]

### Important Citations

- [Author (Year)]: [why it matters to this paper]
- ...
```

#### Step 9: Confirm with User
After writing, print:
1. The file path written
2. A summary of what was extracted
3. Any gaps marked `[HUMAN EDIT REQUIRED]` where information could not be determined from the source files

Ask the user to review and fill in any gaps.

### Integration

This file is consumed by:
- `/audit-section` (Step 3: factual accuracy cross-reference)
- `/check-consistency` (Step 1: canonical values)
- `/edit-section` (Step 2: correct claims and framing)
- `/full-paper-audit` (Step 3: cross-section consistency)
- `/audit-captions` (Step 5: terminology compliance)
- `/outline` (Step 3: project-specific structural checks)
- `/research` (Step 4/7: relevance assessment)

### Re-running

If the paper evolves, re-run `/build-context` to regenerate. The skill will overwrite the existing `guidance/paper-context.md`. The user should review the diff to ensure nothing important was lost.

### Edge Cases

- **Multiple papers in one project**: Name the context file after the paper (e.g., `guidance/paper-context-main.md`). Skills that read `guidance/paper-context.md` will use the default; the user can specify alternatives.
- **No source files found**: Report what was searched and suggest the user provide a file path explicitly.
- **PDF too large**: Read in chunks (10 pages at a time). Summarize each chunk, then synthesize.
- **Related paper (not the user's own)**: Generate context focused on what's relevant for reference — key findings, methodology, terminology. Mark clearly as "Reference paper context, not the project's own paper."
