<!-- DO NOT EDIT — auto-copied from skills/aris/details/training-check.md -->

# `training-check`



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
name: training-check
description: Periodically check WandB metrics during training to catch problems early (NaN, loss divergence, idle GPUs). Avoids wasting GPU hours on broken runs. Use when training is running and you want automated health checks.
argument-hint: [wandb-run-path]
allowed-tools: Bash(*), Read, Grep, Glob, Write, Edit, mcp__codex__codex, mcp__codex__codex-reply
---

# Training Check

Periodically read WandB metrics during training to catch problems early. Do not wait until training finishes to discover it was a waste of GPU time.

## Context: $ARGUMENTS

## Constants

- WANDB_ENTITY and WANDB_PROJECT: read from CLAUDE.md or passed as argument (format: `entity/project/run_id`)
- CHECK_INTERVAL: starts at 10 minutes, then gradually increases if consistently healthy: 10 min → 20 min → 30 min → 60 min (cap)
- REVIEWER_MODEL = `gpt-5.5` — used via Codex MCP for ambiguous cases only

## When to Use

- After training is confirmed running (session alive, loss decreasing for first few steps)
- Set up via CronCreate to fire periodically during training
- **This skill checks training QUALITY, not process HEALTH.** Process health (session alive, GPU utilization) is [watchdog.py](../../tools/watchdog.py)'s job.

## Workflow

### Step 1: Read WandB Metrics

```python
import wandb
api = wandb.Api()
run = api.run("<entity>/<project>/<run_id>")
history = run.history()
```

If WandB is unreachable (API error, network issue), fall back to reading the log file directly via SSH:
```bash
ssh server "tail -100 /path/to/training.log"
```

Check these signals:
- **Loss trend**: Is training loss decreasing over the last N steps?
- **Eval metrics**: Are evaluation metrics improving (or at least not degrading)?
- **NaN / Inf**: Any NaN or Inf values in loss or gradients?
- **Spikes**: Sudden large jumps in loss (>10x normal variance)?
- **Learning rate**: Is the schedule behaving as expected?
- **Gradient norm**: Exploding or vanishing?

### Step 2: Judgment

| Signal | Judgment | Action |
|--------|----------|--------|
| NaN/Inf in loss | **Clearly bad** | Stop training, investigate |
| Loss diverging (increasing for >N steps) | **Clearly bad** | Stop training, investigate |
| Eval metrics significantly worse than baseline | **Clearly bad** | Stop training, investigate |
| Loss decreasing, metrics improving | **Clearly fine** | Continue, increase check interval |
| Loss flat but not diverging | **Unsure** | → Step 3 (Codex judgment) |
| Metrics noisy, can't tell trend | **Unsure** | → Step 3 (Codex judgment) |
| Slightly worse than baseline but still early | **Unsure** | → Step 3 (Codex judgment) |

### Step 3: Codex Judgment (only when unsure)

Only escalate to Codex when the signal is ambiguous. For clearly good or clearly bad signals, act directly.

```
mcp__codex__codex:
  config: {"model_reasoning_effort": "high"}
  prompt: |
    TRAINING HEALTH CHECK — need your judgment on ambiguous metrics.

    Run: <entity>/<project>/<run_id>
    Current epoch/step: X / Y total
    Training loss (last 10 checkpoints): [values]
    Eval metrics (last 3 evals): [values]
    Baseline reference: [numbers from paper/reproduction]

    What I'm unsure about: [specific concern]

    Please respond with exactly one of:
    - STOP: clearly problematic, should kill training
    - CONTINUE: looks fine, check again next interval
    - WAIT: not enough data to judge, check again sooner
```

### Step 4: Act

| Decision | Action |
|----------|--------|
| **Stop** | Kill the training session. Save the WandB run URL, key metrics, and reason for stopping. Log to project notes for debugging. |
| **Continue** | Do nothing. Will be invoked again at next interval (increase interval if consistently healthy). |
| **Wait** | Do nothing but keep the current short interval (don't increase). |

## Integration with Watchdog

Training-check and [watchdog.py](../../tools/watchdog.py) operate at different levels:

| Layer | Tool | What it checks | Frequency |
|-------|------|----------------|-----------|
| Process health | watchdog.py | Session alive? GPU active? | Every 60s (continuous) |
| Training quality | training-check | Loss trend? Metrics improving? | Every 10-60 min (periodic) |

Use both together:
- Watchdog catches crashes and idle GPUs immediately
- Training-check catches subtle quality issues (loss plateau, metric degradation)

## Rules

- Do not stop training on first sign of noise — some loss spikes are normal. Look at **trends over multiple checkpoints**.
- When stopping training, always save the WandB run URL and key metrics as evidence.
- If both WandB and log files are unreachable, report the connectivity issue and try again next interval. Do not assume training is broken.
- Gradually increase check interval when healthy (10 → 20 → 30 → 60 min). Reset to 10 min after any anomaly.
- This skill is meant to be automated via CronCreate — do not ask the user whether to set it up. Just set it.

## CronCreate Setup Example

```
After training is confirmed stable:
  CronCreate (recurring, every 10 minutes initially):
    "Run /training-check for wandb run <entity>/<project>/<run_id>"
```

As the check interval increases, delete the old CronCreate job and create a new one with the longer interval.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/training-check/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/training-check/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
