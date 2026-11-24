<!-- DO NOT EDIT — auto-copied from skills/ai-asset-pricing/details/wrds-ssh.md -->

# `/wrds-ssh`

Connects to WRDS servers to run SAS code and PostgreSQL queries, submit batch jobs and transfer files.

<div class="skill-card" style="background:#fafafa; border:1px solid #e0e0e0; border-radius:8px; padding:1em 1.2em; margin:1em 0 1.5em; font-size:0.95em;"><div style="display:flex; flex-wrap:wrap; gap:1em 2em; align-items:baseline;"><div><b>Pack:</b> <a href="../ai-asset-pricing/">ai-asset-pricing (Alex Dickerson)</a></div><div><b>Category:</b> <code>data-handling</code></div><div><b>Field:</b> finance</div><div><b>License:</b> <code>MIT (repo LICENSE, "Copyright (c) 2025 Alex Dickerson")</code></div><div><b>Updated:</b> 2026-04-19</div></div><div style="margin-top:0.5em;"><b>Stages:</b> <code>data-acquisition</code></div><div style="margin-top:0.8em;"><button onclick="navigator.clipboard.writeText(`gh api repos/Alexander-M-Dickerson/ai-asset-pricing/contents/.claude/skills/wrds-ssh/SKILL.md --jq .content | base64 -d`); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#00897b; color:white; border:none; padding:0.4em 0.8em; border-radius:4px; cursor:pointer; font-size:0.9em; margin-right:0.5em;">&#128203; copy fetch command</button><button onclick="navigator.clipboard.writeText(&apos;https://bhanneke.github.io/RISE/skills/ai-asset-pricing/wrds-ssh/&apos;); this.textContent=&apos;&#x2713; copied&apos;;" style="background:#fff; color:#333; border:1px solid #ccc; padding:0.4em 0.7em; border-radius:4px; cursor:pointer; font-size:0.9em;">&#128279; share link</button></div><div style="margin-top:0.6em; font-size:0.9em;"><a href="https://github.com/Alexander-M-Dickerson/ai-asset-pricing/blob/main/.claude/skills/wrds-ssh/SKILL.md" target="_blank" rel="noopener">&#8599; view SKILL.md on source</a> &middot; <img src="https://img.shields.io/github/stars/Alexander-M-Dickerson/ai-asset-pricing?style=flat" alt="GitHub stars" style="vertical-align:middle;"></div></div>

## WRDS SSH Connection Skill

This skill provides guidance on connecting to and working with WRDS (Wharton Research Data Services) servers via SSH.

### Examples

- `/wrds-ssh` -- connect to WRDS and explore the server
- `/wrds-ssh submit analysis.sas` -- upload and submit a SAS job
- `/wrds-ssh download ~/scratch/output.csv` -- transfer results back

### Connection

The SSH connection to WRDS is pre-configured. Connect using:

```bash
ssh wrds
```

This connects to the WRDS cloud server (`wrds-cloud-sshkey.wharton.upenn.edu`) via the `~/.ssh/config` host alias.

### WRDS Paths

- **Home directory:** `~` (on WRDS)
- **Scratch directory:** `~/scratch` (symlink — see CLAUDE.md setup instructions)

All SSH commands use single quotes to avoid local shell expansion. Paths like `~/scratch/` expand on the remote side.

### Running Commands on WRDS

#### Interactive Session

For quick commands or testing:

```bash
ssh wrds "command_here"
```

#### Running SAS Code

**IMPORTANT:** On WRDS Cloud, you cannot run `sas` directly. You must use `qsas` which submits jobs to the Grid Engine queue. Jobs run asynchronously.

**Step 1: Create the SAS program file on WRDS:**
```bash
ssh wrds 'cat > ~/scratch/myprogram.sas << EOF
options nonotes nosource;
proc contents data=crsp.dsf; run;
EOF'
```

**Step 2: Submit the job:**
```bash
ssh wrds 'qsas ~/scratch/myprogram.sas'
```
This returns immediately with a job ID (e.g., `Your job 12345678 ("myprogram.sas") has been submitted`).

**Step 3: Wait for completion and check output:**
```bash
## Check if job is still running
ssh wrds 'qstat -u $(whoami)'

## Once complete, check the log for errors
ssh wrds 'tail -50 ~/scratch/myprogram.log'

## View the listing output
ssh wrds 'cat ~/scratch/myprogram.lst'
```

**Output files:** SAS creates `.log` and `.lst` files in the same directory as the `.sas` file.

**NOTE:** The `-sync y` option does NOT work on WRDS Cloud. Jobs are always asynchronous. Use `sleep` or poll `qstat` to wait for completion.

#### Running SQL Queries (PostgreSQL)

> **Note:** Direct local `psql service=wrds` is always preferred over SSH-tunneled psql. The SSH SQL examples below are a fallback for when local psql is not available. The specialist agents (crsp-wrds-expert, optionmetrics-wrds-expert) always use local psql.

Use `psql` directly with `~/.pgpass` for automatic authentication:
```bash
## Single query
psql service=wrds \
    -c "SELECT * FROM crsp.dsf WHERE date > '2025-01-01' LIMIT 10;"

## Output to CSV
psql service=wrds \
    -c "COPY (SELECT * FROM optionm.securd LIMIT 100) TO STDOUT WITH CSV HEADER" > output.csv
```

**Via SSH (fallback):**
```bash
ssh wrds "psql -h wrds-pgdata.wharton.upenn.edu -d wrds -c 'SELECT * FROM crsp.dsf LIMIT 10;'"
```

#### Running Python Code

```bash
ssh wrds 'qpython ~/myscript.py'
```

### File Transfer

#### Upload files to WRDS

```bash
scp local_file.sas wrds:~/scratch/
```

#### Download files from WRDS

```bash
scp wrds:~/scratch/results.csv ./
```

#### Bulk transfer with rsync

```bash
rsync -avz wrds:~/scratch/output/ ./local_output/
```

### WRDS Directory Structure

| Path | Purpose | Notes |
|------|---------|-------|
| `~` | Home directory | Permanent storage, limited quota |
| `~/scratch` | Scratch space (symlink) | Large temporary storage, auto-deleted after 48 hours |
| `/wrds/` | Data libraries | SAS libraries for all WRDS databases |

### Common SAS Libraries on WRDS

| Library | Database |
|---------|----------|
| `crsp` | CRSP Stock/Index |
| `comp` | Compustat |
| `optionm` | OptionMetrics |
| `taq` | TAQ Monthly |
| `taqmsec` | TAQ Millisecond |
| `ibes` | I/B/E/S |
| `tfn` | Thomson Reuters |
| `wrdsapps` | WRDS-created linking tables |

### Best Practices

#### 1. Use Scratch Space for Large Files
Always write large intermediate files to `~/scratch/` rather than home directory.

#### 2. Check Job Status
After submitting a batch job:
```bash
ssh wrds "qstat"
```

#### 3. Use Screen for Long Sessions
For long-running interactive sessions:
```bash
ssh wrds "screen -S mysession"
```

Detach with `Ctrl+A, D`. Reattach with:
```bash
ssh wrds "screen -r mysession"
```

#### 4. Download Only Processed Results
Never download raw WRDS data. Process on the server and download only aggregated results.

#### 5. Compress Before Transfer
```bash
ssh wrds 'gzip ~/scratch/large_file.csv'
scp wrds:~/scratch/large_file.csv.gz ./
```

### Example Workflow

**Option A: Upload existing SAS file**
```bash
## 1. Upload SAS program
scp analysis.sas wrds:~/scratch/

## 2. Submit job (returns immediately)
ssh wrds 'qsas ~/scratch/analysis.sas'

## 3. Wait and check job status
ssh wrds 'sleep 60 && qstat -u $(whoami)'

## 4. Check log for errors
ssh wrds 'tail -50 ~/scratch/analysis.log'

## 5. View results or download
ssh wrds 'cat ~/scratch/analysis.lst'
scp wrds:~/scratch/results.csv ./
```

**Option B: Create and run SAS code remotely**
```bash
## 1. Create SAS file via heredoc
ssh wrds 'cat > ~/scratch/analysis.sas << EOF
options nonotes nosource;
proc sql;
    create table out as
    select * from crsp.dsf where date > "01JAN2025"d;
quit;
proc export data=out outfile="~/scratch/results.csv" dbms=csv replace; run;
EOF'

## 2. Submit and wait
ssh wrds 'qsas ~/scratch/analysis.sas'
ssh wrds 'sleep 90 && grep -E "ERROR|WARNING|NOTE:.*created" ~/scratch/analysis.log'

## 3. Download results
scp wrds:~/scratch/results.csv ./
```

### Troubleshooting

**Connection timeout:**
- WRDS may be under maintenance; check https://wrds-www.wharton.upenn.edu/

**Permission denied:**
- Verify SSH key is properly configured
- Check that WRDS account is active

**Job stuck in queue:**
- Check queue status: `ssh wrds "qstat -u username"`
- Consider using off-peak hours for large jobs

**Out of disk space:**
- Clean up scratch: `ssh wrds 'rm -rf ~/scratch/temp*'`
- Check quota: `ssh wrds "quota -s"`
