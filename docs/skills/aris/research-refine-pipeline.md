<!-- DO NOT EDIT — auto-copied from skills/aris/details/research-refine-pipeline.md -->

# `research-refine-pipeline`



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
name: research-refine-pipeline
description: 'Run an end-to-end workflow that chains `research-refine` and `experiment-plan`. Use when the user wants a one-shot pipeline from vague research direction to focused final proposal plus detailed experiment roadmap, or asks to "串起来", build a pipeline, do it end-to-end, or generate both the method and experiment plan together.'
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Agent, mcp__codex__codex, mcp__codex__codex-reply
---

# Research Refine Pipeline: End-to-End Method and Experiment Planning

Refine and concretize: **$ARGUMENTS**

## Overview

Use this skill when the user does not want to stop at a refined method. The goal is to produce a coherent package that includes:

- a problem-anchored, elegant final proposal
- the review history explaining why the method is focused
- a detailed experiment roadmap tied to the paper's claims
- a compact pipeline summary that says what to run next

This skill composes two existing workflows:

1. `research-refine` for method refinement
2. `experiment-plan` for claim-driven validation planning

For stage-specific detail, read these sibling skills only when needed:

- `../research-refine/SKILL.md`
- `../experiment-plan/SKILL.md`

## Core Rule

Do not plan a large experiment suite on top of an unstable method. First stabilize the thesis. Then turn the stable thesis into experiments.

## Default Outputs

- `refine-logs/FINAL_PROPOSAL.md`
- `refine-logs/REVIEW_SUMMARY.md`
- `refine-logs/REFINEMENT_REPORT.md`
- `refine-logs/EXPERIMENT_PLAN.md`
- `refine-logs/EXPERIMENT_TRACKER.md`
- `refine-logs/PIPELINE_SUMMARY.md`

## Workflow

### Phase 0: Triage the Starting Point

- Extract the problem, rough approach, constraints, resources, and target venue.
- Check whether `refine-logs/FINAL_PROPOSAL.md` already exists and still matches the current request.
- If the proposal is missing, stale, or materially different from the current request, run the full `research-refine` stage.
- If the proposal is already strong and aligned, reuse it and jump to experiment planning.
- If in doubt, prefer re-running `research-refine` rather than planning experiments for the wrong method.

### Phase 1: Method Refinement Stage

Run the `research-refine` workflow and keep its V3 philosophy intact:

- preserve the Problem Anchor
- prefer the smallest adequate mechanism
- keep one dominant contribution
- modernize only when it improves the paper

Exit this stage only when these are explicit:

- the final method thesis
- the dominant contribution
- the complexity intentionally rejected
- the key claims and must-run ablations
- the remaining risks, if any

If the verdict is still `REVISE`, continue into experiment planning only if the remaining weaknesses are clearly documented.

### Phase 2: Planning Gate

Before the experiment stage, write a short gate check:

- What is the final method thesis?
- What is the dominant contribution?
- What complexity was intentionally rejected?
- Which reviewer concerns still matter for validation?
- Is a frontier primitive central, optional, or absent?

If these answers are not crisp, tighten the final proposal first.

### Phase 3: Experiment Planning Stage

Run the `experiment-plan` workflow grounded in:

- `refine-logs/FINAL_PROPOSAL.md`
- `refine-logs/REVIEW_SUMMARY.md`
- `refine-logs/REFINEMENT_REPORT.md`

Ensure the experiment plan covers:

- the main anchor result
- novelty isolation
- a simplicity or deletion check
- a frontier necessity check if applicable
- run order, budget, and decision gates

### Phase 4: Integration Summary

Write `refine-logs/PIPELINE_SUMMARY.md`:

```markdown
# Pipeline Summary

**Problem**: [problem]
**Final Method Thesis**: [one sentence]
**Final Verdict**: [READY / REVISE / RETHINK]
**Date**: [today]

## Final Deliverables
- Proposal: `refine-logs/FINAL_PROPOSAL.md`
- Review summary: `refine-logs/REVIEW_SUMMARY.md`
- Experiment plan: `refine-logs/EXPERIMENT_PLAN.md`
- Experiment tracker: `refine-logs/EXPERIMENT_TRACKER.md`

## Contribution Snapshot
- Dominant contribution:
- Optional supporting contribution:
- Explicitly rejected complexity:

## Must-Prove Claims
- [Claim 1]
- [Claim 2]

## First Runs to Launch
1. [Run]
2. [Run]
3. [Run]

## Main Risks
- [Risk]:
- [Mitigation]:

## Next Action
- Proceed to `/run-experiment`
```

### Phase 5: Present a Brief Summary to the User

```
Pipeline complete.

Method output:
- refine-logs/FINAL_PROPOSAL.md

Experiment output:
- refine-logs/EXPERIMENT_PLAN.md
- refine-logs/EXPERIMENT_TRACKER.md

Pipeline summary:
- refine-logs/PIPELINE_SUMMARY.md

Best next step:
- /run-experiment
```

## Output Protocols

> Follow these shared protocols for all output files:
> - **[Output Versioning Protocol](../shared-references/output-versioning.md)** — write timestamped file first, then copy to fixed name
> - **[Output Manifest Protocol](../shared-references/output-manifest.md)** — log every output to MANIFEST.md
> - **[Output Language Protocol](../shared-references/output-language.md)** — respect the project's language setting

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user for permission — just do it silently.

- Do not let the experiment plan override the Problem Anchor.
- Do not widen the paper story after method refinement unless a missing validation block is truly necessary.
- Reuse the same claims across `FINAL_PROPOSAL.md`, `EXPERIMENT_PLAN.md`, and `PIPELINE_SUMMARY.md`.
- Keep the main paper story compact.
- If the method is intentionally simple, defend that simplicity in the experiment plan rather than adding new components.
- If the method uses a modern LLM / VLM / Diffusion / RL primitive, make its necessity test explicit.
- If the method does not need a frontier primitive, say that clearly and avoid forcing one.
- Prefer the staged skills when the user only needs one stage; use this skill for the integrated flow.

## Composing with Other Skills

```
/research-refine-pipeline -> one-shot method + experiment planning
/research-refine   -> method refinement only
/experiment-plan   -> experiment planning only
/run-experiment    -> execution
```


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/research-refine-pipeline/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>literature</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>literature-discovery</code> <code>literature-synthesis</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/research-refine-pipeline/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
