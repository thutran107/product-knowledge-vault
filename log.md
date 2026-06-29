# Wiki Log

Append-only record of all operations. Format: `## [YYYY-MM-DD] <operation> | <title>`

---

## [2026-06-08] query | Investor Portal vs. Integration Hub

**Operation:** query
**Summary:** Synthesized a comparison of Investor Portal and Integration Hub covering purpose, buyer profile, lifecycle fit, pricing, and competitive positioning. Filed as analysis page.
**Pages touched:** wiki/analyses/investor-portal-vs-integration-hub.md (created), index.md (updated)

---

## [2026-06-08] ingest | Batch 7 — Investor Portal (11 entries + 1 bonus file)

**Operation:** ingest
**Source file:** Notion (11 entries); 7 PPTX files downloaded and converted with markitdown; 2 entries have full Notion content; 3 entries metadata-only
**Document type:** sales-deck (×2), pricing (×1), gtm-training (×3), client-training (×2), spec (×1), implementation-guide (×1), rfp (×1), note (×1)
**Product(s):** Investor Portal (9 sources), FundSub (2 sources)
**As-of date:** 2025-02-21 to 2026-01-01
**Conflicts found:** None
**Summary:** Full Batch 7 ingest. Rich content from 7 downloaded PPTX files. Key additions: complete Investor Portal pricing table by AUM tier (Emerging $6K → Super Whale $30K/fund/yr) from the Boston Popup pricing deck; full product capabilities from the main sales deck (2026 roadmap, financial reporting 3-layer framework, document distribution methods); contact matrix data model spec; CS onboarding training script. Two bonus FundSub entries (investor email support feature, Primary vs. Collaborator distinction) filed under FundSub. Created 2 competitor pages (InvestorFlow, AtomInvest). markitdown installed and used for all PPTX conversions.
**Pages touched:**
- wiki/sources/investor-portal-sales-deck.md (created)
- wiki/sources/investor-portal-pricing-faqs-boston.md (created)
- wiki/sources/investor-portal-gtm-primer.md (created)
- wiki/sources/investor-portal-product-overview.md (created)
- wiki/sources/investor-portal-rfp.md (created, metadata only)
- wiki/sources/investor-portal-prerelease-training-boston.md (created, metadata only)
- wiki/sources/investor-portal-customer-training-guide.md (created)
- wiki/sources/investor-portal-contact-management.md (created)
- wiki/sources/investor-portal-training-materials.md (created, metadata only)
- wiki/sources/anduin-investor-guide-may-2025.md (created)
- wiki/sources/fundsub-investor-email-support.md (created)
- wiki/sources/fundsub-primary-vs-collaborator.md (created)
- wiki/products/investor-portal.md (rebuilt — stub → full product page, source_count 0→9)
- wiki/products/fundsub.md (updated — source_count 13→15, added 2 new sources)
- wiki/competitors/investorflow.md (created)
- wiki/competitors/atominvest.md (created)
- wiki/onboarding.md (updated — Investor Portal sales deck added to Sales + RM must-reads)
- index.md (updated — Sources 60→72, Investor Portal 0→9, FundSub 13→15, Competitors 0→2)

---

## [2026-06-03] ingest | Batch 6 — E-signature (5 of 6 entries)

**Operation:** ingest
**Source file:** Notion (5 entries; entry 6 already ingested in Batch 3)
**Document type:** security-whitepaper (×1), sales-deck (×1), client-training (×1), note (×1), faq (×1)
**Product(s):** E-signature, FundSub
**As-of date:** undated to 2026-01-16
**Conflicts found:** None
**Summary:** Ingested Batch 6 E-signature sources. Rich content from entries 3 (Reuse Signature Pages feature — SES-only post-signing edit capability) and 5 (DocuSign/QES Internal FAQ — comprehensive eIDAS coverage, pricing, security, edge cases). Entries 1/2/4 are metadata-only (Google Drive/Slides links). Entry 6 (Schwab workflow guide) was already ingested in Batch 3. Created qes-aes-compliance concept page and DocuSign entity page. Significantly expanded e-signature product page.
**Pages touched:**
- wiki/sources/esignature-whitepaper.md (created)
- wiki/sources/esignature-docusign-sales-deck.md (created)
- wiki/sources/esignature-reuse-signature-pages.md (created)
- wiki/sources/esignature-sample-signed-documents.md (created)
- wiki/sources/esignature-docusign-qes-faq.md (created)
- wiki/concepts/qes-aes-compliance.md (created)
- wiki/entities/docusign.md (created)
- wiki/products/e-signature.md (rebuilt — source_count 2→7, added QES/AES/SES, DocuSign, reuse signature, Schwab)
- index.md (updated — 5 sources added, Sources 55→60, Concepts 8→9, Integrations 4→5, e-signature 2→7)

---

## [2026-05-12] ingest | FundSub — 4 Google Drive placeholders fetched

**Operation:** ingest
**Source file:** Google Drive (4 files)
**Document type:** implementation-guide (×2), sales-deck (×1), note (×1)
**Product(s):** FundSub, E-signature
**As-of date:** 2024-10 to 2025-06
**Conflicts found:** None
**Summary:** Fetched real content for 4 previously placeholder FundSub source pages from Google Drive. Key new information: Essentials pricing tiers (Starter vs Advanced), Duplicate Fund what's-in/what's-out detail, SMTP two-layer model + port specifics, and One Envelope preparer/signer/DocuSign/signing certificate workflow. Created NXSTEP customer page. Filled FundSub Pricing & packaging section.
**Pages touched:**
- wiki/sources/fundsub-duplicate-fund-config.md (updated — full content)
- wiki/sources/fundsub-email-smtp-implementation-guide.md (updated — full content)
- wiki/sources/fundsub-essentials-sales-deck.md (updated — full content)
- wiki/sources/fundsub-one-envelope-experience.md (updated — full content)
- wiki/products/fundsub.md (updated — Pricing & packaging, Related customers)
- wiki/customers/nxstep.md (created)
- index.md (updated — added NXSTEP, customer count 16→17)

---

## [2026-05-12] ingest | Data Room - Brochure v2

**Operation:** ingest
**Source file:** Google Drive (https://docs.google.com/presentation/d/1St2Bn2TeNjkyoAnbu4lJBPSC8Q2rXTtDDqVx61OoEyY/)
**Document type:** one-pager
**Product(s):** Data Room, FundSub
**As-of date:** 2024-03-01
**Conflicts found:** None
**Summary:** Re-ingested Data Room Brochure v2 from Google Drive source (previously a placeholder). Extracted positioning content, stats, permission model, and Accolade Partners customer quote. Added custom URL / white-label detail to Data Room product page. Created Accolade Partners customer page.
**Pages touched:**
- wiki/sources/data-room-brochure-v2.md (updated — replaced placeholder with full content)
- wiki/products/data-room.md (updated — added custom URL/white-label to Key capabilities)
- wiki/customers/accolade.md (created)
- index.md (updated — added Accolade, customer count 15→16)

---

## [2026-04-20] setup | Initial wiki scaffold

**Operation:** setup
**Summary:** Created CLAUDE.md schema, index.md, log.md, and directory structure (raw/, wiki/sources/, wiki/concepts/, wiki/entities/, wiki/analyses/).
**Pages touched:** CLAUDE.md, index.md, log.md

---

## [2026-04-20] ingest | Batch ingest — all 11 sources in raw/

**Operation:** ingest
**Summary:** Read and digested all 11 markdown source files in raw/. Built 30 wiki pages across sources, entities, concepts, and overview. Domain confirmed as Anduin Integration Hub product knowledge library.
**Pages touched:**
- wiki/overview.md (created)
- wiki/sources/mission-and-core-components.md (created)
- wiki/sources/configuration-vs-permission.md (created)
- wiki/sources/user-role.md (created)
- wiki/sources/data-management.md (created)
- wiki/sources/automated-document-repository.md (created)
- wiki/sources/automated-data-room-insights.md (created)
- wiki/sources/automated-onboarding-fundsub-primary.md (created)
- wiki/sources/investor-onboarding-primary-collaborators.md (created)
- wiki/sources/retrieve-subscription-data.md (created)
- wiki/sources/ih-implementation-guide.md (created)
- wiki/sources/neuberger-berman-case-study.md (created)
- wiki/entities/integration-hub.md (created)
- wiki/entities/fundsub.md (created)
- wiki/entities/data-room.md (created)
- wiki/entities/investor-data-management.md (created)
- wiki/entities/investor-access.md (created)
- wiki/entities/dealcloud.md (created)
- wiki/entities/affinity.md (created)
- wiki/entities/box.md (created)
- wiki/entities/salesforce.md (created)
- wiki/entities/neuberger-berman.md (created)
- wiki/concepts/integration-patterns.md (created)
- wiki/concepts/configuration-vs-permission.md (created)
- wiki/concepts/anduin-object-model.md (created)
- wiki/concepts/import-export-templates.md (created)
- wiki/concepts/user-roles.md (created)
- wiki/concepts/investor-onboarding-workflow.md (created)
- wiki/concepts/crm-integration-playbook.md (created)
- wiki/concepts/data-mapping.md (created)
- index.md (updated)
- log.md (updated)
**Note:** PDFs subsequently ingested in the operation below.

---

## [2026-04-20] ingest | PDF batch — Implementation Guide PDF + Sales Deck PDF

**Operation:** ingest
**Summary:** Extracted text from both PDFs via pdftotext. Implementation Guide PDF is duplicate of markdown already ingested. Sales Deck (Feb 2025) contains significant new content: Salesforce full use case, Prismatic as underlying platform, dummy cards concept, Hub provisioning roadmap, and positioning/value prop language.
**Pages touched:**
- wiki/sources/ih-implementation-guide-pdf.md (created)
- wiki/sources/ih-sales-deck-feb-2025.md (created)
- wiki/entities/integration-hub.md (updated — Prismatic, dummy cards, public landing page, provisioning roadmap)
- wiki/entities/salesforce.md (updated — full bidirectional flow now documented)
- wiki/concepts/integration-patterns.md (updated — Salesforce all-three-patterns, dummy cards)
- index.md (updated — 11 → 13 sources)

---

## [2026-05-04] lint | Backfill — schema alignment after CLAUDE.md updates

**Operation:** lint
**Summary:** Updated all 13 source pages with new frontmatter fields (as_of_date, trust_level, products, target_audience, onboarding_required), remapped source_type from `article` to correct values per §10 hierarchy, added `Conflicts & Supersessions` section to all source pages, created 8 product entity stubs and 13 customer entity stubs per updated domain taxonomy, added Onboarding Essentials section to overview.md, updated index.md.
**Pages touched:**
- wiki/sources/mission-and-core-components.md (updated)
- wiki/sources/configuration-vs-permission.md (updated)
- wiki/sources/user-role.md (updated)
- wiki/sources/data-management.md (updated)
- wiki/sources/automated-document-repository.md (updated)
- wiki/sources/automated-data-room-insights.md (updated)
- wiki/sources/automated-onboarding-fundsub-primary.md (updated)
- wiki/sources/investor-onboarding-primary-collaborators.md (updated)
- wiki/sources/retrieve-subscription-data.md (updated)
- wiki/sources/ih-implementation-guide.md (updated)
- wiki/sources/neuberger-berman-case-study.md (updated)
- wiki/sources/ih-implementation-guide-pdf.md (updated)
- wiki/sources/ih-sales-deck-feb-2025.md (updated)
- wiki/entities/platform.md (created)
- wiki/entities/e-signature.md (created)
- wiki/entities/investor-portal.md (created)
- wiki/entities/ocr-data-extraction.md (created)
- wiki/entities/aaa.md (created)
- wiki/entities/landing-page.md (created)
- wiki/entities/side-letter.md (created)
- wiki/entities/engagement-hub.md (created)
- wiki/entities/kkr.md (created)
- wiki/entities/eqt.md (created)
- wiki/entities/blackstone.md (created)
- wiki/entities/hg-capital.md (created)
- wiki/entities/sequoia-heritage.md (created)
- wiki/entities/clearlake.md (created)
- wiki/entities/atalaya.md (created)
- wiki/entities/audax.md (created)
- wiki/entities/proskauer.md (created)
- wiki/entities/stone-ridge.md (created)
- wiki/entities/pag.md (created)
- wiki/entities/oakley.md (created)
- wiki/entities/antler.md (created)
- wiki/overview.md (updated — Onboarding Essentials section added, source_count corrected)
- index.md (updated — entities 10 → 31, split into Products/Integrations/Customers)

---

## [2026-05-05] note | Schema migration — new wiki folder structure

**Operation:** note
**Summary:** Updated CLAUDE.md to new schema (v2): split wiki/entities/ into wiki/products/, wiki/features/, wiki/customers/, wiki/competitors/; added dedicated page templates for each; expanded source_type enum; enriched log format; added onboarding.md; added slug quick-reference table; added auto-lint trigger rule. Migrated 13 product pages to wiki/products/ and 14 customer pages to wiki/customers/. wiki/entities/ retained for integrations only (DealCloud, Affinity, Box, Salesforce). All cross-references updated. index.md restructured to new format.
**Pages touched:**
- CLAUDE.md (replaced with v2 schema)
- wiki/products/aaa.md (moved from wiki/entities/)
- wiki/products/data-room.md (moved from wiki/entities/)
- wiki/products/e-signature.md (moved from wiki/entities/)
- wiki/products/engagement-hub.md (moved from wiki/entities/)
- wiki/products/fundsub.md (moved from wiki/entities/)
- wiki/products/integration-hub.md (moved from wiki/entities/)
- wiki/products/investor-access.md (moved from wiki/entities/)
- wiki/products/investor-data-management.md (moved from wiki/entities/)
- wiki/products/investor-portal.md (moved from wiki/entities/)
- wiki/products/landing-page.md (moved from wiki/entities/)
- wiki/products/ocr-data-extraction.md (moved from wiki/entities/)
- wiki/products/platform.md (moved from wiki/entities/)
- wiki/products/side-letter.md (moved from wiki/entities/)
- wiki/customers/antler.md (moved from wiki/entities/)
- wiki/customers/atalaya.md (moved from wiki/entities/)
- wiki/customers/audax.md (moved from wiki/entities/)
- wiki/customers/blackstone.md (moved from wiki/entities/)
- wiki/customers/clearlake.md (moved from wiki/entities/)
- wiki/customers/eqt.md (moved from wiki/entities/)
- wiki/customers/hg-capital.md (moved from wiki/entities/)
- wiki/customers/kkr.md (moved from wiki/entities/)
- wiki/customers/neuberger-berman.md (moved from wiki/entities/)
- wiki/customers/oakley.md (moved from wiki/entities/)
- wiki/customers/pag.md (moved from wiki/entities/)
- wiki/customers/proskauer.md (moved from wiki/entities/)
- wiki/customers/sequoia-heritage.md (moved from wiki/entities/)
- wiki/customers/stone-ridge.md (moved from wiki/entities/)
- index.md (restructured to new format with Products/Integrations/Customers/Competitors sections)

---

## [2026-05-11] ingest | Batch ingest — IDM sources from Notion Product Knowledge Library

**Operation:** ingest
**Source file:** notion://database/1973f653-b1df-80b6-a036-000b27bbefb2 (Product Knowledge Library — IDM batch)
**Document type:** mixed (spec, implementation-guide, gtm-training, client-training, one-pager, release-notes, sales-deck)
**Product(s):** IDM, Fundsub (2 cross-product entries)
**As-of date:** varies per source; range undated–2025-09-16
**Conflicts found:** IDM Sales Brochure as-of 2024-08-01 — may be outdated vs. current feature set; noted in source page.
**Summary:** Ingested 9 IDM-tagged entries from the Notion Product Knowledge Library database. Source page frontmatter populated directly from Notion database properties. Content bodies for Notion-linked docs noted (not fully fetched); external Google Slides not fetched.
**Pages touched:**
- wiki/sources/idm-feature-documentation.md (created)
- wiki/sources/idm-implementation-guide.md (created)
- wiki/sources/idm-gtm-training.md (created)
- wiki/sources/idm-client-training.md (created)
- wiki/sources/idm-sales-brochure.md (created)
- wiki/sources/idm-release-notes.md (created)
- wiki/sources/idm-release-notes-sprint-362.md (created)
- wiki/sources/idm-fundsub-onboarding-deck-oct2025.md (created)
- wiki/sources/idm-fundsub-investor-onboarding-may-2025.md (created)
- wiki/products/investor-data-management.md (updated — source_count 3→12, sources list)
- index.md (updated — 13→22 sources, IDM count updated)

---

## [2026-05-11] ingest | Batch ingest — OCR Data Extraction sources from Notion Product Knowledge Library

**Operation:** ingest
**Source file:** notion://database/1973f653-b1df-80b6-a036-000b27bbefb2 (Product Knowledge Library — OCR batch)
**Document type:** mixed (implementation-guide x2, pricing, gtm-training, sales-deck x2, security-whitepaper x2, client-training, spec, note)
**Product(s):** OCR Data Extraction (+ FundSub for 1 cross-product entry)
**As-of date:** varies; range undated–2025-11-13
**Conflicts found:** Data Extraction Sales Deck and OCR/AI Managed Services Sales Deck reference the same Google Slides file (different slide anchors) — noted in both source pages. Pre-May-2025 materials may not reflect new OCR UX.
**Summary:** Ingested 11 OCR-tagged entries from the Notion Product Knowledge Library. Created onboarding.md with CS and Sales + RM must-read lists (2 onboarding-required sources found). Fully rebuilt OCR product page from stub.
**Pages touched:**
- wiki/sources/ocr-implementation-guide.md (created)
- wiki/sources/ocr-implementation-journey.md (created)
- wiki/sources/ocr-pricing-guide.md (created)
- wiki/sources/ocr-gtm-training.md (created)
- wiki/sources/ocr-data-extraction-sales-deck.md (created)
- wiki/sources/ocr-managed-services-sales-deck.md (created)
- wiki/sources/ocr-security-whitepaper-textract.md (created)
- wiki/sources/ocr-security-whitepaper-human-augmented.md (created)
- wiki/sources/ocr-fundsub-process-client-training.md (created)
- wiki/sources/ocr-table-view-how-it-works.md (created)
- wiki/sources/ocr-new-ux-overview.md (created)
- wiki/products/ocr-data-extraction.md (rebuilt — source_count 0→11)
- wiki/onboarding.md (created)
- index.md (updated — 22→33 sources, OCR count 0→11)

---

## [2026-05-11] ingest | Batch 3 — Integration Hub sources from Notion Product Knowledge Library

**Operation:** ingest
**Source file:** notion://database/1973f653-b1df-80b6-a036-000b27bbefb2 (Product Knowledge Library — Integration Hub batch)
**Document type:** note, sop, implementation-guide x2, gtm-training, client-training
**Product(s):** Integration Hub (primary), E-signature, FundSub
**As-of date:** varies; range undated–2026-05-07
**Conflicts found:** none
**Summary:** Ingested 7 Notion entries for Integration Hub; skipped Integration Hub Sales Deck (already exists as ih-sales-deck-feb-2025). Created 6 new source pages. Schwab training source filed under E-signature, not IH — first E-signature source. Created Cerity Partners customer page. Added 3 IH sources to onboarding.md under new All Teams section.
**Pages touched:**
- wiki/sources/ih-intro-overview.md (created)
- wiki/sources/ih-sop.md (created)
- wiki/sources/ih-knowledge-hub.md (created)
- wiki/sources/ih-setup-guide.md (created)
- wiki/sources/ih-smtp-gtm-training.md (created)
- wiki/sources/esignature-schwab-cerity-training.md (created)
- wiki/products/integration-hub.md (updated — source_count 7→12, added 5 sources)
- wiki/products/e-signature.md (updated — source_count 0→1, rebuilt from stub)
- wiki/customers/cerity-partners.md (created)
- wiki/onboarding.md (updated — added All Teams section with 3 IH sources; added IH Sales Deck to Sales + RM)
- index.md (updated — 33→39 sources, IH count 5→12, E-sig count 0→1, customers 14→15)

---

## [2026-05-11] ingest | Batch 4 — FundSub sources from Notion Product Knowledge Library

**Operation:** ingest
**Source file:** notion://database/1973f653-b1df-80b6-a036-000b27bbefb2 (Product Knowledge Library — FundSub batch)
**Document type:** sales-deck, one-pager, implementation-guide x3, note, release-notes
**Product(s):** Fundsub (primary), Data Room (1 cross-product), AAA (1 misfiled entry)
**As-of date:** varies; range 2025-03-01–2025-11-01 (1 undated)
**Conflicts found:** none
**Summary:** Ingested 7 Notion entries listed as FundSub batch. One entry ("Assign/unassign subscriptions to advisor entities") is tagged Product: AAA in Notion — filed under AAA source accordingly. Theme customization guide has full content in Notion (fetched); covers FundSub + Data Room at environment level via iTools. FundSub product page rebuilt from IH-focused stub to proper product template. AAA page updated from zero-source stub. Onboarding: FundSub Essentials Sales Deck added to Sales + RM must-reads.
**Pages touched:**
- wiki/sources/fundsub-essentials-sales-deck.md (created)
- wiki/sources/fundsub-new-lp-view-one-pager.md (created)
- wiki/sources/fundsub-email-smtp-implementation-guide.md (created)
- wiki/sources/fundsub-duplicate-fund-config.md (created)
- wiki/sources/fundsub-one-envelope-experience.md (created)
- wiki/sources/fundsub-dataroom-theme-customization.md (created)
- wiki/sources/aaa-advisor-subscription-assign.md (created)
- wiki/products/fundsub.md (rebuilt — source_count 7→13, full product template)
- wiki/products/aaa.md (updated — source_count 0→1, first source, name updated to "AAA (Advisor Advantage)")
- wiki/onboarding.md (updated — FundSub Essentials Sales Deck added to Sales + RM)
- index.md (updated — 39→46 sources, FundSub 7→13, Data Room 3→4, AAA 0→1)

---

## [2026-05-26] ingest | Internal Guide: How to Set Up Schwab Signature Workflow on Anduin FundSub

**Operation:** ingest
**Source file:** notion://d374318469284220bb201efec79e71be
**Document type:** implementation-guide
**Product(s):** E-signature, FundSub
**As-of date:** 2025-12-15
**Conflicts found:** None. More authoritative than esignature-schwab-cerity-training (trust 2 vs. 7) — complementary, not conflicting.
**Summary:** Ingested the internal CS implementation guide for the Schwab custodian signing workflow. Covers the 5-component setup process (RIA + Anduin DocuSign setup, Schwab addendum via SAC, technical validation, digitization with [Schwab form] filename convention, fund-level DocuSign enablement). Based on Cerity Partners and Blue Arc deployments. Updated e-signature product page with full setup detail and corrected Known limitations (not Cerity-only). Updated Cerity customer page source count.
**Pages touched:**
- wiki/sources/esignature-schwab-implementation-guide.md (created)
- wiki/products/e-signature.md (updated — Implementation notes expanded, Known limitations updated, source_count 1→2)
- wiki/customers/cerity-partners.md (updated — source_count 1→2, second source added)
- index.md (updated — 54→55 sources, E-signature count 1→2)

---

## [2026-05-26] lint | 3 broken wikilinks removed

**Operation:** lint
**Conflicts found:** n/a
**Summary:** Removed 3 broken [[wiki/features/...]] links from source pages Connections sections. Feature pages do not yet exist; links were placeholders with "if page exists" notes. No content lost.
**Pages touched:**
- wiki/sources/data-room-api-implementation-guide.md (removed [[wiki/features/data-room-api]])
- wiki/sources/esignature-schwab-cerity-training.md (removed [[wiki/features/esignature-schwab-integration]])
- wiki/sources/ih-smtp-gtm-training.md (removed [[wiki/features/fundsub-smtp-integration]])

---

## [2026-05-11] ingest | Batch 5 — Data Room sources from Notion Product Knowledge Library

**Operation:** ingest
**Source file:** notion://database/1973f653-b1df-80b6-a036-000b27bbefb2 (Product Knowledge Library — Data Room batch)
**Document type:** faq x2, implementation-guide x4, one-pager, cs-training, release-notes
**Product(s):** Data Room (6 sources), Integration Hub (2 sources — Salesforce → Data Room integration)
**As-of date:** varies; range 2024-03-01–2025-08-25 (2 undated)
**Conflicts found:** none; system limits (3K participants, 50K files) not previously documented in vault — added as new Known Limitations entry.
**Summary:** Ingested 8 Notion entries for the Data Room batch. Two entries ("Automated Onboarding to Data Room from Salesforce") are tagged Integration Hub in Notion — filed under IH sources accordingly. These are complementary: one release notes entry (external dev docs), one full internal CS rollout guide (Salesforce screen flow, Connected App prerequisites, step-by-step setup). Notion content pages fetched for: Data Room FAQ, API Access Guide, Demo Sandbox Guide, and Salesforce IH implementation guide. Data Room product page fully rebuilt from IH-centric stub to comprehensive product template with system limits, API details, notification specs, branding specs, and Salesforce integration notes.
**Pages touched:**
- wiki/sources/data-room-faq.md (created)
- wiki/sources/data-room-brochure-v2.md (created)
- wiki/sources/data-room-api-implementation-guide.md (created)
- wiki/sources/data-room-multi-group-training-video.md (created)
- wiki/sources/data-room-system-limits.md (created)
- wiki/sources/data-room-demo-sandbox-guide.md (created)
- wiki/sources/ih-salesforce-dataroom-release-notes.md (created)
- wiki/sources/ih-salesforce-dataroom-implementation-guide.md (created)
- wiki/products/data-room.md (rebuilt — source_count 4→10, full product template)
- wiki/products/integration-hub.md (updated — source_count 12→14, added 2 Salesforce IH sources)
- index.md (updated — 46→54 sources, Data Room 4→10, IH 12→14)

## [2026-06-09] note | Query Answering Showcase — The Karpathy Method

**Operation:** note
**Summary:** Filed a methodology showcase as an analysis: 5 vault queries + grounded responses (distinct angles) generated on Haiku, selected via a comparative single-elimination tournament (the "Karpathy method" — pairwise judging over absolute scoring). Created at repo root, then moved to wiki/analyses/ at user request with analysis frontmatter.
**Pages touched:**
- wiki/analyses/query-answering-karpathy-method.md (created)
- index.md (updated — Analyses 1→2, last-updated 2026-06-09)

## [2026-06-10] ingest | Engagement Hub (3 sources from Notion Product Knowledge Library)

**Operation:** ingest
**Source file:** raw/engagement-hub-product-overview.md, raw/engagement-hub-pricing-proposal.md, raw/engagement-hub-one-pager.md
**Document type:** spec (Product Overview), pricing (Pricing Proposal), one-pager (Brochure)
**Product(s):** Engagement Hub (3), Investor Portal (2 cross-refs), IDM (1 cross-ref)
**As-of date:** 2026-02-02 (overview), 2025-09-18 (pricing), 2025-08-27 (one-pager)
**Conflicts found:** Investor Portal pricing structure — EH decks (newer, trust-3 pricing 2025-09-18 + spec 2026-02-02) restructure Portal pricing to "annual EH fee + lower per-fund Portal fee," superseding the structure in investor-portal-pricing-faqs-boston (2025-05-14). Per user decision: legacy Portal AUM table RETAINED, conflict FLAGGED on the Portal page (not overwritten); exact new per-fund figures not captured (data gap). Secondary tension: EH tier naming ("Ultimate" vs Starter/Growth/Unlimited).
**Summary:** Engagement Hub stub rebuilt into a full product page from 3 Notion/Drive sources (all backed by Google Slides/PDF, pulled via the Google Drive connector — no separate conversion tooling needed). Per user dedup decision, the standalone "Landing Page" product was FOLDED INTO Engagement Hub: Branded Landing Pages is now a feature page under EH, and wiki/products/landing-page.md became a redirect pointer (status: deprecated). New concept page created for the EH/Portal/IDM packaging & bundling motion. EH priced by # of published landing pages (Starter ≤5 / Growth ≤10 / Unlimited; 30% beta discount). Known data gaps: exact EH tier $ figures and new Portal per-fund numbers (on slide tables not captured in text extraction).
**Pages touched:**
- raw/engagement-hub-product-overview.md (created)
- raw/engagement-hub-pricing-proposal.md (created)
- raw/engagement-hub-one-pager.md (created)
- wiki/sources/engagement-hub-product-overview.md (created)
- wiki/sources/engagement-hub-pricing.md (created)
- wiki/sources/engagement-hub-one-pager.md (created)
- wiki/products/engagement-hub.md (rebuilt — source_count 0→3, full product template)
- wiki/features/engagement-hub-branded-landing-pages.md (created — first feature page in vault)
- wiki/products/landing-page.md (folded into EH — now a redirect pointer, status deprecated)
- wiki/products/investor-portal.md (updated — flagged pricing conflict, EH relationship, related links; last_updated 2026-06-10)
- wiki/concepts/product-packaging-bundling.md (created)
- wiki/overview.md (added Investor Portal + Engagement Hub to products table)
- index.md (updated — Sources 72→75, added Features section (1), Concepts 9→10, EH 0→3, Landing Page deprecated)

## [2026-06-10] lint | 0 issues found (auto-triggered by trust-1/trust-3 ingest)

**Operation:** lint
**Summary:** Auto-lint after the Engagement Hub ingest (trust-1 spec + trust-3 pricing). Scoped to the 8 new/edited pages. Broken wikilinks: none (all targets resolve). Orphans: none (new pages have 2–7 inbound links each). Frontmatter: complete per §2 templates. Known data gaps recorded on the pages themselves (exact EH tier $ figures; new Portal per-fund numbers) rather than treated as lint defects.
**Pages touched:** none (no fixes needed).

## [2026-06-10] note | Re-synthesize overview.md against current index

**Operation:** note
**Summary:** Re-synthesized wiki/overview.md from a stale 13-source Integration-Hub-only snapshot (last_updated 2026-05-04) to the current 75-source, 13-product suite view; fixed frontmatter (source_count 13→75), rewrote scope statement, added all products by layer, EH/Portal packaging story, pricing models, known conflicts, customers, competitors, onboarding essentials, and data gaps.
**Pages touched:** wiki/overview.md, index.md (overview description)

## [2026-06-10] lint | Critical + High issues fixed (post overview re-synthesis)

**Operation:** lint
**Summary:** Ran full lint after overview.md re-synthesis. Confirmed re-synthesis introduced no new issues. Fixed 1 Critical broken wikilink and all 14 High orphans; index remained complete. Remaining: Medium (5 product pages missing `status`), Low (7 fragile source_count:1 pages), Style (1 page >200 lines) — left for a later content pass.
**Pages touched:** wiki/sources/investor-portal-sales-deck.md (broken link idm→investor-data-management), wiki/overview.md (13 customer placeholders linked), wiki/products/integration-hub.md (linked orphaned ih-implementation-guide-pdf source)

## [2026-06-10] lint | Medium frontmatter fixed (status fields)

**Operation:** lint
**Summary:** Added missing `status: GA` frontmatter field to 5 product pages (per index status). Re-validated: all product frontmatter now conforms to §2. Remaining open: Low (7 fragile source_count:1 pages), Style (1 page >200 lines).
**Pages touched:** wiki/products/integration-hub.md, wiki/products/investor-data-management.md, wiki/products/investor-access.md, wiki/products/platform.md, wiki/products/side-letter.md

## [2026-06-15] ingest | Batch 8 — AAA & Investor Access

**Operation:** ingest
**Source file:** Notion Product Knowledge Library (collection://1973f653-b1df-80b6-a036-000b27bbefb2) — 11 batch entries
**Document type:** mixed (product brief/note, sales deck, GTM training, client training, implementation guide, release notes, FAQ)
**Product(s):** AAA (6 sources), Investor Access (1 source)
**As-of date:** ranges 2024-11-01 → 2026-01-06
**Conflicts found:** none factual. Notes: (1) FDM vs IDM terminology in the Investor Access FAQ — FDM is an older internal name for IDM, flagged for CS; (2) AAA RIA-count differs across decks (365 in brief vs 630 in GTM) — later count wins, not a conflict; (3) Nov-2024 GTM deck self-flags as partly superseded by the Jan-2026 CS training + sales deck.
**Summary:** Ingested 7 of 11 Batch-8 entries. Notion `Product(s)` tags reassigned the batch away from the tracker's AAA/Investor-Access split: only 1 entry is Investor Access, 6 are AAA, 3 are Platform (SSO + Branding — deferred to a future Platform batch per user), and 1 (Primary-vs-Collaborator) was already ingested in Batch 7 (skipped as duplicate). Three AAA Google Slides decks were extracted as full text via the Google Drive connector (not metadata-only). Rebuilt both product pages.
**Pages touched:** wiki/sources/aaa-product-brief.md, wiki/sources/aaa-sales-deck.md, wiki/sources/aaa-gtm-training.md, wiki/sources/aaa-cs-training.md, wiki/sources/aaa-user-guide.md, wiki/sources/aaa-advisor-tags.md, wiki/sources/investor-access-faq.md (created); wiki/products/aaa.md (rebuilt, 1→7), wiki/products/investor-access.md (rebuilt, 1→2); wiki/onboarding.md (4 sources added); index.md (Sources 75→82, AAA 1→7, Investor Access 1→2, date)

## [2026-06-15] lint | 1 issue fixed (auto-triggered by trust-2 ingest)

**Operation:** lint
**Summary:** Auto-lint after Batch 8 (trust-2 AAA User Guide implementation guide). Scoped to the 9 new/edited pages. Found and fixed 1 Critical broken wikilink (investor-access-faq.md pointed to non-existent wiki/products/idm → corrected to investor-data-management). All other wikilinks resolve; no orphans (every new source is linked from its product page + onboarding); index complete (Sources 82); frontmatter conforms to §2.
**Pages touched:** wiki/sources/investor-access-faq.md

## [2026-06-16] ingest | Engagement Hub naming history (internal Slack)

**Operation:** ingest
**Source file:** N/A — internal Slack threads (#data-room, #product, #product-launch-coordination, #marketing); not stored in raw/
**Document type:** note (Slack provenance; below §10 trust hierarchy — naming/history only)
**Product(s):** Engagement Hub
**As-of date:** 2025-08-27 (spans 2024-10-08 → 2025-08-27)
**Conflicts found:** none on naming (additive). Minor: Slack (Aug 2025) projected Profile Sharing Phase 1 ~Sept / Phase 2 ~Oct-Nov 2025; EH spec deck (Feb 2026) says Dec 2025 / Q3 2026 — spec deck wins per §10, noted not changed.
**Summary:** Verified 5 user-relayed naming claims directly in Slack before writing. Confirmed: "landing page" = "branded landing page" (same product, shorthand); originally "IDM Branding" (Oct 2024); repackaged under Engagement Hub Aug 2025 (public launch Aug 27); EH = 4 features; rename proposal → BLP became a feature, not renamed. Cross-confirmed the launch one-pager Drive ID matches the Batch 9 ingest. Recorded provenance as a low-trust note source page; added a naming/history block to the feature page, corrected the Aug-2025-vs-June-2026 date framing on the landing-page pointer, and added a naming note + public-launch date to the EH product page.
**Pages touched:**
- wiki/sources/engagement-hub-naming-history-slack.md (created — note, trust 10)
- wiki/features/engagement-hub-branded-landing-pages.md (added "Also known as / naming history"; source_count 3→4)
- wiki/products/landing-page.md (corrected repackaging-date framing; stated synonym)
- wiki/products/engagement-hub.md (added Naming & history note + Aug 27 2025 launch; source_count 3→4)
- index.md (Sources 82→83, EH 3→4, Branded Landing Pages 3→4, last_updated 2026-06-16)

## [2026-06-16] note | Architecture Decision Records for the vault

**Operation:** note
**Summary:** Created a retrospective ADR set documenting the vault's own design decisions (meta-documentation, kept outside `wiki/` since that layer is reserved for Anduin product knowledge). Five focused ADRs in a new `docs/adr/` folder, grounded in the decision history in this log: (0001) raw/ immutable vs wiki/ LLM-owned four-layer split; (0002) recency-then-trust conflict resolution per §10; (0003) typed entity folders over the original flat `wiki/entities/` store (schema v2 migration); (0004) Obsidian wiki-link graph + six-dimension lint workflow; (0005) discuss-before-write 9-step ingest + append-only log. Added a `docs/adr/README.md` index.
**Pages touched:** docs/adr/README.md, docs/adr/0001-raw-vs-wiki-separation.md, docs/adr/0002-trust-hierarchy-conflict-resolution.md, docs/adr/0003-entity-type-taxonomy.md, docs/adr/0004-wikilink-graph-and-lint.md, docs/adr/0005-ingest-discipline-and-log.md, log.md

## [2026-06-19] ingest | Competitive Intel Repository — Tracking Table (Notion export)

**Operation:** ingest
**Source file:** raw/notion-competitive-intel-tracking-table/ (153 .md files + _tracking-table-all.csv, exported from Notion)
**Document type:** note (competitive field intel)
**Product(s):** Fundsub (primary), Side Letter, Investor Portal, Data Room, IDM, OCR
**As-of date:** 2026-06-17 (spans 2022-06 → 2026-06)
**Conflicts found:** none requiring overwrite. Directional source (trust 9) — yields to authoritative pricing/spec sources (trust 1–3). Corroborated existing AtomInvest pricing (Boston deck) and merged, not overwritten. De-duplicated re-logged events (iCapital/Parallel Markets, IDR→Sonata One).
**Summary:** Ingested the Notion Competitive Intel "Tracking Table" (153 dated field-intel entries across 37 companies) as one source page, then synthesized into competitor and concept pages. Routed by the export's own Company-type tags: direct/potential competitors → competitor pages; partners/fund-admins/law-firms folded in or noted (K&E kept due to lost deals). 16 companies with ≥2 entries got full pages (Passthrough merged 46, AtomInvest merged 24, etc.); 20 single-mention firms captured compactly in one watchlist roundup; 7 no-company market-intel entries → landscape concept. All competitor/concept pages carry a confidence rating (single underlying source).
**Pages touched:**
- wiki/sources/competitive-intel-tracking-table.md (created — note, trust 9)
- wiki/competitors/passthrough.md, subscribe.md, ontra.md, icapital-cais.md, vega.md, juniper-square.md, bunch.md, nav.md, idr.md, funded.md, flow.md, fenergo.md, bitestream.md, backstop.md, kirkland-ellis.md (created)
- wiki/competitors/atominvest.md (merged 24 new entries; source_count 2→3)
- wiki/competitors/competitor-landscape-watchlist.md (created — 20 single-mention firms)
- wiki/concepts/competitor-pricing-benchmarks.md, competitive-win-loss.md, private-markets-competitive-landscape.md (created)
- index.md (Sources 83→84, Competitors 2→18, Concepts 10→13, last_updated 2026-06-19)
- raw/notion-competitive-intel-tracking-table/ (immutable source copy)

## [2026-06-19] lint | 3 issues found, all fixed

**Operation:** lint
**Summary:** Auto-triggered lint after the large competitive-intel ingest (~22 new/edited pages). Findings, all fixed: (1) Critical — 3 broken wikilinks to `[[wiki/products/idm]]` (correct slug is `investor-data-management`) in passthrough.md and icapital-cais.md → repointed with display alias. (2) High — 2 orphan pages (idr, fenergo) with no inbound links → wired into the consolidation/rebrands bullet of the private-markets-competitive-landscape concept. Verified: all 20 new pages present in index.md; all frontmatter required fields present; every single-source competitor/concept page carries a `confidence` rating (satisfies §7 fragility check). No broken links remain.
**Pages touched:** wiki/competitors/passthrough.md, wiki/competitors/icapital-cais.md, wiki/concepts/private-markets-competitive-landscape.md, log.md

## [2026-06-24] note | Normalize wikilink citation format (strip `wiki/` prefix)

**Operation:** note
**Summary:** Completed the §8 wikilink normalization (policy dated 2026-06-23): converted every citation from the legacy `[[wiki/...]]` form to the `wiki/`-relative `[[...]]` form so the link graph resolves in graph tooling and in an Obsidian vault rooted at `wiki/`. Pure prefix-strip — no content changes. All 157 pages under `wiki/` plus `index.md` (155 links) converted; 0 `[[wiki/...]]` references remain vault-wide. Validated every converted link target resolves to a real file (0 broken). `index.md` last_updated bumped to 2026-06-24.
**Pages touched:** all wiki/ pages (157), index.md, graphify-out/ (regenerated artifacts), log.md

## [2026-06-25] note | Graph-assisted query retrieval — design exploration

**Operation:** note
**Summary:** Brainstormed using the knowledge graph to route/pre-filter queries instead of loading all of `index.md` every time (driver: token cost; stretch driver: semantic search). Established `graph.json` (not `graph_report.md`) as the retrieval data, mapped a query-type taxonomy to mechanisms (entity-anchored→graph, attribute/aggregate→index.md/frontmatter, exploratory→community map), and converged on classifier-routed retrieval exposed via an MCP server with `index.md` as a safe fallback. Phased build: MCP Phase 1 topology (resolve/expand/intersect/community + pruning) → Phase 2 semantics (embed wiki pages, GraphRAG). Cloned `hermes-okf` (Google Open Knowledge Format implementation) which independently validates the pattern and adds an OKF-conformance track. Thought process + 5 open decisions captured in the spec. No `wiki/` content changed.
**Pages touched:** docs/superpowers/specs/2026-06-25-graph-retrieval-design.md (created), log.md

## [2026-06-29] note | Frontmatter normalization (P2 prep — tags, target_audience, topic index)

**Operation:** note
**Summary:** Resumed the 2026-06-25 retrieval roadmap at P2. Discovered the "dirty tags" issue was actually a correctness bug: 26 of 155 wiki pages had unparseable YAML frontmatter. Fixed (1) 23 pages where a `#`-prefixed tag in a `tags: [...]` flow sequence made YAML treat the rest of the line as a comment and drop the closing `]` — stripped `#` from all frontmatter tags (collapsing split counts: sales-motion 24+8→32, onboarding 6+6→12, implementation 21+3→24, integration 11+4→15, pricing 11+1→12, security 1+2→3); (2) 3 AAA pages with an unquoted `: ` inside `original_file:` — wrapped in quotes. All 155 pages now parse (0 failures). Also canonicalized `target_audience` to pipe-delimited ordered `CS | Sales + RM | Digi | All teams` (8 pages: comma/reordered variants collapsed to 10×`CS | Sales + RM`, 3×`CS | Digi`). Added the §3-mandated tag-grouped "Topic Index (by tag)" section to `index.md` (138 wikilinks across 10 preferred tags, all validated to resolve). Updated CLAUDE.md §8 to forbid `#` in frontmatter tags, set the preferred-tag list to bare tokens, and document the `target_audience` canonical form. `index.md` last_updated → 2026-06-29.
**Pages touched:** 30 wiki/ pages (frontmatter), CLAUDE.md (§8), index.md (Topic Index section + date), log.md
