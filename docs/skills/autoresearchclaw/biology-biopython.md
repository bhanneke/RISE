<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/biology-biopython.md -->

# `biology-biopython`



<style>
.skill-layout { display: grid; grid-template-columns: minmax(0, 2fr) 18em; gap: 2em; }
@media (max-width: 900px) { .skill-layout { grid-template-columns: 1fr; } }
.skill-sidebar { background: #fafafa; border:1px solid #eaeaea; border-radius:8px; padding:1em; position:sticky; top:1em; align-self:start; font-size:0.95em; }
.skill-sidebar h3, .skill-sidebar h4 { color:#00695c; }
.skill-sidebar dl dt { margin-top:0.5em; }
.skill-sidebar dl dd { margin:0.1em 0 0 0; }
</style>

<div class="skill-layout">
<div class="skill-content" markdown>

---

---
name: biology-biopython
description: Bioinformatics with Biopython for sequence manipulation, file parsing, BLAST, and phylogenetics. Use when working with DNA/RNA/protein sequences or biological databases.
metadata:
  category: domain
  trigger-keywords: "sequence,FASTA,genome,protein,BLAST,phylogenetic,biopython,bioinformatics,gene,DNA,RNA"
  applicable-stages: "9,10,12"
  priority: "4"
  version: "1.0"
  author: researchclaw
  references: "adapted from K-Dense-AI/claude-scientific-skills"
---

## Biopython Bioinformatics Best Practice

### Sequence Manipulation
1. Create sequences: `from Bio.Seq import Seq; seq = Seq("ATGCGA")`
2. Complement: `seq.complement()`; Reverse complement: `seq.reverse_complement()`
3. Transcription: `seq.transcribe()` (DNA to RNA)
4. Translation: `seq.translate()` (DNA/RNA to protein)
5. GC content: `from Bio.SeqUtils import gc_fraction; gc_fraction(seq)`
6. Molecular weight: `from Bio.SeqUtils import molecular_weight`

### File Parsing (SeqIO)
1. Read FASTA: `for rec in SeqIO.parse("file.fasta", "fasta"): ...`
2. Read GenBank: `for rec in SeqIO.parse("file.gb", "genbank"): ...`
3. Read single record: `rec = SeqIO.read("file.fasta", "fasta")`
4. Write sequences: `SeqIO.write(records, "output.fasta", "fasta")`
5. Convert formats: `SeqIO.convert("input.gb", "genbank", "output.fasta", "fasta")`
6. Index large files: `idx = SeqIO.index("large.fasta", "fasta")` for random access

### BLAST Operations
1. Online BLAST: `from Bio.Blast import NCBIWWW; result = NCBIWWW.qblast("blastn", "nt", seq)`
2. Parse results: `from Bio.Blast import NCBIXML; records = NCBIXML.parse(result)`
3. Local BLAST: run via subprocess, parse XML output with NCBIXML
4. Always set `Entrez.email` before any NCBI access
5. Filter results by e-value (typically < 1e-5) and coverage

### NCBI Database Access (Entrez)
1. Always set email: `Entrez.email = "your@email.com"`
2. Search: `handle = Entrez.esearch(db="pubmed", term="query")`
3. Fetch records: `handle = Entrez.efetch(db="nucleotide", id="ID", rettype="fasta")`
4. Use API key for higher rate limits (10 req/s vs 3 req/s)
5. Respect NCBI rate limits; add delays between batch requests

### Phylogenetics (Bio.Phylo)
1. Read trees: `from Bio import Phylo; tree = Phylo.read("tree.nwk", "newick")`
2. Draw trees: `Phylo.draw(tree)` or `Phylo.draw_ascii(tree)`
3. Supported formats: newick, nexus, phyloxml
4. Traverse clades: `for clade in tree.find_clades(): ...`
5. Calculate distances: `tree.distance(clade1, clade2)`

### Structure Analysis (Bio.PDB)
1. Parse PDB: `parser = PDBParser(); structure = parser.get_structure("id", "file.pdb")`
2. Hierarchy: Structure > Model > Chain > Residue > Atom
3. Get atoms: iterate through `structure.get_atoms()`
4. Calculate distances: use atom coordinate vectors
5. For mmCIF files: use `MMCIFParser()` instead of `PDBParser()`

### Common Pitfalls
1. Always handle `SeqIO.parse` as an iterator — it exhausts after one pass
2. Check sequence alphabet compatibility before operations
3. Large files: use `SeqIO.index()` not `SeqIO.to_dict()` to avoid memory issues
4. Set proper timeout for remote BLAST queries (can take minutes)
5. Validate parsed data — missing annotations are common in public databases


</div>

<div class="skill-sidebar">
<h3 style="margin-top:0;">Use this skill</h3>
<button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/biology-biopython/ --jq .content | base64 -d`); this.textContent='✓ copied';"
  style="background:#00897b; color:white; border:none; padding:0.5em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em;">📋 copy fetch command</button>
<p style="font-size:0.85em; color:#666; margin:0.6em 0;">Pulls the raw SKILL.md from <code>aiming-lab/AutoResearchClaw</code>.</p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.3em 0;">Metadata</h4>
<dl style="font-size:0.85em; margin:0;">
<dt><b>Pack</b></dt><dd><a href="../autoresearchclaw.md">AutoResearchClaw skills</a></dd>
<dt><b>Category</b></dt><dd><code>drafting</code></dd>
<dt><b>Field</b></dt><dd>—</dd>
<dt><b>Pipeline stages</b></dt><dd><code>paper-drafting</code></dd>
<dt><b>License</b></dt><dd>MIT</dd>
<dt><b>Last update</b></dt><dd>2026-04-23</dd>
</dl>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<h4 style="margin:0 0 0.5em 0;">Upstream</h4>
<p style="font-size:0.85em; margin:0.3em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw">⭐ aiming-lab/AutoResearchClaw</a><br><img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="stars"></p>
<p style="margin:0.6em 0;"><a href="https://github.com/aiming-lab/AutoResearchClaw" style="font-size:0.9em;">↗ view SKILL.md on source</a></p>
<hr style="margin:1em 0; border:none; border-top:1px solid #eee;">
<button onclick="navigator.clipboard.writeText('https://bhanneke.github.io/RISE/skills/autoresearchclaw/biology-biopython/'); this.textContent='✓ copied';"
  style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.85em;">🔗 copy share link</button>
<p style="font-size:0.8em; color:#666; margin:0.8em 0 0;">Suggest improvements via <a href="https://github.com/bhanneke/RISE/issues/new">GitHub issue</a> or <a href="https://github.com/bhanneke/RISE/edit/main/skills/autoresearchclaw.yml">edit on GitHub</a>.</p>
</div>

</div>
