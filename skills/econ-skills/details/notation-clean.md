---
name: notation-clean
description: Audit and simplify mathematical NOTATION in LaTeX/markdown documents to Econometrica publication standard — inline one-shot symbols, ratios-of-parameters below the 5-use threshold, Greek letters used for non-parameters, and collisions with reserved standard notation. Trigger only when the request is specifically about notation (e.g., "fix the notation", "clean up notation", "too much notation", "notation-heavy", "excessive notation", "don't introduce new Greek letters"). Skip in favor of /audit-econ for general audit or math correctness, /latex-doc for compile errors, /simplify for code. Also invoke proactively when Claude introduced new sub-notation during a derivation in the current conversation.
argument-hint: <target_path> [--mode audit|fix|both] [--agents N]
---

# Notation Audit & Cleanup

Audit and simplify mathematical notation in research documents. Enforces the Econometrica-level convention that notation is minimal, consistent, and earns its place.

## Trigger conditions

**Invoke** when the user's request is specifically about notation — the word "notation" or a synonym pointing at symbols ("sub-notation", "symbols", "Greek letters", "shortcuts") is in the request. Representative phrases: "notation audit", "fix the notation", "clean up notation", "simplify notation", "too much notation", "excessive notation", "notation-heavy", "too many symbols", "don't introduce new Greek letters".

**Proactive invocation**: invoke *without being asked* only when Claude itself introduced new notation during a derivation in the current conversation (e.g., defined `γ ≡ α/β`, or used a new Greek for a mid-step quantity) — and it ended up used fewer than 5 times or violates a rule in `notation-rules.md`. A derivation that is merely long but reuses established symbols does NOT trigger this. Use the **fast path** below for proactive invocation.

**Do not invoke** for generic "audit"/"review" (→ `/audit-econ`), compile errors (→ `/latex-doc`), code cleanup (→ `/simplify`), or math correctness (→ `/audit-econ`). If ambiguous, ask once: "Notation pass, math-correctness audit, or both?"

## Before starting

Read `references/notation-rules.md` — authoritative for Greek/Latin conventions, reserved symbols (β, r, t, T, k, κ, τ, ...), the 5-use rule, and exception handling. Read each run; the user may update it.

## Arguments

`$ARGUMENTS` may contain:
- **target_path**: file(s) or directory. If missing, ask or use current conversation's math.
- **--mode**: `audit` (report only), `fix`, `both` (default).
- **--agents N**: sub-agents for file audits (default 1 for short files and in-conversation, 2 for full papers).

Supported: `.tex`, `.md` with LaTeX math. `.docx` → ask user to export first. Conversation math → use the fast path.

## Fast path (in-conversation and short derivations)

Use this when the target is math in the current conversation, a single short section, or a proactive check — NOT a full paper.

1. Apply the rules in `notation-rules.md` directly (no sub-agents, no symbol table).
2. Output using Template D from `references/response-templates.md` — a compact list of at most 5 items, each with the symbol, the problem in one sentence, and the inlined rewrite.
3. If the math is clean, one line: "Notation pass: clean."

Skip the rest of the skill. This is the common case for proactive invocation and keeps the quality gate cheap.

## Full path (file audits)

For `.tex` / `.md` files or multi-section audits. Five phases.

### Phase 1: Read and dispatch

Read the full target. Follow `\input{}` / `\include{}` in `.tex`. Building a symbol table is optional scaffolding — do it only if the document is large enough that you need the index to reason about coverage.

Dispatch N sub-agents (default 1 for short files, 2 for full papers) in a single parallel Agent call. Each receives the file path(s), the full contents of `notation-rules.md` pasted into the prompt, and Template 1 from `references/subagent-prompts.md`. Sub-agents work independently.

### Phase 2: Consensus

Collect `FINDING` blocks from each sub-agent. Severity guide:

- **High** — one-shot symbol (used 1–2×) where inlining clarifies; Greek letter for a non-parameter; reserved standard symbol (β, r, t, T, k, κ, τ) used for a non-standard role.
- **Mid** — compound shortcut used 3–4× (below threshold); small/capital Latin stock convention broken; inconsistent decoration.
- **Low** — cosmetic; duplicate definition; flagged exception (rule conflict that deserves surfacing).

When sub-agents disagree, pick the stricter reading. Deduplicate findings that refer to the same symbol.

### Phase 3: Present findings

Use Template A from `references/response-templates.md` (findings table). Sort High → Mid → Low, then by location. No commentary outside the table.

Ask the user to pick: **Apply all**, **Apply subset**, or **Sequential**. Stop here if `--mode audit`.

### Phase 4: Apply fixes

For each approved finding:
- **Inline** — replace a compound symbol with its primitive expression; remove the definition.
- **Rename** — keep the object, change its letter to satisfy the convention.
- **Keep as exception** — leave it, add a `% Exception: ...` comment next to the first definition.

Use `Edit` with `replace_all` only when the symbol token is unambiguous (e.g., `\gamma_1`); otherwise edit with surrounding context. After `.tex` edits, compile using the `/latex-doc` protocol and read the log.

Dispatch one verification sub-agent with Template 2 from `references/subagent-prompts.md`. Iterate if it fails.

### Phase 5: Report

Use Template B from `references/response-templates.md`. List what was applied, what was kept as exception, which file(s) changed. Cite full paths.

## Workflow rules

- **Read `notation-rules.md` every run** — don't rely on memory. It is the source of truth for *what* to flag; this file governs *how* to run the audit.
- **Never change mathematics.** Edit symbols, not meaning. If inlining would require non-trivial algebra, stop and flag.
- **Preserve compile-ability.** After any `.tex` change, compile and check the log.
- **Flag exceptions, don't invent them.** When rules conflict or the literature's standard breaks the convention, surface it as a Low-severity flagged exception rather than silently accepting.
- **Table speaks for itself.** No commentary outside the findings table. Final report is short.
