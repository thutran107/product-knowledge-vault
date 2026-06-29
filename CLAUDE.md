# Anduin Product Knowledge Vault — Schema & Operating Rules

This file governs how I (the LLM agent) maintain this wiki. Every session starts here.

---

## 1. Directory Layout

```
/
├── CLAUDE.md              ← This file. Schema and operating rules.
├── index.md               ← Content catalog. Read first on every query.
├── log.md                 ← Append-only chronological record.
├── raw/                   ← Source documents. Drop files here. NEVER modify contents.
│   └── assets/            ← Downloaded images referenced by sources.
└── wiki/                  ← All LLM-generated pages. I own this layer.
    ├── overview.md        ← High-level synthesis of the entire knowledge base.
    ├── onboarding.md      ← Curated must-read list for new CS and Sales hires.
    ├── sources/           ← One page per ingested source document.
    ├── products/          ← One page per Anduin product.
    ├── features/          ← One page per feature or sub-module.
    ├── customers/         ← One page per named customer.
    ├── concepts/          ← Pricing models, implementation patterns,
    │                         compliance requirements, sales motions.
    ├── competitors/       ← One page per known competitor.
    ├── entities/          ← Integration pages only (e.g. DealCloud, Affinity, Box, Salesforce).
    └── analyses/          ← Filed Q&A answers and comparisons.
```

**Rules:**
- `raw/` is immutable. I read from it; I never write to it.
- `wiki/` is entirely mine. I create, update, and delete pages here.
- `index.md`, `log.md`, and `wiki/onboarding.md` are maintained by me at the root/wiki level.
- `wiki/entities/` is reserved for third-party integrations only. Products → `wiki/products/`, customers → `wiki/customers/`, competitors → `wiki/competitors/`.

---

## 2. Page Formats

### Source page (`wiki/sources/<slug>.md`)
```markdown
---
type: source
title: "<full title>"
date_ingested: YYYY-MM-DD
as_of_date: YYYY-MM-DD | undated
source_type: spec | implementation-guide | pricing | faq | sales-deck | gtm-training | cs-training | client-training | case-study | security-whitepaper | sop | release-notes | rfp | roadmap | one-pager | transcript | note
trust_level: 1–10  # derived from §10 document type hierarchy; 1 = most authoritative
original_file: raw/<filename>
products: [Product A, Product B]
target_audience: CS | Sales + RM | Digi | All teams
onboarding_required: Yes | No
tags: [tag1, tag2]
---

## Summary
2–4 sentence executive summary.

## Key Takeaways
- Bullet list of the most important claims or data points.

## Connections
- Links to product, feature, customer, concept, and competitor pages this source informs.
- Notes on how it supports, contradicts, or extends existing wiki pages.

## Conflicts & Supersessions
- Any claims in this source that conflict with existing wiki pages.
- Note which document has higher trust per §10 and how the conflict was resolved.

## Raw Notes
Anything that didn't fit above — quotes, edge cases, questions raised.
```

---

### Product page (`wiki/products/<slug>.md`)
```markdown
---
type: product
title: "<Product Name>"
status: GA | beta | deprecated
source_count: N
last_updated: YYYY-MM-DD
tags: [tag1, tag2]
---

## What it does
1–3 sentence plain-language description of the product's core purpose.

## Key capabilities
- Bullet list of the most important things it enables for customers.

## Pricing & packaging
Summary of pricing model and plan tiers. Note as-of date. Link to pricing source page.

## Implementation notes
Key setup steps, dependencies, and configuration requirements.
Link to implementation guide source page if available.

## Known limitations
Current gaps, caveats, or constraints that CS and Sales should be aware of.

## Features & sub-modules
Links to `[[wiki/features/...]]` pages for capabilities that belong to this product.

## Related customers
Links to `[[wiki/customers/...]]` pages for known deployments.

## Sources
Links to all source pages that inform this product page.

## Related
Links to related products, concepts, and analyses.
```

---

### Feature page (`wiki/features/<slug>.md`)
```markdown
---
type: feature
title: "<Feature Name>"
parent_product: "<Product Name>"
status: GA | beta | deprecated
source_count: N
last_updated: YYYY-MM-DD
tags: [tag1, tag2]
---

## What it does
Plain-language description of this feature's purpose and scope.

## How it works
Key mechanics, configuration options, and workflow steps.

## Use cases
Specific scenarios where this feature is most valuable. Who benefits and how.

## Pricing & availability
Which plans include this feature. Any add-on or tier restrictions.

## Known limitations
Current gaps or caveats.

## Sources
Links to source pages that inform this feature page.

## Related
Links to parent product, related features, concepts, and analyses.
```

---

### Customer page (`wiki/customers/<slug>.md`)
```markdown
---
type: customer
title: "<Customer Name>"
source_count: N
last_updated: YYYY-MM-DD
tags: [tag1, tag2]
---

## Overview
1–2 sentences on who this customer is and their relationship with Anduin.

## Products & features in use
List of Anduin products and features deployed for this customer.
Link to relevant product and feature pages.

## Key facts
- Bullet list of notable details: deal size, use case, deployment specifics, key contacts.

## Case study highlights
If a case study exists, summarize the outcome and key proof points.
Link to the source page.

## Open questions & considerations
Known gaps, customizations, or sensitivities for this account.

## Sources
Links to source pages (case studies, RFPs, training materials) that mention this customer.

## Related
Links to related products, features, and analyses.
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
Plain-language definition.

## Key dynamics
Core mechanics, forces, or patterns. Updated as sources accumulate.

## Evidence & examples
Specific examples drawn from sources, with [[source links]].

## Tensions & open questions
Where sources disagree. What's unresolved.

## Related
Links to related products, features, customers, competitors, and analyses.
```

---

### Competitor page (`wiki/competitors/<slug>.md`)
```markdown
---
type: competitor
title: "<Competitor Name>"
source_count: N
last_updated: YYYY-MM-DD
tags: [tag1, tag2]
---

## Overview
Who this competitor is and what they offer.

## How they compare to Anduin
Key differentiators — where Anduin wins, where the competitor is strong.

## Products that overlap
Which Anduin products compete most directly with this company.

## Known objections & responses
Common objections raised by prospects when comparing to this competitor,
and the recommended Anduin response.

## Sources
Links to source pages that mention this competitor.

## Related
Links to related products, concepts, and analyses.
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
The main finding.

## Evidence
Sources and reasoning, with [[wiki links]] to supporting pages.

## Caveats
What's uncertain or missing.
```

---

## 3. Index Conventions (`index.md`)

The index is a catalog of all wiki pages. Format:

```markdown
# Wiki Index
Last updated: YYYY-MM-DD

## Overview
- [[wiki/overview]] — High-level synthesis of all knowledge in this base.
- [[wiki/onboarding]] — Must-read list for new CS and Sales hires.

## Sources (N)
| Page | Title | Type | Products | Date |
|------|-------|------|----------|------|
| [[wiki/sources/slug]] | Title | sales-deck | IDM, Data Room | YYYY-MM-DD |

## Products (N)
| Page | Title | Status | Sources |
|------|-------|--------|---------|
| [[wiki/products/slug]] | Product Name | GA | N |

## Features (N)
| Page | Title | Parent Product | Sources |
|------|-------|----------------|---------|
| [[wiki/features/slug]] | Feature Name | IDM | N |

## Customers (N)
| Page | Title | Products in Use | Sources |
|------|-------|-----------------|---------|
| [[wiki/customers/slug]] | Customer Name | IDM, Data Room | N |

## Concepts (N)
| Page | Title | Sources |
|------|-------|---------|
| [[wiki/concepts/slug]] | Concept Name | N |

## Competitors (N)
| Page | Title | Sources |
|------|-------|---------|
| [[wiki/competitors/slug]] | Competitor Name | N |

## Analyses (N)
| Page | Title | Date |
|------|-------|------|
| [[wiki/analyses/slug]] | Title | YYYY-MM-DD |
```

**Rules:**
- Read `index.md` first when answering any query — use it to find relevant pages.
- Update `index.md` at the end of every ingest and after filing any analysis.
- Keep counts accurate.
- When the index grows beyond ~50 sources, add a tag-filtered section grouping pages by key tags (e.g., `#pricing`, `#onboarding`, `#compliance`) to enable faster targeted reads.

---

## 4. Log Conventions (`log.md`)

Append-only. Each entry:

```markdown
## [YYYY-MM-DD] <operation> | <title>

**Operation:** ingest | query | lint | note
**Source file:** raw/<filename>  ← ingest operations only
**Document type:** <type>        ← ingest operations only
**Product(s):** <products>       ← ingest operations only
**As-of date:** <date or "undated">  ← ingest operations only
**Conflicts found:** none | <list>   ← ingest operations only
**Summary:** One sentence on what happened.
**Pages touched:** list of wiki pages created or updated.
```

**Rules:**
- Append to `log.md` at the end of every operation.
- Never edit or delete existing log entries.
- One entry per operation.

---

## 5. Ingest Workflow

When the user adds a source and asks me to ingest it:

### Step 1 — Read & assess the source
Read the file from `raw/`. Before extracting anything, assess:
- **Document type** — is this a spec, pricing doc, sales deck, training deck, case study, SOP, whitepaper, or roadmap? (See §10 for trust hierarchy.)
- **Product(s) covered** — which Anduin products does this document address?
- **Target audience** — CS, Sales + RM, Digi, or all teams?
- **As-of date** — when was this last updated? Extract from metadata or document header. If absent, flag as undated.
- **Length** — is this document over ~15 pages / 3,000 words?

### Step 2 — Chunking (for long documents)
If the document exceeds ~15 pages or 3,000 words, do NOT process it as one block. Split by natural sections (headings, slides, chapters) and process section by section. Extract concepts, features, and entities per section, then merge before writing pages. Flag any section that was unclear or incomplete.

### Step 3 — Discuss before writing
Summarize the document to the user in 3–5 bullet points:
- What it covers
- Which products it addresses
- Who the intended audience is
- Any sections that were unclear, missing dates, or seemed outdated
- Any conflicts noticed with existing wiki pages (see Step 4)

Let the user redirect emphasis or flag corrections before anything is written.

### Step 4 — Conflict detection (before writing)
Before creating or updating any wiki page:
1. Check `index.md` for existing product, feature, customer, concept, and competitor pages related to this source's topics.
2. Read those pages.
3. Identify any claims in the new source that contradict existing pages.
4. If conflicts exist, surface them explicitly to the user:
   - Quote the conflicting claims (new source vs. existing page)
   - State which document type has higher trust per §10 hierarchy
   - Ask the user whether to update the existing page, flag it as superseded, or keep both with a tension note

Do not silently overwrite existing claims. Always surface conflicts first.

### Step 5 — Deduplication check (before creating new pages)
Before creating any new page:
1. Search `index.md` for existing pages with the same or similar name in the relevant folder.
2. If a match exists, update that page rather than creating a duplicate.
3. If a near-match exists (e.g. "Investor Portal" vs "Portal"), ask the user which slug to use before proceeding.

### Step 6 — Write the source page
Create `wiki/sources/<slug>.md` using the source page template (§2).
Populate all frontmatter fields including:
- `source_type` — map document type to the closest schema value
- `as_of_date` — from document metadata or header (use "undated" if absent)
- `target_audience` — CS | Sales + RM | Digi | All teams
- `products` — list of Anduin products covered
- `onboarding_required` — Yes / No (from Notion metadata if available)
- `trust_level` — derive from §10 document type hierarchy (1 = highest)

**Slug convention:** `[product]-[document-type]-[optional-qualifier]`
Examples: `fundsub-pricing.md`, `idm-implementation-guide.md`,
`neuberger-berman-case-study.md`, `anduin-security-whitepaper.md`

### Step 7 — Update product, feature, customer, concept, and competitor pages
For each entity extracted from the source:

**Products** — if a `wiki/products/<slug>.md` page exists, update Key capabilities, Pricing & packaging, Implementation notes, or Known limitations as relevant. If no page exists, create one.

**Features** — if a `wiki/features/<slug>.md` page exists, update it. If no page exists and the source introduces a new named feature or sub-module, create one. Link it to its parent product page.

**Customers** — if the source is a case study, RFP, or customer-specific training material, create or update a `wiki/customers/<slug>.md` page. Add the customer to the product page's "Related customers" section.

**Concepts** — if the source introduces or enriches a cross-cutting concept (a pricing model, compliance requirement, implementation pattern, sales motion), create or update a `wiki/concepts/<slug>.md` page.

**Competitors** — if the source mentions a competitor by name with substantive detail (positioning, objections, comparison), create or update a `wiki/competitors/<slug>.md` page.

When updating any page, update `source_count` and `last_updated` in frontmatter.
When a source introduces ambiguity or partial contradiction, add a note to "Tensions & open questions" on the relevant concept page.

### Step 8 — Flag onboarding-required sources
If the source is tagged `onboarding_required: Yes`, add it to `wiki/onboarding.md` under the appropriate section (CS or Sales + RM). This file should always reflect the current canonical must-read list for new hires.

### Step 9 — Update overview, index, and log
- Update `wiki/overview.md` if this source materially shifts the picture of any product, pricing model, or capability.
- Update `index.md` with all new and updated pages; keep counts accurate.
- Append to `log.md` using the full format defined in §4, including source file, document type, products, as-of date, and any conflicts found.

---

### Quick reference — slug conventions

| Page type | Slug pattern | Example |
|-----------|-------------|---------|
| Source — implementation guide | `[product]-implementation-guide` | `idm-implementation-guide` |
| Source — pricing | `[product]-pricing` | `ocr-data-extraction-pricing` |
| Source — sales deck | `[product]-sales-deck` | `investor-portal-sales-deck` |
| Source — GTM training | `[product]-gtm-training` | `integration-hub-gtm-training` |
| Source — CS training | `[product]-cs-training` | `aaa-cs-training` |
| Source — case study | `[customer]-[product]-case-study` | `neuberger-berman-case-study` |
| Source — security whitepaper | `[scope]-security-whitepaper` | `anduin-security-whitepaper` |
| Source — SOP | `[product]-sop` | `ih-sop` |
| Source — FAQ | `[product]-faq` | `investor-access-faq` |
| Product | `[product-name]` | `investor-portal`, `idm`, `fundsub` |
| Feature | `[product]-[feature-name]` | `idm-aml-kyc`, `esignature-qes` |
| Customer | `[customer-name]` | `neuberger-berman`, `kkr`, `antler` |
| Concept | `[concept-name]` | `fund-digitization`, `qes-aes-compliance` |
| Competitor | `[competitor-name]` | `docusign`, `intralinks` |
| Analysis | `[topic]-[qualifier]` | `esignature-vs-docusign`, `idm-pricing-faq` |

---

## 6. Query Workflow

When the user asks a question:

1. **Read** `index.md` to identify relevant pages.
2. **Read** those pages (products, features, customers, concepts, competitors, analyses as relevant).
3. **Synthesize** an answer with citations using `[[wiki/...]]` links.
4. **Signal confidence** — if fewer than 2 source pages support the answer, say so explicitly and suggest what source would fill the gap.
5. **Offer to file** the answer as an analysis page in `wiki/analyses/`. If the user says yes, write it and update `index.md` and `log.md`.

---

## 7. Lint Workflow

When the user asks me to lint the wiki:

### Step 1 — Run all checks

**Graph integrity**
- Orphan pages: find pages with no inbound `[[wikilinks]]` from any other wiki page.
- Broken wikilinks: find `[[links]]` that point to pages that don't exist on disk.

**Catalog completeness**
- Index completeness: compare all `.md` files under `wiki/` against entries in `index.md`. Flag any page missing from the index.
- Missing entity pages: find products, features, or customers mentioned in any wiki page but lacking their own page under the appropriate folder.

**Schema conformance**
- Frontmatter validation: every wiki page must have all required frontmatter fields for its type (see §2). Flag missing or blank fields.
- Tag audit: list all tags in use across the wiki. Flag any tag not in the preferred tag list defined in §8.

**Freshness and drift**
- Stale claims: find entity or feature pages whose `last_updated` date is more than 90 days older than the `as_of_date` of any source page that covers the same products. Flag as candidates for re-synthesis.
- Source drift: for any file in `raw/` that has a `sha256:` frontmatter field, recompute the hash and flag mismatches. Raw files are immutable — a mismatch means the file was modified after ingest.

**Epistemic quality**
- Contradictions: find pages on the same topic with conflicting claims. Surface all pages with `contested: true` in frontmatter for user review.
- Quality signals: list all pages with `confidence: low`. Also flag any entity page with `source_count: 1` and no `confidence` field — these are fragile and need corroboration or an explicit confidence rating.
- Data gaps: for each product page, note which source types are absent (e.g., no pricing doc, no implementation guide) and flag as gaps.

**Operational hygiene**
- Page size: flag any wiki page over 200 lines as a candidate for splitting.
- Missing cross-references: flag related pages that do not link to each other (e.g., a feature page not linked from its parent product page).
- Log rotation: if `log.md` exceeds 500 entries, prompt the user to rotate it (archive the oldest entries to `log-archive-YYYY.md`).

### Step 2 — Report findings

Group findings by severity:

| Severity | Category |
|---|---|
| Critical | Broken wikilinks |
| High | Orphan pages, index gaps, missing entity pages |
| Medium | Source drift, contested pages, frontmatter errors |
| Low | Stale content, quality signals, data gaps |
| Style | Page size, missing cross-references, tag violations |

Report specific file paths and suggested actions for each finding. Ask the user which issues to fix before changing anything.

### Step 3 — Fix approved issues

Fix approved issues, update `index.md`, append to `log.md`:

```
## [YYYY-MM-DD] lint | N issues found
```

### Auto-trigger rules

Run a lint automatically:
- After every 5th ingest.
- Whenever a `trust_level: 1–3` source (spec, implementation guide, or pricing doc) is ingested.

---

## 8. Naming & Linking

- All internal links use Obsidian wiki-link format with the target path **relative to `wiki/`** (no `wiki/` prefix): `[[products/idm]]`.
- Display text can differ: `[[products/idm|IDM]]`.
- Note: paths are relative to the `wiki/` root so the link graph resolves in knowledge-graph tooling and in an Obsidian vault rooted at `wiki/`. (Earlier pages used a `[[wiki/...]]` prefix; normalized 2026-06-23.)
- Slugs: lowercase, hyphens only, descriptive.
- Tag taxonomy is open — add tags as needed, but reuse existing tags before creating new ones.
- **Frontmatter tags are bare tokens — never prefix with `#`.** The `#x` notation below names a tag conceptually, but in a YAML `tags: [...]` flow sequence a `#` is read as a comment indicator and silently eats the rest of the line (including the closing `]`), breaking the frontmatter. Write `tags: [pricing, onboarding]`, not `tags: [#pricing, #onboarding]`. (23 pages were de-hashed 2026-06-29.)
- Preferred tags: `pricing`, `onboarding`, `compliance`, `implementation`, `security`, `sales-motion`, `case-study`, `competitive`, `integration`, `digitization`.
- `target_audience` is pipe-delimited and ordered `CS | Sales + RM | Digi | All teams` (use only the values that apply). Never comma-delimit.

---

## 9. Session Start

At the start of any session:
1. Read this file (`CLAUDE.md`).
2. Read `index.md` to understand the current state of the wiki.
3. Read the last 5–10 entries in `log.md` to understand recent activity.
4. **Bootstrap check** — if `index.md` does not exist, create it with the empty template from §3. If `log.md` does not exist, create it as an empty file. If `wiki/onboarding.md` does not exist, create it with two empty sections: "CS must-reads" and "Sales + RM must-reads".
5. Confirm ready. Ask what the user wants to do.

---

## 10. Domain

**This knowledge base is focused on:** Anduin's internal product knowledge —
the authoritative reference for CS, Sales, and RM teams to understand what
Anduin's products do, how they work, how they're priced, and how to implement,
sell, and support them.

**Primary users:**
- **CS** — need implementation depth, troubleshooting context, feature specifics, and customer-specific configurations.
- **Sales + RM** — need product positioning, competitive differentiation, pricing guidance, and customer-facing narratives.
- **New hires** — onboarding baseline across all products (flag: `onboarding_required: Yes`).

**Decisions and questions this vault should answer:**
- What does [product] do and how does it work?
- How is [product] priced and what's included in each tier?
- How do I implement [feature] for [customer type]?
- What's the difference between [product A] and [product B]?
- What are known limitations or open questions about [feature]?
- What has [customer] used, and what are relevant case study takeaways?
- How does Anduin compare to [competitor] on [capability]?

**Product taxonomy (entity type: product):**
Platform, E-signature, Data Room, Investor Portal, IDM, Integration Hub,
OCR Data Extraction, AAA, Fundsub, Landing Page, Side Letter, Investor Access,
Engagement Hub

**Sub-feature taxonomy (entity type: feature):**
Workflows, SSO, QES/AES, Digitization, AML/KYC, Signature, Data Management,
Data Extraction, Commenting, Investor Access, Branding, API,
Integration Hub, Custom Integration, User & Group, Schwab integration,
Advanced White Labeling, SMTP Integration, Multi-group, Client Portal

**Document type hierarchy — when sources conflict, later as-of date wins.
Within the same date, trust in this order:**

| Rank | Type | Notes |
|------|------|-------|
| 1 | Spec / How it works doc | Most authoritative on capability |
| 2 | Implementation Guide / SOP | Authoritative on process |
| 3 | Pricing doc | Authoritative on commercials |
| 4 | FAQ | Reflects real CS/Sales questions |
| 5 | GTM / Sales Deck | Positioning — may simplify |
| 6 | CS Training / GTM Training | Internal — may omit customer-facing caveats |
| 7 | Client Training Deck/Guide | Customer-facing — may omit internal detail |
| 8 | Security Whitepaper | Authoritative on security claims only |
| 9 | Case Study / Client Feedback | Directional, not prescriptive |
| 10 | Release Notes / One Pager | Additive or summary — narrow scope |
| 11 | RFP | Customer-specific — may not generalize |
| 12 | Internal Roadmap / Roadmap Deck | Forward-looking — treat as provisional |

**Named customers to track as entities:**
Neuberger Berman, KKR, EQT, Blackstone, Hg Capital, Sequoia Heritage,
Clearlake, Atalaya, Audax, Proskauer, Stone Ridge, PAG, Oakley, Antler,
Accolade, NXSTEP, Cerity Partners

**Concept types to watch for:**
pricing models, implementation patterns, onboarding flows,
compliance requirements (QES/AES, AML/KYC, EU Data Residency),
integration patterns, signature workflows, fund digitization,
investor access patterns, product positioning arguments, competitive differentiation
