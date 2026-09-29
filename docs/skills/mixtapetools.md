<!-- DO NOT EDIT — auto-generated from skills/mixtapetools.yml by scripts/build_skills_index.py -->

# MixtapeTools (Scott Cunningham)

license: `informal permission in README ("Use freely. Attribution appreciated but not required."); no licence file` · 10 skills · last update: 2026-08-26

**Source:** <https://github.com/scunning1975/MixtapeTools>

**Maintainers:** Scott Cunningham (scunning1975 on GitHub; Baylor University)

**Compatibility:** `claude-code`

> The Claude Code toolkit of the author of Causal Inference: The Mixtape, and the most-cited economist skill repository in Velikov's AI-in-economics wiki (464 stars). Ten skills cover the empirical-economics workflow around a project rather than the estimation itself: an adversarial second referee for decks and for cross-language code replication, a many-agent bibliography audit that checks each citation's DOI and fields, a "blindspot" audit for problems and missed opportunities in empirical output, Beamer deck design and compilation built on the author's Rhetoric of Decks, figure-collision checks, careful chunked reading of PDFs, project and book scaffolding, and a warrant-first research task system. The repository has no licence file; its README grants informal permission to use the material freely. Because that permission does not spell out redistribution terms, RISE links to each skill rather than reproducing it.


**Source YAML:** [`skills/mixtapetools.yml`](https://github.com/bhanneke/RISE/blob/main/skills/mixtapetools.yml)

## Skills

### `audit` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`bibcheck`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/bibcheck/SKILL.md){ target=_blank rel=noopener } | — |  | Audits a .bib file by giving each citation to its own narrowly scoped agent, which confirms the DOI or URL and checks that every field belongs to the same paper, catching mismatched or invented references. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/bibcheck/SKILL.md) | 2026-08 |

### `figures` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`tikz`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/tikz/SKILL.md){ target=_blank rel=noopener } | — |  | A quick collision check for figures, whether TikZ inside LaTeX or rendered images from R or Python, looking for overlapping labels and similar layout faults. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/tikz/SKILL.md) | 2026-08 |

### `ideation` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`gtd`](https://github.com/scunning1975/MixtapeTools/blob/main/gtd/SKILL.md){ target=_blank rel=noopener } | — |  | A research task-management system for causal-inference work that organises hypotheses, insights and decisions in separate folders and asks the researcher to state the warrant for each conjecture. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/gtd/SKILL.md) | 2026-08 |

### `infra` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`newbook`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/newbook/SKILL.md){ target=_blank rel=noopener } | — |  | Scaffolds a book project: folder layout, a memoir-class LaTeX skeleton with a custom style, bibliography stub, CLAUDE.md, README and one file per chapter. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/newbook/SKILL.md) | 2026-08 |
| [`newproject`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/newproject/SKILL.md){ target=_blank rel=noopener } | — |  | Scaffolds a new research project with a standard directory layout, a CLAUDE.md template and a documented README. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/newproject/SKILL.md) | 2026-08 |

### `literature` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`split-pdf`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/split-pdf/SKILL.md){ target=_blank rel=noopener } | — |  | Downloads an academic PDF, splits it into short chunks and reads them in small batches, so that long papers are read closely rather than skimmed before a review or summary. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/split-pdf/SKILL.md) | 2026-08 |

### `review` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`blindspot`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/blindspot/SKILL.md){ target=_blank rel=noopener } | — |  | Reviews empirical output for what its author is too close to see, listing both problems hidden in plain sight and overlooked opportunities in the results. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/blindspot/SKILL.md) | 2026-08 |
| [`referee2`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/referee2/SKILL.md){ target=_blank rel=noopener } | — |  | An adversarial second-referee audit in two modes: reviewing a slide deck for rhetoric, visual quality and clean compilation, or re-implementing a paper's code in another language to check that the results replicate. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/referee2/SKILL.md) | 2026-08 |

### `slides` (2)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`beautiful_deck`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/beautiful_deck/SKILL.md){ target=_blank rel=noopener } | — |  | Builds a Beamer presentation end to end, designing a theme for the intended audience and restructuring existing material around the author's Rhetoric of Decks. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/beautiful_deck/SKILL.md) | 2026-08 |
| [`compiledeck`](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/compiledeck/SKILL.md){ target=_blank rel=noopener } | — |  | Creates and compiles Beamer slide decks following the Rhetoric of Decks conventions; the lighter-weight companion to beautiful_deck. | — | [origin](https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/compiledeck/SKILL.md) | 2026-08 |
