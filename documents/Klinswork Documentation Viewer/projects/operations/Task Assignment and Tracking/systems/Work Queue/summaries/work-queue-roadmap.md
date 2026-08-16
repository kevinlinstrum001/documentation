# Work Queue Roadmap

**Document type:** System roadmap  
**System:** Work Queue  
**Project context:** Task Assignment and Tracking  
**Status:** Working target-state roadmap  
**Created:** 2026-08-16  
**System ID:** Unassigned  
**Project ID:** Unassigned

## 1. Purpose

This roadmap defines the durable planned direction for Work Queue as it develops from a functioning but incomplete operational application into a mature Klinswork work-assignment, participation, evidence, history, reporting, and integration system.

The roadmap is intentionally broader than an implementation plan. It describes desired capabilities and bounded capability areas. Individual Work Units and implementation plans can later be created from this roadmap without turning the roadmap itself into a list of code edits.

## 2. Current baseline

Work Queue already functions as an operational application. Current and previously documented capabilities include:

- creating, assigning, filtering, tracking, updating, and completing housekeeping work;
- Google Sheets-backed task and assignment data;
- employee records used for assignee selection;
- stable Assigned Employee ID storage rather than relying only on typed names;
- unit/location-based work filtering;
- a Completed Jobs/history view to some extent;
- relationships to shared Locations data;
- inventory-related task behavior in which completing an applicable task can create an `Inventory_Holder_Event`.

Important current limitations include:

- the running application does not yet establish a verified identity for the current user;
- employee-facing work is not yet separated into a personal queue and an available-work queue;
- task rejection/release and supervisor-review routing are not yet complete;
- inventory-holder events do not yet complete the corresponding inventory transfer from the employee cart to the destination holder;
- schedule information is not yet used as flexible employee/location context;
- history, search, reporting, notes, media, recurring work, and role-specific dashboards remain incomplete;
- several planned integrations do not yet exist or remain only partial.

The roadmap must continue to distinguish verified current behavior from planned target behavior.

## 3. Target product concept

The mature Work Queue should operate as a role-aware operational work system in which:

1. the application knows who is acting;
2. the user's role determines dashboard, permissions, and available actions;
3. supervisors can review, release, assign, prioritize, and monitor work;
4. employees can see their work and eligible unassigned work, claim work, reject or release work, document performance, and complete work;
5. pending work remains in a supervisor-controlled review state and is not exposed as available employee work;
6. Calendar/Scheduling supplies flexible context about who is working and where;
7. Employee Profile supplies durable personnel identity and profile context when that system exists;
8. Inventory integration converts inventory-related task completion into real, attributable inventory transactions;
9. structured notes and images preserve evidence and operational context;
10. QR reporting creates context-aware work requests and can use the OpenAI API for bounded validation/normalization assistance;
11. recurring work supports dailies and other repeatable work patterns;
12. history and search make work discoverable by employee, unit, location, status, task type, and time period;
13. reports can be viewed and printed;
14. paperwork-translation capabilities can turn structured operational records into required human-facing paperwork and support later structured capture where appropriate;
15. building-map/location data is complete enough to support meaningful location-aware work;
16. administrative tools allow routine configuration without source-code edits;
17. the event/history model preserves who did what, when, where, and what downstream effects occurred.

## 4. Governing product principles

### 4.1 Identity before attribution

Names displayed to users are labels. Operational history should use stable employee identity wherever possible.

### 4.2 Roles are views and permissions over one system

Administrator, Supervisor, and Employee should not become separate applications. They should receive different dashboards, controls, and permissions over shared authoritative records.

### 4.3 Pending work is supervisor-controlled

A task may be pending, assigned, or unassigned. Pending work is not part of the employee-available queue. It must first pass the applicable supervisor review/release step.

### 4.4 Assigned and unassigned are participation states, not quality judgments

Released work can become unassigned and return to an eligible queue without implying completion or cancellation.

### 4.5 Schedule informs; it does not imprison

Schedule/Calendar context should help Work Queue know who is working and where, but supervisors must retain the ability to make legitimate operational changes.

### 4.6 Planned work and actual work remain distinguishable

Schedule data describes expected staffing/location context. Work Queue history describes actual assignment and performance.

### 4.7 Inventory effects must be real transactions

Creating an inventory-holder event is not enough when a task represents stock movement. The source cart, destination holder, quantity, product, employee, task, and transaction history must reconcile.

### 4.8 History should explain state

Where practical, important task and assignment transitions should be preserved as events rather than only overwriting the current row.

### 4.9 AI assistance is bounded

OpenAI API use may assist with validation, normalization, classification, extraction, or review of reports and images. It should not silently become the authoritative source for employee identity, task completion, inventory quantity, supervisor approval, or other operational truth.

### 4.10 Configuration should migrate out of code

Ordinary administration of employees, roles, task types, locations, templates, and recurring-work definitions should increasingly be data/configuration-driven.

# 5. Roadmap Areas

## RA-01 — Identity, Authentication, Roles, and Permissions

**Target:** Establish reliable current-user identity and role-aware access.

### Candidate Work Units

- **Employee Identity** — establish the current application user, resolve the user to a stable employee ID, and preserve employee ID on attributable actions.
- **User Session Context** — make employee identity, role, and relevant work context available throughout the application session.
- **Role Resolution** — support at least Employee, Supervisor, and Administrator roles; allow one person to hold more than one authorized role where appropriate.
- **Permission Enforcement** — define and enforce which actions each role may perform, including server-side enforcement.

### Open determinations

- exact login/authentication mechanism;
- whether Google Workspace identity is sufficient;
- how non-employee administrators are represented;
- how temporary or substitute personnel are handled.

## RA-02 — Role-Based Dashboards

**Target:** Present each user with an operationally appropriate home view.

### Employee Dashboard

- My Work;
- Available Work;
- work requiring action;
- recent completions/history;
- current schedule/location context;
- relevant alerts or returned items.

### Supervisor Dashboard

- employees expected/currently working;
- employee location context;
- assigned work;
- unassigned work;
- pending work;
- rejected/released work awaiting review;
- overdue/unfinished work;
- exception indicators;
- operational counts and quick filters.

### Administrator Dashboard

- employee/role administration;
- configuration;
- data-integrity status;
- template and lookup maintenance;
- integration/configuration health;
- diagnostic information appropriate to administrators.

### Candidate Work Units

- Employee Dashboard
- Supervisor Dashboard
- Administrator Dashboard
- Shared Dashboard Metrics
- Role-Aware Navigation

## RA-03 — Work Intake, Pending State, and Supervisor Review

**Target:** Separate proposed/pending work from employee-visible actionable work.

### Intended state model

```text
CREATED / SUBMITTED
        ↓
PENDING SUPERVISOR REVIEW
        ↓
RELEASED
   ↙           ↘
ASSIGNED     UNASSIGNED / AVAILABLE
```

Employees should not see the pending list as available work.

### Candidate Work Units

- Pending Work State
- Supervisor Review Queue
- Approve/Release Work
- Return for Clarification
- Reject/Cancel Proposed Work
- Release as Assigned
- Release as Unassigned
- Pending-Visibility Rules

### Future inputs to review

Pending work may originate from:

- supervisor-created tasks;
- employee submissions;
- QR reports;
- forms;
- recurring-work generation;
- translated paperwork or other integrations.

## RA-04 — Employee Participation and Assignment Lifecycle

**Target:** Turn assignment from a static field into a controlled work-participation lifecycle.

### Target lifecycle

```text
UNASSIGNED / AVAILABLE
        ↓ claim
ASSIGNED
        ↓ accept/start
IN PROGRESS
        ↓
COMPLETED
```

Alternative paths may include:

```text
ASSIGNED
   ↓ reject/release
UNASSIGNED
or
SUPERVISOR REVIEW
```

Additional controlled states may later include Blocked, Deferred, Cancelled, and Reopened.

### Candidate Work Units

- My Work Queue
- Available Work Queue
- Claim Work
- Accept/Start Work
- Reject Assigned Work
- Release Claimed Work
- Reassignment
- Reopen Completed Work
- Cancellation
- Assignment Event History
- Duplicate-Action Protection

## RA-05 — Calendar and Scheduling Integration

**Target:** Use Calendar/Scheduling information as flexible operational context.

### Desired capabilities

- identify who is scheduled to work;
- identify expected unit/location;
- identify shift/time window when available;
- show schedule context on employee and supervisor dashboards;
- prioritize likely assignees based on schedule context;
- permit supervisor override/reassignment;
- preserve the distinction between scheduled location and actual work location;
- support later planned-vs-actual analysis.

### Candidate Work Units

- Current Schedule Context
- Scheduled Employee Resolution
- Scheduled Location Resolution
- Schedule-Aware Assignment Suggestions
- Supervisor Schedule Override
- Planned-vs-Actual Work Comparison
- Calendar Integration Health

### Integration note

The exact System identity and authority boundaries of the Calendar application within the Scheduling Project still require reconciliation.

## RA-06 — Employee Profile Integration

**Target:** Connect Work Queue to the planned Employee Profile capability without making Work Queue the personnel authority.

### Desired capabilities

- stable employee identity resolution;
- display name and preferred operational label;
- role/permission relationship where appropriate;
- current operational status where appropriate;
- profile link/navigation;
- employee-specific work history;
- later achievements, qualifications, or capabilities if those become authoritative elsewhere.

### Candidate Work Units

- Employee Profile Integration Contract
- Employee Profile Lookup
- Profile Link from Work Queue
- Employee Work-History View
- Shared Employee Identity Rules

### Status

Employee Profile is pending. Work Queue should be designed so the future integration can attach cleanly rather than duplicating profile truth.

## RA-07 — Inventory Integration and Transaction Propagation

**Target:** Make inventory-related task completion produce complete, attributable, reconciled inventory transactions.

### Current gap

An applicable completed task can create an `Inventory_Holder_Event`, but that does not yet complete the corresponding transfer from the employee cart to the destination inventory holder.

### Target transaction

```text
Employee
    ↓
Employee Cart
    ↓
Work Queue Task
    ↓
Product + Quantity
    ↓
Destination Inventory Holder
    ↓
Validated Transfer
    ↓
Source cart decreases
Destination holder increases
History preserves both sides
```

### Candidate Work Units

- Acting Employee → Cart Resolution
- Inventory Product Resolution
- Transfer Quantity Capture
- Destination Holder Resolution
- Source Cart Decrement
- Destination Holder Increment
- Transaction/Event Linkage
- Task → Inventory Transaction Linkage
- Employee Attribution on Inventory Events
- Atomic Transfer Handling
- Insufficient-Stock Validation
- Duplicate-Transfer Protection
- Transfer Reversal/Correction
- Inventory Integration Audit

### Required invariants

- one work completion must not transfer the same stock twice;
- source and destination changes must reconcile;
- failed destination update must not silently leave the source decremented;
- history must preserve task ID, employee ID, product, quantity, source, destination, and time.

## RA-08 — Structured Notes, Templates, Images, and Evidence

**Target:** Make notes structured enough to be useful while retaining free-text and visual evidence.

### Desired note-template families

- completion note;
- problem/exception note;
- rejection/release reason;
- supervisor-review note;
- handoff/follow-up note;
- inventory/replenishment note;
- safety/condition note;
- general task note.

### Image capability

- upload or capture an image for a task/note;
- retain image metadata and task linkage;
- permit more than one image where appropriate;
- preserve who added the image and when;
- define retention/access rules;
- show image evidence in supervisor review and history.

### Candidate Work Units

- Structured Note Model
- Note Template Registry
- Note Authoring UI
- Task Image Upload
- Image/Task Linkage
- Image Metadata
- Evidence Viewer
- Evidence Permissions and Retention

## RA-09 — QR Reporting and OpenAI-Assisted Validation

**Target:** Use QR codes as context-aware entrances for reporting work and use the OpenAI API as a bounded validation/normalization assistant.

### Target reporting flow

```text
Scan location/asset QR
        ↓
Context-aware report form
        ↓
Text / structured fields / optional image
        ↓
Validation + normalization assistance
        ↓
Pending Supervisor Review
        ↓
Released as assigned or unassigned work
```

### Possible OpenAI API assistance

- detect obviously incomplete reports;
- normalize free-text descriptions into structured fields;
- suggest task category;
- identify likely duplicate/ambiguous reports;
- extract relevant details from an uploaded image when appropriate;
- flag uncertainty for human review;
- help validate that report content matches the scanned location context.

### Guardrails

- AI output is advisory until accepted by the applicable human/system rule;
- QR identity/location data remains authoritative over model guesses;
- employee identity is not inferred from model output;
- inventory quantity is not changed solely because a model suggested a value;
- model uncertainty/failure must not prevent basic manual reporting.

### Candidate Work Units

- QR Context Model
- QR Code Generation/Registry
- QR Reporting Form
- Report Submission Record
- OpenAI Validation Service
- Validation Result Record
- Duplicate/Ambiguity Detection
- Supervisor Review Integration
- QR Reporting Analytics
- Offline/Failure Fallback

## RA-10 — History, Search, Audit, and Operational Inquiry

**Target:** Turn accumulated Work Queue activity into searchable operational history.

### Search dimensions

- employee;
- assigned employee;
- completed by;
- unit;
- location;
- job/task type;
- status;
- pending/review state;
- assigned/unassigned;
- date/date range;
- priority;
- recurring-work source;
- inventory-related work;
- QR-originated work.

### Candidate Work Units

- Unified History View
- Employee Search
- Unit/Location Search
- Date-Range Search
- Multi-Filter Search
- Assignment History
- Completion History
- Review History
- Inventory-Linked History
- Task Detail Timeline
- Audit Export

### Evolution from Completed Jobs

The current Completed Jobs concept should remain useful, but become one view over a broader Work Queue history rather than the complete history model.

## RA-11 — Reporting, Printing, and Paperwork Translation

**Target:** Produce operational reports from the same authoritative data used by the application and translate structured records into required human-facing paperwork.

### Report families

- Daily Work Report
- Employee Work Report
- Unit/Location Work Report
- Open Work Report
- Pending/Review Report
- Rejected/Released Work Report
- Supervisor Handoff Report
- Inventory-Related Work Report
- Recurring/Dailies Completion Report

### Printing

- print-friendly report layouts;
- date/time and filter criteria on report;
- page headers/footers where useful;
- no separate manually maintained report dataset.

### Paperwork translation

Potential capabilities include:

- project structured task/history data into paper-form layouts;
- generate recurring operational paperwork from authoritative records;
- preserve the source task/employee/location IDs behind generated paperwork;
- later support controlled capture of information from paper/form inputs where useful;
- maintain clear separation between source operational truth and presentation paperwork.

### Candidate Work Units

- Reporting Query Model
- Daily Report
- Employee Report
- Unit Report
- Supervisor Handoff Report
- Print Layout System
- Paperwork Template Registry
- Structured Record → Paperwork Translation
- Paperwork Output History
- Paperwork Capture Investigation

## RA-12 — Recurring Work and Dailies

**Target:** Represent routine repeated work without manually recreating every task.

### Desired capabilities

- define recurring-work templates;
- generate dailies;
- schedule by day, shift, unit, role, or applicable recurrence rule;
- distinguish the recurring definition from each generated task instance;
- suspend or modify a recurring definition without rewriting completed history;
- handle holidays/closures/exceptions where relevant;
- report completion against expected recurring work.

### Candidate Work Units

- Recurring Work Definition
- Daily Work Templates
- Recurrence Engine
- Generated Task Instances
- Recurrence Exceptions
- Temporary Suspension
- Recurring Work Dashboard
- Dailies Completion Reporting
- Recurring Work History

## RA-13 — Building Map and Location Intelligence

**Target:** Complete the shared building/location model enough for Work Queue to use locations reliably and visually where useful.

### Desired capabilities

- complete location records;
- stable location IDs;
- unit/room/area relationships;
- QR-to-location resolution;
- task-to-location validation;
- map-based browsing where useful;
- schedule/location integration;
- inventory-holder/location integration;
- location-aware reporting.

### Candidate Work Units

- Building Map Data Completion
- Location Hierarchy Reconciliation
- Room/Area Coverage Audit
- Location ID Validation
- Map Navigation
- Task Location Picker
- QR Location Linkage
- Inventory Holder Location Linkage
- Schedule Location Linkage
- Location Data Quality Report

## RA-14 — Supervisor Operations and Exception Handling

**Target:** Give supervisors a coherent place to handle work that needs judgment rather than normal employee execution.

### Supervisor queues

- pending-review queue;
- rejected/released work;
- blocked work;
- overdue work;
- tasks requiring clarification;
- QR reports awaiting approval;
- possible duplicate reports;
- inventory integration failures;
- unresolved evidence/notes.

### Candidate Work Units

- Supervisor Review Dashboard
- Rejected Work Queue
- Exception Queue
- Bulk Assignment/Reassignment
- Priority Management
- Due-Date/Time Controls
- Clarification Requests
- Escalation/Follow-Up
- Review Decision History

## RA-15 — Notifications and Communication

**Target:** Surface meaningful work changes without making external messaging a prerequisite for core Work Queue operation.

### Candidate notifications

- new assignment;
- reassignment;
- claim confirmation;
- rejected/released assignment;
- supervisor review required;
- clarification requested;
- high-priority work;
- overdue work;
- task reopened;
- integration failure requiring attention.

### Candidate Work Units

- In-App Notification Model
- Notification Center
- Role-Based Notification Rules
- Assignment Notifications
- Supervisor Alerts
- External Notification Integration Investigation

## RA-16 — Administration, Configuration, Reliability, and Data Integrity

**Target:** Make the application maintainable and trustworthy as a real operational system.

### Administration/configuration

- employee references;
- role assignments;
- task types;
- priorities;
- statuses/state rules;
- note templates;
- report templates;
- recurring-work templates;
- QR definitions;
- integration configuration;
- location references.

### Reliability/data integrity

- stable IDs;
- referential integrity;
- server-side validation;
- duplicate-action prevention;
- atomic multi-system operations where possible;
- error logging;
- integration failure visibility;
- safe reversal/correction;
- regression tests;
- deployment/version identification;
- backup/recovery expectations;
- permissions validation.

### Candidate Work Units

- Admin Configuration UI
- Controlled Lookup Management
- State-Machine Validation
- Referential Integrity Checks
- Integration Error Log
- Duplicate Action Guard
- Transaction/Rollback Pattern
- Regression Test Suite
- Operational Health View
- Backup/Recovery Procedure
- Version/Deployment Diagnostics

# 6. Cross-System Integration Map

| Integration | Direction / Relationship | Target role | Current roadmap status |
|---|---|---|---|
| Work Queue ↔ Inventory 3.0 | bidirectional operational integration | task-driven inventory movement and attributable inventory history | partial; holder-event creation exists, full transfer propagation planned |
| Work Queue ↔ Employee Profile | identity/profile lookup | durable employee context without duplicating profile authority | pending system/integration |
| Calendar/Scheduling → Work Queue | schedule-context provider | who is working, where, and when; flexible assignment context | planned |
| Building Map/Locations → Work Queue | location authority/reference | stable location selection, QR context, map navigation, reporting | partial; location reference exists, map completion planned |
| QR Reporting → Work Queue | work-intake source | context-aware reports enter supervisor-controlled pending state | planned |
| OpenAI API → QR/Report Validation | advisory validation service | bounded normalization/classification/validation assistance | planned |
| Work Queue → Reporting/Printing | derived presentation | printable operational reports from authoritative Work Queue data | planned |
| Work Queue → Paperwork Translation | derived presentation/workflow | produce human-facing paperwork from structured operational records | planned |

# 7. Proposed Maturity Sequence

This sequence expresses dependency and product maturity, not a session-by-session implementation plan.

## Foundation A — Identity and controlled participation

- Employee Identity
- Role Resolution
- Permission Enforcement
- My Work Queue
- Available Work Queue
- Pending Work State
- Supervisor Review Queue
- Claim / reject / release lifecycle
- Assignment Event History

## Foundation B — Operational context and real integrations

- Calendar/Scheduling context
- Employee Profile integration contract
- complete inventory-transfer propagation
- Building Map/location completion
- recurring work/dailies

## Foundation C — Evidence, inquiry, and supervisory operations

- structured notes
- image evidence
- unified history/search
- supervisor exception handling
- advanced filtering
- work timelines

## Foundation D — Reporting and intelligent intake

- QR reporting
- OpenAI-assisted validation
- printable reports
- paperwork translation
- supervisor handoff reporting

## Foundation E — Administrative maturity and hardening

- Administrator dashboard
- configuration UI
- health/integration diagnostics
- regression suite
- recovery/correction tooling
- permissions and data-integrity audits

# 8. Relationship to Work Units

Roadmap Areas are durable planning categories.

Candidate Work Units become Registry records only when they are sufficiently bounded and useful to track as addressable work. A Work Unit should describe a capability outcome, not merely a code edit.

Example:

```text
Roadmap Area:
    Inventory Integration

Work Unit:
    Inventory Transfer Propagation

Possible implementation tasks:
    add source-cart lookup
    add transfer command
    update holder quantity
    write transaction linkage
    add rollback
    test duplicate prevention
```

The roadmap should remain readable even after individual Work Units are completed, deferred, split, or superseded.

# 9. Roadmap State Vocabulary

Suggested roadmap status values:

- `existing`
- `partial`
- `planned`
- `candidate`
- `blocked`
- `deferred`
- `completed`
- `superseded`
- `not-yet-assessed`

Work Unit IDs should remain blank until the Work Unit Registry actually assigns stable `WORK-####` identities.

# 10. Immediate Documentation Follow-On

1. Preserve this document as the human-readable Work Queue roadmap.
2. Create its structured roadmap sidecar.
3. Register the sidecar in a System Roadmap Catalog.
4. Use the same roadmap document + sidecar pattern for Inventory 3.0.
5. Reconcile Calendar's System identity within Scheduling, then create its roadmap document + sidecar.
6. Use the cross-System roadmap catalog to discover roadmaps without collapsing them into one master roadmap.
7. Populate the Work Units Registry from sufficiently mature roadmap items rather than directly from brainstorming.

# 11. Open Product Determinations

The roadmap intentionally leaves these questions open:

- exact login/authentication mechanism;
- exact Employee Profile system architecture and authority;
- final Calendar/System classification within Scheduling;
- precise task state-machine vocabulary;
- when rejected work immediately returns to Available Work versus requires supervisor review;
- OpenAI API validation schema, cost controls, privacy boundaries, and failure behavior;
- image storage platform, retention, and access rules;
- exact paperwork-translation scope;
- which recurring-work rules belong to Calendar/Scheduling versus Work Queue;
- whether report generation is client-side, server-side, or a separate reporting service;
- which administrative configuration values require higher-level approval;
- final System ID and Project ID assignments.

# 12. Definition of a Mature Work Queue

Work Queue can be considered near its intended mature form when:

- users have reliable identity and role-aware access;
- employees can manage their own assigned/available work within policy;
- supervisors control pending work and exceptions;
- schedule context informs assignment without preventing operational flexibility;
- employee/profile identity is shared rather than duplicated;
- inventory-related work produces reconciled inventory transactions;
- recurring work generates reliable dailies;
- notes and images preserve work evidence;
- QR reporting feeds a controlled review process;
- OpenAI assistance is bounded, auditable, and non-authoritative;
- history is searchable across employee, location, unit, state, and time;
- printable reports and paperwork outputs derive from authoritative records;
- building/location data supports the application's operational needs;
- administrators can maintain ordinary configuration without editing source code;
- failures and corrections are visible and recoverable;
- major state changes are attributable to stable identities and preserved in history.
