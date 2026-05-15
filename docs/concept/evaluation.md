# Evaluating RISE systems

How do we tell a good RISE system from a bad one? This is an open
methodological question, and the literature reviewed in this
knowledge base does not yet provide a settled answer.

This page is *not* the project-comparison rubric used to score
catalog entries — that rubric is at
[`projects/EVALUATION.md`](https://github.com/bhanneke/RISE/blob/main/projects/EVALUATION.md).
Rather, this page sketches the *broader methodological question* of
evaluating RISE systems as scholarly artifacts, of which the
catalog's rubric is one concrete operationalization.

## What is being evaluated?

A RISE system has at least three evaluable surfaces, and treatments
of "AI scientist" evaluation in the literature often blur them:

1. **The pipeline itself** — as an information system. Is it
   well-designed, modular, secure, reproducible, documented?
2. **The artifacts it produces** — papers, code, figures, reviews.
   Are they correct, novel, well-argued, methodologically sound?
3. **The research it enables** — counterfactual impact on the
   scholarly community. Does deploying the system shift what gets
   asked, what gets answered, what gets cited?

The catalog's rubric scores (1) directly (architectural
transparency, openness, reproducibility) and (2) indirectly (via
*internal_evaluation*). (3) — field-level effects — is currently
out of scope but is the subject of growing empirical attention
([@tonerrodgers2025genai], [@gartenberg2026morebetter]).

## Output-level evaluation

The classical evaluation surface: given a paper, code release, or
review produced by a RISE pipeline, *how good is it*?

Sub-dimensions that recur in the literature:

- **Faithfulness** — does the artifact's argument match what its
  cited evidence supports? See [@matton2025walkthetalk],
  [@maynez2020faithfulness].
- **Factual accuracy** — are the empirical claims correct? See the
  hallucination survey [@ji2023hallucination].
- **Citation grounding** — are cited references real, relevant, and
  correctly attributed? A core focus of
  [`paper-qa`](../projects/paper-qa.md) and
  [`open-scholar`](../projects/open-scholar.md).
- **Methodological soundness** — does the artifact respect the
  norms of its discipline (identification, pre-registration,
  ethical clearance)?
- **Novelty** — is the contribution incremental, derivative, or
  genuinely new? A notoriously hard target — see the *novelty*
  skill family across the catalog.
- **Peer-review readiness** — would the artifact survive review at
  a venue appropriate to its claims?

A persistent open problem: **the most reliable evaluator of these
properties remains a human expert**, which is exactly what RISE
systems aim to economize on. The catalog's review-focused projects
([`ape`](../projects/ape.md), [`reviewer`](../projects/reviewer.md),
[`marg`](../projects/marg.md)) attempt automated approximations;
their adequacy is itself a live empirical question.

## Process-level evaluation

Distinct from the artifact, the *process* that produced it can be
evaluated:

- **Determinism** — given the same inputs and model, does the
  pipeline produce the same output?
- **Auditability** — can intermediate artifacts (prompts,
  tool calls, decisions) be inspected post-hoc?
- **Reproducibility** — can a third party re-run the pipeline and
  recover the published artifacts?
- **Failure modes** — does the pipeline fail loudly (visible error)
  or silently (plausible-but-wrong output)? RISE systems exhibit a
  high prevalence of the latter — see [@chen2025reasoning] on
  reasoning faithfulness.

## Field-level evaluation

The most ambitious — and most under-developed — evaluation surface.
If RISE systems are deployed at scale, what are the field-level
consequences?

- **Composition shifts.** Does the kind of research that gets done
  change ([@cao2025aifinance], [@tonerrodgers2025genai])?
- **Quality-quantity tradeoffs.** Does more output mean lower
  marginal quality? [@gartenberg2026morebetter] develop this
  argument for peer review specifically; the parallel question for
  *publication* is open.
- **Discipline effects.** Does the IS or economics literature
  reorganize around what RISE makes cheap? Cf.
  [@gopal2025inventing], [@abbasi2026isr].
- **Epistemic trust.** How do readers and reviewers calibrate
  confidence in artifacts of unclear human/agentic provenance?
  Related: [@peter2025anthropomorphic],
  [@riemer2024styleengines].

## Benchmarks vs. case studies

A current methodological tension: **benchmark-driven evaluation**
(numerical scores on fixed tasks) is tractable and comparable
across systems but under-captures what matters for scholarship
(novelty, methodological soundness, peer-review readiness). **Case
studies** (a system deployed on a real research project)
demonstrate end-to-end fitness but resist generalization.

Two compromises are visible in the catalog:

- **Replication-task evaluations** — using the reproduction of a
  published paper as a stand-in for end-to-end fitness. The
  [`social-science-replicability`](../projects/social-science-replicability.md)
  project pursues this directly.
- **Environment-based evaluations** —
  [`aviary`](../projects/aviary.md) and similar provide
  standardized scientific-task environments that bridge benchmark
  comparability and task realism.

Neither is settled. A robust evaluation methodology for RISE remains
one of the field's open problems — and a natural locus for the
discipline's next contributions.
