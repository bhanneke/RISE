---
name: submission-prep
description: Pre-submission checklist for JF, RFS, JFE, or other target journals
---

# Submission Prep Skill

Run a pre-submission checklist tailored to the target journal. Catches common rejection-worthy issues before you submit.

## Examples
- `/submission-prep` -- run full checklist (uses target journal from project's CLAUDE.md)
- `/submission-prep JF` -- run checklist with JF-specific requirements
- `/submission-prep --strict` -- flag warnings as failures

## Workflow

### Step 1: Load Target Journal

Read the project's `CLAUDE.md` for the target journal. If not specified, ask the user. Common targets: **JF, RFS, JFE, RoF, JFQA, MS**.

### Step 2: Run Checks

**2a. Document Structure**
- [ ] Abstract present and within word limit (100--150 words for JF/RFS/JFE)
- [ ] Title length reasonable (<15 words recommended)
- [ ] All expected body sections present (check project's `CLAUDE.md` for section list)
- [ ] Page count within typical range (40--60 pages including appendices for top-3)

**2b. Content Completeness**
- [ ] No `[HUMAN EDIT REQUIRED]` tags remaining in any `.tex` file
- [ ] No `TODO`, `FIXME`, `XXX` comments in `.tex`
- [ ] No `\lipsum` or placeholder text
- [ ] No commented-out sections that should be removed or restored

**2c. Terminology Compliance**
- [ ] Project-specific terminology used consistently (check project's `CLAUDE.md`)
- [ ] No banned words from `academic-writing.md` Section 1

**2d. Tables and Figures**
- [ ] All tables have self-contained captions (sample period, units, variable definitions)
- [ ] All figures have self-contained captions with axis labels
- [ ] All tables and figures are referenced in the text (`\ref` check)
- [ ] Numbers use 2--3 significant digits (not computer output)
- [ ] Tables use booktabs style (`\toprule/\midrule/\bottomrule`, no vertical lines)
- [ ] Figures use vector format (PDF) where possible

**2e. Bibliography**
- [ ] All `\cite{}` keys resolve to `.bib` entries
- [ ] No unused `.bib` entries
- [ ] No duplicate `.bib` entries
- [ ] Consistent BibTeX format (all `@article` have `journal`, `year`, `volume`, `pages`)
- [ ] Proper nouns protected in titles: `{CAPM}`, `{U.S.}`, `{NYSE}`, etc.

**2f. Cross-References**
- [ ] All `\ref{}` and `\eqref{}` resolve to valid labels
- [ ] Equations use `\eqref` not `\ref`
- [ ] Non-breaking spaces used (`Table~\ref`, `Eq.~\eqref`, `Figure~\ref`)

**2g. Writing Quality**
- [ ] No banned words (run `/style-check` if not done recently)
- [ ] No AI-marker words (see `academic-writing.md` for full list)
- [ ] No em-dashes (`---`) in prose
- [ ] No structural AI tells: naked "this", adverb openers, "Together, these results..."
- [ ] Soft-ban words within limits: "highlights" (max 2/paper), "insights" (max 1/paper)
- [ ] No hedge words: somewhat, quite, very (intensifier), arguably, perhaps
- [ ] No previewing: "as we show below", "we will show", "Recall from"
- [ ] Active voice throughout
- [ ] Specific numbers for quantitative claims
- [ ] First sentence is concrete, not throat-clearing

**2h. Compilation**
- [ ] Clean compile with no errors
- [ ] Acceptable warning count (flag if >10 non-font warnings)
- [ ] PDF renders correctly (no missing figures, no ?? references)

**2i. Journal-Specific Requirements**
- [ ] Author information complete (names, affiliations, emails)
- [ ] Acknowledgments section present
- [ ] JEL classification codes present
- [ ] Keywords present (if required by target journal)
- [ ] Data availability statement present (increasingly required)

**2j. Key Results Verification**
- [ ] Key claims in the project's `CLAUDE.md` match the numbers in tables/text
- [ ] Sample period stated consistently across abstract, introduction, and table captions
- [ ] Main results discussed in both introduction and results section

### Step 3: Output

```
SUBMISSION PREP CHECKLIST
=========================

Target: [journal]
Paper: [title from project CLAUDE.md]

PASS: N checks passed
FAIL: M checks failed
WARN: K warnings

--- FAILURES ---
[ ] Line X: [HUMAN EDIT REQUIRED] tag found in section Y
[ ] Table Z: caption missing sample period
[ ] \cite{smith2023}: key not in .bib

--- WARNINGS ---
[!] Abstract is 168 words (target: 100-150)
[!] 14 compilation warnings (non-font)
[!] Page count: 65 pages (typical: 40-60)

--- PASSED ---
[x] All body sections present
[x] All figures referenced in text
[x] Clean compile (0 errors)
[x] Terminology compliant
[etc.]

RECOMMENDATION: [READY TO SUBMIT / FIX N ISSUES FIRST]
```
