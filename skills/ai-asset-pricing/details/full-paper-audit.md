---
name: full-paper-audit
description: Audit the entire paper -- cross-section consistency, all citations, all style issues
user_invocable: true
---

# Full Paper Audit Skill

Comprehensive audit of the entire paper for style compliance, factual consistency, citation correctness, and cross-section coherence.

## Examples
- `/full-paper-audit` -- run complete audit
- `/full-paper-audit --focus style` -- style-only pass
- `/full-paper-audit --focus citations` -- citation-only pass

## Workflow

### Step 1: Load All Context
1. Read `.claude/rules/academic-writing.md`
2. Read `.claude/rules/banned-words.md`
3. Read `guidance/paper-context.md` (if it exists)
4. Read `.claude/rules/latex-citations.md` (if it exists)
5. Read `main.tex` in full

### Step 2: Section-by-Section Audit
Discover sections by scanning for `%% BEGIN:` / `%% END:` markers in `main.tex`. Run `/audit-section` on each section sequentially.

### Step 2b: Math Audit
For sections containing formal environments (any section with `\begin{proposition}`, `\begin{theorem}`, `\begin{lemma}`, or `\begin{proof}`), run `/audit-math`. Include SEVERITY SUMMARY and TOP PRIORITY FIXES in the master report.

### Step 2c: Editorial Artifact Scan
Before proceeding to cross-section checks, grep the full manuscript for submission-blocking editorial artifacts in active prose (not LaTeX `%` comments):
- `[HUMAN EDIT`, `TODO`, `FIXME`, `XXX`, `[TBD]`, `[PLACEHOLDER]`, `[INSERT`
- Parenthetical editing notes: `(change to`, `(should be`, `(need to`, `(fix this)`, `(update this)`
- Missing-reference markers: `[??]`, `[?]`, `[cite]`, `[ref]`
Any hit is **Critical** and goes to the top of the priority fixes list.

### Step 3: Cross-Section Consistency
Check that the SAME numbers are used consistently everywhere:
- Do quantitative claims in the introduction match those in the results sections?
- Does the conclusion match the findings reported in the body?
- Are terminology choices consistent across all sections?
- Are counts (sample size, number of variables, etc.) consistent everywhere they appear?

If `guidance/paper-context.md` exists, cross-reference all claims against its canonical values.

### Step 3b: Caption Consistency
Run `/audit-captions` to check caption-level consistency. Include CRITICAL and IMPORTANT findings in the master report.

### Step 4: Cross-Reference Audit
- Check all `\ref{}` and `\eqref{}` resolve to valid labels
- Check all tables and figures are referenced in text
- Check no orphaned labels exist

### Step 5: Citation Completeness
- Check all `\cite{}` keys exist in .bib
- Check all .bib entries are actually cited (flag unused entries)
- Verify key citations via Perplexity (batch mode, high-priority entries first)

### Step 6: Compile Master Report

### Step 6b: Aggregate AI-Tell Statistics
After section-by-section audit, run a paper-wide pass for patterns that only emerge at scale:
- **AI-marker word frequency**: Count total occurrences of all Kobak/Gray/Liang markers across the full paper. Report density per 1000 words. Flag if >2 per 1000 words.
- **Transition diversity**: List all paragraph-opening words/phrases. Flag if any single opener appears 3+ times.
- **"By contrast" / "In contrast" density**: Flag if >3 uses paper-wide.
- **Soft-ban accumulation**: Sum all soft-ban word uses across sections. Flag if total exceeds 10.
- **Sentence length distribution**: Sample 20 paragraphs. Report coefficient of variation in sentence length. Flag if CV < 0.25 (too uniform).
- **Intensive reflexive count**: Count "itself"/"themselves" paper-wide. Flag if >4.

## Output

```
FULL PAPER AUDIT
=================

OVERVIEW:
- Total issues: N
- Critical: M
- Suggestions: K
- Sections audited: [N body + M appendices]

CROSS-SECTION CONSISTENCY:
- [list of inconsistencies]

STYLE SUMMARY BY SECTION:
| Section | Banned Words | Passive | Vague Claims | Terminology | Total |
|---------|-------------|---------|--------------|-------------|-------|
| [name]  | ...         | ...     | ...          | ...         | ...   |
[etc.]

CITATION AUDIT:
- Total citations: N
- Verified: X
- Flagged: Y

CROSS-REFERENCES:
- Resolved: X
- Broken: Y

AI-TELL STATISTICS:
- AI-marker words: N (density: X per 1000 words)
- Unique paragraph openers: N out of M paragraphs
- Soft-ban total: N uses
- Sentence length CV: X (target: >0.30)

TOP 10 PRIORITY FIXES:
1. [most important issue]
[etc.]
```
