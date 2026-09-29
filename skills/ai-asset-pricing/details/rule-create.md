---
name: rule-create
description: "Creates new .claude/rules/ files following best practices, or audits existing rules for quality and effectiveness."
argument-hint: "[new | audit [<path> | all]]"
---

# Rule Creator & Auditor

Two modes: **Create** a new rule or **Audit** an existing one.

## Examples

- `/rule-create` -- create a new rule (interactive)
- `/rule-create database patterns for PostgreSQL` -- create with topic description
- `/rule-create audit .claude/rules/validation.md` -- audit a specific rule
- `/rule-create audit all` -- audit all rules with summary table

## Mode Selection

Parse `$ARGUMENTS`:
- Empty, `new`, or a topic description → **Create mode**
- `audit`, `audit <path>`, or `audit all` → **Audit mode**

---

# CREATE MODE

Four phases: **Gather → Draft → Write → Verify**.

## Phase 1: Gather Context

### 1a. Scan existing rules
List all files in `.claude/rules/` to understand what rules already exist. This prevents creating duplicates and helps identify the right scope.

### 1b. Ask the user

If `$ARGUMENTS` contains a topic description (anything beyond `new`), use it as the domain. Otherwise, use `AskUserQuestion` with all of the following:

1. **Domain**: What does this rule cover? (e.g., database patterns, security, API conventions, testing, writing style, deployment)
2. **Scope**: What file types or paths should trigger this rule? Give glob patterns (e.g., `**/*.py`, `src/api/**/*.ts`) or say "always load" if it applies everywhere.
3. **Key constraints**: What are the 3-5 most important things Claude must know or do when this rule applies? Be specific — concrete patterns, not abstract goals.
4. **Bad patterns**: Are there specific anti-patterns or mistakes Claude should avoid? (optional but valuable)

### 1c. Check for overlap
Compare the user's answers against existing rules. If there's significant overlap with an existing rule, warn the user and ask whether to:
- Extend the existing rule instead
- Create a new focused rule covering only the non-overlapping parts
- Proceed anyway (user's call)

## Phase 2: Draft

### 2a. Choose a template

Based on the domain, select the best body pattern from the reference:

| Domain Type | Template Pattern | Best For |
|------------|-----------------|----------|
| Code conventions | Quick Reference + Sections | Naming, formatting, architecture patterns |
| Security / correctness | Do / Don't / Why / Refs | Vulnerability prevention, data integrity |
| Writing / style | Banned/Required + Examples | Prose style, documentation standards |
| Data / schema | Schema + Query + Gotchas | Database conventions, data pipelines |

### 2b. Generate the rule

Build the rule file with these requirements:

**Frontmatter:**
```yaml
---
description: [Specific, keyword-rich — Claude uses this to assess relevance]
paths:      # Omit entirely if the rule should always load
  - "[glob patterns from user input]"
---
```

**Description quality check:**
- Must be specific enough that Claude knows when to apply it
- Must contain keywords matching the domain (e.g., "PostgreSQL migration patterns for schema changes" not "Database best practices")
- Under 100 characters

**Scope-gating decision (`paths:` field):**

| Rule type | Scope | Rationale |
|-----------|-------|-----------|
| File conventions (naming, docstrings, formatting) | `paths: ["**/*.py"]` | Only relevant when editing those files |
| Workflow behavior (always save results, always use turnover=True) | **Unscoped** (omit `paths:`) | Must be active even during ad-hoc script execution |
| API gotchas (parameter validation, common mistakes) | **Unscoped** | Needed whenever writing API calls, not just editing source |

**Key lesson**: Path-scoped rules are invisible when the LLM isn't editing files matching those globs. If a rule governs *behavior* (not just *file conventions*), it must be unscoped.

**Body:**
- Use the selected template pattern
- Start with a Quick Reference section (3-5 lines summarizing the most critical points)
- Front-load: put the most important rules first
- Include concrete examples — both good patterns and bad patterns (with corrections)
- Use tables for lookup-style content (banned/preferred terms, naming conventions)
- Keep under 200 lines total

**Filename:**
- Lowercase, hyphens: `database-patterns.md`, `api-security.md`, `testing-conventions.md`
- Descriptive: the filename alone should communicate the rule's domain

### 2c. Print the draft
Show the complete rule to the user before writing. Ask if they want changes.

## Phase 3: Write

Write the file to `.claude/rules/{name}.md` using the Write tool.

Print confirmation:
```
Rule created: .claude/rules/{name}.md
Lines: {count}
Path scope: {paths or "always loaded"}
```

## Phase 4: Verify

Run the full audit checklist (from Audit Mode below) against the newly created rule. Report results inline. If any checks fail, offer to fix them immediately.

---

# AUDIT MODE

Three phases: **Read → Analyze → Report**.

## Phase 1: Read

- `audit <path>` → read that specific file (e.g., `audit .claude/rules/security.md`)
- `audit all` → list and read all `.md` files in `.claude/rules/`
- `audit` (no target) → list all rules as a numbered list, ask which to audit (or offer `all`)
- Also read the project's `CLAUDE.md` (for duplication checks)

## Phase 2: Analyze

Run 10 checks against the rule file. For each, determine PASS, WARN, or FAIL.

### 1. Focus
Does the rule cover one coherent topic?
- **PASS**: All sections relate to a single domain
- **WARN**: Minor scope creep (e.g., a database rule with one section on logging)
- **FAIL**: Mixes unrelated domains (e.g., testing + deployment + security in one file)

### 2. Length
Count total lines (including frontmatter and blank lines).
- **PASS**: Under 150 lines
- **WARN**: 150-200 lines (approaching limit)
- **FAIL**: Over 200 lines — suggest specific split points

### 3. Frontmatter Quality
- **PASS**: Has `description` that is specific and keyword-rich; `paths` scope matches rule type (file conventions → scoped; workflow/behavior rules → unscoped)
- **WARN**: Has `description` but it's vague (e.g., "Development standards"), or workflow rule is path-scoped (may be invisible during ad-hoc execution)
- **FAIL**: Missing `description`, or missing `paths` for a clearly file-specific rule, or behavior rule scoped to paths it won't match during normal workflow

### 4. Actionability
Does the rule contain concrete, implementable guidance?
- **PASS**: Contains code examples, tables, or specific patterns Claude can follow
- **WARN**: Some sections are abstract ("write clean code") without examples
- **FAIL**: Mostly abstract principles with no concrete patterns

### 5. Duplication
Does the rule repeat content from CLAUDE.md or other rule files?
- **PASS**: No meaningful overlap
- **WARN**: Minor overlap (same concept mentioned but with different detail level)
- **FAIL**: Paragraphs or sections duplicated verbatim

### 6. Procedure Leak
Does the rule contain step-by-step workflows that belong in a skill?
- **PASS**: States constraints and conventions only
- **WARN**: Has a short procedural section that could arguably be a constraint
- **FAIL**: Contains multi-step "how-to" procedures (e.g., "Step 1: Create file. Step 2: Run command. Step 3: ...")

### 7. Tool Overlap
Does the rule duplicate what linters, formatters, or CI already enforce?
- **PASS**: Rules address domain knowledge that tools can't capture
- **WARN**: One or two items that a tool could handle
- **FAIL**: Multiple rules about indentation, line length, import ordering, etc.

### 8. Front-Loading
Are the most important rules near the top?
- **PASS**: Critical constraints appear in the first half of the file; Quick Reference section present
- **WARN**: Important rules are present but buried in the middle/end
- **FAIL**: The most critical guidance is at the bottom

### 9. Example Quality
Do examples clearly show the right patterns?
- **PASS**: Both good and bad examples with explanations; code blocks or formatted comparisons
- **WARN**: Only good examples (no anti-patterns shown) or only bad examples
- **FAIL**: No examples at all

### 10. Completeness
Is anything obviously missing for this domain?
- **PASS**: Covers the key aspects of the domain; includes a checklist or summary
- **WARN**: Missing a checklist, or one important sub-topic seems absent
- **FAIL**: Major gaps — e.g., a security rule with no examples, a style rule with no banned patterns

## Phase 3: Report

Print the structured report:

```
RULE AUDIT REPORT
=================

File: {path}
Lines: {count}
Domain: {detected domain}
Path scope: {paths from frontmatter, or "always loaded"}

CHECKLIST:
[PASS] Focus: {brief explanation}
[WARN] Length: {line count} lines — {explanation}
[PASS] Frontmatter: {brief explanation}
[FAIL] Actionability: {brief explanation with specific section references}
[PASS] Duplication: {brief explanation}
[PASS] No procedures: {brief explanation}
[PASS] No tool overlap: {brief explanation}
[WARN] Front-loading: {brief explanation}
[PASS] Examples: {brief explanation}
[PASS] Completeness: {brief explanation}

SUGGESTIONS:
1. {Specific, actionable suggestion with section reference}
2. {Another suggestion}
3. ...

OVERALL: {N}/10 passed, {W} warnings, {F} failures
```

After printing the report, offer to fix any FAIL or WARN items if the user wants.

For `all` mode, after all individual reports, print a summary table:

```
SUMMARY: {N} rules audited
==============================
| Rule                   | Pass | Warn | Fail |
|------------------------|------|------|------|
| academic-writing       |   9  |   1  |   0  |
| latex-citations        |  10  |   0  |   0  |
| latex-compile          |   9  |   0  |   1  |
| latex-conventions      |  10  |   0  |   0  |
| presentation-rules     |   9  |   1  |   0  |
```

---

# Communication Rules

- Before Phase 1 (either mode), print: `Reading best practices reference...`
- In Create mode, always show the draft before writing
- In Audit mode, if auditing multiple files, print each report separately, then a summary table
- If a newly created rule fails its own audit, fix it before considering the skill complete
- Use tables for structured output; avoid walls of text
