---
type: source
title: "Investor Portal — Contact Management (Feature Deep-Dive)"
date_ingested: 2026-06-08
as_of_date: undated
source_type: spec
trust_level: 1
original_file: raw/Investor Portal - Contact Management.pptx
products: [Investor Portal, IDM]
target_audience: CS
onboarding_required: No
tags: [investor-portal, idm, implementation]
---

## Summary
Deep-dive feature deck on Investor Portal's Contact Management module. Authoritative reference on the contact hierarchy, contact matrix data model, communication types, and the three main contact management use cases. High trust — spec-level detail on data structure and permission model.

## Key Takeaways
- Contact Management centralizes scattered FundSub form data into a structured, multi-dimensional contact system.
- Hierarchy: Firm → Client → Investment Entity → Contact Matrix per Fund.
- Each fund investment generates a contact matrix: a 3D grid of (Investment Entity × Fund × Communication Type) with Primary / Secondary / Not Assigned per contact.
- Communication types are customizable per firm and enabled per fund legal entity — they are the building blocks of document distribution permissions.
- Contacts are uniquely identified by email address across the Anduin ecosystem.

## Contact Hierarchy

```
Firm
├── Firm Contacts (generic — not linked to any client)
└── Client
    ├── Generic Client Contacts (linked to client, not to any IE)
    └── Investment Entity (IE)
        ├── Generic IE Contacts (linked to IE, no fund connection yet)
        └── Contact Matrix per Fund (3D permission grid)
```

## Contact Matrix Model
A contact matrix is attached to each (Investment Entity + Fund Legal Entity) pair. It is a 3D grid:
- **Dimension 1:** Investment Entity
- **Dimension 2:** Fund Legal Entity
- **Dimension 3:** Communication Types (Capital Calls, Distribution Notices, Annual Reports, Financial Reports, etc.)

At each intersection, a contact is assigned one of: **Primary** (first click), **Secondary** (second click), **Not Assigned** (third click / removed).

**Communication types** are defined at the firm level and enabled selectively per fund legal entity. Firms can create any list they need. Examples from the deck: Capital Calls, Distribution Notices, Annual Reports, Financial Reports, Contact Notes, FAQs.

## Contact Detail Sections
Each contact record includes:
1. **Personal info:** Name, custom ID, email, phone, company, title, address
2. **Communication:** All permissions across all IEs and funds centralized in one view (Primary/Secondary/Not Assigned per comm type per fund)
3. **Related Clients and IEs:** Which clients and investment entities this contact is linked to
4. **Anduin App Access:** Which Anduin apps and engagements (FundSub, Data Room, Portal) this contact can access
5. **Contact notes:** Free-text internal notes (GP-only)

## Additional System Permissions (beyond comm types)
- **Invitation Emails:** Whether this contact receives future fund subscription invitations
- **Profile Updates:** Whether this contact is allowed to update profile information in the portal (investor self-service)

## Three Key Use Cases

**Use Case 1 — Add new contact to multiple entities:**
From All Contacts tab → Create contact → Fill name + email → Assign clients/IEs → Set up communication matrix

**Use Case 2 — Update permissions for a contact across multiple entities/funds:**
Find contact → Edit communication matrix → Batch apply: one click sets Primary, two clicks sets Secondary, three clicks removes → Review and save

**Use Case 3 — Replace one contact with another (contact leaves):**
Find the departing contact → Clone their permission (pre-fills new contact modal with same matrix) → Fill in new contact's details → Delete the departing contact

## Bulk Import
For large onboarding: use the spreadsheet import feature to create multiple clients, investment entities, and contacts at once.

## Connections
- [[wiki/products/investor-portal]] — Contact Management is a core feature of this product
- [[wiki/products/investor-data-management]] — IDM stores the underlying data structure
- [[wiki/sources/investor-portal-sales-deck]] — contact management covered at a high level in the sales deck
- [[wiki/sources/investor-portal-customer-training-guide]] — CS training on how to set up contacts during onboarding

## Conflicts & Supersessions
None found. This is the most detailed source on the contact matrix model.

## Raw Notes
- The deck notes that contact management resonates well with prospects: the ability to view/update a departing employee's access across all entities is a key selling point.
- "Profile Updates" permission allows specific contacts to view and suggest edits to their contact matrix — GP still reviews/approves before changes are effective.
