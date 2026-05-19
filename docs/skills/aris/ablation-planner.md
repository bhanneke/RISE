<!-- DO NOT EDIT — auto-copied from skills/aris/details/ablation-planner.md -->

# `ablation-planner`



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
name: ablation-planner
description: Use when main results pass result-to-claim (claim_supported=yes or partial) and ablation studies are needed for paper submission. Codex designs ablations from a reviewer's perspective, CC reviews feasibility and implements.
argument-hint: [method-description-or-claim]
allowed-tools: Bash(*), Read, Grep, Glob, Write, Edit, mcp__codex__codex, mcp__codex__codex-reply
---

# Ablation Planner

Systematically design ablation studies that answer the questions reviewers will ask. Codex leads the design (reviewer perspective), CC reviews feasibility and implements.

## Context: $ARGUMENTS

## When to Use

- Main results pass `/result-to-claim` with claim_supported = yes or partial
- User explicitly requests ablation planning
- `/auto-review-loop` reviewer identifies missing ablations

## Workflow

### Step 1: Prepare Context

CC reads available project files to build the full picture:
- Method description and components (from docs/research_contract.md or project CLAUDE.md)
- Current experiment results (from EXPERIMENT_LOG.md, EXPERIMENT_TRACKER.md, or W&B)
- Confirmed and intended claims (from result-to-claim output or project notes)
- Available compute resources (from CLAUDE.md server config, if present)

### Step 2: Codex Designs Ablations

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "xhigh"}
  prompt: |
    You are a rigorous ML reviewer planning ablation studies.
    Given this method and results, design ablations that:

    1. Isolate the contribution of each novel component
    2. Answer questions reviewers will definitely ask
    3. Test sensitivity to key hyperparameters
    4. Compare against natural alternative design choices

    Method: [description from project files]
    Components: [list of removable/replaceable components]
    Current results: [key metrics from experiments]
    Claims: [what we claim and current evidence]

    For each ablation, specify:
    - name: what to change (e.g., "remove module X", "replace Y with Z")
    - what_it_tests: the specific question this answers
    - expected_if_component_matters: what we predict if the component is important
    - priority: 1 (must-run) to 5 (nice-to-have)

    Also provide:
    - coverage_assessment: what reviewer questions these ablations answer
    - unnecessary_ablations: experiments that seem useful but won't add insight
    - suggested_order: run order optimized for maximum early information
    - estimated_compute: total GPU-hours estimate
```

### Step 3: Parse Ablation Plan

Normalize Codex response into structured format:

```markdown
## Ablation Plan

### Component Ablations (highest priority)
| # | Name | What It Tests | Expected If Matters | Priority |
|---|------|---------------|---------------------|----------|
| 1 | remove module X | contribution of X | performance drops on metric Y | 1 |
| 2 | replace X with simpler Z | value of learned vs fixed | drops, especially on dataset A | 2 |

### Hyperparameter Sensitivity
| # | Parameter | Values to Test | What It Tests | Priority |
|---|-----------|---------------|---------------|----------|
| 3 | lambda | [0.01, 0.1, 1.0] | sensitivity to regularization | 3 |

### Design Choice Comparisons
| # | Name | What It Tests | Priority |
|---|------|---------------|----------|
| 4 | joint vs separate matching | whether joint adds value | 4 |

### Coverage Assessment
[What reviewer questions these ablations answer]

### Unnecessary Ablations
[Experiments that seem useful but won't add insight — skip these]

### Run Order
[Optimized for maximum early information]

### Estimated Compute
[Total GPU-hours]
```

### Step 4: CC Reviews Feasibility

Before running anything, CC checks:
- Compute budget: can we afford all ablations with available GPUs?
- Code changes: which ablations need code modifications vs config-only changes?
- Dependencies: which ablations can run in parallel?
- Cuts: if budget is tight, propose removing lower-priority ablations and ask Codex to confirm

### Step 5: Implement and Run

1. Create configs/scripts for each ablation (config-only changes first)
2. Smoke test each ablation before full run
3. Run in suggested order, using descriptive names (e.g., `ablation-no-module-X`)
4. Track results in EXPERIMENT_LOG.md
5. After all ablations complete → update findings.md with insights

## Rules

- **Codex leads the design. CC does not pre-filter or bias the ablation list** before Codex sees it. Codex thinks like a reviewer; CC thinks like an engineer.
- Every ablation must have a clear `what_it_tests` and `expected_if_component_matters`. No "just try it" experiments.
- Config-only ablations take priority over those needing code changes (faster, less error-prone).
- If total compute exceeds budget, CC proposes cuts and asks Codex to re-prioritize — don't silently drop ablations.
- Component ablations (remove/replace) take priority over hyperparameter sweeps.
- Do not generate ablations for components identical to the baseline (no-op ablations).
- Record all ablation results in EXPERIMENT_LOG.md, including negative results (component removal had no effect = important finding).


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/ablation-planner/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>design</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>research-design</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/ablation-planner/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
