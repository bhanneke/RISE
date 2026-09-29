---
name: create-skill
description: "Creates new Claude Code skills, auto-apply skills, or auto-trigger rules, or audits existing ones for quality and effectiveness."
argument-hint: "<skill-name> [description] | audit [skill-name | all]"
---

# Skill Creator & Auditor

Two modes: **Create** a new skill or **Audit** an existing one.

## Examples

- `/create-skill wrds-fundamentals` -- create a skill named `wrds-fundamentals`
- `/create-skill event-study "Auto-apply skill for event study methodology"` -- name + description
- `/create-skill audit wrds-psql` -- audit a specific skill
- `/create-skill audit all` -- audit all skills with summary table

## Mode Selection

Parse `$ARGUMENTS`:
- `audit`, `audit <name>`, or `audit all` → **Audit mode**
- Everything else (name, description, or empty) → **Create mode**

---

# CREATE MODE

Six phases: **Determine Type → Gather Requirements → Choose Pattern → Generate → Validate → Register**.

## Phase 1: Determine Type

Parse `$ARGUMENTS`:
- **First token** = skill name (validate in Phase 2)
- **Remaining tokens** (if any) = optional description

If `$ARGUMENTS` is empty, use `AskUserQuestion` to ask:
> "What do you want to create? Provide a name (lowercase, hyphens) and choose a type."

Three types with different file locations and frontmatter:

| Type | Location | Key frontmatter |
|------|----------|-----------------|
| **User-invocable skill** (`/name`) | `.claude/skills/{name}/SKILL.md` | `name`, `description`, `argument-hint` |
| **Auto-apply skill** (triggers on task match) | `.claude/skills/{name}/SKILL.md` | `name`, `description` (includes "Auto-apply when...") |
| **Auto-trigger rule** (triggers on file paths) | `.claude/rules/{name}.md` | `description`, `paths` (globs). **No `name` field.** |

**How to decide (type):**
- Does the user explicitly invoke it? → **User-invocable skill**
- Should it activate whenever Claude works on a matching task? → **Auto-apply skill**
- Should it activate whenever Claude edits files matching a glob pattern? → **Auto-trigger rule**

**Skill vs Agent decision (ask this first):**
| Question | Yes → | No → |
|----------|-------|------|
| Is the workflow rigid with known inputs? | **Skill** | Consider agent |
| Does it need judgment, discovery, or error recovery? | **Agent** | Skill |
| Will it run frequently (>5x/week)? | **Skill** (token savings compound) | Either |
| Does it need its own tool set or isolation? | **Agent** | Skill |

Skills run in the caller's context (zero spawn overhead, 75-80% fewer tokens than agents). If 90%+ of usage follows a fixed template, build a skill. Reserve agents for exploratory work. See `docs/AGENT_LESSONS_LEARNED.md` for case study.

## Phase 2: Gather Requirements

### Validate name

- Must match: `^[a-z][a-z0-9-]{0,63}$` (lowercase + hyphens, max 64 chars)
- **Reject** names containing "anthropic" or "claude" (reserved by Anthropic)
- **Reject** generic names: `helper`, `utils`, `tools`, `misc`, `data`, `general`, `common`, `documents`
- **Collision check:** if `.claude/skills/{name}/` or `.claude/rules/{name}.md` already exists, ask user whether to overwrite or pick a new name
- If invalid, explain the rules with examples and re-ask

### Collect requirements

Use a single `AskUserQuestion` to gather what's needed. Skip questions already answered by `$ARGUMENTS`:

1. **Purpose** (1-2 sentences): What does this skill do?
2. **Trigger conditions**: When should Claude activate this? (determines `description` field and rule globs)
3. **Arguments**: Does it take arguments? What format? (for `argument-hint`)
4. **Auxiliary files needed?** Reference docs, scripts, templates, style files?
5. **Closest existing skill**: Which skill in this project is most similar in structure?

If the user names an existing skill, read its SKILL.md to understand the pattern before proceeding.

## Phase 3: Choose Structural Pattern

Read the exemplar SKILL.md file for each relevant pattern before generating.

### Pattern catalog

| Pattern | When to use | Exemplar (read this) |
|---------|------------|---------------------|
| **Phased workflow** | Multi-step processes with dependencies between steps | `new-project/SKILL.md` (3 phases) |
| **Checklist / decision table** | Systematic validation, branching logic, audit | `submission-prep/SKILL.md` (10 categories) |
| **Code template** | Must produce or follow exact code patterns | `wrds-psql/SKILL.md` (pipeline template) |
| **Gotchas / known issues** | Encoding domain traps Claude must avoid | `wrds-psql/SKILL.md` (19 numbered items) |
| **Reference table** | Quick-lookup data (palettes, sizes, thresholds) | `publication-figures/SKILL.md` |
| **Philosophy + principles** | Judgment-heavy tasks needing guiding principles | `build-deck/SKILL.md` (Rhetoric of Decks) |

### Common combinations

Most skills combine 2-3 patterns:
- **Phased workflow + code template**: `wrds-psql`, `onboard`
- **Checklist + reference table**: `submission-prep`, `style-check`
- **Philosophy + phased workflow**: `build-deck`, `respond-to-referee`
- **Gotchas + reference table**: `panel-data-rules`, `wrds-psql`

### Degrees of freedom

Match specificity to the task's fragility:

- **Low freedom** (exact scripts/templates): Fragile tasks where errors are costly. Write exact code blocks, step-by-step commands, no deviation. Example: `wrds-psql` pipeline.
- **Medium freedom** (checklists, decision tables): Stable structure, variable content. Write rules with room for judgment. Example: `submission-prep` checks.
- **High freedom** (principles, examples): Creative or judgment-heavy tasks. Write guiding principles and exemplars, let Claude adapt. Example: `write-section`, `respond-to-referee`.

**Before generating, read 1-2 exemplar SKILL.md files** for the chosen pattern(s). This grounds the output in proven patterns from this project.

## Phase 4: Generate the Skill

### Frontmatter

**For user-invocable or auto-apply skills:**

```yaml
---
name: {validated-name}
description: "{third-person description stating WHAT and WHEN, max 1024 chars}"
argument-hint: "{format hint, only if skill takes arguments}"
---
```

**For auto-trigger rules:**

```yaml
---
description: {third-person description of what the rule enforces}
paths:
  - "**/*.{ext}"
  - "{other glob patterns}"
---
```

Rules have NO `name` field. The `paths` field lists glob patterns that trigger the rule.

### Description writing rules

- **Third person**: "Analyzes code for..." not "Analyze code for..."
- **State WHAT + WHEN**: "Extract text from PDFs. Use when working with PDF files or document extraction."
- **Auto-apply skills**: Description must include "Auto-apply when..." trigger clause
- **Include trigger phrases** users would actually say
- **Add negative triggers** if needed: "Do NOT use for simple X (use Y instead)."
- **Max 1024 characters**, no XML angle brackets (`< >`)
- **Debug test**: If someone asks Claude "when would you use {name}?", the description alone should give a clear answer

### Body structure

```markdown
# {Human-Readable Skill Name}

{1-2 sentence purpose statement}

## Examples                          ← only for user-invocable skills
- `/skill-name` -- basic usage
- `/skill-name arg` -- with argument
- `/skill-name --flag` -- variant

{Body sections using chosen pattern(s)}

## Output                           ← if skill produces a report/summary
{Template of what Claude prints when done}
```

### Body writing rules

- **Under 500 lines total.** If approaching this, split reference content into auxiliary files.
- **Challenge every paragraph**: "Does Claude already know this? Does this justify its token cost?"
- **Assume Claude knows** programming, standard tools, common patterns. Only add what's genuinely new: domain rules, project conventions, gotchas, non-obvious sequences.
- **Use forward slashes** in all paths (never Windows backslashes).
- **Provide defaults**, not menus. If there are multiple valid approaches, pick one and note alternatives briefly.
- **No magic numbers** in code blocks — document every value with justification.
- **Auto-apply enforcement**: If the skill has auto-apply behavior, also add a backup rule in `.claude/rules/workflow.md` (or similar). Auto-apply triggers depend on the LLM noticing the description — rules are guarantees. Critical workflows need both.

### Auxiliary files

Only create auxiliary files if:
1. The body would exceed ~400 lines without splitting
2. The content is reference data (lookup tables, code libraries) not core workflow
3. The file can stand alone without needing SKILL.md context

Keep references **ONE level deep** from SKILL.md. Never chain: file A → file B → file C.

For reference files longer than 100 lines, include a **table of contents** at the top.

## Phase 5: Validate

Read `best-practices.md` (in this skill's directory) and run the validation checklist against the generated skill.

### Frontmatter checks

- [ ] `name` matches `^[a-z][a-z0-9-]{0,63}$` (skills) or is absent (rules)
- [ ] `description` under 1024 chars
- [ ] `description` contains no XML tags (`< >`)
- [ ] `description` is in third person
- [ ] `description` states both WHAT and WHEN
- [ ] No "anthropic" or "claude" in name
- [ ] For auto-apply: description includes "Auto-apply when..." clause
- [ ] For rules: `paths` field present with valid glob patterns

### Body checks

- [ ] Total line count under 500
- [ ] No Windows-style paths
- [ ] No tool/package assumptions without checking availability
- [ ] No menus of options without a default
- [ ] Every paragraph earns its token cost
- [ ] `## Examples` section present (if user-invocable)
- [ ] `## Output` section present (if skill produces reports)

### Anti-pattern checks

- [ ] No deeply nested references (max 1 level from SKILL.md)
- [ ] No generic naming (helper, utils, misc, etc.)
- [ ] No verbose explanations of things Claude already knows
- [ ] No time-sensitive information without deprecation markers

**Fix any violations before presenting the skill to the user.**

## Phase 6: Register

### Update CLAUDE.md

1. Read root `CLAUDE.md` and find the `## Skills & Rules` section
2. Determine the correct category subsection:
   - `### Factor Construction & Data` — domain skills for PyBondLab
   - `### Infrastructure` — meta-skills for creating/auditing skills, rules, agents
3. If no category fits, add to the nearest one or propose a new `### Category` section
4. Add a line using the **exact format** (note: em-dash `—`, not `--`):
   - User-invocable: `- \`/skill-name\` — One-line description`
   - Auto-apply: `- \`skill-name\` — One-line description. Auto-apply when...`
   - Rule: `- \`rule-name\` — One-line description`

### Update README.md (infrastructure skills only)

Only add to the README skills tree if the skill is infrastructure-level (not domain-specific). Add under the `skills/` section:
```
    {name}/SKILL.md                    # Short description (/skill-name)
```

### Print summary

```
SKILL CREATED: {name}
==================

Type: {user-invocable skill | auto-apply skill | auto-trigger rule}
Location: {file path}
Patterns: {chosen patterns}
Lines: {line count} / 500

Registered in CLAUDE.md under: {category}

Files created:
  {list of files with line counts}

To test: ask Claude "when would you use {name}?" — the description should give a clear answer.
```

---

# AUDIT MODE

Four phases: **Read → Analyze → Report → Fix**.

## Phase 1: Read

Parse the audit target from `$ARGUMENTS`:
- `audit <name>` → read `.claude/skills/{name}/SKILL.md`
- `audit all` → list and read all `SKILL.md` files in `.claude/skills/*/`
- `audit` (no target) → list all skills as a numbered list, ask which to audit (or offer `all`)

Also read:
- `best-practices.md` (in this skill's directory) for evaluation criteria
- Root `CLAUDE.md` to check ecosystem registration

## Phase 2: Analyze

Run 12 checks grouped in 4 categories. For each: **PASS**, **WARN**, or **FAIL**.

### A. Frontmatter Quality

#### A1. Name Valid
- **PASS**: `name` present, matches `^[a-z][a-z0-9-]{0,63}$`, no reserved words ("anthropic", "claude"), not generic
- **WARN**: Name valid but generic (e.g., `helper`, `data`, `utils`)
- **FAIL**: Missing `name`, invalid characters, or contains reserved words

#### A2. Description Present
- **PASS**: `description` present, non-empty, under 1024 characters, no XML angle brackets
- **WARN**: Present but under 50 characters (likely too vague for routing)
- **FAIL**: Missing or empty

#### A3. Description Quality
- **PASS**: Third person, states both WHAT and WHEN
- **WARN**: First person, or missing WHEN clause
- **FAIL**: Neither WHAT nor WHEN stated

#### A4. Type-Specific Fields
- **PASS**: Auto-apply has "Auto-apply when..." clause; user-invocable with args has `argument-hint`; rules have `paths`
- **WARN**: Field present but imprecise (vague argument-hint, overly broad paths)
- **FAIL**: Required field missing for the skill's type

### B. Body Quality

#### B5. Line Count
- **PASS**: Under 400 lines
- **WARN**: 400-500 lines (approaching limit)
- **FAIL**: Over 500 lines (suggest splitting into auxiliary files)

#### B6. Structured Sections
- **PASS**: Clear headers, organized by pattern (phased workflow, checklist, etc.)
- **WARN**: Missing 1-2 expected sections
- **FAIL**: Unstructured wall of text or only 1 section

#### B7. Examples Section
- **PASS**: `## Examples` present with usage patterns (user-invocable) or N/A (auto-apply/rules)
- **WARN**: Examples present but incomplete (missing argument variants)
- **FAIL**: Missing for a user-invocable skill

#### B8. Token Efficiency
- **PASS**: No verbose fundamentals Claude already knows; every paragraph earns its cost
- **WARN**: 1-2 sections could be trimmed
- **FAIL**: Substantial filler content

#### B9. Anti-Patterns
Check for: Windows-style backslash paths, menus without defaults, nested references deeper than 1 level, tool/package assumptions without availability checks.
- **PASS**: None found
- **WARN**: 1-2 minor instances
- **FAIL**: Systemic anti-pattern usage

### C. Ecosystem Integration

#### C10. CLAUDE.md Registration
Check root `CLAUDE.md` for the skill under the Skills & Rules section.
- **PASS**: Listed in correct category with matching description
- **WARN**: Listed but description or category doesn't match
- **FAIL**: Not listed at all

#### C11. Auxiliary Files
Check if body references other files (e.g., `best-practices.md`, templates).
- **PASS**: All referenced files exist; max 1 level deep from SKILL.md
- **WARN**: Referenced file exists but appears unused by the skill body
- **FAIL**: Referenced file missing, or chain references (A → B → C)
- **N/A**: No auxiliary files referenced (mark as PASS)

### D. Cross-Skill Consistency

#### D12. No Scope Overlap
Compare this skill's description against all other skills.
- **PASS**: No substantial overlap with other skills' descriptions
- **WARN**: Minor wording overlap (different skills, similar phrasing)
- **FAIL**: Another skill covers the same domain (creates routing ambiguity)

## Phase 3: Report

Print structured report:

```
SKILL AUDIT: {name}
=============================
File: .claude/skills/{name}/SKILL.md | Lines: {count} | Type: {user-invocable|auto-apply|rule}

A. FRONTMATTER          B. BODY QUALITY
[PASS] A1 Name          [PASS] B5  Lines ({n})
[PASS] A2 Description   [PASS] B6  Sections
[PASS] A3 Desc quality  [PASS] B7  Examples
[PASS] A4 Type fields   [PASS] B8  Token efficiency
                         [PASS] B9  Anti-patterns

C. ECOSYSTEM            D. CONSISTENCY
[PASS] C10 CLAUDE.md    [PASS] D12 Overlap
[PASS] C11 Aux files

SUGGESTIONS:
1. [B5] At 478 lines, approaching the 500-line limit.

RESULT: 12/12 passed, 0 warnings, 0 failures
```

For `all` mode, print each skill's report separately, then a summary table:

```
SUMMARY: {N} skills audited
==============================
| Skill                  | Pass | Warn | Fail |
|------------------------|------|------|------|
| build-deck             |  12  |   0  |   0  |
| create-skill           |  11  |   1  |   0  |
| wrds-psql              |  12  |   0  |   0  |
| ...                    |      |      |      |
```

## Phase 4: Fix (Optional)

After reporting, offer to fix FAIL items:

- "Would you like me to fix the {N} FAIL items? I'll show each proposed change before applying."
- **C10 (CLAUDE.md)**: propose adding skill to correct category
- **A3 (description)**: propose rewritten description in third person with WHAT+WHEN
- **B7 (examples)**: propose `## Examples` section with usage patterns
- Other items: describe the fix, get approval, apply

Never auto-fix without showing the proposed change first.

---

# Communication Rules

- Before Phase 1 (either mode), print: `Reading best practices reference...`
- In Create mode, always show the draft before writing
- In Audit mode, if auditing multiple skills, print each report separately, then a summary table
- If a newly created skill fails its own audit, fix it before considering the skill complete
- Use the compact report format above — avoid walls of prose
