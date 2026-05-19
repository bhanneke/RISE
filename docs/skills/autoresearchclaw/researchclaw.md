<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/researchclaw.md -->

# `researchclaw`



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
name: researchclaw
description: Run the ResearchClaw autonomous research pipeline from a topic, config, and output directory.
---

# ResearchClaw — Autonomous Research Pipeline Skill

## Description

Run ResearchClaw's 23-stage autonomous research pipeline. Given a research topic, this skill orchestrates the entire research workflow: literature review → hypothesis generation → experiment design → code generation & execution → result analysis → paper writing → peer review → final export.

## Trigger Conditions

Activate this skill when the user:
- Asks to "research [topic]", "write a paper about [topic]", or "investigate [topic]"
- Wants to run an autonomous research pipeline
- Asks to generate a research paper from scratch
- Mentions "ResearchClaw" by name

## Instructions

### Prerequisites Check

1. Verify config file exists:
   ```bash
   ls config.yaml || ls config.researchclaw.example.yaml
   ```
2. If no `config.yaml`, create one from the example:
   ```bash
   cp config.researchclaw.example.yaml config.yaml
   ```
3. Ensure the user's LLM API key is configured in `config.yaml` under `llm.api_key` or via `llm.api_key_env` environment variable.

### Running the Pipeline

**Option A: CLI (recommended)**

```bash
researchclaw run --topic "Your research topic here" --auto-approve
```

Options:
- `--topic` / `-t`: Override the research topic from config
- `--config` / `-c`: Config file path (default: `config.yaml`)
- `--output` / `-o`: Output directory (default: `artifacts/rc-YYYYMMDD-HHMMSS-HASH/`)
- `--from-stage`: Resume from a specific stage (e.g., `PAPER_OUTLINE`)
- `--auto-approve`: Auto-approve gate stages (5, 9, 20) without human input

**Option B: Python API**

```python
from researchclaw.pipeline.runner import execute_pipeline
from researchclaw.config import RCConfig
from researchclaw.adapters import AdapterBundle
from pathlib import Path

config = RCConfig.load("config.yaml", check_paths=False)
results = execute_pipeline(
    run_dir=Path("artifacts/my-run"),
    run_id="research-001",
    config=config,
    adapters=AdapterBundle(),
    auto_approve_gates=True,
)

# Check results
for r in results:
    print(f"Stage {r.stage.name}: {r.status.value}")
```

**Option C: Iterative Pipeline (multi-round improvement)**

```python
from researchclaw.pipeline.runner import execute_iterative_pipeline

results = execute_iterative_pipeline(
    run_dir=Path("artifacts/my-run"),
    run_id="research-001",
    config=config,
    adapters=AdapterBundle(),
    max_iterations=3,
    convergence_rounds=2,
)
```

### Output Structure

After a successful run, the output directory contains:

```
artifacts/<run-id>/
├── stage-1/                # TOPIC_INIT outputs
├── stage-2/                # PROBLEM_DECOMPOSE outputs
├── ...
├── stage-10/
│   └── experiment.py       # Generated experiment code
├── stage-12/
│   └── runs/run-1.json     # Experiment execution results
├── stage-14/
│   ├── experiment_summary.json  # Aggregated metrics
│   └── results_table.tex        # LaTeX results table
├── stage-17/
│   └── paper_draft.md      # Full paper draft
├── stage-22/
│   └── charts/             # Generated visualizations
│       ├── metric_trajectory.png
│       └── experiment_comparison.png
└── pipeline_summary.json   # Overall pipeline status
```

### Experiment Modes

| Mode | Description | Config |
|------|-------------|--------|
| `simulated` | LLM generates synthetic results (no code execution) | `experiment.mode: simulated` |
| `sandbox` | Execute generated code locally via subprocess | `experiment.mode: sandbox` |
| `ssh_remote` | Execute on remote GPU server via SSH | `experiment.mode: ssh_remote` |

### Troubleshooting

- **Config validation error**: Run `researchclaw validate --config config.yaml`
- **LLM connection failure**: Check `llm.base_url` and API key
- **Sandbox execution failure**: Verify `experiment.sandbox.python_path` exists and has numpy installed
- **Gate rejection**: Use `--auto-approve` or manually approve at stages 5, 9, 20

## Tools Required

- File read/write (for config and artifacts)
- Bash (for CLI execution)
- No external MCP servers required for basic operation


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/researchclaw/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>aiming-lab/AutoResearchClaw</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../autoresearchclaw.md">AutoResearchClaw skills</a></dd>
<dt><b>Category</b></dt><dd><code>literature</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>literature-discovery</code> <code>literature-synthesis</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04-23</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw">⭐ aiming-lab/AutoResearchClaw</a><br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/autoresearchclaw/researchclaw/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/autoresearchclaw.yml">edit on GitHub</a>.</p>
</div>

</div>
