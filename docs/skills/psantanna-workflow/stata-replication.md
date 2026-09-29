<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/stata-replication.md -->

# `/stata-replication`

End-to-end Stata pipeline: numbered .do files run through the stata-mcp server, logged outputs, and publication-ready esttab tables and exported figures.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>code-gen</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>code-generation</code> · <code>data-analysis</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/stata-replication/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/stata-replication/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/stata-replication/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## `/stata-replication` — Stata pipeline scaffold + execution

Build a complete Stata replication pipeline in `scripts/stata/`: numbered `.do` files following `.claude/rules/stata-code-conventions.md`, executed via the [`stata-mcp`](https://github.com/SepineTam/stata-mcp) MCP server, with outputs landing in `output/`.

### When to use

- Your project's analysis language is **Stata** (not R). Common in econ field experiments, RCT studies, and any AEA submission where the original replication package is Stata.
- You're porting an R-first project to Stata for an AEA submission.
- You're adding a Stata robustness check to an R-first paper.
- You want a one-command reproduction: `do scripts/stata/99_run_all.do`.

### When NOT to use

- Your project is R-first. Use `/data-analysis`.
- Your project is Python-first. Neither this skill nor `/data-analysis` is the right fit; consider extending the convention rule for Python or porting one of these skills.
- You're doing quick exploratory work. The numbered-pipeline scaffold is for replication packages, not scratch notebooks.

### Prerequisite: `stata-mcp` installed

This skill requires the `stata-mcp` MCP server. Install once per user:

```bash
claude mcp add stata-mcp --scope user -- uvx stata-mcp
```

The MCP server provides command-guarded Stata execution (refuses destructive operations like `!/shell/erase`), RAM monitoring, and Stata Language Server pairing. Maintained by SepineTam.

If `stata-mcp` is not installed, the skill halts at Phase 0 with installation instructions.

### Workflow

#### Phase 0: Pre-flight

1. Verify `stata-mcp` is registered in the user's MCP configuration. If not → halt with install instructions.
2. Verify Stata is installed locally (the MCP server cannot run without it). Output stata version to confirm.
3. Confirm `scripts/stata/` directory exists or can be created.
4. Read `.claude/rules/stata-code-conventions.md` — every emitted `.do` file follows this convention.
5. If `--from-r` flag is set, locate the existing R pipeline at `scripts/R/` and use it as a translation source. Apply the Stata → R pitfalls table from `replication-protocol.md` in reverse.

#### Phase 1: Scaffold the pipeline

Emit (or update) these files in `scripts/stata/`, each conforming to the header convention from `stata-code-conventions.md`:

```
scripts/stata/
├── 00_install.do        # ssc install, set globals, paths, sessionInfo capture
├── 01_clean.do          # raw → cleaned panel
├── 02_descriptive.do    # summary tables, balance (iebaltab), attrition
├── 03_analyze.do        # main regression specs (reghdfe / ivreg2 as needed)
├── 04_robustness.do     # alt specs, sensitivity
├── 05_tables_figures.do # esttab .tex outputs + graph export PDFs
└── 99_run_all.do        # do "01_clean.do" / do "02_..." / ...
```

If the paper or data source suggests specific specs (e.g., DiD with `reghdfe`, IV with `ivreg2`, RD with `rdrobust`), tailor `03_analyze.do` accordingly.

#### Phase 2: Execute (unless `--no-execute`)

For each script in numbered order:

1. Dispatch to `stata-mcp` to execute the `.do` file.
2. Capture the log (Stata writes to `output/NN_log.smcl` per the header convention) and the resulting `.dta` / `.tex` / `.pdf` outputs.
3. If a script fails, first append its specification to the ledger (step 4) with Status `failed` and the error in Why, then halt — do NOT auto-fix unless the failure is trivial (typo flagged by Stata at parse time). For substantive failures (insufficient observations, singular matrices, missing covariates), surface to the user.
4. Append every specification each estimation `.do` file ran — kept, dropped, or failed — to `quality_reports/spec-ledger.md`, with the same columns, commit stamp and append-only block as `/data-analysis` Phase 3 ("Specification ledger"). A failed run is a row too, with Status `failed` and the error in Why.

For long-running scripts (> 2 minutes), use the **Monitor tool** to stream stdout — same pattern documented in `/data-analysis` and `/audit-reproducibility`.

#### Phase 3: Verify

1. Confirm every expected output exists in `output/`.
2. Check `output/sessionInfo_stata.txt` was captured (package versions).
3. Run `/audit-reproducibility` if a manuscript exists — it reads Stata `.dta` outputs via `haven`/`pyreadstat`.
4. Report scripts run, outputs produced, any warnings from Stata.

#### Phase 4 (optional): R cross-check

If `--from-r` was set, run the R version of the same analysis (assumed to live at `scripts/R/`) and compare:

- Point estimates: should match to ~0.01 (per `replication-protocol.md` tolerance).
- Standard errors: should match to ~0.05 (clustering df adjustments can differ slightly between Stata and R).
- Sample sizes: must match exactly.

Discrepancies are surfaced for the user to investigate — typical culprits: clustering df, default options (logit vs probit for PS), bootstrap seed handling.

### Companion skills

- `/data-analysis` — R analogue. Same pipeline shape, different language.
- `/audit-reproducibility` — reads both `.rds` and `.dta` outputs. Cross-checks manuscript claims against the produced values.
- `/review-paper` — if the paper exists and cites tables/figures produced by this pipeline, `/review-paper` auto-invokes `/audit-reproducibility` (per `cross-artifact-review.md`).

### Anti-patterns

- **Hand-editing `.dta` files.** Never. All transformations happen via the `.do` files; `.dta` outputs are derived and reproducible.
- **Skipping the `99_run_all.do`.** This is the AEA-mandated one-command entry point. Build it even for small projects.
- **Using `, robust` by default.** Use `, cluster(id)` at the appropriate level — see `stata-code-conventions.md` §6.
- **Hand-formatting tables in LaTeX.** Use `esttab` and `\input{}` — see `stata-code-conventions.md` §4.
- **Pinning Stata version in only one .do file.** Every `.do` file starts with `version 18` per the convention.

### Cross-references

- `.claude/rules/stata-code-conventions.md` — the discipline contract.
- `.claude/rules/replication-protocol.md` — tolerance thresholds (applies across R / Stata / Python).
- [stata-mcp on GitHub](https://github.com/SepineTam/stata-mcp) — the MCP server this skill depends on.
- [AEA Data Editor checklist](https://aeadataeditor.github.io/) — replication-package standards.

### Long-running fits / batch reruns: use the Monitor tool (Apr 2026)

Long Stata fits (multi-hour bootstrap with `cluster bootstrap`, large `reghdfe` with millions of observations, simulation studies) should be background-launched and tailed with the Monitor tool — same pattern as `/data-analysis` and `/audit-reproducibility` for R / Python. The .do file logs to SMCL (`output/NN_log.smcl`). Monitor does not attach to a background job or its stderr: only the stdout of the command you give it becomes events. So run Monitor on a command that tails the log and filters for progress lines and Stata errors, e.g. `tail -f output/NN_log.smcl | grep --line-buffered -E '\{err\}|r\([0-9]+\);|<your progress marker>'`, so Claude can react to errors mid-stream (a multi-hour run needs `persistent: true`, then TaskStop once the job ends).
