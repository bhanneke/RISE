---
name: read-paper
description: Read and analyze academic papers. Use when the user asks about a paper by citekey (e.g., "cardMinimumWagesEmployment1994"), author-year (e.g., "Card and Krueger 1994"), or pastes a PDF. Also invoke proactively when reading .md notes containing [@citekey] references where the paper content would help answer the current question.
argument-hint: <citekey | "Author et al Year" | pasted PDF> [question or intent]
---

# Read Paper

Analyze an academic paper and respond to the user's question or intent.

## Step 1: Parse Arguments

Arguments: $ARGUMENTS

Split into two parts:
- **paper_reference**: the paper identifier
- **intent**: everything after the identifier (optional — default to "full summary")

Detect input type:
- **Citekey**: a single camelCase word with a year at the end (e.g., `cardMinimumWagesEmployment1994`) → go to Step 2A
- **Author-year**: contains author name(s) + year, possibly a journal (e.g., `Card and Krueger 1994 AER`) → go to Step 2B
- **Pasted PDF**: a PDF file was provided in the conversation → go to Step 2C

## Step 2: Locate the Paper

### 2A: Citekey Lookup

1. Use Grep to search `<REFERENCES_BIB>` for the citekey. Read ~25 lines of context after the match to capture the full BibTeX entry.
2. Extract from the entry: `title`, `author`, `year`, `journal`, and the `file` field.
3. The `file` field may contain multiple paths separated by `;`. Split on `;`, filter for `.pdf` files, prefer the one whose filename contains the author's surname.
4. Verify the PDF exists at the extracted path.
5. If no `file` field or file not found → tell the user: "I found the bib entry for [title] but the PDF is not available locally. Can you help me locate the file?"
6. Pass the PDF path to Step 3.

### 2B: Author-Year Lookup

1. Use WebSearch: `"[author surname] [year] [journal if given] economics paper"`.
2. If multiple plausible matches → present top 3 candidates to the user using AskUserQuestion and wait for disambiguation.
3. Once identified, search `<REFERENCES_BIB>` by author surname + year.
4. If found in bib → follow 2A from step 2.
5. If not in bib → attempt WebFetch on a DOI URL or open-access version.
6. If cannot access → tell the user: "This paper is not in your Zotero library and I cannot access it online. Please download it and try again."

### 2C: Pasted PDF

The PDF is already in the conversation. Pass it directly to sub-agents in Step 3.

## Step 3: Read the Paper via Sub-Agents

**CRITICAL: The brain (main Claude) must NEVER read the PDF itself. All reading is delegated to sub-agents via the Task tool. This prevents context window overflow.**

### Phase 1: Single-Agent Attempt

Launch ONE sub-agent (Task tool, subagent_type: "general-purpose"):

> Read the PDF at [path] using the Read tool (it supports PDF files). Extract and return:
> 1. Research question
> 2. Methodology (structural model, RDD, DiD, GMM, etc.)
> 3. Main contribution (first paper to X, unifies Y with Z, etc.)
> 4. One-paragraph summary: what does the paper do, how, which methods, which data, theoretical vs empirical vs both, structural model?, model-consistent regression?, GMM?, counterfactual?
> 5. Key results and findings
> 6. Total number of pages
>
> Use the prompt templates from `references/subagent-prompts.md` — Template 1.

If the sub-agent returns a coherent, complete response → proceed to Phase 3.

If the sub-agent fails (context overflow, truncated output, incomplete) → proceed to Phase 2.

### Phase 2: Divide and Conquer

Launch multiple sub-agents in parallel, each reading a specific page range using the Read tool's `pages` parameter (max 20 pages per call):

- **Agent A** (pages 1-8): Abstract, Introduction, Literature Review. Extract: research question, positioning in literature, claimed contribution.
- **Agent B** (pages 8-20): Model / Methodology. Extract: model setup, key assumptions, estimation strategy, identification, data description.
- **Agent C** (pages 20-35): Results. Extract: main findings, robustness checks, extensions.
- **Agent D** (pages 35+): Conclusion and Appendices. Extract: summary, limitations, future work, technical highlights.

Adjust page ranges based on Agent A's report of the paper's structure and total length.

Use the prompt templates from `references/subagent-prompts.md` — Template 2 (A/B/C/D).

### Phase 3: Synthesis and Scrutiny

Assemble all sub-agent outputs into a unified understanding.

If the user asked a **specific question**:
1. Identify which section(s) likely contain the answer.
2. Send a NEW targeted sub-agent to re-read those specific pages with the question in mind. Use Template 3 from `references/subagent-prompts.md`.
3. Scrutinize the answer: "Does this fully answer the question? Are there unstated assumptions? Alternative interpretations?" If gaps remain, send a scrutiny agent (Template 4).
4. Require exact quotes with page numbers and section references.

## Step 4: Web Validation

After forming the analysis:

1. WebSearch: `"[author] [year] [short title] critique"` and `"[author] [year] [short title] review"`.
2. Check if the analysis aligns with external understanding (blog posts, review articles, author responses).
3. If discrepancies found → dispatch a new sub-agent to re-examine the specific section.
4. If discrepancy resolved → report consensus.
5. If not resolved → explicitly flag as contested and explain both sides. This is valuable — potential research gap.

## Step 5: Format Response

Use the appropriate template from `references/response-templates.md` based on the intent:

- No intent or "summary" → **Short Summary** template
- "full summary" or "detailed" → **Detailed Summary** template
- "methodology" → **Methodology Analysis** template
- Specific question → **Specific Question** template
- "relevance" → **Relevance Assessment** template

**Always include** regardless of template:
- Research question
- Methodology type
- Contribution
- One-paragraph summary

For specific questions, always include exact quotes: `"Card and Krueger explain in Section X that '...' (p. Y)"`

## Step 6: Proactive Suggestions

At the end of every response:

- Suggest related angles the user may not have considered.
- Recommend 2-3 related papers (from the paper's references, or from knowledge of the user's projects).
- If the paper is only indirectly relevant to the user's apparent interest, say so explicitly.
- Offer: "I think you should also consider [paper/angle] for [reason]. Want me to dig into that?"

## Step 7: Auto-Invocation

When reading a `.md` note file and encountering `[@citekey]` references:

- Do NOT invoke for every citation. Only invoke when understanding the paper would materially help answer the user's current question.
- When auto-invoking, use the lighter **Short Summary** flow unless deeper analysis is clearly needed.
- Inform the user: "I'm reading [@citekey] to better understand [context]..."
- Extract the citekey (strip `[@` and `]`) and follow Step 2A.
