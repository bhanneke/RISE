# The data layer

The data layer supplies the empirical material a RISE pipeline
operates on. In the diagram it enters from the left; in practice it
is often the dimension along which RISE systems differ most sharply,
because access to good data is the binding constraint on what a
pipeline can produce.

## Source typology

Three orthogonal axes:

| Axis | Values |
|---|---|
| **Curation** | raw ↔ curated (peer-reviewed, harmonized, version-tracked) |
| **Provenance** | primary (collected/measured) ↔ derived (computed from other data) |
| **Access** | public ↔ proprietary ↔ controlled (IRB, DUA-gated) |

A RISE system's reach is bounded by which combinations it can
access. Most catalog projects can read public + curated data
(arXiv, OpenAlex); fewer can ingest raw private corpora, and almost
none can negotiate controlled-access pipelines.

## Catalog patterns

- **Domain-corpus consumers** — [`paper-qa`](../projects/paper-qa.md),
  [`open-scholar`](../projects/open-scholar.md): the data layer is
  predominantly *scientific text* (PDFs, abstracts).
- **Market and macro consumers** — [`e2er`](../projects/e2er.md):
  the data layer is *empirical time series* (FRED, yfinance,
  Hyperliquid).
- **Replication consumers** —
  [`social-science-replicability`](../projects/social-science-replicability.md):
  the data layer is *the target paper's data*, often constrained by
  what the original authors released.
- **Domain-specific (biology)** — [`robin`](../projects/robin.md):
  the data layer is gated behind FutureHouse's Edison platform.
- **No data layer** —
  [`zeropaper`](../projects/zeropaper.md),
  [`refine-ink`](../projects/refine-ink.md): these are
  drafting/revision tools whose inputs are textual rather than
  empirical.

## Access patterns

- **Direct API.** Cleanest case (FRED, Semantic Scholar, OpenAlex,
  arXiv). RISE systems typically wrap these in standard adapters.
- **Sandboxed fetching.** When the system must traverse the web at
  large, isolation (containers, SSRF protection, allowlists) is a
  hard requirement to avoid prompt-injection from fetched content.
  This is engineering territory; few catalog projects document it
  thoroughly.
- **Bulk download + index.** PaperQA2's approach: pre-fetch the
  corpus, index it, query it offline.
- **Brokered access.** Edison-style commercial gates (Robin) trade
  reproducibility for capability.

## Provenance and citability

For a RISE artifact to be scholarly, its data must be *citable*. In
practice this means:

- Persistent identifiers (DOI, accession number) for each dataset
  consumed.
- Versioning at the dataset level (the analysis was run against v2,
  not v3).
- Dataset cards or equivalent documentation accompanying each
  source.
- A manifest in the output that lists data sources with versions
  and access timestamps.

Most catalog projects implement *some* of this; few implement all
of it. Field-level evaluation that compares RISE-produced
manifests against journal data-availability standards is an open
empirical opportunity.

## Sandboxing concerns

Two recurring failure modes:

1. **Prompt injection** from fetched content — a third-party page
   instructs the agent to do something other than what its user
   asked. Mitigation: wrap untrusted content in boundary tags,
   strip control characters, run the consuming step with reduced
   tool permissions.
2. **Data exfiltration** — an agent with access to private data
   posts a quote of it into a public endpoint. Mitigation: separate
   the data-reading agent from the publish-capable agent;
   container-level egress filtering.

A RISE system that handles non-trivial data should treat these as
first-order concerns, not afterthoughts.

## Catalogs and discovery

A pipeline that can ideate but cannot *find data appropriate to its
idea* is bottlenecked. Few catalog projects address this directly;
those that do (e.g., [`e2er`](../projects/e2er.md) via its
research-API integration) rely on pre-built catalogs of available
datasets rather than open-ended discovery. Open-ended dataset
discovery is one of the under-developed capabilities in current
RISE systems.
