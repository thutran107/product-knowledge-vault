# Graph Report - wiki  (2026-06-16)

## Corpus Check
- Corpus is ~44,498 words - fits in a single context window. You may not need a graph.

## Summary
- 140 nodes · 478 edges · 7 communities detected
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 20 edges (avg confidence: 0.78)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Anduin Product Knowledge Library — Overview` - 55 edges
2. `FundSub (Fund Subscription)` - 55 edges
3. `Investor Data Management (IDM)` - 33 edges
4. `Data Room` - 29 edges
5. `Investor Portal` - 28 edges
6. `Integration Hub` - 27 edges
7. `Investor Onboarding Workflow` - 21 edges
8. `Neuberger Berman` - 20 edges
9. `Integration Patterns` - 19 edges
10. `E-signature` - 17 edges

## Surprising Connections (you probably didn't know these)
- `Investor Access` --semantically_similar_to--> `Investor Data Management (IDM)`  [INFERRED] [semantically similar]
  wiki/products/investor-access.md → wiki/products/investor-data-management.md
- `Data Mapping` --semantically_similar_to--> `Configuration vs Permission Model`  [INFERRED] [semantically similar]
  wiki/concepts/data-mapping.md → wiki/concepts/configuration-vs-permission.md
- `Retrieve Subscription Data (DealCloud)` --semantically_similar_to--> `CRM Integration Playbook`  [INFERRED] [semantically similar]
  wiki/sources/retrieve-subscription-data.md → wiki/concepts/crm-integration-playbook.md
- `Theme Customization for FundSub and Data Room — Internal Guide` --semantically_similar_to--> `GTM Enablement — Investor Portal Customer Training Guide (Oct 2025)`  [INFERRED] [semantically similar]
  wiki/sources/fundsub-dataroom-theme-customization.md → wiki/sources/investor-portal-customer-training-guide.md
- `IH Knowledge Hub — Guide to All Available Implementations` --semantically_similar_to--> `IH SOP`  [INFERRED] [semantically similar]
  wiki/sources/ih-knowledge-hub.md → wiki/sources/ih-sop.md

## Hyperedges (group relationships)
- **IDM / Engagement Hub / Investor Portal share one IDM Firm space** — investor-data-management, engagement-hub, investor-portal [EXTRACTED 0.90]
- **Neuberger Berman full-stack deployment** — neuberger-berman, fundsub, investor-data-management, integration-hub, salesforce [EXTRACTED 0.85]
- **Automated Investor Onboarding via Integration Hub** — investor-onboarding-workflow, integration-patterns, import-export-templates, data-mapping, fundsub [EXTRACTED 0.90]
- **Engagement Hub / Portal / IDM Packaging Stack** — product-packaging-bundling, engagement-hub, investor-portal, investor-data-management, engagement-hub-branded-landing-pages [EXTRACTED 0.85]
- **Configuration vs Permission across Anduin apps** — configuration-vs-permission, integration-hub, fundsub, investor-data-management, data-room [EXTRACTED 0.85]
- **Anduin Object Model spans products** — anduin-object-model, fundsub, investor-data-management, data-room, integration-hub [EXTRACTED 0.85]
- **AAA advisor workflow concept stack** — aaa-cs-training, aaa, anduin-object-model, user-roles, configuration-vs-permission [EXTRACTED 0.80]
- **Integration Hub configuration over Anduin Objects** — integration-hub, fundsub, investor-data-management, data-room, anduin-object-model [EXTRACTED 0.90]
- **Import/Export data movement via Templates and Mapping** — data-management, import-export-templates, data-mapping, fundsub [EXTRACTED 0.85]
- **Branded Landing Page repackaged into Engagement Hub** — engagement-hub-naming-history-slack, engagement-hub, engagement-hub-branded-landing-pages, landing-page [EXTRACTED 0.85]
- **Schwab DocuSign Custodian Signing Flow** — esignature-schwab-implementation-guide, esignature-schwab-cerity-training, e-signature, fundsub, cerity-partners [EXTRACTED 0.90]
- **Engagement Hub / Portal / IDM Bundling Strategy** — engagement-hub-product-overview, engagement-hub-pricing, engagement-hub, investor-portal, investor-data-management, product-packaging-bundling [EXTRACTED 0.85]
- **DocuSign QES/SES Signature Offering** — esignature-docusign-qes-faq, esignature-docusign-sales-deck, docusign, qes-aes-compliance [EXTRACTED 0.90]
- **OCR End-to-End Security Pipeline (Textract + Human Review)** — ocr-security-whitepaper-textract, ocr-security-whitepaper-human-augmented, ocr-data-extraction [EXTRACTED 0.90]
- **IDM + FundSub Investor Onboarding Flow** — idm-fundsub-investor-onboarding-may-2025, investor-data-management, fundsub, investor-onboarding-workflow [INFERRED 0.80]
- **CRM Order Creation Integrations into FundSub** — dealcloud, affinity, salesforce, fundsub [INFERRED 0.85]
- **Standalone Investor Portal Competitive Set** — investorflow, atominvest, investor-portal, investor-portal-pricing-faqs-boston [INFERRED 0.80]
- **DocuSign Dual Signing Paths (QES/SES + Schwab)** — docusign, e-signature, qes-aes-compliance, cerity-partners [INFERRED 0.80]

## Communities

### Community 0 - "Engagement Layer & Investor Portal"
Cohesion: 0.21
Nodes (26): Anduin Investor Guide (LP-Facing, Jan 2026), AtomInvest, Engagement Hub, Branded Landing Pages, Engagement Hub / Branded Landing Page — Naming History (internal Slack), Engagement Hub naming: Branded Landing Page repackaged as one of four EH features, Anduin Engagement Hub — One Pager, Engagement Hub — Pricing Proposal (+18 more)

### Community 1 - "IDM & Integration Hub Core"
Cohesion: 0.18
Nodes (25): AAA — Product x CS Demo + Training (Jan 2026), Anduin Object Model, Configuration vs Permission Model, Configuration vs Permission (source), CRM Integration Playbook, IDM - Client Training Deck, IDM Feature Guide Library, IDM - GTM Training (+17 more)

### Community 2 - "FundSub & CRM Onboarding"
Cohesion: 0.23
Nodes (24): Affinity, Automated Data Room Insights Retrievals (DealCloud), Automated Document Repository (Box), Automated Onboarding with FundSub — DealCloud (Primary Investor), Box, Data Management, Data Mapping, DealCloud (+16 more)

### Community 3 - "AAA & E-Signature"
Cohesion: 0.25
Nodes (21): AAA (Advisor Advantage), Assign/Unassign Subscriptions to Advisor Entities, AAA — Feature: Advisor's Tags for GP to Communicate with RIAs, AAA GTM Training (Nov 2024), AAA (Advisor Advantage) — Product Brief, AAA (Advisor Advantage) — Sales Deck (Demo Screens), Cerity Partners, DocuSign (+13 more)

### Community 4 - "Named Customers & Suite Overview"
Cohesion: 0.2
Nodes (18): Antler, Atalaya, Audax, Blackstone, Clearlake, EQT, FundSub — Anduin Essentials Sales Deck, Hg Capital (+10 more)

### Community 5 - "OCR Data Extraction"
Cohesion: 0.23
Nodes (14): AAA (Advisor Advantage) — User Guide (RIA User Guide), OCR Data Extraction, Data Extraction Sales Deck, OCR-FundSub Process Client Training, Data Extraction - GTM Training, Data Extraction - Implementation Guide, OCR Implementation Journey, OCR/AI Managed Services - Sales Deck (+6 more)

### Community 6 - "Data Room"
Cohesion: 0.2
Nodes (12): Accolade Partners, Data Room, Data Room - Customer Setup Guide for API Access to DR, Data Room - Brochure v2, Guide to Data Room Demo Sandbox/Simulator Environment, Data Room - FAQ, Data Room - Multiple Group Internal Training Video, Data Room - Internal Slide on System Limits (+4 more)

## Knowledge Gaps
- **15 isolated node(s):** `Engagement Hub naming: Branded Landing Page repackaged as one of four EH features`, `Why Portal AUM table retained despite EH supersession`, `Data Extraction - Pricing Guide`, `Data Room - Multiple Group Internal Training Video`, `Integration Hub Implementation Guide (PDF)` (+10 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Anduin Product Knowledge Library — Overview` connect `Named Customers & Suite Overview` to `Engagement Layer & Investor Portal`, `IDM & Integration Hub Core`, `FundSub & CRM Onboarding`, `AAA & E-Signature`, `OCR Data Extraction`, `Data Room`?**
  _High betweenness centrality (0.318) - this node is a cross-community bridge._
- **Why does `FundSub (Fund Subscription)` connect `FundSub & CRM Onboarding` to `Engagement Layer & Investor Portal`, `IDM & Integration Hub Core`, `AAA & E-Signature`, `Named Customers & Suite Overview`, `OCR Data Extraction`, `Data Room`?**
  _High betweenness centrality (0.308) - this node is a cross-community bridge._
- **Why does `Investor Data Management (IDM)` connect `IDM & Integration Hub Core` to `Engagement Layer & Investor Portal`, `FundSub & CRM Onboarding`, `AAA & E-Signature`, `Named Customers & Suite Overview`, `OCR Data Extraction`, `Data Room`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Investor Portal` (e.g. with `InvestorFlow` and `AtomInvest`) actually correct?**
  _`Investor Portal` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Engagement Hub naming: Branded Landing Page repackaged as one of four EH features`, `Why Portal AUM table retained despite EH supersession`, `Data Extraction - Pricing Guide` to the rest of the system?**
  _15 weakly-connected nodes found - possible documentation gaps or missing edges._