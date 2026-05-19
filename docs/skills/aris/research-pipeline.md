<!-- DO NOT EDIT — auto-copied from skills/aris/details/research-pipeline.md -->

# `research-pipeline`



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
name: research-pipeline
description: "Full research pipeline: Workflow 1 (idea discovery) → implementation → Workflow 2 (auto review loop) → Workflow 3 (paper writing, optional). Goes from a broad research direction all the way to a polished PDF. Use when user says \"全流程\", \"full pipeline\", \"从找idea到投稿\", \"end-to-end research\", or wants the complete autonomous research lifecycle."
argument-hint: [research-direction]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, WebSearch, WebFetch, Agent, Skill, mcp__codex__codex, mcp__codex__codex-reply
---

# Full Research Pipeline: Idea → Experiments → Submission

End-to-end autonomous research workflow for: **$ARGUMENTS**

## Constants

- **AUTO_PROCEED = true** — When `true`, Gate 1 auto-selects the top-ranked idea (highest pilot signal + novelty confirmed) and continues to implementation. When `false`, always waits for explicit user confirmation before proceeding.
- **ARXIV_DOWNLOAD = false** — When `true`, `/research-lit` downloads the top relevant arXiv PDFs during literature survey. When `false` (default), only fetches metadata via arXiv API. Passed through to `/idea-discovery` → `/research-lit`.
- **HUMAN_CHECKPOINT = false** — When `true`, the auto-review loops (Stage 4) pause after each round's review to let you see the score and provide custom modification instructions before fixes are implemented. When `false` (default), loops run fully autonomously. Passed through to `/auto-review-loop`.
- **REVIEWER_DIFFICULTY = medium** — How adversarial the reviewer is. `medium` (default): standard MCP review. `hard`: adds reviewer memory + debate protocol. `nightmare`: GPT reads repo directly via `codex exec` + memory + debate. Passed through to `/auto-review-loop`.
- **AUTO_WRITE = false** — When `true`, automatically invoke Workflow 3 (`/paper-writing`) after Stage 5. Requires `VENUE` to be set. When `false` (default), Stage 5 generates `NARRATIVE_REPORT.md` and stops — user invokes `/paper-writing` manually.
- **VENUE = ICLR** — Target venue for paper writing (Stage 6). Only used when `AUTO_WRITE=true`. Options: `ICLR`, `NeurIPS`, `ICML`, `CVPR`, `ACL`, `AAAI`, `ACM`, `IEEE_CONF`, `IEEE_JOURNAL`.

> 💡 Override via argument, e.g., `/research-pipeline "topic" — AUTO_PROCEED: false, human checkpoint: true, difficulty: nightmare, auto_write: true, venue: NeurIPS`.

## Overview

This skill chains the entire research lifecycle into a single pipeline:

```
/idea-discovery → implement → /run-experiment → /auto-review-loop → /paper-writing (optional)
├── Workflow 1 ──┤            ├────────── Workflow 2 ──────────────┤ ├── Workflow 3 ──┤
```

It orchestrates up to three major workflows plus the implementation bridge between them. Workflow 3 (paper writing) is optional and controlled by `AUTO_WRITE`.

## Pipeline

### Stage 1: Idea Discovery (Workflow 1)

If `RESEARCH_BRIEF.md` exists in the project root, it will be automatically loaded as detailed context (replaces one-line prompt). See `templates/RESEARCH_BRIEF_TEMPLATE.md`.

Invoke the idea discovery pipeline:

```
/idea-discovery "$ARGUMENTS"
```

This internally runs: `/research-lit` → `/idea-creator` → `/novelty-check` → `/research-review`

**Output:** `idea-stage/IDEA_REPORT.md` with ranked, validated, pilot-tested ideas.

**🚦 Gate 1 — Human Checkpoint:**

After `idea-stage/IDEA_REPORT.md` is generated, **pause and present the top ideas to the user**:

```
📋 Idea Discovery complete. Top ideas:

1. [Idea 1 title] — Pilot: POSITIVE (+X%), Novelty: CONFIRMED
2. [Idea 2 title] — Pilot: WEAK POSITIVE (+Y%), Novelty: CONFIRMED
3. [Idea 3 title] — Pilot: NEGATIVE, eliminated

Recommended: Idea 1. Shall I proceed with implementation?
```

**If AUTO_PROCEED=false:** Wait for user confirmation before continuing. The user may:
- **Approve an idea** → proceed to Stage 2.
- **Pick a different idea** → proceed with their choice.
- **Request changes** (e.g., "combine Idea 1 and 3", "focus more on X") → update the idea prompt with user feedback, re-run `/idea-discovery` with refined constraints, and present again.
- **Reject all ideas** → collect feedback on what's missing, re-run Stage 1 with adjusted research direction. Repeat until the user commits to an idea.
- **Stop here** → save current state to `idea-stage/IDEA_REPORT.md` for future reference.

**If AUTO_PROCEED=true:** Present the top ideas, wait 10 seconds for user input. If no response, auto-select the #1 ranked idea (highest pilot signal + novelty confirmed) and proceed to Stage 2. Log: `"AUTO_PROCEED: selected Idea 1 — [title]"`.

> ⚠️ **This gate waits for user confirmation when AUTO_PROCEED=false.** When `true`, it auto-selects the top idea after presenting results. The rest of the pipeline (Stages 2-4) is expensive (GPU time + multiple review rounds), so set `AUTO_PROCEED=false` if you want to manually choose which idea to pursue.

### Stage 2: Implementation

Once the user confirms which idea to pursue:

1. **Read the idea details** from `idea-stage/IDEA_REPORT.md` (hypothesis, experimental design, pilot code) *(fall back to `./IDEA_REPORT.md` if not found)*

2. **Implement the full experiment**:
   - Extend pilot code to full scale (multi-seed, full dataset, proper baselines)
   - Add proper evaluation metrics and logging (wandb if configured)
   - Write clean, reproducible experiment scripts
   - Follow existing codebase conventions

3. **Code review**: Before deploying, do a self-review:
   - Are all hyperparameters configurable via argparse?
   - Is the random seed fixed and controllable?
   - Are results saved to JSON/CSV for later analysis?
   - Is there proper logging for debugging?

### Stage 3: Deploy Experiments (Workflow 2 — Part 1)

Deploy the full-scale experiments. **Route by job count**:

**Small batch (≤5 jobs)** — direct deployment:
```
/run-experiment [experiment command]
```

**Large batch (≥10 jobs, multi-seed sweeps, teacher→student chains)** — use the queue scheduler:
```
/experiment-queue [grid spec or manifest]
```

`experiment-bridge` (Workflow 1.5) auto-routes based on milestone job count. For pipeline runs with multi-seed sweeps from the start, you can override globally with `--- batch: queue` to force `/experiment-queue` for all milestones.

**What this does:**
- Check GPU availability on configured servers
- Sync code to remote server
- Launch experiments in screen sessions with proper CUDA_VISIBLE_DEVICES
- For `/experiment-queue`: also OOM retry, stale-screen cleanup, phase dependencies, crash-safe state
- Verify experiments started successfully

**Monitor progress:**

```
/monitor-experiment [server]
```

Wait for experiments to complete. Collect results.

### Stage 4: Auto Review Loop (Workflow 2 — Part 2)

Once initial results are in, start the autonomous improvement loop:

```
/auto-review-loop "$ARGUMENTS — [chosen idea title], difficulty: $REVIEWER_DIFFICULTY"
```

**What this does (up to 4 rounds):**
1. GPT-5.4 xhigh reviews the work (score, weaknesses, minimum fixes)
2. Claude Code implements fixes (code changes, new experiments, reframing)
3. Deploy fixes, collect new results
4. Re-review → repeat until score ≥ 6/10 or 4 rounds reached

**Output:** `review-stage/AUTO_REVIEW.md` with full review history and final assessment.

### Stage 5: Research Summary & Writing Handoff

After the auto-review loop completes, prepare the handoff for paper writing.

**Step 1:** Write a final research status report (same as before).

**Step 2:** Generate `NARRATIVE_REPORT.md` from:
- `IDEA_REPORT.md` (chosen idea, hypothesis, novelty justification)
- Implementation details from the repo
- Experiment configs and final results
- `AUTO_REVIEW.md` (review history, weaknesses fixed, remaining limitations)

The narrative report must contain:
- Problem statement and core claim
- Method summary
- Key quantitative results with evidence for each claim
- Figure/table inventory (which exist, which need manual creation)
- Limitations and remaining follow-up items

**Output:** `NARRATIVE_REPORT.md` + research pipeline report.

```markdown
# Research Pipeline Report

**Direction**: $ARGUMENTS
**Chosen Idea**: [title]
**Date**: [start] → [end]
**Pipeline**: idea-discovery → implement → run-experiment → auto-review-loop

## Journey Summary
- Ideas generated: X → filtered to Y → piloted Z → chose 1
- Implementation: [brief description of what was built]
- Experiments: [number of GPU experiments, total compute time]
- Review rounds: N/4, final score: X/10

## Writing Handoff
- NARRATIVE_REPORT.md: ✅ generated
- Venue: [VENUE or "not set — run /paper-writing manually"]
- Manual figures needed: [list or "none"]

## Remaining TODOs (if any)
- [items flagged by reviewer that weren't addressed]
```

### Stage 6: Paper Writing (Workflow 3 — Optional)

**Skip this stage if `AUTO_WRITE=false` (default).** Present the `/paper-writing` command for manual use:

```
📝 Research complete. To write the paper:
/paper-writing "NARRATIVE_REPORT.md" — venue: ICLR
```

**If `AUTO_WRITE=true`:**

🚦 **Gate 2 — Writing Checkpoint:**

```
📝 Research pipeline complete. Ready for Workflow 3.

- Venue: [VENUE]
- Input: NARRATIVE_REPORT.md
- Manual figures required: [list or none]
- Next step: /paper-writing "NARRATIVE_REPORT.md — venue: [VENUE]"

Proceeding with paper writing...
```

Checks before proceeding:
- If `VENUE` is missing → stop and ask. Do NOT silently use a default venue.
- If manual figures are required → pause and list them. Wait for user to add them.

Then invoke:

```
/paper-writing "NARRATIVE_REPORT.md" — venue: $VENUE
```

This delegates to Workflow 3 which handles its own phases:
`/paper-plan → /paper-figure → /paper-write → /paper-compile → /auto-paper-improvement-loop`

When Workflow 3 finishes, update the pipeline report with:
- Paper writing completion status
- Final PDF path (`paper/main.pdf`)
- Improvement scores (round 0 → round N)
- Remaining issues

**Output:** `paper/` directory with LaTeX source, compiled PDF, and `PAPER_IMPROVEMENT_LOG.md`.

## Output Protocols

> Follow these shared protocols for all output files:
> - **[Output Versioning Protocol](../shared-references/output-versioning.md)** — write timestamped file first, then copy to fixed name
> - **[Output Manifest Protocol](../shared-references/output-manifest.md)** — log every output to MANIFEST.md
> - **[Output Language Protocol](../shared-references/output-language.md)** — respect the project's language setting

## Key Rules

- **Large file handling**: If the Write tool fails due to file size, immediately retry using Bash (`cat << 'EOF' > file`) to write in chunks. Do NOT ask the user for permission — just do it silently.

- **Human checkpoint after Stage 1 is controlled by AUTO_PROCEED.** When `false`, do not proceed without user confirmation. When `true`, auto-select the top idea after presenting results.
- **Stages 2-4 can run autonomously** once the user confirms the idea. This is the "sleep and wake up to results" part.
- **If Stage 4 ends at round 4 without positive assessment**, stop and report remaining issues. Do not loop forever.
- **Budget awareness**: Track total GPU-hours across the pipeline. Flag if approaching user-defined limits.
- **Documentation**: Every stage updates its own output file. The full history should be self-contained.
- **Fail gracefully**: If any stage fails (no good ideas, experiments crash, review loop stuck), report clearly and suggest alternatives rather than forcing forward.

## Typical Timeline

| Stage | Duration | Can sleep? |
|-------|----------|------------|
| 1. Idea Discovery | 30-60 min | Yes if AUTO_PROCEED=true |
| 2. Implementation | 15-60 min | Yes (autonomous after Gate 1) |
| 3. Deploy | 5 min + experiment time | Yes ✅ |
| 4. Auto Review | 1-4 hours (depends on experiments) | Yes ✅ |

**Sweet spot**: Run Stage 1-2 in the evening, launch Stage 3-4 before bed, wake up to a reviewed paper.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/research-pipeline/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/research-pipeline/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
