---
name: review-r
description: Read-only R code review protocol for `.R` scripts. Checks code quality, reproducibility, domain correctness, tidyverse idioms, and professional standards; produces a report without editing. Use when user says "review this R script", "check the R code", "audit the analysis code", "code review on the R", or when an R file is touched as part of a paper submission. NOT for running the code — pair with `/audit-reproducibility` for numeric verification.
argument-hint: "[filename or 'all' or 'LectureN']"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Agent", "Task"]
disallowed-tools: ["Edit", "MultiEdit"]
---

# Review R Scripts

Run the comprehensive R code review protocol.

## Steps

1. **Identify scripts to review:**
   - If `$ARGUMENTS` is a specific `.R` filename: review that file only
   - If `$ARGUMENTS` is `LectureN`: review all R scripts matching that lecture
   - If `$ARGUMENTS` is `all`: review all R scripts in `scripts/R/` and `Figures/*/`

2. **For each script, launch the `r-reviewer` agent** with instructions to:
   - Follow the full protocol in the agent instructions
   - Read `.claude/rules/r-code-conventions.md` for current standards
   - Return its report as its final response (ending with the findings `json` block); this skill saves it to `quality_reports/[script_name]_r_review.md` — the agent is read-only

3. **After all reviews complete**, present a summary:
   - Total issues found per script
   - Breakdown by severity (Critical / High / Medium / Low)
   - Top 3 most critical issues

4. **Leave the R source files unchanged** — the report goes to the user, who decides what to fix.
   Only produce reports. Fixes are applied after user review.
