<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/write-section.md -->

# `/write-section`

Writes a new section or subsection of an empirical finance paper under the repo's academic writing rules.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-24</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/write-section/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/write-section/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/write-section/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Write Section Skill

When this skill is invoked, follow this structured workflow to write a new section or subsection of a paper.

### Examples

- `/write-section introduction` -- write the introduction
- `/write-section "robustness checks"` -- write a specific subsection
- `/write-section conclusion` -- write the conclusion

### Input

The user specifies which section to write (by name or description) and any additional instructions.

### Workflow

#### Step 1: Load Context
1. Read the project's `CLAUDE.md` for paper structure, key claims, terminology, and domain concepts
2. Read `.claude/rules/academic-writing.md` for style rules and banned words
3. Read `.claude/rules/latex-conventions.md` for LaTeX formatting, section markers, and figure/table conventions
4. Read the current `.tex` file(s) to identify what already exists vs. what needs to be written

#### Step 2: Load Exemplar
Read `.claude/exemplars/cochrane_writing_tips.md` for foundational writing principles. If the project has its own exemplars (in `literature/` or referenced in the project's `CLAUDE.md`), read those too.

Extract the structural pattern appropriate for the section type:
- **Introduction**: Punchline first, enumerate contributions, literature after your contribution
- **Data / Methods**: State approach upfront, define variables precisely, explain identifying assumptions
- **Results**: Lead with main result, give economic magnitudes, address surprises immediately
- **Conclusion**: 2 paragraphs maximum, enumerate contributions, no speculation
- **Abstract**: One sentence per key finding, specific numbers

#### Step 3: Load Technical References (if needed)
If writing about methodology or formal results:
- Read existing methodology/model sections for notation and definitions
- Use notation consistently with what's already in the paper

#### Step 4: Draft
Write the section following these rules:
1. **First sentence**: Concrete finding or claim, no throat-clearing
2. **Structure**: Follow the appropriate paragraph flow for the section type
3. **Voice**: Active, present tense for results ("Table 3 shows...")
4. **Quantitative claims**: Use specific numbers from the project's results
5. **Terminology**: Follow the project's `CLAUDE.md` for paper-specific terms
6. **LaTeX**: Follow `.claude/rules/latex-conventions.md` conventions
7. **Length**: Every sentence earns its place
8. **Citations**: Check all `\cite{}` keys exist in the `.bib` file. For any NEW citation, follow the verification protocol in `.claude/rules/latex-citations.md`. Never cite from memory.

#### Step 5: Self-Validate
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

#### Step 6: Compile Check (optional)
If requested, verify LaTeX compiles using the paths from canonical local state reported by `tools/bootstrap.py audit` (or a repo-root compatibility shim if present):
```bash
cd {latex_dir} && pdflatex -interaction=nonstopmode {file} && bibtex {stem} && pdflatex -interaction=nonstopmode {file} && pdflatex -interaction=nonstopmode {file}
```

### Output

Present the LaTeX text ready to insert. Include:
1. The section content
2. A brief note on any `[HUMAN EDIT REQUIRED]` flags
3. Any structural decisions made (and why)
