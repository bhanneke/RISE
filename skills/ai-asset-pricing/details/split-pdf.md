---
name: split-pdf
description: Download, split, and deeply read academic PDFs with adaptive chunking. Splits into optimally-sized chunks based on paper length, reads in controlled batches, and produces structured extraction notes tailored for empirical finance papers.
user_invocable: true
---

# Split-PDF: Download, Split, and Deep-Read Academic Papers

**CRITICAL RULE: Never read a full PDF in one pass.** Only read the split files, and only one batch at a time. Reading a full PDF will either crash the session with an unrecoverable "prompt too long" error -- destroying all context -- or produce shallow, hallucinated output where Claude skims the abstract, gets fuzzy on methodology, and fabricates details from results sections.

## When This Skill Is Invoked

The user wants to read, review, or summarize an academic paper. The input is either:
- A file path to a local PDF (e.g., `./articles/smith_2024.pdf`)
- A search query or paper title (e.g., `"Bai Bali Wen 2019 corporate bond factors"`)

**You must know what paper to read.** If the user invokes this skill without specifying a paper, ask them. Do not guess.

## Step 1: Acquire the PDF

**If a local file path is provided:**
- Verify the file exists
- If not already in `./articles/`, copy it there (preserve original)
- Proceed to Step 2

**If a search query is provided:**
1. Use Perplexity MCP tools to find the paper (prefer `perplexity_search`)
2. Use Bash (curl/wget) to download the PDF
3. Save to `./articles/` (create directory if needed)
4. Proceed to Step 2

**CRITICAL: Always preserve the original PDF.** The original in `articles/` must NEVER be deleted, moved, or overwritten. Split files are derivatives.

## Step 2: Determine Chunk Size (Adaptive)

Before splitting, determine total page count and select the optimal chunking strategy:

```python
from PyPDF2 import PdfReader
import os

reader = PdfReader(input_path)
total_pages = len(reader.pages)
```

**Chunking strategy by paper length:**

| Paper Length | Action | Chunk Size | Batch Size | Pages/Batch |
|-------------|--------|-----------|------------|-------------|
| < 12 pages | Read directly (no splitting) | -- | -- | -- |
| 12-25 pages | Light splitting | 8 pages | 2 chunks | ~16 pages |
| 25-45 pages | Standard splitting | 6 pages | 3 chunks | ~18 pages |
| 45-80 pages | Dense splitting | 5 pages | 3 chunks | ~15 pages |
| > 80 pages | Heavy splitting | 4 pages | 3 chunks | ~12 pages |

**Rationale**: Shorter papers have lower total token load, so larger chunks are safe. Longer papers (monographs, dissertations, papers with extensive appendices) need smaller chunks to maintain attention quality. The batch size controls how much you read before writing notes and pausing.

**Override**: If the user specifies a chunk size, use it. The adaptive sizing is a default, not a mandate.

## Step 3: Split the PDF

Create a subdirectory and split:

```python
from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_path, output_dir, pages_per_chunk):
    os.makedirs(output_dir, exist_ok=True)
    reader = PdfReader(input_path)
    total = len(reader.pages)
    prefix = os.path.splitext(os.path.basename(input_path))[0]

    for start in range(0, total, pages_per_chunk):
        end = min(start + pages_per_chunk, total)
        writer = PdfWriter()
        for i in range(start, end):
            writer.add_page(reader.pages[i])

        out_name = f"{prefix}_pp{start+1}-{end}.pdf"
        out_path = os.path.join(output_dir, out_name)
        with open(out_path, "wb") as f:
            writer.write(f)

    print(f"Split {total} pages into {-(-total // pages_per_chunk)} chunks of {pages_per_chunk} pages in {output_dir}")
```

**Directory convention:**
```
articles/
+-- bai_bali_wen_2019.pdf                    # original -- NEVER DELETE
+-- split_bai_bali_wen_2019/                 # split subdirectory
    +-- bai_bali_wen_2019_pp1-6.pdf
    +-- bai_bali_wen_2019_pp7-12.pdf
    +-- ...
    +-- notes.md                              # structured extraction
```

If PyPDF2 is not installed: `pip install PyPDF2`

## Step 4: Read in Batches

Read exactly one batch at a time (see table above for batch sizes). After each batch:

1. **Read** the batch of split PDFs using the Read tool
2. **Update** the running notes file (`notes.md` in the split subdirectory)
3. **Report** to the user:

> "Finished reading pages X-Y (batch N of M). Notes updated. N chunks remaining. Continue?"

4. **Wait** for user confirmation before reading the next batch

Do NOT read ahead. Do NOT read all splits at once. The pause-and-confirm protocol is mandatory.

## Step 5: Structured Extraction

As you read, extract information along these dimensions and write into `notes.md`. The dimensions are ordered by priority -- the first four are always populated; the rest are populated as information becomes available.

### Core Dimensions (always extract)

1. **Research question & motivation** -- What is the paper asking? What gap does it fill? Why does it matter?

2. **Data & sample construction** -- What data sources? Sample period? Universe (bonds, stocks, firms)? Filters applied? Number of observations? Unit of analysis? How are returns computed?

3. **Methodology** -- Econometric approach? Identification strategy? Portfolio sorts vs. Fama-MacBeth vs. factor models? Key specifications? How are standard errors computed?

4. **Key results** -- Main coefficient estimates, t-statistics, economic magnitudes (basis points, Sharpe ratios). Be specific: "long-short return of 45bp/month (t=2.87)" not "significant positive return."

### Extended Dimensions (extract when available)

5. **Factor/signal definitions** -- For asset pricing papers: How are sorting variables constructed? What price data is used? Holding period? Rebalancing frequency? Breakpoints (NYSE, full sample)?

6. **Robustness & alternatives** -- Subperiods? Alternative specifications? Placebo tests? What survives and what doesn't?

7. **Relevance to our work** -- How does this paper relate to our replication crisis paper? Does it use standard or adjusted approaches? Does it address measurement error? Is it in our factor zoo? What can we learn or cite?

8. **Replication feasibility** -- Is data publicly available? Replication archive? Code repository? Enough detail to reproduce Table 1?

### Extraction Rules

- **Be specific, not summarizing.** Write "long-short return = 0.45%/month (t=2.31) for quintile sorts on credit spread" not "the credit spread factor is significant."
- **Capture exact numbers.** Coefficient estimates, standard errors, t-statistics, sample sizes, R-squared values.
- **Note page references.** When recording a key finding, note which pages it came from (e.g., "Table 3, p. 18").
- **Flag contradictions.** If later sections contradict earlier findings or your understanding, note this explicitly.

## The Notes File

Output: `articles/split_<name>/notes.md`

Structure with clear headers for each dimension. Update incrementally after each batch -- do not rewrite from scratch. By completion, the notes should contain specific data sources, variable definitions, equation references, sample sizes, and coefficient estimates. Not a summary -- a structured extraction.

**Header format:**
```markdown
# Reading Notes: [Paper Title]
**Authors**: [Authors]
**Journal/Year**: [Journal, Year]
**Pages**: [Total pages] | **Chunks**: [N] | **Strategy**: [chunk size]pp x [batch size] batches

---

## 1. Research Question & Motivation
[Updated incrementally]

## 2. Data & Sample Construction
[Updated incrementally]

## 3. Methodology
[Updated incrementally]

## 4. Key Results
[Updated incrementally]

## 5. Factor/Signal Definitions
[Updated incrementally]

## 6. Robustness & Alternatives
[Updated incrementally]

## 7. Relevance to Our Work
[Updated incrementally]

## 8. Replication Feasibility
[Updated incrementally]

---
*Last updated after batch N (pages X-Y)*
```

## Triage Mode

For quick relevance assessment, read only the first chunk (abstract + introduction). Report:
- What the paper is about (1-2 sentences)
- Whether it's relevant to our work (yes/no/maybe + reason)
- Whether a full read is warranted

Invoke triage mode: `/split-pdf --triage <path-or-query>`

## Quick Reference

| Step | Action |
|------|--------|
| **Acquire** | Download to `./articles/` or use existing local file |
| **Size** | Count pages, select chunk size from table |
| **Split** | PyPDF2 chunks into `./articles/split_<name>/` |
| **Read** | One batch at a time, pause after each |
| **Extract** | Update `notes.md` with structured information |
| **Confirm** | Ask user before continuing to next batch |

## Why This Design

**Why adaptive chunks instead of fixed 4-page?** Academic papers vary enormously in density. A 20-page empirical paper with large tables can be read in bigger chunks than a 60-page theory paper with dense proofs. The adaptive strategy matches chunk size to cognitive load.

**Why these extraction dimensions?** They capture what a finance researcher needs to build on, replicate, or cite a paper. Generic "research question + method + findings" misses the specifics that matter: exactly how signals are constructed, what data filters are applied, whether measurement error is addressed.

**Why pause between batches?** To catch errors before they compound, redirect focus for specific sections, and prevent the notes from drifting. The human checkpoint is not overhead -- it's quality control.
