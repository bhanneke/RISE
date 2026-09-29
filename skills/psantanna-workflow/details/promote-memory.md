---
name: promote-memory
description: Review candidate learnings in Claude Code's native auto memory (`~/.claude/projects/<project>/memory/`, machine-local) and run them through a five-critic council in parallel: generality, staleness, redundancy, evidence, format. Majority vote (3+ of 5) promotes the entry to MEMORY.md. Use when user says "promote memory", "review my learnings", "what should graduate to MEMORY.md", "five-critic council", or as monthly memory maintenance.
argument-hint: "[entry-substring or 'all']"
disable-model-invocation: true
allowed-tools: ["Read", "Write", "Glob", "Grep", "Agent", "Task", "Bash"]
metadata:
  author: Claude Code Academic Workflow
  version: 1.0.0
---

<!-- Pattern adapted with attribution from Chris Blattman's claudeblattman v2.1
     "Five-critic council" (claudeblattman.com, Apr 2026 continuous-improvement
     loop). Blattman uses it to decide what enters his MEMORY layer; we adapt
     it to the auto-memory → MEMORY.md promotion question codified in
     .claude/rules/meta-governance.md. -->

# `/promote-memory` — five-critic council for memory promotion

The template's [`meta-governance.md`](../../rules/meta-governance.md) rule splits memory into two tiers:

- **`MEMORY.md`** (committed, ≤ 200 lines) — generic learnings that help all forkers.
- **native auto memory** (`~/.claude/projects/<project>/memory/` — machine-local, typed `user`/`feedback`/`project`/`reference`, no size cap on topic files) — machine-specific and user-specific learnings.

The rule says generic patterns should sync via git; personal patterns stay local. **What it doesn't say** is *who decides which is which*. `/promote-memory` operationalizes the call: spawn five critics in parallel, each reviewing the candidate `[LEARN]` entries on a single dimension, and promote on majority vote (3+ of 5).

## When to use

- **Monthly memory maintenance.** Personal-memory accumulates faster than MEMORY.md; the council periodically harvests the genuinely generic learnings.
- **Before sharing a fork.** Someone is about to clone your template — what should they inherit?
- **After a large project ships.** Lessons from a paper or a course cycle deserve curation before the next project starts adding noise.
- **Not on a schedule.** This skill is user-invoked (`disable-model-invocation`), so a scheduled task cannot fire it, and its candidates live in machine-local auto memory that a cloud routine cannot see. Set yourself a monthly reminder and run it in a local session; every promotion waits for your approval anyway.

## When NOT to use

- **For a single fresh `[LEARN]` after a single correction.** Just let auto memory record it; let it sit until the next council runs.
- **For deleting stale entries.** Edit MEMORY.md by hand, per `meta-governance.md` (dated addendum, or a merge to hold the cap). `/promote-memory` never deletes — though near the cap it *proposes* a demotion (Step 4).
- **For project-specific context.** That belongs in CLAUDE.md or session logs, not in either memory tier.

## The five critics

Each critic runs in an isolated, fresh context (its own `Agent` call — never a conversation fork) — they don't see each other's verdicts or the user's draft. Each casts one **YES/NO** vote per candidate entry with a one-sentence rationale.

### 1. Generality critic

> "Would a non-econ forker benefit from this `[LEARN]` entry — a biology PhD, a sociology postdoc, a CS instructor? If the lesson is specific to *your* setup (your bibliography path, your machine's TeX install, your discipline's notation), vote NO."

### 2. Staleness critic

> "Does this entry contradict the current state of the codebase? Run `grep -r` on the file paths, function names, or settings the entry references. If the referenced thing has been renamed, removed, or significantly changed, vote NO — the entry is stale and would mislead a future session."

### 3. Redundancy critic

> "Is this lesson already encoded in MEMORY.md, CLAUDE.md, or an existing rule? Read the relevant files. If yes (even paraphrased), vote NO — duplication erodes the index's signal."

### 4. Evidence critic

> "Does the entry cite the incident, file path, or specific case that motivated it? If the entry is `[LEARN:foo] always do X` with no anchor to *why*, vote NO. Future Claude can't judge edge cases without the rationale."

### 5. Format critic

> "Does the entry fit the format of the tier it lands in? MEMORY.md entries are `[LEARN:category] wrong → right` (see [`MEMORY.md`](../../../MEMORY.md) itself); a feedback/project candidate coming from native auto memory should carry the `**Why:**` + `**How to apply:**` lines auto memory writes, so the reason survives the move. If it's just a free-form note, vote NO — fix the format first, then re-submit."

### Council verdict

Each critic returns YES/NO + rationale. The promotion threshold is **majority (3+ YES)**.

- **5 YES** — promote without modification.
- **4 YES** — promote with a one-line note about the dissenting concern.
- **3 YES** — promote but address the dissenting critics' concerns first (typically: trim, add evidence, fix format).
- **2 or fewer YES** — do not promote. Either fix the entry per the dissenting critics' feedback and re-submit, or leave it in auto memory.

## Steps

### Step 1: Read candidate entries

If `$ARGUMENTS` is `all`, read every topic file in `~/.claude/projects/<project>/memory/` (skip the `MEMORY.md` there: it is only an index pointing at the topic files); each topic file is one candidate. Otherwise treat `$ARGUMENTS` as a substring filter on a topic file's filename, `description`, or type (e.g., `latex` matches `feedback_latex_texinputs.md`, and `feedback` matches every feedback memory). Auto memory does not store entries in `[LEARN:category]` form; a candidate is rewritten into that shape only for the proposal in Step 4.

### Step 2: Spawn the council

Five `Agent` invocations in parallel, one per critic, each in a fresh context:

- **Generality critic** — context: the candidate entry + a one-paragraph description of who the template's audience is (academic researchers across disciplines).
- **Staleness critic** — context: the candidate entry + the ability to `Read` / `Grep` the codebase. Should explicitly check any file paths / function names / settings the entry references.
- **Redundancy critic** — context: the candidate entry + the current `MEMORY.md` + `CLAUDE.md` + relevant rule files.
- **Evidence critic** — context: the candidate entry only. Vote based on whether the entry self-describes its motivation.
- **Format critic** — context: the candidate entry + [`.claude/rules/meta-governance.md`](../../rules/meta-governance.md) for the schema reference.

Use the **Haiku tier** for all five critics (per [`.claude/rules/model-routing.md`](../../rules/model-routing.md): mechanical-ish review work). The user can override via the agent's `model:` field if they want Sonnet for the harder calls.

### Step 3: Aggregate votes

Collect verdicts. For each candidate entry, compute the vote count + per-critic verdicts.

### Step 4: Present the verdicts

For each entry:

```markdown
## `[LEARN:foo] <summary>`

**Vote:** 4-of-5 YES (promote with note)

| Critic | Vote | Rationale |
|---|:---:|---|
| Generality | YES | ... |
| Staleness | YES | ... |
| Redundancy | YES | ... |
| Evidence | NO  | Entry doesn't cite the originating incident. Add a one-line "Incident:" pointer before promoting. |
| Format | YES | ... |

**Recommendation:** Address Evidence critic, then promote.

**Proposed MEMORY.md addition:**
```text
[LEARN:foo] <full proposed text>
```
```

**Near the cap, adding means removing.** MEMORY.md is capped at 200 lines **and** 25KB, and the byte cap usually binds first. When the file plus the proposed additions would pass ~190 lines or ~24KB (`wc -c MEMORY.md`), the report also names the **weakest current entry** as a demotion candidate — stale (a named file, flag, or model that no longer exists), contradicted by a newer rule, or local rather than generic — with the evidence, and asks the user whether to move it to auto memory or delete it. The test for keeping an entry: *would removing it cause a mistake on many tasks?*

### Step 5: User approves the promotions

The user reviews the report and explicitly approves which entries to promote. The skill writes approved entries to MEMORY.md, marks the same entries in their auto-memory topic files with `# promoted YYYY-MM-DD` for audit, and surfaces a summary.

Do **not** auto-promote — even on 5-of-5 YES votes. The user's approval is the final gate.

## Output

- Per-entry council report (verdicts, rationales, recommendations) — to the conversation.
- On approval: MEMORY.md updated (append at appropriate `[LEARN:category]` section), the auto-memory topic file updated (entry marked promoted).
- A `quality_reports/memory_promotion_<date>.md` audit file recording the full council session for forensics.

## Anti-patterns

- **Auto-promoting on 5-of-5 YES.** Even unanimous critic agreement can be wrong; the user's domain judgment is the final gate.
- **Re-running the council on the same entry repeatedly** hoping for a different result. If 4 critics consistently say NO, the entry doesn't belong in MEMORY.md — leave it in auto memory and stop.
- **Skipping the Evidence critic** because the entry "looks obvious." Evidence is what makes the entry portable across forkers; obvious-to-you ≠ obvious-to-them.
- **Demoting via this skill.** It only promotes. Demotion is a manual edit + commit.

## Cross-references

- [`.claude/rules/meta-governance.md`](../../rules/meta-governance.md) — the two-tier memory contract this skill operationalizes.
- [`.claude/agents/promote-memory-council.md`](../../agents/promote-memory-council.md) — the five-critic implementation (one agent file with five role specs, dispatched in parallel via the `Agent` tool).
- [`.claude/rules/model-routing.md`](../../rules/model-routing.md) — why critics default to Haiku tier.
- `/learn` (existing skill) — captures new `[LEARN]` entries; pairs with `/promote-memory` (which decides what graduates).

## Source of candidates (v2.5)

Candidates come from **native auto memory** — `~/.claude/projects/<project>/memory/`. Claude
writes these itself as it works, typed `user` / `feedback` / `project` / `reference`, and the
`MEMORY.md` there is an index, not the content.

The promotion question is unchanged and is the whole point: *would a researcher in a different
field, forking this template, be better off knowing this?* If yes it belongs in the committed
`MEMORY.md`; if it is about this machine, this dataset, or this person's preferences, it stays
local.

**Retired:** `.claude/state/personal-memory.md`. The two-tier idea was right; Claude Code now
ships the local tier natively, so the hand-rolled file is redundant. An existing one still
reads as a plain file, but nothing writes to it.

## The capture gate — before anything is remembered

Promotion decides what becomes *shared* knowledge. This gate decides what is worth recording
**at all**. Five questions; a candidate must pass all five:

1. **Durable** — will this still be true in six months, or is it about today's branch?
2. **Non-obvious** — would a competent person rediscover it in five minutes anyway?
3. **Stable** — does it describe a rule, or a symptom that a fix will erase?
4. **Specific** — is it actionable, or is it a mood? *"Be careful with merges"* is a mood.
5. **Not already captured** — does an existing entry cover it? Extend that one instead.

> **Just-in-case memories are banned.** They pollute the index and make the useful entries
> unfindable. A memory store nobody trusts is a memory store nobody reads.

Promotion from local observation to committed knowledge is a **reviewed act, not an autosave** —
which is why the five-critic council exists and why the user is the final gate even on a
unanimous vote.
