<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/prompt-only.md -->

# `/prompt-only`

Skill that only produces a prompt (no execution)

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>meta</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/prompt-only.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/prompt-only/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/prompt-only.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## /prompt-only — Format Without Executing

*v2.0 — Format informal requests into structured prompts. Output only — do not execute.*

Format an informal request into a structured prompt. Output only — do not execute.

### Reference Files
@~/.claude/commands/prompt-references/formatting-core.md

### Input
$ARGUMENTS

### Instructions

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

### Important
- Do NOT over-engineer simple requests. Match formatting complexity to task complexity.
- Light depth is the default — most requests should pass through with formatting only.
- For one-off prompts, skip the version header and eval cases.
- Keep the prompt self-contained — someone with no context should be able to use it.
