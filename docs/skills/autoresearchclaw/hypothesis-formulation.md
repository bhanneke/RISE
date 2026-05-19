<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/hypothesis-formulation.md -->

# `hypothesis-formulation`



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
name: hypothesis-formulation
description: Structured scientific hypothesis generation from observations. Use when formulating testable hypotheses, competing explanations, or experimental predictions.
metadata:
  category: experiment
  trigger-keywords: "hypothesis,prediction,mechanism,falsifiable,null,alternative,testable"
  applicable-stages: "7,8,9"
  priority: "3"
  version: "1.0"
  author: researchclaw
  references: "adapted from K-Dense-AI/claude-scientific-skills"
---

## Hypothesis Formulation Best Practice

### Structured Hypothesis Development
1. Start with a clear observation or pattern that requires explanation
2. Review existing literature for known mechanisms and prior explanations
3. Identify what is already established vs. what remains uncertain
4. Formulate the hypothesis as a specific, testable statement
5. Ensure the hypothesis is falsifiable — define what outcome would refute it

### Hypothesis Format
1. **Null hypothesis (H0)**: There is no effect or no difference
2. **Alternative hypothesis (H1)**: There is a specific, directional effect
3. State both explicitly; design experiments to reject H0
4. Use "If... then... because..." structure for mechanistic hypotheses:
   - If [independent variable is manipulated], then [predicted outcome], because [proposed mechanism]

### Generating Competing Hypotheses
1. Propose at least 2-3 plausible explanations for the same observation
2. For each, identify unique predictions that distinguish it from alternatives
3. Rank hypotheses by parsimony, consistency with prior evidence, and testability
4. Design experiments that can discriminate between competing hypotheses
5. Consider confounding variables that could produce the same observation

### Testable Predictions
1. Derive specific, measurable predictions from each hypothesis
2. Define expected effect direction AND approximate magnitude
3. Specify what experimental conditions would confirm vs. refute the prediction
4. Identify potential confounds and plan controls to address them
5. Ensure predictions are achievable with available methods and resources

### Aligning with Experimental Design
1. Map each hypothesis to a concrete experimental condition or comparison
2. Ensure sample size is adequate to detect the predicted effect (power analysis)
3. Pre-register hypotheses and analysis plans when possible
4. Distinguish confirmatory (hypothesis-testing) from exploratory analyses
5. Plan for both positive and null results — what will you conclude in each case?


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/hypothesis-formulation/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>aiming-lab/AutoResearchClaw</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../autoresearchclaw.md">AutoResearchClaw skills</a></dd>
<dt><b>Category</b></dt><dd><code>ideation</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>rq-formulation</code> <code>hypothesis-generation</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04-23</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw">⭐ aiming-lab/AutoResearchClaw</a><br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/autoresearchclaw/hypothesis-formulation/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/autoresearchclaw.yml">edit on GitHub</a>.</p>
</div>

</div>
