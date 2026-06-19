# Graph Report - .  (2026-06-19)

## Corpus Check
- 161 files · ~99,999 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 179 nodes · 595 edges · 11 communities detected
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 40 edges (avg confidence: 0.77)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Fundsub` - 75 edges
2. `Anduin Product Knowledge Library — Overview` - 55 edges
3. `Investor Data Management (IDM)` - 35 edges
4. `Investor Portal` - 35 edges
5. `Data Room` - 34 edges
6. `Integration Hub` - 28 edges
7. `Competitive Intel Tracking Table` - 24 edges
8. `Investor Onboarding Workflow` - 21 edges
9. `Neuberger Berman` - 20 edges
10. `Integration Patterns` - 19 edges

## Surprising Connections (you probably didn't know these)
- `Investor Access` --semantically_similar_to--> `Investor Data Management (IDM)`  [INFERRED] [semantically similar]
  wiki/products/investor-access.md → wiki/competitors/passthrough.md
- `Data Mapping` --semantically_similar_to--> `Configuration vs Permission Model`  [INFERRED] [semantically similar]
  wiki/concepts/data-mapping.md → wiki/concepts/configuration-vs-permission.md
- `Retrieve Subscription Data (DealCloud)` --semantically_similar_to--> `CRM Integration Playbook`  [INFERRED] [semantically similar]
  wiki/sources/retrieve-subscription-data.md → wiki/concepts/crm-integration-playbook.md
- `Theme Customization for FundSub and Data Room — Internal Guide` --semantically_similar_to--> `GTM Enablement — Investor Portal Customer Training Guide (Oct 2025)`  [INFERRED] [semantically similar]
  wiki/sources/fundsub-dataroom-theme-customization.md → wiki/sources/investor-portal-customer-training-guide.md
- `IH Knowledge Hub — Guide to All Available Implementations` --semantically_similar_to--> `IH SOP`  [INFERRED] [semantically similar]
  wiki/sources/ih-knowledge-hub.md → wiki/sources/ih-sop.md

## Hyperedges (group relationships)
- **Fund admins building in-house onboarding** — nav, flow, dynamo [INFERRED 0.85]
- **AI-native / LP-side entrants** — juniper-square, vantager, daphne, blueflame-ai [INFERRED 0.80]
- **Side-letter / MFN rivals** — ontra, pro-vision, carta, kirkland-ellis [INFERRED 0.80]

## Communities

### Community 0 - "Data Room & IDM Core"
Cohesion: 0.11
Nodes (38): AAA — Product x CS Demo + Training (Jan 2026), Accolade Partners, Anduin Object Model, Configuration vs Permission Model, Configuration vs Permission (source), CRM Integration Playbook, Data Room, Data Room - Customer Setup Guide for API Access to DR (+30 more)

### Community 1 - "FundSub & Integration Hub"
Cohesion: 0.17
Nodes (29): Affinity, Anduin Investor Guide (LP-Facing, Jan 2026), Automated Data Room Insights Retrievals (DealCloud), Automated Document Repository (Box), Automated Onboarding with FundSub — DealCloud (Primary Investor), Box, Data Management, Data Mapping (+21 more)

### Community 2 - "Competitive Intelligence"
Cohesion: 0.17
Nodes (29): Backstop, BiteStream (Investor Pointe), BlueFlame.ai, Carta, Competitive Intel Tracking Table, Competitive Win/Loss Patterns, Competitor Landscape Watchlist, Competitor Pricing Benchmarks (+21 more)

### Community 3 - "Investor Portal & Engagement Hub"
Cohesion: 0.2
Nodes (27): AtomInvest, bunch, Engagement Hub, Branded Landing Pages, Engagement Hub / Branded Landing Page — Naming History (internal Slack), Engagement Hub naming: Branded Landing Page repackaged as one of four EH features, Anduin Engagement Hub — One Pager, Engagement Hub — Pricing Proposal (+19 more)

### Community 4 - "E-signature & AAA"
Cohesion: 0.26
Nodes (20): AAA (Advisor Advantage), Assign/Unassign Subscriptions to Advisor Entities, AAA — Feature: Advisor's Tags for GP to Communicate with RIAs, AAA GTM Training (Nov 2024), AAA (Advisor Advantage) — Product Brief, AAA (Advisor Advantage) — Sales Deck (Demo Screens), Cerity Partners, DocuSign (+12 more)

### Community 5 - "Customers"
Cohesion: 0.22
Nodes (17): Antler, Atalaya, Audax, Blackstone, Clearlake, EQT, FundSub — Anduin Essentials Sales Deck, Hg Capital (+9 more)

### Community 6 - "OCR Data Extraction"
Cohesion: 0.24
Nodes (15): AAA (Advisor Advantage) — User Guide (RIA User Guide), OCR Data Extraction, Data Extraction Sales Deck, OCR-FundSub Process Client Training, Data Extraction - GTM Training, Data Extraction - Implementation Guide, OCR Implementation Journey, OCR/AI Managed Services - Sales Deck (+7 more)

### Community 7 - "Arcesium (watchlist)"
Cohesion: 1.0
Nodes (1): Arcesium

### Community 8 - "Mantle Portal (watchlist)"
Cohesion: 1.0
Nodes (1): Mantle Portal

### Community 9 - "Altruist (watchlist)"
Cohesion: 1.0
Nodes (1): Altruist

### Community 10 - "Techquity (watchlist)"
Cohesion: 1.0
Nodes (1): Techquity

## Knowledge Gaps
- **24 isolated node(s):** `Engagement Hub naming: Branded Landing Page repackaged as one of four EH features`, `Why Portal AUM table retained despite EH supersession`, `Data Extraction - Pricing Guide`, `Data Room - Multiple Group Internal Training Video`, `Integration Hub Implementation Guide (PDF)` (+19 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Arcesium (watchlist)`** (1 nodes): `Arcesium`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Mantle Portal (watchlist)`** (1 nodes): `Mantle Portal`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Altruist (watchlist)`** (1 nodes): `Altruist`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Techquity (watchlist)`** (1 nodes): `Techquity`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Fundsub` connect `FundSub & Integration Hub` to `Data Room & IDM Core`, `Competitive Intelligence`, `Investor Portal & Engagement Hub`, `E-signature & AAA`, `Customers`, `OCR Data Extraction`?**
  _High betweenness centrality (0.396) - this node is a cross-community bridge._
- **Why does `Anduin Product Knowledge Library — Overview` connect `Customers` to `Data Room & IDM Core`, `FundSub & Integration Hub`, `Competitive Intelligence`, `Investor Portal & Engagement Hub`, `E-signature & AAA`, `OCR Data Extraction`?**
  _High betweenness centrality (0.235) - this node is a cross-community bridge._
- **Why does `Investor Portal` connect `Investor Portal & Engagement Hub` to `Data Room & IDM Core`, `FundSub & Integration Hub`, `Competitive Intelligence`, `Customers`, `OCR Data Extraction`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Fundsub` (e.g. with `Verivend / Veriform` and `Dynamo (InvestHub)`) actually correct?**
  _`Fundsub` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Engagement Hub naming: Branded Landing Page repackaged as one of four EH features`, `Why Portal AUM table retained despite EH supersession`, `Data Extraction - Pricing Guide` to the rest of the system?**
  _24 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Data Room & IDM Core` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._