---
name: extract-section
description: Extract a section from main.tex by key name
user_invocable: true
---

# Extract Section Skill

Extract a specific section from `main.tex` for reading or editing.

## Examples
- `/extract-section introduction` -- extract the introduction
- `/extract-section data` -- extract the data section
- `/extract-section results` -- extract the results section
- `/extract-section internet-appendix` -- extract the full Internet Appendix

## Section Keys

Look up the project's section keys in its `CLAUDE.md` (under "LaTeX Section
Keys"). The boilerplate template ships with these default keys:

| Key | Section |
|-----|---------|
| `introduction` | Introduction |
| `data` | Data |
| `methodology` | Methodology |
| `results` | Results |
| `conclusion` | Conclusion |
| `appendix-a` | Appendix A |
| `internet-appendix` | Internet Appendix |

Projects may register additional keys in their `CLAUDE.md`.

## Workflow

1. Read `main.tex`
2. Find `%% BEGIN:<key>` and `%% END:<key>` markers
3. Extract all content between the markers (inclusive)
4. Return clean LaTeX with line numbers relative to main.tex

**Marker format**: Each section is delimited by `%% BEGIN:<key>` and `%% END:<key>` comment lines in `main.tex`. Use Grep to locate the markers, then Read to extract the content between them.

## Output

The raw LaTeX content of the requested section, with line numbers relative to main.tex.
