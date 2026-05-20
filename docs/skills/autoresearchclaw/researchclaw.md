<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/researchclaw.md -->

# `researchclaw`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../autoresearchclaw/">AutoResearchClaw skills</a></div><div><b>Category:</b> <code>literature</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>literature-discovery</code> · <code>literature-synthesis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/researchclaw/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/autoresearchclaw/researchclaw/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/aiming-lab/AutoResearchClaw" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## ResearchClaw — Autonomous Research Pipeline Skill

### Description

Run ResearchClaw's 23-stage autonomous research pipeline. Given a research topic, this skill orchestrates the entire research workflow: literature review → hypothesis generation → experiment design → code generation & execution → result analysis → paper writing → peer review → final export.

### Trigger Conditions

Activate this skill when the user:
- Asks to "research [topic]", "write a paper about [topic]", or "investigate [topic]"
- Wants to run an autonomous research pipeline
- Asks to generate a research paper from scratch
- Mentions "ResearchClaw" by name

### Instructions

#### Prerequisites Check

1. Verify config file exists:
   ```bash
   ls config.yaml || ls config.researchclaw.example.yaml
   ```
2. If no `config.yaml`, create one from the example:
   ```bash
   cp config.researchclaw.example.yaml config.yaml
   ```
3. Ensure the user's LLM API key is configured in `config.yaml` under `llm.api_key` or via `llm.api_key_env` environment variable.

#### Running the Pipeline

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

## Check results
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

#### Output Structure

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

#### Experiment Modes

| Mode | Description | Config |
|------|-------------|--------|
| `simulated` | LLM generates synthetic results (no code execution) | `experiment.mode: simulated` |
| `sandbox` | Execute generated code locally via subprocess | `experiment.mode: sandbox` |
| `ssh_remote` | Execute on remote GPU server via SSH | `experiment.mode: ssh_remote` |

#### Troubleshooting

- **Config validation error**: Run `researchclaw validate --config config.yaml`
- **LLM connection failure**: Check `llm.base_url` and API key
- **Sandbox execution failure**: Verify `experiment.sandbox.python_path` exists and has numpy installed
- **Gate rejection**: Use `--auto-approve` or manually approve at stages 5, 9, 20

### Tools Required

- File read/write (for config and artifacts)
- Bash (for CLI execution)
- No external MCP servers required for basic operation
