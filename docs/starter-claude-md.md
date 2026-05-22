# Starter CLAUDE.md

Copy the content below the horizontal rule into a file named `CLAUDE.md` at the root of your vault. Then do three things to make it yours:

1. **Replace the entity type names** — this template uses `topics/`, `organizations/`, `people/`, `concepts/` as the wiki subfolders. Rename them to match your domain. A product knowledge base might use `products/`, `features/`, `customers/`. A legal vault might use `matters/`, `statutes/`, `firms/`.

2. **Fill in your domain taxonomy** — at the bottom of the file, replace the example entity lists with your own: your named topics, organizations, document types. The more specific this is, the better Claude's output.

3. **Adjust the trust hierarchy** — the ranked document type list tells Claude which source wins when two sources contradict each other. Reorder it to match how authoritative different source types are in your domain.

Everything else — the workflows, page templates, index and log conventions — works as-is. Tune it after your first few ingests once you see what Claude produces.

---

---

# Knowledge Vault — Schema & Operating Rules

This file governs how the AI agent maintains this wiki. Read it at the start of every session.

---

## 1. Directory Layout

```
/
├── CLAUDE.md              ← This file.
├── index.md               ← Content catalog. Read first on every query.
├── log.md                 ← Append-only chronological record.
├── raw/                   ← Source documents. Never modify contents.
│   └── assets/            ← Downloaded images referenced by sources.
└── wiki/
    ├── overview.md        ← High-level synthesis of the entire knowledge base.
    ├── onboarding.md      ← Curated must-reads for new team members.
    ├── sources/           ← One page per ingested source document.
    ├── topics/            ← One page per major topic. [RENAME to match your domain]
    ├── organizations/     ← One page per named org, company, or institution. [RENAME]
    ├── people/            ← One page per named person (optional). [RENAME or remove]
    ├── concepts/          ← Cross-cutting definitions, patterns, frameworks.
    └── analyses/          ← Filed Q&A answers and comparisons.
```

**Rules:**
- `raw/` is immutable. Read from it; never write to it.
- `wiki/` is entirely mine. I create, update, and delete pages here.
- `index.md`, `log.md`, `wiki/overview.md`, and `wiki/onboarding.md` are maintained by me.

---

## 2. Page Formats

### Source page (`wiki/sources/<slug>.md`)

```markdown
---
type: source
title: "<full title of the document>"
date_ingested: YYYY-MM-DD
as_of_date: YYYY-MM-DD | undated
source_type: primary-source | research-report | technical-doc | news | blog-post | transcript | interview | internal-note
trust_level: 1–8
original_file: raw/<filename>
topics: [Topic A, Topic B]
tags: [tag1, tag2]
---

## Summary
2–4 sentence executive summary of what this source covers and why it matters.

## Key Takeaways
- Most important claims, data points, or conclusions.
- Keep to 5–8 bullets maximum.

## Connections
- Links to topic, organization, concept, and analysis pages this source informs.
- Note how it supports, contradicts, or extends existing wiki pages.

## Conflicts & Supersessions
- Any claims in this source that conflict with existing wiki pages.
- Note which document has higher trust per §8 and how the conflict was resolved.

## Raw Notes
Anything that didn't fit above — notable quotes, edge cases, follow-up questions.
```

---

### Topic page (`wiki/topics/<slug>.md`)
*Rename this folder to match your domain: `products/`, `subjects/`, `projects/`, etc.*

```markdown
---
type: topic
title: "<Topic Name>"
status: active | archived | emerging
source_count: N
last_updated: YYYY-MM-DD
tags: [tag1, tag2]
---

## What it is
1–3 sentence plain-language description of this topic's scope and significance.

## Key findings
- The most important things we know about this topic.
- Updated as sources accumulate.

## Key dynamics
Core forces, patterns, or mechanisms at work. What drives this topic.

## Open questions
What we don't know yet. What source type would fill the gap.

## Related organizations
Links to `[[wiki/organizations/...]]` pages for entities involved in this topic.

## Sources
Links to all source pages that inform this topic page.

## Related
Links to related topics, concepts, and analyses.
```

---

### Organization page (`wiki/organizations/<slug>.md`)
*Rename this folder to match your domain: `companies/`, `customers/`, `competitors/`, `institutions/`, etc.*

```markdown
---
type: organization
title: "<Organization Name>"
category: company | institution | government | nonprofit
source_count: N
last_updated: YYYY-MM-DD
tags: [tag1, tag2]
---

## Overview
1–2 sentences on who this organization is and why they matter to this knowledge base.

## Key facts
- Bullet list of notable details: size, location, focus areas, key relationships.

## Relevance to tracked topics
How this organization connects to the topics in this vault.
Links to relevant topic pages.

## Notable positions or actions
Specific claims, decisions, or contributions drawn from sources.
Link to source pages with [[wiki/sources/slug]] citations.

## Open questions
Known gaps or unresolved questions about this organization.

## Sources
Links to source pages that mention or focus on this organization.

## Related
Links to related organizations, topics, concepts, and analyses.
```

---

### Person page (`wiki/people/<slug>.md`)
*Optional. Remove this section and the `wiki/people/` folder if you don't need to track individuals.*

```markdown
---
type: person
title: "<Full Name>"
role: "<Title or role>"
affiliated_org: "<Organization>"
source_count: N
last_updated: YYYY-MM-DD
tags: [tag1, tag2]
---

## Who they are
1–2 sentences on this person's role and relevance to the knowledge base.

## Key contributions or positions
Notable claims, work, or decisions attributed to this person in sources.

## Sources
Links to source pages where this person is mentioned.

## Related
Links to their organization, related topics, and analyses.
```

---

### Concept page (`wiki/concepts/<slug>.md`)

```markdown
---
type: concept
title: "<Concept Name>"
source_count: N
last_updated: YYYY-MM-DD
tags: [tag1, tag2]
---

## Definition
Plain-language definition. What this concept means in the context of this vault.

## Key dynamics
Core mechanics, forces, or patterns. How this concept operates in practice.

## Evidence & examples
Specific examples drawn from sources, with [[source links]].

## Tensions & open questions
Where sources disagree. What's unresolved or contested.

## Related
Links to related topics, organizations, concepts, and analyses.
```

---

### Analysis page (`wiki/analyses/<slug>.md`)

```markdown
---
type: analysis
title: "<Analysis Title>"
date: YYYY-MM-DD
tags: [tag1, tag2]
---

## Question
The question or task this analysis addresses.

## Answer / Synthesis
The main finding, stated directly.

## Evidence
Sources and reasoning, with [[wiki/...]] links to supporting pages.

## Caveats
What's uncertain or missing. What source would strengthen this answer.
```

---

## 3. Index Conventions (`index.md`)

```markdown
# Wiki Index
Last updated: YYYY-MM-DD

## Overview
- [[wiki/overview]] — High-level synthesis of the knowledge base.
- [[wiki/onboarding]] — Must-read list for new members.

## Sources (N)
| Page | Title | Type | Topics | Date |
|------|-------|------|--------|------|
| [[wiki/sources/slug]] | Title | research-report | Topic A | YYYY-MM-DD |

## Topics (N)
| Page | Title | Status | Sources |
|------|-------|--------|---------|
| [[wiki/topics/slug]] | Topic Name | active | N |

## Organizations (N)
| Page | Title | Category | Sources |
|------|-------|----------|---------|
| [[wiki/organizations/slug]] | Org Name | company | N |

## Concepts (N)
| Page | Title | Sources |
|------|-------|---------|
| [[wiki/concepts/slug]] | Concept Name | N |

## Analyses (N)
| Page | Title | Date |
|------|-------|------|
| [[wiki/analyses/slug]] | Title | YYYY-MM-DD |
```

**Rules:**
- Read `index.md` first on every query.
- Update `index.md` at the end of every ingest and after filing any analysis.
- Keep counts accurate.
- Once the index exceeds ~50 sources, add a tag-filtered section grouping pages by key tags.

---

## 4. Log Conventions (`log.md`)

Append-only. One entry per operation. Format:

```markdown
## [YYYY-MM-DD] <operation> | <title>

**Operation:** ingest | query | lint | note
**Source file:** raw/<filename>        ← ingest operations only
**Document type:** <type>              ← ingest operations only
**Topics:** <topics>                   ← ingest operations only
**As-of date:** <date or "undated">    ← ingest operations only
**Conflicts found:** none | <list>     ← ingest operations only
**Summary:** One sentence on what happened.
**Pages touched:** list of wiki pages created or updated.
```

Never edit or delete existing log entries.

---

## 5. Ingest Workflow

When a source is added and ingest is requested:

### Step 1 — Read & assess
Read the file from `raw/`. Assess:
- Document type (see §8 for trust hierarchy)
- Topics covered
- As-of date (extract from metadata or content; flag as "undated" if absent)
- Length — is this over ~15 pages or 3,000 words?

### Step 2 — Chunk long documents
If over ~3,000 words, process section by section. Extract entities per section, then merge before writing pages.

### Step 3 — Summarize before writing
Summarize to the user in 3–5 bullets:
- What it covers
- Which topics and organizations it addresses
- Any sections that are unclear, undated, or seem outdated
- Any conflicts noticed with existing wiki pages

Wait for the user to confirm or redirect before writing anything.

### Step 4 — Conflict detection
Before creating or updating any page:
1. Check `index.md` for existing pages related to this source's topics.
2. Read those pages.
3. Identify any claims that contradict existing pages.
4. If conflicts exist, surface them explicitly:
   - Quote the conflicting claims (new source vs. existing page)
   - State which has higher trust per §8
   - Ask the user whether to update, flag as superseded, or keep both with a tension note

Never silently overwrite existing claims.

### Step 5 — Deduplication check
Before creating a new page, search `index.md` for existing pages with the same or similar name. If a match exists, update rather than create. If a near-match exists, ask the user which slug to use.

### Step 6 — Write the source page
Create `wiki/sources/<slug>.md` using the source page template from §2.

**Slug convention:** `[topic]-[document-type]-[optional-qualifier]`
Examples: `ai-agents-research-report.md`, `acme-corp-interview-2025.md`

### Step 7 — Update entity pages
For each entity extracted:
- **Topics** — update or create `wiki/topics/<slug>.md`
- **Organizations** — update or create `wiki/organizations/<slug>.md`
- **People** — update or create `wiki/people/<slug>.md` (if tracking individuals)
- **Concepts** — update or create `wiki/concepts/<slug>.md`

Update `source_count` and `last_updated` in frontmatter on any updated page.

### Step 8 — Update index and log
- Update `wiki/overview.md` if this source materially shifts the picture of any topic.
- Update `index.md` with all new and updated pages.
- Append to `log.md` using the full format from §4.

---

## 6. Query Workflow

When the user asks a question:

1. Read `index.md` to identify relevant pages.
2. Read those pages.
3. Synthesize an answer with `[[wiki/...]]` citations.
4. Signal confidence — if fewer than 2 source pages support the answer, say so explicitly and suggest what source would fill the gap.
5. Offer to file the answer as an analysis page in `wiki/analyses/`. If yes, write it and update `index.md` and `log.md`.

---

## 7. Lint Workflow

When asked to lint:

1. Read all pages in `wiki/`.
2. Check for:
   - Contradictions between pages
   - Stale claims (compare `as_of_date` fields across conflicting sources)
   - Orphan pages (no inbound links)
   - Topics, organizations, or concepts mentioned but lacking their own page
   - Missing cross-references between related pages
   - Pages with `source_count: 1` — flag as fragile (single-source)
   - Data gaps — suggest which source types are missing for each topic
3. Report findings. Ask which issues to fix.
4. Fix approved issues, update `index.md`, append to `log.md`.

**Auto-trigger:** Run lint automatically after every 5th ingest.

---

## 8. Domain Taxonomy

### Entity types tracked

**Topics** — the main subjects this vault covers:
- [Replace with your topics, e.g.: "AI Agents", "RAG Systems", "Vector Databases"]
- [Add as many as needed]

**Organizations** — named entities to track:
- [Replace with your organizations, e.g.: "OpenAI", "Anthropic", "Google DeepMind"]

**Key concepts** — cross-cutting ideas to watch for:
- [Replace with your concepts, e.g.: "context windows", "fine-tuning vs. prompting", "retrieval augmentation"]

### Document type hierarchy

When sources conflict, the source with the **lower rank number** and the **more recent as-of date** wins.

| Rank | Type | Notes |
|------|------|-------|
| 1 | Primary source / official specification | Most authoritative |
| 2 | Peer-reviewed research / formal report | High rigor |
| 3 | Technical documentation | Authoritative on implementation |
| 4 | Journalism / news article | Timely but may simplify |
| 5 | Expert blog post / analysis | Insightful but opinionated |
| 6 | Transcript / interview | First-hand but informal |
| 7 | Social media / forum post | Signal only, low authority |
| 8 | Internal notes | Contextual, not verifiable |

### Naming conventions

| Page type | Slug pattern | Example |
|-----------|-------------|---------|
| Source | `[topic]-[type]-[qualifier]` | `ai-agents-research-report-2025` |
| Topic | `[topic-name]` | `retrieval-augmented-generation` |
| Organization | `[org-name]` | `anthropic`, `openai` |
| Person | `[firstname-lastname]` | `andrej-karpathy` |
| Concept | `[concept-name]` | `context-window-limits` |
| Analysis | `[topic]-[qualifier]` | `rag-vs-fine-tuning-comparison` |

### Tag taxonomy

Reuse existing tags before creating new ones.
Starting set: `#overview`, `#technical`, `#commercial`, `#research`, `#opinion`, `#onboarding`, `#outdated`

---

## 9. Session Start

At the start of every session:
1. Read this file.
2. Read `index.md` to understand the current state of the wiki.
3. Read the last 5 entries in `log.md` to understand recent activity.
4. **Bootstrap check** — if `index.md` does not exist, create it with the empty template from §3. If `log.md` does not exist, create it as an empty file. If `wiki/onboarding.md` does not exist, create it with two placeholder sections.
5. Confirm ready. Ask what the user wants to do.
