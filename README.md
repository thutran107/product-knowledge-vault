# Anduin Product Knowledge Vault

You already use AI to write code, draft docs, and answer questions. This vault is the next step: giving your AI agent a **persistent, structured memory** that gets better every time you add something to it.

It's built on three tools — Obsidian (file browser), Claude Code (AI agent), and plain Markdown — and no database, no backend, no server. Everything is a `.md` file on disk.

Here's what you can ask it right now:

```
How is OCR Data Extraction priced, and what's included at each tier?
What's the difference between IDM and FundSub for a new LP onboarding flow?
What has Neuberger Berman deployed, and what does their case study show?
Which Integration Hub setup steps are required before Salesforce sync works?
```

Claude reads the wiki, pulls the relevant pages, and gives a cited answer — tracing every claim back to the source document it came from.

---

## How This Works: The Pattern

This vault is built on a pattern called the **Karpathy wiki method** — named after the approach Andrej Karpathy described for building LLM-powered knowledge bases. The core idea:

> Stop re-deriving. Start compiling.

Instead of searching raw source documents every time you have a question, you run an AI agent over those documents once and extract structured, cross-linked knowledge into a wiki. The wiki compounds — every new source enriches what's already there, surfaces conflicts with what you thought you knew, and connects to everything related.

**The stack:**

| Tool | Role |
|------|------|
| **Obsidian** | Renders the wiki as a navigable, visual knowledge graph. Free desktop app, works offline. |
| **Claude Code** | The AI agent that ingests sources, writes wiki pages, detects conflicts, and answers questions. |
| **Git** | Version control. Every session's changes are tracked; you can diff, revert, or share. |

---

## Starting Point: The Generic Setup

If you're new to Obsidian, the baseline setup is straightforward. Most guides cover these six steps:

```
📁 your-vault/
 ├── 📄 claude.md        ← Minimal rules: how Claude should navigate the files
 ├── 📁 raw/             ← Dump everything here: articles, PDFs, web clips
 └── 📁 wiki/
      ├── 📄 master_index.md
      ├── 📁 topic-one/
      │    └── 📄 index.md
      └── 📁 topic-two/
           └── 📄 index.md
```

1. Download **Obsidian** (obsidian.md — free) and point it at a new folder as your vault
2. Create `raw/` and `wiki/` subfolders
3. Write a `claude.md` rules file telling Claude how to navigate and write
4. Install **Obsidian Web Clipper** (obsidian.md/clipper) and set its save location to `raw/`
5. Install the **Local Images Plus** community plugin so clipped images save locally
6. Ask Claude Code to generate a wiki from whatever's in `raw/`

> **Full walkthrough:** [docs/guide-generic-obsidian-setup.md](docs/guide-generic-obsidian-setup.md)

This works well. It's a fast way to turn a pile of clipped articles into a navigable wiki on any topic. But it hits limits quickly once your knowledge base grows beyond a handful of topics or needs to be reliable enough to share with a team.

---

## The Upgrade: Five Design Decisions

This vault extends the generic pattern with five deliberate changes. Each one addresses a specific failure mode.

---

### 1. Typed entity folders instead of flat topic folders

**Standard approach:** One folder per topic — `wiki/ai-agents/`, `wiki/rag-systems/`. Clean and simple.

**The problem:** Once you have 50+ pages, a flat structure collapses. "What does Neuberger Berman use?" requires navigating through product folders, finding every mention. There's no concept of a *customer*, a *feature*, or a *concept* as a distinct type of thing.

**Decision here:** The `wiki/` folder is divided by entity type, not topic:

```
wiki/
 ├── sources/      ← One page per ingested document (provenance layer)
 ├── products/     ← One page per Anduin product
 ├── features/     ← One page per feature or sub-module
 ├── customers/    ← One page per named customer
 ├── concepts/     ← Cross-cutting patterns: pricing models, compliance requirements
 ├── competitors/  ← One page per competitor
 └── analyses/     ← Filed Q&A answers and comparisons
```

Every entity type has its own namespace. Customers live in `customers/`, always. Products in `products/`, always. Claude knows exactly where to look and what kind of page to create for any new thing it encounters.

---

### 2. CLAUDE.md as a schema, not just navigation rules

**Standard approach:** A short `claude.md` that says "read `master_index.md` first, use wiki-link format, create pages in `wiki/<topic>/`."

**The problem:** With minimal rules, output quality depends entirely on how well you prompt each time. Ask on Monday and you get one page structure. Ask on Friday and you get something completely different. You can't lint it, compare it, or trust it across sessions.

**Decision here:** `CLAUDE.md` is a full schema with:
- **Page templates** — exact frontmatter fields and section headings for every page type. A source page always has `trust_level`, `as_of_date`, `source_type`, and `target_audience`. A product page always has Key capabilities, Pricing & packaging, Implementation notes, Known limitations.
- **Ingest workflow** — a numbered procedure Claude follows every time: read the source, summarize to the user, check for conflicts, wait for confirmation, write pages, update the index and log.
- **Query workflow** — read `index.md` first, read relevant pages, synthesize with citations, signal confidence if fewer than two sources support an answer.
- **Lint workflow** — a health check that catches orphan pages, stale claims, and missing cross-references. Auto-triggers after every fifth ingest.

The schema is what makes the wiki consistent enough to trust. It's the difference between "AI-generated notes" and "a knowledge base."

---

### 3. Source provenance and a trust hierarchy

**Standard approach:** Claude writes a wiki page with claims extracted from sources. The sources aren't tracked separately.

**The problem:** Six months later, a claim on a product page says "pricing starts at $X/month." Is that still true? Which document said that? When was it written? If a newer document says something different, which one wins?

**Decision here:** Every ingest creates a `wiki/sources/<slug>.md` page — a permanent record of the original document with full metadata:

```yaml
type: source
title: "OCR Data Extraction Pricing Guide"
as_of_date: 2025-03-01
source_type: pricing
trust_level: 3          ← derived from the document type hierarchy
original_file: raw/ocr-pricing-guide.md
products: [OCR Data Extraction]
```

And `CLAUDE.md` defines a **document type hierarchy** for resolving conflicts:

| Rank | Type | Notes |
|------|------|-------|
| 1 | Spec / How it works doc | Most authoritative on capability |
| 2 | Implementation Guide / SOP | Authoritative on process |
| 3 | Pricing doc | Authoritative on commercials |
| 4 | FAQ | Reflects real CS/Sales questions |
| 5 | GTM / Sales Deck | Positioning — may simplify |
| ... | ... | ... |
| 12 | Roadmap | Forward-looking — treat as provisional |

When sources conflict, the hierarchy decides which wins. The resolution is logged. Every claim in the wiki traces back to a source page with a trust level and an as-of date.

---

### 4. Structured ingest with conflict detection

**Standard approach:** Drop files in `raw/`, prompt Claude to generate a wiki. It reads the files and writes pages.

**The problem:** Claude doesn't know what it already wrote. Ingesting a second document about the same product can silently overwrite correct information with incorrect information, or create duplicate pages with slightly different names.

**Decision here:** The ingest workflow has five gates before Claude writes anything:

```
raw/your-doc.md
      ↓
  Claude reads & assesses the source
      ↓
  Summarizes to you: what it covers, what's unclear, any conflicts spotted
      ↓
  You confirm (or redirect)
      ↓
  Conflict check: reads existing pages, quotes conflicting claims, asks how to resolve
      ↓
  Deduplication check: finds near-duplicate pages before creating new ones
      ↓
  Writes pages → updates index.md → appends to log.md
```

Nothing gets written until you've seen what Claude found. Conflicts are surfaced explicitly — with the conflicting claims quoted side by side and the trust hierarchy applied — before anything is changed.

---

### 5. Root-level index.md as a structured catalog

**Standard approach:** `master_index.md` lives inside `wiki/`. Claude navigates into `wiki/` to find it.

**The problem:** At scale, Claude needs to scan `master_index.md` on every query to orient itself. Having it one directory deep adds unnecessary navigation. More importantly, a flat list of links doesn't give Claude enough signal to know *which* pages are most relevant before reading them.

**Decision here:** `index.md` lives at the vault root — the first file Claude reads every session. It's a structured, table-formatted catalog organized by entity type:

```markdown
## Sources (54)
| Page | Title | Type | Products | Date |
|------|-------|------|----------|------|
| [[wiki/sources/ocr-pricing-guide]] | OCR Pricing Guide | pricing | OCR Data Extraction | 2025-03 |

## Products (13)
| Page | Title | Status | Sources |
| [[wiki/products/ocr-data-extraction]] | OCR Data Extraction | GA | 11 |
```

Claude can scan this in one pass, identify the three most relevant pages for any query, and go read exactly those — without navigating the folder tree.

---

## What's in This Vault

This vault covers Anduin's full product surface — 13 products, 54 source documents, 17 named customers.

| Product | What it does | Sources |
|---------|-------------|---------|
| **Integration Hub** | Connects Anduin to CRMs (Salesforce, DealCloud, Affinity) and document systems (Box) | 14 |
| **FundSub** | Fund subscription platform for GP/LP subscription workflows | 13 |
| **IDM** | Investor Data Management — centralized investor profile repository | 12 |
| **OCR Data Extraction** | AI-powered digitization of subscription documents using Amazon Textract + human review | 11 |
| **Data Room** | Secure investor document sharing with engagement analytics | 10 |
| **E-signature** | Electronic signing including AES/QES for regulated markets | 1 |
| **AAA (Advisor Advantage)** | GP-side interface for RIA and advisor subscription workflows | 1 |
| **Investor Access** | LP-facing access product | 1 |
| **Investor Portal, Platform, Landing Page, Side Letter, Engagement Hub** | Mapped, awaiting source coverage | 0 |

Also tracked: **17 named customers** (Neuberger Berman, KKR, Blackstone, EQT, and more), **4 third-party integrations**, **8 cross-cutting concepts**.

---

## Navigating the Vault

| File | What it is |
|------|-----------|
| `index.md` | Full catalog of every page, organized by type |
| `wiki/overview.md` | High-level synthesis across all products |
| `wiki/onboarding.md` | Curated must-reads for new CS and Sales hires |
| `log.md` | Every ingest, query, and lint operation, in order |
| `CLAUDE.md` | The full schema: page templates, workflows, domain taxonomy |

**To ask a question**, open Claude Code in this directory and ask naturally:

```
What are the setup requirements for the Salesforce integration?
How does the OCR process work end to end?
What's the difference between AES and QES for e-signature?
```

Claude reads `index.md`, pulls the relevant pages, and responds with citations. If the answer is worth keeping, ask it to file it as an analysis page.

---

## Build Your Own

The schema in `CLAUDE.md` is the part worth stealing. It works for any knowledge-intensive domain — not just product wikis.

| Guide | What it covers |
|-------|---------------|
| [Generic Obsidian + Claude Code setup](docs/guide-generic-obsidian-setup.md) | The six-step baseline: Obsidian, Web Clipper, minimal claude.md |
| [Full vault guide with Web Clipper + ingest patterns](docs/guide-obsidian-claude-code.md) | End-to-end: capture, schema design, ingest, query, maintenance |
