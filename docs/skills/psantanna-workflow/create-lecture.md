<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/create-lecture.md -->

# `/create-lecture`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

---
name: create-lecture
description: Create a new Beamer lecture `.tex` from source papers and materials, with notation consistency checks and the project's preamble wired in. Use when user says "create a lecture on X", "new lecture from these papers", "start a deck on topic Y", "scaffold a new Beamer file", "build me a lecture from these PDFs". Scaffolds the full deck — NOT for compiling existing `.tex` (use `/compile-latex`).
argument-hint: "[Topic name]"
allowed-tools: ["Read", "Grep", "Glob", "Write", "Edit", "Bash", "Task"]
context: fork
disable-model-invocation: true
---

# Lecture Creation Workflow

Create a beautiful, pedagogically excellent Beamer lecture deck.

**This is a collaborative, iterative process. The instructor drives the vision; Claude is a thinking partner.**

---

## CONSTRAINTS (Non-Negotiable)

1. **Read the knowledge base FIRST** — notation registry, narrative arc, applications database
2. Every new symbol MUST be checked against the notation registry
3. Motivation before formalism — no exceptions
4. Worked example within 2 slides of every definition
5. Max 2 colored boxes per slide
6. No `\pause` or overlay commands (check project rules)
7. Transition slides at major conceptual pivots
8. Thread at least 1 running empirical application throughout
9. All citations verified against the bibliography
10. **Work in batches of 5-10 slides** — share for feedback, don't bulk-dump

---

## WORKFLOW

### Phase 0: Intake & Context (Pre-Flight Report required)

Read the inputs, then produce a Pre-Flight Report in your response before Phase 1 starts.

Inputs to read:
- `.claude/rules/knowledge-base-template.md` — notation registry, narrative arc, applications
- `.claude/rules/content-invariants.md` — INV-1..INV-8 govern slide content
- Any source papers / existing slides the user provided
- The previous lecture's `.tex` (last section + ending slide) if one exists

Required Pre-Flight Report block:

```markdown
## Pre-Flight Report

**Sources read:**
- [source 1]: [one-line takeaway — what notation, what result, what diagram]
- [source 2]: ...

**Notation registry check:**
- New symbols this lecture will introduce: [list]
- Symbols reused from prior lectures: [list, with the lecture each was introduced in]
- Conflicts detected: [none / specific clashes]

**Narrative position:** [Where does this lecture sit in the course arc? What did the previous lecture end on? What does the next lecture need you to set up?]

**Pedagogical goal:** [one sentence]

**Running application:** [which real-world example threads through this deck]
```

State the pedagogical goal, get user confirmation, then proceed.

**First-lecture fallback (fresh fork, empty knowledge base).** If `.claude/rules/knowledge-base-template.md` still has unfilled placeholder tables (no notation registry entries, no applications, no prior lectures in `Slides/`), do NOT halt waiting for it. Instead:

1. Acknowledge the template is empty and we're creating the course's first lecture.
2. Propose a **minimal starter knowledge base** from the user's topic: 5-8 key symbols with conventions, 1-2 running applications, a short narrative arc (intro → main idea → implications). Present for approval.
3. Write the approved stub into the knowledge base template so subsequent lectures inherit it.
4. Continue to Phase 1.

This prevents `/create-lecture` from deadlocking for every new forker.

### Phase 1: Paper Analysis (When Papers Provided)
- Split into chunks, extract key ideas
- Map paper notation → course notation
- Identify slide-worthy content
- Present summary for approval

### Phase 2: Structure Proposal
- Propose outline (5-Act or 3-Part template)
- List TikZ diagrams and R figures needed
- List new notation to introduce
- **GATE: User approves before Phase 3**

### Phase 3: Draft Slides (Iterative)
- Work in batches of 5-10 slides
- Check notation, apply creation patterns
- Quality checks during drafting

### Phase 4: Figures & Code
- R scripts following conventions
- TikZ diagrams in Beamer source (single source of truth)
- Save RDS for future Quarto integration

### Phase 5: Polish & Compile
- Full 3-pass compilation
- Run Devil's Advocate
- Run Substance Review (if domain reviewer configured)
- Update knowledge base with new notation

---

## Post-Creation Checklist

```
[ ] Lecture compiles without errors
[ ] No overfull hbox > 10pt
[ ] All citations resolve
[ ] Every definition has motivation + worked example
[ ] Max 2 colored boxes per slide
[ ] 2-3 Socratic questions embedded
[ ] Transition slides between sections
[ ] At least 1 running application threaded throughout
[ ] New notation added to knowledge base
[ ] Session log updated
[ ] Devil's Advocate run
```


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/create-lecture/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>slides</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>dissemination</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/create-lecture/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/create-lecture/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
