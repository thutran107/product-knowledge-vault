# Wiki Log

Append-only record of all operations. Format: `## [YYYY-MM-DD] <operation> | <title>`

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
