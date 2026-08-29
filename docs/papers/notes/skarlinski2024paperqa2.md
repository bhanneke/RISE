---
citekey: skarlinski2024paperqa2
title: Language agents achieve superhuman synthesis of scientific knowledge
authors:
- Skarlinski, M. D.
- Cox, S.
- Laurent, J. M.
- Braza, J. D.
- Hinks, M.
- Hammerling, M. J.
- Ponnapati, M.
- Rodriques, S. G.
- White, A. D.
year: 2024
venue: arXiv preprint
doi: ''
url: https://arxiv.org/abs/2409.13740
kind: preprint
themes:
- hallucination
- agentic-tool-use
- evaluation-of-ai-research
methods:
- system-design
- expert-comparison
- benchmark-evaluation
relates_to_projects:
- paper-qa
status: skimmed
arxiv_id: '2409.13740'
---

## Summary

The PaperQA2 paper evaluates a language-model agent "optimized for
improved factuality" against subject-matter experts on three
literature tasks: information retrieval, summarization, and
contradiction detection. The authors develop a human–AI comparison
methodology in which humans are unrestricted (full internet, search
tools, time) and report that PaperQA2 matches or exceeds expert
performance on all three tasks. PaperQA2 writes cited,
Wikipedia-style summaries reported to be significantly more accurate
than existing human-written Wikipedia articles. The paper introduces
LitQA2, a hard literature-research benchmark that guided PaperQA2's
design. Applied to a random subset of biology papers, PaperQA2
identifies 2.34 +/- 1.99 contradictions per paper, of which 70% are
validated by human experts. The abstract concludes that language
agents can now exceed domain experts on meaningful literature tasks.

## Contribution

Claimed: superhuman performance on scientific-literature synthesis; a
rigorous human–AI comparison methodology; the LitQA2 benchmark; and
contradiction detection as a new application.

What the abstract supports: the comparison conditions are specified
(unrestricted humans, three tasks), but the only numbers given are
for contradiction detection (2.34 +/- 1.99 per paper, 70% validated).
The margins on retrieval and summarization, and the definition of
"accuracy" for the Wikipedia comparison, are not in the abstract. The
abstract itself states that LitQA2 "guided design of PaperQA2", so
the LitQA2 result is a co-developed benchmark rather than an
independent test. "Superhuman" is the paper's framing; the abstract
supports "matches or exceeds" on the tasks and comparators chosen.

## Method

Design: PaperQA2, a frontier language-model agent; the abstract does
not describe its architecture beyond "optimized for improved
factuality".

Evaluation: (1) human–AI comparison on retrieval, summarization, and
contradiction detection with unrestricted human experts; (2) accuracy
of cited Wikipedia-style summaries versus existing Wikipedia
articles; (3) LitQA2; (4) contradiction detection on a random subset
of biology papers with expert validation of flagged contradictions.

Not specified in the abstract: number of experts and papers, sample
sizes per task, LitQA2 size and construction, the underlying LLM,
how summary accuracy was scored, and how the 30% of contradictions
that were not validated are classified (false positives versus
unresolved).

## Relevance to RISE

Informs `literature-discovery` and `literature-synthesis`. Catalog
slug: `paper-qa`; the catalog's internal-evaluation and
runtime-assurance scores (both 3) are grounded in this paper's
claims. Contradiction detection is the most RISE-relevant task in
the abstract: a cross-document consistency check that feeds
gap identification in literature synthesis (whether it transfers to
`referee-simulation` is not tested in the abstract). Grounded
comparison: the OpenScholar abstract
([asai2024openscholar](asai2024openscholar.md)) reports a 7%
correctness advantage over PaperQA2 on ScholarQABench; this abstract
does not compare against OpenScholar.

Multi-agent structure / aggregation: the abstract describes PaperQA2
as a single "language model agent" and names no multi-agent, debate,
or consensus mechanism — worth noting because the catalog page tags
the project `multi-agent`, which the abstract neither supports nor
contradicts. The contradiction-detection task is nonetheless an
aggregation-quality probe in the curator's sense: it tests whether
an agent can reconcile claims across papers, though here as an
evaluation task rather than a generation mechanism, with expert
validation of 70% of flagged contradictions serving as the
consensus check.

## Critique / open questions

- The high dispersion (+/- 1.99 around a mean of 2.34) suggests
  contradiction counts vary widely across papers; the abstract does
  not say whether this reflects paper heterogeneity or detector
  noise.
- 30% of flagged contradictions were not expert-validated; the
  abstract does not distinguish false positives from disagreement
  among validators.
- The human comparator's expertise level, incentives, and time
  actually spent are not stated.
- The contradiction study is restricted to biology; transfer to
  fields with different evidentiary norms (including IS and social
  science) is untested per the abstract.
- The benchmark that shows PaperQA2 "exceeding human performance"
  was, by the abstract's own account, used to guide its design.
- The abstract concedes only the motivating problem (LLMs "are known
  to hallucinate"); it names no PaperQA2-specific limitations.

## Key quotes

> "We show that PaperQA2, a frontier language model agent optimized
> for improved factuality, matches or exceeds subject matter expert
> performance on three realistic literature research tasks without
> any restrictions on humans (i.e., full access to internet, search
> tools, and time)." (abstract)

> "We also introduce a hard benchmark for scientific literature
> research called LitQA2 that guided design of PaperQA2, leading to
> it exceeding human performance." (abstract)

> "PaperQA2 identifies 2.34 +/- 1.99 contradictions per paper in a
> random subset of biology papers, of which 70% are validated by
> human experts." (abstract)
