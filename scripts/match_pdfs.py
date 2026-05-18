"""Match manually-downloaded PDFs in papers/pdfs/ to citekeys in references.bib.

The user often downloads PDFs from publisher sites with messy filenames
(e.g., 'gartenberg-et-al-2026-more-versus-better-...pdf'). This script:

  1. Reads every *.pdf in papers/pdfs/ that isn't already named <citekey>.pdf
  2. Matches each filename against the bibtex titles using token overlap
  3. Reports proposed renames; with --apply, renames them in place

Idempotent: only acts on files whose basename doesn't already match a known citekey.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIB = ROOT / "papers" / "references.bib"
PDFS = ROOT / "papers" / "pdfs"

STOPWORDS = {
    "a", "an", "and", "the", "of", "in", "on", "for", "to", "with",
    "is", "are", "be", "by", "from", "at", "as", "or", "that", "this",
    "we", "our", "their", "its", "it", "but", "not", "no",
}


def normalize(s: str) -> str:
    """Lowercase, strip diacritics, replace non-alnum with spaces."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-zA-Z0-9]+", " ", s.lower()).strip()
    return s


def tokens(s: str) -> set[str]:
    return {t for t in normalize(s).split() if t and t not in STOPWORDS and len(t) > 2}


def _read_field_value(body: str, start: int) -> tuple[str, int]:
    """Read a brace- or quote-delimited value starting at position start.
    Handles nested braces. Returns (value, end_position)."""
    if start >= len(body):
        return "", start
    if body[start] == "{":
        depth = 1
        i = start + 1
        while i < len(body) and depth > 0:
            if body[i] == "{":
                depth += 1
            elif body[i] == "}":
                depth -= 1
                if depth == 0:
                    return body[start + 1 : i], i + 1
            i += 1
        return body[start + 1 :], len(body)
    elif body[start] == '"':
        end = body.find('"', start + 1)
        if end == -1:
            return body[start + 1 :], len(body)
        return body[start + 1 : end], end + 1
    else:
        # Bare value: read until comma or newline
        end = start
        while end < len(body) and body[end] not in ",\n":
            end += 1
        return body[start:end].strip(), end


def parse_bib() -> list[dict[str, str]]:
    text = BIB.read_text(encoding="utf-8")
    entries = []
    # Find each @kind{citekey, ... }
    for entry_match in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,", text):
        kind = entry_match.group(1)
        citekey = entry_match.group(2)
        # Find matching close brace for this entry
        body_start = entry_match.end()
        depth = 1
        i = body_start
        while i < len(text) and depth > 0:
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    break
            i += 1
        body = text[body_start:i]

        fields = {"_kind": kind, "_citekey": citekey}
        # Parse fields
        j = 0
        while j < len(body):
            fm = re.match(r"\s*(\w+)\s*=\s*", body[j:])
            if not fm:
                j += 1
                continue
            name = fm.group(1).lower()
            val_start = j + fm.end()
            value, val_end = _read_field_value(body, val_start)
            fields[name] = re.sub(r"\s+", " ", value).strip()
            j = val_end
            # skip trailing comma + whitespace
            while j < len(body) and body[j] in ", \n\t":
                j += 1
        entries.append(fields)
    return entries


def extract_arxiv_id_from_filename(name: str) -> str | None:
    m = re.match(r"(\d{4}\.\d{4,5})", name)
    return m.group(1) if m else None


def extract_ssrn_id(name: str) -> str | None:
    m = re.search(r"ssrn[-_]?(\d+)", name.lower())
    return m.group(1) if m else None


def extract_nber_number(name: str) -> str | None:
    m = re.match(r"(w\d+)", name.lower())
    return m.group(1) if m else None


def best_match(pdf_name: str, entries: list[dict]) -> tuple[str | None, float]:
    """Return (citekey, score) of best match."""
    # 1. Direct ID matches first
    aid = extract_arxiv_id_from_filename(pdf_name)
    if aid:
        for e in entries:
            if e.get("eprint") == aid:
                return e["_citekey"], 1.0

    sid = extract_ssrn_id(pdf_name)
    if sid:
        for e in entries:
            url = e.get("url", "") or e.get("howpublished", "")
            if f"abstract_id={sid}" in url or sid in url:
                return e["_citekey"], 1.0

    nber = extract_nber_number(pdf_name)
    if nber:
        for e in entries:
            if e.get("number", "").lower() == nber:
                return e["_citekey"], 1.0

    # 2. Token overlap with titles
    pdf_tokens = tokens(pdf_name)
    best = (None, 0.0)
    for e in entries:
        title = e.get("title", "")
        if not title:
            continue
        title_tokens = tokens(title)
        if not title_tokens:
            continue
        # Jaccard
        inter = len(pdf_tokens & title_tokens)
        union = len(pdf_tokens | title_tokens)
        if union == 0:
            continue
        score = inter / union
        # Also boost when first 3+ significant tokens of title appear in filename
        first_title = list(title_tokens)[:5]
        boost = sum(1 for t in first_title if t in pdf_tokens) / max(len(first_title), 1)
        combined = 0.6 * score + 0.4 * boost
        if combined > best[1]:
            best = (e["_citekey"], combined)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="actually rename files")
    ap.add_argument("--threshold", type=float, default=0.35,
                    help="minimum match score (default 0.35)")
    args = ap.parse_args()

    if not PDFS.exists():
        print("papers/pdfs/ does not exist", file=sys.stderr)
        return 1

    entries = parse_bib()
    citekeys = {e["_citekey"] for e in entries}

    pdfs = sorted(PDFS.glob("*.pdf"))
    matched = []
    skipped = []
    unmatched = []

    for p in pdfs:
        stem = p.stem
        # Already a citekey-named file?
        if stem in citekeys:
            skipped.append((p.name, stem, "already-named"))
            continue
        ck, score = best_match(stem, entries)
        if ck and score >= args.threshold:
            # Conflict check: target exists?
            target = PDFS / f"{ck}.pdf"
            if target.exists() and target != p:
                skipped.append((p.name, ck, f"target {ck}.pdf already exists"))
                continue
            matched.append((p.name, ck, score))
        else:
            unmatched.append((p.name, ck, score))

    # Report
    print(f"=== Already named after citekey ({len(skipped)}) ===")
    for name, ck, why in skipped[:5]:
        print(f"  {name:60} → {ck:30} ({why})")
    if len(skipped) > 5:
        print(f"  … {len(skipped)-5} more")

    print(f"\n=== Proposed matches ({len(matched)}) ===")
    for name, ck, score in matched:
        print(f"  {score:.2f}  {name[:60]:60} → {ck}")

    print(f"\n=== Unmatched / below threshold ({len(unmatched)}) ===")
    for name, ck, score in unmatched:
        suggestion = f"best guess: {ck} ({score:.2f})" if ck else "no candidate"
        print(f"  {name[:60]:60}  {suggestion}")

    if args.apply:
        n = 0
        for name, ck, _ in matched:
            src = PDFS / name
            dst = PDFS / f"{ck}.pdf"
            src.rename(dst)
            n += 1
        print(f"\nRenamed {n} files.")
    else:
        print(f"\n(dry run — re-run with --apply to rename {len(matched)} files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
