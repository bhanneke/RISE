<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/audit-section.md -->

# `/audit-section`

Deep audit of one section of a paper for style, factual accuracy, citations and logical flow.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>audit</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-03-12</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>revision-editing</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/audit-section/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/audit-section/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/audit-section/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Audit Section Skill

Comprehensive single-section audit combining style checking, factual verification, citation auditing, and logical flow analysis.

### Examples
- `/audit-section introduction` -- deep audit of the introduction
- `/audit-section data` -- audit the data section
- `/audit-section results` -- audit the results section

### Workflow

#### Step 1: Load Context
1. Read `.claude/rules/academic-writing.md` for style rules
2. Read `.claude/rules/banned-words.md` for hard/soft bans
3. Read `.claude/rules/grammar-punctuation.md` for grammar conventions
4. Read `.claude/rules/latex-citations.md` for citation protocol
5. If the project has `guidance/paper-context.md`, read it for correct claims and numbers
6. Read the target section from `main.tex` (use `/extract-section`)

#### Step 2: Style Audit
Run the full `/style-check` analysis:
- Banned words, throat-clearing, passive voice, superlatives, vague claims, self-praise
- Structural AI tells: em-dashes, AI-marker words (per Kobak/Liang), naked "this", adverb openers, "Together, these results...", soft-ban counts
- Hedge words & previewing: somewhat/quite/very/arguably/perhaps (Nikolov); "as we show below"/"Recall from" (Cochrane); nominalizations (Williams)
- See `banned-words.md` and `academic-writing.md` for the full current lists

#### Step 3: Factual Accuracy
If the project has `guidance/paper-context.md`, cross-reference every quantitative claim:
- Do numerical claims match the paper's canonical values?
- Do table references match actual table content?
- Flag any inconsistency between text claims and tables/figures

If no paper-context file exists, flag claims that cannot be verified.

#### Step 4: Citation Audit
For each citation in the section:
- Verify key exists in .bib
- Check citation supports the claim being made (not just existence but relevance)
- Flag citations used out of context

#### Step 5: Logical Flow
- Does the section follow a logical progression?
- Are transitions between paragraphs smooth?
- Is there redundancy (same point made twice)?
- Does the opening paragraph set up what follows?
- Does the section deliver on its implicit promise?

#### Step 6: Economic Reasoning
- Are economic arguments sound?
- Are mechanisms explained correctly and consistently with the paper's framework?
- Do the results follow from the methodology described?

### Output

```
SECTION AUDIT: [section name]
================================

STYLE ISSUES: N total (M critical, K suggestions)
[categorized list]

FACTUAL ACCURACY:
- [list of verified/flagged claims with specific numbers]

CITATION AUDIT:
- [status of each citation in section]

LOGICAL FLOW:
- [structural observations and suggestions]

ECONOMIC REASONING:
- [any issues with mechanism descriptions]

PRIORITY FIXES:
1. [highest priority issue]
2. [second priority]
3. [etc.]

SUGGESTED REWRITES:
[specific rewrite suggestions for the worst passages]
```
