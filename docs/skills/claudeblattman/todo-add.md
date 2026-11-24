<!-- DO NOT EDIT — auto-copied from skills/claudeblattman/details/todo-add.md -->

# `/todo-add`

Add a task to the appropriate configured to-do list while checking for duplicates.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../claudeblattman/">claudeblattman (Chris Blattman)</a></div><div><b>Category:</b> <code>infra</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-11-18</div></div><div style="margin-top:0.5em;"><b>Stages:</b> —</div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/chrisblattman/claudeblattman/contents/skills/todo-add/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/claudeblattman/todo-add/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/chrisblattman/claudeblattman/blob/main/skills/todo-add/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/chrisblattman/claudeblattman?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Add To-Do Item
*v1.1 — Adapted for public use*

Add a new to-do item to the correct list with duplicate checking.

### Instructions

#### 1. Get the item details

If not provided by the user, ask:
- What's the task? (brief description)
- Any additional context?

#### 2. Determine the correct list

Based on the item content, suggest the appropriate list using the routing table below. This table is an example — customize it to match your own lists and keywords.

| Keywords/Topics | Suggested List |
|----------------|----------------|
| config, settings, infrastructure, setup, tools | **Main** |
| email, calendar, briefing, scheduling | **Work** |

Present your suggestion:
```
This sounds like a [Main/Work] item because [reason].

Suggested list: ~/Documents/todo.md
Priority: [High/Medium/Low]

Is this correct, or should it go elsewhere?
```

#### 3. Check for duplicates

Read the target TODO file and scan for similar items. Check for:
- Same keywords in item titles
- Related tasks that might overlap
- Items that could be expanded instead of duplicated

If potential duplicate found:
```
Potential duplicate detected:

Existing item: "[item title]"
Location: [file path], [priority level]

Options:
1. Add anyway (they're different enough)
2. Update the existing item instead
3. Cancel
```

#### 4. Add the item

Once confirmed, add to the appropriate section with this format:
```markdown
- [ ] **[Item title]**
  - [Context/details if provided]
```

Update the "Last updated" date in the file header.

#### 5. Confirm

```
Added to [list name]:
  - [ ] **[Item title]**

Priority: [High/Medium/Low]
```

### File Locations

- **Main:** `~/Documents/todo.md`

Add more lists by creating additional todo files and adding them here. For example:
- **Work:** `~/Documents/todo-work.md`
- **Personal:** `~/Documents/todo-personal.md`

### Priority Definitions

| Priority | When to use |
|----------|-------------|
| **High** | Blocking progress, causing problems, or time-sensitive |
| **Medium** | Would improve things but not blocking |
| **Low** | Nice to have, someday |

### Notes

- If the user specifies a list directly, skip the routing suggestion
- If the user specifies priority, use it; otherwise suggest based on urgency cues

---

### Customization Points

**To set up this skill for your workflow:**

1. **File locations**: Edit the "File Locations" section to point to your actual todo files. You can use any number of lists — one file per list works well.

2. **Keyword routing table**: Edit the table in Step 2 to reflect your own categories. For example, if you have a "Research" list, add a row like `| papers, data, analysis, literature | **Research** |`.

3. **Priority mapping**: If your todo files use different section names (e.g., "Active" / "Up Next" / "Someday" instead of "High" / "Medium" / "Low"), add a mapping note. For example:
   ```
   High → Active
   Medium → Up Next
   Low → Someday
   ```

4. **Single vs. multi-list**: If you only use one todo file, you can simplify this skill by removing the routing logic in Step 2 entirely and hardcoding the single file path.

5. **Item format**: The default format uses `- [ ] **Title**` with indented context. Adjust to match your existing todo file format (e.g., plain `- [ ] Title` or numbered lists).
