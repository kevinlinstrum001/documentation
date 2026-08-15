# Inventory 3.0

| Field | Current value |
|---|---|
| **Document role** | System-local orientation and navigation |
| **System** | Inventory 3.0 |
| **Parent Project** | Inventory Management |
| **System ID** | Unassigned; no permanent `SYS-###` is being created in this documentation step |
| **System Identity Entity Record** | Not created; System Identity schema is intentionally deferred |
| **Human-readable System definition** | `summaries/system-summary.md` |
| **System Summary sidecar** | `sidecars/system-summary-sidecar.json` |
| **Documentation status** | Working System documentation layer complete without formal System Identity |
| **Last reconciled** | 2026-08-15 |

---

## 1. Purpose of this README

This README is the local orientation document for the **Inventory 3.0 System**.

Its job is to help a person, tool, or future work session enter this System directory and determine:

- what Inventory 3.0 is;
- which Project gives the System its operational meaning;
- which local records explain the System;
- what source material supports the current interpretation;
- where current implementation truth should be verified;
- which statements are historical design intent versus implementation evidence;
- what is still unresolved;
- how to resume System work without prematurely creating a System Identity schema.

The governing rule is:

> **Describe the System now; formalize System Identity only after the Project model has been proven and the System boundary has been reconciled.**

This README is not a System Identity Entity Record.

---

## 2. System context

Inventory 3.0 is the **principal known System** presently associated with the **Inventory Management Project**.

Current semantic relationship:

```text
Inventory Management
        ↓
    Inventory 3.0
```

The relationship above explains placement and meaning. It is not an identity encoding.

Inventory 3.0 should be understood as the coherent implementation mechanism through which inventory-management behavior, interfaces, data, validation, event history, and supporting Resources can be organized.

The distinction is:

```text
Inventory Management
    = Project

Inventory 3.0
    = System

Applications / spreadsheets / scripts / datasets / deployments
    = Resources or implementation artifacts
```

Earlier records may use “Inventory 3.0” primarily as an application name or may call the broader Inventory Management undertaking a System. Preserve those records as historical evidence rather than rewriting them.

---

## 3. Why there is no `system-identity.json` yet

This documentation layer intentionally stops short of a formal System Identity Entity Record.

No file such as:

```text
system-identity.json
```

is being created here.

No permanent:

```text
SYS-###
```

is being assigned.

That is deliberate.

The Project Definition exemplar must first prove that the separation among:

- Entity Record;
- README;
- human-readable summary;
- document sidecar;
- relationships;
- Resources;
- implementation evidence;
- historical evidence;

works reliably at the Project level.

Only after that should Klinswork decide what stable facts belong in a System Identity schema.

For now, this directory documents **what Inventory 3.0 means and how it is understood**, without pretending that the System Identity architecture has been finalized.

---

## 4. Local records and authority

### `README.md`

This file.

Role:

- local orientation;
- reading order;
- authority routing;
- resume-work guidance;
- explanation of the deliberate absence of a System Identity Entity Record.

### `summaries/system-summary.md`

Role:

- human-readable System definition;
- purpose;
- functional role;
- architecture baseline;
- data model and operational behavior described by source records;
- historical implementation evidence;
- current-state limitations;
- Resources and integrations;
- unresolved System questions;
- next work.

It is the explanatory source for the System interpretation represented there.

### `sidecars/system-summary-sidecar.json`

Role:

- machine-readable structured companion to `summaries/system-summary.md`;
- discovery and Viewer support;
- structured representation of the Summary's main concepts, current state, source basis, and unresolved questions.

It is **not** a System Identity record.

### Parent Project documentation

For the durable Project context, read:

```text
../../project-identity.json
../../README.md
../../summaries/project-summary.md
../../sidecars/project-summary-sidecar.json
```

Project documentation owns the explanation of why Inventory Management exists and how Inventory 3.0 fits into that Project.

### Live implementation sources

For claims about what the current deployed System actually does, verify against:

- current Apps Script source;
- current authoritative datastore;
- current deployment configuration;
- current test evidence;
- current Resource Registry entries;
- current workflow-run / execution evidence where applicable.

Historical plans and work updates are evidence of earlier design or implementation state, not automatic proof of the live state today.

---

## 5. Documentation structure

Current System-local structure:

```text
Inventory 3.0/
├── README.md
├── summaries/
│   └── system-summary.md
└── sidecars/
    └── system-summary-sidecar.json
```

This is intentionally smaller than a future formal System Definition package.

There is no System Identity Entity Record in this step.

---

## 6. Source basis

The current System interpretation is grounded primarily in three evidence classes.

### Current Project-definition material

The Inventory Management Project Summary establishes that:

- Inventory 3.0 is the principal known System;
- Inventory Management and Inventory 3.0 are not synonymous;
- System Identity and permanent `SYS-###` assignment are intentionally deferred;
- current deployment behavior and live inventory state were not comprehensively reverified during the Project-definition work.

### Inventory 3.0 roadmap

The historical Inventory 3.0 roadmap describes the intended implementation as a standalone Google Apps Script web application using Google Sheets as its datastore, with a mobile-friendly custom interface, server-side validation, event history, current inventory, and product/SDS reference data.

The roadmap is a **planning/design source**.

Its unchecked verification items must not be converted into claims that those tests were performed.

### Historical implementation evidence

Dated work-update/catalog evidence from July 2026 records that Inventory 3.0 was actually constructed and expanded. That evidence includes Google Apps Script and Google Sheets implementation, product-information pages, inventory browsing/filtering, and SDS-link integration.

That evidence is historical.

It does not establish that the same deployment, code, schema, or feature set is still current without present verification.

---

## 7. Working System model

The roadmap's implementation model is:

```text
mobile or desktop browser
        ↓
Apps Script HTML interface
        ↓
Apps Script inventory services
        ↓
Google Sheets datastore
```

Major implementation concerns include:

- product reference data;
- location reference data;
- current inventory state;
- inventory-event history;
- opening balances;
- receiving;
- use;
- corrections;
- transfers;
- validation;
- protection against invalid or duplicate writes;
- history/audit views;
- SDS access;
- administrative maintenance;
- reporting;
- mobile usability.

This is a working System interpretation derived from the source material.

It is not a frozen System schema.

---

## 8. Historical datastore model

The original roadmap names an `Inventory-3.0` Google Sheets workbook and describes these sheets:

```text
Products
SDS
Locations
Current Inventory
Inventory Events
Inv2_Archive
```

It also describes Inventory 2.0 history as preserved separately in `Inv2_Archive`, with new Inventory 3.0 live state intended to begin from verified physical counts rather than importing stale quantities.

Treat that as historical design/implementation evidence.

Before using a workbook ID, sheet name, deployment URL, or current schema operationally, resolve and verify the current Resource through the Resource Registry and live source.

---

## 9. Resume-work sequence

For System-level work:

```text
Inventory 3.0 work begins
        ↓
read this README
        ↓
read summaries/system-summary.md
        ↓
read system-summary sidecar where useful
        ↓
read parent Inventory Management Project Summary
        ↓
resolve required Resources through Resource Registry
        ↓
verify current Apps Script / datastore / deployment as needed
        ↓
load applicable workflow
        ↓
load current implementation plan and execution/run state
        ↓
load relevant Activities / historical work records
        ↓
record unresolved discrepancies
        ↓
perform work
```

Do not create a System Identity record merely because a work session wants a convenient place to store mutable implementation facts.

---

## 10. Implementation plans

Implementation planning currently lives at the **Inventory Management Project** level:

```text
../../implementation-plans/
```

That location is appropriate for bounded Project work affecting Inventory 3.0.

A historical implementation plan also exists for the Inventory 3.0 SDS Registry rebuild and app integration.

When resuming implementation:

```text
workflow specification
    → reusable method

implementation plan
    → intended work

execution evidence / workflow run
    → what happened

System Summary
    → explanatory System interpretation
```

Do not treat a plan as proof of completion.

---

## 11. Unresolved questions

The following remain open:

- What stable facts should eventually belong in a System Identity Entity Record?
- Does Inventory 3.0 receive a permanent `SYS-###`, and under what allocation authority?
- What is the final System boundary?
- Is “Inventory 3.0” the stable System name, a version-bearing System name, or a historical implementation label that may later need a different canonical System identity?
- Which current Apps Script project is authoritative?
- Which current datastore is authoritative?
- Which deployment is current?
- Which historical roadmap phases were completed, modified, skipped, or superseded?
- Which tests were actually performed?
- Which current Resources already have valid `RES-###` identities?
- Which Inventory 3.0 Resources are shared with Documentation, SDS, Locations, or other Klinswork Projects/Systems?
- What Viewer behavior should distinguish a System Summary from a future System Identity Entity Record?
- What evidence is required before System Identity can be formalized?

Do not resolve these questions by inference merely to make the documentation package look complete.

---

## 12. Next work

With this System documentation layer present, the next Project Definition work is to:

1. regenerate the Klinswork Documentation Viewer manifest;
2. verify Project-space discovery of the Project and System summary sidecars;
3. verify companion-document resolution;
4. verify that `project-identity.json` is treated as an Entity Record rather than a sidecar;
5. verify that the Viewer can distinguish the Inventory Management Project Summary from the Inventory 3.0 System Summary;
6. reconcile Resource Registry entries needed for current System routing;
7. test a context-naive resume path;
8. only then decide what the exemplar teaches us about the future System Identity schema.

The goal of this layer is **System understanding without premature System Identity formalization**.
