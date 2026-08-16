For Inventory 3.0, we are actually in a **better starting position than we were with Work Queue**, because yesterday's exemplar already created a substantial current-state documentation layer.

We already have:

* `Inventory 3.0/README.md`
* `Inventory 3.0/summaries/system-summary.md`
* `Inventory 3.0/sidecars/system-summary-sidecar.json`
* the parent `Inventory Management/summaries/project-summary.md`
* the Project implementation plan
* substantial historical design evidence and known open questions. 

The System Summary already covers the things we would otherwise have to reconstruct first: architecture, components, datastore, event model, interfaces, validation, Resources, implementation history, current uncertainty, and open questions. 

So I think the source packet for an **Inventory 3.0 roadmap** should be:

1. **Current System truth**

   * `system-summary.md`
   * `system-summary-sidecar.json`
   * `README.md`

2. **Project context**

   * Inventory Management `project-summary.md`
   * Project README / identity record
   * especially the Project boundaries: Inventory owns inventory state and effects; Work Queue owns the task lifecycle; Scheduling owns temporal/person/place assignment. 

3. **Existing plans**

   * the Inventory SDS Registry rebuild implementation plan;
   * any older Inventory roadmaps/design notes;
   * historical work updates that describe intended features.

   We have to keep those as **planning evidence**, not automatically claim they were implemented. Yesterday explicitly established that discipline for Inventory 3.0. 

4. **Current Registry/resource map**
   We should resolve the resources already associated with Inventory, particularly:

   * Inventory app;
   * Inventory data workbook;
   * Inventory Events;
   * Products;
   * SDS Registry;
   * Chemical Product Catalog;
   * relevant implementation-plan resources;
   * shared Locations data.

5. **Live application/data inspection**

   This is the piece I would consider essential before calling the roadmap nearly complete.

   We should open the actual Inventory app and its data workbook and ask:

   > What does it actually do today?

   > What partially works?

   > What is missing?

   > What is awkward enough that it should be redesigned?

   > What capabilities should the mature Inventory System have?

The existing summary gives us a strong documented architecture baseline:

```text
browser
   ↓
Apps Script HTML interface
   ↓
Apps Script inventory services
   ↓
Google Sheets datastore
```

with historically documented sheets such as Products, SDS, Locations, Current Inventory, Inventory Events and `Inv2_Archive`, and event concepts including opening balances, received, used, corrections and transfers. 

Then I think we do exactly what we just did conversationally with Work Queue: **talk through the mature application.**

Some obvious Inventory roadmap areas already suggest themselves, but I would not freeze them yet:

```text
Inventory 3.0

Inventory State & Reconciliation
Receiving
Usage / Consumption
Transfers
Employee Cart Inventory
Inventory Holder Inventory
Work Queue Integration
Employee Attribution
Product Management
SDS / Chemical Information
Locations & Building Map
Search & History
Reporting / Printing
QR Inventory Operations
Inventory Auditing
Corrections / Reversals
Administration
Data Integrity / Reliability
```

And there are already interesting cross-System requirements coming from the Work Queue roadmap.

For example:

```text
Work Queue task completion
        ↓
Inventory transfer
        ↓
Employee Cart  - quantity
Inventory Holder + quantity
        ↓
Inventory Events
        ↓
employee + task + source + destination
```

From the Inventory side, that same capability has different concerns: transactional integrity, source quantity, destination quantity, event linkage, duplicate protection and reconciliation. So it belongs in **both System roadmaps as an integration**, but each roadmap describes its own responsibility.

### What I think we should do next

Before writing anything, I would gather these four primary records:

```text
Inventory Management/
├── summaries/project-summary.md
├── implementation-plans/implementation-plan.md
└── systems/Inventory 3.0/
    ├── README.md
    └── summaries/system-summary.md
```

Then inspect the **live Inventory app and data workbook**.

After that we have a conversation like the one we just had about Work Queue and define the desired mature Inventory 3.0.

The products would then be:

```text
Inventory 3.0/
├── summaries/
│   ├── system-summary.md          ← what it is now
│   └── inventory-3-roadmap.md     ← what it should become
│
└── sidecars/
    ├── system-summary-sidecar.json
    └── inventory-3-roadmap-sidecar.json
```

and finally we add Inventory 3.0 as the **second active entry** in `klinswork-system-roadmap-catalog-001.json`. The repository already has the necessary Inventory exemplar structure to receive those records cleanly. 

So the main thing we *don't* need is another large archaeology project. Yesterday already did much of that. What we need now is **current-state verification plus target-state design**.
