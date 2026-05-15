# Papers KB — note schema

Each file in `docs/papers/notes/` is a markdown document with YAML
front-matter conforming to the schema below, plus a structured prose
body. The corresponding BibTeX entry must exist in
`papers/references.bib` under the same `citekey`.

## File naming

`docs/papers/notes/<citekey>.md` where `<citekey>` is the BibTeX key,
of the form `lastnameYEARword` (all lowercase, no punctuation).

Example: `wu2025agenticreasoning.md` ↔ `@inproceedings{wu2025agenticreasoning, ...}`.

(Paper notes live inside `docs/` so MkDocs can render them as part of
the site. The BibTeX file and this schema documentation stay in
`papers/`.)

## Front-matter schema

```yaml
---
citekey: string                # MUST match the .bib entry exactly
title: string
authors: [string]              # "Lastname, F."
year: integer
venue: string                  # journal, conference, or "preprint" / "blog"
doi: string                    # optional
url: string                    # optional; canonical link if no DOI
kind: paper | preprint | essay | survey | book-chapter | misc
themes: [enum]                 # from projects/VOCABULARY.md → themes
methods: [string]              # free-form: survey | benchmark | rct | case-study | …
relates_to_projects: [slug]    # slugs from projects/ catalog
status: queued | skimmed | read | re-reading
rating: 1|2|3|4|5              # optional, personal/curator rating
---
```

## Body sections

Use these headings, in this order. Any may be left empty for
`queued`/`skimmed` notes, but the headings should be present.

```markdown
## Summary

One paragraph (≤150 words). What the paper does, in plain prose.

## Contribution

What is genuinely new. Distinguish claimed contribution from actual.

## Method

Data, design, models, sample. Enough to assess the claims.

## Relevance to RISE

Why this paper belongs in this knowledge base. Which part(s) of the
RISE pipeline does it inform? Which projects does it relate to (cite
slugs)?

## Critique / open questions

Limitations the paper acknowledges + ones it doesn't.

## Key quotes

Verbatim quotes (with page numbers if available) for citation.
```

## Notes

- `themes:` MUST use tags from [`projects/VOCABULARY.md`](../projects/VOCABULARY.md).
- `relates_to_projects:` accepts only slugs present in the projects
  catalog. The build script flags unknown slugs.
- BibTeX entries without a corresponding note are allowed (used for
  citation only). Notes without a `.bib` entry are flagged as errors.
