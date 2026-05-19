# BibTeX Conventions for Economics

Guidelines for maintaining clean, consistent, and complete BibTeX databases
for economics research. These conventions follow the norms of top economics
journals and the `natbib` citation system.

## Preamble setup

```latex
\usepackage[authoryear,round]{natbib}  % Author-year citations with round parens
\usepackage{doi}                        % REQUIRED — renders DOIs as clickable links
\bibliographystyle{plainnat}            % Default: shows DOI in references
% Journal-specific alternatives: aer, ecta, chicago, jpe (check DOI support)

% At the end of the document:
\bibliography{references}               % Points to references.bib
```

**IMPORTANT:** Always include `\usepackage{doi}`. This package renders DOI fields
as clickable hyperlinks in the bibliography. The `plainnat` style displays DOIs
by default. If using a journal-specific style (e.g., `aer`), verify that it
renders the `doi` field — if not, switch to `plainnat` or add a custom `.bst`.

### Common bibliography styles in economics

| Style file | Journal | DOI display | Notes |
|-----------|---------|-------------|-------|
| `plainnat`| General natbib | **Yes** | **Default choice** — shows DOI in references |
| `aer`     | American Economic Review | No | Most common in applied micro; DOI via `\usepackage{doi}` only |
| `ecta`    | Econometrica | No | Preferred for theory papers |
| `chicago` | Chicago Manual of Style | Partial | Used by JPE, others |
| `jpe`     | Journal of Political Economy | No | Chicago-adjacent |

**Rule:** Use `plainnat` as default unless submitting to a specific journal that
requires its own `.bst`. This ensures DOIs are always visible in the bibliography.

## Citation commands (natbib)

```latex
\citet{autor2013}        % Autor, Dorn, and Hanson (2013)
\citep{autor2013}        % (Autor, Dorn, and Hanson, 2013)
\citealt{autor2013}      % Autor, Dorn, and Hanson 2013   (no parens)
\citealp{autor2013}      % Autor, Dorn, and Hanson, 2013  (no parens, with comma)
\citeauthor{autor2013}   % Autor, Dorn, and Hanson
\citeyear{autor2013}     % 2013
\citeyearpar{autor2013}  % (2013)

% Multiple citations
\citep{autor2013,dix-carneiro2017}  % (Autor et al., 2013; Dix-Carneiro and Kovak, 2017)

% Citation with page/chapter reference
\citep[p.~42]{autor2013}              % (Autor et al., 2013, p. 42)
\citep[see][chapter~3]{autor2013}     % (see Autor et al., 2013, chapter 3)
```

Use `\citet` when the authors are the grammatical subject of the sentence.
Use `\citep` for parenthetical references.

```latex
% Correct usage:
\citet{autor2013} document large employment declines.
The employment effects are substantial \citep{autor2013}.

% WRONG:
\citep{autor2013} document large employment declines.  % Don't use \citep as subject
```

## Entry types

### @article -- Published journal articles

The most common entry type in economics. Required fields: author, title, journal,
year, volume.

```bibtex
@article{autor2013,
  author    = {Autor, David H. and Dorn, David and Hanson, Gordon H.},
  title     = {The China Syndrome: Local Labor Market Effects of Import
               Competition in the United States},
  journal   = {American Economic Review},
  year      = {2013},
  volume    = {103},
  number    = {6},
  pages     = {2121--2168},
  doi       = {10.1257/aer.103.6.2121},
}
```

### @techreport -- Working papers

Use for NBER working papers, CEPR discussion papers, Fed working papers,
university working paper series, and any unpublished manuscript with a
series number.

```bibtex
@techreport{smith2024wp,
  author      = {Smith, Jane A. and Johnson, Robert},
  title       = {The Long-Run Effects of Universal Pre-K},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {31245},
  year        = {2024},
  doi         = {10.3386/w31245},
}
```

For NBER specifically, the convention is:

```bibtex
@techreport{jones2023nber,
  author      = {Jones, Charles I.},
  title       = {Recipes and Economic Growth: A Combinatorial March Down
                 an Exponential},
  institution = {National Bureau of Economic Research},
  type        = {Working Paper},
  number      = {31441},
  year        = {2023},
  series      = {NBER Working Paper Series},
  doi         = {10.3386/w31441},
}
```

### SSRN working papers

```bibtex
@techreport{chen2024ssrn,
  author      = {Chen, Wei and Liu, Xiaodong},
  title       = {Network Effects in Peer-to-Peer Markets},
  institution = {Social Science Research Network},
  type        = {SSRN Working Paper},
  number      = {4567890},
  year        = {2024},
  note        = {Available at \url{https://ssrn.com/abstract=4567890}},
}
```

### CEPR discussion papers

```bibtex
@techreport{mueller2023cepr,
  author      = {Mueller, Hannes and Rauh, Christopher},
  title       = {The Hard Problem of Prediction for Conflict Prevention},
  institution = {Centre for Economic Policy Research},
  type        = {Discussion Paper},
  number      = {17820},
  year        = {2023},
}
```

### Federal Reserve working papers

```bibtex
@techreport{garcia2024fed,
  author      = {Garcia, Maria and Williams, John C.},
  title       = {Monetary Policy Transmission in a Low-Rate Environment},
  institution = {Federal Reserve Bank of New York},
  type        = {Staff Report},
  number      = {1089},
  year        = {2024},
}
```

### @unpublished -- Manuscripts without a series

Use for papers without an official working paper number (e.g., job market
papers, manuscripts in preparation, papers "under review").

```bibtex
@unpublished{doe2024jmp,
  author = {Doe, Jane},
  title  = {Information Frictions and Housing Markets},
  note   = {Job Market Paper, MIT},
  year   = {2024},
}

@unpublished{lee2024manuscript,
  author = {Lee, David S. and Park, Jimin},
  title  = {New Evidence on Tax Salience},
  note   = {Manuscript, Princeton University},
  year   = {2024},
}
```

### @incollection -- Chapters in edited volumes

Common for Handbook chapters (Handbook of Labor Economics, Handbook of
Public Economics, etc.).

```bibtex
@incollection{card1999handbook,
  author    = {Card, David},
  title     = {The Causal Effect of Education on Earnings},
  booktitle = {Handbook of Labor Economics},
  editor    = {Ashenfelter, Orley C. and Card, David},
  volume    = {3},
  chapter   = {30},
  pages     = {1801--1863},
  publisher = {Elsevier},
  year      = {1999},
  doi       = {10.1016/S1573-4463(99)03011-4},
}
```

### @inproceedings -- Conference proceedings

Rarely used in economics (unlike computer science). Use only for AEA Papers
and Proceedings or similar.

```bibtex
@inproceedings{chetty2014pp,
  author    = {Chetty, Raj and Hendren, Nathaniel and Kline, Patrick
               and Saez, Emmanuel},
  title     = {Where is the Land of Opportunity? The Geography of
               Intergenerational Mobility in the United States},
  booktitle = {American Economic Review: Papers \& Proceedings},
  year      = {2014},
  volume    = {104},
  number    = {5},
  pages     = {141--147},
  doi       = {10.1257/aer.104.5.141},
}
```

### @book -- Monographs and textbooks

```bibtex
@book{mascolell1995,
  author    = {Mas-Colell, Andreu and Whinston, Michael D. and Green, Jerry R.},
  title     = {Microeconomic Theory},
  publisher = {Oxford University Press},
  year      = {1995},
  address   = {New York},
}

@book{angrist2009,
  author    = {Angrist, Joshua D. and Pischke, J{\"o}rn-Steffen},
  title     = {Mostly Harmless Econometrics: An Empiricist's Companion},
  publisher = {Princeton University Press},
  year      = {2009},
  address   = {Princeton, NJ},
}
```

## Citation key conventions

Use a consistent naming scheme throughout the `.bib` file. The most common
convention in economics:

```
lastnameYYYY          % Single author: card1999
lastname1lastname2YYYY % Two authors: angristpischke2009
lastnameetal2013      % Three+ authors: autoretal2013
```

For disambiguation when an author has multiple papers in one year:

```
card1999a             % First paper
card1999b             % Second paper
```

Alternative conventions (less common but also acceptable):

```
ADH2013               % Initials + year (used in some working paper databases)
autor-dorn-hanson-2013 % Hyphenated (readable but long)
```

Pick one convention and stick with it across your entire `.bib` file and
all your papers. Consistency matters more than the specific scheme.

## Author name formatting

BibTeX expects `Lastname, Firstname` format with `and` between authors:

```bibtex
% Correct:
author = {Autor, David H. and Dorn, David and Hanson, Gordon H.},

% Also correct (reversed order):
author = {David H. Autor and David Dorn and Gordon H. Hanson},

% WRONG: do not use commas between authors
author = {Autor, David H., Dorn, David, Hanson, Gordon H.},

% WRONG: do not use & or other separators
author = {Autor, David H. & Dorn, David & Hanson, Gordon H.},
```

### Special characters in names

Use LaTeX escapes for accented characters:

```bibtex
author = {Pischke, J{\"o}rn-Steffen},           % umlaut
author = {Pi{\~n}eiro, Carlos},                  % tilde
author = {S{\'a}nchez, Mar{\'\i}a},              % acute accents
author = {Bj{\"o}rklund, Anders},                % Swedish umlaut
author = {Mas-Colell, Andreu},                    % hyphenated name
author = {{World Bank}},                          % institutional author
author = {{Congressional Budget Office}},          % institutional author
```

Wrap institutional/corporate authors in double braces to prevent BibTeX
from parsing them as "Firstname Lastname."

## Required vs. optional fields by entry type

### @article

| Field | Required? | Notes |
|-------|-----------|-------|
| author | Yes | |
| title | Yes | |
| journal | Yes | Full name, not abbreviation |
| year | Yes | |
| volume | Yes | |
| number | Recommended | Issue number |
| pages | Recommended | Use en-dash: `2121--2168` |
| doi | **Required** | Must be included — look up via CrossRef if missing |
| url | Optional | Usually redundant if DOI present |
| month | Optional | Rarely needed |

### @techreport

| Field | Required? | Notes |
|-------|-----------|-------|
| author | Yes | |
| title | Yes | |
| institution | Yes | E.g., "National Bureau of Economic Research" |
| year | Yes | |
| type | Recommended | "Working Paper", "Discussion Paper", "Staff Report" |
| number | Recommended | The WP number |
| doi | **Required** | NBER papers have DOIs; look up via CrossRef for others |

### @incollection

| Field | Required? | Notes |
|-------|-----------|-------|
| author | Yes | Chapter author |
| title | Yes | Chapter title |
| booktitle | Yes | Book title |
| editor | Yes | Book editors |
| publisher | Yes | |
| year | Yes | |
| pages | Recommended | |
| volume | Recommended | For multi-volume handbooks |
| chapter | Optional | |
| doi | **Required** | Look up via CrossRef if missing |

## DOI formatting

**Every reference MUST include a DOI.** This is non-negotiable for published
articles, book chapters, and working papers with assigned DOIs. For the rare
entry without a DOI (e.g., very old books, unpublished manuscripts), add a
`note` field explaining why. Format consistently:

```bibtex
% Preferred: just the DOI identifier
doi = {10.1257/aer.103.6.2121},

% Also acceptable: full URL
doi = {https://doi.org/10.1257/aer.103.6.2121},

% DO NOT mix both doi and url when the URL is just the DOI resolver:
doi = {10.1257/aer.103.6.2121},
url = {https://doi.org/10.1257/aer.103.6.2121},  % REDUNDANT -- remove
```

## Journal name conventions

Use full journal names, not abbreviations. BibTeX style files handle
abbreviation if needed.

```bibtex
% Correct:
journal = {American Economic Review},
journal = {Quarterly Journal of Economics},
journal = {Journal of Political Economy},
journal = {Econometrica},
journal = {Review of Economic Studies},
journal = {Journal of Finance},
journal = {Review of Economics and Statistics},
journal = {Journal of Monetary Economics},
journal = {Journal of Public Economics},
journal = {Journal of Labor Economics},
journal = {Journal of Econometrics},
journal = {American Economic Journal: Applied Economics},
journal = {American Economic Journal: Economic Policy},
journal = {American Economic Journal: Macroeconomics},
journal = {American Economic Journal: Microeconomics},

% WRONG: do not abbreviate
journal = {AER},
journal = {QJE},
journal = {JPE},
journal = {ECTA},
journal = {REStud},
```

## Page ranges

Always use en-dash (`--`) for page ranges. BibTeX converts `--` to an
en-dash in the output.

```bibtex
pages = {2121--2168},    % Correct: en-dash
pages = {2121-2168},     % Wrong: hyphen (technically works but bad practice)
pages = {2121},          % Single page (for very short items like editorials)
```

## Title capitalization

BibTeX style files typically handle capitalization. To preserve capitalization
of proper nouns, acronyms, and specific terms, wrap them in braces:

```bibtex
% Words in braces will NOT be downcased by the style file:
title = {The {China} Syndrome: Local Labor Market Effects of Import
         Competition in the {United States}},

title = {An {ARCH} Model of the {Fisher} Effect},

title = {{GDP}, Prices, and Growth: Lessons from the {Great Recession}},

% Protect the entire title only if necessary (defeats the purpose of style files):
title = {{The China Syndrome: Local Labor Market Effects}},  % Avoid this
```

## Handling forthcoming papers

```bibtex
@article{smith2024forth,
  author  = {Smith, Jane A.},
  title   = {Returns to Education in Developing Countries},
  journal = {American Economic Review},
  year    = {forthcoming},
  note    = {Accepted June 2024},
}
```

## Sorting and organization

Keep your `.bib` file sorted alphabetically by citation key. This makes it
easy to find entries and spot duplicates.

Use a consistent structure within each entry:
1. `author`
2. `title`
3. `journal` / `booktitle` / `institution`
4. `year`
5. `volume`, `number`, `pages`
6. `editor`, `publisher`, `address` (for books/chapters)
7. `doi`
8. `note` / `url` (if needed)

## Common mistakes to avoid

1. **Inconsistent author names.** The same person appears as "Autor, David",
   "Autor, David H.", and "David Autor" in different entries. Pick one
   and be consistent.

2. **Missing braces around proper nouns.** "United States" becomes "united
   states" in some styles. Always brace proper nouns in titles.

3. **Duplicate entries.** The same paper with two different keys. Use a
   consistent key scheme and search before adding.

4. **Outdated working papers.** A paper was cited as a working paper but has
   since been published. Update the entry to `@article` with the journal info.
   Referees notice this.

5. **Missing DOIs.** DOIs are **required** for all references. Use CrossRef
   (crossref.org/SimpleTextQuery) to look them up. A bibliography without
   DOIs is incomplete and will be flagged in review.

6. **Journal abbreviations.** Use full names. Let the style file handle it.

7. **Wrong entry type.** Using `@article` for a working paper, or `@misc`
   for a book chapter. Use the correct type so the style file formats it
   properly.

8. **Forgetting AEA P&P.** "American Economic Review: Papers and Proceedings"
   is a separate publication from the AER. Cite it correctly.

9. **Not escaping special characters.** Ampersands (`\&`), percent signs (`\%`),
   and accented characters need LaTeX escapes.

10. **Overly long notes fields.** The `note` field is for brief metadata
    ("Forthcoming", "Revised version"), not abstracts or summaries.

## Useful tools

- **Google Scholar:** Export BibTeX directly (but always clean up the output --
  Google Scholar entries are often incomplete or poorly formatted).
- **CrossRef / doi.org:** Look up DOIs and get clean BibTeX via
  `https://doi.org/[DOI]` with Accept header `application/x-bibtex`.
- **JabRef / BibDesk:** GUI tools for managing `.bib` files. JabRef is
  cross-platform; BibDesk is macOS-only but excellent.
- **Zotero:** Reference manager with BibTeX export via Better BibTeX plugin.
  Good for collaborative projects.
- **dblp / EconLit:** Look up entries if Google Scholar's version is incomplete.
