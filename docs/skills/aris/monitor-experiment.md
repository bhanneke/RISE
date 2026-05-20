<!-- DO NOT EDIT — auto-copied from skills/aris/details/monitor-experiment.md -->

# `monitor-experiment`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../aris/">ARIS skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-05-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/monitor-experiment/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/aris/monitor-experiment/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Monitor Experiment Results

Monitor: $ARGUMENTS

### Workflow

#### Step 1: Check What's Running

**SSH server:**
```bash
ssh <server> "screen -ls"
```

**Vast.ai instance** (read `ssh_host`, `ssh_port` from `vast-instances.json`):
```bash
ssh -p <PORT> root@<HOST> "screen -ls"
```

Also check vast.ai instance status:
```bash
vastai show instances
```

**Modal** (when `gpu: modal` in CLAUDE.md):
```bash
modal app list         # List running/recent apps
modal app logs <app>   # Stream logs from a running app
```
Modal apps auto-terminate when done — if it's not in the list, it already finished. Check results via `modal volume ls <volume>` or local output.

#### Step 2: Collect Output from Each Screen
For each screen session, capture the last N lines:
```bash
ssh <server> "screen -S <name> -X hardcopy /tmp/screen_<name>.txt && tail -50 /tmp/screen_<name>.txt"
```

If hardcopy fails, check for log files or tee output.

#### Step 3: Check for JSON Result Files
```bash
ssh <server> "ls -lt <results_dir>/*.json 2>/dev/null | head -20"
```

If JSON results exist, fetch and parse them:
```bash
ssh <server> "cat <results_dir>/<latest>.json"
```

#### Step 3.5: Pull W&B Metrics (when `wandb: true` in CLAUDE.md)

**Skip this step entirely if `wandb` is not set or is `false` in CLAUDE.md.**

Pull training curves and metrics from Weights & Biases via Python API:

```bash
## List recent runs in the project
ssh <server> "python3 -c \"
import wandb
api = wandb.Api()
runs = api.runs('<entity>/<project>', per_page=10)
for r in runs:
    print(f'{r.id}  {r.state}  {r.name}  {r.summary.get(\"eval/loss\", \"N/A\")}')
\""

## Pull specific metrics from a run (last 50 steps)
ssh <server> "python3 -c \"
import wandb, json
api = wandb.Api()
run = api.run('<entity>/<project>/<run_id>')
history = list(run.scan_history(keys=['train/loss', 'eval/loss', 'eval/ppl', 'train/lr'], page_size=50))
print(json.dumps(history[-10:], indent=2))
\""

## Pull run summary (final metrics)
ssh <server> "python3 -c \"
import wandb, json
api = wandb.Api()
run = api.run('<entity>/<project>/<run_id>')
print(json.dumps(dict(run.summary), indent=2, default=str))
\""
```

**What to extract:**
- **Training loss curve** — is it converging? diverging? plateauing?
- **Eval metrics** — loss, PPL, accuracy at latest checkpoint
- **Learning rate** — is the schedule behaving as expected?
- **GPU memory** — any OOM risk?
- **Run status** — running / finished / crashed?

**W&B dashboard link** (include in summary for user):
```
https://wandb.ai/<entity>/<project>/runs/<run_id>
```

> This gives the auto-review-loop richer signal than just screen output — training dynamics, loss curves, and metric trends over time.

#### Step 4: Summarize Results

Present results in a comparison table:
```
| Experiment | Metric | Delta vs Baseline | Status |
|-----------|--------|-------------------|--------|
| Baseline  | X.XX   | —                 | done   |
| Method A  | X.XX   | +Y.Y              | done   |
```

#### Step 5: Interpret
- Compare against known baselines
- Flag unexpected results (negative delta, NaN, divergence)
- Suggest next steps based on findings

#### Step 6: Feishu Notification (if configured)

After results are collected, check `~/.claude/feishu.json`:
- Send `experiment_done` notification: results summary table, delta vs baseline
- If config absent or mode `"off"`: skip entirely (no-op)

### Key Rules
- Always show raw numbers before interpretation
- Compare against the correct baseline (same config)
- Note if experiments are still running (check progress bars, iteration counts)
- If results look wrong, check training logs for errors before concluding
- **Vast.ai cost awareness**: When monitoring vast.ai instances, report the running cost (hours * $/hr from `vast-instances.json`). If all experiments on an instance are done, remind the user to run `/vast-gpu destroy <instance_id>` to stop billing
- **Modal cost awareness**: Modal auto-scales to zero — no idle billing. When reporting results from Modal runs, note the actual execution time and estimated cost (time * $/hr from the GPU tier used). No cleanup action needed
