<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/skill-refresh.md -->

# `/skill-refresh`

Diagnose, update, simplify, or retest an existing agent skill using an observed failure, user correction, or changed tool.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>meta</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-11-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/skill-refresh/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/skill-refresh/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/skill-refresh/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Refresh a skill

### Find the copy and the problem

Identify the skill the user means, the copy the app actually used, and the source the user can maintain. Check the whole skill folder and its supporting files before editing. If the user installed it from a plugin or shared library, check the supported customization or update route. Preserve same-named copies and individual changes.

Start with the failure or opportunity the user describes. Recover what was asked, what happened, what the user wanted, and what should keep working. Use a representative run, a correction, or a known good example when available. A request to assess or diagnose calls for findings. A clear request to fix the identified skill authorizes a bounded repair to that skill.

### Make the smallest useful change

Distinguish a missing dependency, a tool change, and an instruction problem. Check whether the agent followed the instructions it already had. For claims about a changed app or tool, check current documentation where it affects the repair. Keep an effective skill as it is when the evidence points elsewhere.

Preserve the existing skill's purpose and useful behavior. Back up the previous version or use version control before applying a change so the user can restore it. Edit the relevant instruction, reference, or helper and verify links between them. Avoid copying a fix into a different installed version by mistake. If a choice would materially change what the skill does, bring that choice to the user.

For a simple problem, work through the diagnosis directly. When independent review would help, offer it or use it if the user has asked for it and the app supports it.

### Test the repair

Start with the failure that motivated the refresh. Then use a different example that tests the same distinction and checks that the skill still handles normal cases. If the original issue is about tool access, verify the required action using an appropriate test. For a wording or judgment problem, inspect the new output.

When possible, try the revised skill in a fresh session and confirm which copy loaded. When a fresh run requires a separate session or unavailable connection, give the user the exact trial and say what remains untested. Report what changed, what evidence supports the repair, and how to undo it.
