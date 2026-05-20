<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/prompt-refine.md -->

# `/prompt-refine`

Iteratively refine a prompt

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>meta</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/prompt-refine.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/prompt-refine/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/prompt-refine.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## /prompt-refine — Review and Improve an Existing Prompt

*v2.0 — Substance checklist, depth calibration, tool routing, expanded anti-patterns*

Audit an existing prompt against quality criteria and output an improved version.

### Reference Files
@~/.claude/commands/prompt-references/formatting-core.md

### Input
$ARGUMENTS

### Instructions

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

### Important
- Do NOT rewrite from scratch if the original is mostly good. Make targeted improvements.
- Preserve the user's intent and voice — don't make it sound generic.
- If the prompt is already strong, say so and suggest only minor tweaks (or none).
- Do NOT execute the refined prompt. Output only.
- Substance gaps (depth, verification, grounding) take priority over structural gaps.
