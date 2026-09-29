---
name: style-check
description: Analyze LaTeX text for violations of academic writing standards
---

# Style Check Skill

When this skill is invoked, analyze the provided text for violations of the academic writing standards in `.claude/rules/academic-writing.md`.

## Examples

- `/style-check` -- check the current .tex file
- `/style-check introduction` -- check only the introduction section
- `/style-check projects/my_paper/latex/main.tex` -- check a specific file

## Input

The user provides a `.tex` file path or text block to analyze.

## Workflow

1. Read `.claude/rules/academic-writing.md` for the full rule set
2. Read the project's `CLAUDE.md` for project-specific terminology
3. Read the target text (from file path or section markers)
4. Run all 13 analysis categories below
5. Check citations against the project's `.bib` file
6. Produce the structured report

## Analysis Categories

### 1. Banned Word Scan
Check for all terms in `academic-writing.md` Section 1 and flag each occurrence:
- delve, crucial, comprehensive, multifaceted, utilize, leverage, facilitate
- endeavor, paramount, myriad, plethora, noteworthy
- "it is important to note", "it should be noted", "in this regard"
- "the fact that", "in order to", "due to the fact that"
- "a number of", "the vast majority of", "at the present time"
- "in the context of", "with respect to", "in terms of", "as such"
- All AI-marker words: underscores, showcasing, pivotal, intricate, meticulous, illuminate, unveil, bolster, realm, landscape, foster, encompass, aligns with, shed light on, profound, grappling, etc.

### 2. Throat-Clearing Detection
Flag openings that don't state a concrete finding:
- "The literature has long..."
- "Financial economists have wondered..."
- "An important question..."
- "Recent years have witnessed..."
- "It is well known that..."
- "There has been growing interest in..."
- "A growing body of literature..."

### 3. Passive Voice Check
Flag passive constructions:
- "it is shown that" -> "we show that"
- "it was found that" -> "we find that"
- "can be seen" -> "shows"
- "has been documented" -> "[Author] documents"

### 4. Superlative Stacking
Flag sequences of emphasis words:
- "crucial new insights into this important phenomenon"
- "significant novel contribution to this vital area"
- "robust striking results that highlight key findings"

### 5. Vague Quantitative Claims
Flag imprecise language when numbers should be given:
- "substantial premium" -> give the number
- "large bias" -> give the magnitude
- "many factors" -> give the count
- "significant at conventional levels" -> give the t-stat
- "economically large" -> give the percentage

### 6. Terminology Violations (project-configurable)
Check for incorrect terminology per the project's `CLAUDE.md`. Each project defines its own preferred/banned terminology. If no project-specific terminology is defined, skip this category.

### 7. Self-Praise Detection
Flag adjectives that praise the work:
- "striking results"
- "important contribution"
- "novel approach"
- "comprehensive analysis"
- "rigorous methodology"
- "impressive performance"

### 8. Domain-Specific Consistency (project-configurable)
Check for consistency in how results are presented, per the project's conventions. For example, if the project requires decomposing costs into components, flag any place where costs are lumped together.

### 9. Citation Check
For each `\cite{}` or `\citep{}` in the text:
- Extract the BibTeX key
- Verify it exists in the project's `.bib` file
- Flag any missing keys
- For new citations: note they should be verified via Perplexity (see `.claude/rules/latex-citations.md`)

### 10. Structural AI Tells
Check for patterns flagged by Kobak et al. (2025) and Liang et al. (2024):
- **Em-dashes** (`---`) in prose: rewrite with commas, semicolons, colons, or parentheses
- **En-dashes** (`--`) as parenthetical asides: only valid for ranges and compound modifiers
- **"Together, these results..."** as paragraph opener (max 1 per paper)
- **"This finding"** as sentence opener (max 1 per paper)
- **Naked "this"** without a noun ("This implies..." -> "This result implies...")
- **"Importantly," / "Notably," / "Specifically,"** as sentence-opening adverbs
- **"In this section, we..."** throat-clearing
- **"Overall,"** as paragraph opener
- **Soft-ban overuse**: "highlights" (max 2/paper), "insights" (max 1/paper)
- **Uniform paragraph length**: flag if 5+ consecutive paragraphs have similar length
- **Consecutive same-structure paragraph openers**: 2+ consecutive paragraphs with same grammatical pattern
- **Content-free meta-announcements**: "We now turn to...", "We next examine..."
- **Closing-summary paragraphs**: "In summary," within non-conclusion sections
- **Gerund-opener density**: 2+ gerund-phrase openers in same paragraph
- **Sentence length uniformity**: 5+ consecutive sentences of similar word count
- **"First...Second...Third" overuse**: more than one enumeration per subsection
- **Intensive reflexive overuse**: "itself", "themselves" as emphasis (max 2/section)

### 11. Hedge Words & Previewing (Cochrane, Nikolov)
Flag filler hedge words:
- "somewhat", "rather" (as hedge), "quite", "very" (as intensifier), "arguably", "perhaps"
- Replace with magnitude: "somewhat larger" -> "12 basis points larger"

Flag previewing/recalling:
- "as we show below", "we will show", "Recall from Section X"

Flag nominalizations:
- "conduct an analysis" -> "analyze"
- "provide evidence that" -> "show that"

### 12. Finance-Specific Formulaic Patterns
Flag cliche constructions:
- "Our findings contribute to the growing literature on..."
- "speaks to the broader debate"
- "a battery of robustness checks"
- "the economic mechanism is as follows"
- "We exploit variation in..."
- "is not statistically significantly different from zero"

### 13. Editorial Artifact Detection
Scan for leftover editing comments and placeholders in active prose:
- `[HUMAN EDIT REQUIRED` -- draft placeholders
- `(change to...` / `(should be...` / `(fix this)` -- editing notes
- `TODO` / `FIXME` / `XXX` -- developer-style markers
- `[TBD]` / `[PLACEHOLDER]` / `[INSERT` -- slot markers
- `[??]` / `[?]` / `[cite]` / `[ref]` -- missing-reference markers

**Severity**: Always **Critical**. These are submission-blocking artifacts.

## Output Format

```
STYLE CHECK REPORT
==================

File: [filename]
Lines analyzed: [count]

BANNED WORDS FOUND:
- Line X: "delve" -> suggest "examine" or "investigate"         [Critical]
- Line Y: "utilize" -> suggest "use"                            [Critical]

THROAT-CLEARING:
- Line W: "The literature has long..." -> Start with concrete claim  [Critical]

PASSIVE VOICE:
- Line V: "it is shown that" -> "we show that"                 [Suggestion]

[... all categories ...]

SUMMARY:
- Total issues: N
- Critical (must fix): M
- Suggestions: K
```

## Severity Levels
- **Critical**: Banned words, missing citation keys, structural AI tells (em-dashes, formulaic adverb openers), editorial artifacts
- **Suggestion**: Passive voice, vague claims, self-praise, naked "this", hedge words, nominalizations

## Usage Notes

1. Run on any `.tex` file, text block, or full document
2. Prioritize issues by severity (Critical first)
3. Provide specific line numbers where possible
4. Always suggest concrete replacements
5. Focus on actionable feedback
