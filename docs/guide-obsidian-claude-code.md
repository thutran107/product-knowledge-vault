# Building a Knowledge Vault with Obsidian, Web Clipper, and Claude Code

A practical guide to the Karpathy wiki method: capturing raw sources with Obsidian Web Clipper, turning them into a structured wiki with Claude Code, and querying that wiki to get cited answers — all in plain Markdown files on your local machine.

---

## The Idea

Most knowledge management breaks down the same way: you capture things and can never find them again. Search returns noise. Notes go unread. You re-read the same source documents every time you need an answer because nothing has been synthesized into something queryable.

Andrej Karpathy's insight is simple: **stop re-deriving, start compiling.** Instead of searching raw sources every time, you run an AI agent over those sources once and extract structured, cross-linked knowledge into a wiki. The wiki compounds — every new source adds to what's already there, surfaces conflicts with what you thought you knew, and connects to everything related.

The architecture has three layers:

```
raw/          ← Source documents. Drop them in. Never modify them.
wiki/         ← AI-generated pages. Structured, cross-linked, queryable.
CLAUDE.md     ← The schema. Tells the AI what to extract and how.
```

The AI does the bookkeeping. You do the thinking.

This pattern works for any knowledge-intensive domain: internal product documentation, competitive research, legal or compliance reference, engineering architecture notes, academic literature reviews, investment research. The stack is always the same; only the schema changes.

---

## The Stack

| Tool | Role | Cost |
|------|------|------|
| **Obsidian** | Local Markdown viewer, graph view, vault navigation | Free |
| **Obsidian Web Clipper** | Captures web pages and articles directly into `raw/` | Free |
| **Claude Code** | AI agent that ingests sources and maintains the wiki | Claude subscription |
| **Git** | Version control and backup | Free |

No database. No backend. No sync service. Everything is a `.md` file on your local disk.

---

## Part 1: Set Up the Vault

### 1.1 Directory structure

Create the following structure. Every folder has a purpose defined in the schema.

```
your-vault/
├── CLAUDE.md          ← Schema and operating rules for the AI
├── index.md           ← Auto-maintained catalog of all wiki pages
├── log.md             ← Append-only operation log
├── raw/               ← Source documents (AI reads, never writes here)
│   └── assets/        ← Downloaded images referenced by sources
└── wiki/
    ├── overview.md    ← High-level synthesis of the entire knowledge base
    ├── onboarding.md  ← Curated must-reads for new team members
    ├── sources/       ← One page per ingested source document
    ├── topics/        ← One page per major topic or domain concept
    ├── entities/      ← One page per named entity (person, org, product, etc.)
    ├── concepts/      ← Cross-cutting patterns, models, definitions
    └── analyses/      ← Filed Q&A answers and comparisons
```

**Adapt the subfolder names to your domain.** A legal knowledge base might use `matters/` and `statutes/`. A competitive research vault might use `companies/` and `products/`. A personal learning vault might use `books/` and `papers/`. The structure is the schema — name it after how you think about your subject.

The one rule that never changes: **`raw/` is immutable.** The AI reads from it; it never writes to it. Every source document you drop in stays exactly as you put it in.

### 1.2 Write your CLAUDE.md

`CLAUDE.md` is the most important file in the system. It lives at the vault root and instructs Claude Code on how to behave: what page types exist, what their frontmatter looks like, how to run an ingest, how to detect conflicts, and what your domain's entities and taxonomy are.

A complete `CLAUDE.md` needs four sections:

**Directory rules** — what the AI owns (`wiki/`) vs. reads but never modifies (`raw/`). Be explicit: "Never write to raw/."

**Page templates** — exact Markdown frontmatter and section structure for each page type. The more precise these templates are, the more consistent the wiki will be. Vague templates produce vague pages.

**Workflows** — step-by-step instructions for ingest, query, and lint operations. These are the AI's procedures; it follows them literally.

**Domain taxonomy** — the named entity types that exist in your domain, document type hierarchy (which source types are most authoritative when claims conflict), and any domain-specific rules.

> A sample `CLAUDE.md` template is included in the [Appendix](#appendix-sample-claudemd) at the end of this guide.

### 1.3 Bootstrap the vault with Claude Code

Open Claude Code in your vault directory and send this prompt:

```
This is a new knowledge vault. CLAUDE.md defines the schema and operating rules.
Please bootstrap the vault: create index.md using the empty catalog template from
the schema, create log.md as an empty file, and create wiki/onboarding.md with
two placeholder sections. Confirm when done.
```

Claude creates the three bootstrap files. The vault is ready.

### 1.4 Open in Obsidian

1. Open Obsidian → **Open folder as vault** → select your vault root directory
2. Install two community plugins (Settings → Community Plugins → Browse):
   - **Dataview** — lets you query pages by frontmatter fields (e.g., all sources tagged `#pricing`, all entities with status `active`)
   - **Graph View** is built in — enable it to visualize the connection network between pages
3. Verify that internal wiki links like `[[wiki/topics/your-topic]]` resolve in Obsidian's preview

Obsidian is your read layer. You browse and navigate here. You do not edit wiki pages in Obsidian — that is Claude's job.

---

## Part 2: Capture Content with Obsidian Web Clipper

Obsidian Web Clipper is a browser extension that converts web pages to Markdown and saves them directly into your vault. It is the primary capture tool for web-sourced content.

### 2.1 Install

Search "Obsidian Web Clipper" in your browser's extension store (Chrome, Firefox, Safari, and Arc are all supported). Install the extension published by the Obsidian team.

### 2.2 Configure

Open the Web Clipper settings after installing:

**Set the target vault**
The extension detects Obsidian vaults registered on your machine. Select your vault.

**Set the save location**
Set the note save location to `raw`. All clips land in `raw/` by default.

**Set the filename template**
Use a clean, slug-friendly template:

```
{{title}}
```

Or with a date prefix for easier batch sorting:

```
{{date}}-{{title}}
```

**Set the note content template**
This controls the frontmatter and structure of every clipped note. Use this:

```
---
clipped_from: {{url}}
date_clipped: {{date}}
title: "{{title}}"
---

{{content}}
```

The `clipped_from` and `date_clipped` fields give Claude the provenance it needs to populate the `as_of_date` and source metadata fields during ingest.

**Optional: add a processing tag**
Add `status: unprocessed` to the default frontmatter template. This lets you filter in Obsidian for clips that haven't been ingested yet.

### 2.3 Clip content

Navigate to any web page and click the Web Clipper icon in your browser toolbar. The extension shows a preview of the captured content — it usually strips navigation, sidebars, ads, and footers automatically. Review the preview, then click **Save**. The note appears in `raw/` within seconds.

**What clips well:**
- Documentation and help center pages
- Blog posts and articles
- Product or feature announcement pages
- Research papers (HTML versions)
- Forum threads and Q&A posts

**What needs a different approach:**

| Content type | Best capture method |
|-------------|-------------------|
| PDF files | Download directly into `raw/` |
| Notion pages | Export as Markdown (Settings → Export → Markdown & CSV), drop the `.md` file into `raw/` |
| Google Docs | File → Download → Plain Text (`.txt`), rename to `.md`, drop into `raw/` |
| Slack threads or emails | Copy the relevant text into a new `.md` file in `raw/` with a brief frontmatter header noting the source, date, and participants |
| YouTube or video content | Paste the transcript (if available) or your own notes into a `.md` file in `raw/` |

### 2.4 Triage before ingesting

If you clip several pages before sitting down to ingest, a quick triage saves time:

1. Open Obsidian's file browser filtered to `raw/`
2. Scan the titles — delete anything obviously low-quality, off-topic, or already covered
3. Group related clips mentally (three pages about the same topic can be ingested as a batch)
4. Anything you're unsure about: keep it. Claude will tell you if it's redundant.

---

## Part 3: Ingest with Claude Code

Ingesting is the core operation. You point Claude at a file in `raw/`, and it follows the ingest workflow defined in `CLAUDE.md`:

1. Reads and assesses the source
2. Checks `index.md` for conflicts with existing wiki pages
3. Summarizes its findings and surfaces conflicts to you
4. Waits for your confirmation before writing anything
5. Writes or updates all relevant wiki pages
6. Updates `index.md` and appends to `log.md`

### 3.1 Orient Claude at session start

Claude Code reads `CLAUDE.md` and `index.md` at the start of each session automatically. If it doesn't acknowledge the vault context, prompt it:

```
Read CLAUDE.md and index.md to understand the schema and current wiki state.
Confirm when you're oriented and ready.
```

### 3.2 Ingest a single file

```
Ingest raw/your-clipped-article.md
```

Claude responds with a 3–5 bullet summary before writing anything:
- What the source covers
- Which topics or entities it addresses
- Who the intended audience appears to be
- Anything that was unclear, undated, or seems outdated
- Any conflicts with existing wiki pages

**Review this summary before confirming.** If Claude flagged a conflict — for example, a new article that contradicts a claim on an existing wiki page — decide how to resolve it:

```
The new source is more recent and authoritative. Update the wiki page with
the new claim and note that it supersedes the earlier source.
```

Or:

```
Keep both. Add a tension note to the relevant concept page — the evidence
is genuinely mixed and we shouldn't pick a side yet.
```

Once you confirm, Claude writes the pages, updates `index.md`, and appends to `log.md`.

### 3.3 Ingest a batch of related files

When several clips cover the same topic, process them together:

```
Ingest these three files together — they all cover the same topic and
should be cross-referenced:
- raw/article-one.md
- raw/article-two.md
- raw/product-docs-page.md
```

Claude processes them as a set, deduplicates claims, and notes where sources agree or diverge.

### 3.4 Ingest a long document

For documents over ~3,000 words, ask Claude to chunk:

```
Ingest raw/long-report.md — this is a long document.
Process it section by section and check in with me before writing pages.
```

Claude works through each section by heading, summarizing as it goes. This surfaces cases where one section contradicts another and keeps you in the loop on long or complex sources.

### 3.5 What gets created

After a typical ingest you will see:
- A new `wiki/sources/<slug>.md` page — frontmatter, summary, key takeaways, connections to other pages
- Updated or new `wiki/topics/<slug>.md`, `wiki/entities/<slug>.md`, and `wiki/concepts/<slug>.md` pages as applicable
- Updated `index.md` with new and updated entries
- A new entry appended to `log.md`

Open Obsidian's graph view after a few ingests to watch the connection network build.

---

## Part 4: Query the Vault

Once you have at least 5–10 sources ingested, you can ask questions and get structured, cited answers.

### 4.1 Ask a question

Ask naturally in Claude Code:

```
What are the main arguments for [topic]?
How does [A] differ from [B]?
What do we know about [entity]?
What are the known limitations of [approach]?
What sources do we have on [subject]?
```

Claude will:
1. Read `index.md` to identify relevant pages
2. Read those pages
3. Synthesize an answer with `[[wiki/...]]` citations
4. Signal confidence — if fewer than two source pages support the answer, it says so explicitly

That confidence signal is important. A low-confidence answer tells you where your knowledge base has gaps and what kind of source to find next.

### 4.2 File an answer as an analysis

If the synthesized answer is worth keeping — a comparison you'll reference again, a summary you'll share — tell Claude:

```
This answer is worth keeping. File it as an analysis page.
```

Claude writes `wiki/analyses/<slug>.md` with the question, answer, supporting evidence, and caveats, then updates `index.md`.

### 4.3 Querying across sessions

Because `index.md` orients Claude at the start of every session, you can ask follow-up questions days or weeks later and get answers that build on everything previously ingested. The wiki is the persistent memory layer between sessions.

---

## Part 5: Maintain the Vault

### 5.1 Lint regularly

Lint is a health check on the entire wiki. Run it after every 5–10 ingests:

```
Lint the wiki. Check for: contradictions between pages, stale claims
from older sources, orphan pages with no inbound links, entities mentioned
but lacking their own page, and missing cross-references.
```

Claude produces a prioritized issue list. You decide what to fix:

```
Fix the missing cross-references automatically.
For the contradiction on the pricing page, show me both claims before changing anything.
```

### 5.2 Handle superseded sources

When you ingest a newer version of something already in the vault:

```
Ingest raw/updated-report-2025.md — this supersedes the version we
ingested earlier (wiki/sources/report-2024.md). Update all affected pages
and mark the old source as superseded.
```

The old source page is preserved but marked stale. The new source becomes authoritative. The change is logged.

### 5.3 Refresh the overview

After a significant batch of new ingests:

```
Update wiki/overview.md to reflect the current state of the vault.
Several new sources have been added since it was last written.
```

### 5.4 Keep the onboarding page current

`wiki/onboarding.md` is the curated entry point for anyone new to the knowledge base. Review it periodically:

```
Review wiki/onboarding.md. Given everything ingested in the last month,
are there sources that should be added, removed, or reordered?
```

---

## Part 6: Tips and Common Mistakes

**The schema is the product.**
The quality of your `CLAUDE.md` determines the quality of the wiki. Invest time in the page templates and domain taxonomy before you ingest anything. Vague templates produce vague pages. If the AI keeps generating inconsistent output, the fix is almost always in the schema, not the prompts.

**Ingest in small batches, not dumps.**
Drop 3–5 files at a time and review what Claude produces before adding more. The quality of the first 10 pages sets the pattern for everything that follows. A sloppy early ingest creates inconsistencies that compound.

**Conflicts are features, not bugs.**
When Claude surfaces a conflict between a new source and an existing page, that is the system working correctly. An article that contradicts your existing summary means something changed — or one source is wrong. Always resolve conflicts explicitly. Don't let them sit as unresolved tension notes.

**Raw is immutable.**
Never ask the AI to edit anything in `raw/`. If you realize a clip is wrong, delete it and re-clip. The separation between `raw/` and `wiki/` is what makes the system auditable — you can always trace every wiki claim back to a source file.

**Confidence signals matter.**
When Claude says it has fewer than two sources to support an answer, take it seriously. That is a gap. Note what type of source would fill it and go find one.

**Avoid writing wiki pages manually.**
If you find yourself typing facts directly into a wiki page without a source document, stop. That knowledge has no provenance. Find the source, drop it in `raw/`, and ingest it properly. Unsourced claims rot silently and undermine trust in the whole wiki.

**Lint every 5–10 ingests.**
Orphan pages and stale claims accumulate faster than expected. A lint run is 5–10 minutes and keeps the wiki healthy.

---

## Appendix: Sample CLAUDE.md

A minimal template to adapt for any domain. Fill in the bracketed sections with your own page templates, taxonomy, and workflows.

```markdown
# Knowledge Vault — Schema & Operating Rules

## 1. Directory Layout

raw/        ← Source documents. Immutable. I read from here, never write.
wiki/       ← LLM-generated pages. I own this layer entirely.
  sources/  ← One page per ingested source
  topics/   ← One page per major topic (adapt name to your domain)
  entities/ ← One page per named entity (person, org, product, etc.)
  concepts/ ← Cross-cutting patterns and definitions
  analyses/ ← Filed Q&A answers
index.md    ← Content catalog. I read this first on every query.
log.md      ← Append-only operation log.

Rules:
- Never write to raw/.
- wiki/ is entirely mine to create, update, and delete.
- Update index.md and append to log.md after every operation.

## 2. Page Templates

[Define frontmatter fields and section headings for each page type.
Be precise. The AI follows these templates exactly.]

Example source page frontmatter:
  type: source
  title: ""
  date_ingested: YYYY-MM-DD
  as_of_date: YYYY-MM-DD | undated
  source_type: [article | report | documentation | transcript | ...]
  trust_level: 1–10
  original_file: raw/<filename>
  topics: []
  tags: []

## 3. Index Conventions

Format: table per page type with columns for page link, title, type, date.
Keep counts accurate. Read index.md first on every query.

## 4. Log Conventions

Append-only. One entry per operation. Format:
  ## [YYYY-MM-DD] <operation> | <title>
  Operation: ingest | query | lint | note
  Source file: raw/<filename>
  Summary: one sentence.
  Pages touched: list.

## 5. Ingest Workflow

Step 1 — Read & assess the source document
Step 2 — Summarize to user (3–5 bullets) before writing anything
Step 3 — Check index.md for conflicts with existing pages
Step 4 — Surface conflicts; wait for user resolution
Step 5 — Check for duplicate pages before creating new ones
Step 6 — Write wiki/sources/<slug>.md
Step 7 — Create or update topic, entity, and concept pages
Step 8 — Update index.md and append to log.md

## 6. Query Workflow

1. Read index.md to identify relevant pages
2. Read those pages
3. Synthesize answer with [[wiki/...]] citations
4. Signal confidence if fewer than 2 sources support the answer
5. Offer to file as analysis page

## 7. Lint Workflow

Check for: contradictions, stale claims, orphan pages,
missing cross-references, entity mentions without pages.
Auto-trigger after every 5th ingest or when requested.

## 8. Domain Taxonomy

[List your entity types, document type hierarchy, and trust ordering.
Example trust hierarchy — when sources conflict, higher rank wins:
  1. Official specification or authoritative documentation
  2. Implementation guide or process document
  3. Analyst or research report
  4. News article or press release
  5. Forum post or secondary commentary
]
```

---

## Quick Reference

| Task | Claude Code prompt |
|------|--------------------|
| Bootstrap new vault | `Read CLAUDE.md and bootstrap the vault: create index.md, log.md, and wiki/onboarding.md` |
| Ingest one file | `Ingest raw/filename.md` |
| Ingest a batch | `Ingest these files together: raw/a.md, raw/b.md, raw/c.md` |
| Ingest a long document | `Ingest raw/long-doc.md — process section by section and check in before writing` |
| Ask a question | Ask naturally — Claude reads index.md first |
| File an answer | `This is useful. File it as an analysis page.` |
| Lint | `Lint the wiki.` |
| Refresh overview | `Update wiki/overview.md to reflect the current state of the vault.` |
| Supersede an old source | `Ingest raw/new.md — it supersedes wiki/sources/old-slug.md` |
