<!-- DO NOT EDIT — auto-copied from skills/evoskills/details/research-survey.md -->

# `research-survey`

Survey/literature review generation

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
name: research-survey
description: "Generates structured literature survey reports from collected papers using a multi-stage pipeline: outline generation (query-type adaptive) → draft survey → section-by-section expansion → summary section refinement → final assembly. Produces survey-grade output with taxonomy-based method analysis, LaTeX formalizations, comparative tables, and dense citations. Use when: user wants a literature review, research survey, field overview, or systematic synthesis of multiple papers. Do NOT use for finding/searching papers (use paper-navigator), generating research ideas (use research-ideation), or writing a paper's Related Work section (use paper-writing)."
allowed-tools: "write_file edit_file read_file think_tool"
metadata:
  author: EvoScientist
  version: '1.0.0'
  tags: [core, research, literature, survey, synthesis]
---

# Research Survey

Generates high-quality, survey-grade literature reviews from papers collected by `paper-navigator`.

```
paper-navigator (collect 30-120 papers)
    ↓
Stage 1: Generate Outline (query-type adaptive structure)
    ↓
Stage 2: Draft Survey (outline + top-30 papers)
    ↓
Stage 3: Expand Sections (draft + all papers, section-by-section)
    ↓
Stage 4: Generate Section Summaries
    ↓
Stage 5: Refine Summary Sections (Abstract/Intro/Conclusion)
    ↓
Stage 6: Assemble + References
```

## When to Use

- User asks for a "literature review", "survey", "field overview", or "systematic review"
- User has collected papers and wants them synthesized into a structured report
- User wants to understand the full landscape of a research field

## When NOT to Use

- **Finding papers** → use `paper-navigator` first, then come here
- **Generating research ideas** → use `research-ideation`
- **Writing a Related Work section for a paper** → use `paper-writing`

## Dependency: paper-navigator

This skill requires papers as input. If the user hasn't provided papers, **first invoke `paper-navigator`** (Workflow 1, target 30-120 papers) to collect them.

**CRITICAL: All paper discovery MUST use the `paper-navigator` skill and its scripts (scholar_search, citation_traverse, arxiv_monitor, recommend, etc.). Using WebSearch, WebFetch, or any generic web search tool for finding papers is PROHIBITED.** Generic web search cannot access Semantic Scholar, citation graphs, or academic recommendation systems. Only `paper-navigator` provides the academic search infrastructure needed for survey-quality literature collection.

---

## Stage 1: Generate Outline

**This is a two-phase process.** Different fields have different survey conventions — a clinical systematic review looks nothing like a CS methods survey. First generate a domain-appropriate template, then create the detailed outline.

### Phase 1A: Generate Domain-Specific Survey Template

Before outlining, identify the field and adapt the structure:

1. **Identify the field** from the user's goal and collected papers
2. **Select section names and organization logic** using the field-specific conventions in `assets/survey-template.md` (e.g., medicine organizes by intervention type and follows PRISMA; chemistry organizes by reaction class; social sciences organize by theoretical perspective)
3. **Add field-specific sections** (e.g., Risk of Bias Assessment for medicine, Structure-Property Relationships for materials, Ethical Considerations for human-subjects research)
4. **Determine comparison table dimensions** appropriate to the field

### Phase 1B: Create Detailed Outline

With the domain-specific template as the framework, generate the outline:

#### Query Type Classification

| Type | Example | Structure |
|------|---------|-----------|
| **A: Single-topic deep dive** | "Catalyst design for electrochemical CO2 reduction" | Intro → Problem Definition → **Methods (by mechanism/approach)** → Evaluation → Challenges → Conclusion |
| **B: Multi-topic parallel** | "Drug resistance mechanisms and therapeutic strategies in cancer immunotherapy" | Intro → **Topic 1 (definition + methods)** → **Topic 2 (definition + methods)** → Evaluation → Challenges → Conclusion |
| **C: Pipeline/stage-based** | "From sample preparation to data analysis in single-cell RNA sequencing" | Chapters organized by workflow stages |

#### Outline Requirements

The outline is NOT a simple heading list — it's a **blueprint with meta-instructions** for each section. For each `## Section`:

- Include `[Instruction: ...]` specifying what the section must contain
- Specify required tables with field-appropriate columns
- For main body sections: mandate taxonomy by underlying principle/mechanism, NOT chronology
- Include any field-required elements (e.g., PRISMA flowchart for medical systematic reviews, mathematical formalism for physics)

See `references/survey-methodology.md` for full outline generation rules and `assets/survey-template.md` for field-specific conventions.

---

## Stage 2: Draft Survey

Generate a complete draft from the outline using the **top-30 most relevant papers**.

- Use numbered citations [1], [2, 3] throughout
- Follow the outline's meta-instructions strictly
- Each methods section must build a taxonomy and include comparison tables
- Problem definition must include LaTeX formalization (`$$...$$`)

---

## Stage 3: Expand Sections

Expand each non-summary section using **all collected papers** (30-120). This is where survey-grade depth is achieved.

### Section Expansion Targets

| Section Type | Target Length | Focus |
|---|---|---|
| **Methods** | 6000+ words per paradigm chapter | Technical narratives, mechanism analysis, comparison tables |
| **Evaluation** | 3500+ words | Benchmark taxonomy, metric analysis, SOTA summary |
| **Challenges** | 3000+ words | Problem definition + evidence + opportunity per challenge |
| **Applications** | 3000+ words | Real-world use cases with specific achievements |
| **Problem Definition** | 2000+ words | LaTeX formalization, constraints, assumptions |
| **Other** | 2500+ words | Default |

### Expansion Rules

1. **Thematic coherence**: Keep same themes and narrative flow as draft — don't introduce unrelated topics
2. **Cite comprehensively**: Use as many relevant papers from the full collection as possible
3. **Survey-grade depth**: Multi-paragraph technical narratives per method family, not shallow bullet points
4. **For each paradigm/method family, include**:
   - Technical narrative: How it works, theoretical assumptions, nuances between papers
   - Critical analysis: Why effective, trade-offs, failure modes
   - Comparative analysis table: Method | Core Mechanism | Key Advantage | Limitation | Performance

---

## Stage 4: Generate Section Summaries

After all content sections are expanded, generate a condensed summary for each major section:

1. Summarize each expanded section in 150-300 words
2. Preserve the key taxonomy, representative methods, and main trade-offs
3. Keep citation anchors so later summary sections remain grounded

These section summaries become the shared context for the final abstract, introduction, and conclusion.

---

## Stage 5: Refine Summary Sections

After all content sections are expanded, refine the **summary sections** (Abstract, Introduction, Conclusion):

1. Use all section summaries as context to rewrite Abstract, Introduction, Conclusion
2. This ensures summary sections accurately reflect the full survey content

### Summary Section Standards

**Abstract** (300-500 words):
- Continuous narrative, NO bullet points or bold labels
- Must cover: background → gap → scope → key findings → outlook

**Introduction**:
- Continuous narrative, NO subsections or bullet points
- Must cover: research background → why traditional methods fail → method summary → scope & organization

**Conclusion**:
- Summarize findings, state which paradigm is most promising
- Respond to user's original research goal
- Provide clear "next step" recommendation

---

## Stage 6: Assemble Final Survey

Assemble sections in outline order, then append formatted references:

```
**1. Title** (Year). _Authors_. *Venue*. Citations: N. [[Link]](url)
```

Save to `/artifacts/survey-{topic}-{date}.md`.

---

## Core Quality Principles

1. **Build taxonomy, don't enumerate**: Cluster papers by technical mechanism, not chronology. This is the defining characteristic of a survey vs. a summary.

2. **Critical insight over description**: For EVERY method, analyze WHY it works, WHAT trade-off it makes, WHERE it fails. This separates survey-grade writing from shallow summaries.

3. **Goal-centric filtering**: Every piece of information must answer "How does this help achieve the research goal?" Discard information that doesn't serve the goal, even if it's interesting.

4. **Strict terminology fidelity**: Use the user's exact technical terms. Do NOT drift to related but different concepts.

5. **Dense citations**: Ground ALL claims with numbered citations [X]. Nearly every sentence should reference at least one paper.

6. **Zero vagueness**: Replace generic statements with specific method names, dataset names, metric values, and problem descriptions.

7. **Visual structure**: Use Markdown tables extensively — paradigm comparison, intra-paradigm method comparison, benchmark tables, metric tables.

---

## Reference Materials

| Resource | Location | Purpose |
|----------|----------|---------|
| Multi-stage pipeline details | `references/survey-methodology.md` | Full methodology: outline rules, section standards, expansion targets |
| Section quality checklist | `references/section-quality-checklist.md` | Per-section verification checklist before finalizing |
| Survey output template | `assets/survey-template.md` | English Markdown template with section structure, table formats, and placeholder guidance |

---

## Handoff

| From → To | When |
|-----------|------|
| `paper-navigator` → here | Papers collected, user wants synthesis |
| Here → `research-ideation` | Survey reveals research gaps worth pursuing |
| Here → `paper-writing` | Survey informs Related Work section of a paper |
| Here → `paper-planning` | Survey provides literature context for story design |


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/EvoScientist/EvoSkills/contents/skills/research-survey/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>EvoScientist/EvoSkills</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../evoskills.md">EvoSkills</a></dd>
<dt><b>Category</b></dt><dd><code>literature</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>literature-discovery</code> <code>literature-synthesis</code></dd>
<dt><b>License</b></dt><dd>Apache-2.0</dd>
<dt><b>Last update</b></dt><dd>2026-05-17</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/EvoScientist/EvoSkills">⭐ EvoScientist/EvoSkills</a><br><img src="https://img.shields.io/github/stars/EvoScientist/EvoSkills?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/EvoScientist/EvoSkills" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/evoskills/research-survey/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/evoskills.yml">edit on GitHub</a>.</p>
</div>

</div>
