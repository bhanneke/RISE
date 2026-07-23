<!-- DO NOT EDIT — auto-copied from skills/awesome-journal-skills/details/rt-execution-bridge.md -->

# `rt-execution-bridge`

Runs and audits the empirical analysis rather than just advising — maps a DiD/IV/RDD/synthetic-control/DML design to the concrete StatsPAI / Stata MCP tools in the environment and reports the fitted, audited number.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../awesome-journal-skills/">Awesome Journal Skills (AJS)</a></div><div><b>Category:</b> <code>analysis</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code> · <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/brycewang-stanford/Awesome-Journal-Skills/contents/Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/awesome-journal-skills/rt-execution-bridge/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/brycewang-stanford/Awesome-Journal-Skills/blob/main/Research-Toolkit-Skills/skills/rt-execution-bridge/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/brycewang-stanford/Awesome-Journal-Skills?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Execution Bridge (rt-execution-bridge)

Close the last mile: turn "you should use a heterogeneity-robust DiD / weak-IV-robust CI /
multiple-testing correction" into an actual fitted, audited estimate. Full map +
orchestration spine + validated worked-examples (DiD / IV / RDD / synthetic-control / DML):
`shared-resources/empirical-methods/execution-with-mcp.md`.

### When to trigger

- You have data and a design and need the actual estimate + its diagnostics.
- A reviewer objection (real or simulated) needs an executed answer (e.g. "TWFE is biased
  under staggered adoption" → run Callaway–Sant'Anna + Goodman-Bacon).

### The spine (always)

1. `detect_design` → `preflight` / `recommend` → fit with `as_handle=true`.
2. `audit_result(result_id)` — enumerate the checks the design still owes; run each
   `suggest_function` it names.
3. Design-specific sensitivity from the handle (`honest_did_from_result`,
   `sensitivity_from_result`, `evalue_from_result`).
4. `bibtex(keys=[…])` for citations — never invent references.

### Design → tools (summary; full table in the canonical doc)

- **Staggered DiD:** `callaway_santanna` / `sun_abraham` + `bacon_decomposition` + `honest_did_from_result`.
- **IV:** `iv` + `effective_f_test` + `anderson_rubin_ci` (weak-IV-robust).
- **RDD:** `rdrobust` + `rddensity` / `mccrary_test`.
- **Synthetic control:** `synth` / `sdid` + placebo inference.
- **DML / high-dim:** `dml` + `dml_diagnostics` (overlap) + `oster` / `sensemakr`.
- **Multiple testing / inference:** `romano_wolf`, `wild_cluster_bootstrap`, `twoway_cluster`.
- **Exhibits:** `etable` / `did_summary_to_latex` straight from the handle.

### Hard rules

1. **Run, don't claim** — every reported estimate/CI/F/bound traces to a tool call.
2. **`bibtex` is the only citation source.**
3. **Method here, placement there** — where the result goes (body vs. appendix, page limit,
   house table style) is the target pack's skills + `official-source-map.md`.
4. **Degrade honestly** — if StatsPAI/Stata are not connected, adapt the `code/` skeleton
   and flag any unverified number.

### Output format

```
【Design】DiD / IV / RDD / SCM / DML / …
【Estimate】point [CI] (estimator)
【Key diagnostic】(first-stage/effective F, pre-trends p, overlap, placebo p, …)
【Audit gaps run】…
【Magnitude】interpretable units
【Next】rt-submission-readiness / the pack's tables-figures skill
```
