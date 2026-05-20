<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/devils-advocate.md -->

# `/devils-advocate`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/devils-advocate/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/devils-advocate/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/devils-advocate/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Devil's Advocate Review

Critically examine a slide deck and challenge its design with 5-7 specific pedagogical questions.

**Philosophy:** "We arrive at the best possible presentation through active dialogue."

---

### Setup

1. **Read the target file** (the lecture being challenged)
2. **Read the knowledge base** in `.claude/rules/` for notation conventions and narrative arc
3. If applicable, **read adjacent lectures** for narrative continuity

---

### Challenge Categories

Generate 5-7 challenges from these categories:

#### 1. Ordering Challenges
> "Could students understand this better if we showed X before Y?"

#### 2. Prerequisite Challenges
> "Do students have the background for this notation at this point?"

#### 3. Gap Challenges
> "Should we include an intuitive example before this formal proof?"

#### 4. Alternative Presentation Challenges
> "Here are 2 other ways to visualize/present this concept."

#### 5. Notation Conflict Challenges
> "This symbol conflicts with earlier lecture usage."

#### 6. Cognitive Load Challenges
> "This slide has too many new symbols. Can we split?"

#### 7. Book Vision Challenges
> "If this becomes a book chapter, does this section stand alone?"

---

### Output Format

```markdown
## Devil's Advocate: [Lecture Title]

### Challenges

#### Challenge 1: [Category] — [Short title]
**Question:** [The specific pedagogical question]
**Why it matters:** [What could go wrong]
**Suggested resolution:** [Specific action]
**Slides affected:** [Numbers or titles]
**Severity:** [High / Medium / Low]

[Repeat for 5-7 challenges]

### Summary Verdict
**Strengths:** [2-3 things done well]
**Critical changes:** [0-2 changes before teaching]
**Suggested improvements:** [2-3 nice-to-have changes]
```

---

### Principles

- **Be specific:** Reference exact slides and notation
- **Be constructive:** Every challenge has a suggested resolution
- **Be honest:** If the deck is good, say so
- **Prioritize:** Notation conflicts > missed metaphors
- **Think like a student:** Where do they get lost?
