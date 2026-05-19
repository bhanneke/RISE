# Skills KB — controlled vocabularies

Tag values used in `skills/*.yml` files. New tags require a proposal
(issue/PR) before being applied.

## Skill categories

A skill's headline focus. Pick the single best-fit tag.

| Tag | Meaning |
|---|---|
| `ideation` | Idea / hypothesis / RQ generation, gap-finding, brainstorming |
| `literature` | Search, retrieval, synthesis, gap analysis, citation discovery |
| `design` | Identification strategy, experiment design, pre-analysis plan |
| `data-handling` | Data discovery, acquisition, cleaning, schema-building |
| `analysis` | Estimation, modeling, simulation, statistical reporting |
| `modeling` | Formal / mathematical model derivation, proof construction |
| `code-gen` | Generating analysis or replication code |
| `drafting` | First-draft paper/section/abstract production |
| `editing` | Revision, polish, style, prose quality |
| `figures` | Figure planning, generation, rendering, spec |
| `slides` | Slide / talk / presentation pipelines |
| `review` | Referee simulation, internal review, quality checks |
| `revision` | Rebuttal, R&R response, addressing reviewer comments |
| `audit` | Claim-faithfulness, citation audit, math audit, novelty check |
| `replication` | Reproducing published results, replication packaging |
| `submission` | Journal targeting, formatting, submission packaging |
| `infra` | Memory, state, hooks, helpers, sub-skill orchestration |
| `meta` | Skill-about-skills (skill-creator, self-improvement, etc.) |

## Compatibility (agent runtimes)

Which agent runtime(s) a skill is designed for or known to work with.

| Tag | Meaning |
|---|---|
| `claude-code` | Anthropic Claude Code CLI / IDE plugins |
| `codex` | OpenAI Codex CLI |
| `cursor` | Cursor IDE |
| `gemini-cli` | Google Gemini CLI |
| `copilot-cli` | GitHub Copilot CLI |
| `kimi-cli` | Moonshot Kimi CLI |
| `openclaw` | OpenClaw CLI / agent layer |
| `trae` | ByteDance Trae IDE |
| `antigravity` | Google Antigravity IDE |
| `windsurf` | Codeium Windsurf IDE |
| `vscode` | VS Code (with appropriate extension) |
| `jetbrains` | JetBrains IDEs |
| `mcp` | Standalone MCP server (runtime-agnostic) |
| `agnostic` | Pure-Markdown SKILL.md usable by any LLM agent |

## How to extend

1. Propose new tag in an issue/PR.
2. Add it to this file with a one-line definition.
3. Apply to existing entries where it now fits.
4. Regenerate indexes: `python scripts/build_skills_index.py`.
