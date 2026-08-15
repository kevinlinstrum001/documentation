# Operations

**Project documentation root:** `documentation/documents/work-update-catalog/projects/operations/`  
**Entity type:** Parent Project  
**Project ID:** To be assigned during Project Registry formalization  
**Status:** Active working architecture  
**Primary current operational environment:** Meadows Housekeeping  
**Purpose:** Highest-level canonical orientation document for the Klinswork Operations project family  
**Last major working revision:** 2026-08-15

---

## 1. Purpose of This Document

This README is the highest-level documentation entry point for the **Operations** parent project within Klinswork.

Its purpose is to establish enough authoritative context that a human maintainer or AI assistant can understand:

- what the Operations project is;
- which child projects belong beneath it;
- what real operational work those projects represent;
- how systems relate to projects;
- how shared resources cross project boundaries;
- what belongs to Operations and what does not;
- where canonical child-project documentation lives;
- how to navigate from the Operations project down to systems, resources, implementation evidence, and history;
- which sources should be trusted for different kinds of information.

This README should remain a **parent-project map and semantic authority**.

It should not duplicate the detailed operational, technical, or implementation documentation maintained by child projects and systems.

---

## 2. Project Identity

**Canonical name:** Operations  
**Entity type:** Parent Project  
**Parent:** Klinswork  
**Project ID:** Pending  
**Primary current environment:** Meadows Housekeeping  
**Boundary status:** Confirmed at the parent-project level

Operations is the Klinswork parent project concerned with organizing durable bodies of work that model, document, analyze, or support real operational activity.

The current Operations project family is centered on Meadows Housekeeping.

Conceptually:

```text
Klinswork
    ↓
Operations
    │
    ├── Inventory Management
    ├── Scheduling
    ├── Task Assignment and Tracking
    └── Employee Achievements
```

Each child project may contain one or more systems.

Example:

```text
Operations
    ↓
Task Assignment and Tracking
    ↓
Work Queue
```

In this relationship:

- **Operations** is the parent project;
- **Task Assignment and Tracking** is a child project;
- **Work Queue** is a system within that project;
- individual deployments, workbooks, datasets, scripts, and documents are resources used by that system or project.

---

## 3. Core Principle

**Projects, systems, and resources are different entities.**

The Operations project family should not be organized around application names alone.

A real operational need may continue to exist before, during, or after a particular system or application is created.

Likewise, a project may contain several systems over its lifetime.

The current working relationship is:

```text
Project
    ↓
Child Project, where applicable
    ↓
System
    ↓
Resource
```

The physical repository structure may resemble this hierarchy, but repository location does not define semantic identity.

---

## 4. Primary Operational Environment

The primary current operational environment represented by Operations is:

**Meadows Housekeeping**

Meadows Housekeeping is the real-world setting from which much of the current Operations work originates.

It includes:

- housekeeping employees and supervisors;
- work areas and locations;
- routine cleaning and maintenance;
- schedules and area assignments;
- supply storage and replenishment;
- work requests and task assignment;
- completion reporting;
- observations and inspections;
- paper records;
- verbal reports;
- email and other communications;
- operational history.

The operational environment is not itself assumed to be a project.

It supplies the people, work, evidence, constraints, and processes represented by Operations projects and systems.

The Operations architecture should remain capable of representing additional operational environments in the future without requiring existing project identities to change.

---

## 5. Current Child Projects

### Inventory Management

**Entity type:** Child Project  
**Parent:** Operations  
**Status:** Active  
**Project ID:** Pending

Inventory Management organizes work concerned with supply identity, quantity, storage, movement, replenishment, consumption, product information, and inventory history.

Its represented operational function exists independently of any software implementation.

Principal current system:

```text
Inventory Management
    ↓
Inventory 3.0
```

Inventory 3.0 is a system within the Inventory Management project.

Its resources include application deployments, Apps Script projects, inventory workbooks, product records, Inventory Events, SDS-related records, and other registered artifacts.

Canonical project documentation should live beneath:

```text
projects/operations/Inventory Management/
```

---

### Scheduling

**Entity type:** Child Project  
**Parent:** Operations  
**Status:** Active / architecture under reconciliation  
**Project ID:** Pending

Scheduling organizes work concerned with:

- who is expected to be where;
- on what date;
- at what time;
- under what assignment or coverage arrangement.

Scheduling should remain distinct from Task Assignment and Tracking.

Being scheduled to an area may imply routine operational responsibilities without creating a discrete task record.

Systems and implementations may include calendar, roster, schedule-display, trigger, or related scheduling mechanisms as they are reconciled and formally identified.

---

### Task Assignment and Tracking

**Entity type:** Child Project  
**Parent:** Operations  
**Status:** Active  
**Project ID:** Pending

Task Assignment and Tracking organizes work concerned with:

- work intake;
- task identity;
- assignment;
- communication;
- responsibility;
- status;
- performance;
- completion;
- verification;
- reporting;
- history;
- downstream effects.

Principal current system:

```text
Task Assignment and Tracking
    ↓
Work Queue
```

Work Queue is a system within the Task Assignment and Tracking project.

The Work Queue system may include:

- a deployed web application;
- Apps Script services and logic;
- structured Google Sheets data;
- task records;
- assignment data;
- employee relationships;
- location relationships;
- activity/history records;
- inventory-linked completion behavior;
- system-specific technical documentation;
- historical implementations.

The Work Queue system is broader than any one deployment URL or workbook.

---

### Employee Achievements

**Entity type:** Child Project candidate  
**Parent:** Operations  
**Status:** Provisional  
**Project ID:** Not yet assigned

Employee Achievements is the current working project candidate concerned with:

- accomplishments;
- contribution;
- training;
- recognition;
- demonstrated capability;
- work history;
- evidence of completed or improved work.

Its exact boundary remains under review.

A permanent Project ID should not be assigned until its scope is sufficiently reconciled and distinguished from:

- Task Assignment and Tracking;
- Documentation;
- official institutional performance evaluation;
- general employment records;
- personal portfolio material.

---

## 6. Operational Functions and Systems

An Operations project may represent a real-world operational function while containing one or more Klinswork systems that model or support that function.

Example:

```text
Task Assignment and Tracking project
    │
    ├── represents:
    │      real work intake, assignment,
    │      completion, reporting, and history
    │
    └── contains:
           Work Queue system
```

This distinction is important.

The real operational function does not depend on the Klinswork system.

Paperwork, verbal instructions, ordinary institutional procedures, observations, email, or other channels may continue to perform or record the real work even when no Klinswork system is used.

---

## 7. Paperwork Parallel

Operations projects should preserve a **paperwork parallel**.

Klinswork systems may structure, mirror, reconcile, analyze, route, or preserve operational information, but they should not be described as the source of the real operational process merely because the digital system exists.

Operational information may originate through:

- institutional forms;
- paper lists;
- handwritten notes;
- verbal reports;
- supervisor instructions;
- employee observations;
- photographs;
- email;
- meetings;
- direct physical inspection;
- digital forms;
- system-generated events;
- later transcription or batch conversion.

A person may participate in an Operations project as an information provider without ever directly using a Klinswork system.

Digital participation, operational participation, editorial authority, and administrative authority should not be inferred from one another.

---

## 8. Project Boundaries

### In scope for Operations

Operations includes durable Klinswork projects concerned with real operational work, including:

- inventory and supply management;
- scheduling and coverage;
- task assignment and tracking;
- work-performance evidence and achievements where that project boundary is confirmed;
- systems developed within those projects;
- project-specific implementation plans;
- project-specific histories;
- project-specific documentation;
- tests and deployment decisions;
- non-deployment and adoption decisions;
- integrations among Operations projects and systems.

### Related but not automatically part of Operations

The following may support Operations without belonging exclusively to it:

- Documentation;
- Klinswork Resource Registry;
- Email Composer;
- shared employee and role records;
- shared Locations data;
- common identifiers;
- repository infrastructure;
- GitHub / GitHub Pages;
- Google Drive;
- Google Sites;
- shared Apps Script infrastructure;
- import/export utilities;
- generic viewers;
- general Klinswork communication resources.

Project membership should be determined by purpose, scope, and authority rather than dependency alone.

---

## 9. Shared Resources

Operations projects rely on resources that may cross multiple project boundaries.

Examples include:

- shared Locations data;
- employee and role data;
- Email Composer;
- common identifier sets;
- repository infrastructure;
- reusable forms and templates;
- common import/export tools;
- shared documentation and publication infrastructure.

A shared resource should normally be registered once in the Klinswork Resource Registry and related to every project or system that uses it.

It should not be duplicated conceptually into each project as though independently owned.

---

## 10. Integration Model

Operations projects and systems may exchange information while retaining separate authority.

For example:

```text
Task Assignment and Tracking
        ↓
Work Queue completion
        ↓
inventory-related event request
        ↓
Inventory Management
```

Task Assignment and Tracking owns the task and completion relationship.

Inventory Management owns the resulting inventory-state effect.

Likewise:

```text
Scheduling
        ↓
person / place / time relationship

Task Assignment and Tracking
        ↓
specific work responsibility / task relationship
```

The fact that two projects share data or trigger one another does not merge their identities.

Integration documentation should identify:

- participating projects;
- participating systems;
- shared identifiers;
- triggering conditions;
- records exchanged or created;
- source-system authority;
- error behavior;
- verification requirements;
- current versus planned behavior.

---

## 11. Relationship to Documentation

Documentation is a separate Klinswork project.

It supports Operations by preserving and organizing:

- project READMEs;
- system documentation;
- implementation plans;
- work updates;
- summaries;
- sidecars;
- catalogs;
- manifests;
- templates;
- workflow records;
- lessons;
- technical manuals;
- historical records;
- publication artifacts.

Documentation does not become an Operations project merely because it documents Operations.

Operations documentation should use the Documentation project infrastructure while preserving the identity and authority of the operational projects being described.

---

## 12. Project Documentation Structure

The canonical physical root for Operations project documentation is:

```text
documents/work-update-catalog/projects/operations/
```

The expected structure is approximately:

```text
operations/
├── README.md
├── Inventory Management/
│   ├── README.md
│   ├── systems/
│   ├── implementation-plans/
│   └── other project material
├── Scheduling/
│   ├── README.md
│   └── ...
├── Task Assignment and Tracking/
│   ├── README.md
│   ├── systems/
│   │   └── Work Queue/
│   └── ...
└── Employee Achievements/
    ├── README.md
    └── ...
```

Not every directory must exist immediately.

Folders should be created when they have meaningful content rather than as empty placeholders.

Repository layout supports navigation but does not itself establish project identity.

---

## 13. Project and System Identity

Projects use the planned identifier namespace:

```text
PROJ-###
```

Systems use the planned identifier namespace:

```text
SYS-###
```

Resources already use:

```text
RES-###
```

Example:

```text
PROJ-??? — Task Assignment and Tracking
    ↓
SYS-??? — Work Queue
    ↓
RES-002 — Work Queue deployed application
RES-003 — Work Queue data workbook
RES-012 — Work Queue Tasks dataset
RES-013 — Work Queue Employees dataset
...
```

Project, system, and resource identity should remain stable across ordinary location changes.

Identity should not encode hierarchy.

For example:

```text
Project ID: PROJ-004
Parent Project ID: PROJ-001
```

is preferred over constructing a hierarchical identifier such as:

```text
PROJ-001-004
```

Relationships should be stored as relationships.

---

## 14. Documentation Authority

Different artifacts answer different questions.

### This README

Authoritative for:

- Operations parent-project identity;
- current child-project structure;
- parent-level scope and boundaries;
- relationships among Operations child projects;
- parent-level navigation;
- current high-level terminology.

### Child-Project READMEs

Authoritative for:

- child-project identity;
- purpose;
- scope;
- boundaries;
- systems;
- project-specific history;
- project-specific navigation.

### System Documentation

Authoritative for:

- system identity;
- system purpose;
- architecture;
- resources;
- current known capabilities at the appropriate level;
- implementation relationships.

### Live Source Code

Authoritative for:

- what a current software implementation actually does.

Current implementation claims should be verified against live source where implementation accuracy matters.

### Current Data Stores

Authoritative for:

- current structured records and schemas, subject to the authority rules of the relevant project and data domain.

### Work Updates and Historical Records

Authoritative for:

- what was understood;
- what changed;
- what was tested;
- what was deployed;
- what was decided;
- what was considered current at a particular time.

Historical truth should not automatically be treated as current truth.

---

## 15. Historical Terminology

Operations documentation contains important bootstrap-era and transitional terminology.

Earlier records may:

- call Work Queue a project;
- call Inventory Management a system rather than a project;
- call Work Queue an application rather than a system;
- organize work around application names;
- place system-level material directly under project directories;
- use older repository paths;
- describe planned structures that were later revised.

These records should normally be preserved.

The current architecture should not be projected backward into historical documents as though it always existed.

Instead, canonical documentation should identify the relationship between:

```text
historical terminology
    ↓
transitional terminology
    ↓
current canonical terminology
```

This README supersedes the former use of `projects/operations/README.md` as a Work Queue project README.

The useful Work Queue-specific content from that earlier document should be preserved and reconciled into the canonical documentation for:

```text
Operations
    ↓
Task Assignment and Tracking
    ↓
Work Queue
```

---

## 16. Repository Structure Versus Semantic Structure

The physical repository answers:

> Where is the file?

Project documentation answers:

> What does the thing mean?

The Project Registry answers:

> What stable project identity and relationship does this project have?

The Resource Registry answers:

> What registered resource is this, and where is it now?

A manifest answers:

> What files or records physically exist and where are they located?

Conceptually:

```text
projects/README.md
    = rules for the Klinswork project layer

operations/README.md
    = meaning and navigation for Operations

child-project README
    = meaning and navigation for one Operations project

system documentation
    = meaning and architecture for one system

Project Registry
    = stable project identity and relationships

Resource Registry
    = resource identity, routing, location, and provenance

manifest
    = physical discovery
```

---

## 17. Progressive Context Acquisition

A future work session should not load every Operations artifact before beginning.

Preferred route:

```text
Klinswork orientation
    ↓
projects/README.md
    ↓
Operations README
    ↓
relevant child-project README
    ↓
relevant system documentation
    ↓
specific resource, source, data, history, or evidence
```

Example:

```text
Klinswork
    ↓
Operations
    ↓
Task Assignment and Tracking
    ↓
Work Queue
    ↓
current Work Queue source/data/resources
```

Use the Resource Registry to resolve registered resources to their current locations.

Use historical work updates when chronology or rationale matters.

Use live source and current data when implementation accuracy matters.

---

## 18. Current Documentation Priorities

The immediate Operations documentation priorities are:

1. assign the permanent Project ID for Operations after the project-ID rules are finalized;
2. create or reconcile canonical READMEs for Inventory Management;
3. create or reconcile canonical READMEs for Scheduling;
4. create or reconcile canonical READMEs for Task Assignment and Tracking;
5. determine whether Employee Achievements is ready for permanent project identity;
6. move or reconcile Work Queue-specific documentation beneath Task Assignment and Tracking;
7. identify the first formal systems and assign `SYS-###` identifiers only after system-ID rules are finalized;
8. reconcile old application-centered terminology without erasing historical evidence;
9. establish canonical project relationships in the future Project Registry;
10. ensure the Resource Registry points to canonical project/system context where appropriate.

---

## 19. Open Determinations

The following questions remain open:

- What permanent `PROJ-###` ID should Operations receive?
- What permanent IDs should its confirmed child projects receive?
- Is Employee Achievements sufficiently mature to receive a permanent Project ID?
- What exact project type vocabulary should be used in the Project Registry?
- What permanent `SYS-###` ID should Work Queue receive?
- What permanent `SYS-###` ID should Inventory 3.0 receive?
- Which scheduling implementations should be treated as distinct systems?
- Which employee and role records belong to shared infrastructure rather than an Operations project?
- What exact canonical child-project folder names should be used?
- Which bootstrap-era Work Queue documentation should be moved, linked, or preserved in place?
- Which integrations require dedicated contracts or relationship records?
- What additional Operations projects may emerge from future documentation work?

Unresolved questions should remain explicit rather than being filled with assumptions.

---

## 20. Working Rule for Future Sessions

A future session entering the Operations project should:

1. read the repository root README when broader repository orientation is needed;
2. read `projects/README.md` for current project-layer rules;
3. read this Operations README;
4. identify the child project involved;
5. read that project's canonical README;
6. identify the system or operational question involved;
7. follow relevant system documentation;
8. resolve registered resources through the Resource Registry;
9. inspect current source or data when implementation accuracy matters;
10. consult historical records when chronology or rationale matters;
11. update lower-level documentation first when new detailed facts are discovered;
12. reconcile durable project-level discoveries upward into the appropriate project README;
13. update the Project Registry when project identity or relationships change;
14. update the Resource Registry when registered resource identity, routing, or canonical location changes.

Do not attempt to load the entire Operations project family before beginning work.

Use progressive context acquisition.

---

## 21. Status

Operations is now treated as the **parent project** for the current Klinswork operational project family.

The earlier `projects/operations/README.md` described Work Queue using an older project-centered vocabulary. That document represented an important transitional stage in the architecture, but its identity model has now been superseded.

The current structure separates:

```text
Operations
    ↓
child projects
    ↓
systems
    ↓
resources
```

The next major milestone is to reconcile the canonical child-project READMEs and then assign durable `PROJ-###` identities through the formal Project Registry.
