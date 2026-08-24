# Inventory 3.0 Roadmap

**Document type:** System roadmap  
**System:** Inventory 3.0  
**Project context:** Inventory Management  
**Status:** Working target-state roadmap  
**Created:** 2026-08-16  
**System ID:** Unassigned  
**Project ID:** Unassigned  
**Governing Work Unit:** WORK-0006

## 1. Purpose

This roadmap defines the durable planned direction for Inventory 3.0 as it develops from a functioning, Sheets-backed inventory application into a mature Klinswork inventory-control, material-state, transaction-history, reconciliation, and integration system.

The roadmap is intentionally broader than an implementation plan. It describes desired capabilities, operating invariants, cross-System responsibilities, and bounded capability areas. Individual Work Units and implementation plans can later be derived from this roadmap without turning the roadmap itself into a list of code edits.

Inventory Management is the Project. Inventory 3.0 is the principal System supporting that Project. The Project documentation governs the meaning of the real-world inventory operation; this roadmap governs the planned direction of the System that represents and supports it.

## 2. Current baseline

Inventory 3.0 already functions as an operational web application built with Google Apps Script and Google Sheets.

Verified current capabilities include:

- location-first inventory browsing;
- product search;
- category filtering;
- in-stock filtering;
- product-detail and standalone product views;
- product images where supplied;
- manufacturer/product reference links where supplied;
- SDS links where an SDS record exists;
- opening-balance entry;
- receiving inventory;
- recording use;
- upward and downward corrections;
- generic location-to-location transfers;
- active Product and Location validation for inventory-changing operations;
- no-negative inventory enforcement;
- script locking around inventory-changing operations;
- maintained Current Inventory state plus appended Inventory Event evidence;
- best-effort compensating rollback for multi-step write failures;
- responsive browser presentation.

The current Inventory 3.0 workbook contains the principal stores Products, SDS, Locations, Current Inventory, Inventory Events, and Inv2_Archive.

The current event vocabulary includes:

- `OPENING_BALANCE`;
- `RECEIVED`;
- `USED`;
- `CORRECTION_UP`;
- `CORRECTION_DOWN`;
- `TRANSFER`.

The current implementation also participates in a broader operational data environment. Shared Locations, Inventory_Holders, Inventory_Holder_Events, and Work Queue task structures already represent physical service endpoints and task-linked holder-state changes.

Important current limitations include:

- the web client does not yet provide a completed user-facing Inventory History interface even though Inventory Events are persisted;
- Work Queue completion can create holder-state evidence, but does not yet produce the corresponding Inventory 3.0 deduction from the completing employee's personal cart;
- Inventory Events do not yet preserve complete cross-System provenance such as Work Queue task ID, Holder Event ID, source System, correlation ID, and idempotency key;
- employee attribution is currently based primarily on Apps Script active-user email where available rather than a durable Employee-to-Cart relationship;
- Inventory 3.0 still maintains local `LOC-*` identifiers while the shared Locations / Building Map model is intended to become canonical physical context;
- the current holder table does not fully represent the broader domain needs of shelves, multi-product or restricted-product holders, target/par levels, or lot/expiration-aware stock;
- SDS population is incomplete for the full active chemical set;
- current workbook data contains known quality issues, including partial shared-location mapping and at least one observed orphan Current Inventory location identifier;
- formal reversal, audit, reporting, printing, QR operation, and administrative editing workflows remain incomplete or absent;
- deployment-to-inspected-source correspondence remains to be explicitly verified.

The roadmap must continue to distinguish verified current behavior from planned target behavior.

## 3. Target product concept

The mature Inventory 3.0 should operate as the inventory-control and material-state authority for Klinswork-supported housekeeping inventory while allowing routine inventory changes to arise automatically from the operational action that caused them when enough trustworthy context exists.

In the mature model:

1. Supply Room, housekeeping closet, employee cart, and Inventory Holder stock movements are represented explicitly and consistently;
2. material state is attributable to stable Product, Location, Holder, Employee, task, and transaction identities where those identities exist;
3. routine Work Queue restock completion can create the appropriate Inventory transaction without requiring duplicate manual entry;
4. manual Inventory controls remain available for receiving, direct use, corrections, reconciliation, recovery, and exceptions;
5. Current Inventory and Inventory Events remain reconcilable representations of current state and transaction evidence;
6. cross-System operations are idempotent and preserve enough provenance to explain why a material change occurred;
7. shared Locations / Building Map supplies canonical physical identity once the transition is complete;
8. Inventory Holders and Assets represent real physical storage/dispensing structures without forcing every holder into a one-product/one-capacity model;
9. lot and expiration information can be preserved where operationally necessary;
10. Products and SDS information are complete enough to support safe and reliable inventory use;
11. supervisors can understand closet stock, replenishment needs, exceptions, and discrepancies;
12. employees can understand their personal cart inventory and relevant replenishment actions;
13. history, search, reports, and audits can reconstruct stock movement by product, place, employee, task, and time;
14. routine administration increasingly occurs through data/configuration rather than source-code edits;
15. deployed behavior, source version, datastore state, and documentation can be checked against one another without guesswork.

## 4. Governing product principles

### 4.1 Inventory 3.0 is the material-state authority, not the only operational interface
Routine work should be performed in the System best suited to the work. Work Queue can own task completion while Inventory 3.0 owns the resulting material meaning and quantity integrity.

### 4.2 Project truth and System representation remain distinct
The Inventory Management Project defines the real inventory operation. Inventory 3.0 represents that operation technically. A limitation of the current schema does not redefine the physical domain.

### 4.3 Routine operational effects should not require duplicate entry
When a Work Queue task already supplies trustworthy employee, task, location, holder, product, quantity, and completion context, the corresponding Inventory effect should be generated automatically rather than re-entered manually.

### 4.4 Manual controls are exception and recovery tools, not defects
Opening balance, receive, use, correction, transfer, and future reversal/reconciliation controls remain necessary even as automation expands.

### 4.5 History should explain state
Current quantity alone is insufficient. Material state should be supported by event evidence that explains how it changed.

### 4.6 Current state and event evidence must reconcile
Inventory 3.0 deliberately maintains both Current Inventory and Inventory Events. Neither should drift silently from the other.

### 4.7 No-negative inventory is a System invariant
Routine transactions must not reduce tracked source stock below available quantity unless an explicit reconciliation workflow is being used to correct a known state error.

### 4.8 Cross-System effects must be idempotent
Retries, callbacks, page refreshes, duplicate completion signals, or repeated integration calls must not apply the same material movement twice.

### 4.9 Physical identity should converge on shared Locations
Inventory-local location identifiers may remain during transition, but physical place identity should not be permanently duplicated across Systems.

### 4.10 Holder behavior is typed, not universal
A one-roll dispenser, four-roll dispenser, two-bundle towel dispenser, cabinet, J-Fill position, shelf, and expiration-sensitive soap holder have different capacity and stock semantics. Holder Type should govern behavior where appropriate.

### 4.11 Capacity, target level, and current quantity are different concepts
Maximum physical capacity, desired par/target level, and observed current stock should not be collapsed into one field.

### 4.12 Unknown remains unknown
Missing or unverified values should not be silently filled by assumption. Reconciliation should preserve uncertainty until evidence establishes the value.

### 4.13 Product identity should remain stable
Product descriptions, manufacturers, package sizes, or status may change without requiring historical transaction identity to be rewritten.

### 4.14 Deployment identity, source identity, and runtime behavior are separate facts
The registered app route, Apps Script project, inspected source, and currently executing deployment version must be verified rather than assumed to be identical.

# 5. Roadmap Areas

## RA-01 — Inventory State, Ledger, and Reconciliation
**Target:** Maintain trustworthy current quantity state with event evidence that can be reconciled and investigated.

Candidate Work Units: Current Inventory Referential Integrity; Inventory Event Completeness; State/Event Reconciliation Procedure; Reconciliation Dashboard or Report; Discrepancy Classification; Controlled State Repair; Event Replay Investigation; Unknown-versus-Zero Rules; Inventory Opening-State Governance.

Open determinations: whether Inventory Events eventually become a replay-capable authority or remain supporting evidence for maintained state; what discrepancy thresholds should trigger review; which repairs require explicit approval.

## RA-02 — Receiving and External Intake
**Target:** Represent material entering the tracked Inventory network with enough source, quantity, product, and evidence to support later reconciliation.

Candidate Work Units: Receiving Workflow; Receiving Source/Vendor Context; Requisition-to-Receipt Linkage; Partial Receipt; Receipt Exception Handling; Receipt Evidence/Notes; Receiving History and Search.

Open determination: permanent boundary between Inventory 3.0 and requisition/procurement tracking.

## RA-03 — Internal Transfers and Replenishment
**Target:** Model ordinary physical stock movement between tracked inventory locations consistently.

```text
Supply Room
    ↓ supervisor replenishment
Housekeeping Closet
    ↓ employee cart replenishment
Personal Employee Cart
```

Candidate Work Units: Supply Room → Closet Transfer; Closet → Employee Cart Transfer; Generic Location Transfer Hardening; Transfer Notes and Reason Codes; Transfer Provenance; Transfer Confirmation; Transfer Exception Handling; Transfer History; Transfer Reversal/Correction.

Required invariants: source and destination reconcile; source cannot go below available stock; one transfer produces one correlated material movement; failed multi-step writes cannot be reported as successful.

## RA-04 — Direct Use, Consumption, Loss, and Other Inventory-Out Boundaries
**Target:** Preserve meaningful inventory-out transactions for products or circumstances that do not terminate in a modeled Inventory Holder.

Candidate Work Units: Direct Use; Loss / Damage / Disposal Reasoning; Chemical Consumption Recording; Liner/Consumable Use; Inventory-Out Reason Codes; Exceptional Inventory-Out Review; Direct-Use History.

Design rule: `USED` or an evolved inventory-out model should remain available for genuine direct-consumption or loss boundaries. It should not be forced to represent mature cart-to-holder restock when the destination holder is explicitly modeled.

## RA-05 — Employee Cart Inventory
**Target:** Treat each personal cart as a durable movable inventory location associated with one Employee, while keeping cart assignment distinct from unit assignment and daily work assignment.

Candidate Work Units: Employee → Cart Registry; Cart Location Normalization; Employee Cart Inventory View; Cart Replenishment; Cart Assignment History; Temporary Cart Substitution; Floater Cart Source Rules; Cart Stock Exceptions.

Open determinations: whether a personal cart follows the Employee through unit reassignment without physical-location remapping; temporary cart sharing; normal replenishment source for floaters.

## RA-06 — Housekeeping Closet Inventory and Supervisor Replenishment
**Target:** Represent housekeeping closets as operational inventory places for which the supervisor holds custodial/process responsibility.

Candidate Work Units: Closet Location Normalization; Closet Stock View; Closet Par/Target Levels; Supervisor Replenishment Workflow; Closet Check Record; Low-Stock Exception; Closet Reconciliation; Closet Replenishment History.

Design rule: a unit-assigned Employee may be operationally associated with the unit's closet, but the closet is not the Employee's inventory property. Supervisor custodial responsibility and employee cart inventory are separate relationships.

## RA-07 — Inventory Holders, Assets, Holder Stock, and Capacity
**Target:** Represent real physical service endpoints and storage positions in which inventory resides or is dispensed.

Working vocabulary:
- Location — place in the building hierarchy.
- Asset — physical equipment or fixture at a Location.
- Inventory Holder — bounded storage/dispensing position inside a Location or Asset.
- Holder Type — reusable behavioral definition.
- Holder Stock — material currently installed or stored.
- Stock Lot / Inventory Lot — stock instance where lot/expiration identity matters.

Known examples include one-roll and four-roll TP dispensers, six-roll cabinets, one/two-bundle C-fold dispensers, expiration-sensitive soap/sanitizer holders, J-Fill stations with multiple chemical positions, and multi-product shelves.

Candidate Work Units: Holder Type Registry; Capacity Unit Model; Target/Par Level Model; Fixed Product Holder Rule; Restricted Product Holder Rule; Multi-Product Holder Rule; Holder Stock Model; Asset ↔ Holder Relationship; J-Fill Asset Model; Shelf Holder Investigation; Holder Quantity Capture; Holder Condition/State Model.

## RA-08 — Work Queue Integration and Transaction Propagation
**Target:** Make qualifying Work Queue completion produce a complete, attributable, reconciled Inventory transaction.

```text
completed restock task
        ↓
resolve completing Employee
        ↓
resolve Employee's personal Cart
        ↓
resolve Product + actual quantity placed
        ↓
validate destination Holder
        ↓
create correlated Inventory material event
        ↓
decrease source cart stock
        ↓
create/retain Holder Event
        ↓
correlate task + holder + holder event + inventory event
        ↓
prevent duplicate execution
```

Candidate Work Units: Work Queue → Inventory Integration Contract; Acting Employee → Cart Resolution; Inventory Product Resolution; Restock Quantity Capture; Destination Holder Resolution; Source Cart Deduction; Holder Restock Material Event; Task → Inventory Event Linkage; Holder Event → Inventory Event Linkage; Cross-System Correlation ID; Idempotency Key; Duplicate-Execution Protection; Integration Failure Recovery; End-to-End Integration Audit.

Required validation: once propagation exists, trace one controlled restock through Task/Task_Activity, Holder Event, holder state, Inventory Event, cart decrement, provenance, and safe replay proving no duplicate deduction.

## RA-09 — Employee Identity, Attribution, and Operational Provenance
**Target:** Attribute inventory-changing actions to durable operational identity rather than only display labels or active-user email.

Candidate Work Units: Employee Identity Resolution; Employee ID on Inventory Events; Employee ↔ Cart Resolution; Actor/Employee Distinction; Supervisor Attribution; Source-System Attribution; Task Provenance; Holder Provenance; Correlation/Origin Metadata.

## RA-10 — Product Management, Units, and Product Lifecycle
**Target:** Maintain stable, validated Product identities with clear inventory units and lifecycle behavior.

Candidate Work Units: Product Data Cleanup; Inventory Unit Vocabulary; Product Validation Rules; Product Administration UI; Product Deactivation; Product Replacement/Supersession; Product Merge Investigation; Product Referential-Integrity Audit.

Open determination: canonical units of measure and package-to-inventory-unit conversion rules.

## RA-11 — SDS and Chemical Information
**Target:** Ensure chemical inventory records can reliably reach the current controlled SDS and related chemical reference information.

Candidate Work Units: SDS Coverage Reconciliation; SDS Onboarding Rule; SDS Current-Version Rule; SDS Verification Workflow; Chemical Product Catalog Linkage; Missing-SDS Warning/Block; SDS Revision History; Product/SDS Integrity Audit.

Boundary rule: Inventory 3.0 should expose controlled chemical references without silently becoming the authority for all chemical-safety policy.

## RA-12 — Locations, Building Map, and Physical Identity
**Target:** Converge Inventory 3.0 on the shared physical-location model while preserving transition compatibility.

Candidate Work Units: Location Authority Decision; Inventory `LOC-*` Mapping Audit; Shared Location Adoption; Location Mapping Migration; Orphan Location Reconciliation; Inventory-Enabled Location Rules; Holder-Eligible Location Rules; Movable Cart Location Model.

Open determination: permanent authority/synchronization rule between Inventory-local IDs and shared physical Locations.

## RA-13 — Lots, Expiration, and Stock Instance Tracking
**Target:** Preserve stock-instance information where product safety or operational control requires more than aggregate quantity.

Candidate Work Units: Stock Lot Model; Lot/Expiration Capture at Receipt; Lot Movement Through Locations; Cart Lot Tracking Investigation; Holder Lot Tracking; Expiration Warning; Expired Stock Removal; Lot History and Audit.

Open determinations: which Products require lot tracking; useful granularity at closet/cart/holder levels; explicit vs rule-based lot selection.

## RA-14 — History, Search, and Operational Inquiry
**Target:** Make Inventory state and material movement discoverable without opening raw spreadsheet tabs.

Search dimensions: Product; Location; Employee; Event type; date/date range; source/destination; Work Queue task; Holder; Holder Event; correction/reconciliation reason; lot/expiration.

Candidate Work Units: User-Facing Inventory History; Product History; Location History; Employee/Cart History; Date-Range Search; Event-Type Search; Multi-Filter Search; Transaction Detail View; Cross-System Trace View; Inventory Timeline.

## RA-15 — Reporting, Printing, Dailies, and Operational Evidence
**Target:** Produce useful inventory reports from authoritative state and transaction data and connect operational paperwork/evidence without duplicating truth.

Report families: Current Stock by Location; Supply Room Stock; Closet Stock; Employee Cart Stock; Low/Below-Target Stock; Product Movement; Receiving; Transfer; Inventory-Out; Correction/Reconciliation; SDS Completeness; Expiration/Lot.

Dailies relationship: employees currently record inventory usage on paper “dailies.” The mature architecture should determine whether/how that evidence becomes structured Inventory evidence without duplicate or contradictory entry.

Candidate Work Units: Reporting Query Model; Current Stock Report; Location Stock Report; Employee Cart Report; Low-Stock Report; Movement Report; Reconciliation Report; Print Layout System; Dailies Field Investigation; Dailies → Inventory Translation Investigation.

## RA-16 — Corrections, Reversals, Audit, and Exception Handling
**Target:** Correct modeled state while preserving what happened and why.

Candidate Work Units: Correction Reason Model; Transaction Reversal; Reversal Linkage; Reconciliation Case Record; Exception Review Queue; Audit Trail; Correction Analytics; Partial-Failure Recovery.

Design rule: correction should repair modeled state without erasing evidence of prior state or transaction.

## RA-17 — QR and Context-Aware Inventory Operations
**Target:** Use QR codes where they reduce navigation or identification errors without making scanning mandatory.

Candidate Work Units: Inventory QR Context Model; Location QR Routing; Cart QR Routing; Holder/Asset QR Routing; Product Scan Investigation; QR Transfer Workflow; QR Audit Workflow; Manual Fallback Rules.

## RA-18 — Administration, Reliability, Deployment, and Data Integrity
**Target:** Make Inventory 3.0 maintainable, diagnosable, and safe to evolve.

Candidate Work Units: Data Integrity Validator; Orphan Reference Report; Product/Location Normalizer; Deployment Version Verification; Time-Zone Normalization Policy; Integration Idempotency Store; Error/Failure Logging; Maintenance Dashboard; Inv2_Archive Migration Decision; Backup/Recovery Procedure; Configuration Administration.

Open determinations: long-term Sheets datastore viability; deployment/version evidence; Inventory 2 archive disposition.

# 6. Cross-System and Shared-Data Relationships

## 6.1 Work Queue
Current relationship: partial operational integration. Work Queue owns task lifecycle and holder-linked work evidence. Inventory 3.0 owns material quantity/state effects.

## 6.2 Shared Locations / Building Map
Current relationship: partial mapping / transitional authority. Shared Locations is the intended canonical physical context.

## 6.3 Inventory Holders and Holder Events
Current relationship: implemented service-endpoint state model, incomplete material propagation. Holder state and bulk state are complementary.

## 6.4 Employee records / future Employee Profile capability
Inventory automation requires durable Employee identity and personal-cart resolution without duplicating personnel/profile truth.

## 6.5 Scheduling / Calendar
Potential relationship: operational context about who is working and where; it should not redefine durable Employee ↔ Cart assignment or transaction truth.

## 6.6 Chemical Product Catalog / SDS documentation
Inventory Product identity and controlled SDS/chemical references should remain cross-referenced and internally consistent.

# 7. Maturity Sequence

## Sequence 1 — Integrity and identity foundation
Current state/event reconciliation; Product and Location cleanup; Employee ↔ Cart identity; shared-location authority; deployment/version verification; provenance requirements.

## Sequence 2 — Real operational stock flow
Supply Room → Closet; Closet → Cart; cart visibility; holder-model refinement; Work Queue propagation; idempotency and failure recovery.

## Sequence 3 — Reconciliation and supervisory control
Closet target/par; receiving exceptions; corrections/reversals; audit/reconciliation; low-stock and discrepancy reporting.

## Sequence 4 — Inquiry, evidence, and safety completeness
History; search; reporting/printing; dailies relationship; SDS completeness; lot/expiration where required.

## Sequence 5 — Operational convenience and administrative maturity
QR operations; administrative UI; richer dashboards; automated integrity checks; maintenance tooling; archive/migration decisions; long-term persistence review.

# 8. Work Unit derivation policy

Roadmap Areas are durable capability areas, not Work Units themselves. Candidate Work Units are descriptive proposals only and receive no `WORK-####` identifier until sufficiently bounded and assigned by the Work Unit Registry.

A candidate is ready when it has one coherent outcome, a clear completion condition, known/discoverable evidence, a reasonable Project/System boundary, and explicit-enough dependencies.

Prefer capability outcomes over code-edit descriptions.

# 9. Open architectural determinations

- permanent authority/synchronization rule between Inventory-local `LOC-*` IDs and shared physical Locations;
- durable Employee → personal Cart resolution and assignment-history rules;
- floater replenishment/source rules;
- temporary cart-sharing/substitution rules;
- closet check frequency, par/target rules, and evidence requirements;
- exact dailies fields and whether/how dailies become structured inventory evidence;
- requisition/procurement boundary for receiving;
- canonical units of measure and conversion rules;
- quantity-versus-state rules for Inventory Holders;
- shelf representation;
- J-Fill measurement semantics;
- lot/expiration applicability and granularity;
- Inventory Event provenance fields and cross-System correlation schema;
- idempotency mechanism for Work Queue-driven inventory effects;
- formal reversal and audit/reconciliation workflow;
- long-term authority relationship between Current Inventory and Inventory Events;
- whether/how Inv2_Archive should be migrated;
- minimum SDS completeness requirements for chemical onboarding;
- deployment-to-source correspondence for the current registered route;
- long-term datastore architecture if Sheets transaction limits become material.

# 10. Roadmap maintenance rules

1. Keep current implementation, history, target direction, and open determinations distinguishable.
2. Do not promote planned capability to current merely because it appears in this roadmap.
3. Update current baseline only from strong present-tense evidence.
4. Keep Project-domain semantics in Inventory Management documentation and implementation mechanics in technical documentation.
5. Preserve historical roadmap versions or material revisions when substantial direction changes.
6. Record Work Unit IDs only after Registry assignment.
7. Do not assign Project or System IDs from this roadmap.
8. Update the System Roadmap Catalog when this roadmap is created, superseded, archived, or materially reclassified.
9. Keep the structured sidecar aligned with the human-readable roadmap; the roadmap remains authoritative for planned System direction.

# 11. Source basis and verification boundary

This roadmap was created from the WORK-0006 reconciliation effort and is grounded in the current Inventory Management Project/domain documentation, rebuilt Inventory technical manual, current Apps Script source inspection, current Inventory workbook inspection, shared Locations/Holder evidence, Work Queue integration evidence, the existing Inventory System Summary and sidecar, the Work Queue roadmap pattern, historical Inventory planning where explicitly treated as history/planning, and the 2026-08-16 WORK-0006 target-state discussion.

This roadmap does **not** claim that target capabilities already exist. It also does not resolve the still-open correspondence between the inspected source and the exact code serving the registered deployment.
