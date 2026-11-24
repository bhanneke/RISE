<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/skill-build.md -->

# `/skill-build`

Create a reusable agent skill from a recurring task, an established workflow, or work and corrections the user has just finished.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>meta</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-11-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/skill-build/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/skill-build/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/skill-build/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Build a skill

### Work out what is worth saving

Start with the task the user wants to repeat. Read the relevant project instructions, a representative example, and any previous attempts or corrections the user points to. Check whether an existing skill already handles the task. Use the evidence at hand and ask a focused question only if the missing answer would change the skill.

Work out what the user has taught the agent that would be useful next time. A persistent project instruction, a small script, or ordinary project work may be enough. Continue with a skill when a reader will benefit from instructions they can call up for a particular job. Keep facts about a single meeting, client, or deadline in the project record.

Honor the requested scope. A build request can authorize writing the new skill in the agreed location. A request for options, a review, or a plan calls for advice at that stage.

### Write the skill

- Confirm the skill's name, intended app, and location from the request or project conventions. For a new project-local skill, use `.claude/skills/<name>/` in Claude Code or `.agents/skills/<name>/` in Codex. For a different scope, check the app's installation instructions before writing. Look for an existing copy with the same name and preserve it unless the user requested a change to it.
- Give the skill a `SKILL.md` with YAML `name` and `description`. Say what it does and which requests should select it. Write instructions for performing the job, including the user's judgment, what inputs to read, what to produce, and how to tell if it worked.
- Preserve useful decisions and examples from the work. Use a short example when the distinction is easier to show than describe. Put supporting material alongside the skill and refer to it by relative path. Include a script only when it makes a repeatable operation more reliable. State material dependencies and what to do if they are unavailable.
- Make the usual request easy. Use the information already supplied before asking for more. Preserve the user's choices about review and changes with external effects. If the skill expects an optional app or another skill, give the user a clear way to proceed when it is missing.

### Check that it helps

Check the folder, frontmatter, and links. Give the user a fresh-session trial using a second input that exercises the important choice or correction. If requested and the app permits it, run that trial. Check which copy loaded and inspect what it produced. For a skill meant to save repeated explanation, also check whether the agent still asked for information it already had.

Report the skill's location, how to use it, what you actually tested, and anything still needed. Keep untested behavior explicit. A request to create a local skill does not authorize publishing it.
