<!-- DO NOT EDIT — auto-generated from projects/landscape/econtools.yml by scripts/build_indexes.py -->

# EconTools

`external` · status: `active` · focus: `review` · discipline: `economics` · started: 2026

**Project page:** <https://github.com/johanfourieza/econtools>

**Licence:** `MIT`

**Source:** [`projects/landscape/econtools.yml`](https://github.com/bhanneke/RISE/blob/main/projects/landscape/econtools.yml)

## Positioning

A personal Claude Code skill pack for economic-history and economics research workflows: simulated peer review with named referee personas (Diebolt), Economic History Review journal house-style automation (EHRstyle), a research-idea sounding board modelled on a real doctoral mentor (Janluiten), a dual-model adversarial reference auditor (Kris), a LaTeX-Word round-trip for language editing (Tanniedi), and a PDF-to-markdown literature converter (Tyler). Spans ideation, literature processing, revision, referee-simulation, and dissemination.

## Distinctive contribution

Two skills stand out versus other cataloged economics skill packs: Kris runs Claude and Codex (GPT-5.4) as two genuinely independent verification methods over a .bib file, randomly pairs references across models so no fixed Claude/Codex pair reviews the same batch, and stages an adversarial challenge round before flagging a reference as fake; EHRstyle encodes an entire journal's submission house style (Economic History Review, Feb 2026 Notes for Contributors) down to a bespoke biblatex style file. Diebolt's referee panel is explicit about its inspiration and gives public credit to two upstream projects (PHY041/claude-skill-citation-checker and Imbad0202/academic-research-skills).

## Evaluation scores

| Dimension | Score (0–3) | Note |
|---|:---:|---|
| Lifecycle coverage | 2 | Five distinct stages (idea sounding board, literature conversion, dissemination formatting, citation/language revision, referee simulation) but no data-analysis, formal-modeling, or paper-drafting-from-scratch skill. |
| Autonomy level | 1 | Copilot pattern throughout: Diebolt's editor briefing requires the user to choose which changes to implement; Kris produces a scorecard for human sign-off rather than auto-editing the bibliography. |
| Architectural transparency | 3 | All skills are public Markdown with full prompt text; Kris additionally ships 8 open Python helper scripts and a labelled test fixture. |
| Inputs supported | 2 | Multiple input forms (LaTeX manuscript, .bib file, PDF folder, free-text research idea) plus literature-API access (CrossRef/OpenAlex/Semantic Scholar/arXiv and more for Kris); no private data-source access. |
| Outputs / reproducibility | 2 | Persists revised manuscripts, bibliographies, review logs (review_log.json), and a markdown literature wiki; no unified cross-skill artifact manifest. |
| Internal evaluation | 1 | Only Kris ships a labelled test fixture (10 references with known REAL/FAKE/CHIMERIC cases); the other five skills have no reported evaluation. |
| Openness | 2 | MIT license; skills are plain Markdown/Python but require per-user placeholder substitution (paths, Codex availability, Zotero setup) before they run out of the box. |
| Maturity / traction | 1 | 37 stars, 9 forks, single maintainer; active (69 commits) but pre-1.0 personal tool. |
| Cross-family policy | 1 | Diebolt and Kris both add a second model family (Codex/GPT-5.4) when available, but it is explicitly conditional ('if Codex is available') rather than required or the sole default path. |
| Runtime assurance | 2 | Kris runs two non-overlapping verification methods plus an adversarial challenge round before a reference is flagged fake; Diebolt enforces information barriers between isolated referees. |
| Cross-platform portability | 1 | Primary runtime is Claude Code, with Codex CLI as an optional second backend for two skills; no other IDEs or providers documented. |

*Scored on 2026-10-01. See the [evaluation rubric](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).*

## Tags

**Pipeline stages:** `rq-formulation` `literature-synthesis` `revision-editing` `referee-simulation` `dissemination`


**Architectural features:** `multi-agent` `debate-consensus` `tool-use`


**Inputs:** `paper-draft` `bibtex-file` `pdf-folder` `research-idea`


**Outputs:** `review-report` `revised-bibliography` `formatted-manuscript` `markdown-literature-wiki`


**Knowledge sources:** `crossref` `openalex` `semantic-scholar` `arxiv` `orcid` `retraction-watch` `internet-archive` `openlibrary`


## Limitations

- Single-maintainer personal project; heavy per-user placeholder setup (paths, Codex availability, Zotero/BibTeX pipeline).
- EHRstyle is hard-coded to one journal's house style (Economic History Review) and not generalizable without rewriting the style files.
- Only one of six skills (Kris) has any labelled evaluation; the rest are undemonstrated beyond README description.
- Low external traction (37 stars) relative to the sophistication of the Kris verification design.

## Related projects in this catalog

- [`ai-peer-review-skill`](ai-peer-review-skill.md)
- [`academic-research-skills`](academic-research-skills.md)
- [`aris`](aris.md)
- [`econ-skills`](econ-skills.md)
