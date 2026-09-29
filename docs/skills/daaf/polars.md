<!-- DO NOT EDIT — auto-copied from skills/daaf/details/polars.md -->

# `/polars`

Python guide to Polars, DAAF's default DataFrame library, covering lazy and eager execution, expressions, Parquet and CSV I/O, joins and aggregations, performance patterns, anti-patterns and migration from pandas.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../daaf/">DAAF — Data Analyst Augmentation Framework (Brian Heseung Kim)</a></div><div><b>Category:</b> <code>data-handling</code></div><div><b>Field:</b> general</div><div><b>License:</b> <code>LGPL-3.0-or-later (as declared in the README, badge and CITATION.cff; the repo ships the GPL-3.0 text as LICENSE plus COPYING.LESSER)</code></div><div><b>Updated:</b> 2026-07-16</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-analysis</code> · <code>code-generation</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/DAAF-Contribution-Community/daaf/contents/.claude/skills/polars/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/daaf/polars/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/DAAF-Contribution-Community/daaf/blob/main/.claude/skills/polars/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/DAAF-Contribution-Community/daaf?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## Polars Skill

Polars DataFrame library for high-performance data manipulation in Python. Covers lazy/eager execution, expressions, I/O (CSV, Parquet, JSON, database), aggregations, joins, string/datetime operations, pandas/NumPy interop, and performance optimization. Use when working with Polars DataFrames, migrating from pandas, reading Parquet files, or optimizing data pipeline performance.

Comprehensive skill for high-performance data manipulation with Polars. Use decision trees below to find the right guidance, then load detailed references.

### What is Polars?

Polars is a **fast** DataFrame library for Python (and Rust):
- **Fast**: Written in Rust, optimized for modern CPUs with SIMD and parallelism
- **Lazy Evaluation**: Build query plans that get optimized before execution
- **Expressive**: Powerful expression API for complex transformations
- **Memory Efficient**: Columnar format, streaming for larger-than-memory data
- **No Dependencies**: Pure Rust core, no NumPy/Pandas required

### Version Notes

This skill targets **Polars 1.x** (tested with 1.37.1). Key changes from 0.x:
- `apply` renamed to `map_elements` (0.19+)
- `groupby` renamed to `group_by` (0.19+)
- `melt` renamed to `unpivot` (1.0+)
- Streaming engine improvements in 1.x
- `pl.Utf8` is now `pl.String` (1.0+, Utf8 still works as alias)

### How to Use This Skill

#### Reference File Structure

Each topic in `./references/` contains focused documentation:

| File | Purpose | When to Read |
|------|---------|--------------|
| `quickstart.md` | Installation, concepts, first DataFrame | Starting with Polars |
| `dataframes-series.md` | Creation, selection, filtering, modification | Basic data manipulation |
| `io-data.md` | CSV, Parquet, JSON, database I/O | Loading/saving data |
| `expressions.md` | Expression system, contexts, chaining | Understanding Polars idioms |
| `aggregations-grouping.md` | GroupBy, window functions, statistics | Summarizing data |
| `joins-concat.md` | Joins, concatenation, pivot/unpivot | Combining DataFrames |
| `strings-datetime-categorical.md` | String ops, datetime, categoricals | Type-specific operations |
| `performance.md` | Lazy execution, optimization, anti-patterns | Making code faster |
| `interop.md` | Pandas, NumPy, PyArrow, DuckDB | Working with other tools |
| `gotchas.md` | Common errors, anti-patterns, migration | Debugging issues |

#### Reading Order

1. **New to Polars?** Start with `quickstart.md` then `expressions.md`
2. **Coming from Pandas?** Read `quickstart.md`, `expressions.md`, then `interop.md`
3. **Performance issues?** Check `performance.md` first

**The reference-file routing in this skill applies to advisory and brainstorming turns as much as implementation.** Recommending an approach, reviewing a plan, or answering a question that touches a routed topic calls for reading the routed reference file just as much as writing code does — the reference files carry curated caveats and environment-specific constraints that this overview and general knowledge lack.

### Quick Decision Trees

#### "I need to get started"

```
Getting started?
├─ Install Polars → ./references/quickstart.md
├─ Create first DataFrame → ./references/quickstart.md
├─ Understand lazy vs eager → ./references/quickstart.md
├─ Learn expression syntax → ./references/expressions.md
└─ Coming from Pandas → ./references/interop.md
```

#### "I need to load or save data"

```
Loading/saving data?
├─ Read CSV file → ./references/io-data.md
├─ Read Parquet (recommended) → ./references/io-data.md
├─ Read JSON/NDJSON → ./references/io-data.md
├─ Read from database → ./references/io-data.md
├─ Read multiple files (glob) → ./references/io-data.md
├─ Write to file → ./references/io-data.md
└─ Larger-than-memory data → ./references/performance.md
```

#### "I need to filter or select data"

```
Filtering/selecting?
├─ Select columns by name → ./references/dataframes-series.md
├─ Select by pattern/regex → ./references/dataframes-series.md
├─ Select by data type → ./references/dataframes-series.md
├─ Filter rows by condition → ./references/dataframes-series.md
├─ Filter with multiple conditions → ./references/dataframes-series.md
├─ Handle null values → ./references/dataframes-series.md
└─ Add/modify columns → ./references/dataframes-series.md
```

#### "I need to aggregate or group data"

```
Aggregating data?
├─ Basic statistics (sum, mean, etc.) → ./references/aggregations-grouping.md
├─ Group by columns → ./references/aggregations-grouping.md
├─ Multiple aggregations → ./references/aggregations-grouping.md
├─ Window functions (over) → ./references/aggregations-grouping.md
├─ Rolling/moving averages → ./references/aggregations-grouping.md
├─ Cumulative operations → ./references/aggregations-grouping.md
└─ Ranking within groups → ./references/aggregations-grouping.md
```

#### "I need to combine DataFrames"

```
Combining data?
├─ Join two DataFrames → ./references/joins-concat.md
├─ Left/right/outer join → ./references/joins-concat.md
├─ Anti-join (not in) → ./references/joins-concat.md
├─ Concatenate vertically → ./references/joins-concat.md
├─ Pivot (long to wide) → ./references/joins-concat.md
└─ Unpivot/melt (wide to long) → ./references/joins-concat.md
```

#### "I need better performance"

```
Performance issues?
├─ Use lazy evaluation → ./references/performance.md
├─ Avoid row iteration → ./references/performance.md
├─ Reduce memory usage → ./references/performance.md
├─ Process large files → ./references/performance.md
├─ Optimize query plan → ./references/performance.md
└─ Common anti-patterns → ./references/performance.md
```

#### "Something isn't working"

```
Having issues?
├─ Type errors → ./references/gotchas.md
├─ Null handling → ./references/gotchas.md
├─ Expression context errors → ./references/gotchas.md
├─ String operations → ./references/strings-datetime-categorical.md
├─ Date parsing issues → ./references/strings-datetime-categorical.md
├─ Performance problems → ./references/gotchas.md
├─ Pandas migration issues → ./references/gotchas.md
├─ Memory errors → ./references/gotchas.md
└─ General troubleshooting → ./references/gotchas.md
```

### File-First Execution in Research Workflows

**Important:** In data research pipelines (see `CLAUDE.md`), Polars transformations are executed through **script files**, not interactively. This ensures auditability and reproducibility.

**The pattern:**
1. Write transformation code to `scripts/stage{N}_{type}/{step}_{task-name}.py`
2. Execute via Bash with automatic output capture wrapper script
3. Validation results get automatically embedded in scripts as comments
4. If failed, create versioned copy for fixes

Closely read `agent_reference/SCRIPT_EXECUTION_REFERENCE.md` for the mandatory file-first execution protocol covering complete code file writing, output capture, and file versioning rules.

**See:**
- `agent_reference/SCRIPT_EXECUTION_REFERENCE.md` — Script execution protocol and format with validation

The examples below show Polars syntax. In research workflows, wrap them in scripts following the file-first pattern.

---

### Quick Reference

#### Essential Import

```python
import polars as pl
import polars.selectors as cs  # For column selection by type
```

#### Lazy vs Eager (One-Liner)

```python
## Eager: immediate execution
df = pl.read_csv("data.csv")

## Lazy: deferred, optimized execution (preferred for large data)
lf = pl.scan_csv("data.csv")
df = lf.collect()  # Execute when ready
```

#### Core Expression Patterns

```python
## Select columns
df.select("a", "b")
df.select(pl.col("a"), pl.col("b"))
df.select(pl.all().exclude("id"))

## Filter rows
df.filter(pl.col("a") > 10)
df.filter((pl.col("a") > 10) & (pl.col("b") == "x"))

## Add/modify columns
df.with_columns(
    (pl.col("a") * 2).alias("a_doubled"),
    pl.col("b").str.to_uppercase().alias("b_upper")
)

## Conditional column
df.with_columns(
    pl.when(pl.col("a") > 10)
      .then(pl.lit("high"))
      .otherwise(pl.lit("low"))
      .alias("category")
)

## Group and aggregate
df.group_by("category").agg(
    pl.col("value").sum().alias("total"),
    pl.col("value").mean().alias("average"),
    pl.len().alias("count")
)
```

#### Essential Functions

| Function | Purpose |
|----------|---------|
| `pl.col("name")` | Reference a column |
| `pl.lit(value)` | Literal value |
| `pl.all()` | All columns |
| `pl.exclude("col")` | All except specified |
| `pl.len()` | Row count |
| `pl.when().then().otherwise()` | Conditional logic |
| `.alias("name")` | Rename result |
| `.cast(pl.Int64)` | Convert type |

#### Common Data Types

| Type | Description |
|------|-------------|
| `pl.Int64`, `pl.Int32` | Integers |
| `pl.Float64`, `pl.Float32` | Floats |
| `pl.String` (or `pl.Utf8`) | Strings |
| `pl.Boolean` | True/False |
| `pl.Date`, `pl.Datetime` | Dates and timestamps |
| `pl.Duration` | Time differences |
| `pl.Categorical` | Categorical strings |
| `pl.List` | List of values |
| `pl.Struct` | Named fields |

#### Quick Cheatsheet

```python
## I/O
df = pl.read_csv/parquet/json("file")
lf = pl.scan_csv/parquet/ndjson("file")  # Lazy
df.write_csv/parquet/json("file")

## Selection
df.select("a", "b")
df.select(cs.numeric())  # By type

## Filtering
df.filter(pl.col("a") > 1)

## Aggregation
df.group_by("key").agg(pl.col("val").sum())

## Joining
df1.join(df2, on="key", how="left")

## Sorting
df.sort("col", descending=True)

## Lazy execution
lf.collect()  # Run query
lf.explain()  # Show plan
```

### Topic Index

| Topic | Reference File |
|-------|---------------|
| Installation | `./references/quickstart.md` |
| DataFrame Creation | `./references/quickstart.md` |
| Lazy vs Eager | `./references/quickstart.md` |
| Column Selection | `./references/dataframes-series.md` |
| Row Filtering | `./references/dataframes-series.md` |
| Adding Columns | `./references/dataframes-series.md` |
| CSV Files | `./references/io-data.md` |
| Parquet Files | `./references/io-data.md` |
| Database Connections | `./references/io-data.md` |
| Expressions | `./references/expressions.md` |
| Method Chaining | `./references/expressions.md` |
| Contexts | `./references/expressions.md` |
| GroupBy | `./references/aggregations-grouping.md` |
| Window Functions | `./references/aggregations-grouping.md` |
| Rolling Windows | `./references/aggregations-grouping.md` |
| Joins | `./references/joins-concat.md` |
| Concatenation | `./references/joins-concat.md` |
| Pivot/Unpivot | `./references/joins-concat.md` |
| String Operations | `./references/strings-datetime-categorical.md` |
| Datetime Handling | `./references/strings-datetime-categorical.md` |
| Categorical Data | `./references/strings-datetime-categorical.md` |
| Query Optimization | `./references/performance.md` |
| Memory Management | `./references/performance.md` |
| Anti-Patterns | `./references/performance.md` |
| Pandas Conversion | `./references/interop.md` |
| NumPy Integration | `./references/interop.md` |
| DuckDB Integration | `./references/interop.md` |
| Type Errors | `./references/gotchas.md` |
| qcut Label Gotcha | `./references/gotchas.md` |
| Null Handling Issues | `./references/gotchas.md` |
| Expression Context Errors | `./references/gotchas.md` |
| Performance Anti-Patterns | `./references/gotchas.md` |
| Migration from Pandas | `./references/gotchas.md` |
| Memory Issues | `./references/gotchas.md` |

### Citation

When this library is used as a primary analytical tool, include in the report's
Software & Tools references:

> Vink, R. et al. Polars: Blazingly fast DataFrames [Computer software]. https://pola.rs/

**Cite when:** Polars is the core data processing engine for the analysis (typically always true in DAAF pipelines).
**Do not cite when:** Only used for trivial file I/O in a script primarily using another tool.
