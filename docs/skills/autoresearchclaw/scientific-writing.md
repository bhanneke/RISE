<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/scientific-writing.md -->

# `scientific-writing`



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
name: scientific-writing
description: Academic manuscript writing with IMRAD structure, citation formatting, and reporting guidelines. Use when drafting or revising research papers.
metadata:
  category: writing
  trigger-keywords: "paper,manuscript,writing,IMRAD,citation,abstract,introduction,methods,results,discussion"
  applicable-stages: "16,17,19"
  priority: "2"
  version: "1.0"
  author: researchclaw
  references: "adapted from K-Dense-AI/claude-scientific-skills"
---

## Scientific Writing Best Practice

### IMRAD Structure
1. **Abstract**: State objective, methods, key results, and conclusion in 150-300 words
2. **Introduction**: Move from broad context to specific gap to your contribution (funnel structure)
3. **Methods**: Sufficient detail for replication; use past tense, passive voice
4. **Results**: Present findings without interpretation; pair text with figures/tables
5. **Discussion**: Interpret results, compare with literature, acknowledge limitations, state implications

### Paragraph-Level Guidance
1. Each paragraph should convey ONE main idea
2. Open with a topic sentence; close with a transition to the next paragraph
3. Write in full flowing prose — never submit bullet points as final manuscript text
4. Use active voice for clarity: "We measured..." not "Measurements were taken..."
5. Vary sentence length; aim for average 15-25 words per sentence

### Citation Best Practices
1. Cite primary sources over reviews when making specific claims
2. Use citation styles consistently (APA, Vancouver, IEEE) per target journal
3. Every factual claim needs a citation unless it is common knowledge in the field
4. Avoid citation strings of 5+ references — select the most relevant 2-3
5. Self-citations should be limited to genuinely relevant prior work

### Common Writing Pitfalls
1. Avoid hedge-stacking: "It might possibly suggest..." — choose one hedge
2. Do not start sentences with "It is well known that" — cite or remove
3. Distinguish "significant" (statistical) from "substantial" (practical)
4. Ensure figures/tables are referenced in text BEFORE they appear
5. Keep abbreviations to a minimum; define each on first use

### Reporting Guidelines
1. Randomized trials: follow CONSORT checklist
2. Observational studies: follow STROBE checklist
3. Systematic reviews: follow PRISMA checklist
4. Diagnostic accuracy: follow STARD checklist
5. Always check target journal's author guidelines for specific requirements

### Revision Checklist
1. Verify all figures/tables are cited in text and numbered sequentially
2. Confirm reference list matches in-text citations exactly
3. Check that abstract accurately reflects the final manuscript content
4. Ensure methods section enables independent replication
5. Read aloud to catch awkward phrasing and run-on sentences


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/scientific-writing/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>aiming-lab/AutoResearchClaw</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../autoresearchclaw.md">AutoResearchClaw skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04-23</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw">⭐ aiming-lab/AutoResearchClaw</a><br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/autoresearchclaw/scientific-writing/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/autoresearchclaw.yml">edit on GitHub</a>.</p>
</div>

</div>
