# Projects KB — entry schema

Every file in this directory (and `landscape/`) is a YAML document
conforming to the schema below. The build script
(`scripts/build_indexes.py`) validates the schema and renders the
comparison matrix.

## File naming

- Owned projects: `projects/<slug>.yml` (e.g., `e2er.yml`).
- External projects: `projects/landscape/<slug>.yml`.
- `<slug>` is lowercase, hyphen-separated, stable (treat as an
  identifier — other entries may reference it via `related:`).

## Full schema

```yaml
# ── Identity ─────────────────────────────────────────────────────
slug: string                      # filename stem; stable identifier
name: string                      # human-readable name
type: owned | external            # owned = this catalog's authors maintain it
status: active | dormant | archived | research-prototype
url: string                       # canonical project URL (repo or homepage)
maintainers: [string]             # optional
year_started: integer

# ── Positioning ──────────────────────────────────────────────────
positioning: |                    # 1–3 sentences; where it sits on the RISE diagram
  ...
distinctive_contribution: |       # 1–3 sentences; what it does that others don't
  ...

# ── What it does ─────────────────────────────────────────────────
focus: enum                       # from VOCABULARY.md → focus (one tag)
pipeline_stages: [enum]           # from VOCABULARY.md → pipeline stages
architectural_features: [enum]    # from VOCABULARY.md → architectural features
discipline: enum                  # from VOCABULARY.md → disciplinary scope
inputs: [string]                  # free-form: idea | rq | paper | dataset | …
outputs: [string]                 # free-form: paper | code | figures | review | …
data_sources: [string]            # named data sources it can access
knowledge_sources: [string]       # named knowledge sources (arxiv, openalex, …)

# ── Evaluation (per EVALUATION.md) ───────────────────────────────
scores:
  lifecycle_coverage:         {score: 0|1|2|3, note: "..."}
  autonomy_level:             {score: 0|1|2|3, note: "..."}
  architectural_transparency: {score: 0|1|2|3, note: "..."}
  inputs_supported:           {score: 0|1|2|3, note: "..."}
  outputs_reproducibility:    {score: 0|1|2|3, note: "..."}
  internal_evaluation:        {score: 0|1|2|3, note: "..."}
  openness:                   {score: 0|1|2|3, note: "..."}
  maturity_traction:          {score: 0|1|2|3, note: "..."}
scored_on: "YYYY-MM-DD"

# ── Narrative ────────────────────────────────────────────────────
limitations:                      # bullet list of strings
  - "..."
related: [slug]                   # other entries in this catalog
references: [citekey]             # citekeys from papers/references.bib
```

## Notes

- All enum tags MUST come from [`VOCABULARY.md`](VOCABULARY.md). New
  tags require updating VOCABULARY.md first.
- `references:` accepts only citekeys present in `papers/references.bib`.
  The build script flags unknown citekeys.
- `related:` accepts only slugs present in this catalog. The build
  script flags broken links.
- `scored_on` is required whenever `scores` is set. Re-scoring updates it.
