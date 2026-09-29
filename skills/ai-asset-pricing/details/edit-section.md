---
name: edit-section
description: Revise an existing section for style, clarity, and correctness
user_invocable: true
---

# Edit Section Skill

When this skill is invoked, follow this structured workflow to revise an existing section of the paper.

## Input

The user specifies which section to edit (file path or section key) and what kind of revision (style cleanup, content revision, restructuring, or specific feedback to address).

## Workflow

### Step 1: Read Current Text
1. Read the target section from `main.tex`
2. Note the current structure, length, and key claims

### Step 2: Load Standards
1. Read `.claude/rules/academic-writing.md` for banned words, terminology, and style rules
2. Read `.claude/rules/banned-words.md` for the full banned-word list
3. Read `guidance/paper-context.md` for correct claims, numbers, and paper framing (if it exists)

### Step 3: Diagnose Issues
Run through each check category:

**A. Banned Words** (read `banned-words.md` for the full current list; key examples: delve, crucial, comprehensive, utilize; AI markers: underscores, showcasing, pivotal, intricate, encompass, aligns with; previewing: "as we show below", "Recall from"; filler: of course, obviously, in other words)
**B. Opening Quality** -- Does sentence 1 state a concrete finding?
**C. Voice and Tense** -- Flag passive constructions
**D. Quantitative Precision** -- Numbers instead of adjectives; cross-check against paper-context.md if available
**E. Terminology** -- If `guidance/paper-context.md` defines a terminology table, check compliance. Otherwise flag any terms used inconsistently within the section.
**F. Self-Praise** -- Flag "striking", "important contribution", "novel"
**G. Concision** -- Cut repeated ideas, "in other words", sentences that don't earn their place
**H. Em-Dashes** -- No `---` in prose (rewrite with commas, semicolons, colons, or parentheses)
**I. Structural AI Tells** -- Check for patterns from academic-writing.md: naked "this" without noun, "Importantly,"/"Notably,"/"Specifically," as sentence openers, "Together, these results..." openers (max 1/paper), "In this section, we..." throat-clearing, "This finding" repetition (max 1/paper), "Overall," as paragraph opener. Check soft-ban counts: "highlights" (max 2/paper), "insights" (max 1/paper)
**J. Hedge Words** -- Delete or quantify: somewhat, quite, very (intensifier), rather (hedge), arguably, perhaps. Replace with magnitudes. (See academic-writing.md "Kill Hedge Words")
**K. Nominalizations** -- Prefer verbs: "conduct an analysis" → "analyze", "provide evidence" → "show". (See academic-writing.md "Prefer Verbs over Nominalizations")

### Step 4: Load Exemplar for Reference
Read the relevant exemplar from `.claude/exemplars/` to check structural patterns (if exemplars exist for this project).

### Step 5: Revise
Make targeted edits:
1. Fix all banned words (provide specific replacements)
2. Fix terminology violations
3. Tighten passive voice
4. Add specific numbers where vague claims exist
5. Cut redundant sentences
6. Restructure opening if needed

**Preserve**: Do not change content that is correct and well-written. Minimize diff size.

### Step 6: Verify Citations
Check all `\cite{}` keys against the .bib file. For new citations, verify via Perplexity (see `.claude/rules/latex-citations.md` if it exists).

### Step 7: Present Changes
Show the user:
1. A categorized summary of changes (banned words, voice, precision, terminology, etc.)
2. The revised LaTeX text
3. Any `[HUMAN EDIT REQUIRED]` flags for claims that could not be verified
