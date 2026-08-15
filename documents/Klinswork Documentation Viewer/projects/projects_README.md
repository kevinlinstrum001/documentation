# Klinswork Projects

**Repository path:** `documentation/documents/work-update-catalog/projects/`  
**Status:** Active working architecture  
**Purpose:** Canonical orientation for the Klinswork project layer  
**Project ID namespace:** `PROJ-###`  
**Last revised:** 2026-08-15

---

## 1. Purpose of This Directory

This directory is the canonical documentation root for **Klinswork projects**.

It exists to provide a stable, human-readable and machine-routable structure for identifying projects, documenting their relationships, locating their canonical project records, and navigating from high-level project meaning down to the systems and resources that implement or support that work.

This directory should answer questions such as:

- What projects currently exist in Klinswork?
- Which projects are parent projects?
- Which projects are children of other projects?
- What is the canonical identity of each project?
- What systems belong to each project?
- Which resources support a project without belonging exclusively to it?
- Where is the authoritative README for a project?
- Which parts of the repository are historical, provisional, or still unresolved?
- How should a new work session move from project identity to current implementation evidence?

This README defines the **project layer itself**. Individual project READMEs define the meaning, boundaries, systems, history, and current state of particular projects.

---

## 2. Project Model

Klinswork is the broader organizing environment.

Within Klinswork, work is organized into durable projects. A project may contain child projects and systems.

The current working hierarchy is:

```text
Klinswork
    ↓
Project
    ↓
Child Project, where applicable
    ↓
System
    ↓
Resource
```

This hierarchy describes semantic relationships, not merely physical folder nesting.

A project may be represented by a repository directory, but its identity is not defined by that directory. A project may be renamed, moved, reorganized, or gain additional systems without becoming a different project.

---

## 3. Working Vocabulary

### Klinswork

The broader organizing environment for the user's projects, systems, resources, documentation, registries, applications, histories, and related tools.

Klinswork is not itself assumed to be a project.

### Project

A durable organized body of Klinswork work with its own identity, purpose, scope, objectives, history, documentation, systems, resources, and lifecycle.

A project may:

- contain systems;
- contain child projects;
- depend on shared resources;
- represent or support a real-world operational function;
- include historical implementations;
- continue to exist even when a particular application or system is replaced.

Project identity should remain stable across ordinary changes in name, folder location, implementation, and documentation structure.

### Parent Project

A project that organizes one or more related child projects under a broader purpose or domain.

A parent project is still a project. Parent-child relationships are recorded separately from project identity.

Current example:

```text
Operations
    ├── Inventory Management
    ├── Scheduling
    ├── Task Assignment and Tracking
    └── Employee Achievements
```

### Child Project

A project whose work is organized under a parent project while retaining its own project identity, scope, history, systems, and documentation.

### System

A coherent implemented mechanism, tool, service, application family, or technical system developed or maintained within a project.

A system may consist of multiple resources, including:

- deployed applications;
- Apps Script projects;
- data stores;
- datasets;
- interfaces;
- scripts;
- forms;
- viewers;
- configuration;
- documentation;
- deployment records.

A system is not identical to any one URL, file, workbook, deployment, or application resource.

Examples under the current working model include:

- **Inventory 3.0** as a system within the Inventory Management project;
- **Work Queue** as a system within the Task Assignment and Tracking project.

### Operational Function

A real-world function, process, or management activity represented, studied, supported, or organized by a project.

The operational function exists independently of any Klinswork system used to represent it.

For example, task assignment and tracking continues to exist as real work even when the Work Queue system is not used.

### Application

A user-facing software implementation or interface.

An application may be a resource within a larger system. Application is not required to be a separate hierarchy level between System and Resource.

For example, a deployed Work Queue web application can be registered as a Resource while the broader Work Queue implementation is identified as a System.

### Resource

A specific identifiable artifact, dataset, file, application, document, service, repository location, deployment, or other item used by a project or system.

Registered resources use stable `RES-###` identifiers in the Klinswork Resource Registry.

Resource identity is distinct from resource location.

### Shared Resource

A resource used by more than one project or system and therefore not assumed to belong exclusively to one of them.

Shared resources should be registered once and related to each project or system they support.

---

## 4. Project IDs

Klinswork projects use the namespace:

```text
PROJ-###
```

Examples:

```text
PROJ-001
PROJ-002
PROJ-003
```

Project numbers are identifiers, not classifications.

The number should not encode:

- project name;
- parent project;
- department;
- repository path;
- status;
- system type;
- implementation;
- operating environment.

These properties belong in project records and relationships.

### Project ID Rules

1. A Project ID identifies one project.
2. Project IDs are permanent once assigned.
3. Project IDs are not recycled.
4. Renaming a project does not normally change its Project ID.
5. Moving a project directory does not change its Project ID.
6. Changing a project's systems does not change its Project ID.
7. Changing a parent relationship does not automatically change its Project ID.
8. Historical names should be preserved as aliases or history rather than by issuing a new ID.
9. A Project ID should not be assigned until there is sufficient evidence that the entity is a durable project.
10. Provisional project candidates may remain unnumbered until their boundary is sufficiently clear.

---

## 5. Project Relationships

Project hierarchy is represented through relationships rather than encoded into IDs.

Example:

```text
Project ID: PROJ-004
Canonical Name: Task Assignment and Tracking
Parent Project ID: PROJ-001
```

The Project ID remains `PROJ-004` regardless of whether the project is later moved to another repository location or its parent relationship is revised.

This supports the same general principle already used by the Resource Registry:

```text
identity != location
```

and extends it to project structure:

```text
identity != hierarchy
```

Hierarchy is a relationship involving an identity. It is not the identity itself.

---

## 6. Current Working Project Structure

The following structure is the current working model and should be reconciled into canonical project records before being treated as a complete Project Registry.

```text
Klinswork
│
├── Operations
│   │
│   ├── Inventory Management
│   │   └── Inventory 3.0
│   │
│   ├── Scheduling
│   │   └── scheduling systems and implementations
│   │
│   ├── Task Assignment and Tracking
│   │   └── Work Queue
│   │
│   └── Employee Achievements
│       └── systems to be determined
│
└── Documentation
    └── documentation systems and infrastructure
```

In this model:

- **Operations** is a parent project.
- **Inventory Management** is a project under Operations.
- **Scheduling** is a project under Operations.
- **Task Assignment and Tracking** is a project under Operations.
- **Employee Achievements** is currently a project candidate whose exact boundary may remain provisional.
- **Documentation** is a separate cross-project Klinswork project.
- **Inventory 3.0** is a system under Inventory Management.
- **Work Queue** is a system under Task Assignment and Tracking.

This structure should be treated as the current architecture being formalized, not as evidence that historical files used the same terminology.

---

## 7. Historical and Bootstrap Terminology

Klinswork applications, folders, and documents were created before the current project model and stable project identifiers existed.

Historical material may therefore use terms differently.

Examples may include:

- calling an application a project;
- calling a project a system;
- using an application name as the name of a broader body of work;
- placing implementation material directly under a project root before a system layer existed;
- using repository paths that no longer match the current semantic model.

These historical records should normally be preserved.

They should not be silently rewritten as though the present architecture existed from the beginning.

Where practical, later canonical documentation should distinguish:

- historical terminology;
- transitional terminology;
- current canonical terminology.

---

## 8. Project Folder Contract

A mature project should normally have a canonical project directory containing a top-level `README.md`.

A typical structure may be:

```text
project-name/
├── README.md
├── systems/
├── implementation-plans/
├── history/
└── other project-specific material
```

Not every project needs every subdirectory.

Directory structure should follow actual documentation needs rather than a mandatory empty-folder template.

### Canonical Project README

The top-level project README should normally be authoritative for:

- Project ID;
- canonical project name;
- parent project relationship;
- project classification;
- project purpose;
- project scope and boundaries;
- represented operational or technical function;
- systems belonging to the project;
- important shared-resource relationships;
- current status;
- high-level history;
- navigation to deeper documentation;
- open determinations affecting the project.

The project README should remain high-level.

Detailed implementation behavior should be delegated to system documentation, live source, data documentation, implementation plans, historical records, and other lower-level artifacts.

---

## 9. System Documentation

Projects may contain one or more systems.

A system should have its own stable system identity when the system layer is formalized.

The planned identifier namespace is:

```text
SYS-###
```

The system layer should distinguish the identity of a system from the resources that currently implement it.

Example:

```text
PROJ-004 — Task Assignment and Tracking
    ↓
SYS-??? — Work Queue
    ↓
RES-002 — deployed Work Queue application
RES-003 — Work Queue data workbook
RES-012 — Work Queue Tasks dataset
RES-013 — Work Queue Employees dataset
...
```

A system may therefore survive:

- a new application deployment;
- replacement of a workbook;
- code reorganization;
- migration to another platform;
- changes in current URLs.

System ID rules should be formalized before permanent `SYS-###` identifiers are assigned.

---

## 10. Resource Registry Relationship

The Klinswork Resource Registry and the Project Registry serve different purposes.

```text
Project documentation
    = what the project means

Project Registry
    = stable project identity and high-level relationships

Resource Registry
    = stable resource identity, location, routing, and provenance

Manifest
    = what files or records physically exist and where
```

A project may depend on many Resource IDs.

A resource may also support more than one project.

Project membership should therefore not be inferred solely from:

- the resource's physical path;
- the application that consumes it;
- the document in which it appears;
- the project currently being discussed.

Relationships should be recorded explicitly.

---

## 11. Project Registry

A formal Project Registry is intended to provide the structured identity and relationship layer for Klinswork projects.

The Project Registry should be synthesized from reconciled project documentation rather than used to invent project structure prematurely.

The initial registry should remain compact.

Recommended minimum fields:

| Field | Purpose |
|---|---|
| `PROJECT ID` | Stable `PROJ-###` identity |
| `CANONICAL NAME` | Current canonical project name |
| `PARENT PROJECT ID` | Parent relationship when applicable |
| `PROJECT TYPE` | High-level project classification |
| `STATUS` | Current project state |
| `CANONICAL README` | Authoritative project orientation resource |
| `PRIMARY PURPOSE` | Concise description of the project |
| `LAST UPDATE` | Evidence-based project-record update state |

Additional relationships can be stored in linked records rather than expanding the Project Registry into a complete project database.

---

## 12. Project Types

Project type should describe the broad nature of the project without becoming part of its identifier.

Current useful categories may include:

- Parent Project
- Operational Project
- Documentation / Infrastructure Project
- Research / Investigation Project
- Personal Project
- Other classifications established later

This taxonomy remains subject to reconciliation as additional Klinswork projects are documented.

---

## 13. Status

Project status and system status should remain distinct.

Useful project states may include:

- Proposed
- Provisional
- Active
- Paused
- Completed
- Superseded
- Retired
- Historical

The existence of a functioning application does not automatically establish the status of the project that contains it.

Likewise, a project may remain active while one of its systems is replaced or retired.

---

## 14. Authority and Source of Truth

Different project facts may have different authorities.

### Project README

Authoritative for:

- project identity;
- purpose;
- scope;
- boundaries;
- parent relationship;
- systems;
- current high-level project relationships.

### Project Registry

Authoritative for:

- assigned Project ID;
- current canonical project name;
- current parent-project relationship;
- routing to the canonical project README.

### System Documentation

Authoritative for:

- system identity;
- system purpose;
- system boundaries;
- system resources;
- implementation architecture at the appropriate level.

### Live Source and Current Data

Authoritative for:

- what an implementation currently does;
- current schemas and records;
- current deployed behavior.

### Historical Work Updates and Records

Authoritative for:

- what was understood;
- what changed;
- what was tested;
- what was decided;
- what was considered current at a particular time.

Historical truth should not automatically be treated as current truth.

---

## 15. Repository Structure Versus Semantic Structure

Repository directories provide physical organization.

They do not by themselves establish project identity or semantic ownership.

For example:

```text
documents/work-update-catalog/projects/operations/
```

may serve as the physical documentation home for the Operations parent project and its child projects.

The fact that a resource appears inside that directory does not automatically mean that Operations exclusively owns it.

Similarly, bootstrap-era paths may remain in place even after the canonical project model changes.

Use:

```text
README
    = meaning and navigation

Project Registry
    = project identity and relationships

Resource Registry
    = resource identity and routing

manifest
    = physical discovery
```

---

## 16. Progressive Context Acquisition

A new work session should not load every artifact belonging to a project.

The preferred route is:

```text
Klinswork orientation
    ↓
projects/README.md
    ↓
relevant project README
    ↓
relevant system documentation
    ↓
specific resources, source, data, history, or evidence
```

The project documentation should identify what deeper context is relevant.

The Resource Registry should resolve known registered resources to their current locations.

Implementation accuracy should be verified against live implementation or current data when necessary.

---

## 17. Current Documentation Priorities

Before assigning the first permanent Project IDs, the project layer should complete the following normalization:

1. confirm the project vocabulary in the Housekeeping Operations architecture documentation;
2. reconcile Operations as the parent project;
3. reconcile Inventory Management as a child project;
4. reconcile Scheduling as a child project;
5. reconcile Task Assignment and Tracking as a child project;
6. determine whether Employee Achievements is ready for permanent project identity;
7. reconcile Documentation as a separate Klinswork project;
8. establish canonical project README locations;
9. preserve older project/system terminology as historical rather than silently rewriting it;
10. create the initial Project Registry from the reconciled project records.

---

## 18. Working Rule for Project Identification

Before assigning a new `PROJ-###` identifier, ask:

1. Is this a durable organized body of work rather than merely a file, application, dataset, or task?
2. Does it have a meaningful scope and purpose?
3. Can it reasonably contain systems or resources?
4. Does it have—or warrant—its own history and documentation?
5. Can its identity survive replacement of its current implementation?
6. Is its relationship to any parent project sufficiently understood?
7. Is there enough evidence to distinguish it from adjacent projects?
8. Is the proposed project identity consistent with current canonical vocabulary?

If the answer remains uncertain, preserve the candidate as provisional rather than assigning an ID prematurely.

---

## 19. Current Status

The Klinswork project layer is transitioning from bootstrap-era and application-centered organization into a stable project-centered architecture.

The Resource Registry already provides durable resource identity.

The next major documentation milestone is to establish durable project identity, beginning with the projects whose boundaries are now sufficiently understood.

The initial Project Registry should be created only after the current project READMEs and controlled vocabulary have been reconciled enough that the first `PROJ-###` assignments can reasonably be treated as permanent.
