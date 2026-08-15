# Inventory 3.0 — System Summary

| Field | Current value |
|---|---|
| **Document role** | Human-readable System definition and current System interpretation |
| **System** | Inventory 3.0 |
| **Parent Project** | Inventory Management |
| **System ID** | Unassigned; permanent `SYS-###` assignment is intentionally deferred |
| **System Identity Entity Record** | Not created |
| **Companion sidecar** | `../sidecars/system-summary-sidecar.json` |
| **Current-state confidence** | High for semantic placement and historical source interpretation; current live implementation requires verification |
| **Last reconciled** | 2026-08-15 |
| **Reconciliation timestamp** | 2026-08-15T13:02:00-06:00 |

---

## 1. Document purpose and authority

This document is the human-readable System Summary for **Inventory 3.0**.

It exists so Klinswork can describe the System richly enough to understand and resume work **without** prematurely creating a formal System Identity schema.

This Summary explains:

- the System's role inside the Inventory Management Project;
- the implementation model described by the historical roadmap;
- its major functional responsibilities;
- its data model and event model as originally designed;
- historical evidence that the System was actually implemented and expanded;
- the distinction between planning evidence, historical implementation evidence, and current live truth;
- relevant Resources and integrations;
- historical continuity with Inventory 2.0;
- current documentation state;
- unresolved System questions;
- next work.

This Summary is an explanatory authority for the **current System interpretation expressed here**.

It is not:

- a System Identity Entity Record;
- an authority for a permanent `SYS-###`;
- proof of current deployment state;
- proof that every roadmap item was implemented;
- proof that every planned test passed;
- a replacement for current source code or current datastore evidence;
- a replacement for the Resource Registry;
- a replacement for formal relationship records.

---

## 2. Relationship to the Inventory Management Project

Inventory 3.0 exists within the meaning supplied by the **Inventory Management Project**.

Current working relationship:

```text
Inventory Management
        ↓
    Inventory 3.0
```

The Project is the durable undertaking concerned with reliable knowledge and operational control of inventory.

Inventory 3.0 is the principal known System presently used to implement that undertaking.

Therefore:

```text
Inventory Management
    != Inventory 3.0
```

The Project can survive replacement or major redesign of Inventory 3.0.

Likewise, a repository move, deployment replacement, workbook replacement, or interface rewrite does not by itself establish a new Project.

Whether it establishes a new **System** is precisely the kind of System Identity question that is intentionally deferred.

---

## 3. Why System Identity is deferred

The Project Definition exemplar now has a narrow Project Identity Entity Record, local orientation, a Project Summary, and a Project Summary sidecar.

The next question is whether the same architecture should be copied directly to Systems.

The answer is not assumed.

Inventory 3.0 is being documented first through:

```text
README.md
summaries/system-summary.md
sidecars/system-summary-sidecar.json
```

This lets the exemplar test:

- whether System meaning can be separated cleanly from Project meaning;
- whether current implementation facts can stay outside intrinsic identity;
- whether Resource relationships can remain external to identity;
- whether historical names and versions create ambiguity;
- whether the Viewer can distinguish Project and System records;
- which stable System facts actually need a future Entity Record.

No `system-identity.json` is created in this step.

No `SYS-###` is invented.

---

## 4. System purpose

Inventory 3.0 is intended to provide a coherent implementation environment for inventory work.

Its functional purpose is to connect user actions to controlled inventory-state changes while preserving enough information to verify and reconstruct those changes.

The historical roadmap describes a design in which the System should:

- load product and location reference data;
- show current inventory;
- establish verified opening balances;
- receive inventory;
- record use;
- correct inventory against physical counts;
- transfer inventory between locations;
- record complete inventory-event history;
- make SDS information available from product records;
- protect writes against invalid or duplicate changes;
- support mobile use;
- later support administration and reporting.

This System purpose is narrower than the Inventory Management Project.

The Project represents the operational undertaking.

The System represents a coherent implemented mechanism serving that undertaking.

---

## 5. Architecture baseline

The historical Inventory 3.0 roadmap defines this architecture:

```text
Mobile or desktop browser
        ↓
Apps Script HTML interface
        ↓
Apps Script inventory services
        ↓
Google Sheets datastore
```

The roadmap identifies these main components:

- Google Apps Script web application;
- Google Sheets datastore;
- custom HTML, CSS, and JavaScript interface;
- Apps Script server-side validation;
- inventory event history;
- current inventory table;
- product reference data;
- SDS reference data.

The roadmap explicitly aimed to replace a Google Forms workflow with a custom mobile-friendly interface.

This architecture should be treated as the **design baseline**.

Historical work-update evidence later confirms that Google Apps Script and Google Sheets were in actual use and that Inventory 3.0 was expanded with product-information pages, filtering/browsing improvements, and SDS-link integration.

Current source should still be checked before assuming that the same architecture, files, deployment, or schema remains live today.

---

## 6. Datastore and data model

### 6.1 Historical workbook

The roadmap names:

```text
Inventory-3.0
```

as the Google Sheets datastore.

It records a spreadsheet ID in the historical design source.

That identifier is not repeated here as current routing authority because current Resource identity and location should be resolved through the Resource Registry or live implementation evidence.

### 6.2 Historical sheet model

The roadmap describes six sheets:

```text
Products
SDS
Locations
Current Inventory
Inventory Events
Inv2_Archive
```

### 6.3 Products

Historical design fields:

```text
product_id
product_name
manufacturer
manufacturer_product_code
category
container_size
inventory_unit
product_image_url
manufacturer_page_url
active
```

### 6.4 SDS

Historical design fields:

```text
sds_id
product_id
revision_date
document_url
source
date_verified
current
```

### 6.5 Locations

Historical design fields:

```text
location_id
location_name
location_type
active
```

### 6.6 Current Inventory

Historical design fields:

```text
inventory_id
product_id
location_id
quantity
unit
last_updated
```

### 6.7 Inventory Events

Historical design fields:

```text
event_id
timestamp
event_type
product_id
quantity
from_location
to_location
performed_by
notes
```

### 6.8 Design rules

The roadmap states design rules including:

- unique product IDs;
- unique location IDs;
- at most one current-inventory row for a product/location combination;
- numeric quantities;
- no negative inventory;
- standardized units;
- real date values;
- every inventory change must create an event;
- Current Inventory must not be changed without an accompanying event.

These are design requirements from the roadmap.

They should not be reported as currently enforced until verified against live implementation source and current test evidence.

---

## 7. Inventory actions and event model

The roadmap defines these event types:

```text
OPENING_BALANCE
RECEIVED
USED
CORRECTION_INCREASE
CORRECTION_DECREASE
TRANSFER
```

### Opening balance

The design establishes inventory from a verified physical quantity.

The initial Inventory 3.0 plan deliberately avoided importing old live quantities from Inventory 2.0 because those quantities were not trusted as current physical stock.

### Receive

Design intent:

```text
increase destination inventory
create RECEIVED event
return updated quantity
```

### Use

Design intent:

```text
verify sufficient quantity
decrease inventory
create USED event
return updated quantity
```

### Correction

Design intent:

```text
compare stored quantity with physical count
determine difference
require reason
create correction event
update stored quantity
```

### Transfer

Design intent:

```text
verify source inventory
reduce source quantity
increase destination quantity
create transfer event
return updated records
```

These rules describe the intended System behavior.

Current implementation verification remains separate.

---

## 8. Write protection and integrity

The roadmap's write-protection model is:

```text
Acquire lock
Validate command
Read current quantity
Write event
Update Current Inventory
Release lock
Return result
```

It also specifies intended protections against:

- zero or negative action quantities;
- invalid product IDs;
- invalid location IDs;
- insufficient inventory;
- transfers to the same location;
- duplicate opening balances;
- duplicate rapid submissions;
- client-supplied totals;
- browser-generated identifiers or timestamps;
- failed operations leaving partially changed live tables.

The roadmap's verification checklist for these protections is historical planned testing.

Unchecked boxes must remain unchecked in interpretation unless execution evidence establishes otherwise.

---

## 9. History and audit model

The roadmap defines a goal that every inventory change should be reviewable.

Planned history views include:

- recent activity;
- product history;
- location history;
- date-range history;
- event-type filtering;
- performed-by filtering.

Planned history display fields include:

- timestamp;
- product;
- action;
- quantity;
- source location;
- destination location;
- person;
- notes;
- resulting quantity where useful.

The design also keeps:

```text
Inv2_Archive
```

separate from active Inventory 3.0 event history.

The archived Inventory 2.0 history was intended not to affect current Inventory 3.0 calculations.

---

## 10. SDS integration

The roadmap defines SDS integration as a read-only operational reference in the first version.

Its planned product view includes:

- product name;
- manufacturer;
- SDS revision date;
- source;
- verification date;
- current status;
- an SDS-document action.

Historical July 2026 work-update evidence indicates that SDS access was in fact integrated into Inventory 3.0 product pages.

Later August planning records describe a further **SDS Registry Rebuild and App Integration** effort intended to improve source verification, revision preservation, catalog status, and Inventory 3.0 interface behavior.

Those sources show that SDS integration evolved beyond the earliest roadmap.

They do not, by themselves, establish the exact live SDS implementation state on 2026-08-15.

---

## 11. User interface and usability

The roadmap's guiding principles include:

- mobile first;
- fast to use;
- one action per button press;
- clear feedback;
- complete history;
- verified inventory;
- no hidden spreadsheet changes;
- no inventory update without an event;
- data structure independent from the interface;
- simple before advanced.

The first development target called for a page that could:

1. load Products and Locations;
2. display products;
3. accept a verified opening quantity;
4. write an `OPENING_BALANCE` event;
5. create a Current Inventory record;
6. return the updated quantity;
7. update the interface without reloading.

Later historical work-update evidence indicates that Inventory 3.0 was expanded with a product-information page system, more practical product filtering, SDS access from product pages, and mobile-related refinements.

Again, those are dated implementation observations, not automatic statements about the current deployment.

---

## 12. Administration and reporting

The roadmap places administrative tools and reporting after core inventory behavior.

Possible administrative functions included:

- add/edit/activate/deactivate products;
- add/edit locations;
- update or verify SDS links;
- review inventory corrections;
- export inventory reports;
- inspect data problems.

Possible reports included:

- current inventory by location;
- low-stock items;
- received inventory by date;
- product usage by date;
- corrections by product;
- transfers between locations;
- recent changes;
- historical quantity trends;
- order-justification reporting.

These were planned capabilities.

This Summary does not claim they were all implemented.

---

## 13. Historical implementation evidence

### 13.1 Inventory 2.0 → Inventory 3.0

The roadmap treats Inventory 2.0 as:

- prototype;
- historical reference;
- source of useful ideas and product data;
- preserved history.

Inventory 3.0 was intended as a rebuilt application rather than a direct continuation of old live quantities.

### 13.2 July 2026 construction and expansion

Historical work-update/catalog records describe Inventory 3.0 as actually created and expanded during July 2026.

Those records identify implementation technologies including:

- Google Apps Script;
- Google Sheets;
- JavaScript;
- HTML;
- CSS.

They also record features and integrations including:

- inventory browser behavior;
- product pages;
- product filtering;
- SDS links;
- Google Sites launch links;
- QR-code use;
- shared Tool Center presentation.

A July 23 record specifically describes establishment of a product-information page system, improved product filtering, and SDS access integrated into product pages.

These are useful historical facts because they show that Inventory 3.0 progressed beyond a roadmap-only concept.

### 13.3 August 2026 SDS work

By early August, an implementation plan titled:

```text
Inventory 3.0 SDS Registry Rebuild and App Integration
```

had been documented.

Its purpose was to rebuild the Inventory App SDS registry, preserve historical revisions, integrate catalog verification status, and update the Inventory 3.0 interface.

That plan is evidence of intended subsequent work.

Its existence does not prove that every planned change was executed.

---

## 14. Resources and implementation artifacts

Inventory 3.0 is associated with several classes of implementation Resource.

These include:

### Application / interface

- Apps Script web application;
- HTML/CSS/JavaScript client interface;
- product-information pages;
- inventory browser.

### Data

- product records;
- location records;
- current inventory;
- inventory events;
- SDS records;
- Inventory 2.0 archive.

### Server-side code

Historical records name implementation files/components such as:

- `Config.gs`;
- `DataService.gs`;
- `InventoryService.gs`;
- `Validation.gs`;
- `Scripts.html`.

These names are historical implementation evidence.

Current source should be verified before treating that set as complete or current.

### Deployments and launch surfaces

Historical records include an Apps Script deployment and launch/integration through Google Sites / Tool Center mechanisms.

Current deployment routing should come from the Resource Registry or verified live implementation, not from copied historical URLs.

### Documentation

Relevant documentation includes:

- Inventory 3.0 roadmap;
- Inventory Management Project documentation;
- SDS Registry implementation plan and sidecar;
- historical work updates;
- this System Summary and sidecar.

### Resource rule

Do not assign new `RES-###` identifiers from this Summary.

Resolve or reconcile them through the Resource Registry.

---

## 15. Current state

### Semantic state

High confidence:

- Inventory 3.0 is the principal known System inside the Inventory Management Project.
- Inventory Management and Inventory 3.0 are different semantic entities.
- Inventory 3.0 is implementation-oriented.
- System Identity has not yet been formalized.
- No permanent `SYS-###` is assigned in this exemplar step.

### Historical implementation state

The available historical record supports that:

- Inventory 3.0 was built, not merely proposed;
- Google Apps Script and Google Sheets were core implementation technologies;
- product browsing/pages and SDS access existed in July 2026 historical work;
- later SDS-registry improvement work was planned.

### Live/current implementation state

Not comprehensively verified in this documentation step.

This Summary does not establish:

- the current deployment URL;
- the current source-project identifier;
- the current application version;
- current spreadsheet schema;
- current live quantities;
- current user access configuration;
- current test status;
- completion of every roadmap phase;
- completion of the August SDS-registry plan.

Those facts should be resolved from live implementation evidence.

### Documentation state

This System layer now contains:

```text
Inventory 3.0/
├── README.md
├── summaries/
│   └── system-summary.md
└── sidecars/
    └── system-summary-sidecar.json
```

No System Identity Entity Record exists by design.

---

## 16. Boundaries

Inventory 3.0 should not absorb the identity or authority of adjacent things simply because it uses them.

### Inventory Management Project

Inventory 3.0 implements/supports the Project; it is not the Project itself.

### Google Sheets datastore

The datastore is an implementation Resource, not the System identity.

### Apps Script deployment

The deployment is a mutable Resource/location, not the System identity.

### SDS records and Documentation

SDS records may participate in inventory work, but SDS-documentation infrastructure has its own authority and history.

### Locations

Location reference data participates in inventory state, but general location governance can remain shared or separate.

### Tool Center / launch surfaces

A launch hub can expose Inventory 3.0 without becoming part of the core inventory System.

### Historical Inventory 2.0

Inventory 2.0 is predecessor/prototype history, not active Inventory 3.0 state merely because its archive is preserved.

---

## 17. Resume-work procedure

A future System-level session should proceed in this order:

```text
read Inventory 3.0/README.md
        ↓
read summaries/system-summary.md
        ↓
interpret system-summary-sidecar.json where useful
        ↓
read parent Inventory Management Project Summary
        ↓
resolve current Resources in Resource Registry
        ↓
inspect current Apps Script source and datastore
        ↓
verify deployment and test evidence as needed
        ↓
load applicable workflow
        ↓
load current implementation plan / run state
        ↓
compare live state with historical roadmap/work updates
        ↓
record discrepancies explicitly
        ↓
perform work
```

This sequence protects against a common failure mode: using an old roadmap or work update as though it were a current implementation specification.

---

## 18. Unresolved questions

### Identity and boundary

- What stable facts belong in a future System Identity record?
- Does Inventory 3.0 receive a permanent `SYS-###`?
- Is the “3.0” version label part of stable System identity or evidence that the current name is implementation/version-specific?
- When would a future Inventory implementation count as the same System versus a successor System?
- What exact boundary separates Inventory 3.0 from its Apps Script application, datastore, and shared SDS/Location Resources?

### Current implementation

- What Apps Script source is current?
- What datastore is current?
- What deployment is current?
- What version is current?
- Which roadmap phases are complete?
- Which planned tests have actual execution evidence?
- Which features have been superseded since July/August 2026?
- What is the actual current SDS-registry state?

### Resources

- Which Inventory 3.0 Resources already have valid `RES-###` registrations?
- Which historical paths or URLs are stale?
- Which Resources are shared with other Projects or Systems?
- Which Resource should future Startup resolve first for live implementation work?

### Documentation / Viewer

- Will the Viewer discover this System Summary through the Projects Documentation Space?
- Can it distinguish this System Summary from the parent Project Summary?
- Should a future dedicated System Summary sidecar profile exist?
- What Viewer behavior should be reserved for a future System Identity Entity Record?

---

## 19. Next work

The System documentation layer is now sufficient for the next Project Definition test.

Next:

1. regenerate the Klinswork Documentation Viewer manifest;
2. verify discovery of the Inventory Management Project Summary sidecar;
3. verify discovery of the Inventory 3.0 System Summary sidecar;
4. verify both companions resolve correctly;
5. verify `project-identity.json` is not interpreted as a sidecar;
6. verify Project and System records are distinguishable in the Viewer;
7. reconcile any discovery or authority problems;
8. reconcile the Resource Registry for live Inventory 3.0 implementation routing;
9. test a context-naive resume sequence;
10. use the exemplar results to decide what, if anything, belongs in a future System Identity schema.

The deliberate result at this stage is:

```text
System understood
        ≠
System Identity prematurely frozen
```

---

## 20. Source and interpretation notes

This Summary is grounded in:

- the current Inventory Management Project Summary and Project Summary sidecar;
- the historical `Inventory 3.0 Roadmap`;
- July 2026 work-update/catalog records describing Inventory 3.0 construction and expansion;
- early-August documentation for the `Inventory 3.0 SDS Registry Rebuild and App Integration` implementation plan.

Interpretation rules used here:

- roadmap statements are treated as design/planning evidence unless corroborated by implementation evidence;
- work updates are treated as historical implementation evidence at the date recorded;
- current live implementation claims are not inferred from historical documents;
- unresolved IDs remain unresolved;
- mutable Resource facts are kept out of System identity;
- no System Identity schema is created by implication.
