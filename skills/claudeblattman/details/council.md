# /council — Parallel Critics + Separate Synthesis

*v1.3 — Removed the Phase 4 "rate-limit advisory" line: it depended on response headers that aren't accessible under OAuth-only auth, so it printed "unavailable" on every run. The "Ctrl-C to abort" affordance was also phantom — print and dispatch happen in the same model turn, so there's no actual abort window. Replaced with a clean dispatch announcement: `$PANEL_NAME panel: dispatched N critics on $COUNCIL_CRITIC_MODEL`. v1.2 added `--chef-skill`. v1.1 added `--mixed` (cross-vendor peer). v1.0: dispatches N critic agents in parallel, runs a separate synthesis pass; hard cap 5; single-round only; never majority-votes on narrative output.*

Dispatches N critic agents in parallel, collects raw outputs, and runs a separate synthesis pass. Hard cap of 5 critics. Single-round only. Never majority-votes on narrative output.

## Quick Start

The fastest path that works out of the box:

```
/council --chef-skill <topic or file:path>
```

This uses a hardcoded 3-role panel (skill-engineer + UX-for-tools + non-expert-adoption) implemented as `general-purpose` subagents with inline role-strings. **No persona files required** — runs immediately.

For broader use (plan / paper / decision / grant panels), see "Default panels" below — those require persona agent files in `~/.claude/agents/`.

## Config

```
COUNCIL_CRITIC_MODEL=opus       # or sonnet for cheaper runs
COUNCIL_SYNTHESIS_MODEL=opus
COUNCIL_MAX_CRITICS=5
COUNCIL_DEFAULT_N=3
```

Models are set here, not in persona frontmatter. Next-model migration = edit two lines.

## Invocation

**Primary:** `/council <topic>` or `/council file:<path> [flags]`

**Natural-language triggers:**
- "spin up a council on X" / "council this" / "panel of advisors"
- **Chef-skill voice triggers** → auto-set `--chef-skill`: "council this skill" / "skill council" / "council on this tool / command / workflow" / "bespoke skill council"
- Meta-reference guard: sentences *about* councils as a topic are not invocations. On low confidence, ask one line.

## Flags

| Flag | Effect |
|------|--------|
| `--panel a,b,c` | Explicit persona list (names without `-agent` suffix) |
| `--n K` | Number of critics (default 3, max 5) |
| `--type plan\|paper\|decision\|grant` | Forces panel default + synthesis branch |
| `--mixed [codex\|gemini]` | Swap ONE Claude critic for a cross-vendor peer |
| `--chef-skill` | Hardcoded 3-role skill/tool-design panel. Bypasses panel resolution and persona-file check. **Works out of box.** |

## Default panels (resolve from `--type` or keyword inference)

These require persona agent files in `~/.claude/agents/`. The file naming convention is `<persona-name>-agent.md` or `experts/<persona-name>.md`.

| Task type | Default panel | N |
|-----------|---------------|---|
| Plan / architecture review | skills-engineer, skeptic, pre-mortem, budget-hawk | 4 |
| Paper / proposal review | academic-editor, harsh-referee, methodologist | 3 |
| Grant proposal | academic-editor, harsh-referee, methodologist, grant-strategist, funder-officer | 5 |
| Decision support | skeptic, pre-mortem, chief-of-staff | 3 |
| Ambiguous | prompt user to pick | — |

If you don't have these persona files yet, use `--chef-skill` for skill-design topics or run with explicit `--panel` listing personas you do have. The skill aborts cleanly if a referenced persona file is missing — no silent fallback to `general-purpose`.

Keyword inference (used if `--type` not given): "plan / architecture / design" → plan; "paper / referee / submission / manuscript" → paper; "proposal / grant / funder / NSF / Gates" → grant; "should I / go-no-go / accept / reject / decide" → decision; else ambiguous → ask.

## Dispatch phases

### Phase 1 — Parse and resolve

1. Parse topic + flags.
2. If `file:<path>`, Read the file; that is the content for the critics.
3. Resolve panel:
   - Explicit `--panel` → use verbatim
   - `--type X` → use that row's panel
   - Keyword inference → pick type
   - Ambiguous → ask one line: "Panel type: plan / paper / decision / grant?"
4. Cap N at `COUNCIL_MAX_CRITICS`. If user asks for >5, refuse with: "Hard cap is 5. Pick a tighter panel."

### Phase 1.5 — `--chef-skill` short-circuit

If `--chef-skill` flag is set, skip Phases 2 (meta-guard) and 3 (persona-file check). This branch ships a hardcoded 3-role panel for skill/tool-design review, dispatched as `general-purpose` subagents with inline role-string prefixes — not persona files.

Pre-populate these 3 role-strings and jump directly to Phase 5 dispatch:

1. **Skills engineer** — *"Will this skill work, will it last, and does the abstraction earn its keep? Focus on: invocation discoverability, prompt-budget discipline, failure recovery, and whether it duplicates existing skill/rule coverage."*
2. **UX-for-tools critic** — *"Where does this add friction, cognitive load, or break on voice input? Focus on: flag syntax vs. natural-language triggers, multi-step workflow friction, CLI ergonomics."*
3. **Non-expert adoption critic** — *"Will a junior user with <10h Claude Code successfully invoke and recover from failure? Focus on: discoverability of invocation, clarity of error messages, cold-start onboarding."*

Panel type for synthesis: **plan**. N critics: **3**.

### Phase 2 — Meta-reference guard

If invocation is via natural-language trigger (not explicit `/council`), classify whether this is an invocation or a meta-reference. Dispatch one short Task call to classify; if META or UNCLEAR, ask one line before dispatching critics. Skip this phase if `--chef-skill` is set.

### Phase 3 — Persona file existence check

For each persona in the resolved panel, Glob both:
- `~/.claude/agents/{name}-agent.md`
- `~/.claude/agents/experts/{name}.md`

If any persona file is missing, abort with a clear error listing the missing personas. **No silent fallback to `general-purpose`.** Skip this phase if `--chef-skill` is set.

### Phase 4 — Dispatch announcement

Print one line before the parallel Task calls:

```
$PANEL_NAME panel: dispatched N critics on $COUNCIL_CRITIC_MODEL
```

No terminal period (this is a status line, not prose). `$PANEL_NAME` is one of `plan` / `paper` / `decision` / `grant` / `chef-skill`. If `$COUNCIL_CRITIC_MODEL` resolves to a long versioned string, display the short label (e.g., `opus-4.7`).

<!-- v1.3: previous "Rate-limit advisory: unavailable…" line removed. The header-based advisory was structurally inert under OAuth-only auth, and "Ctrl-C to abort" was a phantom affordance (print and dispatch happen in the same model turn). If the harness later exposes rate-limit state via /status hook or env var, restore a real advisory here. -->


### Phase 4.5 — Peer swap (only if `--mixed` flag set)

If `--mixed codex|gemini` was passed, swap ONE Claude critic for a cross-vendor peer. Preserves the 5-critic cap.

**Persona-to-vendor auto-mapping:**

| Peer vendor | Best swap target | Rationale |
|---|---|---|
| Codex | `skeptic`, `pre-mortem`, or `harsh-referee` | Codex strong on empirical rigor + failure modes |
| Gemini | `completeness-checker`, `domain-expert`, or `academic-editor` | Gemini strong on long-context synthesis + broad coverage |

Pick the first match from the resolved panel. If none match, swap the last critic (deterministic).

The swapped Claude critic becomes a peer-vendor critic via Bash dispatch (Codex CLI or Gemini CLI). The other N-1 critics stay as Task dispatches. **Direction:** Claude → peer only. Do NOT dispatch peer-first-then-Claude (asymmetric dismissal).

If the peer binary is missing, print one line ("Gemini CLI not installed; falling back to all-Claude council") and continue with the unswapped panel. Graceful degradation.

### Phase 5 — Parallel Task dispatch

Send one message with N Task tool calls (true parallelism). Each call:
- `subagent_type`: persona slug (e.g., `skeptic-agent`)
- `model`: value of `COUNCIL_CRITIC_MODEL` (explicit, overrides any persona frontmatter)
- `description`: 3-5 word summary
- `prompt`: the topic or file content + brief instruction to produce raw critique in the persona's output shape

**Mixed mode addition:** If Phase 4.5 swapped a critic, include ONE Bash call in the same parallel message that invokes the peer binary. Output goes to `/tmp/council-peer-$RUN_ID.md`. The synthesis pass in Phase 7 reads the peer output alongside the Claude critic outputs.

**`--chef-skill` mode:** Dispatch 3 `general-purpose` Task calls in parallel (not persona-agent slugs). Each call's `prompt` opens with the corresponding role-string from Phase 1.5 as a prefix, followed by the topic/file content and the instruction *"Produce raw critique in this role's voice. End with VERDICT: APPROVE | REVISE + one-line rationale."*

### Phase 6 — Collect

Collect raw critic outputs. Do NOT inline-synthesize.

### Phase 7 — Separate synthesis dispatch

One more Task call:
- `subagent_type`: `general-purpose`
- `model`: `COUNCIL_SYNTHESIS_MODEL`
- `prompt`: synthesis template + the panel-type branch + raw critic outputs + original content

Panel-type branches:
- **plan** → Verdict (ship/revise/kill) → Top 3 blockers → Top 3 patches → per-critic verdict
- **paper** → Referee recommendation → Contribution-claim strength → Required revisions → Optional revisions → per-critic verdict
- **decision** → Recommended action → Top 3 risks → Top 3 reasons in favor → per-critic verdict
- **grant** → Paper branch + funder-officer fundability verdict

### Phase 8 — Emit

Emit the synthesis. Include raw critic outputs inside a `<details>` collapsible at the bottom for verification.

### Phase 9 — Log

Append one row to a council invocation log (e.g., `~/.claude-assistant/logs/council-invocations.csv`):

```
timestamp,run_id,topic,panel_resolved,critic_count,synthesis_verdict,wall_time_sec,model_critic,model_synthesis
```

## Why a Council

Multiple critics with explicit lenses outperform one general critic on review/decision tasks. The pattern:

- **Parallel** — each critic sees the same input and produces output independently
- **Separate synthesis** — a fresh-context model reads the raw critic outputs as data, not as conversation history
- **Single round** — no iterative debate. Round 2+ documented to drift toward conformity (see 2025-2026 multi-agent literature)
- **Hard cap 5** — beyond 5 critics, you get diminishing returns and harder synthesis

## Out of scope (v1.0+)

- Round 2 / iterative debate (single-round only)
- Majority voting on narrative output (conformity bias)
- LLM-proposed persona generation (`--chef` mode without `-skill`): requires a router. Hardcoded `--chef-skill` is the minimum-viable path for now.

## Performance Logging

```bash
echo "$(date +%Y-%m-%d),council,TOOL_CALLS,${N_CRITICS}-critics-${PANEL_TYPE}" >> ~/.claude-assistant/logs/skill-performance.csv
```

## Setup Notes

- For chef-skill mode: nothing required. Works out of box.
- For default panels: place persona agent files in `~/.claude/agents/`. The site provides one starter agent (`agents/proposal-critic-agent.md`); add more as you build out your panel library.
- For mixed mode: install the peer CLI (Codex via macOS app, Gemini via `npm install -g @google/gemini-cli`). The skill degrades gracefully if either is missing.
