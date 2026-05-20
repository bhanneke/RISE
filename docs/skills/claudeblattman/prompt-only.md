<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/prompt-only.md -->

# `/prompt-only`

Skill that only produces a prompt (no execution)

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

# /prompt-only — Format Without Executing

*v2.0 — Format informal requests into structured prompts. Output only — do not execute.*

Format an informal request into a structured prompt. Output only — do not execute.

## Reference Files
@~/.claude/commands/prompt-references/formatting-core.md

## Input
$ARGUMENTS

## Instructions

You are a prompt formatter. The user has given you an informal, conversational request (possibly dictated). Your job is to produce a clean, well-structured prompt they can use anywhere — Claude Code, Claude.ai, ChatGPT, or other tools.

1. **Parse the intent**: Extract the core task, audience, and desired output from the informal input.

2. **Calibrate depth** using the heuristic in formatting-core.md:
   - **Light** (default): Format only. No depth injection.
   - **Standard**: Format + append assumptions/rationale block.
   - **Deep**: Format + append research/compare/verify block.
   - User can override with `depth:light`, `depth:standard`, or `depth:deep`.

3. **Format into a structured prompt** using the formatting elements in formatting-core.md. Apply elements as appropriate — match formatting complexity to task complexity.

4. **Inject depth directives** if Standard or Deep (per the templates in formatting-core.md). For Light, skip this step entirely.

5. **Output the formatted prompt** in a clean fenced code block.

6. **Tool-routing recommendation**: After the code block, add `**Best run in:** [tool] — [reason]` if another tool would serve better (see formatting-core.md). If Claude Code is the best fit, omit this line.

7. **If the prompt looks reusable** (template, workflow, recurring task):
   - Add a version header: `## Prompt v1.0 — [short name]`
   - Suggest 3-5 eval test cases: brief input/expected-output pairs to verify quality

8. **If the prompt has agent/workflow context** (system instructions vs. user turn):
   - Separate into **System Prompt** and **User Prompt** sections within the code block

9. **Do NOT execute the prompt.** Output only.

## Important
- Do NOT over-engineer simple requests. Match formatting complexity to task complexity.
- Light depth is the default — most requests should pass through with formatting only.
- For one-off prompts, skip the version header and eval cases.
- Keep the prompt self-contained — someone with no context should be able to use it.


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/prompt-only.md --jq .content | base64 -d`); this.textContent='✓ copied';"
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
<p style="margin:0.6em 0;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/prompt-only.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/claudeblattman/prompt-only/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/claudeblattman.yml">edit on GitHub</a>.</p>
</div>

</div>
