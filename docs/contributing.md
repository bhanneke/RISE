# Contributing

This knowledge base accepts two kinds of contributions:

1. **New paper notes** — markdown notes on academic references that
   relate to Research Information Systems Engineering.
2. **New project entries** — structured evaluations of agentic-research
   systems (open-source or commercial).

We also welcome corrections, prose improvements, and additions to the
controlled vocabularies.

## Adding a paper

1. Add the BibTeX entry to [`papers/references.bib`](https://github.com/bhanneke/RISE/blob/main/papers/references.bib).
2. Pick a citekey of the form `lastnameYEARword` (lowercase, no
   punctuation) — e.g., `wu2025agenticreasoning`.
3. Create `papers/notes/<citekey>.md` following the template in
   [`papers/schema.md`](https://github.com/bhanneke/RISE/blob/main/papers/schema.md).
4. Fill in the structured sections (summary, contribution, method,
   relevance to RISE, critique).
5. Tag with themes drawn from
   [`projects/VOCABULARY.md`](https://github.com/bhanneke/RISE/blob/main/projects/VOCABULARY.md).
6. Open a pull request.

## Adding a project

1. Copy `projects/landscape/sakana-ai-scientist.yml` as a template.
2. Fill in fields per
   [`projects/schema.md`](https://github.com/bhanneke/RISE/blob/main/projects/schema.md).
3. Score the project against the eight dimensions of
   [`projects/EVALUATION.md`](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).
   Provide a one-line justification per dimension.
4. Cross-reference papers (`references: [citekey1, citekey2]`).
5. Open a pull request.

## Style

- Tone: academic. Assume a research-literate reader.
- Cite when making non-obvious claims, using `[@citekey]` syntax in
  markdown body (rendered by the `mkdocs-bibtex` plugin).
- Prefer specificity over hedging.
- Do not edit auto-generated sections of `docs/projects/index.md` or
  `docs/papers/index.md` — edit the YAML/markdown sources instead.

## License of contributions

By contributing, you agree your contribution will be licensed under
[CC-BY-4.0](https://github.com/bhanneke/RISE/blob/main/LICENSE).
