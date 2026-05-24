# 2. Agent stack — Claude Code or Codex

> *Install a coding agent on your laptop and authenticate it
> against the repository from step 1.*

## Why this step matters

The agent is what turns prompts into changes on disk. Both Claude
Code (Anthropic) and Codex (OpenAI) are terminal-first coding
agents — they run in your shell, read your project's files, edit
them in place, and execute commands on your behalf, asking
permission before each change.

This guide covers both **in parallel**. You only need to install
one to follow the rest of the guide. If you have no preference,
**Claude Code** is the slight default for this knowledge base
because most entries in the [skills catalog](../skills/index.md)
were written for it; Codex works equivalently but its skill
ecosystem is smaller.

At the end of this step you will have:

- A coding agent installed on your laptop.
- Authenticated against your Anthropic or OpenAI account.
- A working first run inside the manuscript repository from
  [step 1](manuscript.md).

Time: ~10–20 minutes (longer if you need to install Node.js or
similar prerequisites).

---

## 2.1 Decide which one

| | Claude Code | Codex |
|---|---|---|
| **Vendor** | Anthropic | OpenAI |
| **Default model family** | Claude (Sonnet / Opus) | GPT (incl. GPT-5 family) |
| **Authentication** | Claude Pro/Max/Team/Enterprise subscription **or** Anthropic Console API key | ChatGPT Plus/Pro/Business/Edu/Enterprise subscription **or** OpenAI API key |
| **RISE skills compatibility** | Most catalog skill packs target Claude Code | Compatible with provider-agnostic skill packs only |
| **Pricing if billed via API** | Per-token (Anthropic API rates) | Per-token (OpenAI API rates) |

If you already have a paid Anthropic or ChatGPT subscription, the
"sign in with subscription" path is the smoother default. API-key
billing is per-token and harder to forecast.

---

## 2.2 Install Claude Code

> Authoritative source:
> [code.claude.com/docs/en/quickstart](https://code.claude.com/docs/en/quickstart).

### macOS / Linux / WSL — native installer (recommended)

In your terminal:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Restart your terminal or run `exec $SHELL` so the new `claude`
command is on your path. Verify:

```bash
claude --version
```

> ![Screenshot placeholder: terminal output of `claude --version`]
> *Drop screenshot at `docs/assets/screenshots/claude-version.png` and replace this line.*

### macOS — Homebrew alternative

```bash
brew install --cask claude-code
```

### Windows — PowerShell

```powershell
irm https://claude.ai/install.ps1 | iex
```

(WinGet alternative: `winget install Anthropic.ClaudeCode`.)

### First run + login

From your terminal, navigate into the manuscript repository from
[step 1](manuscript.md) and start Claude Code:

```bash
cd ~/Projects/crypto-momentum-paper
claude
```

On first run, Claude Code prints a URL and opens your browser. Log
in with your Claude or Anthropic Console account and click
**Allow**. Return to the terminal — you should see a welcome
screen.

> ![Screenshot placeholder: Claude Code welcome screen after login]
> *Drop screenshot at `docs/assets/screenshots/claude-welcome.png` and replace this line.*

Type a smoke-test prompt:

```text
what does this repository contain?
```

Claude Code reads your files, prints a short summary, and waits for
the next instruction. Type `/exit` (or Ctrl+D) to leave the
session; your authentication is saved.

---

## 2.3 Install OpenAI Codex (alternative)

> Authoritative source:
> [github.com/openai/codex](https://github.com/openai/codex).

### macOS / Linux — curl installer

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

### macOS — Homebrew alternative

```bash
brew install --cask codex
```

### Windows — PowerShell

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

### npm alternative (any OS, requires Node.js ≥ 20)

```bash
npm install -g @openai/codex
```

### First run + login

From your terminal, navigate into the manuscript repository and
start Codex:

```bash
cd ~/Projects/crypto-momentum-paper
codex
```

On first run, Codex shows two authentication options:

1. **Sign in with ChatGPT** — uses your Plus / Pro / Business /
   Edu / Enterprise subscription. Browser-based flow.
2. **Use an OpenAI API key** — paste a key from
   [platform.openai.com](https://platform.openai.com/api-keys).

> ![Screenshot placeholder: Codex sign-in screen]
> *Drop screenshot at `docs/assets/screenshots/codex-signin.png` and replace this line.*

Pick the subscription path if you have one. After login, try the
smoke test:

```text
what does this repository contain?
```

Codex reads your files and replies. Press Ctrl+C twice (or type
`exit`) to leave; auth is saved.

---

## 2.4 Set a budget cap

Whichever agent you chose, set a billing cap **before** you do
serious work. Both providers let you do this in two clicks.

- **Anthropic Console** —
  [console.anthropic.com](https://console.anthropic.com/) → Plan &
  Billing → **Spend Limits** → set a monthly cap.
- **OpenAI Platform** —
  [platform.openai.com](https://platform.openai.com/account/billing/limits) →
  Billing → **Usage limits** → set a hard cap.

A first-month cap of US $20–50 is plenty for the workflows in this
guide and saves you from runaway loops.

---

## What you have now

- Either Claude Code or Codex installed and authenticated.
- A working first conversation inside your manuscript repository.
- A spending cap configured.

The agent can already read every file in the repo. It cannot yet
do anything *useful* with them — that is the next step.

---

## Common pitfalls

- **`claude: command not found` after install.** Restart your
  terminal. If it still fails, your `PATH` does not include the
  install location — the install script printed it; either source
  your shell config (`source ~/.zshrc`) or add it manually.
- **`npm: command not found`** (Codex via npm path). Install
  Node.js ≥ 20 first: macOS `brew install node`; Linux via your
  distribution's package manager; Windows from
  [nodejs.org](https://nodejs.org).
- **Login browser opens but never returns to terminal.** Make sure
  you completed the **Allow** confirmation on the browser page,
  then return to the terminal — the prompt updates within a few
  seconds. If it hangs, kill the agent (Ctrl+C) and try `claude`
  or `codex` again.
- **Agent reports "API key not configured" inside an organisation
  account.** Your subscription may be on a workspace you have not
  switched to. In Claude Code: `/login` and pick the right account.
  In Codex: restart with `codex --login`.
- **Agent runs but every edit asks for permission.** That is by
  design. After a few edits you will trust certain operations
  (running tests, reading PDFs); you can grant standing permission
  per tool, but resist the urge to enable "accept all" until you
  know the agent.

---

Next: [**3. First workflow — turn a PDF into a curator note** →](first-workflow.md)
