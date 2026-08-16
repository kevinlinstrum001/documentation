# Task Assignment and Tracking — Project Summary

| Field | Current value |
|---|---|
| **Document role** | Authoritative human-readable Project definition and current Project interpretation |
| **Project** | Task Assignment and Tracking |
| **Entity type** | Project |
| **Project ID** | Unassigned — permanent `PROJ-###` allocation is intentionally pending |
| **Principal known System** | Work Queue |
| **Parent relationship** | Operations — current relationship model; not intrinsic Project identity |
| **Primary operational environment** | Meadows Housekeeping — current application context; not intrinsic Project identity |
| **Project-definition status** | Second working Klinswork Project Definition exemplar |
| **Reference exemplar** | Inventory Management → Inventory 3.0 |
| **Project Identity profile** | `project-identity / 1.0-draft` |
| **Companion sidecar** | `../sidecars/project-summary-sidecar.json` — pending |
| **System roadmap** | `../systems/Work Queue/summaries/work-queue-roadmap.md` — current |
| **Last reconciled** | 2026-08-16 |
| **Reconciliation timestamp** | 2026-08-16T07:40:00-06:00 |

---

## 1. Document purpose and authority

This document is the durable human-readable Project Summary for the **Task Assignment and Tracking Project**.

Its purpose is to preserve the rich Project definition that does not belong in the narrow Project Identity Entity Record. It explains what Task Assignment and Tracking is for, what operational function it represents, what falls inside and outside its scope, which System presently implements the function, which neighboring Projects and shared Resources it depends on, how the Project has been understood historically, where the Project stands now, what remains unresolved, and what work should happen next.

This document is intended to answer questions such as:

- Why does the Task Assignment and Tracking Project exist?
- What operational responsibility does it represent?
- What is inside the Project boundary?
- What is outside the Project boundary?
- How is Work Queue related to the Project?
- How do Scheduling, Inventory Management, Employee Profile, Building Map / Locations, and Documentation relate without becoming part of the Project identity?
- Which kinds of Resources participate in the Project?
- What is authoritative for identity, relationships, Resources, current implementation behavior, roadmap direction, and history?
- What is known about the current Project state?
- Which questions remain open?
- What should a future work session load and do next?

This Project Summary is the **human-readable explanatory authority** for the Project's current purpose, scope, boundary narrative, current interpretation, historical framing, and unresolved Project-definition questions expressed here.

It is **not** the authority for every fact concerning Task Assignment and Tracking or Work Queue.

The authority model is deliberately distributed:

```text
Project identity facts
    → ../project-identity.json

Project purpose / scope / boundaries / current interpretation
    → this Project Summary

Structured interpretation of this Project Summary
    → ../sidecars/project-summary-sidecar.json

Project registration / ID allocation / global routing
    → Project Registry when formalized

Resource identity / current location / routing
    → Resource Registry

Cross-entity relationships
    → relationship authority when formalized

Work Queue current-state System details
    → ../systems/Work Queue/summaries/system-summary.md

Work Queue planned System direction
    → ../systems/Work Queue/summaries/work-queue-roadmap.md

Current software behavior
    → current implementation sources / deployment / datastore / tests

Historical change / provenance events
    → Activity Registry + dated historical records

Bounded intended work
    → implementation plans

What actually occurred in a bounded work session
    → Work Implementation Session + execution evidence
```

The companion sidecar may structure this document for discovery, routing, validation, and Viewer presentation, but the sidecar remains a companion to this Markdown source rather than replacing it.

---

## 2. Project identity context

**Task Assignment and Tracking** is a Klinswork **Project**.

The Project represents the durable body of operational responsibility, rules, records, history, decisions, Systems, and continuing work associated with identifying discrete work and preserving its lifecycle from intake through responsibility, performance, completion, verification, reporting, and history.

The Project Identity Entity Record is:

```text
../project-identity.json
```

That record currently establishes:

```text
entityType: project
canonicalName: Task Assignment and Tracking
projectId: ""
projectIdAssignmentStatus: unassigned
```

The blank Project ID is deliberate.

A permanent `PROJ-###` value has not yet been formally allocated and must not be invented from:

- the Project name;
- repository location;
- parent relationship;
- Work Queue;
- historical Tasker naming;
- Resource IDs;
- Work Unit IDs;
- current operational environment;
- any previously discussed provisional numbering.

The Project is intended to retain continuity across ordinary changes in:

- name;
- repository location;
- parent relationship;
- operational environment;
- principal System;
- application implementation;
- spreadsheet or datastore;
- Resource set;
- deployment URL;
- lifecycle state;
- user interface;
- implementation language or platform.

The governing identity invariant is:

```text
Project identity
    != Project name
    != repository location
    != hierarchy
    != System
    != application
    != Resource
    != operational environment
    != deployment
    != lifecycle state
    != implementation
```

This Summary may explain surrounding facts because they are necessary to understand the Project, but their appearance here does not convert them into intrinsic Project identity.

---

## 3. Purpose

The purpose of the Task Assignment and Tracking Project is to preserve and improve **reliable operational knowledge and control of discrete work**.

At the practical level, the Project exists so people and Systems can answer:

- What work exists?
- Why does it exist?
- Where does it belong?
- Is it pending review, assigned, available, in progress, blocked, completed, or otherwise in a controlled state?
- Who is responsible for it?
- Who actually performed or completed it?
- What notes, evidence, exceptions, or images are associated with it?
- What happened to the assignment over time?
- Was the work completed or verified?
- What downstream operational effect did the work cause?
- Can the history be reconstructed later?
- Can the work be found by employee, location, unit, state, type, or date?
- Can the information be summarized or translated into reports or paperwork?

The Project is not merely an application-development effort.

The underlying operational function exists independently of Work Queue:

```text
work need / observation / request
        ↓
identified work
        ↓
review / acceptance where required
        ↓
responsibility
        ↓
assignment or availability
        ↓
performance / status
        ↓
notes / evidence / exceptions
        ↓
completion
        ↓
verification / review
        ↓
history / reporting
        ↓
downstream operational effects
```

A web app may support this process. A spreadsheet may store part of it. A paper list may communicate it. A supervisor may assign it verbally. A QR form may submit it. A schedule may provide context. None of those artifacts individually *is* the Task Assignment and Tracking Project.

The durable objective is to make work identity, responsibility, state, evidence, completion, and history dependable enough to support real operations.

---

## 4. Operational function

The Project represents the operational function **Task Assignment and Tracking**.

That function includes the controlled transition from an identified need for work to an attributable operational record of what happened.

A useful functional model is:

```text
IDENTIFY WORK
    need
    request
    observation
    recurring obligation
        ↓
ESTABLISH CONTEXT
    location
    unit
    task type
    priority
    schedule context where relevant
        ↓
REVIEW / RELEASE
    pending
    supervisor review
    clarification
    approved work
        ↓
ESTABLISH RESPONSIBILITY
    assigned employee
    unassigned / available work
    claim
    reassignment
        ↓
PERFORM / TRACK
    accepted
    in progress
    blocked / exception
    notes / evidence
        ↓
COMPLETE / VERIFY
    completion
    completion attribution
    supervisor review where applicable
        ↓
PRESERVE HISTORY
    assignment events
    status events
    evidence
    completion
    downstream effects
        ↓
USE INFORMATION
    operational inquiry
    reporting
    handoff
    planning
    accountability
    later analysis
```

The Project therefore concerns more than storing a task row.

It concerns the rules, identities, relationships, and evidence that make the work record interpretable.

### 4.1 Core operational concerns

Current Project documentation identifies the following working concerns:

- work intake;
- work identity;
- pending work;
- supervisor review;
- assignment;
- unassigned or available work;
- employee responsibility;
- claiming work;
- rejection or release;
- reassignment;
- status and lifecycle;
- performance and completion;
- completion attribution;
- structured notes;
- images or other task evidence;
- exception handling;
- verification;
- recurring work and dailies where represented as discrete work;
- search and operational inquiry;
- history and audit;
- reporting and printable output;
- paperwork translation from structured work records;
- QR-originated reporting;
- location relationships;
- schedule context;
- employee/profile relationships;
- inventory-related downstream effects;
- administrative controls;
- validation;
- data integrity;
- testing;
- documentation of the task-assignment-and-tracking function and its Systems.

These concerns define the present working Project scope.

They should be refined as formal relationship records, Work Queue current-state documentation, and live implementation evidence become more complete.

---

## 5. Scope

### 5.1 In scope

At the present level of reconciliation, Task Assignment and Tracking includes work needed to define, implement, operate, verify, and preserve the discrete-work lifecycle.

This includes:

### Work identity and intake

- creating or receiving a work item;
- preserving a stable task/work identity where implemented;
- identifying work source or provenance where useful;
- preserving task type, description, unit, location, priority, and related operational context;
- supporting work that originates from people, recurring definitions, forms, QR reports, integrations, or other controlled sources.

### Review and release

- pending work;
- supervisor-controlled review;
- clarification;
- release into actionable work;
- distinction between pending work and employee-visible available work;
- release as assigned or unassigned where policy permits.

### Responsibility and assignment

- assigned employee;
- stable employee identity where available;
- unassigned or available work;
- claiming work;
- reassignment;
- rejection or release;
- preservation of assignment history.

### Work performance and status

- accepted or started work where modeled;
- in-progress state;
- completion;
- blocking conditions;
- deferral, cancellation, reopening, or other controlled lifecycle states where later adopted;
- prevention of ambiguous or contradictory states.

### Notes and evidence

- structured notes;
- free-text context;
- completion notes;
- rejection/release reasons;
- supervisor-review notes;
- handoff/follow-up notes;
- task-linked images;
- evidence metadata;
- attribution of who added evidence and when.

### History and audit

- preserved task history;
- assignment history;
- completion history;
- review history;
- employee-attributed actions;
- downstream-system linkage;
- later reconstruction of what happened.

### Search and reporting

- search by employee;
- search by unit or location;
- search by task type or status;
- search by assignment state;
- search by date/date range;
- printable operational reports;
- employee, unit, daily, open-work, review, and handoff reporting where later implemented.

### Recurring work

- representation of repeated work such as dailies;
- recurring-work definitions;
- generated task instances;
- recurrence exceptions;
- preservation of completed instance history.

### Integrations

- Scheduling context;
- shared employee identity/profile context;
- shared location / Building Map context;
- Inventory Management effects;
- QR reporting;
- advisory validation services where later adopted.

### Administration and integrity

- controlled task types;
- priorities;
- lifecycle rules;
- note templates;
- recurring-work definitions;
- integration configuration;
- validation;
- permissions;
- duplicate-action prevention;
- error visibility;
- testing;
- recovery/correction patterns.

### Documentation and knowledge

- Project documentation;
- System documentation;
- System roadmaps;
- implementation plans;
- structured sidecars;
- catalogs;
- preserved historical evidence;
- explanatory and downstream reference products.

### 5.2 Potentially related but not automatically in scope

Some work may touch Task Assignment and Tracking without belonging to the Project itself.

Examples include:

- creation and governance of the employee/personnel master record;
- the general scheduling function;
- the authoritative inventory-state model;
- general Building Map / location governance;
- general SDS governance;
- general Documentation infrastructure;
- communication platforms not specific to task operations;
- application hosting infrastructure shared by many Klinswork tools.

A relationship to a task does not automatically make another function part of the Task Assignment and Tracking Project.

---

## 6. Project boundaries

The Project boundary is functional rather than application-based.

Task Assignment and Tracking should remain distinguishable from neighboring Klinswork Projects and shared infrastructure even when they exchange information or trigger one another.

### 6.1 Scheduling

Task Assignment and Tracking does not become **Scheduling** merely because schedule information helps determine who is expected to work, where, or when.

Scheduling concerns expected person/place/time relationships.

Task Assignment and Tracking concerns a discrete work responsibility and its lifecycle.

```text
Scheduling
        ↓
expected person / place / time context
        ↓
Task Assignment and Tracking
        ↓
specific work responsibility / task
```

Schedule information may inform task assignment without becoming the task record itself.

Likewise, actual task performance should not silently rewrite the schedule merely because work occurred somewhere different from the expected assignment.

The intended mature relationship is flexible:

- schedule context may suggest likely assignees;
- supervisors may make legitimate operational changes;
- planned location and actual work location can remain distinguishable;
- later analysis may compare expected staffing context with actual work without conflating the two authorities.

### 6.2 Inventory Management

Task Assignment and Tracking does not become **Inventory Management** merely because a task causes inventory to be checked, moved, replenished, consumed, or transferred.

A task may produce an inventory effect:

```text
Task Assignment and Tracking
        ↓
task / completion relationship
        ↓
inventory-related request or effect
        ↓
Inventory Management
        ↓
inventory transaction / state
```

Task Assignment and Tracking owns the work identity, responsibility, completion, and task-side linkage.

Inventory Management owns the resulting inventory-state effect and the integrity of inventory transactions.

Current Work Queue evidence supports a partial operational integration: completion of an applicable task can create an `Inventory_Holder_Event` associated with the exact inventory holder and location. Further propagation, such as deducting the corresponding quantity from an employee cart, remains planned rather than verified current behavior.

That distinction is important:

```text
task completion
    != complete inventory transfer
```

The mature integration should preserve both task history and inventory transaction history without making either Project the authority for the other's core state.

### 6.3 Employee Profile / personnel information

Task Assignment and Tracking does not become the authoritative employee-profile or personnel system merely because work must be attributable to people.

Employee identity and profile truth should be shared or resolved from the appropriate personnel/profile authority.

Task Assignment and Tracking may legitimately preserve:

- stable employee ID references;
- who was assigned;
- who claimed work;
- who completed work;
- who added a note or image;
- who approved or reviewed work;
- employee-specific work history.

It should not silently create a competing personnel authority.

Current Work Queue evidence already supports use of employee records as an active personnel source for assignment, including preservation of stable Assigned Employee ID rather than relying only on typed names.

### 6.4 Building Map / Locations

Task Assignment and Tracking does not own the shared **Building Map / Locations** model merely because work occurs somewhere.

However, a complete and stable location model is an important dependency for the intended mature Project/System behavior.

Location identity may support:

- task location;
- unit/room/area relationships;
- schedule context;
- employee location context;
- QR reporting;
- inventory-holder relationships;
- search;
- reporting;
- map-based navigation;
- validation that a task refers to a real operational location.

The Work Queue roadmap therefore includes **Building Map and Location Intelligence** as a target capability area.

Its stated target is to complete the shared building/location model enough for Work Queue to use locations reliably and visually where useful.

This includes planned work such as:

- Building Map data completion;
- location hierarchy reconciliation;
- room/area coverage audit;
- stable location-ID validation;
- map navigation;
- task location selection;
- QR location linkage;
- Inventory Holder location linkage;
- Schedule location linkage;
- location-data quality reporting.

The boundary rule is:

> **Task Assignment and Tracking depends on a complete, stable shared location model; it does not become the owner of that model merely because Work Queue consumes it.**

Building Map completion should therefore be represented as a shared dependency and integration concern with direct consequences for this Project.

### 6.5 Documentation

Task Assignment and Tracking does not become the **Documentation Project** merely because it uses:

- Entity Records;
- READMEs;
- summaries;
- sidecars;
- implementation plans;
- System roadmaps;
- catalogs;
- manifests;
- the Klinswork Documentation Viewer;
- publication infrastructure.

Documentation supplies infrastructure for describing, finding, preserving, and resuming the Project.

The operational authority for task state remains with the applicable task-assignment-and-tracking System/data, not with its documentation.

### 6.6 Meadows Housekeeping

Task Assignment and Tracking does not equal **Meadows Housekeeping**.

Meadows Housekeeping is the primary current operational environment in which the Project is being modeled and used.

The environment supplies real work, employees, rooms, units, routines, constraints, exceptions, schedules, inventory interactions, paper processes, and operational evidence.

The operational environment can change without creating a new Project identity.

### 6.7 Work Queue

Task Assignment and Tracking does not equal **Work Queue**.

This distinction is fundamental:

```text
Task Assignment and Tracking
    = Project

Work Queue
    = System
```

The Project is the durable undertaking.

Work Queue is the principal currently identified System used to implement and support that undertaking.

---

## 7. Paperwork and human-process parallel

Task Assignment and Tracking should preserve a **paperwork and human-process parallel**.

Klinswork systems may structure, mirror, reconcile, route, analyze, or preserve work information, but the digital System should not be described as the sole source of the real operational process merely because it exists.

Operational information may originate through:

- paper work lists;
- institutional forms;
- handwritten notes;
- supervisor instructions;
- verbal reports;
- employee observations;
- photographs;
- meetings;
- inspections;
- email;
- QR reports;
- digital forms;
- recurring operational routines;
- schedule information;
- Work Queue actions;
- system-generated events;
- later transcription or batch conversion.

A person may participate in the real operational process without directly using Work Queue.

Digital participation, operational participation, supervisory authority, administrative authority, and documentation authority should not be inferred from one another.

This parallel is especially important for planned **paperwork translation** capabilities.

A mature System may be able to project structured work/history records into human-facing paperwork, while preserving the underlying task, employee, and location identities.

That does not make the paperwork the source of operational truth unless the applicable workflow explicitly assigns it that role.

---

## 8. Principal known System — Work Queue

**Work Queue** is the principal System presently identified within the Task Assignment and Tracking Project.

The current conceptual relationship is:

```text
Operations
    ↓
Task Assignment and Tracking
    ↓
Work Queue
```

That diagram is a relationship view. It does not encode identity.

Work Queue should be understood as the coherent System through which task-assignment-and-tracking behavior, data, interfaces, relationships, and supporting Resources can be organized.

Current Klinswork vocabulary distinguishes:

```text
Project
    Task Assignment and Tracking

System
    Work Queue

Resources
    application / deployment
    Apps Script source and services
    Google Sheets datastore
    task dataset
    employee reference dataset
    location reference data
    technical documentation
    supporting assets
    other implementation resources
```

The System is broader than any single application screen, deployment URL, spreadsheet, source file, or historical version.

### 8.1 Current evidence supporting the System role

Current documentation supports the following limited System-level facts:

- the visible Work Queue application supports creation, assignment, tracking, updating, and completion of work;
- the application reads from and writes to connected Google Sheets;
- the data layer includes work items/task history, assignments/status changes, locations, employee/role records, inventory holders/events, SDS/product records, and configuration/lookup relationships;
- employee records are used in current assignment behavior;
- stable Assigned Employee ID can be preserved;
- applicable task completion can create an `Inventory_Holder_Event`;
- complete employee-cart-to-holder transfer propagation is not yet verified current behavior.

These facts help establish Work Queue as the principal current System.

They are **not** intended to substitute for the later Work Queue `system-summary.md`, which should carry the detailed System-level architecture and current-state analysis.

### 8.2 Current-state versus future-state documentation

The Work Queue documentation layer now intentionally separates:

```text
systems/Work Queue/summaries/system-summary.md
    answers:
    What is Work Queue now, based on evidence?

systems/Work Queue/summaries/work-queue-roadmap.md
    answers:
    What should Work Queue become?
```

The current roadmap must not be used as proof that its planned capabilities already exist.

### 8.3 System identity remains deferred

The following remain intentionally unresolved:

- permanent `SYS-###` assignment;
- final System Identity Record Profile;
- exact Work Queue System identity fields;
- whether a separate Application/Implementation entity should exist beneath the System;
- complete Resource membership and relationship map;
- final System boundary.

System Identity remains deferred while the Project Definition architecture is tested through the second exemplar.

---

## 9. Resources

Task Assignment and Tracking uses concrete **Resources**, but Resources are not the Project itself.

### 9.1 Current Work Queue Resource references

The current System Roadmap Catalog references the following Resources for Work Queue:

```text
RES-002   Work Queue app
RES-003   Work Queue app data sheet
RES-012   Work Queue Tasks dataset
RES-013   Work Queue Employees dataset
RES-014   Work Queue Locations reference
RES-047   Work Queue app technical manual
```

These references establish useful current routing points, but this Project Summary does not redefine their identity, path, URL, deployment, or current version.

Those facts belong in the Resource Registry and current implementation evidence.

### 9.2 Applications

User-facing or administrative applications may provide interfaces for:

- creating work;
- assigning work;
- reviewing work;
- updating status;
- completing work;
- searching history;
- reporting;
- administration.

The application interface should remain distinguishable from the Work Queue System that contains or coordinates it.

### 9.3 Data stores and datasets

Known or documented Work Queue data roles include:

- work items and task history;
- assignment and status data;
- employee records;
- role records;
- location references;
- inventory-holder and inventory-event relationships;
- product/SDS references;
- configuration and lookup data.

Google Sheets is a major current implementation medium, but the Project Summary should not hard-code a workbook as Project identity.

### 9.4 Employee reference data

Employee data is important because task responsibility must be attributable to stable people rather than only displayed names.

Current evidence supports stable Assigned Employee ID usage.

Future Project/System work may extend employee attribution into:

- completion;
- task updates;
- inventory effects;
- search;
- reporting;
- employee work history.

The personnel/profile authority itself remains outside the Project boundary.

### 9.5 Location Resources / Building Map

Location reference data participates in the Project because tasks occur at operational locations.

The current roadmap catalog includes a Work Queue Locations reference, and the roadmap separately identifies Building Map / Location completion as a planned integration dependency.

The Project should consume stable location identity without independently duplicating or redefining that identity in each task-oriented Resource.

### 9.6 Technical documentation

The Work Queue technical manual is a current documentation Resource supporting architectural and operational understanding of the System ecosystem.

It documents, among other things:

- the application layer;
- Google Sheets data;
- employee/personnel relationships;
- inventory relationships;
- Documentation dependencies;
- hosting and development infrastructure;
- access/publication layers;
- human operational labor.

Detailed System claims derived from that manual belong primarily in the Work Queue System Summary.

### 9.7 Documentation Resources

This Project documentation space contains or is intended to contain:

```text
Task Assignment and Tracking/
├── project-identity.json
├── README.md
├── summaries/
│   └── project-summary.md
├── sidecars/
│   └── project-summary-sidecar.json
├── systems/
│   └── Work Queue/
│       ├── README.md
│       ├── summaries/
│       │   ├── system-summary.md
│       │   └── work-queue-roadmap.md
│       └── sidecars/
│           ├── system-summary-sidecar.json
│           └── work-queue-roadmap-sidecar.json
└── implementation-plans/
```

### 9.8 Resource authority rule

A Resource should normally be registered once.

When a formal Resource ID exists, Project and System documentation should refer to stable Resource identity rather than treating a path or URL as identity.

```text
Resource identity remains stable
        ↓
Resource location changes
        ↓
Resource Registry is updated
        ↓
Project/System relationship remains resolvable
```

This Summary does not attempt to reproduce the complete Resource Registry.

---

## 10. Current state

The Project currently has at least three different kinds of state that must not be conflated:

1. **operational/implementation state** — what Work Queue and current data actually do now;
2. **planned System direction** — what the Work Queue roadmap says the System should become;
3. **Project-definition/documentation state** — how well the durable Project is formally defined and discoverable.

### 10.1 Operational / implementation state

Current documentation establishes that Work Queue is a functioning but incomplete operational System.

Documented current behavior includes:

- task creation;
- assignment;
- filtering/tracking;
- updating;
- completion;
- Google Sheets-backed task and assignment data;
- employee records used for assignee selection;
- stable Assigned Employee ID storage;
- location/unit relationships;
- some Completed Jobs/history capability;
- partial Inventory integration through `Inventory_Holder_Event` creation.

Important limitations documented in the current roadmap baseline include:

- no reliable current-user identity in the running application;
- incomplete employee My Work / Available Work participation model;
- incomplete pending-work and supervisor-review routing;
- incomplete inventory transfer propagation from employee cart to destination holder;
- schedule context not yet integrated;
- Employee Profile integration pending;
- role-based dashboards incomplete;
- search/history/reporting/printing incomplete;
- structured notes and image evidence incomplete;
- QR reporting and OpenAI-assisted validation not implemented;
- recurring dailies incomplete;
- Building Map / location model incomplete for target use.

This Project Summary preserves those points only as high-level Project context.

Detailed verification belongs in Work Queue System documentation and current implementation evidence.

### 10.2 Planned System direction

The Work Queue roadmap is now a first-class System record.

It defines a mature target System across 16 roadmap areas:

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

These roadmap areas are **planned or partially existing capability domains**.

They should not be rewritten here as though they are already implemented.

### 10.3 Project-definition state

As of 2026-08-16, the Project-definition layer is actively being built as the second Klinswork exemplar.

Completed or present:

```text
Task Assignment and Tracking recognized as Project
Work Queue recognized as principal System
Project directory created
project-identity.json instantiated
README.md created
Work Queue System directory created
Work Queue roadmap created
Work Queue roadmap sidecar created
System Roadmap Catalog created
Documentation Viewer taught System Roadmap preview
project-summary.md created by this step
```

Still pending after this document:

```text
sidecars/project-summary-sidecar.json
systems/Work Queue/README.md
systems/Work Queue/summaries/system-summary.md
systems/Work Queue/sidecars/system-summary-sidecar.json
discovery / companion validation
Registry / Activity / architecture effect reconciliation
implementation-session closure
```

### 10.4 Project ID state

```text
projectId: ""
projectIdAssignmentStatus: unassigned
```

This is not an omission to be casually fixed.

It is an explicit representation of the current architecture state.

---

## 11. Current records and authority routing

The Project-local record set now forms a deliberate layered structure.

### 11.1 `project-identity.json`

**Status:** created.

**Role:** narrow Project Identity Entity Record.

Use it for stable intrinsic Project identity facts assigned to the Project Identity profile.

Do not use it as authority for:

- Project purpose narrative;
- hierarchy;
- Work Queue;
- Resources;
- operational environment;
- repository path;
- lifecycle;
- implementation behavior;
- current task state.

### 11.2 `README.md`

**Status:** created.

**Role:** local orientation, navigation, authority routing, reading order, and resume-work guidance.

Use it to enter the Project documentation space and determine what to read next.

### 11.3 `summaries/project-summary.md`

**Status:** this document.

**Role:** rich human-readable Project definition and current interpretation.

### 11.4 `sidecars/project-summary-sidecar.json`

**Status:** pending.

**Role:** machine-readable companion to this Markdown source.

It must remain a **sidecar**, not an Entity Record.

### 11.5 `systems/Work Queue/`

**Status:** System directory exists.

Current records:

```text
summaries/work-queue-roadmap.md
sidecars/work-queue-roadmap-sidecar.json
```

Still pending:

```text
README.md
summaries/system-summary.md
sidecars/system-summary-sidecar.json
```

### 11.6 `implementation-plans/`

**Status:** Project-local implementation-plan space exists; exact current contents should be resolved from the repository at use time.

**Role:** bounded intended work.

An implementation plan is not proof of execution.

### 11.7 Work Implementation Session

The current declared Work Implementation Session exists specifically to construct and validate the second Project Definition exemplar.

Its semantic writing test is important:

```text
Project Summary
    answers:
    Why / what operational undertaking exists?

System Summary
    answers:
    How is that operational function coherently implemented by Work Queue?
```

If this Project Summary becomes a Work Queue feature history, the boundary has failed.

---

## 12. Relationships and integration context

Task Assignment and Tracking participates in several important cross-Project or shared-data relationships.

These are relationships, not intrinsic identity.

### 12.1 Operations

Current architecture places Task Assignment and Tracking beneath Operations:

```text
Klinswork
└── Operations
    └── Task Assignment and Tracking
```

This is the current relationship model.

It is not encoded into Project identity.

### 12.2 Work Queue

Work Queue is the principal current System.

```text
Task Assignment and Tracking
        ↓
Work Queue
```

The Project may survive replacement, redesign, or renaming of that System.

### 12.3 Scheduling

Scheduling provides or is expected to provide person/place/time context.

The mature Work Queue roadmap expects flexible schedule integration so the System can understand who is working and where without making the schedule an inflexible task-assignment rule.

### 12.4 Inventory Management

Work Queue and Inventory 3.0 are expected to participate in a bidirectional operational relationship.

The present roadmap describes that relationship as partial because holder-event creation exists while full transfer propagation remains planned.

### 12.5 Employee Profile

The Employee Profile capability is pending.

Its intended relationship is to provide durable employee/profile context without duplicating personnel authority inside Work Queue.

### 12.6 Building Map / Locations

Building Map / Locations provides shared location authority/reference context.

The relationship is currently partial.

The mature target requires:

- complete stable locations;
- QR linkage;
- map navigation;
- task-location validation;
- schedule-location linkage;
- inventory-holder-location linkage;
- location-aware reporting.

Completion of the shared Building Map is therefore an important dependency for mature Task Assignment and Tracking behavior.

### 12.7 QR Reporting

QR reporting is a planned work-intake source.

The intended flow is approximately:

```text
scan QR
    ↓
resolve location / asset context
    ↓
submit report
    ↓
optional text / image validation assistance
    ↓
pending supervisor review
    ↓
released as assigned or available work
```

Pending work remains supervisor-controlled and should not automatically appear in the employee available-work queue.

### 12.8 OpenAI API

The Work Queue roadmap proposes bounded OpenAI API assistance for validation, normalization, classification, extraction, ambiguity detection, or image/report review.

The model must not become operational authority for:

- employee identity;
- supervisor approval;
- task completion;
- inventory quantity;
- location identity;
- other controlled operational truth.

### 12.9 Documentation

Documentation preserves Project/System records, sidecars, roadmaps, catalogs, manifests, plans, workflows, and history.

It is an infrastructure relationship, not ownership of task state.

---

## 13. Building Map dependency

The Building Map deserves explicit treatment because the Task Assignment and Tracking function is inherently location-aware.

A task is often meaningful only when it can be associated with a dependable place:

```text
task
    ↓
unit / room / area / holder / asset
```

Location also provides a shared bridge among several Systems:

```text
Scheduling
        ↘
         shared location identity
        ↗        ↑
Work Queue       │
        ↘        │
        Inventory Management
```

If the Building Map / Locations model is incomplete or inconsistent, several mature Work Queue capabilities become weaker or ambiguous:

- selecting where work belongs;
- determining which unit/room/area is affected;
- linking QR reports to real places;
- validating a reported task location;
- using schedule context;
- linking Inventory Holders to the same place;
- searching work by location;
- producing reliable unit/location reports;
- browsing work spatially.

For that reason, the Work Queue roadmap contains the roadmap area:

```text
RA-13 — Building Map and Location Intelligence
```

The goal is not for Task Assignment and Tracking to absorb Building Map governance.

The goal is for the Project/System to depend on a location model that is complete enough to support reliable task operations.

This dependency should remain visible in future planning and Work Unit derivation.

---

## 14. Roadmap, Work Units, and implementation plans

Task Assignment and Tracking now has a useful planning hierarchy:

```text
Project
    Task Assignment and Tracking
        ↓
System
    Work Queue
        ↓
System Roadmap
    durable future direction
        ↓
Roadmap Area
    capability domain
        ↓
Work Unit
    bounded capability outcome
        ↓
Implementation Plan / tasks
    intended execution method
```

These layers must not be collapsed.

### 14.1 System roadmap

The Work Queue roadmap describes the intended mature System.

It remains useful across many implementation sessions.

### 14.2 Roadmap areas

Roadmap Areas organize durable capability domains.

They are broader than implementation chores.

### 14.3 Work Units

A stable Work Unit should be created only when a capability outcome is sufficiently bounded and useful to track.

Examples of good Work Unit shapes include:

```text
Employee Identity
Supervisor Review Queue
Inventory Transfer Propagation
Building Map Data Completion
Recurring Work Definition
```

A code edit such as:

```text
add employee_id column
```

is generally implementation detail rather than the Work Unit itself.

Do not invent `WORK-####` IDs inside roadmap documents.

The Work Unit Registry assigns stable Work Unit identity.

### 14.4 Implementation plans

An implementation plan describes bounded intended work.

It does not prove execution.

### 14.5 Work Implementation Sessions

A Work Implementation Session records the bounded execution context, decisions, evidence, deviations, tests, resulting state, and handoff.

The current Project Definition work is being performed under such a declared session.

---

## 15. History and architectural evolution

Task Assignment and Tracking has a history that predates the current Project/System vocabulary.

### 15.1 Earlier application-centered understanding

Earlier Klinswork material may:

- call Work Queue a Project;
- organize work around the Work Queue application;
- use the earlier `Tasker` name;
- refer to one deployment or spreadsheet as though it were the whole System;
- describe application features without distinguishing Project/System/Resource;
- contain old paths or URLs;
- describe planned capabilities that were never implemented;
- describe implementation state that was correct only at the time.

Those records should generally remain intact as historical evidence.

Current canonical documentation should explain the newer interpretation without rewriting history to make the present ontology appear older than it is.

### 15.2 Current semantic interpretation

The current architecture distinguishes:

```text
Task Assignment and Tracking
    = durable Project / operational undertaking

Work Queue
    = principal System

Work Queue application
    = Resource / implementation surface

Google Sheets / datasets / Apps Script / deployments
    = Resources

Meadows Housekeeping
    = operational environment
```

### 15.3 Evidence classes

Use three evidence classes explicitly.

```text
HISTORICAL IMPLEMENTATION EVIDENCE
    dated Work Updates
    historical sidecars
    prior screenshots
    prior source snapshots
    dated technical descriptions

PLANNING / DESIGN EVIDENCE
    roadmaps
    implementation plans
    unchecked planned items
    design notes
    future-state architecture

CURRENT IMPLEMENTATION EVIDENCE
    current source
    current Resource Registry
    current deployment
    current datastore / schema
    current executable behavior
    fresh test evidence
```

Rules:

1. Historical evidence establishes what existed or was reported at a particular time.
2. Planning evidence establishes intention, not completion.
3. Current implementation claims require current evidence.
4. Do not convert unchecked plan items into completion claims.
5. Preserve historical terminology when it accurately represents the historical record.
6. Interpret historical material through current architecture without rewriting what the source said.

---

## 16. Current operational evidence boundary

This Project Summary is intentionally not a full live verification of Work Queue.

Current evidence is sufficient to support the Project/System interpretation and several high-level implementation facts, but the detailed current-state System record is still pending.

The Work Queue technical manual provides a useful architecture baseline.

It describes Work Queue as a connected operating environment involving:

```text
Application and operational data
    Work Queue application
    Google Sheets data
    employee/personnel records
    Inventory and SDS relationships

Knowledge / documentation
    Documentation Project
    JSON workflows / schemas / rules
    GitHub repository / Pages
    publication and communication products

Development / integration
    Google Drive / Apps Script
    VS Code
    paths / IDs / permissions / deployments
    testing and reconciliation

Access
    central tools page
    mobile access

Human operations
    architecture
    integration
    testing
    documentation
    maintenance
```

This supports the conclusion that Work Queue is broader than a single screen or prompt-generated application.

However, the later Work Queue System Summary should determine, from current evidence:

- exact current application boundary;
- current source and deployment;
- current datastore/schema;
- current Resources;
- current task lifecycle behavior;
- current history behavior;
- current inventory integration behavior;
- current validation;
- current permissions;
- current tests;
- current unresolved implementation issues.

This Project Summary should not preempt that work.

---

## 17. How to enter or resume work on this Project

A context-naive work session should load Task Assignment and Tracking progressively rather than reading the entire Klinswork repository indiscriminately.

Preferred route:

```text
Task Assignment and Tracking work begins
        ↓
resolve Project identity
        ↓
read ../project-identity.json
        ↓
read ../README.md
        ↓
read this Project Summary
        ↓
resolve required Project relationships
        ↓
identify relevant System
        ↓
read Work Queue README
        ↓
choose current-state or future-state authority
        ↓
System Summary OR System Roadmap
        ↓
resolve required Resources through Registry
        ↓
inspect live implementation evidence when behavior matters
        ↓
read historical records only when chronology / rationale matters
```

### 17.1 For roadmap work

```text
Work Queue README
        ↓
work-queue-roadmap.md
        ↓
roadmap sidecar / Viewer
        ↓
select bounded candidate capability
        ↓
create / resolve Work Unit
        ↓
implementation plan when selected for execution
```

### 17.2 For current implementation work

```text
Work Queue README
        ↓
system-summary.md
        ↓
technical documentation
        ↓
Resource Registry
        ↓
current source / data / deployment
        ↓
tests / fresh verification
```

### 17.3 For Building Map-related task work

```text
Work Queue roadmap / relevant Work Unit
        ↓
resolve shared Building Map / Location authority
        ↓
determine location gaps
        ↓
preserve stable location IDs
        ↓
test Work Queue / Scheduling / Inventory relationships
```

Do not create private duplicate location identities merely to make one Work Queue feature easier.

---

## 18. Project Definition exemplar role

Task Assignment and Tracking is currently the **second working exemplar** for the Klinswork Project Definition architecture.

The first exemplar was:

```text
Inventory Management
    ↓
Inventory 3.0
```

The second exemplar tests whether the same architecture remains useful for a different operational domain:

```text
Task Assignment and Tracking
    ↓
Work Queue
```

The expected Project Definition package is approximately:

```text
Task Assignment and Tracking/
├── project-identity.json
├── README.md
├── summaries/
│   └── project-summary.md
├── sidecars/
│   └── project-summary-sidecar.json
├── systems/
│   └── Work Queue/
│       ├── README.md
│       ├── summaries/
│       │   ├── system-summary.md
│       │   └── work-queue-roadmap.md
│       └── sidecars/
│           ├── system-summary-sidecar.json
│           └── work-queue-roadmap-sidecar.json
└── implementation-plans/
```

The roadmap pair is an extension beyond the minimum first-exemplar package because Work Queue already has a sufficiently mature future-state planning need.

The directory itself is not the definition.

The definition emerges from the coordinated authority roles of the records.

The exemplar should be considered successful when a future person or tool can determine:

- what Project this is;
- what its durable purpose is;
- what its scope and boundaries are;
- where intrinsic identity lives;
- where Project narrative lives;
- where System current-state narrative lives;
- where System future-state direction lives;
- where relationships belong;
- where Resource routing lives;
- what evidence establishes current implementation;
- what happened historically;
- what remains unresolved;
- what work should happen next.

---

## 19. Unresolved questions

The following questions remain intentionally unresolved.

### 19.1 Project identity and registry

- What permanent `PROJ-###` value will be allocated to Task Assignment and Tracking?
- Which authority formally allocates Project IDs?
- What exact precedence/reconciliation rule applies if the Project Registry and `project-identity.json` disagree?
- Does the Project Identity Entity Record need a separate stable record ID in addition to the Project ID?
- Which historical names, if any, should become formal Project aliases rather than remain only historical terms?

### 19.2 Relationships

- What is the final Relationship Registry schema?
- What controlled predicate represents Operations → Task Assignment and Tracking?
- How should Project → System relationships be formalized?
- How should Project → Resource relationships be formalized?
- How should operational-environment relationships be represented?
- How should shared-location dependencies be represented?
- Which relationships should be current-state records versus historical Activities?

### 19.3 System identity

- What permanent `SYS-###` value, if any, will be allocated to Work Queue?
- What fields belong in the System Identity profile?
- What is the final Work Queue System boundary?
- Should the visible Work Queue application be modeled as a distinct Application/Implementation entity beneath the System?
- Which Resources belong specifically to Work Queue versus being shared?

### 19.4 Resource reconciliation

- Which current Work Queue Resources are fully reconciled in the Resource Registry?
- Which source, deployment, and datastore Resource entries are authoritative for current behavior?
- Which shared Resources should be related rather than duplicated?
- What is the authoritative shared Building Map / Locations Resource relationship?
- Which documentation Resources should be formally related to the Project/System?

### 19.5 Work lifecycle

- What is the final controlled task state machine?
- Does rejection always return work to unassigned/available, or do some cases require supervisor review?
- Which transitions are employee-authorized versus supervisor-authorized?
- How should blocked, deferred, cancelled, reopened, and corrected work be represented?
- Which transitions must be preserved as immutable events?

### 19.6 Identity and permissions

- What exact login/authentication mechanism should establish current-user identity?
- How should employee identity resolve against Employee Profile or personnel data?
- Can one person hold Employee, Supervisor, and Administrator roles simultaneously?
- Which actions require server-side permission checks?
- How should temporary/substitute personnel be represented?

### 19.7 Scheduling relationship

- What exact Calendar/System classification will be adopted within Scheduling?
- Which Scheduling data is authoritative for expected assignment?
- How should Work Queue represent divergence between scheduled location and actual work location?
- Which recurring-work rules belong to Scheduling versus Task Assignment and Tracking?

### 19.8 Inventory relationship

- What is the final transaction contract between Work Queue and Inventory 3.0?
- How is the acting employee's cart resolved?
- How are product, quantity, source, destination, task, and employee identities linked?
- What transaction/rollback behavior prevents partial inventory transfers?
- How are corrections and reversals represented?

### 19.9 Building Map / Locations

- What is the complete shared location hierarchy?
- Which location IDs are already stable?
- Which rooms, areas, units, assets, or holders remain unmapped?
- Which Project/System owns or governs completion of the shared Building Map?
- How should QR codes resolve against location authority?
- How should map completion be tested across Work Queue, Scheduling, and Inventory relationships?

### 19.10 Notes, evidence, and images

- What structured note templates should exist?
- Where are task images stored?
- What retention/access rules apply?
- What metadata is required?
- Which roles can add, remove, or review evidence?
- How are corrections handled without destroying history?

### 19.11 QR and OpenAI validation

- What exact QR reporting schema should be used?
- Which reports enter pending supervisor review?
- What may the OpenAI API validate, normalize, classify, or extract?
- What cost controls, privacy boundaries, and failure modes apply?
- How is model uncertainty represented?
- Which facts must always remain human/system-authoritative?

### 19.12 Reporting and paperwork translation

- Which reports are operationally necessary?
- Which report filters and layouts are standard?
- What paperwork should be generated from structured records?
- Should any paper/form inputs be captured back into structured records?
- Which artifact remains authoritative when printed paperwork and digital state disagree?

### 19.13 Viewer and Record Profiles

- Should Project Summaries receive a dedicated Record Profile?
- Should System Roadmaps receive a dedicated Record Profile rather than the current generic-compatible draft?
- How should Entity Records, Project Summaries, System Summaries, and Roadmaps be visually distinguished in the Viewer?
- What companion and discovery validation should be automatic?

### 19.14 Project Definition template

- Which parts of the Inventory Management and Task Assignment and Tracking exemplars are genuinely generic?
- Which Project-definition elements are mandatory versus optional?
- Should every System with active future planning have a roadmap pair?
- When is the architecture mature enough to extract a reusable Project Definition template?

### 19.15 Operational history and current implementation

- What is the fully reconciled chronology of Tasker → Work Queue development?
- Which planned Work Queue capabilities were actually implemented?
- Which tests were actually run?
- What is the current deployment state?
- Which current datastore is authoritative?
- Which earlier resources should be explicitly linked as predecessors?
- Which historical terminology should be preserved as aliases, and which should remain only historical evidence?

These questions should remain visible until evidence or a formal architecture decision resolves them.

---

## 20. Next work

### Immediate next step

Create:

```text
../sidecars/project-summary-sidecar.json
```

as the machine-readable structured companion to this Project Summary.

The sidecar should:

- identify this Markdown document as its companion source;
- use an appropriate recognized document-sidecar profile;
- preserve this Markdown document as the narrative authority;
- identify Task Assignment and Tracking as the subject Project without replacing `project-identity.json`;
- expose purpose, operational function, scope, boundaries, Work Queue context, Resources, relationships, current state, evidence classes, Building Map dependency, and unresolved questions for discovery;
- support the Klinswork Documentation Viewer;
- avoid inventing Project, System, Relationship, or Resource IDs.

### Subsequent Project Definition work

After the Project Summary sidecar:

1. create `../systems/Work Queue/README.md`;
2. create `../systems/Work Queue/summaries/system-summary.md`;
3. create `../systems/Work Queue/sidecars/system-summary-sidecar.json`;
4. reconcile the current Work Queue Resource set;
5. regenerate the Klinswork Documentation Viewer manifest;
6. verify Project-space discovery;
7. verify Project Summary companion resolution;
8. verify Work Queue roadmap companion resolution;
9. verify that `project-identity.json` remains an Entity Record rather than a sidecar;
10. inspect the Project and System records in the Viewer;
11. reconcile profile, path, manifest, catalog, and Viewer failures;
12. test a context-naive resume sequence;
13. assess Resource Registry / Activity Registry / Architecture Changelog effects;
14. update and close the current Work Implementation Session;
15. derive reusable Project Definition rules only after the second exemplar has exposed any architecture weaknesses.

### Product-planning follow-on

Once the Project/System current-state package is complete:

1. review the Work Queue roadmap against the Work Queue System Summary;
2. mark roadmap capabilities more precisely as existing, partial, planned, blocked, or not-yet-assessed;
3. identify candidate Work Units that are sufficiently bounded;
4. allocate stable Work Unit IDs only through the Work Unit Registry;
5. prioritize foundational Work Units before dependent capability layers;
6. coordinate Building Map, Scheduling, Employee Profile, and Inventory dependencies rather than implementing duplicate local substitutes.

---

## 21. Resulting Project state

Task Assignment and Tracking now has the beginnings of a durable Project-definition layer independent of its current Work Queue implementation.

The important conceptual result is:

```text
Task Assignment and Tracking
        │
        ├── identity
        │     → ../project-identity.json
        │
        ├── local orientation
        │     → ../README.md
        │
        ├── rich Project definition
        │     → summaries/project-summary.md
        │
        ├── machine-readable Project Summary
        │     → ../sidecars/project-summary-sidecar.json [next]
        │
        ├── principal System
        │     → ../systems/Work Queue/
        │
        ├── current System definition
        │     → Work Queue/system-summary.md [pending]
        │
        ├── future System direction
        │     → Work Queue/work-queue-roadmap.md
        │
        ├── bounded planned work
        │     → ../implementation-plans/
        │
        ├── Work Units
        │     → Work Unit Registry
        │
        ├── Resource routing
        │     → Resource Registry
        │
        ├── cross-entity relationships
        │     → future/formal relationship authority
        │
        └── history / provenance
              → Activities + Work Implementation Sessions + preserved historical records
```

This structure allows the Project to remain intelligible if:

- Work Queue is replaced;
- the app is redesigned;
- a deployment URL changes;
- Google Sheets is replaced as a datastore;
- the repository is reorganized;
- the parent relationship changes;
- the Project is used in another operational environment;
- Building Map or Scheduling infrastructure changes;
- Inventory integration is redesigned.

That is the central purpose of the Project Definition architecture.

---

## 22. Current canonical interpretation

The current semantic model is:

```text
Klinswork
└── Operations                                      [Project]
    └── Task Assignment and Tracking                [Project]
        └── Work Queue                              [System]
            ├── Work Queue application              [Resource / implementation surface]
            ├── Work Queue data                     [Resources]
            ├── Employees reference                 [shared / related Resource]
            ├── Locations / Building Map            [shared / related Resource]
            ├── Inventory integration               [cross-Project relationship]
            ├── Scheduling integration              [cross-Project relationship]
            ├── technical documentation             [Resource]
            ├── current-state System documentation
            └── future-state System roadmap
```

The durable Project concern is:

> **the lifecycle, responsibility, evidence, completion, verification, reporting, downstream effects, and preserved history of discrete operational work.**

The durable System concern is:

> **the coherent Work Queue mechanism used to support that operational function.**

The Building Map concern is:

> **shared, stable location identity and coverage sufficient for reliable task, schedule, QR, inventory-holder, search, reporting, and map relationships.**

The roadmap concern is:

> **the intended mature capability of Work Queue.**

Those distinctions should remain visible as the Project evolves.

---

## 23. Source and evidence basis

This Project Summary was reconciled from the current Project Definition work and supporting evidence available as of 2026-08-16.

Principal source classes include:

### Current Project-definition records

- `Task Assignment and Tracking/project-identity.json`
- `Task Assignment and Tracking/README.md`
- `work-implementation-session-2026-08-16-task-assignment-and-tracking.md`

### Reference exemplar

- `Inventory Management/project-identity.json`
- `Inventory Management/README.md`
- `Inventory Management/summaries/project-summary.md`
- Inventory 3.0 Project/System Definition records

### Current Work Queue planning records

- `Work Queue/summaries/work-queue-roadmap.md`
- `Work Queue/sidecars/work-queue-roadmap-sidecar.json`
- `klinswork-system-roadmap-catalog-001.json`

### Work Queue architecture / implementation evidence

- `work-queue-app-technical-manual`
- current Work Queue Resource references
- current repository structure

### Evidence discipline

This Summary does not silently promote roadmap intent into current implementation truth.

Where detailed current behavior matters, the next Work Queue System Summary should verify it from current implementation evidence.

---

## 24. Governing rule

The Project should remain understandable through distributed authority rather than one overloaded file.

```text
project-identity.json
    = who / which Project this is

README.md
    = how to orient and navigate here

project-summary.md
    = what the Project means

project-summary-sidecar.json
    = structured companion to Project meaning

Work Queue README
    = how to orient within the System

Work Queue system-summary.md
    = what Work Queue is now

Work Queue roadmap.md
    = what Work Queue should become

Work Unit Registry
    = bounded capability identities selected for tracking

implementation plan
    = bounded intended method

Work Implementation Session
    = execution record

Resource Registry
    = Resource identity and routing

relationship authority
    = cross-entity relationships

current source / data / deployment / tests
    = current implementation truth where applicable
```

Do not collapse these authorities merely because they concern the same Project or System.
