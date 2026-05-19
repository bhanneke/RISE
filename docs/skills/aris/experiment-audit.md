<!-- DO NOT EDIT — auto-copied from skills/aris/details/experiment-audit.md -->

# `experiment-audit`



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
name: experiment-audit
description: "Audit experiment integrity before claiming results. Uses cross-model review (GPT-5.4) to check for fake ground truth, score normalization fraud, phantom results, and insufficient scope. Use when user says \"审计实验\", \"check experiment integrity\", \"audit results\", \"实验诚实度\", or after experiments complete before writing claims."
argument-hint: [experiment-dir-or-results-path]
allowed-tools: Bash(*), Read, Write, Edit, Grep, Glob, Agent, mcp__codex__codex, mcp__codex__codex-reply
---

# Experiment Audit: Cross-Model Integrity Verification

Audit experiment integrity for: **$ARGUMENTS**

## Why This Exists

LLM agents can produce fraudulent experimental results through:
1. **Fake ground truth** — creating synthetic "reference" from model outputs, then reporting high agreement as performance
2. **Score normalization** — dividing metrics by the model's own max to get 0.99+
3. **Phantom results** — claiming numbers from files that don't exist or functions never called
4. **Insufficient scope** — reporting 2-scene pilots as "comprehensive evaluation"

These are NOT intentional deception — they are failure modes of optimizing agents that lack integrity constraints. This skill adds that constraint.

## Core Principle

**The executor (Claude) collects file paths. The reviewer (GPT-5.4) reads code and judges integrity. The executor does NOT participate in integrity judgment.**

This follows `shared-references/reviewer-independence.md` and `shared-references/experiment-integrity.md`.

## Constants

- **REVIEWER_BACKEND = `codex`** — Default: Codex MCP (xhigh). Override with `— reviewer: oracle-pro` for GPT-5.4 Pro via Oracle MCP. See `shared-references/reviewer-routing.md`.

## Workflow

### Step 1: Collect Artifacts (Executor — Claude)

Locate and list these files WITHOUT reading or summarizing their content:

```
Scan project directory for:
1. Evaluation scripts:    *eval*.py, *metric*.py, *test*.py, *benchmark*.py
2. Result files:          *.json, *.csv in results/, outputs/, logs/
3. Ground truth paths:    look in eval scripts for data loading (dataset paths, GT references)
4. Experiment tracker:    EXPERIMENT_TRACKER.md, EXPERIMENT_LOG.md
5. Paper claims:          NARRATIVE_REPORT.md, paper/sections/*.tex, PAPER_PLAN.md
6. Config files:          *.yaml, *.toml, *.json configs with metric definitions
```

**DO NOT summarize, interpret, or explain any file content.** Only collect paths.

### Step 2: Send to Reviewer (GPT-5.4 via Codex MCP)

Pass ONLY file paths and the audit checklist to the reviewer. The reviewer reads everything directly.

```
mcp__codex__codex:
  model: gpt-5.5
  config: {"model_reasoning_effort": "xhigh"}
  sandbox: read-only
  cwd: [project directory]
  prompt: |
    You are an experiment integrity auditor. Read ALL files listed below
    and check for the following fraud patterns.

    Files to read:
    - Evaluation scripts: [list paths]
    - Result files: [list paths]
    - Experiment tracker: [list paths]
    - Paper claims: [list paths]
    - Config files: [list paths]

    ## Audit Checklist

    ### A. Ground Truth Provenance
    For each evaluation script:
    1. Where does "ground truth" / "reference" / "target" come from?
    2. Is it loaded from the DATASET, or generated/derived from MODEL OUTPUTS?
    3. If derived: is it explicitly labeled as proxy evaluation?
    4. Are official eval scripts used when available for this benchmark?
    FAIL if: GT is derived from model outputs without explicit proxy labeling.

    ### B. Score Normalization
    For each metric computation:
    1. Is any metric divided by max/min/mean of the model's OWN output?
    2. Are raw scores reported alongside any normalized scores?
    3. Are any scores suspiciously close to 1.0 or 100%?
    FAIL if: Normalization denominator comes from prediction statistics.

    ### C. Result File Existence
    For each claim in the paper/narrative:
    1. Does the referenced result file actually exist?
    2. Does the claimed metric key exist in that file?
    3. Does the claimed NUMBER match what's in the file?
    4. Is the experiment tracker status DONE (not TODO/IN_PROGRESS)?
    FAIL if: Claimed results reference nonexistent files or mismatched numbers.

    ### D. Dead Code Detection
    For each metric function defined in eval scripts:
    1. Is it actually CALLED in any evaluation pipeline?
    2. Does its output appear in any result file?
    WARN if: Metric functions exist but are never called.

    ### E. Scope Assessment
    1. How many scenes/datasets/configurations were actually tested?
    2. How many seeds/runs per configuration?
    3. Does the paper use words like "comprehensive", "extensive", "robust"?
    4. Is the actual scope sufficient for those claims?
    WARN if: Scope language exceeds actual evidence.

    ### F. Evaluation Type Classification
    Classify each evaluation as:
    - real_gt: uses dataset-provided ground truth
    - synthetic_proxy: uses model-generated reference
    - self_supervised_proxy: no GT by design
    - simulation_only: simulated environment
    - human_eval: human judges

    ## Output Format

    For each check (A-F), report:
    - Status: PASS | WARN | FAIL
    - Evidence: exact file:line references
    - Details: what specifically was found

    Overall verdict: PASS | WARN | FAIL
    
    Be thorough. Read every eval script line by line.
```

### Step 3: Parse and Write Report (Executor — Claude)

Parse the reviewer's response and write `EXPERIMENT_AUDIT.md`:

```markdown
# Experiment Audit Report

**Date**: [today]
**Auditor**: GPT-5.4 xhigh (cross-model, read-only)
**Project**: [project name]

## Overall Verdict: [PASS | WARN | FAIL]

## Integrity Status: [pass | warn | fail]

## Checks

### A. Ground Truth Provenance: [PASS|WARN|FAIL]
[details + file:line evidence]

### B. Score Normalization: [PASS|WARN|FAIL]
[details]

### C. Result File Existence: [PASS|WARN|FAIL]
[details]

### D. Dead Code Detection: [PASS|WARN|FAIL]
[details]

### E. Scope Assessment: [PASS|WARN|FAIL]
[details]

### F. Evaluation Type: [real_gt | synthetic_proxy | ...]
[classification + evidence]

## Action Items
- [specific fixes if WARN or FAIL]

## Claim Impact
- Claim 1: [supported | needs qualifier | unsupported]
- Claim 2: ...
```

Also write `EXPERIMENT_AUDIT.json` for machine consumption:

```json
{
  "date": "2026-04-10",
  "auditor": "gpt-5.5-xhigh",
  "overall_verdict": "warn",
  "integrity_status": "warn",
  "checks": {
    "gt_provenance": {"status": "pass", "details": "..."},
    "score_normalization": {"status": "warn", "details": "..."},
    "result_existence": {"status": "pass", "details": "..."},
    "dead_code": {"status": "pass", "details": "..."},
    "scope": {"status": "warn", "details": "..."},
    "eval_type": "real_gt"
  },
  "claims": [
    {"id": "C1", "impact": "supported"},
    {"id": "C2", "impact": "needs_qualifier"}
  ]
}
```

### Step 4: Print Summary

```
🔬 Experiment Audit Complete

  GT Provenance:      ✅ PASS — real dataset GT used
  Score Normalization: ⚠️ WARN — boundary metric uses self-reference
  Result Existence:    ✅ PASS — all files exist, numbers match
  Dead Code:           ✅ PASS — all metric functions called
  Scope:               ⚠️ WARN — 2 scenes, paper says "comprehensive"

  Overall: ⚠️ WARN
  
  See EXPERIMENT_AUDIT.md for details.
```

## Integration with Other Skills

### Automatic in /research-pipeline (advisory, never blocks)

When integrated into the pipeline, this skill runs automatically after `/experiment-bridge` and before `/auto-review-loop`:

```
/experiment-bridge → results ready
    ↓
/experiment-audit (automatic, advisory)
    ├── PASS  → continue normally
    ├── WARN  → print ⚠️ warning, continue, tag claims as [INTEGRITY: WARN]
    └── FAIL  → print 🔴 alert, continue, tag claims as [INTEGRITY CONCERN]
    ↓
/auto-review-loop → proceeds with integrity tags visible to reviewer
```

**Never blocks the pipeline.** Even on FAIL, the pipeline continues — but claims carry visible integrity tags.

### Read by /result-to-claim (if exists)

```
if EXPERIMENT_AUDIT.json exists:
    read integrity_status
    attach to verdict: {claim_supported: "yes", integrity_status: "warn"}
    if integrity_status == "fail":
        downgrade verdict display: "yes [INTEGRITY CONCERN]"
else:
    verdict as normal, integrity_status = "unavailable"
    mark as "provisional — no integrity audit"
```

### Read by /paper-write (if exists)

```
if EXPERIMENT_AUDIT.json exists AND integrity_status == "fail":
    add footnote to affected claims: "Note: integrity audit flagged concerns with this evaluation"
```

## Key Rules

- **Reviewer independence**: executor collects paths, reviewer judges. Period.
- **Never block**: warn loudly, never halt the pipeline.
- **File-as-switch**: no EXPERIMENT_AUDIT.md = skill was never run = zero impact on existing behavior.
- **Cross-model**: the reviewer MUST be a different model family from the executor.
- **Honest about limits**: the audit catches common patterns, not all possible fraud. It is a safety net, not a guarantee.

## Acknowledgements

Motivated by community-reported integrity issues (#57, #131) where executor agents created fake ground truth and self-normalized scores.

## Review Tracing

After each `mcp__codex__codex` or `mcp__codex__codex-reply` reviewer call, save the trace following `shared-references/review-tracing.md` (Policy C — forensic; never silently skip). Use `save_trace.sh` (resolved per the chain in `shared-references/integration-contract.md` §2) or write files directly to `.aris/traces/<skill>/<date>_run<NN>/`. Respect the `--- trace:` parameter (default: `full`).


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/experiment-audit/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>wanshuiyin/Auto-claude-code-research-in-sleep</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../aris.md">ARIS skills</a></dd>
<dt><b>Category</b></dt><dd><code>audit</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-05-18</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep">⭐ wanshuiyin/Auto-claude-code-research-in-sleep</a><br><img src="https://img.shields.io/github/stars/wanshuiyin/Auto-claude-code-research-in-sleep?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/experiment-audit/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
