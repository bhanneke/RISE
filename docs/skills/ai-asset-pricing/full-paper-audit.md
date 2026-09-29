<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/full-paper-audit.md -->

# `/full-paper-audit`

Runs the section audits across the whole paper, checking cross-section consistency, every citation and all style issues.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code> · <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/full-paper-audit/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/full-paper-audit/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/full-paper-audit/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Full Paper Audit Skill

Comprehensive audit of the entire paper for style compliance, factual consistency, citation correctness, and cross-section coherence.

### Examples
- `/full-paper-audit` -- run complete audit
- `/full-paper-audit --focus style` -- style-only pass
- `/full-paper-audit --focus citations` -- citation-only pass

### Workflow

#### Step 1: Load All Context
1. Read `.claude/rules/academic-writing.md`
2. Read `.claude/rules/banned-words.md`
3. Read `guidance/paper-context.md` (if it exists)
4. Read `.claude/rules/latex-citations.md` (if it exists)
5. Read `main.tex` in full

#### Step 2: Section-by-Section Audit
Discover sections by scanning for `%% BEGIN:` / `%% END:` markers in `main.tex`. Run `/audit-section` on each section sequentially.

#### Step 2b: Math Audit
For sections containing formal environments (any section with `\begin{proposition}`, `\begin{theorem}`, `\begin{lemma}`, or `\begin{proof}`), run `/audit-math`. Include SEVERITY SUMMARY and TOP PRIORITY FIXES in the master report.

#### Step 2c: Editorial Artifact Scan
Before proceeding to cross-section checks, grep the full manuscript for submission-blocking editorial artifacts in active prose (not LaTeX `%` comments):
- `[HUMAN EDIT`, `TODO`, `FIXME`, `XXX`, `[TBD]`, `[PLACEHOLDER]`, `[INSERT`
- Parenthetical editing notes: `(change to`, `(should be`, `(need to`, `(fix this)`, `(update this)`
- Missing-reference markers: `[??]`, `[?]`, `[cite]`, `[ref]`
Any hit is **Critical** and goes to the top of the priority fixes list.

#### Step 3: Cross-Section Consistency
Check that the SAME numbers are used consistently everywhere:
- Do quantitative claims in the introduction match those in the results sections?
- Does the conclusion match the findings reported in the body?
- Are terminology choices consistent across all sections?
- Are counts (sample size, number of variables, etc.) consistent everywhere they appear?

If `guidance/paper-context.md` exists, cross-reference all claims against its canonical values.

#### Step 3b: Caption Consistency
Run `/audit-captions` to check caption-level consistency. Include CRITICAL and IMPORTANT findings in the master report.

#### Step 4: Cross-Reference Audit
- Check all `\ref{}` and `\eqref{}` resolve to valid labels
- Check all tables and figures are referenced in text
- Check no orphaned labels exist

#### Step 5: Citation Completeness
- Check all `\cite{}` keys exist in .bib
- Check all .bib entries are actually cited (flag unused entries)
- Verify key citations via Perplexity (batch mode, high-priority entries first)

#### Step 6: Compile Master Report

#### Step 6b: Aggregate AI-Tell Statistics
After section-by-section audit, run a paper-wide pass for patterns that only emerge at scale:
- **AI-marker word frequency**: Count total occurrences of all Kobak/Gray/Liang markers across the full paper. Report density per 1000 words. Flag if >2 per 1000 words.
- **Transition diversity**: List all paragraph-opening words/phrases. Flag if any single opener appears 3+ times.
- **"By contrast" / "In contrast" density**: Flag if >3 uses paper-wide.
- **Soft-ban accumulation**: Sum all soft-ban word uses across sections. Flag if total exceeds 10.
- **Sentence length distribution**: Sample 20 paragraphs. Report coefficient of variation in sentence length. Flag if CV < 0.25 (too uniform).
- **Intensive reflexive count**: Count "itself"/"themselves" paper-wide. Flag if >4.

### Output

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
