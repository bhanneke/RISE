<!-- DO NOT EDIT — auto-copied from skills/psantanna-workflow/details/deep-audit.md -->

# `/deep-audit`



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
name: deep-audit
description: |
  Deep consistency audit of the entire repository infrastructure.
  Launches 4 parallel specialist agents to find factual errors, code bugs,
  count mismatches, and cross-document inconsistencies. Then fixes all issues
  and loops until clean.
  Use when: after making broad changes, before releases, or when user says
  "audit", "find inconsistencies", "check everything".
author: Claude Code Academic Workflow
version: 1.0.0
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Task"]
disable-model-invocation: true
---

# /deep-audit — Repository Infrastructure Audit

Run a comprehensive consistency audit across the entire repository, fix all issues found, and loop until clean.

## When to Use

- After broad changes (new skills, rules, hooks, guide edits)
- Before releases or major commits
- When the user asks to "find inconsistencies", "audit", or "check everything"

## Workflow

### PHASE 0: Mechanical checks (run FIRST, cheap, deterministic)

Before spawning agents, run the mechanical parity checks:

```bash
python3 scripts/check-skill-integrity.py --verbose
```

This catches four classes of bug that agent-based audits have historically missed:

1. Frontmatter `allowed-tools` ↔ body tool-invocation parity (e.g. body spawns `Task` but `Task` not in `allowed-tools` — the v1.7.0 PR #92 miss).
2. `argument-hint` ↔ body flag parity (flags documented but not advertised, or vice versa).
3. Internal markdown anchors resolve (no broken `[text](path#anchor)` links — the `#category-11-numerical-discipline` miss on PR #87).
4. Rule `paths:` ↔ skill implementation parity (rule claims skill follows protocol but skill body has none of the protocol keywords — the `/interview-me` miss on PR #92).

If Phase 0 reports P0 or P1 findings, fix them (or tune the regex if they are false positives) **before** launching the 4 agents. The mechanical layer is cheaper and more precise than agent prompts for these classes.

### PHASE 1: Launch 4 Parallel Audit Agents

Launch these 4 agents simultaneously using `Task` with `subagent_type=general-purpose`. Each agent's prompt **must** tell it to read `.claude/references/audit-pet-peeves.md` and explicitly check for each class of bug before reporting clean. The pet-peeves file is a living catalogue of drift patterns review bots have caught; it grows with each PR.

#### Agent 1: Guide Content Accuracy
Focus: `guide/workflow-guide.qmd`
- All numeric claims match reality (skill count, agent count, rule count, hook count)
- All file paths mentioned actually exist on disk
- All skill/agent/rule names match actual directory names
- Code examples are syntactically correct
- Cross-references and anchors resolve
- No stale counts from previous versions

#### Agent 2: Executable Code Quality
Focus: **all** executable code in the repo — `.claude/hooks/*.py`, `.claude/hooks/*.sh`, `scripts/*.py`, `scripts/*.sh`, `.claude/scripts/*.sh`. Not just `.claude/hooks/` — when PR #93 added new code under `scripts/`, the original narrow scope meant Copilot + Codex caught 5 bugs the audit missed.

Hook-specific checks (Stop/PreToolUse/SessionStart protocols, `CLAUDE_PROJECT_DIR` usage, hash-length consistency) apply only to `.claude/hooks/`. Everything below applies to ALL executable code:

- No remaining `/tmp/` usage in anything that manages state (should use `~/.claude/sessions/`)
- Hash length consistency (`[:8]` across all hooks) [hooks only]
- Proper error handling — **fail-open pattern** where the docstring promises it (top-level `try/except` with `sys.exit(0)`). Python `read_text()` must catch `UnicodeError` (not just `OSError`) if the script is promised fail-open for corrupt files. Bash `set -u` without `set -e` or explicit post-command checks does NOT catch command failures — verify.
- **Docstring-claim ↔ implementation parity.** If a function's docstring describes "bidirectional parity" / "fail-open" / "exits 1 on X", the implementation must match. Common drift: one-directional implementation of a claimed-bidirectional contract; exit codes documented as one thing but returning another.
- **Config-map entries point at live targets.** Keyword dicts, path maps, and rule registries should not contain dead entries (e.g. rule files that don't exist, fields the script doesn't actually read). Dead entries mislead maintainers.
- JSON input/output correctness (stdin for input, stdout/stderr for output) [hooks only]
- Exit code correctness. Two valid blocking protocols for Stop/PreToolUse hooks:
  (a) **exit 2 + reason on stderr** — legacy, still supported
  (b) **exit 0 + JSON `{"decision": "block", "reason": "..."}` on stdout** — modern; this is what `log-reminder.py` uses and it works correctly
  Non-blocking hooks always exit 0. PreCompact hooks MUST exit 0 (stdout is discarded by the harness — use stderr for diagnostics)
- `from __future__ import annotations` for Python 3.8+ compatibility
- Correct field names from hook input schema (`source` not `type` for SessionStart)
- PreCompact hooks print to stderr (stdout is ignored)

#### Agent 3: Skills and Rules Consistency
Focus: `.claude/skills/*/SKILL.md` and `.claude/rules/*.md`
- Valid YAML frontmatter in all files
- No stale `disable-model-invocation: true`
- `allowed-tools` values are sensible
- **`allowed-tools` actually covers every tool the skill body invokes.** For every `Task` spawn, `Bash` command, `Write`/`Edit` call mentioned in the skill's Steps / Phases / Workflow body, verify the tool appears in the `allowed-tools` array. Common miss: skill body says "spawn `agent-X` via `Task` with `context=fork`" but `Task` is absent from `allowed-tools` — runtime permission error or silent bypass. Caught this class of bug after Codex/Copilot flagged it on PR #92 (4 skills promised `Task` in their Post-Flight sections but 3 of 4 had no `Task` permission).
- **Rule `paths:` scope matches skill implementation.** If rule X lists skill Y in `paths:`, verify skill Y actually implements the protocol rule X mandates. A rule claiming a skill follows a protocol is meaningless if the skill doesn't.
- Rule `paths:` reference existing directories
- No contradictions between rules
- CLAUDE.md skills table matches actual skill directories 1:1
- All templates referenced in rules/guide exist in `templates/`

#### Agent 4: Cross-Document Consistency
Focus: `README.md`, `docs/index.html`, `docs/workflow-guide.html`
- All feature counts agree across all 3 documents
- All links point to valid targets
- License section matches LICENSE file
- Directory tree matches actual structure
- No stale counts from previous versions

### PHASE 2: Triage Findings

Categorize each finding:
- **Genuine bug**: Fix immediately
- **False alarm**: Discard (document WHY it's false for future rounds)

Common false alarms to watch for:
- Quarto callout `## Title` inside `:::` divs — this is standard syntax, NOT a heading bug
- `allowed-tools` linter warning — known linter bug (Claude Code issue #25380), field IS valid
- Counts in old session logs — these are historical records, not user-facing docs
- Counts in `CHANGELOG.md` under past version headings — those are snapshots; do NOT update
- `log-reminder.py` outputting `{"decision": "block"}` with `sys.exit(0)` — this IS the modern Claude Code Stop-hook block protocol, NOT a bug

**Count drift specifically: search for every phrasing variant.** A common failure mode is that `replace_all` on one phrasing (e.g., `"26 skills"`) misses sibling phrasings in the same repo. When checking counts, grep for ALL of:
- `"N skills"`, `"N skill "` (with space)
- `"N slash commands"`
- `"N specialized"` (as in "N specialized agents")
- `"template's N"` (informal count in prose)
- Commas/conjunctions: `"skills,"` vs `"skills, and"` are treated as different strings by `replace_all`
Verify zero matches for the OLD number across the whole tree before declaring clean.

### PHASE 3: Fix All Issues

Apply fixes in parallel where possible. For each fix:
1. Read the file first (required by Edit tool)
2. Apply the fix
3. Verify the fix (grep for stale values, check syntax)

### PHASE 4: Re-render if Guide Changed

If `guide/workflow-guide.qmd` was modified:
```bash
quarto render guide/workflow-guide.qmd
cp guide/workflow-guide.html docs/workflow-guide.html
```

### PHASE 5: Loop or Declare Clean

After fixing, launch a fresh set of 4 agents to verify.
- If new issues found → fix and loop again
- If zero genuine issues → declare clean and report summary

**Max loops: 5** (to prevent infinite cycling)

## Key Lessons from Past Audits

These are real bugs found across 7 rounds — check for these specifically:

| Bug Pattern | Where to Check | What Went Wrong |
|-------------|---------------|-----------------|
| Stale counts ("19 skills" → "21") | Guide, README, landing page | Added skills but didn't update all mentions |
| Hook exit codes | All Python hooks | Exit 2 in PreCompact silently discards stdout |
| Hook field names | post-compact-restore.py | SessionStart uses `source`, not `type` |
| State in /tmp/ | All Python hooks | Should use `~/.claude/sessions/<hash>/` |
| Hash length mismatch | All Python hooks | Some used `[:12]`, others `[:8]` |
| Missing fail-open | Python hooks `__main__` | Unhandled exception → exit 1 → confusing behavior |
| Python 3.10+ syntax | Type hints like `dict | None` | Need `from __future__ import annotations` |
| Missing directories | quality_reports/specs/ | Referenced in rules but never created |
| Always-on rule listing | Guide + README | meta-governance omitted from listings |
| macOS-only commands | Skills, rules | `open` without `xdg-open` fallback |
| Stale hook references | Rules, guide, CHANGELOG, settings.json | Removed hooks still mentioned somewhere |

## Output Format

After each round, report:

```
## Round N Audit Results

### Issues Found: X genuine, Y false alarms

| # | Severity | File | Issue | Status |
|---|----------|------|-------|--------|
| 1 | Critical | file.py:42 | Description | Fixed |
| 2 | Medium | file.qmd:100 | Description | Fixed |

### Verification
- [ ] No stale counts (grep confirms)
- [ ] All hooks have fail-open + future annotations
- [ ] Guide renders successfully
- [ ] docs/ updated

### Result: [CLEAN | N issues remaining]
```


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/pedrohcgs/claude-code-my-workflow/contents/.claude/skills/deep-audit/SKILL.md --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>pedrohcgs/claude-code-my-workflow</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../psantanna-workflow.md">Pedro Sant'Anna's Claude Code Workflow</a></dd>
<dt><b>Category</b></dt><dd><code>audit</code></dd>
<dt><b>Field</b></dt><dd>economics</dd>
<dt><b>Pipeline stages</b></dt><dd><code>referee-simulation</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow">⭐ pedrohcgs/claude-code-my-workflow</a><br><img src="https://img.shields.io/github/stars/pedrohcgs/claude-code-my-workflow?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/pedrohcgs/claude-code-my-workflow/blob/main/.claude/skills/deep-audit/SKILL.md" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/psantanna-workflow/deep-audit/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/psantanna-workflow.yml">edit on GitHub</a>.</p>
</div>

</div>
