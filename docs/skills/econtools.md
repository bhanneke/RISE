<!-- DO NOT EDIT — auto-generated from skills/econtools.yml by scripts/build_skills_index.py -->

# EconTools

license: `MIT` · 6 skills · last update: 2026-09

**Source:** <https://github.com/johanfourieza/econtools>

**Maintainers:** Johan Fourie (Stellenbosch University, Economic History)

**Related project entry:** [`econtools`](../projects/econtools.md)

**Compatibility:** `claude-code` `codex`

> Six personal Claude Code skills for economic-history and economics research, each named after a real person who shaped the author's career (Claude Diebolt, Jan Luiten van Zanden, Kris Inwood, Di Kilpert, Tyler Cowen). Diebolt and Kris both optionally recruit Codex (GPT-5.4) as a second, independent model family. Kris explicitly credits two upstream projects (PHY041/claude-skill-citation-checker and Imbad0202/academic-research-skills, the latter already in this catalog) for parts of its design.


**Source YAML:** [`skills/econtools.yml`](https://github.com/bhanneke/RISE/blob/main/skills/econtools.yml)

## Skills

### `audit` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/kris`](econtools/kris.md) | economics | `revision-editing` | Catches hallucinated and chimeric .bib entries by running Claude and Codex (GPT-5.4) as two genuinely independent verification methods (API-cascade cross-checking vs. DOI/landing-page/Retraction-Watch/ORCID/Internet-Archive checks), randomly assigning references so no fixed pair shares a batch, then staging an adversarial challenge round on disagreements before producing an evidence-backed scorecard. | [view](econtools/kris.md) | [origin](https://github.com/johanfourieza/econtools/blob/main/kris/skill.md) | 2026-09 |

### `editing` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/tanniedi`](econtools/tanniedi.md) | economics | `revision-editing` | Round-trips a LaTeX paper to Word for human copy-editing (pack) and applies the editor's tracked changes back into the original .tex files (unpack), preserving LaTeX formatting, equations, and cross-references. | [view](econtools/tanniedi.md) | [origin](https://github.com/johanfourieza/econtools/blob/main/tanniedi/skill.md) | 2026-09 |

### `ideation` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/janluiten`](econtools/janluiten.md) | economics | `rq-formulation` | A research-idea sounding board modelled on a real doctoral mentor; listens first, then stress-tests the idea against the long view of research-program cycles, cultural-evolution pressures on field prestige, and behavioural misreading of one's own motives, to help decide what to work on, with whom, and why. | [view](econtools/janluiten.md) | [origin](https://github.com/johanfourieza/econtools/blob/main/janluiten/skill.md) | 2026-09 |

### `literature` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/tyler`](econtools/tyler.md) | economics | `literature-synthesis` | Converts a folder of academic PDFs into a token-efficient markdown wiki (one .md per paper plus a summary.txt index) so Claude Code can read literature cheaply without re-parsing raw PDFs each time. | [view](econtools/tyler.md) | [origin](https://github.com/johanfourieza/econtools/blob/main/tyler/SKILL.md) | 2026-09 |

### `review` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/diebolt`](econtools/diebolt.md) | economics | `referee-simulation` | Simulated peer review for economics working papers — a panel of independent referee agents, each with a distinct subspecialisation, personality and fictitious affiliation, reviewing in isolation under strict information barriers; an editor synthesises a prioritised briefing, and accepted revisions are applied to the LaTeX source. Adds a second-model-family (Codex/GPT-5.4) audit when available. | [view](econtools/diebolt.md) | [origin](https://github.com/johanfourieza/econtools/blob/main/diebolt/skill.md) | 2026-09 |

### `submission` (1)

| Skill | Field | Stages | Description | Full text | Source | Updated |
|---|---|---|---|---|---|---|
| [`/ehrstyle`](econtools/ehrstyle.md) | economics | `dissemination` | Applies the Economic History Review house style (Feb 2026 Notes for Contributors) to a LaTeX manuscript, bibliography, title page, and cover letter, with a bespoke biblatex style (echr.bbx/echr.cbx) for EHR-specific footnote and bibliography conventions. | [view](econtools/ehrstyle.md) | [origin](https://github.com/johanfourieza/econtools/blob/main/ehrstyle/SKILL.md) | 2026-09 |
