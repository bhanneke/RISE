---
citekey: neurips2024checklist
title: 'Usefulness of LLMs as an Author Checklist Assistant for Scientific Papers:
  NeurIPS''24 Experiment'
authors:
- Goldberg, A.
- Ullah, I.
- Khuong, T. G. H.
- Rachmat, B. K.
- Xu, Z.
- Guyon, I.
- Shah, N. B.
year: 2024
venue: arXiv 2411.03417 (NeurIPS 2024 experiment report)
doi: ''
url: https://arxiv.org/abs/2411.03417
kind: paper
themes:
- peer-review
- ai-publishing-ecosystems
- evaluation-rigor
methods:
- field-experiment
- survey
relates_to_projects: []
status: read
arxiv_id: '2411.03417'
---

## Summary

A field experiment run at NeurIPS 2024 in which 234 voluntarily-submitted
papers were vetted by an LLM-based *Checklist Assistant* against the
conference's 15-question author checklist (reproducibility, ethics,
transparency, etc.). Authors received the LLM's feedback privately —
reviewers did not see it. The study combines pre/post-usage surveys
(539 / 78 responses), analysis of LLM feedback content, and a small
re-submission analysis (40 authors who submitted twice).

## Contribution

The first published, deployed conference-scale evaluation of an LLM as
an *author-facing* compliance aid (as opposed to a reviewer or
decision aid). Three main findings: (1) >70% of post-usage respondents
found the assistant useful and intended to revise based on its
feedback; (2) qualitative evidence that some authors made substantive
revisions to submissions because of LLM feedback (though no causal
identification); (3) the assistant could be **gamed** — fabricated
justifications elicited higher compliance scores, exposing a real
vulnerability of automated review tools.

## Method

Pre/post-usage surveys plus content analysis of LLM feedback;
re-submission comparisons for the 40 authors who submitted twice;
a small adversarial experiment to probe gameability of the assistant
via fabricated justifications.

## Relevance to RISE

A canonical example of using LLMs in the *peer-review pipeline* —
specifically at the author-side checklist step, rather than the
reviewer side. Directly relevant to the evaluation-rigor and
peer-review threads in the RISE catalog. Pairs naturally with
[gartenberg2026morebetter](gartenberg2026morebetter.md),
[naddaf2025aipeer](naddaf2025aipeer.md), and
[latona2024reviewlottery](latona2024reviewlottery.md) on the broader
peer-review-with-AI literature, but is one of the few that reports
*actual deployment* data rather than survey-only or observational
findings. The gameability finding is also a concrete example of the
"plausible unsupported success" failure mode that [yang2026aris](yang2026aris.md)
formalises as the central problem in long-horizon agentic workflows.

## Critique / open questions

The 234 submissions were self-selected — authors who opted in are
likely systematically different from those who did not, limiting
generalisability of the satisfaction numbers. Causal attribution to
the assistant is not identified ("qualitative evidence" rather than
estimated effects). The post-usage survey response rate (78/234, ~33%)
is modest. The gameability result is small-sample but the failure mode
itself is the more important takeaway than the magnitude.

## Key quotes

> "We conduct an experiment at the 2024 Neural Information Processing
> Systems (NeurIPS) conference, where 234 papers were voluntarily
> submitted to an 'LLM-based Checklist Assistant.'"

> "In post-usage surveys, over 70% of authors found the assistant
> useful, and 70% indicate that they would revise their papers or
> checklist responses based on its feedback."

> "We also conduct experiments to understand potential gaming of the
> system, which reveal that the assistant could be manipulated to
> enhance scores through fabricated justifications, highlighting
> potential vulnerabilities of automated review tools."
