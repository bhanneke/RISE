<!-- DO NOT EDIT — auto-copied from skills/aris/details/figure-description.md -->

# `figure-description`



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
name: figure-description
description: "Process user-provided patent figures and generate formal drawing descriptions. Use when user says \"附图处理\", \"figure description\", \"附图说明\", \"drawings description\", or wants to describe patent figures with reference numerals."
argument-hint: [figure-directory-or-figure-list]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Figure Description for Patents

Process patent figures and generate drawing descriptions based on: **$ARGUMENTS**

Unlike `/paper-figure` which generates data plots, this skill processes user-provided technical diagrams and assigns reference numerals.

## Constants

- `FIGURE_DIR = "patent/figures/"` — Output directory for figure descriptions
- `REFERENCE_NUMERAL_PREFIX = 100` — Starting numeral for first figure's components
- `NUMERAL_SERIES = 100` — Each figure uses a separate 100-series (Fig 1: 100-199, Fig 2: 200-299, etc.)

## Inputs

1. User-provided figures (PNG, JPG, SVG, PDF) — search for them in the project directory
2. `patent/INVENTION_DISCLOSURE.md` — for understanding what components to identify
3. `patent/CLAIMS.md` — for mapping numerals to claim elements

## Workflow

### Step 1: Discover Figures

1. Search the project directory for figure files:
   - Check `patent/figures/`, `figures/`, root directory
   - Look for PNG, JPG, SVG, PDF files
   - Check INVENTION_BRIEF.md or INVENTION_DISCLOSURE.md for figure references
2. List all discovered figures with their paths
3. If figures are missing that claims require, note them as `[MISSING: description needed]`

### Step 2: Analyze Each Figure

For each figure found:

1. **Read the image** using the Read tool (supports image files)
2. **Identify components**: What labeled or visually distinct components are shown?
3. **Identify connections**: How do components relate to each other?
4. **Identify flow**: If it's a flowchart or sequence, what is the step order?

### Step 3: Assign Reference Numerals

For each figure, assign numerals using the series convention:

| Figure | Numeral Range |
|--------|-------------|
| FIG. 1 | 100-199 |
| FIG. 2 | 200-299 |
| FIG. 3 | 300-399 |

For each identified component:
- Assign the next available numeral in the series
- Cross-reference to the claim elements it supports
- Note if a component appears in multiple figures (use same numeral across figures)

### Step 4: Generate Drawing Descriptions

Write formal drawing descriptions (附图说明):

**For CN jurisdiction (Chinese)**:
```
图1是[发明名称]的系统结构示意图；
图2是[发明名称]的方法流程图；
图3是[具体组件]的详细结构示意图；
```

**For US/EP jurisdiction (English)**:
```
FIG. 1 is a block diagram illustrating the system architecture according to one embodiment;
FIG. 2 is a flowchart illustrating the method steps according to one embodiment;
FIG. 3 is a detailed view of the processing module of FIG. 1;
```

### Step 5: Generate Reference Numeral Index

Create a complete mapping:

```markdown
## Reference Numeral Index

| Numeral | Component Name | Figure(s) | Claim Element |
|---------|---------------|-----------|---------------|
| 100 | System | FIG. 1 | Claim X preamble |
| 102 | Processor | FIG. 1 | Claim X, element 1 |
| 104 | Memory | FIG. 1 | Claim X, element 2 |
| 106 | Communication bus | FIG. 1 | Claim X, element 3 |
| 200 | Method | FIG. 2 | Claim 1 preamble |
| 202 | Receiving step | FIG. 2 | Claim 1, step 1 |
| 204 | Processing step | FIG. 2 | Claim 1, step 2 |
```

### Step 6: Cross-Reference to Claims

Verify that every claim element has at least one reference numeral:

| Claim Element | Figure | Numeral | Status |
|---------------|--------|---------|--------|
| [element] | [which fig] | [numeral] | Covered / [MISSING] |

If any claim element has no corresponding figure or numeral, flag it:
- `[MISSING FIGURE: Need a diagram showing {element description}]`
- `[MISSING NUMERAL: Component {name} in figure {X} needs a numeral]`

### Step 7: Output

Write `patent/figures/figure_descriptions.md`:
```markdown
## Figure Descriptions

### FIG. 1 — [Description]
[Formal one-paragraph description with all reference numerals]

### FIG. 2 — [Description]
[Formal one-paragraph description with all reference numerals]
...
```

Write `patent/figures/numeral_index.md`:
```markdown
## Reference Numeral Index

[Complete table of all numerals, components, figures, and claim mappings]
```

## Key Rules

- Every component in every figure must have a reference numeral.
- Every reference numeral must be explained in the specification.
- Numeral series must be consistent: 100-series for FIG. 1, 200-series for FIG. 2.
- If the same component appears in multiple figures, use the SAME numeral.
- Do NOT modify user-provided figures -- only describe them.
- Flag missing figures that the claims require but the user has not provided.
- Drawing descriptions are one sentence each, in a consistent format.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/figure-description/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>figures</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/figure-description/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
