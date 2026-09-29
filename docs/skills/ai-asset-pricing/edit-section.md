<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/edit-section.md -->

# `/edit-section`

Revises an existing paper section for style, clarity and correctness under the repo's writing rules.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>editing</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/edit-section/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/edit-section/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/edit-section/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Edit Section Skill

When this skill is invoked, follow this structured workflow to revise an existing section of the paper.

### Input

The user specifies which section to edit (file path or section key) and what kind of revision (style cleanup, content revision, restructuring, or specific feedback to address).

### Workflow

#### Step 1: Read Current Text
1. Read the target section from `main.tex`
2. Note the current structure, length, and key claims

#### Step 2: Load Standards
1. Read `.claude/rules/academic-writing.md` for banned words, terminology, and style rules
2. Read `.claude/rules/banned-words.md` for the full banned-word list
3. Read `guidance/paper-context.md` for correct claims, numbers, and paper framing (if it exists)

#### Step 3: Diagnose Issues
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

#### Step 4: Load Exemplar for Reference
Read the relevant exemplar from `.claude/exemplars/` to check structural patterns (if exemplars exist for this project).

#### Step 5: Revise
Make targeted edits:
1. Fix all banned words (provide specific replacements)
2. Fix terminology violations
3. Tighten passive voice
4. Add specific numbers where vague claims exist
5. Cut redundant sentences
6. Restructure opening if needed

**Preserve**: Do not change content that is correct and well-written. Minimize diff size.

#### Step 6: Verify Citations
Check all `\cite{}` keys against the .bib file. For new citations, verify via Perplexity (see `.claude/rules/latex-citations.md` if it exists).

#### Step 7: Present Changes
Show the user:
1. A categorized summary of changes (banned words, voice, precision, terminology, etc.)
2. The revised LaTeX text
3. Any `[HUMAN EDIT REQUIRED]` flags for claims that could not be verified
