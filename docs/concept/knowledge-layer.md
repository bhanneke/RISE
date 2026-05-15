# The knowledge layer

The knowledge layer supplies prior scholarship a RISE pipeline draws
on: the literature, prior artifacts, theories, and methodological
recipes that inform what the pipeline produces. In the diagram it
enters from the right; in practice it is often the dimension where
RISE projects differentiate most clearly from generic LLM
applications, because *grounded* scholarship requires explicit
literature integration.

## Sources

| Class | Examples |
|---|---|
| Open-access corpora | arXiv, bioRxiv, SSRN, OpenAlex, Semantic Scholar |
| Paywalled venues | JSTOR, Elsevier, INFORMS, ACM, IEEE |
| Institutional preprints | NBER, IZA, CEPR |
| Gray literature | Working papers, technical reports, blog essays |
| Reusable methodological resources | Method libraries, prompt collections, skill files |

Catalog projects vary in their reach. The literature-focused
projects ([`paper-qa`](../projects/paper-qa.md),
[`open-scholar`](../projects/open-scholar.md),
[`storm`](../projects/storm.md)) are designed around scientific
corpora; the drafting projects
([`refine-ink`](../projects/refine-ink.md),
[`coarse-ink`](../projects/coarse-ink.md)) typically have minimal
knowledge integration; end-to-end pipelines
([`e2er`](../projects/e2er.md),
[`agent-laboratory`](../projects/agent-laboratory.md)) mix
literature integration with method-skill libraries.

## Acquisition

PDF acquisition for non-OA papers is a recurring engineering
problem. A common pattern (see, e.g., the LitFetcher service in
adjacent infrastructure):

1. **Metadata enrichment** — given a DOI, title, or BibTeX entry,
   resolve to canonical metadata via CrossRef + OpenAlex.
2. **Waterfall fetching** — try arXiv → Unpaywall → Semantic Scholar
   → OpenAlex → CORE.
3. **OCR pipeline** — for scanned or image-heavy PDFs, fall back to
   pymupdf4llm, Tesseract, or PaddleOCR.
4. **Section-aware chunking** — preserve abstract / introduction /
   methods boundaries when embedding.
5. **Hallucinated-citation detection** — verify a cited paper
   actually exists and matches the claim being made.

Few RISE projects implement all five; doing so well is itself a
research-engineering contribution.

## Representation

A scholarly knowledge base is more than a flat vector index. The
representation choices that distinguish good RISE systems:

- **Citation graphs.** Edges between papers carry methodological
  signal that pure-text embeddings miss.
- **Section-aware embeddings.** A chunk from a *methods* section
  has different semantics than a chunk from a *literature review*.
- **Sibling-chunk context expansion.** When retrieving one chunk,
  also surface neighbors from the same document.
- **Retraction and version awareness.** A retracted paper
  resurfaced as a citation is a failure mode that
  [`paper-qa`](../projects/paper-qa.md) explicitly addresses.

## Retrieval patterns

- **Hybrid semantic + keyword search** — the workhorse pattern;
  vector similarity for breadth, keyword filters for precision.
- **Recall with citations** — return not just text but the
  source-of-record, so downstream agents can quote responsibly.
- **Deep vs. shallow context** — some pipelines build large
  literature contexts (~10K characters) for deep workers and
  compact contexts (~5K) for lighter steps.
- **Iterative retrieval** — the agent retrieves, reads, then
  retrieves again based on what it learned. STORM's
  perspective-guided question-asking is a canonical version.

## Knowledge hygiene

A pipeline that consumes the literature must also *maintain* its
view of the literature. Practical hygiene items:

- **De-duplication.** The same paper arrives via multiple sources
  (arXiv preprint + journal version + working paper).
- **Version tracking.** v1 of an arXiv paper may differ from v3 on
  the conclusion you cite.
- **Retraction awareness.** PubMed and Retraction Watch maintain
  feeds that should be consulted.
- **Citation-graph staleness.** A paper's citation count and its
  citing-paper set change continuously.

The catalog's evaluation rubric does not yet score knowledge hygiene
explicitly; this is a candidate dimension for a future rubric
version.

## Method libraries

Distinct from the *content* of the literature is its *methods*: how
do you actually run a difference-in-differences design, draft a
review, prepare a figure to journal specifications? Several
catalog projects ([`e2er`](../projects/e2er.md) most explicitly)
maintain libraries of reusable skill files — markdown documents
that instruct workers on methodological norms. These are part of
the knowledge layer too, even though they look like prompts
rather than papers.

## Trust calibration

A RISE pipeline that cites a paper makes an implicit claim: *I
have read this paper, and it supports my argument*. The literature
on faithfulness ([@matton2025walkthetalk],
[@maynez2020faithfulness]) and hallucination
([@ji2023hallucination]) is unanimous that this claim is often
false in current LLM systems. Treating the knowledge layer as a
trust-calibration problem — and instrumenting the pipeline to
report *how confident* it is that a citation supports a claim — is
an under-explored design move.
