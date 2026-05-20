<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/prompt-refine.md -->

# `/prompt-refine`

Iteratively refine a prompt

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

# /prompt-refine — Review and Improve an Existing Prompt

*v2.0 — Substance checklist, depth calibration, tool routing, expanded anti-patterns*

Audit an existing prompt against quality criteria and output an improved version.

## Reference Files
@~/.claude/commands/prompt-references/formatting-core.md

## Input
$ARGUMENTS

## Instructions

You are a prompt reviewer and editor. The user has given you an existing prompt to improve. Your job:

1. **Run the substance checklist first** (new issues matter most):
   - [ ] Depth calibration — does the prompt instruct the model on how deeply to engage?
   - [ ] Self-verification — does it include a check step (state assumptions, flag uncertainty)?
   - [ ] Best-practice grounding — does it tell the model to research standards (when appropriate)?
   - [ ] Specificity of "good" — does it define what strong output looks like?
   - [ ] Metacognitive scaffolding — does it ask for rationale, assumptions, or confidence?

2. **Run the structure checklist:**
   - [ ] Task clarity — is the core ask unambiguous?
   - [ ] Context — enough background for a cold reader?
   - [ ] Constraints — length, tone, format, exclusions specified?
   - [ ] Output format — structure defined (bullets, table, sections)?
   - [ ] Role/persona — included if it would improve output?
   - [ ] Examples — provided if they would reduce ambiguity?
   - [ ] Bookend pattern — key instruction restated at end (if prompt is long)?
   - [ ] System/user separation — clear if used in agent/API context?
   - [ ] Versioning — version header if reusable?

3. **Identify the primary finding.** Lead with the single most impactful improvement. Common primary findings:
   - "This prompt specifies format but not depth. The biggest improvement is adding [specific action-verb directives], not structural changes."
   - "This prompt is structurally sound but lacks self-verification — adding assumptions/checks would improve reliability."
   - "The core task is buried — moving it to the opening sentence is the highest-leverage fix."

4. **Fix common anti-patterns:**
   - Format-only prompts for substantive tasks — add depth directives
   - Vague thoroughness language ("be meticulous", "be comprehensive") — replace with specific action verbs ("compare against [standard]", "research current best practices for [domain]", "flag where your approach deviates")
   - Over-prompting — soften "CRITICAL", "YOU MUST", "ABSOLUTELY" to calm, specific directives (modern Claude models respond better to calm specificity than emphatic caps)
   - Excessive caveats or hedging ("try to", "if possible", "feel free to") — make direct
   - Vague format instructions ("give me a summary") — specify structure
   - Missing constraints that lead to verbose output — add length/scope limits
   - "Show your reasoning" without purpose — replace with "Brief rationale:" or remove
   - Redundant instructions — consolidate
   - Buried lede — move the core task to the top

5. **Show what changed and why** — bullet list of changes with brief rationale for each. Lead with the primary finding.

6. **Present the refined prompt** in a fenced code block.

7. **Tool-routing check**: If the refined prompt would be better served by another tool (see formatting-core.md), note it in the changes list.

8. **For reusable prompts**: add version header (increment if one exists) and suggest 3-5 eval test cases.

## Important
- Do NOT rewrite from scratch if the original is mostly good. Make targeted improvements.
- Preserve the user's intent and voice — don't make it sound generic.
- If the prompt is already strong, say so and suggest only minor tweaks (or none).
- Do NOT execute the refined prompt. Output only.
- Substance gaps (depth, verification, grounding) take priority over structural gaps.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/prompt-refine.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>chrisblattman/claudeblattman</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../claudeblattman.md">claudeblattman (Chris Blattman)</a></dd>
<dt><b>Category</b></dt><dd><code>meta</code></dd>
<dt><b>Field</b></dt><dd>general</dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/chrisblattman/claudeblattman">⭐ chrisblattman/claudeblattman</a><br><img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/prompt-refine.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/claudeblattman/prompt-refine/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/claudeblattman.yml">edit on GitHub</a>.</p>
</div>

</div>
