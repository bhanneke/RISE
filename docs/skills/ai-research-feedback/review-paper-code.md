<!-- DO NOT EDIT — auto-copied from skills/ai-research-feedback/details/review-paper-code.md -->

# `/review-paper-code`

Reviews an empirical project's LaTeX paper against its Stata, R, or Python code on three fronts: reproducibility (paths, seeds, outputs, dependencies, run order, documentation), code quality, and paper-to-code alignment of tables, variables, sample restrictions, methods, clustering, and fixed effects. Calibrated to treat gaps as items to verify rather than accusations.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-research-feedback/">AI Research Feedback (Claes Bäckman)</a></div><div><b>Category:</b> <code>replication</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-07-05</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>replication</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/claesbackman/AI-research-feedback/contents/Skills/review-paper-code/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-research-feedback/review-paper-code/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/claesbackman/AI-research-feedback/blob/main/Skills/review-paper-code/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/claesbackman/AI-research-feedback?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Review Paper Code

Review a research project's paper and code for reproducibility, code quality, and paper-code alignment. Be constructive, concrete, and calibrated. Treat gaps as items to verify, not accusations.

### Scope

This skill supports:
- LaTeX papers
- Stata (`.do`), R (`.R`, `.r`), and Python (`.py`) code

Default review depth:
- `main`: prioritize the main paper, main scripts, and core outputs
- `full`: inspect all detected code files in scope

If no depth is provided, default to `main`.

### Phase 1: Discover the Project

First parse `$ARGUMENTS`:
- If one argument looks like a `.tex` path, use it as `PAPER_FILE`.
- If one argument looks like a directory path, use it as `CODE_DIR`.
- If one argument is `main` or `full`, use it as `REVIEW_DEPTH`.

If any of the above are missing, auto-detect them.

#### 1. Find the paper

Use Glob to search for `**/*.tex`, excluding obvious build folders such as `_minted-*`, `build/`, `output/`, `.git/`, `node_modules/`.

Identify the main paper file as the best candidate containing `\documentclass` or `\begin{document}`.

If multiple candidates exist, first discard files whose document class is `beamer` (slides) and files whose name or folder suggests an old draft or a response letter (`response*`, `letter*`, `slides*`, `old*`, `archive/`, etc.). Then prefer:
1. A path explicitly provided in `$ARGUMENTS`
2. A file in `Writing/`, `writing/`, `Paper/`, `paper/`, `Draft/`, or the repo root
3. The file that appears to include the most component files via `\input{}` / `\include{}`

Record the result as `PAPER_FILE`.

#### 2. Find the code

If `CODE_DIR` was not provided, look for likely code roots in this order:
- `Code/`
- `Analysis/`
- `code/`
- `analysis/`
- `scripts/`
- `src/`
- `programs/`
- `replication/`

If no single directory is clearly best, use the repo root and limit later discovery to likely code files.

Record the result as `CODE_DIR`.

#### 3. Find code files

Within `CODE_DIR` and subdirectories, find:
- `**/*.do`
- `**/*.R`
- `**/*.r`
- `**/*.py`

Exclude obvious caches, environments, and generated folders where appropriate.

If `REVIEW_DEPTH = main`, prioritize:
- Master scripts such as `main.do`, `master.do`, `run_all.R`, `main.R`, `main.py`, `run.py`
- Files referenced by those scripts
- Files that generate tables, figures, or final datasets
- If no master script exists, select the most central files and cap the initial review set at a reasonable number

If `REVIEW_DEPTH = full`, include all detected code files.

Record:
- `CODE_FILES_ALL`
- `CODE_FILES_REVIEWED`
- languages present

#### 4. Find supporting documentation

Look for:
- `README.md`, `README.txt`, `readme.md`
- `requirements.txt`, `environment.yml`, `pyproject.toml`
- `renv.lock`, `DESCRIPTION`

Record relevant files as available.

#### 5. Handle ambiguity gracefully

If you find a paper and at least some code, continue even if discovery is imperfect.

Only stop if you cannot find either:
- a main paper file, or
- any relevant Stata, R, or Python code files

If you stop, tell the user briefly what was missing and what paths they can pass explicitly.

Before proceeding, tell the user:
- the paper file chosen
- the code directory chosen
- the number of code files detected and the number selected for review
- the review depth
- any ambiguity worth noting

### Phase 2: Read the Paper

Read `PAPER_FILE`.

Recursively read files referenced by:
- `\input{}`
- `\include{}`
- `\subfile{}`

Extract a compact working summary for later cross-checking:
- Paper title
- Main research question
- Main sample description
- Main data sources
- Main dependent variables
- Main explanatory variables or treatments
- Main estimation methods
- Fixed effects and clustering, if stated
- Main sample restrictions
- Main tables and figures only
- Headline quantitative claims only

Do not try to extract every statistic in the paper. Prioritize the main empirical design and the outputs most likely to map to code.

Store this as `PAPER_SUMMARY`.

### Phase 3: Launch 2 Agents in Parallel

In a single message, launch both agents using the Agent tool with `subagent_type: "general-purpose"`.

Each agent must produce a compact, high-signal output. Do not ask for exhaustive per-file prose on every file unless the project is very small.

---

#### AGENT A: Code Reproducibility and Quality

Store as `CODE_REVIEW_SUMMARY`.

Prompt:

> You are reviewing research code for reproducibility and code quality in a social science / economics project.
>
> Files in scope:
> - Reviewed code files: [insert `CODE_FILES_REVIEWED`]
> - README / documentation files: [insert discovered supporting files or "none found"]
>
> Review ONLY the files in scope. Do not use Glob or Grep to discover other files, and ignore any previous review reports (`code_review_report*.md`, `PRE_SUBMISSION_REVIEW_*.md`, `QUICK_REVIEW_*.md`, anything in a `reviews/` folder) — they must not influence your review.
>
> Review the files and produce a compact report focused on the most decision-relevant findings.
>
> Check:
> 1. Hardcoded absolute paths or machine-specific assumptions
> 2. Randomized procedures without an obvious seed in local or upstream execution context
> 3. Outputs that appear to be consumed but not obviously generated in the reviewed pipeline
> 4. Data inputs and whether path conventions are consistent
> 5. Dependency management and software requirements
> 6. Run order and presence of a master script or documented pipeline
> 7. Large commented-out blocks, weak script structure, or hard-to-follow long files
> 8. Opaque transformations, unexplained filters, recodes, merges, or thresholds that are important for interpretation
>
> Use these labels:
> - PASS: looks solid
> - NOTE: minor improvement opportunity
> - VERIFY: worth human confirmation before treating as a problem
> - MISSING: expected project support file or documentation is absent
>
> Output exactly these sections:
>
> ## Overall
> 3-6 bullets on the overall state of the codebase.
>
> ## Top Findings
> Up to 10 items total, ordered by importance.
> Format each item as:
> - [LABEL] Short finding title — file(s): line reference(s) if available — why it matters — what to check next
>
> ## Strengths
> 3-8 bullets with genuine positives.
>
> ## Reproducibility Checklist
> One line each for:
> - Relative paths
> - Random seed practice
> - Outputs generated by pipeline
> - Dependency management
> - Run order
> - README / documentation
>
> Use this format:
> - Check name: PASS / NOTE / VERIFY / MISSING — brief note
>
> ## File Notes
> Include brief notes only for files that have a VERIFY, NOTE, or especially strong positive signal.
> Use at most 1-3 bullets per file.
>
> Be calibrated. If something might be handled in an upstream script, say so.

---

#### AGENT B: Paper-to-Code Mapping

Store as `MAPPING_SUMMARY`.

Prompt:

> You are mapping a research paper's main empirical claims to its code implementation.
>
> Inputs:
> - Paper summary: [insert `PAPER_SUMMARY`]
> - Reviewed code files: [insert `CODE_FILES_REVIEWED`]
> - Code directory: [insert `CODE_DIR`]
>
> Read the code files as needed and identify whether the paper's core empirical design appears in the code. Confine your reading to the listed code files and files inside the code directory that they reference. Ignore any previous review reports (`code_review_report*.md`, `PRE_SUBMISSION_REVIEW_*.md`, `QUICK_REVIEW_*.md`, anything in a `reviews/` folder) and old paper drafts — they must not influence the mapping.
>
> Focus on the main paper elements only:
> 1. Main tables and figures
> 2. Main variables and treatments
> 3. Main sample restrictions and time period
> 4. Main estimation methods
> 5. Fixed effects and clustering, if central
> 6. Main datasets or intermediate analysis files
>
> Use these confidence labels:
> - HIGH: clear and specific match
> - MEDIUM: plausible match but not airtight
> - LOW: weak or indirect match
> - NOT FOUND: no plausible match found in reviewed files
>
> Output exactly these sections:
>
> ## Verified Matches
> Up to 10 bullets.
> Format:
> - Paper element -> Code evidence -> HIGH / MEDIUM -> brief note
>
> ## Items To Verify
> Up to 12 bullets.
> Format:
> - Paper element -> Code evidence or absence -> LOW / NOT FOUND / MEDIUM -> why this deserves a check
>
> ## Likely Discrepancies
> Only include items where paper and code appear to point in different directions.
> Use up to 8 bullets.
>
> ## Coverage Notes
> 3-6 bullets on what was easy to match, what was ambiguous, and what may sit outside the reviewed files.
>
> Be conservative. Do not mark a match HIGH unless the specification, output, or variable mapping is genuinely clear.

### Phase 4: Synthesize

After both agents return, synthesize the results yourself.

Do not launch another critic agent by default. Instead:
- compare the two outputs for agreement and tension
- downgrade any overconfident claims
- note where limited file coverage or naming ambiguity weakens confidence

If the repo is unusually complex and a second-pass critic is truly necessary, you may launch one additional agent. Otherwise, keep the workflow lean.

Create:
- `OVERALL_ASSESSMENT`: 2-4 sentences leading with what works
- `TOP_ACTIONS`: 3-8 concrete next steps, ordered by importance
- `MATCHED_ITEMS`: high-confidence paper-code matches
- `VERIFY_ITEMS`: gaps or ambiguous matches worth checking
- `NOT_FOUND_ITEMS`: important paper elements with no plausible code match in reviewed files

### Phase 5: Write the Report

Write the final report to a `reviews/` subfolder of the current working directory (create it if it does not exist) as:
- `reviews/code_review_report.md`

Keeping the report in `reviews/` prevents it from being picked up as project material by future review runs.

Use this structure:

```markdown
## Code Review Report: [Paper Title]

*Reviewed: [today's date] | Languages: [languages found] | Depth: [REVIEW_DEPTH] | Paper: [PAPER_FILE filename]*

### Overall Assessment

[2-4 sentences. Lead with strengths. Then summarize the main reproducibility or alignment issues worth checking.]

### What's Working Well

- [Specific positive]
- [Specific positive]
- [Specific positive]

### Reproducibility Checklist

| Check | Status | Details |
|---|---|---|
| Relative file paths | [PASS / NOTE / VERIFY / MISSING] | [...] |
| Random seed practice | [PASS / NOTE / VERIFY / MISSING] | [...] |
| Outputs generated by pipeline | [PASS / NOTE / VERIFY / MISSING] | [...] |
| Dependency management | [PASS / NOTE / VERIFY / MISSING] | [...] |
| Run order documented | [PASS / NOTE / VERIFY / MISSING] | [...] |
| README / documentation | [PASS / NOTE / VERIFY / MISSING] | [...] |

### Code Quality Summary

[Short prose summary grouped by module, pipeline stage, or only the files with notable findings. Do not force one paragraph per file if the project is large.]

### Paper-Code Consistency

#### Matched
- [High-confidence match]

#### Items To Verify
- [Paper element] — [what the paper says] — [what the code appears to do] — [why it is worth checking] — [specific suggested next step]

#### Not Found In Reviewed Files
- [Important paper element] — [brief note]

### Suggested Next Steps

1. ...
2. ...
3. ...

### Appendix: Compact Evidence

#### Code Review Summary
[Paste `CODE_REVIEW_SUMMARY`]

#### Paper Summary
[Paste the compact `PAPER_SUMMARY`]

#### Mapping Summary
[Paste `MAPPING_SUMMARY`]
```

Keep the final report readable. Prefer concise, high-signal summaries over exhaustive dumps.

### Final User Message

After writing the report, tell the user:
- that the code review is complete
- that the report was written to `reviews/code_review_report.md`
- the `Overall Assessment`
- 3-5 bullets from `What's Working Well`
- the top 3 suggested next steps
