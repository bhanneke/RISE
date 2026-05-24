# 1. Manuscript stack — Overleaf ↔ GitHub

> *Set up a Git-backed manuscript so the agent has something real
> to operate on.*

## Why this step matters

Before adding an agent, give it a real file structure to work in.
The cleanest way to do this for a paper-writing workflow is to make
your manuscript a **Git repository synced to Overleaf**: you keep
writing in Overleaf as usual, but every edit lives in a versioned
GitHub repo that your local agent can read, edit, and commit to.

At the end of this step you will have:

- A GitHub account and one empty (or near-empty) repository for
  your paper.
- An Overleaf account with a project linked to that repository.
- A clone of the repository on your laptop, ready for the agent.

Time: ~15–25 minutes.

---

## 1.1 Create or sign in to GitHub

If you do not already have a GitHub account, go to
[https://github.com/signup](https://github.com/signup) and create
one with your university email.

> ![Screenshot placeholder: GitHub signup page]
> *Drop screenshot at `docs/assets/screenshots/github-signup.png` and replace this line.*

A few tips:

- **Use your university email** if possible — GitHub gives free
  Pro features (private repos, etc.) to academic users via
  [GitHub Education](https://education.github.com).
- **Set up two-factor authentication.** GitHub requires it for any
  account that pushes code; doing it now saves friction later.

---

## 1.2 Create the manuscript repository

In the top-right corner of GitHub, click the **+** button and
choose **New repository**.

- **Repository name:** something short and descriptive, e.g.
  `crypto-momentum-paper`.
- **Visibility:** Private is fine while you are drafting.
- **Initialize with a README:** yes, leave the box checked.

Click **Create repository**.

> ![Screenshot placeholder: GitHub new-repository form]
> *Drop screenshot at `docs/assets/screenshots/github-new-repo.png` and replace this line.*

You should land on the repo's main page. Copy the URL from the
address bar — it will look like
`https://github.com/<your-username>/crypto-momentum-paper`. You will
need it in the next step.

---

## 1.3 Create or sign in to Overleaf

Go to [https://www.overleaf.com](https://www.overleaf.com) and sign
in (or sign up). If your university has an Overleaf institutional
subscription, sign in via your university SSO so the paid features
are available — **the GitHub sync feature requires a paid plan**
(either Overleaf Pro, Overleaf Professional, or an institutional
license that includes it).

> **No paid Overleaf?** You can still follow this guide by writing
> in any local LaTeX editor (TeXShop, VS Code with LaTeX Workshop,
> etc.) and pushing directly to GitHub. The agent steps work
> identically; only the Overleaf round-trip in 1.5 is skipped.

---

## 1.4 Create a project in Overleaf

In Overleaf, click **New Project → Blank Project**.

Give it the same name as your GitHub repository (e.g.
`crypto-momentum-paper`). You will land in the Overleaf editor with
a stub `main.tex`. You can start writing immediately, but the next
step is to wire it to GitHub.

> ![Screenshot placeholder: Overleaf new blank project]
> *Drop screenshot at `docs/assets/screenshots/overleaf-new-project.png` and replace this line.*

---

## 1.5 Connect Overleaf to GitHub

From the Overleaf editor, click the menu icon in the top-left, then
**GitHub** in the side menu. Click **Link GitHub Account**. You
will be sent to GitHub to authorise the integration; click
**Authorize Overleaf** and confirm.

You will be returned to Overleaf with a list of your GitHub
repositories. Pick the one you created in 1.2 (e.g.
`crypto-momentum-paper`) and confirm.

> ![Screenshot placeholder: Overleaf GitHub integration panel]
> *Drop screenshot at `docs/assets/screenshots/overleaf-github-link.png` and replace this line.*

From now on:

- Overleaf shows a **Sync → Push to GitHub** button. Click it after
  any batch of edits you want to send to GitHub.
- GitHub commits made by your agent (or anyone else) appear in
  Overleaf after **Sync → Pull from GitHub**.

Sync is manual, not automatic — this is a feature, not a bug. It
lets you decide when an Overleaf draft is good enough to push, and
when an agent's commit is safe to pull back into your writing
session.

---

## 1.6 Clone the repository locally

Open a terminal on your laptop.

- **macOS:** ⌘+Space, type "Terminal", hit Enter.
- **Windows:** open the Start menu, type "Ubuntu" (if you installed
  WSL) or "PowerShell".
- **Linux:** you know where it is.

Pick a directory to keep your projects in. A common choice is
`~/Projects`:

```bash
mkdir -p ~/Projects
cd ~/Projects
```

Clone the repository (substitute your username and repo name):

```bash
git clone https://github.com/<your-username>/crypto-momentum-paper.git
cd crypto-momentum-paper
ls
```

You should see your repository's files (a `README.md` and, if you
synced Overleaf in 1.5, `main.tex` and friends).

> **Don't have `git` installed?** On macOS, running `git --version`
> the first time will prompt you to install Xcode Command Line
> Tools. On Windows, install [Git for Windows](https://git-scm.com/download/win).
> On Linux, `sudo apt install git` (Debian/Ubuntu) or your
> distribution's equivalent.

---

## What you have now

- A GitHub repository for your paper.
- An Overleaf project synced to it.
- A local clone on your laptop in `~/Projects/<repo-name>`.

This local clone is what the agent will read from and write to.
Keep this terminal window open — you will need it in the next step.

---

## Common pitfalls

- **Overleaf says "GitHub" is not available.** Your Overleaf
  account does not have a paid plan. Either upgrade via your
  institution, or skip Overleaf and write locally — the rest of
  this guide still works.
- **`git clone` says "Permission denied (publickey)".** You tried
  to clone via SSH (`git@github.com:...`) without setting up an SSH
  key. Use the HTTPS URL (`https://github.com/...`) for now;
  GitHub will prompt for credentials on your first push.
- **"fatal: not a git repository".** You ran `git` commands outside
  the cloned directory. Run `cd ~/Projects/<repo-name>` first.

---

Next: [**2. Agent stack — Claude Code or Codex** →](agent.md)
