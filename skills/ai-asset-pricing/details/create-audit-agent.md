---
name: create-audit-agent
description: "Creates new Claude Code agent configuration files or audits existing ones in .claude/agents/. Validates frontmatter, routing keywords, body-frontmatter alignment, ecosystem integration, and cross-agent consistency using a 17-point checklist."
argument-hint: "[agent-name | audit [agent-name | all]]"
---

# Agent Creator & Auditor

Two modes: **Create** a new agent or **Audit** an existing one.

## Examples

- `/create-audit-agent my-data-expert` -- create a new agent
- `/create-audit-agent audit my-data-expert` -- audit a specific agent
- `/create-audit-agent audit all` -- audit all agents with summary table

## Mode Selection

Parse `$ARGUMENTS`:
- `audit`, `audit <name>`, or `audit all` → **Audit mode**
- Anything else (name, description, or empty) → **Create mode**

---

# CREATE MODE

Five phases: **Gather → Reference → Generate → Register → Verify**.

## Phase 1: Gather Requirements

### 1a. Scan existing agents
List all `.md` files in `.claude/agents/` to prevent name collisions and understand existing scope.

### 1b. Ask the user

If `$ARGUMENTS` contains a name or description, use it. Otherwise, use `AskUserQuestion` with all of the following:

1. **Name**: lowercase-with-hyphens identifier (e.g., `my-data-expert`)
2. **Purpose**: What domain does this agent cover? What databases, tables, or APIs does it work with?
3. **Key routing terms**: What keywords should trigger delegation? (database names, table names, acronyms, paper names)
4. **Tools needed**: What tools should the agent have? (read-only vs full access, specific tools)
5. **Skills**: Should any skills be injected at startup? (e.g., `wrds-psql`)
6. **Model**: `inherit` (default), `sonnet`, `opus`, or `haiku`?

### 1c. Skill vs Agent decision
Before proceeding, ask: "Is this a known, rigid workflow with fixed inputs?" If yes, recommend a **skill** (`/create-skill`) instead. Agents are for tasks requiring judgment, discovery, or error recovery. Skills run in the caller's context with zero spawn overhead (75-80% fewer tokens). See `docs/AGENT_LESSONS_LEARNED.md` for rationale.

### 1d. Check for overlap
Compare the user's answers against existing agents. If there's scope overlap (same tables, same databases), warn the user and ask whether to:
- Extend the existing agent instead
- Create a new focused agent with clear scope boundaries
- Proceed anyway

## Phase 2: Generate

Build the agent `.md` file:

**Frontmatter:**
```yaml
---
name: [validated name]
description: "[WHAT + WHEN statement with 3 <example> blocks including <commentary>]"
tools: [appropriate tool list]
model: [inherit unless specified]
---
```

**Description requirements:**
- Include 3+ `<example>` blocks with realistic user queries, assistant responses, and `<commentary>`
- Include ALL key routing keywords: database names, table names, schema names, acronyms
- State WHAT the agent does and WHEN to use it
- Under 1024 characters (but multi-line with examples can be longer in practice)

**Body structure:**
```markdown
You are [role description matching frontmatter scope].

**Before running any psql query, invoke the `wrds-psql` skill** [if applicable]

## Overview
[Domain knowledge, key paper references, data sources]

## Table(s)
[Schema.table names with brief descriptions]

## Database Connection
[Connection pattern]

## [Domain-Specific Sections]
[Filters, identifiers, signal names, etc.]

## Example Queries
[2+ tested query patterns with explanations]

## Gotchas
[Data quality issues, common mistakes, edge cases]
```

**Body rules:**
- Opening paragraph must match frontmatter description scope exactly
- Under 400 lines preferred (warn at 400, fail at 600). Every line costs tokens on every spawn.
- No Windows paths, no verbose fundamentals Claude already knows
- Every paragraph must earn its token cost — if content exists in `.claude/rules/`, reference it with a one-liner instead of duplicating
- **Routing rule**: Create a corresponding entry in `.claude/rules/workflow.md` (or similar) stating WHEN to use this agent. Description-based routing is opt-in; rule-based routing is enforced.

### 3b. Show draft
Print the complete agent file to the user before writing. Ask if they want changes.

### 3c. Write
Write to `.claude/agents/{name}.md`.

## Phase 3: Register

### 4a. CLAUDE.md
Add the agent to the specialist agent list in root `CLAUDE.md` under "WRDS Database Access" (for WRDS agents) or appropriate section.

### 4b. Orchestrator dispatch table
If this is a WRDS agent, add a row to `.claude/agents/wrds-query-orchestrator.md` in the "Specialized Agents Available" table.

Print confirmation:
```
Agent created: .claude/agents/{name}.md
Lines: {count}
Registered in: CLAUDE.md, wrds-query-orchestrator.md
```

## Phase 4: Verify

Run the full 17-point audit checklist (from Audit Mode below) against the new agent. Report results. Fix any FAIL items before considering the skill complete.

---

# AUDIT MODE

Four phases: **Read → Analyze → Report → Fix**.

## Phase 1: Read

Parse the audit target from `$ARGUMENTS`:
- `audit <name>` → read `.claude/agents/{name}.md`
- `audit all` → list and read all `.md` files in `.claude/agents/`
- `audit` (no target) → list all agents as a numbered list, ask which to audit (or offer `all`)

Also read:
- Root `CLAUDE.md` to check ecosystem integration (specialist agent section)
- `.claude/agents/wrds-query-orchestrator.md` to check dispatch table (for WRDS agents, if it exists)

## Phase 2: Analyze

Run 17 checks grouped in 5 categories. For each: **PASS**, **WARN**, or **FAIL**.

### A. Frontmatter Quality

#### A1. Name Valid
- **PASS**: `name` present, matches `^[a-z][a-z0-9-]{0,63}$`, no reserved words ("anthropic", "claude"), not generic
- **WARN**: Name valid but generic (e.g., `helper`, `data-agent`, `utils`)
- **FAIL**: Missing `name`, invalid characters, or contains reserved words

#### A2. Description Present
- **PASS**: `description` present, non-empty, under 1024 characters
- **WARN**: Present but under 50 characters (likely too vague for routing)
- **FAIL**: Missing or empty

#### A3. Description Has Examples
- **PASS**: 3+ `<example>` blocks with realistic user queries and `<commentary>`
- **WARN**: 1-2 `<example>` blocks
- **FAIL**: Zero `<example>` blocks

#### A4. Routing Keywords Present
Scan body for database names, `schema.table` patterns (e.g., `contrib.global_factor`, `crsp.dsf`), key acronyms, and paper/author names. Check if each appears in the description.
- **PASS**: All key domain terms from body appear in description
- **WARN**: 1-2 key terms in body missing from description
- **FAIL**: 3+ key terms in body not in description (routing will fail — the JKP problem)

#### A5. Tools Field
- **PASS**: `tools` field present with tool list appropriate for agent's role
- **WARN**: `tools` omitted (inherits all — may be intentional but worth noting)
- **FAIL**: Role mismatch — read-only agent with Write/Edit, or WRDS agent missing Bash

### B. Body-Frontmatter Alignment

#### B6. Scope Match
Compare body opening paragraph with frontmatter description scope.
- **PASS**: Body scope matches description (same databases, same domain, same capabilities)
- **WARN**: Minor drift (body mentions something not in description, but it's related)
- **FAIL**: Body documents completely different databases/tools than description claims

#### B7. Keyword Coverage
Extract all `schema.table` patterns, database identifiers, acronyms, and domain terms from body. Compute what percentage appear in description.
- **PASS**: 90%+ of body domain terms appear in description
- **WARN**: 70-90% coverage
- **FAIL**: Under 70% (high routing failure risk)

#### B8. No Orphan Knowledge
Check if body contains substantial documentation for databases/tools/workflows NOT mentioned in the description.
- **PASS**: All body content falls within description's stated scope
- **WARN**: One tangential topic (brief mention)
- **FAIL**: Body includes substantial content outside description scope

### C. Body Quality

#### C9. Skill Invocation
- **PASS**: Body includes explicit skill invocation (e.g., "Before running any psql query, invoke the `wrds-psql` skill")
- **WARN**: Skill referenced but not as an explicit "invoke" instruction
- **FAIL**: No skill invocation for an agent that should use skills (e.g., any WRDS agent)
- **N/A**: Agent doesn't use skills (mark as PASS)

#### C10. Structured Sections
Check for organized sections with headers.
- **PASS**: Has Overview, Tables/Schema, Examples, and Gotchas sections (or equivalent)
- **WARN**: Missing 1-2 expected sections
- **FAIL**: Unstructured wall of text or only 1 section

#### C11. Example Queries
- **PASS**: 2+ example queries or code blocks that are syntactically plausible
- **WARN**: Only 1 example
- **FAIL**: No examples in body

#### C12. Line Count & Token Efficiency
Every line in an agent body is loaded on every spawn. Treat agent definitions like hot code paths.
- **PASS**: Under 400 lines; no sections that duplicate `.claude/rules/` content
- **WARN**: 400-600 lines, or body contains sections that restate rules already in `.claude/rules/` (suggest replacing with one-liner references like "See `.claude/rules/api-gotchas.md` for parameter validation")
- **FAIL**: Over 600 lines, or >50 lines duplicating rules files (move to rules, reference them)

#### C13. Anti-Patterns
Check for: Windows-style backslash paths, verbose explanations of fundamentals Claude already knows, magic numbers without justification, menus without defaults.
- **PASS**: None found
- **WARN**: 1-2 minor instances
- **FAIL**: Systemic anti-pattern usage

### D. Ecosystem Integration

#### D14. CLAUDE.md Registration
Check root `CLAUDE.md` for the agent under the specialist agent section.
- **PASS**: Listed with name and description matching the agent's actual scope
- **WARN**: Listed but description differs from agent's actual description/scope
- **FAIL**: Not listed at all

#### D15. Orchestrator Dispatch Table
For WRDS agents only: check `.claude/agents/wrds-query-orchestrator.md` dispatch table.
- **PASS**: Listed in orchestrator with matching use-case description
- **WARN**: Listed but description/scope outdated
- **FAIL**: Not in dispatch table (orchestrator won't route to it)
- **N/A**: Not a WRDS agent (mark as PASS)

### E. Cross-Agent Consistency

#### E16. Scope Overlap
Compare this agent's documented tables/schemas against all other agents.
- **PASS**: No table or schema documented in multiple agents (or overlap is an intentional cross-reference with clear ownership)
- **WARN**: 1-2 tables appear in multiple agents without clear ownership designation
- **FAIL**: Substantial schema overlap with another agent (creates routing ambiguity)

#### E17. Tool Allocation Consistency & Minimality
Each unused tool adds ~200 tokens of JSON schema to every spawn. Start minimal, add only when needed.
- **PASS**: Tool set is minimal for the agent's role; every listed tool is actually used in the agent's workflows
- **WARN**: 1-2 unnecessary tools present (e.g., WebFetch on an agent that never fetches URLs, Edit on an agent that only generates scripts)
- **FAIL**: 3+ unused tools, missing essential tools, or dangerous allocation (Write on read-only agent)

## Phase 3: Report

Print structured report:

```
AGENT AUDIT: {name}
=============================
File: .claude/agents/{name}.md | Lines: {count} | Model: {model}

A. FRONTMATTER          B. ALIGNMENT           C. BODY QUALITY
[PASS] A1 Name          [PASS] B6 Scope        [PASS] C9  Skill invocation
[PASS] A2 Description   [WARN] B7 Keywords     [PASS] C10 Sections
[PASS] A3 Examples      [PASS] B8 Orphans      [PASS] C11 Examples
[FAIL] A4 Routing                               [PASS] C12 Lines ({n})
[PASS] A5 Tools                                 [PASS] C13 Anti-patterns

D. ECOSYSTEM            E. CONSISTENCY
[PASS] D14 CLAUDE.md    [PASS] E16 Overlap
[PASS] D15 Orchestrator [PASS] E17 Tools

SUGGESTIONS:
1. [A4] Add "contrib.global_factor" and "JKP" to description — these
   key body terms are missing from routing metadata.
2. [B7] Keyword coverage is 75% — consider surfacing "permno",
   "gvkey" in description.

RESULT: 15/17 passed, 1 warning, 1 failure
```

For `all` mode, print each agent's report separately, then a summary table:

```
SUMMARY: {N} agents audited
==============================
| Agent                       | Pass | Warn | Fail |
|-----------------------------|------|------|------|
| crsp-wrds-expert            |  16  |   1  |   0  |
| jkp-wrds-expert             |  17  |   0  |   0  |
| bonds-wrds-expert           |  15  |   1  |   1  |
| ff-wrds-expert              |  16  |   0  |   1  |
| optionmetrics-wrds-expert   |  17  |   0  |   0  |
| taq-wrds-expert             |  16  |   1  |   0  |
| paper-reader                |  15  |   2  |   0  |
| wrds-query-orchestrator     |  16  |   1  |   0  |
```

## Phase 4: Fix (Optional)

After reporting, offer to fix FAIL items:

- "Would you like me to fix the {N} FAIL items? I'll show each proposed change before applying."
- **A4/B7 (routing keywords)**: propose updated description with missing terms added
- **D14 (CLAUDE.md)**: propose adding agent to specialist section
- **D15 (orchestrator)**: propose adding row to dispatch table
- **B6 (scope mismatch)**: propose updated body opening paragraph
- Other items: describe the fix, get approval, apply

Never auto-fix without showing the proposed change first.

---

# Communication Rules

- Before Phase 1 (either mode), print: `Reading agent configuration and reference material...`
- In Create mode, always show the complete draft before writing
- In Audit mode, if auditing multiple agents, print each report separately then the summary
- If a newly created agent fails its own audit, fix it before considering the skill complete
- Use the compact report format above — avoid walls of prose
