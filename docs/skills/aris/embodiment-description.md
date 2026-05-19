<!-- DO NOT EDIT — auto-copied from skills/aris/details/embodiment-description.md -->

# `embodiment-description`



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
name: embodiment-description
description: "Write detailed embodiment descriptions for patent specifications. Use when user says \"撰写实施例\", \"write embodiment\", \"实施例描述\", \"detailed description\", or wants to describe how to practice an invention."
argument-hint: [claims-path-or-embodiment-details]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob
---

# Embodiment Description

Write detailed embodiments for: **$ARGUMENTS**

Embodiments describe HOW to make and use the invention -- they are the patent equivalent of experiment sections, but describe the invention rather than evaluating it empirically.

## Constants

- `MIN_EMBODIMENTS = 1` — At least one complete embodiment required
- `MAX_EMBODIMENTS = 3` — Practical limit; more embodiments strengthen enablement
- `EMBODIMENT_STYLE = detailed` — `detailed` (full working example) or `outline` (sketch)
- `REFERENCE_NUMERAL_PREFIX = 100` — Starting reference numeral for first figure's components

## Inputs

1. `patent/INVENTION_DISCLOSURE.md` — invention decomposition (core/supporting/optional features)
2. `patent/CLAIMS.md` — drafted claims that the embodiments must support
3. User-provided figures (if any) in any directory
4. `patent/figures/numeral_index.md` if it exists (from `/figure-description`)

## Workflow

### Step 1: Plan Embodiments

For each claim category (method, system, etc.), plan at least one embodiment:

| Embodiment | Covers Claims | Type | Key Variations |
|-----------|--------------|------|----------------|
| 1 | Claims 1, X | Best mode / preferred | [primary implementation] |
| 2 | Claims 2, 3 | Alternative | [different parameters/materials] |
| 3 | Claims 4, 5 | Additional alternative | [different configuration] |

### Step 2: Write Each Embodiment

For each embodiment, write a detailed description following this structure:

**Opening paragraph**:
"In one embodiment, [invention summary with reference to what is being described]."

**Component/step-by-step description**:

For method embodiments:
- Describe each step in order
- Reference figure numerals: "As shown in FIG. 1, at step 202, the processor 102 receives the input data 104..."
- Include specific parameters, ranges, and conditions
- Describe what happens at each decision point

For system/apparatus embodiments:
- Describe each component
- Reference figure numerals: "Referring to FIG. 1, the system 100 comprises a processor 102, a memory 104, and a communication interface 106..."
- Describe interconnections between components
- Describe operation of the system step-by-step

**Variations and alternatives**:
- "In some embodiments, the processor 102 may be a GPU, an FPGA, or an ASIC."
- "In another embodiment, the memory 104 may be replaced with a distributed storage system."
- "The parameters described above are exemplary; other values within the range [X, Y] are also contemplated."

These variations are critical -- they support broader claim interpretation.

### Step 3: Reference Numeral Integration

Ensure consistent reference numeral usage:

1. Every component mentioned must have a numeral
2. Numeral must appear first in parentheses after the component name: "the processor (102)"
3. Subsequent references: "the processor 102" (no parentheses)
4. Numbering follows figure series: 100-series for FIG. 1, 200-series for FIG. 2

**Format**:
- First mention: "the processor (102)"
- Later in same embodiment: "the processor 102"
- Cross-figure: "the processor 102 (shown in both FIG. 1 and FIG. 2)"

### Step 4: Claim Support Verification

For each claim element, verify it appears in at least one embodiment:

| Claim Element | Embodiment | Reference Numeral | Description Paragraph |
|---------------|-----------|-------------------|----------------------|
| [element] | [which] | [numeral] | [paragraph reference] |

If any claim element lacks embodiment support, add the necessary description.

### Step 5: Software/Algorithm Embodiments (if applicable)

For method/software inventions, include:
- Pseudocode or algorithmic description (NOT actual code)
- Flowchart description tied to figures
- Data structure descriptions
- Interface specifications

Example:
```
In one embodiment, the method comprises the following steps:
At step 202, the processor 102 receives input data from the input device 108.
At step 204, the processor 102 extracts feature vectors from the input data using a convolutional neural network.
At step 206, the processor 102 applies the attention mechanism 110 to the feature vectors...
```

### Step 6: Output

Embodiment sections are written to `patent/specification/detailed_description.md` (or appended to the specification structure).

Each embodiment section should be self-contained but cross-reference other embodiments when describing alternatives.

## Key Rules

- Embodiments must teach a POSITA to make and use the invention without undue experimentation.
- Include at least one "best mode" embodiment (US requirement).
- Multiple embodiments strengthen the specification against enablement challenges.
- Describe the invention, do NOT evaluate it empirically ("The embodiment achieves 95% accuracy" is wrong; "The processor classifies the input data" is correct).
- **CRITICAL — NO experimental data, test results, accuracy percentages, detection rates, precision values, or comparative performance data.** These belong in papers, not patents. The embodiment teaches HOW to make and use, not HOW WELL it performs.
- WRONG: "传感器对直径超过150μm的金属颗粒实现了100%的检测精度，即使在检测限处仍保持94%的高精度。"
- RIGHT: "当不锈钢颗粒通过间隙传感区域时，谐振频率下降。颗粒直径越大，频率偏移幅度越大。"
- Do NOT include tables of experimental results, graphs of measurement data, or comparisons with prior art performance.
- **CRITICAL — An embodiment is NOT an experiment.** Do NOT describe "repeated experiments", "accuracy evaluation", "precision testing", "calibration experiments", or "comparison with reference methods". An embodiment describes ONE way to make and use the invention — it is a recipe, not a test report.
- Do NOT copy experimental sections from source papers verbatim. Transform the experimental setup into a manufacturing/operation description.
- If the source material is a paper, extract ONLY: (1) what was built, (2) what materials/parameters were used, (3) how it operates. Ignore all test methodology, results, and performance metrics.
- Include specific parameters where possible, but frame them as exemplary, not limiting.
- Reference numerals must be consistent with the figures.
- Do NOT use subjective language ("excellent", "surprising", "superior").


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/embodiment-description/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/embodiment-description/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
