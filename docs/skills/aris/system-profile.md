<!-- DO NOT EDIT — auto-copied from skills/aris/details/system-profile.md -->

# `system-profile`



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
name: system-profile
description: Profile a target (script, process, GPU, memory, interconnect) using external tools and code instrumentation. Produces structured performance reports with actionable recommendations. Use when user says "profile", "benchmark", "bottleneck", or wants performance analysis.
argument-hint: <target, e.g. "train.py", "gpu", "pid 1234", "vllm serving">
---

# System Profile

Profile the specified target and summarize the results. Target: $ARGUMENTS

## Instructions

You are a profiling assistant. Based on the user's target, choose appropriate profiling strategies, **including writing instrumentation code when needed**, then run profiling, analyze results, and produce a summary.

### Step 1: Determine the profiling target

Parse `$ARGUMENTS` to understand what to profile. Examples:
- A Python script or module
- A running process (PID or service name)
- A specific function or code block
- An entire framework or system (e.g., "autogen", "vllm serving") — profile its end-to-end execution, identify bottlenecks across components
- "gpu" / "interconnect" / "memory" for focused profiling

If `$ARGUMENTS` is empty or unclear, ask the user.

### Step 2: Choose profiling methods

Select from external tools and/or code instrumentation as appropriate. Don't limit yourself to the examples below — use whatever makes sense for the target.

**External tools** (check availability first):
- CPU: `cProfile`, `py-spy`, `line_profiler`, `perf stat`, `/usr/bin/time -v`
- Memory: `tracemalloc`, `memory_profiler`, `memray`
- GPU: `nvidia-smi`, `nvidia-smi dmon`, `nvitop`, `torch.profiler`, `nsys`
- Interconnect: `nvidia-smi topo -m`, `nvidia-smi nvlink`, `NCCL_DEBUG=INFO`
- System: `strace -c`, `iostat`, `vmstat`

**Code instrumentation** — when external tools are insufficient, write and insert profiling code into the target. Typical scenarios:
- Timing specific code blocks (wall time vs CPU time)
- Measuring CPU-GPU or GPU-GPU transfer size, frequency, and bandwidth
- Tracking memory allocation across CPU and GPU to detect redundancy
- Wrapping NCCL collectives to measure latency and throughput
- Adding CUDA event timing around kernels

Design the instrumentation based on what you observe in the code — don't use a fixed template.

### Step 3: Key dimensions to investigate

Depending on the target, focus on some or all of these:

**CPU overhead**
- Context switching (voluntary / involuntary)
- CPU utilization: ratio of CPU time to wall time
- Per-function execution time hotspots

**Memory overhead**
- CPU and GPU memory usage (allocated vs reserved vs peak)
- Redundant replication: same data living on both CPU and GPU
- Per-device allocation balance in multi-GPU setups

**Interconnect & communication**
- CPU-GPU transfer: frequency, per-transfer size, total volume, bandwidth achieved
- GPU-GPU transfer: P2P bandwidth, NVLink vs PCIe topology impact
- NCCL collectives: operation type, message size distribution, latency
- Communication-to-computation ratio

**GPU compute**
- SM utilization, kernel launch overhead
- Memory bandwidth utilization vs peak

### Step 4: Instrumentation guidelines

When inserting code into the target:
1. Read and understand the target code first
2. Prefer wrapping (decorator, context manager, standalone runner) over inline edits
3. If inline edits are necessary, mark them clearly (e.g., `# [PROFILE]` comments)
4. Minimize observer effect — don't instrument tight inner loops; sample instead
5. Collect results into a structured log, don't scatter print statements

### Step 5: Run profiling

1. Check available tools and hardware topology
2. Run the chosen methods, capture all output
3. Save artifacts (flamegraphs, traces, logs) to `./profile_output/`

### Step 6: Produce the report

**Part A — Profiling results** (structured tables by dimension, as applicable):
- CPU overhead table
- Memory overhead table (with redundancy column)
- Interconnect table (transfer type / frequency / size / latency / bandwidth)
- Hotspots / bottleneck identification
- Actionable recommendations ranked by expected impact

**Part B — Instrumentation changelog** (MANDATORY):
List every file that was modified or created for profiling purposes:

| File | Change type | What was added/modified | Line(s) |
|------|-------------|------------------------|---------|
| ... | modified | ... | ... |
| ... | created | ... | — |

This allows the user to review and revert all instrumentation changes.
Offer to clean up (remove all instrumentation) when the user is done.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/wanshuiyin/Auto-claude-code-research-in-sleep/contents/skills/system-profile/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/aris/system-profile/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/aris.yml">edit on GitHub</a>.</p>
</div>

</div>
