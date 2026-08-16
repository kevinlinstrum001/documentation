# Work Queue

| Field | Current value |
|---|---|
| **Document role** | System-local orientation and navigation |
| **System** | Work Queue |
| **Parent Project** | Task Assignment and Tracking |
| **System ID** | Unassigned; no permanent `SYS-###` is being created in this documentation step |
| **System Identity Entity Record** | Not created; System Identity schema remains intentionally deferred |
| **Human-readable current-state System definition** | `summaries/system-summary.md` — current |
| **System Summary sidecar** | `sidecars/system-summary-sidecar.json` — current |
| **System Roadmap** | `summaries/work-queue-roadmap.md` — current |
| **System Roadmap sidecar** | `sidecars/work-queue-roadmap-sidecar.json` — current |
| **Technical documentation Resource** | `RES-047` — Work Queue app technical manual |
| **Documentation status** | System-local README, current-state System Summary/sidecar, and future-state roadmap/sidecar are present; discovery and companion validation completed in WORK-0001 |
| **Last reconciled** | 2026-08-16 |

---

## 1. Purpose of this README

This README is the local orientation document for the **Work Queue System**.

Its job is to help a person, tool, or future work session enter this System directory and determine:

- what Work Queue is in the current Klinswork architecture;
- which Project gives the System its operational meaning;
- which local record answers a current-state question;
- which local record answers a future-state question;
- where the technical architecture baseline lives;
- where current Resources should be resolved;
- which neighboring Projects and shared foundations affect Work Queue;
- where current implementation behavior must be verified;
- what remains unresolved;
- how to resume Work Queue work without loading unrelated Klinswork material or prematurely creating System Identity.

The governing rule is:

> **Use this README for orientation. Use the System Summary for current System interpretation, the System Roadmap for intended future direction, the Resource Registry for Resource identity/routing, and current implementation evidence for claims about what the software actually does.**

This README is not:

- a System Identity Entity Record;
- a substitute for `system-summary.md`;
- a substitute for the Work Queue roadmap;
- a live application specification;
- a Resource Registry;
- an implementation plan;
- execution evidence.

---

## 2. System context

Work Queue is the **principal known System** within the **Task Assignment and Tracking Project**.

Current semantic relationship:

```text
Klinswork
└── Operations                                      [Project]
    └── Task Assignment and Tracking                [Project]
        └── Work Queue                              [System]
```

This relationship explains the System's current organizational and operational context.

It does not encode intrinsic System identity.

The current distinction is:

```text
Task Assignment and Tracking
    = Project

Work Queue
    = principal System

Work Queue application
Google Sheets / datasets
source code
deployments
technical manuals
other implementation artifacts
    = Resources or implementation surfaces
```

The Project may survive a redesign, replacement, or renaming of Work Queue.

Likewise, Work Queue should not be reduced to one visible application screen, one spreadsheet, one deployment, or one historical implementation.

The Project Summary describes Work Queue as broader than a single application surface and identifies the detailed current-state System interpretation as the responsibility of the current System Summary.

---

## 3. Why there is no `system-identity.json` yet

This documentation layer intentionally stops short of a formal System Identity Entity Record.

No file such as:

```text
system-identity.json
```

is being created in this Project Definition pass.

No permanent:

```text
SYS-###
```

is being assigned.

That is deliberate.

The second Project Definition exemplar has validated the separation among:

- Project identity;
- Project definition;
- System orientation;
- System current-state definition;
- System roadmap;
- Resources;
- relationships and dependencies;
- implementation plans;
- execution evidence;
- history and provenance.

System Identity should be formalized only after Klinswork has enough evidence to decide:

- which facts are truly intrinsic to a System;
- how System identity differs from an application or implementation;
- how stable System names should behave across versions and replacements;
- how System IDs are allocated;
- how System relationships are registered;
- how System Identity conflicts with other authorities are reconciled.

For now:

> **Describe Work Queue accurately without pretending the System Identity architecture has already been finalized.**

---

## 4. Local records and authority

### `README.md`

This file.

Role:

- System-local orientation;
- navigation;
- reading order;
- authority routing;
- Project/System distinction;
- evidence-class guidance;
- resume-work guidance;
- explanation of the deliberate absence of formal System Identity.

It should not silently absorb authority assigned elsewhere.

---

### `summaries/system-summary.md`

**Status:**

```text
CURRENT — created 2026-08-16
```

Role:

- authoritative human-readable current-state System explanation;
- Work Queue purpose and operational role;
- current System boundary;
- current architecture;
- application/data relationships;
- task and assignment behavior;
- employee identity/assignment relationships;
- location relationships;
- history behavior;
- Inventory integration behavior;
- supporting Resources;
- technical documentation;
- current limitations;
- uncertainty and unresolved questions;
- next current-state verification work.

The System Summary should answer:

> **What is Work Queue now, based on the evidence currently available?**

It must not become a duplicate of the System Roadmap.

---

### `sidecars/system-summary-sidecar.json`

**Status:**

```text
CURRENT — created 2026-08-16
```

Role:

- machine-readable structured companion to `summaries/system-summary.md`;
- Viewer/discovery representation of supported current-state System facts;
- structured System context, Resource references, evidence basis, current limitations, and unresolved questions.

It is not:

- a System Identity Entity Record;
- the authority over the Markdown System Summary;
- proof that planned roadmap capabilities exist.

---

### `summaries/work-queue-roadmap.md`

**Status:**

```text
CURRENT — created 2026-08-16
```

Role:

- durable planned direction for Work Queue;
- target System concept;
- roadmap areas;
- capability gaps;
- integration direction;
- maturity sequence;
- candidate Work Units;
- future product determinations.

The roadmap answers:

> **What should Work Queue become?**

It does **not** prove that the desired capabilities already exist.

---

### `sidecars/work-queue-roadmap-sidecar.json`

**Status:**

```text
CURRENT
```

Role:

- structured companion to the Work Queue roadmap;
- machine-readable roadmap baseline, target state, roadmap areas, integrations, maturity sequence, Work Unit policy, and vocabulary;
- specialized System Roadmap Viewer preview source.

The roadmap sidecar structures the roadmap.

It does not replace the human-readable roadmap as authority for planned System direction.

---

### Parent Project documentation

For the durable Project context, read:

```text
../../project-identity.json
../../README.md
../../summaries/project-summary.md
../../sidecars/project-summary-sidecar.json
```

Those records answer questions such as:

- why Task Assignment and Tracking exists;
- what operational responsibility belongs to the Project;
- how Work Queue fits into the Project;
- where the Project boundary lies;
- how Scheduling, Inventory Management, Employee Profile, Building Map / Locations, Documentation, and Meadows Housekeeping relate.

System documentation should not redefine the Project.

---

### Technical documentation

The current registered Work Queue technical documentation Resource is:

```text
RES-047
Work Queue app technical manual
```

The dated technical manual provides an important architecture baseline and explains Work Queue as an ecosystem involving:

- an application layer;
- Google Sheets data;
- employee/personnel records;
- inventory relationships;
- Documentation;
- repository/publishing infrastructure;
- Google-managed files and services;
- development and integration work;
- access/publication layers;
- human operational work.

Because the manual is dated technical evidence, use it as a source for understanding and reconciliation.

Do not assume every implementation detail in it remains current without current verification.

---

### Resource Registry

Use the Resource Registry for:

- stable Resource identity;
- current location;
- current routing;
- known datastore/workbook identity;
- source/deployment pointers where registered;
- technical-document routing;
- other Resource-level facts.

Known Work Queue Resource references currently include:

```text
RES-002   Work Queue app
RES-003   Work Queue app data sheet
RES-012   Work Queue Tasks dataset
RES-013   Work Queue Employees dataset
RES-014   Work Queue Locations reference
RES-047   Work Queue app technical manual
```

These IDs identify Resources.

They do not establish System identity.

---

### Live implementation evidence

Where a claim concerns what the current Work Queue implementation actually does, verify against the appropriate current evidence:

```text
current source
current datastore / schema
current deployment
current registered Resources
current executable behavior
fresh tests / validation
```

The System Summary may interpret that evidence.

This README should not preempt it.

---

## 5. Current System-local documentation structure

Current structure:

```text
Work Queue/
├── README.md
├── summaries/
│   ├── system-summary.md                  [current]
│   └── work-queue-roadmap.md              [current]
└── sidecars/
    ├── system-summary-sidecar.json        [current]
    └── work-queue-roadmap-sidecar.json    [current]
```

There is intentionally no:

```text
system-identity.json
```

in this Project Definition pass.

---

## 6. Authority map

Use the following routing rule when entering Work Queue documentation:

| Question | Primary authority / evidence |
|---|---|
| What Project is Work Queue part of? | `../../summaries/project-summary.md` |
| What is intrinsic to the Task Assignment and Tracking Project? | `../../project-identity.json` |
| What is Work Queue now? | `summaries/system-summary.md` |
| What should Work Queue become? | `summaries/work-queue-roadmap.md` |
| What is the structured roadmap representation? | `sidecars/work-queue-roadmap-sidecar.json` |
| What is the structured current-state System representation? | `sidecars/system-summary-sidecar.json` |
| Where is the technical architecture baseline? | `RES-047` |
| What is a Resource and where is it now? | Resource Registry |
| What does the live software actually do? | current source / data / deployment / executable verification |
| What happened historically? | dated Work Updates, Activities, historical records |
| What is intended to be changed in a bounded body of work? | implementation plan |
| What actually occurred during formal implementation? | Work Implementation Session + execution evidence |
| What is current Work Unit state? | Work Unit Registry |
| What materially changed in Work Unit history? | Work Unit Activities |

A record should not acquire authority merely because it is convenient to read.

---

## 7. Current evidence classes

Work Queue has extensive historical, planning, and implementation material.

These evidence classes must remain distinct.

### 7.1 Historical implementation evidence

Examples:

- dated Work Updates;
- dated technical descriptions;
- historical screenshots;
- prior source snapshots;
- earlier Tasker / Work Queue records;
- historical deployment notes.

Historical evidence can establish:

> **What existed, was reported, or was understood at that time?**

It does not automatically establish the current state.

---

### 7.2 Planning / design evidence

Examples:

- `summaries/work-queue-roadmap.md`;
- implementation plans;
- design notes;
- unchecked candidate Work Units;
- target-state architecture.

Planning evidence establishes:

> **What was or is intended?**

It is not completion evidence.

---

### 7.3 Current implementation evidence

Examples:

- current source;
- current datastore/schema;
- current deployment;
- current Resource Registry;
- current executable behavior;
- fresh tests.

Current implementation evidence supports:

> **What does Work Queue actually do now?**

The current System Summary reconciles these evidence classes explicitly.

---

## 8. Current high-level baseline

The Work Queue roadmap and current Project definition support a bounded high-level baseline.

Work Queue is a functioning but incomplete operational System/application environment.

Documented current or previously verified capabilities include:

- creating work;
- assigning work;
- filtering and tracking work;
- updating work;
- completing work;
- Google Sheets-backed task and assignment data;
- employee records used for assignee selection;
- stable Assigned Employee ID storage rather than relying only on typed names;
- location/unit relationships;
- some Completed Jobs/history capability;
- relationships to shared Locations data;
- inventory-related completion behavior in which an applicable completed task can create an `Inventory_Holder_Event`.

Important documented limitations include:

- no reliably verified current-user identity in the running application;
- incomplete employee-facing My Work / Available Work separation;
- incomplete reject/release and supervisor-review routing;
- incomplete full inventory transfer propagation;
- Scheduling context not yet integrated as mature assignment context;
- Employee Profile integration pending;
- role-based dashboards incomplete;
- history/search/reporting capabilities incomplete;
- structured notes and image evidence incomplete;
- QR reporting and bounded OpenAI-assisted validation not implemented;
- recurring work/dailies incomplete;
- Building Map / location infrastructure incomplete for mature location-aware use.

These points are **orientation-level baseline facts**.

The current System Summary provides the detailed current-state reconciliation and qualifies claims according to their evidence.

---

## 9. Work Queue is broader than the visible application

The technical manual's core premise is that Work Queue is not merely one visible application screen.

A useful working model is:

```text
Work Queue System
│
├── operational interface / application surface
├── task and assignment data
├── employee/personnel references
├── location references
├── inventory relationships
├── workflow and validation logic
├── supporting Resources
├── development / deployment infrastructure
├── documentation and operating knowledge
└── human operational decisions and maintenance
```

The visible interface depends on structured data, stable identifiers, field compatibility, permissions, hosted assets, integration rules, and ongoing maintenance.

This supports the current System interpretation:

> **Work Queue is the coherent operating mechanism around task assignment and tracking, not merely whichever application happens to render its current user interface.**

The exact final System boundary remains unresolved in the current System Summary and is also a later System Identity question.

---

## 10. Parent Project boundary

Work Queue implements or supports the operational function represented by **Task Assignment and Tracking**.

The Project's durable responsibility is the lifecycle of discrete work.

A simplified conceptual flow is:

```text
need / request
        ↓
work identity
        ↓
review / acceptance where applicable
        ↓
assigned or available responsibility
        ↓
performance / status
        ↓
notes / evidence / exception
        ↓
completion
        ↓
verification / review
        ↓
history / reporting
        ↓
downstream effects
```

Work Queue is the current principal System supporting that function.

The Project remains meaningful even if the System later changes.

---

## 11. Integration boundaries

Work Queue participates in several important cross-System, cross-Project, or shared-data relationships.

These relationships do not become intrinsic Work Queue identity merely because the System depends on them.

### 11.1 Scheduling

Scheduling provides or is expected to provide person/place/time context.

Target relationship:

```text
Scheduling context
        ↓
Work Queue
```

The roadmap principle is:

> **Schedule informs; it does not imprison.**

Scheduling may help determine who is working and where, while Work Queue preserves actual assignment and performance history and allows legitimate supervisor changes.

---

### 11.2 Inventory Management / Inventory 3.0

Work Queue may produce inventory-related operational effects.

Current documented relationship is partial.

An applicable completed task can create an `Inventory_Holder_Event`, but current documentation does not establish complete transfer propagation from an employee cart to the destination holder.

The authority boundary is:

```text
Work Queue
    owns / preserves task lifecycle meaning

Inventory Management / Inventory 3.0
    owns / preserves inventory-state and inventory-transaction meaning
```

A task that causes an inventory effect does not make Work Queue the inventory authority.

---

### 11.3 Employee Profile / personnel context

Work Queue depends on stable employee identity for assignment and attribution.

Current evidence supports employee records and stable Assigned Employee ID usage.

The mature target includes richer Employee Profile integration.

Work Queue should consume authoritative personnel/profile context rather than becoming a competing personnel authority.

---

### 11.4 Building Map / Locations

Work Queue depends on stable shared location identity.

Current location references participate in:

- unit/location filtering;
- task location;
- inventory-holder relationships;
- reporting context.

The mature target also expects:

- complete stable locations;
- QR linkage;
- map navigation;
- task-location validation;
- schedule/location relationships;
- location-aware reporting.

The governing boundary is:

> **Work Queue consumes shared location identity; Task Assignment and Tracking does not own Building Map / Locations merely because the System uses it.**

---

### 11.5 QR Reporting

QR reporting is a planned work-intake source.

Target concept:

```text
scan QR
    ↓
resolve location / asset context
    ↓
submit report
    ↓
optional bounded validation / normalization
    ↓
pending supervisor review
    ↓
released into Work Queue
```

This remains planned capability, not current-state proof.

---

### 11.6 OpenAI assistance

The Work Queue roadmap permits a bounded advisory role for OpenAI/API-assisted validation.

The authority rule is:

> **AI may assist with interpretation, normalization, extraction, classification, or review; it does not silently become the authority for employee identity, task completion, inventory quantity, supervisor approval, or other operational truth.**

This remains target-state guidance unless current implementation evidence establishes a specific deployed capability.

---

## 12. Roadmap versus current-state System Summary

This distinction is central to the Work Queue documentation layer.

### System Summary

```text
summaries/system-summary.md
```

Answers:

> **What is Work Queue now?**

Expected basis:

- current Project definition;
- Resource Registry;
- current technical documentation;
- current implementation source/data/deployment where inspected;
- fresh verification when needed;
- dated historical evidence when chronology matters.

---

### System Roadmap

```text
summaries/work-queue-roadmap.md
```

Answers:

> **What should Work Queue become?**

The roadmap currently defines 16 roadmap areas:

1. Identity, Authentication, Roles, and Permissions
2. Role-Based Dashboards
3. Work Intake, Pending State, and Supervisor Review
4. Employee Participation and Assignment Lifecycle
5. Calendar and Scheduling Integration
6. Employee Profile Integration
7. Inventory Integration and Transaction Propagation
8. Structured Notes, Templates, Images, and Evidence
9. QR Reporting and OpenAI-Assisted Validation
10. History, Search, Audit, and Operational Inquiry
11. Reporting, Printing, and Paperwork Translation
12. Recurring Work and Dailies
13. Building Map and Location Intelligence
14. Supervisor Operations and Exception Handling
15. Notifications and Communication
16. Administration, Configuration, Reliability, and Data Integrity

These are future capability domains, including some areas with partial current behavior.

They are not a list of completed features.

---

## 13. Roadmap principles that matter to current System work

Several roadmap principles are useful architecture constraints even before the target features are implemented.

### Identity before attribution

Operational history should preserve stable employee identity wherever possible rather than relying only on display names.

### Roles are views and permissions over one System

Employee, Supervisor, and Administrator should not casually become separate Systems merely because they receive different dashboards and permissions.

### Pending work is supervisor-controlled

Target pending work should not appear as ordinary employee-available work before applicable supervisor review/release.

### Schedule context and actual work are different records

Planned staffing/location context and actual task history answer different questions.

### Inventory effects must become real inventory transactions

A holder event alone is not sufficient when the work represents actual stock movement.

### History should explain state

Where practical, important task/assignment transitions should be preserved as events rather than only overwriting current values.

### Configuration should migrate out of code

Routine administration should increasingly use governed data/configuration rather than requiring source edits.

These principles belong to target direction and architecture reasoning.

They should not be rewritten as current implementation claims unless verified.

---

## 14. Work Units and implementation planning

The Work Queue roadmap is intentionally broader than one implementation session.

Roadmap Areas organize durable capability domains.

Work Units represent bounded addressable outcomes.

Implementation plans describe intended execution for selected bounded work.

Conceptually:

```text
Task Assignment and Tracking     Project
        ↓
Work Queue                       System
        ↓
Roadmap Area                     durable planning category
        ↓
Work Unit                        bounded outcome
        ↓
Implementation Plan             intended execution
        ↓
Work Implementation Session     detailed bounded execution
        ↓
Work Unit Activities            material history
```

Do not invent `WORK-####` IDs from roadmap bullets.

The Work Unit Registry allocates stable Work Unit identity.

---

## 15. Historical terminology

Work Queue predates the current Project/System/Resource vocabulary.

Earlier records may:

- use the name `Tasker`;
- call Work Queue a Project;
- treat one application or deployment as the whole System;
- use application-centered architecture;
- contain old repository paths or URLs;
- describe planned features that were not implemented;
- accurately describe a past implementation that no longer matches the current implementation.

Preserve those records as historical evidence.

Current documentation should interpret them through the current architecture without rewriting what the older source actually said.

---

## 16. Resume-work sequence

A context-naive Work Queue session should load context progressively.

### General System work

```text
Work Queue work begins
        ↓
read this README
        ↓
read parent Task Assignment and Tracking Project Summary
        ↓
choose the question type
        ↓
CURRENT STATE or FUTURE DIRECTION
```

---

### Current-state work

```text
Work Queue README
        ↓
summaries/system-summary.md
        ↓
RES-047 technical manual where relevant
        ↓
Resource Registry
        ↓
current source / datastore / deployment
        ↓
fresh tests / executable verification
        ↓
historical evidence only when chronology matters
```

Do not use the roadmap to fill current-state gaps.

---

### Roadmap / product-direction work

```text
Work Queue README
        ↓
summaries/work-queue-roadmap.md
        ↓
sidecars/work-queue-roadmap-sidecar.json where useful
        ↓
identify bounded capability
        ↓
create / resolve Work Unit through Registry
        ↓
implementation plan when selected
```

Do not turn every roadmap bullet into a Work Unit automatically.

---

### Integration work

```text
Work Queue README
        ↓
System Summary
        ↓
identify integration boundary
        ↓
load authoritative neighboring Project/System records
        ↓
resolve shared Resources
        ↓
inspect current implementation contract
        ↓
record uncertainty before changing cross-System behavior
```

Examples:

- Scheduling;
- Inventory Management / Inventory 3.0;
- Employee Profile;
- Building Map / Locations;
- QR Reporting;
- Documentation.

---

## 17. Current questions by destination

### What is Work Queue?

Read:

```text
README.md
summaries/system-summary.md
```

The System Summary is the main human-readable current-state answer.

---

### Why does Work Queue exist?

Read the parent Project:

```text
../../summaries/project-summary.md
```

Task Assignment and Tracking provides the durable Project meaning.

---

### What should Work Queue become?

Read:

```text
summaries/work-queue-roadmap.md
sidecars/work-queue-roadmap-sidecar.json
```

---

### Where are the current app/data Resources?

Resolve through the Resource Registry, especially:

```text
RES-002
RES-003
RES-012
RES-013
RES-014
RES-047
```

---

### What does the current software actually do?

Use current implementation evidence:

```text
source
datastore/schema
deployment
current Resource records
fresh test / executable behavior
```

---

### What did Work Queue do at an earlier date?

Use dated historical evidence.

Do not silently convert dated truth into current truth.

---

### What work should be implemented next?

Use:

```text
roadmap
    ↓
bounded Work Unit
    ↓
implementation plan
```

---

## 18. Current unresolved questions

The following remain open and should remain visible until evidence or formal architecture resolves them.

### 18.1 System identity

- What permanent `SYS-###` value, if any, will Work Queue receive?
- What authority allocates that ID?
- What stable facts belong in a future System Identity Entity Record?
- What is the final System boundary?
- Should a separate Application / Implementation entity exist beneath Work Queue?
- Is `Work Queue` the permanent canonical System name?

### 18.2 Current implementation

- Which current application source is authoritative?
- Which current deployment is authoritative?
- Which datastore/workbook and schema are authoritative?
- Which technical-manual claims remain current?
- What exact task state model is currently implemented?
- What exact history behavior is currently implemented?
- Which permissions are currently enforced?
- Which tests currently pass?
- Which limitations are verified versus inherited from recent planning/history?

### 18.3 Employee identity and roles

- How is the current acting user established?
- Which employee identity authority should Work Queue consume?
- What is the final role model?
- How should one person holding multiple roles be represented?
- Which actions require server-side role enforcement?

### 18.4 Task lifecycle

- What are the final controlled states?
- What is the exact meaning of assigned, unassigned, pending, in progress, completed, blocked, deferred, cancelled, and reopened?
- Which transitions require supervisor action?
- Which transitions must be preserved as immutable events?

### 18.5 Scheduling

- Which Scheduling System/Resource is authoritative?
- How is current scheduled employee/location context consumed?
- What may supervisors override?
- How should planned-versus-actual work be preserved?

### 18.6 Inventory

- What is the exact Work Queue → Inventory transaction contract?
- How is acting employee → employee cart resolved?
- How are source decrement and destination increment made atomic/reconcilable?
- How is duplicate transfer prevented?
- How are corrections/reversals represented?

### 18.7 Locations / Building Map

- What is the authoritative shared location model?
- Which current location IDs are stable?
- What gaps remain before QR reporting and map navigation can depend on the model?
- How are task, schedule, inventory-holder, and map location references reconciled?

### 18.8 Evidence and reporting

- What structured note model is needed?
- What image/evidence retention and permission rules apply?
- Which history/search queries are operationally important?
- Which reports must be printable?
- What paperwork-translation outputs are genuinely required?

### 18.9 QR / AI

- What QR identities should be registered?
- What report fields are authoritative?
- What validation may the OpenAI API assist with?
- What fallback exists when AI is unavailable or uncertain?
- What privacy and retention rules apply to text/images sent for advisory processing?

### 18.10 Documentation architecture

- What Viewer semantics should distinguish a System Summary from a future System Identity record?
- Which parts of this Work Queue documentation layer are generic enough for future System Definition templates?
- What evidence threshold should be required before Klinswork formalizes System Identity?

Do not resolve these questions merely to make the documentation package appear complete.

---

## 19. Current System documentation state

As of 2026-08-16:

### Complete / present

```text
Work Queue recognized as principal System
System directory present
README.md present
summaries/system-summary.md present
sidecars/system-summary-sidecar.json present
summaries/work-queue-roadmap.md present
sidecars/work-queue-roadmap-sidecar.json present
parent Task Assignment and Tracking Project-level definition package complete
RES-047 technical documentation available
known Work Queue Resource references identified
System Summary and roadmap companions resolved by the source-aware Viewer manifest
current-state and future-state Viewer semantics validated together
context-naive resume routing validated
```

### Remaining in WORK-0001

```text
reconcile creation-time status annotations in current human-readable documents
finish the formal Work Implementation Session record
review the WORK-0001 completion rule
close the session and Work Unit if the completion rule remains satisfied
```

### Deliberately deferred

```text
permanent SYS-### assignment
system-identity.json
final System Identity Record Profile
formal Relationship Registry implementation
broad Work Queue feature development
datastore redesign
universal reusable System Definition template extraction
```

---

## 20. Next work

The Work Queue System-definition package for WORK-0001 is complete and validated:

```text
README.md
summaries/system-summary.md
sidecars/system-summary-sidecar.json
summaries/work-queue-roadmap.md
sidecars/work-queue-roadmap-sidecar.json
```

No additional Work Queue System-definition artifact is required before closing the current Project Definition Work Unit.

The immediate WORK-0001 work is closure-oriented: reconcile remaining creation-time status annotations, finish the formal Work Implementation Session record, review the Work Unit completion rule, and close the session/Work Unit if the rule remains satisfied.

Future Work Queue feature development should be selected from the System Roadmap through bounded Work Units rather than being silently folded into this Project Definition session.

---

## 21. Governing rule

The local System documentation layer should make Work Queue understandable without collapsing the authorities around it.

The governing interpretation is:

```text
Task Assignment and Tracking
    = Project / durable operational undertaking

Work Queue
    = principal System

System Summary
    = current human-readable System interpretation

System Roadmap
    = intended future System direction

System Summary sidecar
    = structured companion to current-state interpretation

Roadmap sidecar
    = structured companion to planned direction

Resources
    = concrete application/data/source/deployment/document artifacts

Resource Registry
    = Resource identity and routing authority

Current source/data/deployment/tests
    = live implementation evidence

Work Units
    = bounded addressable work

Implementation Plans
    = intended bounded execution

Work Implementation Sessions
    = detailed execution records

Work Unit Activities
    = material Work Unit history
```

If a future work session can enter this directory, identify the question it is trying to answer, and route itself to the correct authority without conflating current state, future direction, Project identity, System identity, Resources, or historical evidence, this README is doing its job.
