# Product Knowledge Vault

A structured internal wiki built on **Obsidian** and maintained by **Claude Code** (AI). It serves as the single authoritative reference for CS, Sales, and RM teams — covering what Anduin's products do, how they're priced, how to implement them, and how to sell them.

---

## What is a Knowledge Vault?

A knowledge vault is a local, file-based wiki where every page is a plain Markdown file. You browse and navigate it with Obsidian; you build and maintain it with Claude Code.

The core idea: instead of chasing knowledge across Notion, Google Drive, Slack, and email threads, you drop source documents into one place and let an AI agent extract, synthesize, and cross-link everything into a structured, queryable wiki.

---

## The Stack

| Tool | Role |
|------|------|
| **Obsidian** | Local Markdown viewer and navigator. Renders wiki links, shows the graph view, lets you browse pages without any server. |
| **Claude Code** | AI agent that reads source documents, writes wiki pages, detects conflicts, answers questions, and keeps the index and log up to date. |
| **Git + GitHub** | Version control and backup. Every session's changes are tracked; you can diff, revert, or share. |

No database. No backend. Everything is a `.md` file on disk.

---

## How to Create Your Own Vault

### 1. Set up the directory structure

```
your-vault/
├── CLAUDE.md        ← Schema and operating rules for the AI agent
├── index.md         ← Auto-maintained catalog of all wiki pages
├── log.md           ← Append-only operation log
├── raw/             ← Drop source documents here (never modified)
└── wiki/
    ├── overview.md
    ├── onboarding.md
    ├── sources/     ← One page per ingested document
    ├── products/    ← One page per product
    ├── features/    ← One page per feature
    ├── customers/   ← One page per customer
    ├── concepts/    ← Cross-cutting patterns and models
    ├── competitors/ ← One page per competitor
    └── analyses/    ← Filed Q&A answers
```

### 2. Write your CLAUDE.md

`CLAUDE.md` is the instruction file that tells Claude Code how to behave in this project. It defines:

- **Directory rules** — what Claude owns (wiki/) vs. what it reads but never modifies (raw/)
- **Page templates** — exact Markdown frontmatter and section structure for each page type
- **Ingest workflow** — step-by-step process: read → assess → detect conflicts → deduplicate → write pages → update index and log
- **Query workflow** — how Claude answers questions: read index → read relevant pages → synthesize with citations → offer to file as analysis
- **Domain and taxonomy** — what products, customers, concepts, and competitors exist in your domain

The quality of your CLAUDE.md directly determines the quality and consistency of the wiki. Treat it as the schema definition for your knowledge base.

### 3. Open in Obsidian

Point Obsidian at the vault root as a new vault. Internal links use `[[wiki/products/slug]]` format (Obsidian wiki-link syntax). The graph view maps the connections between pages.

Enable these Obsidian plugins for the best experience:
- **Dataview** — query pages by frontmatter (e.g., all sources tagged `#pricing`)
- **Graph View** — visualize connections between products, customers, and concepts

### 4. Drop source documents into `raw/`

Paste a Notion export, a PDF, a Google Doc export, or a plain `.md` file into `raw/`. Then tell Claude Code:

```
ingest raw/your-document.md
```

Claude will assess the document, surface conflicts with existing pages, ask for your confirmation, then write or update all relevant wiki pages and update the index and log.

### 5. Ask questions

```
How is OCR Data Extraction priced?
What does Neuberger Berman use?
What's the difference between IDM and FundSub?
```

Claude reads the index, pulls the relevant pages, and gives a cited answer. If it's worth keeping, it files it as an analysis page.

---

## Workflow Diagram

```
Source doc (raw/)
      ↓
  Claude reads & assesses
      ↓
  Conflict check against existing wiki pages
      ↓
  User confirms
      ↓
  wiki/sources/<slug>.md  ←  created
  wiki/products/<slug>.md ←  updated
  wiki/features/<slug>.md ←  updated
  wiki/customers/<slug>.md ← updated
  wiki/concepts/<slug>.md ← updated
      ↓
  index.md updated
  log.md appended
```

---

## Tips

- **Trust levels matter.** When two sources conflict, the document type hierarchy in `CLAUDE.md` decides which wins (spec > implementation guide > pricing doc > sales deck > case study). Always surface conflicts before overwriting.
- **Raw is immutable.** Never ask the AI to edit files in `raw/`. It reads from there; it writes to `wiki/`.
- **The log is your audit trail.** Every ingest, query, and lint run is appended to `log.md` with source file, document type, products, as-of date, and any conflicts found.
- **Lint regularly.** Ask Claude to lint the wiki every few weeks — it catches orphan pages, stale claims, and missing cross-references.
- **Onboarding page.** Maintain `wiki/onboarding.md` as a curated must-read list for new team members. It should reflect the current state of the vault, not just what was flagged at ingest time.

---

## About This Vault

This vault contains internal product knowledge for **Anduin** — a fintech platform for fund managers and LPs.

### Products covered (13)

| Product | What it does | Coverage |
|---------|-------------|----------|
| **Integration Hub** | Connects Anduin to CRMs (Salesforce, DealCloud, Affinity) and document systems (Box) | 14 sources |
| **FundSub** | Fund subscription platform for GP/LP subscription workflows | 13 sources |
| **IDM** | Investor Data Management — centralized investor profile repository | 12 sources |
| **OCR Data Extraction** | AI-powered digitization of subscription documents using Amazon Textract + human review | 11 sources |
| **Data Room** | Secure investor document sharing with engagement analytics | 10 sources |
| **E-signature** | Electronic signing including AES/QES for regulated markets | 1 source |
| **AAA (Advisor Advantage)** | GP-side interface for RIA and advisor subscription workflows | 1 source |
| **Investor Access** | LP-facing access product | 1 source |
| **Investor Portal** | LP portal for documents and subscription tracking | 0 sources |
| **Platform** | Core authentication and entity management layer | 0 sources |
| **Landing Page** | Public/authenticated entry point to fund flows | 0 sources |
| **Side Letter** | Investor-specific side letter agreements | 0 sources |
| **Engagement Hub** | Investor engagement product | 0 sources |

### Also tracked

- **17 named customers** — including Neuberger Berman, KKR, Blackstone, EQT, Cerity Partners
- **4 third-party integrations** — DealCloud, Affinity, Box, Salesforce
- **8 cross-cutting concepts** — integration patterns, investor onboarding workflow, CRM integration playbook, data mapping, and more
- **54 source documents** — spanning specs, implementation guides, sales decks, pricing docs, training materials, and case studies

### Primary users

- **CS** — implementation depth, feature specifics, troubleshooting context
- **Sales + RM** — product positioning, competitive differentiation, pricing guidance
- **New hires** — onboarding baseline via `wiki/onboarding.md`

---

## Navigation

| File | Purpose |
|------|---------|
| `index.md` | Full catalog of all pages |
| `wiki/overview.md` | High-level synthesis of all products |
| `wiki/onboarding.md` | Must-reads for new CS and Sales hires |
| `log.md` | Full history of all ingest and query operations |
| `CLAUDE.md` | Schema, templates, and operating rules |
