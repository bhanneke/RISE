<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/r-package-check.md -->

# `/r-package-check`

Runs the full R package release gate (docs, tests, R CMD check --as-cran) and triages every ERROR, WARNING and NOTE against CRAN policy.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-09-26</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/r-package-check/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/r-package-check/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/r-package-check/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## `/r-package-check` — R Package Release Gate

Run the document → test → check → triage pipeline that decides whether an R package is releasable, then review the source for the issues `R CMD check` cannot see.

**Input:** `$ARGUMENTS` — the package root (a directory containing `DESCRIPTION`). If blank, autodetect by searching upward/within the working directory for `DESCRIPTION`.

---

### Constraints

- **Follow `.claude/rules/r-package-conventions.md`** — the CRAN-readiness bar (0 errors, 0 warnings, explained notes) is the gate.
- **Treat `man/` and `NAMESPACE` as generated** — regenerate with `devtools::document()`; never hand-edit them.
- **Run the `r-package-reviewer` agent** on the source before declaring the package releasable.
- **Do not bump the version or write to CRAN.** This skill *checks*; the human decides when to submit.

---

### Workflow Phases

#### Phase 0: Pre-Flight Report

```markdown
### Pre-Flight Report — R Package Check

**Package:** [name + version from DESCRIPTION]
**Root:** [path]
**Exported functions:** [from NAMESPACE / `@export` count]
**Dependencies:** Imports [list] · Suggests [list] · Depends [list]
**Toolchain available:** devtools [✓/✗], roxygen2 [✓/✗], testthat [✓/✗], R CMD [✓/✗], covr [✓/✗]
**Plan:** document → test → check --as-cran → triage → review
```

Detect the toolchain with a quick probe; if `devtools`/`R CMD` is missing, stop and tell the user what to install.

```bash
Rscript -e 'cat("devtools:", requireNamespace("devtools", quietly=TRUE),
               "roxygen2:", requireNamespace("roxygen2", quietly=TRUE),
               "testthat:", requireNamespace("testthat", quietly=TRUE),
               "covr:", requireNamespace("covr", quietly=TRUE), "\n")'
```

#### Phase 1: Document

Regenerate `man/` + `NAMESPACE` and detect drift (generated docs that were not committed):

```bash
Rscript -e 'devtools::document("[pkg]")'
git -C "[pkg]" status --short man/ NAMESPACE   # any diff = generated docs were stale
```

If `git status` shows changes, flag: the committed `man/`/`NAMESPACE` were out of sync with the roxygen blocks.

#### Phase 2: Test

```bash
Rscript -e 'devtools::test("[pkg]")'
```

Report failures and (if `covr` is available, Phase 4) coverage of exported functions.

#### Phase 3: Check (`--as-cran`)

Run the full check. **This is slow** (minutes) — background-launch and stream with the **Monitor tool** rather than blocking:

```bash
Rscript -e 'devtools::check("[pkg]", args = "--as-cran")'
## or: R CMD build [pkg] && R CMD check --as-cran [pkg]_*.tar.gz
```

Then **triage every result** into a table:

| Result | Tier | CRAN-policy meaning | Action |
|---|---|---|---|
| … | ERROR / WARNING / NOTE | … | fix / justify |

- **ERROR / WARNING** → must fix before submission.
- **NOTE** → fix if cheap; otherwise write the justification you'd put in `cran-comments.md` (e.g., "New submission", "Found the following (possibly) invalid URLs … the URL is correct and reachable").

#### Phase 4: Coverage (optional)

```bash
Rscript -e 'covr::package_coverage("[pkg]")'
```

Report per-function coverage; flag exported functions with 0% coverage.

#### Phase 5: Source Review

```
Delegate to the r-package-reviewer agent:
"Review the package source at [pkg]"
```

The agent is read-only and returns its report; save it to `quality_reports/[pkg]_package_review.md`. Address Critical (CRAN-policy violations) and High (check WARNINGs) findings.

#### Phase 6: Release Gate + Report

Save a report to `quality_reports/[package]_package_check.md` and present a verdict:

```markdown
### Release Gate — [package] [version]
- R CMD check --as-cran: E errors, W warnings, N notes
- Tests: P passed, F failed
- Coverage: X% of exported functions
- r-package-reviewer: C critical, H high
- **Verdict:** RELEASABLE / FIX-FIRST / POLICY-VIOLATION

#### CRAN-submission checklist
[ ] 0 errors, 0 warnings; each note justified in cran-comments.md
[ ] Version bumped + NEWS.md updated
[ ] devtools::check_win_devel() / R-hub on other platforms (note: run separately)
[ ] Reverse-dependency check if this is an update (revdepcheck)
```

---

### Important

- **`--as-cran` or it doesn't count.** A plain `R CMD check` misses the policy checks that actually gate submission.
- **Generated files are generated.** If docs drift, the fix is `devtools::document()`, not editing `.Rd`.
- **The gate is 0/0/explained.** 0 errors, 0 warnings, every remaining note justified — nothing less is "CRAN-ready."
- **This skill does not submit.** Cross-platform checks (win-devel, R-hub) and the actual `devtools::release()` are the maintainer's call.

### Long-running checks: use the Monitor tool

`R CMD check --as-cran` and `covr` can run for several minutes. Don't block on them, and don't poll with `sleep`: start the **Monitor tool** with a command that runs the check itself, tees the full output to a log, and prints only the lines you would act on, e.g. `Rscript -e 'devtools::check("[pkg]", args = "--as-cran")' 2>&1 | tee quality_reports/r-package-check.log | grep --line-buffered -E 'ERROR|WARNING|NOTE|Status:|[Ee]rror'`. The watch ends when the check exits; set `timeout_ms` above the default 5 minutes (max 3600000). The filter must match failure as well as success, because silence looks the same as "still running". If you only need one notice when the check finishes, run it with Bash `run_in_background: true` instead and read the log when the job reports its exit. Monitor has no job-id parameter, so it cannot attach to a job already running in the background; see `data-analysis/SKILL.md` for the log-and-tail variant.
