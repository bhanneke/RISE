---
name: write-section
description: Write a new section or subsection of an empirical finance paper following academic writing rules
---

# Write Section Skill

When this skill is invoked, follow this structured workflow to write a new section or subsection of a paper.

## Examples

- `/write-section introduction` -- write the introduction
- `/write-section "robustness checks"` -- write a specific subsection
- `/write-section conclusion` -- write the conclusion

## Input

The user specifies which section to write (by name or description) and any additional instructions.

## Workflow

### Step 1: Load Context
1. Read the project's `CLAUDE.md` for paper structure, key claims, terminology, and domain concepts
2. Read `.claude/rules/academic-writing.md` for style rules and banned words
3. Read `.claude/rules/latex-conventions.md` for LaTeX formatting, section markers, and figure/table conventions
4. Read the current `.tex` file(s) to identify what already exists vs. what needs to be written

### Step 2: Load Exemplar
Read `.claude/exemplars/cochrane_writing_tips.md` for foundational writing principles. If the project has its own exemplars (in `literature/` or referenced in the project's `CLAUDE.md`), read those too.

Extract the structural pattern appropriate for the section type:
- **Introduction**: Punchline first, enumerate contributions, literature after your contribution
- **Data / Methods**: State approach upfront, define variables precisely, explain identifying assumptions
- **Results**: Lead with main result, give economic magnitudes, address surprises immediately
- **Conclusion**: 2 paragraphs maximum, enumerate contributions, no speculation
- **Abstract**: One sentence per key finding, specific numbers

### Step 3: Load Technical References (if needed)
If writing about methodology or formal results:
- Read existing methodology/model sections for notation and definitions
- Use notation consistently with what's already in the paper

### Step 4: Draft
Write the section following these rules:
1. **First sentence**: Concrete finding or claim, no throat-clearing
2. **Structure**: Follow the appropriate paragraph flow for the section type
3. **Voice**: Active, present tense for results ("Table 3 shows...")
4. **Quantitative claims**: Use specific numbers from the project's results
5. **Terminology**: Follow the project's `CLAUDE.md` for paper-specific terms
6. **LaTeX**: Follow `.claude/rules/latex-conventions.md` conventions
7. **Length**: Every sentence earns its place
8. **Citations**: Check all `\cite{}` keys exist in the `.bib` file. For any NEW citation, follow the verification protocol in `.claude/rules/latex-citations.md`. Never cite from memory.

### Step 5: Self-Validate
Before presenting the draft, check:
- [ ] No banned words (see `academic-writing.md` Section 1 for full list)
- [ ] No throat-clearing opening
- [ ] Active voice throughout
- [ ] No stacked superlatives
- [ ] Specific numbers for quantitative claims
- [ ] Project-specific terminology consistent
- [ ] No self-praise ("striking", "important contribution", "comprehensive")
- [ ] No em-dashes (`---`) in prose (use commas, semicolons, colons, or parentheses)
- [ ] No structural AI tells (see `academic-writing.md`)
- [ ] No hedge words: somewhat, quite, very (intensifier), rather, arguably, perhaps
- [ ] No previewing: "as we show below", "we will show", "Recall from"
- [ ] Soft-ban words within per-paper limits
- [ ] Prefer verbs over nominalizations
- [ ] No editorial artifacts: TODO, FIXME, [TBD], [PLACEHOLDER], [??]
- [ ] Flag uncertain claims with `[HUMAN EDIT REQUIRED: ...]`

### Step 6: Compile Check (optional)
If requested, verify LaTeX compiles using the paths from canonical local state reported by `tools/bootstrap.py audit` (or a repo-root compatibility shim if present):
```bash
cd {latex_dir} && pdflatex -interaction=nonstopmode {file} && bibtex {stem} && pdflatex -interaction=nonstopmode {file} && pdflatex -interaction=nonstopmode {file}
```

## Output

Present the LaTeX text ready to insert. Include:
1. The section content
2. A brief note on any `[HUMAN EDIT REQUIRED]` flags
3. Any structural decisions made (and why)
