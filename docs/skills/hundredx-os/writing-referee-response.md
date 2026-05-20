<!-- DO NOT EDIT — auto-copied from skills/hundredx-os/details/writing-referee-response.md -->

# `referee-response`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../hundredx-os/">100xOS shared skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> economics</div><div><b>License:</b> <code>private (curator-owned)</code></div><div><b>Updated:</b> 2026-05-20</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><p style="font-size:0.9em; color:#555;">Curator-private skill — copy text from <code>100xOS/shared/skills/writing/referee-response.md</code>.</p></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a></div></div>

## Writing Referee Responses

### Purpose and Tone

A referee response (also called a "response to reviewers" or "reply to referees") is a formal document submitted alongside a revised manuscript. Its purpose is to demonstrate that you have taken every concern seriously and addressed each one substantively. The tone should be professional, respectful, and direct -- never defensive, dismissive, or sarcastic, even when the referee is wrong.

A well-crafted response dramatically increases the probability of acceptance. A poor response -- even to a favorable report -- can derail a paper.

---

### Document Structure

#### Opening

Begin with a brief paragraph thanking the editor and referees:

```
We thank the editor and two anonymous referees for their careful reading
and constructive suggestions. The comments have significantly improved
the paper. Below we address each point in detail. For convenience, referee
comments are in italics, and our responses follow in regular text.
All page and line references correspond to the revised manuscript.
```

If you want to highlight the most significant changes upfront, add a short summary paragraph:

```
The main changes in this revision are: (1) we add an instrumental variables
specification to address the endogeneity concern raised by Referee 1
(new Table 5); (2) we extend the sample period by three years as suggested
by Referee 2 (all tables updated); and (3) we substantially rewrite
Section 4 to clarify the identification strategy.
```

#### Point-by-Point Responses

Address every point raised by every referee. Do not skip any comment, no matter how minor. Organize responses by referee.

---

### Response Format for Each Point

Use this structure for every individual comment:

**1. Quote the referee's concern.**
Reproduce the referee's words exactly, in italics or a block quote. If the comment is very long, quote the key sentences and note "[excerpt]." Never paraphrase in a way that softens or misrepresents the concern.

**2. Acknowledge the point.**
Begin your response by acknowledging the validity of the concern: "This is an excellent point," "We agree that this was unclear," "Thank you for raising this important issue." This is not sycophancy -- it signals that you took the comment seriously and understood it.

**3. Explain what you did.**
Describe the specific changes you made in response. Be concrete:
- "We have added a new subsection (Section 3.2, pp. 14--16) that discusses..."
- "We now include this robustness check in Table A3 (Appendix, p. 42)."
- "We have rewritten the third paragraph of the introduction (p. 2, lines 8--15) to clarify..."

**4. If you disagree, explain why respectfully.**
Sometimes a referee's suggestion would make the paper worse, or is based on a misunderstanding. In these cases:
- First acknowledge why the suggestion seems reasonable.
- Then explain your reasoning clearly and with evidence.
- Offer a compromise when possible: "While we believe the current approach is more appropriate because [reason], we have added a footnote (fn. 12, p. 18) discussing the alternative approach the referee suggests."
- Never write "the referee is mistaken" or "this comment reflects a misunderstanding." Instead: "We may not have been clear enough in the original draft. To clarify..."

**5. Provide page/line references.**
Always tell the referee exactly where to find the change. This saves the referee from having to search the entire manuscript. Use the format: "(p. 14, lines 3--8)" or "(see revised Table 3, column 4)" or "(new Appendix Section B.2)."

---

### Example Response

```
RESPONSE TO REFEREE 1

We thank Referee 1 for the thorough and insightful report. We address
each comment below.

---

Comment 1.1:

> "The identification strategy relies on the assumption that the policy
> change was not anticipated by firms. However, several news reports
> from early 2018 suggest that the reform was widely discussed before
> its announcement. The authors should address this threat."

We thank the referee for raising this important concern. We agree that
anticipation effects could bias our estimates if firms adjusted behavior
before the official announcement date.

We have addressed this in three ways:

First, we now discuss the legislative history in detail in the revised
Section 2 (pp. 8--9), documenting that while the reform was debated in
parliament, the specific provisions affecting our outcome variable were
added as amendments in the final week of deliberations, making precise
anticipation unlikely.

Second, we conduct an event-study analysis (new Figure 3, p. 23) that
shows no evidence of pre-trends in the four quarters before the
announcement. The point estimates for pre-announcement quarters are
small, statistically insignificant, and show no systematic pattern.

Third, we re-estimate our main specification dropping the six months
immediately surrounding the announcement (Table A5, Appendix p. 44).
Results are virtually unchanged (coefficient of 0.034 vs. 0.037 in
the baseline), suggesting that anticipation effects do not drive our
findings.

---

Comment 1.2:

> "Table 2 should include industry fixed effects."

We agree and have added industry fixed effects to all specifications
in Table 2. As the referee anticipated, the point estimates are
slightly smaller but remain statistically significant and economically
meaningful. See revised Table 2, columns 3--6 (p. 21).
```

---

### Common Scenarios and How to Handle Them

#### The referee asks for a fundamentally different paper.

Acknowledge the alternative approach as valid, but explain why your approach better serves the research question. Offer small concessions (a discussion, a robustness check) without abandoning your framework.

"We appreciate this thoughtful suggestion. We considered this approach early in the project but ultimately chose [current approach] because [specific reason]. We now discuss the tradeoffs between the two approaches in footnote 15 (p. 19). We also report the results using [referee's approach] in Appendix Table A7, which yields qualitatively similar findings."

#### The referee misunderstood something.

This is almost always your fault as a writer. Accept responsibility for the lack of clarity and fix it.

"We apologize for the lack of clarity on this point. The referee's reading is understandable given the original wording. We have substantially rewritten Section 4.1 (pp. 17--18) to make clear that [correct interpretation]. In particular, we now state explicitly on p. 17 that..."

#### The referee requests an analysis you cannot do.

Be transparent about why, and offer the best available alternative.

"Unfortunately, the data do not allow us to perform this analysis directly because [specific reason -- e.g., the variable is not available before 2010]. However, as a partial test, we [describe alternative analysis]. We also discuss this limitation explicitly in the conclusion (p. 32, lines 4--9)."

#### The referee is factually wrong.

Be gracious. Do not say "the referee is incorrect." Instead:

"We appreciate this comment. We believe there may be a misunderstanding that was likely caused by our original exposition. To clarify: [correct statement with citation or evidence]. We have revised the text on p. 12 to state this more precisely."

#### The referee wants you to cite specific papers.

Cite them. Even if the papers are only tangentially related, citing them costs nothing and shows good faith. If the referee is likely an author of those papers, be especially generous in your acknowledgment.

"Thank you for pointing us to these important references. We now cite and discuss Smith (2019) and Jones (2021) in the literature review (p. 5) and relate our identification strategy to theirs in Section 4 (p. 16)."

#### Multiple referees raise the same concern.

Address it fully under the first referee's comment, then cross-reference:

"[Under Referee 2, Comment 2.3]: Referee 1 raised a similar concern (Comment 1.1 above). As described in our response there, we have [summary of changes]. Please see pp. 8--9 and Figure 3 in the revised manuscript."

---

### Formatting Best Practices

- **Number all comments** (1.1, 1.2, ... for Referee 1; 2.1, 2.2, ... for Referee 2).
- **Use consistent visual formatting** to distinguish referee comments from your responses. Italics, block quotes, or a different font all work.
- **Bold or highlight new text** in the manuscript itself if the journal permits it (many do for the revision). This helps referees verify changes quickly.
- **Include a change log** at the end listing all modified pages/sections if the revision is extensive.
- **Keep responses concise but complete.** Do not pad with filler. A tight, well-organized response signals competence.

---

### Strategic Considerations

- **Respond promptly.** If the journal gives you 3 months, do not take 6 months unless genuinely necessary. Delayed responses signal disinterest.
- **The editor is your audience too.** The editor reads the response to decide whether you have adequately addressed concerns. Make it easy for the editor to say yes.
- **Err on the side of doing what referees ask.** Pick your battles carefully. Resist on methodological points that would genuinely weaken the paper. Comply on everything else.
- **Track changes or marked-up manuscripts** should accompany the response letter if the journal allows it.
- **If a revision introduces new analysis,** be upfront about it. Note that you added it in response to a concern, and flag any changes to the results.

---

### Checklist

- [ ] Every referee comment is quoted and addressed
- [ ] No comment is skipped or summarized away
- [ ] Tone is professional and non-defensive throughout
- [ ] All changes include page/line references to the revised manuscript
- [ ] Disagreements are supported with evidence or reasoning
- [ ] New tables/figures are referenced by number
- [ ] Cross-references used when multiple referees raise the same point
- [ ] Opening paragraph thanks editor and referees
- [ ] Summary of major changes included at the top
- [ ] Response is formatted consistently and easy to navigate
