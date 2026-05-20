<!-- DO NOT EDIT — auto-copied from skills/autoresearchclaw/details/biology-biopython.md -->

# `biology-biopython`



<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../autoresearchclaw/">AutoResearchClaw skills</a></div><div><b>Category:</b> <code>drafting</code></div><div><b>Field:</b> —</div><div><b>License:</b> <code>MIT</code></div><div><b>Updated:</b> 2026-04-23</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>paper-drafting</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/aiming-lab/AutoResearchClaw/contents/.claude/skills/biology-biopython/ --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/autoresearchclaw/biology-biopython/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/aiming-lab/AutoResearchClaw" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/aiming-lab/AutoResearchClaw?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

### Biopython Bioinformatics Best Practice

#### Sequence Manipulation
1. Create sequences: `from Bio.Seq import Seq; seq = Seq("ATGCGA")`
2. Complement: `seq.complement()`; Reverse complement: `seq.reverse_complement()`
3. Transcription: `seq.transcribe()` (DNA to RNA)
4. Translation: `seq.translate()` (DNA/RNA to protein)
5. GC content: `from Bio.SeqUtils import gc_fraction; gc_fraction(seq)`
6. Molecular weight: `from Bio.SeqUtils import molecular_weight`

#### File Parsing (SeqIO)
1. Read FASTA: `for rec in SeqIO.parse("file.fasta", "fasta"): ...`
2. Read GenBank: `for rec in SeqIO.parse("file.gb", "genbank"): ...`
3. Read single record: `rec = SeqIO.read("file.fasta", "fasta")`
4. Write sequences: `SeqIO.write(records, "output.fasta", "fasta")`
5. Convert formats: `SeqIO.convert("input.gb", "genbank", "output.fasta", "fasta")`
6. Index large files: `idx = SeqIO.index("large.fasta", "fasta")` for random access

#### BLAST Operations
1. Online BLAST: `from Bio.Blast import NCBIWWW; result = NCBIWWW.qblast("blastn", "nt", seq)`
2. Parse results: `from Bio.Blast import NCBIXML; records = NCBIXML.parse(result)`
3. Local BLAST: run via subprocess, parse XML output with NCBIXML
4. Always set `Entrez.email` before any NCBI access
5. Filter results by e-value (typically < 1e-5) and coverage

#### NCBI Database Access (Entrez)
1. Always set email: `Entrez.email = "your@email.com"`
2. Search: `handle = Entrez.esearch(db="pubmed", term="query")`
3. Fetch records: `handle = Entrez.efetch(db="nucleotide", id="ID", rettype="fasta")`
4. Use API key for higher rate limits (10 req/s vs 3 req/s)
5. Respect NCBI rate limits; add delays between batch requests

#### Phylogenetics (Bio.Phylo)
1. Read trees: `from Bio import Phylo; tree = Phylo.read("tree.nwk", "newick")`
2. Draw trees: `Phylo.draw(tree)` or `Phylo.draw_ascii(tree)`
3. Supported formats: newick, nexus, phyloxml
4. Traverse clades: `for clade in tree.find_clades(): ...`
5. Calculate distances: `tree.distance(clade1, clade2)`

#### Structure Analysis (Bio.PDB)
1. Parse PDB: `parser = PDBParser(); structure = parser.get_structure("id", "file.pdb")`
2. Hierarchy: Structure > Model > Chain > Residue > Atom
3. Get atoms: iterate through `structure.get_atoms()`
4. Calculate distances: use atom coordinate vectors
5. For mmCIF files: use `MMCIFParser()` instead of `PDBParser()`

#### Common Pitfalls
1. Always handle `SeqIO.parse` as an iterator — it exhausts after one pass
2. Check sequence alphabet compatibility before operations
3. Large files: use `SeqIO.index()` not `SeqIO.to_dict()` to avoid memory issues
4. Set proper timeout for remote BLAST queries (can take minutes)
5. Validate parsed data — missing annotations are common in public databases
