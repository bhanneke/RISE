---
citekey: maynez2020faithfulness
title: On Faithfulness and Factuality in Abstractive Summarization
authors:
- Maynez, J.
- Narayan, S.
- Bohnet, B.
- McDonald, R.
year: 2020
venue: Proceedings of ACL 2020
doi: ''
url: ''
kind: paper
themes:
- hallucination
- reasoning-faithfulness
- evaluation-of-ai-research
methods:
- empirical
- human-evaluation
relates_to_projects:
- storm
- autosurvey
- surveyx
- paper-qa
status: read
---

## Summary

A 2020 ACL paper that conducts a large-scale human evaluation of
hallucinated content in neural abstractive summarisation systems on
the eXtreme Summarization (XSum) task. The authors compare RNN, CNN,
Transformer and pretrained-LM summarisers as well as human-written
summaries, asking how frequently each hallucinates and what kinds of
hallucinations they produce. They also evaluate whether automatic
metrics correlate with the human faithfulness judgements.

## Contribution

Two pieces. (1) A documented finding that "human annotators found
substantial amounts of hallucinated content in all model generated
summaries," but that pretrained models are better summarisers — not
only by ROUGE but also by human-judged faithfulness and factuality.
(2) A methodological finding: textual-entailment-based measures
correlate with faithfulness better than standard ROUGE-style metrics,
pointing toward better automatic evaluation, training and decoding
criteria.

## Method

Large-scale human evaluation on XSum across multiple model families
(RNN, CNN, Transformer, pretrained), plus correlation analysis of
candidate automatic metrics against human faithfulness judgements.
Annotations released publicly.

## Relevance to RISE

A foundational pre-LLM reference on hallucination in
text-generation that anchors the *hallucination* and
*reasoning-faithfulness* themes for RISE. Catalog projects that
synthesise or summarise sources at scale —
[`storm`](../../projects/storm.md),
[`autosurvey`](../../projects/autosurvey.md),
[`surveyx`](../../projects/surveyx.md),
[`paper-qa`](../../projects/paper-qa.md) — inherit exactly the
intrinsic/extrinsic hallucination failure modes this paper documents,
and the entailment-as-evaluation finding directly informs how their
output should be measured.

## Critique / open questions

Conducted on XSum, an extreme-summarisation benchmark not
representative of research-paper-length generation; pre-LLM era, so
quantitative numbers do not directly transfer to current models.
Faithfulness is defined relative to a single source document, not to
multi-source synthesis as in RISE pipelines.

## Key quotes

> "These models are highly prone to hallucinate content that is
> unfaithful to the input document."

> "Textual entailment measures better correlate with faithfulness
> than standard metrics, potentially leading the way to automatic
> evaluation metrics as well as training and decoding criteria."
