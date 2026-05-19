<!-- DO NOT EDIT — auto-copied from skills/awesome-econ-ai-stuff/details/research-ideation.md -->

# `research-ideation`

Generate research questions from economic phenomena.

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
name: research-ideation
description: Generate research questions from economic phenomena
workflow_stage: ideation
compatibility:
  - claude-code
  - cursor
  - codex
  - gemini-cli
author: Awesome Econ AI Community
version: 1.0.0
tags:
  - research
  - ideation
  - hypothesis
  - brainstorming
---

# Research Ideation

## Purpose

This skill helps economists generate and refine research questions by applying economic thinking frameworks. It guides the process from observing phenomena to formulating testable hypotheses.

## When to Use

- Starting a new research project
- Brainstorming dissertation topics
- Finding angles for policy analysis
- Developing extensions of existing work

## Instructions

### Step 1: Understand the Starting Point

Ask the user:
1. Do you have a phenomenon, puzzle, or data source in mind?
2. What field/subfield of economics?
3. What's your methodological preference? (Theory, empirical, structural)
4. Any constraints? (Data access, timeline, etc.)

### Step 2: Apply Ideation Frameworks

Use these approaches:

**1. The Puzzle Approach**
- What's surprising about current patterns?
- What contradicts conventional economic wisdom?
- Where do standard models fail?

**2. The Policy Approach**
- What policies lack rigorous evaluation?
- What natural experiments remain unexploited?
- What interventions might solve important problems?

**3. The Data Approach**
- What new data sources have become available?
- What can existing data tell us that hasn't been explored?
- What linkages between datasets are possible?

**4. The Extension Approach**
- How can seminal papers be extended?
- What mechanisms remain unexplored?
- Can methods from one field apply to another?

### Step 3: Evaluate and Refine

For each idea, assess:
- **Feasibility**: Can this be done with available data/methods?
- **Contribution**: What's new here?
- **Interest**: Who cares about this question?
- **Identification**: Can effects be credibly estimated?

## Example Interaction

**User Query:** "I'm interested in labor economics and have access to LinkedIn data"

**Generated Response:**

## Research Ideas: LinkedIn Data × Labor Economics

### 1. Network Effects in Job Search
**Question:** How do professional networks affect job transitions and wage changes?

**Puzzle:** Standard search models assume random matching, but most jobs come through networks. How much do networks matter for outcomes?

**Approach:**
- Track profile updates signaling job changes
- Measure network overlap between current/future employers
- Instrument with exogenous network shocks (school alumni connections)

**Contribution:** Quantify the causal role of networks vs. unobserved ability

---

### 2. Skill Signaling and Returns
**Question:** Do workers who list specific skills on profiles earn wage premiums?

**Puzzle:** Are listed skills signals of ability, or just cheap talk? What's the return to skill acquisition vs. skill signaling?

**Approach:**
- Compare wages before/after workers add skills
- Use skill endorsements as validation
- Exploit skill assessment features as quasi-experiments

---

### 3. Gender Gaps in Self-Promotion
**Question:** Do men and women describe equivalent achievements differently?

**Puzzle:** Lab evidence shows women understate accomplishments. Does this appear in real profiles and affect outcomes?

**Approach:**
- NLP analysis of profile language (adjectives, quantification)
- Compare language for workers in same role/company
- Link to recruiter contact rates if available

---

### 4. Remote Work and Labor Market Geography
**Question:** How has remote work changed the geographic reach of job matching?

**Approach:**
- Compare pre/post-2020 job applications by distance
- Measure changes in location signals on profiles
- Study wage convergence across cities

---

## Evaluation Matrix

| Idea | Data Feasibility | Identification | Policy Relevance |
|------|-----------------|----------------|------------------|
| Network effects | High | Medium (need IV) | High |
| Skill signaling | High | Medium | Medium |
| Gender language | High | High (descriptive) | High |
| Remote geography | High | High (COVID natural experiment) | High |

## Recommended Next Steps

1. **For empirical work:** Start with Idea #4 (clearest identification)
2. **For policy impact:** Idea #1 has most implications for job matching platforms
3. **For methodological novelty:** Idea #3 combines NLP with quasi-experimental methods

---

## Frameworks for Generating Questions

### The "5 Whys" for Economics

Start with an observation and drill down:
1. GDP growth is slowing → Why?
2. Productivity is stagnant → Why?
3. Investment is low → Why?
4. Uncertainty is high → Why?
5. Policy is unpredictable → **Testable: Does policy uncertainty cause low investment?**

### The "What If" Generator

- What if [policy X] were implemented?
- What if [technology Y] became widespread?
- What if [assumption Z] were relaxed?

### The Cross-Field Pollinator

Take a method from one field and apply to another:
- IO techniques → Labor markets (how do firms choose wages like prices?)
- Finance models → Education (returns to schooling as asset pricing)
- Macro shocks → Micro outcomes (firm-level effects of exchange rate changes)

## Common Pitfalls

- ❌ Questions that are too broad ("What causes inequality?")
- ❌ Questions without clean identification ("Does education cause income?")
- ❌ Questions without data ("Were medieval peasants happy?")
- ❌ Questions already well-answered

## References

- [Shapiro (2022) How to Get Started on Research in Economics](https://www.brown.edu/Research/Shapiro/pdfs/research.pdf)
- [Angrist & Pischke on Mostly Harmless research design](https://www.mostlyharmlesseconometrics.com/)
- [AEA Research Pipelines](https://www.aeaweb.org/rfe/)

## Changelog

### v1.0.0
- Initial release with ideation frameworks


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/meleantonio/awesome-econ-ai-stuff/contents/_skills/ideation/research-ideation/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>meleantonio/awesome-econ-ai-stuff</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../awesome-econ-ai-stuff.md">awesome-econ-ai-stuff (Antonio Mele)</a></dd>
<dt><b>Category</b></dt><dd><code>ideation</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>rq-formulation</code> <code>hypothesis-generation</code></dd>
<dt><b>License</b></dt><dd>Other (see repo)</dd>
<dt><b>Last update</b></dt><dd>2026</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff">⭐ meleantonio/awesome-econ-ai-stuff</a><br><img src="https://img.shields.io/github/stars/meleantonio/awesome-econ-ai-stuff?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/meleantonio/awesome-econ-ai-stuff/blob/main/_skills/ideation/research-ideation/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/awesome-econ-ai-stuff/research-ideation/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/awesome-econ-ai-stuff.yml">edit on GitHub</a>.</p>
</div>

</div>
