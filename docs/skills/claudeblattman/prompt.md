<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/prompt.md -->

# `/prompt`

Build a prompt from scratch with formatting-core

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>meta</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/prompt.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/prompt/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/prompt.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## /prompt — Format and Execute

*v2.1 — Opus 4.7 update: long-context ordering and system-vs-user separation in the formatting core; optional `council` token to route a formatted prompt through a multi-critic review (`/council`) instead of executing it directly.*

Format an informal request into a structured prompt, then execute it.

### Reference Files
@~/.claude/commands/prompt-references/formatting-core.md

### Input
$ARGUMENTS

### Instructions

You are a prompt formatter. The user has given you an informal, conversational request (possibly dictated). Your job:

1. **Parse the intent**: Extract the core task, audience, and desired output from the informal input.

2. **Calibrate depth** using the heuristic in formatting-core.md:
   - **Light** (default): Format only. No depth injection.
   - **Standard**: Format + append assumptions/rationale block.
   - **Deep**: Format + append research/compare/verify block.
   - User can override with `depth:light`, `depth:standard`, or `depth:deep`.

3. **Format into a structured prompt** using the formatting elements in formatting-core.md. Apply elements as appropriate — match formatting complexity to task complexity.

4. **Inject depth directives** if Standard or Deep (per the templates in formatting-core.md). For Light, skip this step entirely.

5. **Show the formatted prompt** in a fenced code block so the user can see exactly what will run.

6. **Tool-routing check**: If another tool would serve this task better (see formatting-core.md), add a brief note before executing. Don't block — just flag it.

7. **Council opt-in**: If the input contains the literal token `council`, do NOT execute directly. Instead, after formatting, invoke `/council` with the formatted prompt as the topic. The `council` token is opt-in only — `/prompt` does NOT default-wrap in council. This prevents accidental council dispatches from casual `/prompt` uses.

8. **Execute the prompt immediately** — respond to it as if the user had typed it directly (unless step 7's council token was present).

9. **Ask ONE clarifying question ONLY if** the ambiguity would lead to a significantly different output. Otherwise, make reasonable assumptions and proceed.

### Important
- Do NOT over-engineer simple requests. A 1-sentence ask doesn't need a 20-line prompt.
- Match complexity of formatting to complexity of task.
- Light depth is the default — most requests should pass through with formatting only.
- If the user says "hold" or "don't run" or "just format", show the prompt but do not execute.
- `council` token handling: opt-in only. `/prompt X depth:deep council` → format, then dispatch via `/council`. `/prompt X` → format + execute directly (no council).
- Use Claude Code tools (MCP, file access, search) when executing if the task requires them.
