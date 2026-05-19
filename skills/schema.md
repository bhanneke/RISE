# Skills KB — schema

Each file in this directory is a YAML document describing one **skill
pack** — a Markdown-defined skill library distributed by a research
project. Skill packs ship multiple skills; each pack file contains
pack-level metadata plus an array of individual skill entries.

## File naming

`skills/<pack-slug>.yml`. `<pack-slug>` matches the slug of the
corresponding entry in `projects/landscape/<pack-slug>.yml` whenever
the pack is published as part of a project in the catalog.

## Full schema

```yaml
# ── Pack-level metadata ──────────────────────────────────────────
pack:
  slug: string                    # filename stem
  name: string                    # human-readable pack name
  source_url: string              # repo or distribution URL
  maintainers: [string]
  license: string                 # e.g., "MIT", "Apache-2.0", "CC BY-NC 4.0", "none"
  total_skills: integer
  last_update: "YYYY-MM-DD"
  related_project: string         # slug from projects/landscape/ — leave empty if standalone
  compatibility: [string]         # agent runtimes; controlled vocab in VOCABULARY.md
  notes: string                   # optional 1-2 sentences

# ── Individual skills (list) ─────────────────────────────────────
skills:
  - slug: string                  # skill identifier (often the SKILL.md folder name)
    name: string                  # invocation form, e.g., "/research-pipeline" or "research-pipeline"
    category: enum                # single tag from VOCABULARY.md → skill categories
    pipeline_stages: [enum]       # RISE pipeline stages this skill serves (from projects/VOCABULARY.md)
    description: string           # 1-line summary
    source_path: string           # optional path under the repo, e.g., "skills/research-pipeline/SKILL.md"
```

## Notes

- A skill's `category` is the single best-fit headline tag; use
  `pipeline_stages` for multi-stage skills that serve more than one
  block of the RISE pipeline.
- All enum tags MUST come from
  [`skills/VOCABULARY.md`](VOCABULARY.md) (skill categories +
  compatibility) and
  [`projects/VOCABULARY.md`](../projects/VOCABULARY.md) (pipeline
  stages).
- The `related_project` cross-reference enables joining the skills
  catalog to the projects catalog — both ARIS the project and ARIS
  the skill pack become discoverable from either entry point.
