# Plan Review
*v1.3 — Step 7 logging hardened: routes through an atomic-write helper (no sync-race row loss) and adds a trailing `hostname` field for cross-machine diagnosis. Step 0 announces plan-mode detection (the harness blocks writes in plan mode → logging will be skipped for that run).*
*v1.2 — Added optional cross-vendor peer critic (Codex, Gemini) dispatched in parallel with the Claude critic.*
*v1.1 — Step 4 upgraded to agent dispatch for fresh-context review*

Stress-test a plan with structured expert critique, web research on best practices, and a revised version if needed. Use after developing a plan in plan mode, or on any plan file. Catches blind spots, missing steps, and wishful thinking.

**Pre-approved tools:** WebSearch, filesystem reads, and the Task tool (for agent dispatch in Step 4) are pre-approved. Call tools directly.

## Instructions

### Step 0: Pre-checks

**Plan-mode check (v1.3):** If this session is currently in Claude Code plan mode, announce up-front: *"⚠ Plan-mode detected — this run will NOT be logged to `skill-performance.csv` (the harness blocks file writes in plan mode, so Step 7 will silently fail). Invoke `/review-plan` outside plan mode if invocation-count accuracy matters."* Proceed with the review; the only affected step is Step 7 logging.

Parse `$ARGUMENTS` for flags. **If `$ARGUMENTS` is `help`, print the table below and stop — do not execute the review.**

| Flag | Syntax | Default | Purpose |
|------|--------|---------|---------|
| Help | `help` | — | Show this options table and stop |
| File path | `file:path` | Auto-detect | Explicit plan location |
| Expert role | `role:"..."` | Auto-detect | Override persona |
| Focus area | `focus:dimension` | All dimensions | Weight one dimension (e.g. `focus:feasibility`) |
| Depth | `depth:quick/standard/deep` | `standard` | Web research intensity |
| Quick | `quick` | Off | Shorthand for `depth:quick` |
| **Peer critic** | `peer:codex\|gemini\|both` | None (Claude-only) | Dispatch a cross-vendor critic in parallel with the Claude critic (see Step 4.5) |
| Dry run | `dryrun` | Off | Show role + research plan only |

**Natural-language peer keywords also recognized** (parse ARGUMENTS in-context):
- "with codex", "codex second opinion", "codex peer", "have codex critique" → `peer:codex`
- "with gemini", "from gemini", "have gemini critique", "gemini second opinion" → `peer:gemini`
- "with codex and gemini", "both peers", "cross-vendor" → `peer:both`

If ARGUMENTS mention "second opinion" or "another opinion" without a vendor, ask ONE clarifying question: "Which peer critic? codex / gemini / both / claude-only". Do NOT fabricate a default peer.

### Step 1: Locate and Read the Plan

Three-tier priority:
1. **Explicit file** — `file:path/to/plan.md` argument
2. **Plan-mode file** — most recent file in `~/.claude/plans/` (use Glob `~/.claude/plans/*.md`)
3. **Conversation history** — scan the current session for the plan developed in plan mode or discussed inline

If no plan found in any tier:
> "No plan found. Usage: `/review-plan` (after plan mode) or `/review-plan file:path/to/plan.md`"

If the plan is very short (<50 words), warn: "This plan is unusually brief. Proceeding, but the review may be limited."

Read the full plan content before continuing.

### Step 2: Assign Expert Role

Infer the domain from plan content using these heuristics:

| Domain signals | Assigned role |
|---------------|---------------|
| skill, command, agent, MCP, Claude Code | AI engineering and skill design specialist (include dimension 7) |
| proposal, grant, funder, budget | Grant strategy and research funding specialist |
| paper, manuscript, identification, regression | Academic research methodology specialist |
| project management, tracker, workflow, dashboard | Operations and project management specialist |
| data, analysis, pipeline, code, replication | Data science and reproducibility specialist |
| curriculum, teaching, syllabus | Academic program design specialist |
| Default (no strong signal) | Strategic planning and implementation specialist |

If `role:"..."` is provided, use that instead.

**Announce the role to the user:**
> "**Reviewing as:** Meticulous [role]. (Override with `role:"your preferred role"` if this doesn't fit.)"

If `dryrun`: Also show the planned web search queries (from Step 3) and stop. Do not execute the review.

### Step 3: Research Best Practices

**Query construction:** Extract the plan's primary *domain* and primary *technique/approach*. Build queries:
- Query A: "[technique/approach] best practices [year]"
- Query B: "[domain] common pitfalls" OR "[domain] failure modes"
- Query C (deep only): "[specific methodology in plan] implementation guide"
- Query D (deep only): "[domain] checklist [year]"

**Depth controls:**

| Depth | Web searches | Local references |
|-------|-------------|-----------------|
| `quick` | 0 — skip entirely | Scan local references for relevant files only |
| `standard` | 2 (queries A + B) | Same local scan |
| `deep` | 3-4 (queries A + B + C + D) | Same local scan |

**Local reference selection** (dynamic based on domain):
- Skill/agent plans → read your skill-patterns reference, if you maintain one
- Proposal plans → read your proposal voice reference, if you maintain one
- Other → scan a directory listing of local references for relevant files

**If web search fails:** Continue with local references only. Note: "Web research unavailable; review based on local references and domain knowledge."

**If local refs not found:** Continue without. Note which files were unavailable.

Distill research into 3-5 key principles relevant to this specific plan. These feed into the review.

### Step 4: Structured Review (Agent Dispatch)

**Dispatch a review agent for fresh-context critique.** This avoids the bias of reviewing your own plan inline.

Use the Task tool to launch a subagent with these parameters:
- **subagent_type:** Choose based on the assigned role from Step 2:
  - Grant/proposal plans → `Review Methodology` (if empirical) or `Review Writing` (if narrative-focused)
  - Skill/agent/technical plans → `general-purpose`
  - All other plans → `general-purpose`
- **model:** `sonnet` (fast, sufficient for structured critique)
- **timeout:** 60 seconds max

**Agent prompt template** (fill in the bracketed values):

```
You are a meticulous [expert role from Step 2]. Your job is to find what's missing, what will break, and what's wishful thinking. Do not rationalize or hedge.

PLAN TO REVIEW:
[Full plan text from Step 1]

BEST PRACTICES CONTEXT:
[3-5 principles from Step 3]

FOCUS AREA: [focus dimension if set, otherwise "all dimensions equally"]

Review against these 6 dimensions:

1. PRE-MORTEM: "It's 3 months later and this plan failed. Top 3 causes?" Work backward from failure. Single-point-of-failure assumptions? External dependencies that could break?

2. COMPLETENESS: What's missing that a domain expert would expect? All stakeholders, dependencies, inputs accounted for? What would a reviewer's first question be?

3. FEASIBILITY: Steps depending on unconfirmed resources, approvals, or data? Could each step be executed tomorrow? Are estimates realistic?

4. BEST-PRACTICE ALIGNMENT: How does this compare to the best practices provided? Where does the plan deviate — is the deviation justified?

5. SEQUENCING: Hidden blockers? Would reordering reduce risk or improve parallelism? Dependencies explicit? Critical path?

6. SPECIFICITY: Could someone unfamiliar execute each step? Where are the vague hand-waves ("figure out", "coordinate with", "as needed")? Success criteria defined?

7. AGENT ARCHITECTURE (include ONLY if domain = AI engineering / skill design; skip otherwise):
   - Single-agent gate: Does the plan establish single-agent reliability before spawning sub-agents?
   - context:fork discipline: Are sub-agents explicitly forked (context:fork) to prevent parent-state pollution?
   - Case facts: Is there a persistent structured handoff (shared state file, HANDOFF.md, or state object) so agents don't re-derive context each run?
   - Hook coverage: Are PostToolUse or stop_reason hooks specified for error detection where relevant?
   - Failure recovery: Is there a specified retry or fallback path, not just a "handle errors" hand-wave?
   Classify findings per the Red/Yellow/Green scheme below.

Classify each finding:
- Red — Critical. Will likely cause failure or major rework.
- Yellow — Important. Creates risk, but plan can proceed.
- Green — Minor. Nice-to-have.

Output format: For each dimension, list findings with classification. End with a VERDICT: APPROVE (no red issues, executable as-is) or REVISE (red issues or multiple yellows that collectively undermine the plan). If REVISE, include a revised plan with [CHANGED] and [NEW] markers.
```

**After the agent returns**, incorporate its findings into the output format in Step 5. If the agent fails or times out, fall back to inline review using the same 6 dimensions above.

### Step 4.5: Peer Critique (optional — only if peer flag is set)

If `peer:codex`, `peer:gemini`, or `peer:both` was parsed from ARGUMENTS (Step 0), dispatch the peer critic(s) **IN PARALLEL** with the Claude agent from Step 4. That means: send ONE message containing the Task call (Claude critic) AND the Bash call(s) (peer critic), not sequential.

**Load config values** from your deep-research config (a small file with binary paths, model names, and output formats for Codex and Gemini CLIs):
- Codex: `CODEX_BIN`, `CODEX_MODEL`, `CODEX_SANDBOX`, `CODEX_UNATTENDED_FLAG`
- Gemini: `GEMINI_BIN`, `GEMINI_OUTPUT_FORMAT`

**Graceful degradation:** If the required binary is missing (e.g., `$GEMINI_BIN` empty), skip that peer with a user-visible note ("Gemini CLI not installed; skipping Gemini peer critic. Run `npm install -g @google/gemini-cli`."). Do NOT fail the whole review.

**Peer prompt template** (same 6-dimension structure as Claude agent — just routed to the peer model):

```
You are a meticulous [expert role from Step 2]. You are being dispatched as a PEER CRITIC alongside a Claude reviewer — your job is to find things Claude might miss, particularly blind spots that stem from shared training-data priors.

PLAN TO REVIEW:
[Full plan text from Step 1]

BEST PRACTICES CONTEXT:
[3-5 principles from Step 3]

FOCUS AREA: [focus dimension if set, otherwise "all dimensions equally"]

Review against the 6 dimensions (Pre-Mortem, Completeness, Feasibility, Best-Practice Alignment, Sequencing, Specificity) + dimension 7 (Agent Architecture) if domain = AI skills. Full dimension definitions in the Claude agent prompt above — use the same framework.

Classify findings as Red / Yellow / Green. End with VERDICT: APPROVE or REVISE + brief rationale. Do not include a revised plan (Claude handles that in synthesis).
```

**Codex dispatch** (if `peer:codex` or `peer:both`):
```bash
"$CODEX_BIN" exec --model "$CODEX_MODEL" $CODEX_SANDBOX \
  $CODEX_UNATTENDED_FLAG \
  -o /tmp/review-codex-$RUN_ID.md \
  -- "$PEER_PROMPT" 2>/tmp/review-codex-$RUN_ID.stderr
```
The `--` separator is defense-in-depth against prompts containing `---` YAML-frontmatter tokens.

**Gemini dispatch** (if `peer:gemini` or `peer:both`):
```bash
"$GEMINI_BIN" "$PEER_PROMPT" --output-format "$GEMINI_OUTPUT_FORMAT" \
  > /tmp/review-gemini-$RUN_ID.json 2>/tmp/review-gemini-$RUN_ID.stderr
# Parse response field: jq -r .response /tmp/review-gemini-$RUN_ID.json > /tmp/review-gemini-$RUN_ID.md
```

**After ALL dispatches return** (Claude via Task, Codex via Bash, Gemini via Bash — all in one parallel message):
- Read each output file (`/tmp/review-codex-$RUN_ID.md`, `/tmp/review-gemini-$RUN_ID.md`).
- If any peer returned empty output or non-zero exit, note the failure in the output but proceed with remaining critics.
- Incorporate peer findings into Step 5 as distinct sections.

**Direction:** Claude→peer only. Do NOT dispatch peer-first-then-Claude-reacts. Reverse direction has documented asymmetric dismissal.

**Permission denial handling.** If the peer Bash call returns a tool-result containing "Permission for this action has been denied" OR matches the harness's heuristic message about untrusted code execution paths, the sandbox is blocking the peer binary. Do NOT retry or error. Instead:

1. Note the denial in the output as a peer-unavailable row ("⚠️ Codex peer denied by permission sandbox — prerequisite rule missing from settings.json").
2. Continue with the Claude critic's output only.
3. At the bottom of the output, surface one line telling the user how to add the peer binary path to their permissions allow-list.

This keeps the skill functional for users on fresh machines where settings haven't synced yet, rather than failing the whole review.

### Step 5: Generate Output

**Standard output format:**

```
════════════════════════════════════════════════
PLAN REVIEW — [Plan Title or Summary]
════════════════════════════════════════════════

**Reviewing as:** Meticulous [expert role]
**Plan source:** [file path / plan mode / conversation]
**Depth:** [quick / standard / deep]

────────────────────
BEST PRACTICES CONTEXT
────────────────────
[3-5 key principles from research, numbered]

────────────────────
STRENGTHS
────────────────────
1. **[Label]** — [Explanation]
2. ...

────────────────────
WEAKNESSES & GAPS (from Claude critic)
────────────────────
🔴 **[Label]** — [Issue] → **Fix:** [Specific recommendation]
🟡 **[Label]** — [Issue] → **Fix:** [Specific recommendation]
🟢 **[Label]** — [Issue] → **Fix:** [Specific recommendation]

────────────────────
PEER CRITIC(S)  (only present if peer: flag was set)
────────────────────
[One subsection per peer vendor dispatched, labeled by vendor]

**From Codex (gpt-5.x-codex):**
🔴 **[Label]** — [Issue from Codex's output] → **Fix:** [Recommendation]
🟡 ...
Verdict: APPROVE / REVISE — [rationale]

**From Gemini (gemini-2.5-pro or OAuth-default):**
🔴 **[Label]** — [Issue from Gemini's output] → **Fix:** [Recommendation]
🟡 ...
Verdict: APPROVE / REVISE — [rationale]

────────────────────
AGREEMENTS & DISAGREEMENTS  (only present if peer: flag was set)
────────────────────
**Agreements:** [Issues flagged by Claude AND peer(s); highest-confidence findings]
**Disagreements:** [Issues flagged by only one critic — surface without picking a winner]
**Unique per-peer insight:** [Anything the peer caught that Claude missed — the core value of cross-vendor dispatch]

────────────────────
VERDICT
────────────────────
✅ APPROVE — [Rationale + minor notes]
  OR
🔄 REVISE — [Rationale]. See revised plan below.
[If peers dispatched: note whether verdict was unanimous across critics or which critic dissented]

────────────────────
REVISED PLAN (only if REVISE)
────────────────────
[Full revised plan with [CHANGED] and [NEW] markers on modified/added sections]
════════════════════════════════════════════════
```

**Quick mode output** (condensed):

```
PLAN REVIEW (quick) — [Plan Title]
Verdict: ✅ APPROVE / 🔄 REVISE
Top issues:
1. [Most important]
2. [Second]
3. [Third]
[Revised plan if REVISE]
```

### Step 6: Iteration Gate

After presenting the review, ask:

> "Apply these revisions? Or provide feedback to refine further."

User can:
- **Accept** — apply revisions to the plan file (if file-based) or present final version
- **Give feedback** — loop back to Step 4 with user's notes incorporated
- **Dismiss** — end without changes

After 2 review cycles on the same plan, note:
> "This plan has been reviewed [N] times. Further iteration may have diminishing returns. Consider implementing and iterating in practice."

### Step 7: Log Performance

```bash
echo "$(date +%Y-%m-%d),review-plan,TOOL_CALLS,NOTES,$(hostname -s)" \
  >> ~/.claude-assistant/logs/skill-performance.csv
```

Replace TOOL_CALLS with your exact count of tool uses this run (no `~` prefix). Replace NOTES with a brief summary like `standard-depth-claude-only` or `deep-peer-codex-claude-approve` or `quick-revise-2-cycles`. If the peer flag was set, include the peer vendor(s) in notes (e.g., `peer-codex`, `peer-gemini`, `peer-both`).

**Schema note (v1.3):** rows now have a trailing `hostname` field (5 fields: `date,skill,tool_calls,notes,hostname`). Pre-v1.3 rows are 4 fields. Readers parsing positionally are unaffected; readers needing hostname should tolerate missing field on legacy rows.

**Plan-mode limitation (v1.3):** Claude Code plan mode blocks file-write Bash operations, so this log step will SILENTLY FAIL if `/review-plan` was invoked while the parent session is in plan mode. Step 0 announces this up-front so the user knows the run won't appear in skill-performance.csv. There is no fix at the skill level — the harness owns that constraint. If invocation-count accuracy matters for a given decision, run `/review-plan` outside plan mode.

## Error Handling

| Condition | Behavior |
|-----------|----------|
| No plan found | Usage message with examples |
| Web search fails | Continue with local references, note limitation |
| Local refs not found | Continue without, note which were unavailable |
| Plan very short (<50 words) | Warn, proceed anyway |
| `file:` path doesn't exist | "File not found: [path]. Check the path and try again." |

## Examples

```
/review-plan
/review-plan file:~/Documents/skill-plan.md
/review-plan quick
/review-plan depth:deep focus:feasibility
/review-plan role:"clinical trial design specialist" file:~/project/trial-plan.md
/review-plan dryrun
/review-plan peer:codex file:~/Documents/grant-plan.md
/review-plan peer:both depth:deep
```
