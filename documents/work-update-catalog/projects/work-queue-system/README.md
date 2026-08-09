# Work Queue System

**Project documentation root:** `documentation/documents/work-update-catalog/projects/work-queue-system/`  
**Status:** Active working document  
**Purpose:** Highest-level canonical orientation document for the Work Queue system  
**Last major working revision:** 2026-08-09

---

## 1. Purpose of This Document

This README is the highest-level documentation entry point for the **Work Queue system** within the Klinswork Tools documentation structure.

Its job is to establish enough authoritative context that a human maintainer or AI assistant can understand:

- what the Work Queue system is;
- what operational problem it represents;
- what belongs to the project;
- what does not belong to the project;
- which applications, data stores, integrations, and documentation resources participate in it;
- where deeper technical or implementation documentation lives;
- which sources should be trusted for different kinds of information;
- how to navigate from this project-level description down to individual artifacts.

This document is not intended to duplicate every implementation detail.

It should remain a **project-level map and semantic authority**, with deeper explanations delegated to lower-level documents, source files, technical manuals, manifests, data records, and historical work documentation.

---

## 2. Project Identity

The Work Queue system is the Klinswork project concerned with **representing, assigning, tracking, completing, and preserving operational work**.

The visible Work Queue web application is one implementation of this project.

The project itself is broader than the application.

Conceptually:

```text
Work Queue system
    │
    ├── represented operational process
    │      ├── work is identified
    │      ├── work becomes a task
    │      ├── responsibility is assigned
    │      ├── status changes are recorded
    │      ├── work is completed
    │      └── history and downstream effects are preserved
    │
    ├── application implementation
    │      └── Work Queue Apps Script web application
    │
    ├── structured data
    │      ├── tasks
    │      ├── employees / assignees
    │      ├── locations
    │      ├── status and completion information
    │      └── related operational records
    │
    ├── integrations
    │      ├── inventory
    │      ├── locations
    │      ├── personnel / employee records
    │      └── other Klinswork services as they are verified
    │
    └── documentation and history
           ├── project documentation
           ├── technical/manual documentation
           ├── work updates
           ├── sidecars and structured records
           └── historical implementation material
```

---

## 3. Core Principle

**The Work Queue application is not the Work Queue project.**

The application is a user-facing implementation of a larger operational system.

The project includes the meaning of the work records, assignment rules, responsibility relationships, location relationships, completion behavior, downstream integrations, historical evolution, and documentation needed to understand and maintain the system.

This distinction should be preserved throughout the documentation.

---

## 4. Operational System Being Represented

At the highest level, Work Queue models the lifecycle of work.

A simplified model is:

```text
need / work request
        ↓
task record
        ↓
assignment
        ↓
active work
        ↓
status change
        ↓
completion
        ↓
history / downstream effects
```

The digital implementation should be understood as a representation of this operational process rather than as the source of the process itself.

As this README is developed, this section should eventually describe:

- what qualifies as a task;
- how tasks originate;
- who or what may own a task;
- who may be assigned to perform it;
- how locations participate;
- what task states exist;
- what completion means;
- what records completion creates or changes;
- how bulk assignment works;
- how task history is preserved;
- what downstream systems may react to task completion.

---

## 5. Current Implementation

The current visible implementation is an **Apps Script web application** backed by structured Google Sheets data.

At a high level, the implementation includes:

```text
Browser
    ↓
Work Queue web application
    ↓
Apps Script services / logic
    ↓
Google Sheets data
    ↓
related Klinswork data and integrations
```

Current implementation details should be verified against the live source before being treated as current truth.

Historical descriptions remain useful as design evidence even when code has changed.

---

## 6. Current Known Capabilities

Known current capabilities include:

- creating work tasks;
- assigning work;
- associating tasks with employees;
- using stable employee identifiers;
- associating work with locations;
- tracking task status;
- completing tasks;
- recording structured task data;
- supporting task-to-inventory relationships;
- creating an `Inventory_Holder_Event` from applicable completed work;
- supporting future or developing bulk-assignment workflows.

This list is intentionally high-level.

Detailed capability descriptions should eventually live in lower-level documentation and be verified against the live implementation.

---

## 7. Primary Data Relationships

The Work Queue system depends on several structured data domains.

### Tasks

Task records are central to the project.

They represent work that has been created, assigned, tracked, and completed.

Important task fields and lifecycle rules should be documented separately and referenced here.

### Employees

Employee records provide the personnel dimension used by Work Queue.

The system can associate tasks with an assigned employee using a stable employee identifier.

Employee data may be shared with other Klinswork systems and should not automatically be considered owned by Work Queue.

### Locations

Tasks may reference operational locations.

Location data is a shared foundation and may have its own authority outside the Work Queue project.

The exact authoritative location source should be documented and reconciled where multiple historical location datasets exist.

### Inventory relationships

Work Queue can interact with inventory-state records.

A verified example is task completion creating an `Inventory_Holder_Event` associated with the exact relevant holder or location.

Inventory itself remains a separate project/domain even when Work Queue initiates or displays inventory-related activity.

---

## 8. Project Boundaries

### In scope

The Work Queue project includes the systems and rules directly necessary to represent and manage operational work, including:

- task identity;
- task creation;
- assignment;
- employee association;
- location association;
- status;
- completion;
- task history;
- task-related interfaces;
- task-specific configuration;
- task-triggered integration behavior;
- Work Queue-specific documentation and implementation history.

### Related but not automatically part of Work Queue

The following may be essential to Work Queue without belonging to the Work Queue project:

- Inventory Management;
- shared employee/personnel data;
- shared location data;
- SDS and product-information systems;
- Email Composer;
- Documentation project;
- GitHub / GitHub Pages;
- Google Sites;
- general Klinswork infrastructure;
- shared Apps Script services;
- shared Drive resources.

Project membership should be determined by function and authority, not merely by dependency.

---

## 9. Integrations

Work Queue participates in relationships with other Klinswork systems.

Known or developing relationships include:

### Inventory

Task completion can create inventory-holder activity for applicable tasks.

The exact integration contract should eventually document:

- triggering task conditions;
- shared IDs;
- location/holder mapping;
- event creation;
- quantity/state distinctions;
- downstream inventory effects;
- error behavior;
- verification requirements.

### Employees

Work Queue uses employee records to support assignment and responsibility.

The employee data source should be treated as a shared authority unless project documentation establishes otherwise.

### Locations

Work Queue uses location records to identify where work occurs and to support downstream operational relationships.

### Other integrations

Additional integrations should be added only when verified.

Do not infer project relationships simply because two systems appear in the same document or repository.

---

## 10. Technical Manual / Ecosystem Document

A separate Google Doc is being developed as a **technical and ecosystem manual** for Work Queue.

That document contains broader and more detailed discussion of:

- application components;
- Apps Script files and their intended responsibilities;
- data layers;
- integrations;
- infrastructure;
- development tools;
- hosting;
- publishing;
- human maintenance;
- historical system understanding.

The technical manual is intentionally separate from this README.

This README should remain the highest-level project orientation document.

The technical manual may preserve older conceptual explanations even when they have not yet been verified against current code.

During future documentation work, those explanations can be used as hypotheses and navigation aids, then compared with the live implementation.

**Technical / ecosystem manual:**

https://docs.google.com/document/d/12ejlkcZEs6B7F-Ti2t8uO_uLzMUrI4qNqo77ZkswbaQ/edit

---

## 11. Documentation Authority

Different artifacts answer different questions.

### This README

Authoritative for:

- project identity;
- project purpose;
- project boundaries;
- highest-level architecture;
- navigation to deeper documentation;
- current high-level project relationships.

### Technical / ecosystem manual

Useful for:

- deeper conceptual explanation;
- component descriptions;
- historical technical understanding;
- Apps Script file roles;
- infrastructure relationships;
- implementation interpretation.

It should not automatically be assumed to describe current code exactly.

### Live source code

Authoritative for:

- what the current implementation actually does.

Code should be inspected directly when implementation accuracy matters.

### Current data stores

Authoritative for:

- current structured records and schemas, subject to the authority rules of the relevant data domain.

### Work updates and historical records

Authoritative for:

- what was understood, changed, tested, or decided at a particular time.

Historical truth should not automatically be treated as current truth.

---

## 12. Apps Script Documentation Model

Apps Script source files may not always be directly searchable from an AI work session.

For that reason, project documentation should preserve conceptual descriptions of important source files.

A file-level description may include:

```text
Apps Script file
    ├── intended responsibility
    ├── important functions
    ├── data read
    ├── data written
    ├── services used
    ├── callers / consumers
    ├── important IDs / field contracts
    ├── integration responsibilities
    ├── historical design notes
    └── verified-current observations
```

These descriptions do not need to claim that old documentation exactly matches current code.

Instead, they provide a map for future code inspection.

When implementation accuracy matters:

```text
conceptual / historical description
        ↓
inspect live source
        ↓
compare expected role with actual behavior
        ↓
update canonical documentation
```

---

## 13. Documentation Navigation

This project should be navigable from high-level meaning down to implementation detail.

Expected hierarchy:

```text
Klinswork Tools Resource Registry
        ↓
Work Queue project
        ↓
this README
        ↓
technical / resource documentation
        ↓
folder manifest / repository manifest
        ↓
specific source, data, history, or implementation artifact
```

The Resource Registry should eventually point to this README as the canonical metadata/context reference for Work Queue project resources where appropriate.

---

## 14. Folder Contents and Manifests

The physical contents of this project folder may be exposed through a repository-level or project-level manifest.

The manifest's role is **location and discovery**, not semantic interpretation.

Conceptually:

```text
README.md
    = what this project is and how to navigate it

manifest
    = what files physically exist and where

individual files
    = implementation, evidence, history, or deeper documentation
```

If a project-specific manifest is later created, reference it here.

If the root `repository-manifest.json` already exposes this folder completely, a separate project manifest may not be necessary.

Expected repository path:

```text
documents/work-update-catalog/projects/work-queue-system/
```

---

## 15. Documentation Development Method

The Work Queue documentation will be developed primarily **from the bottom up**.

Existing documents, source files, data structures, applications, work updates, sidecars, manifests, and historical records will be inspected and organized.

The resulting understanding will then be reconciled upward into this README.

Conceptually:

```text
actual implementation / evidence
        ↑
resource-level documentation
        ↑
Work Queue project documentation
        ↑
Klinswork Tools Resource Registry
```

Once established, future work sessions will normally navigate in the opposite direction:

```text
Klinswork Tools Resource Registry
        ↓
Work Queue project README
        ↓
resource / technical documentation
        ↓
specific implementation artifacts
```

**Bottom-up work establishes truth; top-down structure makes that truth navigable.**

---

## 16. Historical Material

Historical Work Queue documents should generally be preserved.

Older descriptions may reveal:

- previous architecture;
- former assumptions;
- abandoned designs;
- earlier data models;
- deployment history;
- terminology changes;
- integration evolution;
- reasons current structures exist.

Outdated material should be classified rather than silently erased.

Where possible, documentation should distinguish:

- current;
- historical;
- superseded;
- provisional;
- planned;
- unresolved.

---

## 17. Current Documentation Priorities

This README is intentionally incomplete.

Near-term documentation work should establish:

1. formal Work Queue project identity and Project ID;
2. exact project boundary;
3. current app architecture;
4. Apps Script file inventory and roles;
5. task data model;
6. employee relationship;
7. location relationship;
8. inventory integration;
9. task lifecycle and status model;
10. assignment and bulk-assignment behavior;
11. current deployment information;
12. current source-of-truth records;
13. important historical versions and transitions;
14. canonical technical/manual references;
15. project integrations;
16. project-specific work updates and sidecars;
17. unresolved architectural questions.

---

## 18. Open Questions

The following questions should be resolved during the next documentation pass:

- What formal Project ID should Work Queue use?
- What is the exact canonical name of the project?
- Which data tables are owned by Work Queue?
- Which data tables are shared foundations?
- What is the current authoritative Locations source?
- What is the complete current task lifecycle?
- Which Apps Script files currently implement each capability?
- Which functions are public entry points versus internal helpers?
- What task-completion actions exist besides status change?
- What inventory effects are implemented now?
- Which inventory effects remain planned?
- How should bulk assignment be modeled at the project level?
- What versions or deployments should be treated as historical?
- Which work updates constitute major architectural milestones?
- Which other Klinswork projects have durable integrations with Work Queue?

Unresolved questions should remain explicit rather than being filled with assumptions.

---

## 19. Working Rule for Future Sessions

A future work session entering Work Queue through the Klinswork Tools Resource Registry should:

1. read this README;
2. identify the specific subsystem or question involved;
3. follow the relevant technical/manual or resource documentation;
4. use manifests to locate physical artifacts;
5. inspect current source or data when implementation accuracy matters;
6. consult historical work updates when chronology or rationale matters;
7. update lower-level documentation first when new facts are discovered;
8. reconcile durable project-level changes back into this README;
9. update the Resource Registry when routing, identity, or canonical context changes.

Do not attempt to load every Work Queue artifact before beginning work.

Use progressive context acquisition.

---

## 20. Status

This README is a newly created working document and is expected to change substantially as the Work Queue system is examined in detail.

Its immediate purpose is to establish the correct documentation layer and give the next documentation session a stable place to reconcile discoveries.

The intended long-term role is to become the canonical highest-level description of the Work Queue system within the Klinswork Documentation repository.
