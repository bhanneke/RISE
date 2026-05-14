# RISE — Research Information Systems Engineering

> A public knowledge base introducing **Research Information Systems
> Engineering**: the design and study of information systems that
> *produce* scholarly knowledge, with a focus on agentic research
> pipelines.

**Site:** https://bhanneke.github.io/RISE/ (deployed via GitHub Pages)
**License:** [CC-BY-4.0](LICENSE)
**Citation:** see [`CITATION.cff`](CITATION.cff)

---

## What is RISE?

RISE names a discipline at the intersection of information systems,
research infrastructure, AI/agentic workflows, and open science. A
RISE system takes a research *input* (an idea, an open question, a
replication target), combines it with *data* and prior *knowledge*,
and produces durable *outputs* (artifacts, papers, replication
packages, datasets).

```
                  ┌─────────────────────────┐
                  │   INPUTS                │
                  │   • human idea          │
                  │   • agentic idea        │
                  │   • research question   │
                  │   • replication target  │
                  └───────────┬─────────────┘
                              │
        ┌─────────┐           ▼           ┌──────────────┐
        │  DATA   │──►  KNOWLEDGE        ◄──│ KNOWLEDGE   │
        │ (raw,   │     PRODUCTION         │ (literature, │
        │ macro,  │  ──────────────────    │  prior work, │
        │ crypto, │  Agentic Research      │  theory,     │
        │ admin,  │     Pipelines          │  methods)    │
        │  …)     │  ──────────────────    │              │
        └─────────┘           │            └──────────────┘
                              ▼
                  ┌─────────────────────────┐
                  │   OUTPUTS               │
                  │   • artifacts (code,    │
                  │     figures, tables)    │
                  │   • papers / preprints  │
                  │   • datasets            │
                  │   • replication reports │
                  └─────────────────────────┘
```

## What's in this repo?

Two curated catalogs and a documentation site that exposes them.

| Path | Contents |
|------|----------|
| `docs/` | The MkDocs site (concept, projects, papers, glossary) |
| `papers/references.bib` | BibTeX database of academic references |
| `papers/notes/` | One structured markdown note per paper |
| `papers/schema.md` | Front-matter schema for paper notes |
| `projects/e2er.yml` | Owned project entry (E2ER) |
| `projects/landscape/` | External agentic-research projects (Sakana AI Scientist, zeropaper, APE, …) |
| `projects/EVALUATION.md` | Standard evaluation rubric used to score every project |
| `projects/VOCABULARY.md` | Controlled vocabularies (themes, pipeline stages, architectural features) |
| `scripts/build_indexes.py` | Regenerates `docs/papers/index.md` and `docs/projects/index.md` from sources |

## How to read it

- New to the topic? Start with [`docs/index.md`](docs/index.md) and
  [`docs/concept/definition.md`](docs/concept/definition.md).
- Looking for a specific paper? Browse `papers/notes/` or the
  generated index at `docs/papers/index.md`.
- Comparing systems? See `projects/EVALUATION.md` for the rubric and
  the comparison matrix at `docs/projects/index.md`.

## How to contribute

See [`docs/contributing.md`](docs/contributing.md). New paper notes and
project entries are welcome via pull request; both must conform to the
schemas in `papers/schema.md` and `projects/schema.md`.
