<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/verify.md -->

# `/verify`

Runs the repository's gates on the work about to be committed (the backtest suite and the quality score of each staged .qmd, .tex and .R file) and stops the commit if one fails.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../psantanna-workflow/">Pedro Sant'Anna's Claude Code Workflow</a></div><div><b>Category:</b> <code>review</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-11-07</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>referee-simulation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/verify/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/psantanna-workflow/verify/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/verify/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## /verify — the gates, before a commit

Since Claude Code 2.1.286, Claude is *told* to run a project skill named `verify` right before it commits, except for docs-only and tests-only commits. This one runs the same gates `/commit` runs. It is a reminder, not enforcement: Claude can skip it, and an exempt commit never triggers it, even one that changes a `.qmd` or `.tex` file. The enforcing gates are the git pre-commit hook (`./scripts/install-hooks.sh`) and `/commit`. It **does not** commit, push, stage, or edit anything.

### Steps

1. **Is the git hook already doing this?** Only when all three checks from `/commit` Step 0b hold: `git config --get core.hooksPath` prints `.githooks`; `test -x "$(git rev-parse --show-toplevel)/.githooks/pre-commit" && echo executable` prints `executable` (git skips a hook file that is missing or not executable, and still commits); and `git status --porcelain -- ':/.githooks'` prints nothing (an edited hook is itself what needs testing, and it could exit 0 without running anything). Then the pre-commit hook will run the backtest and the quality gate on this commit anyway. Say so in one line and stop, because running everything twice wastes a minute and adds nothing. Otherwise go on to step 2.
2. **Run the backtest:** `./scripts/backtest.sh`. Capture the exit code and the last lines. A non-zero exit fails `/verify`; report the failing gate's own message, not a summary of it.
3. **Score staged prose and code:** for each staged file ending in `.qmd`, `.tex` or `.R` (`git diff --cached --name-only --diff-filter=ACMR`), run `python3 scripts/quality_score.py <file>`. A score below 80 fails `/verify`.
4. **Report.** One line per check (`PASS` / `FAIL`, with the score or the gate's message), then the verdict.
   - **FAIL:** do not commit. Say what failed and what fixes it.
   - **PASS:** say the commit can go ahead.

   If the user has explicitly said "commit anyway" or "skip quality gate", pass that on: `/commit` records such an override as `SKIP_QUALITY_GATE=1`, which skips only the quality score. Never suggest `git commit --no-verify`.

### Not this skill's job

Fixing what failed (do that, then run `/verify` again), writing the commit message (`/commit`), and deciding whether a change is wanted (the user). A gate that cannot run, such as a missing interpreter or a script error, is a FAIL, not a pass.
