<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/check-consistency.md -->

# `/check-consistency`

Fast scan across sections for inconsistent numbers, terminology and cross-references.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/check-consistency/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/check-consistency/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/check-consistency/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Check Consistency Skill

Fast, focused scan for cross-section inconsistencies in `main.tex`. Lighter than `/full-paper-audit` -- designed for iterative use during editing.

### Examples
- `/check-consistency` -- full scan of main.tex
- `/check-consistency numbers` -- only check quantitative claims
- `/check-consistency terminology` -- only check terminology consistency

### Workflow

#### Step 1: Load Reference Values
Read `guidance/paper-context.md` to get canonical values (if it exists):
- Key quantitative results and their canonical magnitudes
- Sample description (date range, number of observations, variable counts)
- Any other numbers that appear in multiple sections

If no paper-context file exists, the skill still works by cross-referencing sections against each other (without a canonical reference).

#### Step 2: Quantitative Consistency
Grep `main.tex` for all quantitative claims and cross-reference:
- Percentages and basis points mentioning specific variables or factors
- Sample period mentions (start date, end date, number of periods)
- Counts (variables, observations, subsamples, etc.)
- Any number that appears in more than one section

Flag: mismatches between text claims and canonical values (if available), or between sections.

#### Step 3: Terminology Consistency
If `guidance/paper-context.md` defines a terminology table, grep across all sections for violations.

Also check for within-paper drift regardless of paper-context:
- Same concept called different names in different sections
- Inconsistent abbreviation introduction (defined in one section, used without definition in another)
- Check against `.claude/rules/banned-words.md` for hard-banned terms

#### Step 4: Cross-Reference Integrity
1. Extract all `\ref{...}` and `\eqref{...}` targets
2. Extract all `\label{...}` definitions
3. Flag any `\ref` or `\eqref` that points to a non-existent label
4. Flag any `\ref` used where `\eqref` should be (equation references)
5. Check that all tables and figures are cited at least once in the text

#### Step 5: Section Cross-References
Check that claims about other sections are accurate:
- "As shown in Section X" -- does Section X actually show this?
- "Table Y reports" -- does Table Y match the claim?
- "See Appendix Z" -- does the appendix contain the referenced content?

#### Step 5b: Caption Consistency
Run `/audit-captions`. Include CRITICAL and IMPORTANT findings in the output.

#### Step 6: Output

```
CONSISTENCY CHECK
=================

QUANTITATIVE MISMATCHES: [N found]
- Line X: claims "[value]" but canonical value is "[value]" for [variable]
- Line Y: says "[count]" but paper-context.md says "[count]"
(or: "No paper-context.md — cross-section comparison only")

TERMINOLOGY VIOLATIONS: [N found]
- Line X: "[deprecated term]" (should be "[correct term]")
- Line Y: "[term A]" in this section vs "[term B]" in [other section]

REFERENCE INTEGRITY: [N issues]
- Line X: \ref{eq:decomp} should be \eqref{eq:decomp}
- Line Y: \ref{fig:missing} -- label not found

CROSS-SECTION CONSISTENCY: [N issues]
- Line X claims "Table 3 shows..." but Table 3 actually shows...

SUMMARY:
- Critical issues: N
- Warnings: M
- All clear: [list of checks that passed]
```
