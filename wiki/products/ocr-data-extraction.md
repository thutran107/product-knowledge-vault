---
type: product
title: "OCR Data Extraction"
status: GA
source_count: 11
last_updated: 2026-05-11
tags: [ocr, data-extraction, digitization]
---

## What it does
Anduin's OCR-powered data extraction service that digitizes structured data from investor documents — subscription forms, KYC packets, fund documents — using Amazon Textract augmented by a human review layer.

## Key capabilities
- Automated document ingestion using Amazon Textract (AI/OCR engine).
- Human-augmented review layer — analysts validate and correct extraction output.
- Table view for reviewing extracted data before it flows downstream.
- Integration with FundSub document processing pipeline.
- Pricing is proposal-based; a Google Sheets pricing guide exists for Sales use.
- Two customer-facing security whitepapers available (Textract security + human processing security).

## Pricing & packaging
Proposal-based pricing. See [[wiki/sources/ocr-pricing-guide|Data Extraction Pricing Guide]] (as-of 2025-11-13) for the proposal-building framework. For Sales + RM use only.

## Implementation notes
Two implementation guides exist for the end-to-end delivery process:
- [[wiki/sources/ocr-implementation-guide|Implementation Guide]] (internal training deck, CS + Digi, onboarding required)
- [[wiki/sources/ocr-implementation-journey|Implementation Journey CS-DEA-Client]] (Notion SOP covering the three-party process, onboarding required)

New OCR UX launched May 2025 — verify that pre-May training materials reflect current UX.

## Known limitations
- Implementation and GTM training materials have no as-of dates — currency unverified.
- OCR/AI Managed Services Sales Deck and Data Extraction Sales Deck point to the same underlying Google Slides presentation (different sections) — rationalize to avoid confusion.

## Features & sub-modules
- Data Extraction (core OCR pipeline)
- Table View (data review interface — see [[wiki/sources/ocr-table-view-how-it-works]])
- FundSub integration (see [[wiki/sources/ocr-fundsub-process-client-training]])

## Related customers
All customers (no named-customer-specific sources ingested yet).

## Sources
- [[wiki/sources/ocr-implementation-guide|Implementation Guide]] *(trust 2, onboarding required)*
- [[wiki/sources/ocr-implementation-journey|Implementation Journey CS-DEA-Client]] *(trust 2, onboarding required)*
- [[wiki/sources/ocr-pricing-guide|Pricing Guide]] *(trust 3, as-of 2025-11-13)*
- [[wiki/sources/ocr-gtm-training|GTM Training]]
- [[wiki/sources/ocr-data-extraction-sales-deck|Data Extraction Sales Deck]] *(as-of 2025-08-20, preferred)*
- [[wiki/sources/ocr-managed-services-sales-deck|OCR/AI Managed Services Sales Deck]] *(same deck, older entry)*
- [[wiki/sources/ocr-security-whitepaper-textract|Security Whitepaper — Amazon Textract]]*
- [[wiki/sources/ocr-security-whitepaper-human-augmented|Security Whitepaper — Human-Augmented Processing]]*
- [[wiki/sources/ocr-fundsub-process-client-training|FundSub Process Client Training]]
- [[wiki/sources/ocr-table-view-how-it-works|Table View — How It Works]] *(trust 1, as-of 2025-09-16)*
- [[wiki/sources/ocr-new-ux-overview|New OCR UX Overview]] *(as-of 2025-05-14)*

## Related
- [[wiki/products/fundsub|FundSub]] — OCR integrates into FundSub subscription document processing.
- [[wiki/products/investor-data-management|IDM]] — extracted data may populate IDM investor profiles.
