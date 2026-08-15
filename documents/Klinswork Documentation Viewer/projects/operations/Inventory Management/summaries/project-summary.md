# Inventory Management — Project Summary

| Field | Current value |
|---|---|
| **Document role** | Authoritative human-readable Project definition and current Project interpretation |
| **Project** | Inventory Management |
| **Entity type** | Project |
| **Project ID** | Unassigned — permanent `PROJ-###` allocation is intentionally pending |
| **Principal known System** | Inventory 3.0 |
| **Parent relationship** | Operations — current relationship model; not intrinsic Project identity |
| **Primary operational environment** | Meadows Housekeeping — current application context; not intrinsic Project identity |
| **Project-definition status** | First working Klinswork Project Definition exemplar |
| **Project Identity profile** | `project-identity / 1.0-draft` |
| **Companion sidecar** | `../sidecars/project-summary-sidecar.json` — pending |
| **Last reconciled** | 2026-08-15 |
| **Reconciliation timestamp** | 2026-08-15T12:55:00-06:00 |

---

## 1. Document purpose and authority

This document is the durable human-readable Project Summary for the **Inventory Management Project**.

Its purpose is to preserve the rich Project definition that does not belong in the narrow Project Identity Entity Record. It explains what Inventory Management is for, what operational function it represents, what falls inside and outside its scope, which System presently implements the function, what kinds of Resources participate, how the Project has been understood historically, where the Project stands now, what remains unresolved, and what work should happen next.

This document is intended to answer questions such as:

- Why does the Inventory Management Project exist?
- What operational responsibility does it represent?
- What is inside the Project boundary?
- What is outside the Project boundary?
- How is Inventory 3.0 related to the Project?
- Which kinds of Resources participate in the Project?
- What is authoritative for identity, relationships, Resources, implementation behavior, and history?
- What is known about the current state?
- Which questions remain open?
- What should a future work session load and do next?

This Project Summary is the **human-readable explanatory authority** for the Project's current purpose, scope, boundary narrative, current interpretation, historical framing, and unresolved Project-definition questions expressed here.

It is **not** the authority for every fact concerning Inventory Management.

The authority model is deliberately distributed:

```text
Project identity facts
    → project-identity.json

Project purpose / scope / boundaries / current interpretation
    → this Project Summary

Structured interpretation of this Project Summary
    → project-summary-sidecar.json

Project registration / ID allocation / global routing
    → Project Registry when formalized

Resource identity / current location / routing
    → Resource Registry

Cross-entity relationships
    → relationship authority when formalized

Inventory 3.0 System details
    → Inventory 3.0 System documentation

Current software behavior
    → live implementation sources

Current inventory data
    → authoritative current inventory datastore(s)

Historical change / provenance events
    → Activity Registry and preserved historical records

Bounded intended work
    → implementation plans

What actually occurred
    → execution evidence / workflow-run records / validated work records
```

A later sidecar may structure this document for discovery, routing, validation, and Viewer presentation, but that sidecar will remain a companion to this Markdown source rather than replacing it.

---

## 2. Project identity context

**Inventory Management** is a Klinswork **Project**.

The Project represents the durable body of operational responsibility, rules, records, history, decisions, Systems, and continuing work associated with managing inventory.

The Project Identity Entity Record is:

```text
../project-identity.json
```

That record currently establishes:

```text
entityType: project
canonicalName: Inventory Management
projectId: ""
projectIdAssignmentStatus: unassigned
```

The blank Project ID is deliberate.

A permanent `PROJ-###` value has not yet been formally allocated and must not be invented from the Project name, repository path, parent relationship, current System, historical numbering, or any other contextual clue.

The Project is intended to retain continuity across ordinary changes in:

- name;
- repository location;
- parent relationship;
- operational environment;
- principal System;
- application implementation;
- spreadsheet or datastore;
- Resource set;
- deployment;
- lifecycle state.

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

This Summary may explain those surrounding facts because they are necessary to understand the Project, but their appearance here does not convert them into intrinsic Project identity.

---

## 3. Purpose

The purpose of the Inventory Management Project is to preserve and improve **reliable knowledge and operational control of inventory**.

At the practical level, the Project exists so that inventory can be identified, located, counted, changed, traced, verified, and used to support operational decisions.

The Project is not merely an application-development effort.

It exists because the underlying operational function exists:

```text
physical supplies
        ↓
identified products
        ↓
identified locations
        ↓
known or reconciled quantity/state
        ↓
controlled inventory events
        ↓
preserved history
        ↓
verification
        ↓
operational decisions
```

An application may help perform this work. A spreadsheet may store part of the state. A script may apply transaction rules. A Viewer may explain the records. None of those artifacts individually *is* the Inventory Management Project.

The durable objective is to make inventory state understandable and dependable enough that the people and Systems using it can answer:

- What product is this?
- Where is it stored or assigned?
- How much is present?
- How did the current quantity arise?
- What changed?
- Why did it change?
- Was the change valid?
- Can the history be reconstructed?
- Can the physical count be reconciled with the recorded count?
- What SDS or product information is associated with the item where relevant?
- What should happen next operationally?

---

## 4. Operational function

The Project represents the operational function **Inventory Management**.

That function includes the controlled transition between physical inventory, recorded inventory state, and historical evidence.

A useful functional model is:

```text
IDENTIFY
    products
    units
    locations
        ↓
ESTABLISH STATE
    opening balances
    current quantities
        ↓
CHANGE STATE
    receive
    use
    transfer
    correct
        ↓
PRESERVE EVENT HISTORY
    event type
    affected product
    affected location
    quantity change
    timestamp / identifier
    reason where required
        ↓
VERIFY
    physical count
    recorded state
    event history
        ↓
USE INFORMATION
    replenishment
    availability
    accountability
    reporting
    operational planning
```

The Project therefore concerns more than storage of a number. It concerns the rules and evidence that make the number interpretable.

### 4.1 Core operational concerns

Current Project documentation identifies the following working concerns:

- product identity and inventory units;
- storage and operational locations;
- current inventory quantities;
- opening balances;
- receiving inventory;
- recording use or depletion;
- inventory corrections based on physical counts;
- transfers among locations;
- inventory-event history;
- verification and reconciliation;
- SDS relationships and access where relevant;
- inventory-oriented reporting;
- administrative tools;
- data integrity;
- testing;
- migration from earlier inventory implementations;
- documentation of the inventory-management function and its Systems.

These concerns define the present working Project scope. They should be refined as source evidence, live implementation state, and formal relationship records become more complete.

---

## 5. Scope

### 5.1 In scope

At the present level of reconciliation, Inventory Management includes work needed to define, implement, operate, verify, and preserve the inventory-management function.

This includes:

**Inventory state**

- representation of quantities;
- product/location state;
- current-state calculation or storage;
- opening-state establishment;
- prevention or detection of invalid state.

**Inventory events**

- receiving;
- use;
- transfers;
- corrections;
- other controlled changes that may later be added under an explicit event model;
- unique event identity where implemented;
- preserved event history.

**Inventory reference data**

- products;
- units;
- categories where used;
- locations;
- product-to-SDS or product-information relationships where applicable.

**Data integrity**

- validation;
- prevention of invalid quantities;
- duplicate-event prevention;
- controlled writes;
- reconciliation of current state against events and physical counts;
- preservation of historical evidence.

**Operational interfaces and tools**

- applications and interfaces used to perform inventory actions;
- administrative or reporting capabilities belonging to the inventory function;
- mobile or desktop interaction where supported by the System.

**Documentation and knowledge**

- Project documentation;
- System documentation;
- implementation plans;
- structured companions;
- preserved historical evidence;
- explanatory and downstream reference products.

### 5.2 Potentially related but not automatically in scope

Some work may touch Inventory Management without belonging to the Project itself.

Examples include:

- employee scheduling;
- assignment of work to employees;
- general employee records;
- general location governance outside the inventory relationship;
- general SDS-documentation infrastructure;
- general Klinswork documentation infrastructure;
- website or Viewer infrastructure not specific to Inventory Management;
- organization-wide communication systems.

A relationship to inventory does not automatically make another function part of the Inventory Management Project.

---

## 6. Project boundaries

The Project boundary is functional rather than application-based.

Inventory Management should remain distinguishable from neighboring Klinswork Projects even when they exchange information or trigger one another.

### 6.1 Scheduling

Inventory Management does not become **Scheduling** merely because inventory activity occurs at a particular time or because a scheduled employee performs it.

Scheduling concerns person/place/time relationships.

Inventory Management concerns inventory state and inventory-state change.

### 6.2 Task Assignment and Tracking

Inventory Management does not become **Task Assignment and Tracking** merely because a task causes inventory to be checked, moved, replenished, or consumed.

A task may produce an inventory effect:

```text
Task Assignment and Tracking
        ↓
task / completion
        ↓
inventory-related request or event
        ↓
Inventory Management
        ↓
inventory-state effect
```

The task and completion relationship belongs to Task Assignment and Tracking.

The resulting inventory-state effect belongs to Inventory Management.

### 6.3 Documentation

Inventory Management does not become the **Documentation Project** merely because it uses:

- Entity Records;
- READMEs;
- summaries;
- sidecars;
- implementation plans;
- manifests;
- catalogs;
- the Klinswork Documentation Viewer;
- publication infrastructure.

Documentation supplies infrastructure for describing and retrieving the Project.

The Project being documented remains Inventory Management.

### 6.4 Meadows Housekeeping

Inventory Management does not equal **Meadows Housekeeping**.

Meadows Housekeeping is the primary current operational environment in which this Project is being modeled and used.

The environment can change without creating a new Project identity.

### 6.5 Inventory 3.0

Inventory Management does not equal **Inventory 3.0**.

This distinction is fundamental:

```text
Inventory Management
    = Project

Inventory 3.0
    = System
```

The Project is the durable undertaking.

Inventory 3.0 is the principal currently identified System used to implement that undertaking.

---

## 7. Principal known System — Inventory 3.0

**Inventory 3.0** is the principal System presently identified within the Inventory Management Project.

The current conceptual relationship is:

```text
Operations
    ↓
Inventory Management
    ↓
Inventory 3.0
```

That diagram is a relationship view. It does not encode identity.

Inventory 3.0 should be understood as a coherent implementation System through which inventory-management behavior, data, interfaces, and supporting Resources can be organized.

Current Klinswork vocabulary distinguishes:

```text
Project
    Inventory Management

System
    Inventory 3.0

Resources
    applications
    data stores
    scripts
    datasets
    deployments
    documentation artifacts
    supporting files and services
```

### 7.1 What is known

Inventory 3.0 is the principal System currently associated with the Inventory Management Project.

Its documentation space already exists at:

```text
systems/
└── Inventory 3.0/
    ├── sidecars/
    └── summaries/
```

### 7.2 What is not yet formalized

The following remain intentionally unresolved:

- permanent `SYS-###` assignment;
- final System Identity Record Profile;
- exact Inventory 3.0 System identity fields;
- final System boundary;
- complete Resource membership/relationship map;
- complete current implementation verification;
- formal System Summary and companion sidecar.

System identity work is deferred until the Project model has been tested sufficiently to avoid carrying unresolved Project-design mistakes into the System layer.

---

## 8. Resources

Inventory Management uses concrete **Resources**, but Resources are not the Project itself.

Known Resource classes relevant to the Project include:

### 8.1 Applications

User-facing or administrative applications used to perform inventory work.

The current principal System is Inventory 3.0, but an application interface should still be distinguished from the System that contains or coordinates it.

### 8.2 Data stores

Potential or known data-store roles include:

- product data;
- location data;
- inventory-event history;
- current-inventory state;
- configuration or lookup data;
- administrative/reference tables.

Google Sheets workbooks have historically been a major implementation medium in Klinswork inventory work, but this Summary does not assign a specific workbook as authoritative without Registry or implementation evidence.

### 8.3 Scripts and services

Apps Script projects, supporting scripts, build tools, or services may implement inventory rules, reads, writes, validation, reporting, or deployment behavior.

Current behavior claims should be checked against live source rather than inferred from this Summary.

### 8.4 Deployments

A deployment URL is a mutable Resource location.

It must not be copied into Project identity as though the Project would cease to exist if the deployment changes.

### 8.5 Product and SDS resources

Inventory-managed products may relate to:

- SDS source documents;
- chemical-product structured records;
- SDS information sheets;
- related product graphics or reference material.

Those Resources may participate in both Inventory Management and Documentation/SDS workflows without being conceptually duplicated.

### 8.6 Documentation resources

This Project documentation space contains or is intended to contain:

```text
Inventory Management/
├── project-identity.json
├── README.md
├── summaries/
│   └── project-summary.md
├── sidecars/
│   └── project-summary-sidecar.json
├── systems/
│   └── Inventory 3.0/
└── implementation-plans/
```

### 8.7 Resource authority rule

A Resource should normally be registered once.

When a formal Resource ID exists, Project and System documentation should refer to the stable Resource identity rather than treating a path or URL as identity.

```text
Resource identity remains stable
        ↓
Resource location changes
        ↓
Resource Registry is updated
        ↓
Project/System relationship remains resolvable
```

### 8.8 Current limitation of this Summary

This Summary does **not** assert a complete list of Inventory Management `RES-###` identifiers.

The source material used for this Project Definition does not yet establish a fully reconciled Resource membership list. Exact Resource IDs, current URLs, workbook IDs, deployments, and routing instructions should be resolved through the Resource Registry and current implementation evidence rather than invented here.

---

## 9. Current state

The Project currently has two different kinds of state that must not be conflated:

1. **operational/implementation state** — what the inventory System and current data actually do now;
2. **Project-definition/documentation state** — how well the durable Project is formally defined and discoverable.

### 9.1 Operational / implementation state

This Project Summary does not claim to be a real-time verification of the Inventory 3.0 deployment or its inventory data.

Existing material establishes that Inventory 3.0 is the principal known System and that the Project concerns controlled inventory state and events. However, claims about current application behavior, deployed versions, live quantities, current schemas, or successful tests should be verified against:

- current implementation source;
- authoritative data stores;
- deployment evidence;
- current test evidence;
- applicable implementation-plan and workflow-run records.

Accordingly, the operational state should presently be treated as **partially documented but not comprehensively reverified by this Project Summary**.

### 9.2 Project-definition state

As of 2026-08-15, the Project-definition layer is substantially farther along.

Completed in the current exemplar sequence:

```text
Record Profile Library                         established
Record Profile Registry                        broadened to multiple record families
Project Identity Record Profile                created as 1.0-draft
project-identity-template-1.0-draft.json        created
Inventory Management/project-identity.json     instantiated
Inventory Management/README.md                 reconciled
Inventory Management/project-summary.md        created by this step
```

Still pending:

```text
sidecars/project-summary-sidecar.json
systems/Inventory 3.0/README.md
systems/Inventory 3.0/summaries/system-summary.md
systems/Inventory 3.0/sidecars/system-summary-sidecar.json
Project-space discovery test
Entity Record discovery behavior
manifest regeneration / validation
Viewer interpretation test
reconciliation of failures
generic Project Definition extraction
```

### 9.3 Project ID state

```text
projectId: ""
projectIdAssignmentStatus: unassigned
```

This is not an omission to be casually fixed.

It is an explicit representation of the current architecture state.

---

## 10. Current records and authority routing

The Project-local record set now begins to form a deliberate layered structure.

### 10.1 `project-identity.json`

**Status:** created.

**Role:** narrow Project Identity Entity Record.

Use it for stable intrinsic Project identity facts assigned to the Project Identity profile.

Do not use it as the authority for:

- Project purpose narrative;
- hierarchy;
- Resources;
- Systems;
- operational environment;
- repository path;
- lifecycle;
- implementation behavior;
- current inventory.

### 10.2 `README.md`

**Status:** created and reconciled.

**Role:** local orientation, navigation, authority routing, reading order, and resume-work guidance.

Use it to enter the Project documentation space and determine what to read next.

### 10.3 `summaries/project-summary.md`

**Status:** this document.

**Role:** rich human-readable Project definition and current interpretation.

### 10.4 `sidecars/project-summary-sidecar.json`

**Status:** pending.

**Role:** future machine-readable companion to this Markdown source.

It must remain a **sidecar**, not an Entity Record.

### 10.5 `systems/Inventory 3.0/`

**Status:** scaffold exists; System-level documents pending.

**Role:** documentation local to the principal known System.

### 10.6 `implementation-plans/`

**Status:** directory and planning records exist in the Project scaffold.

**Role:** bounded intended work.

An implementation plan is not proof of execution.

---

## 11. History and architectural evolution

The Project has a history that predates the current Project/System vocabulary.

This section distinguishes what is currently established from what still requires historical reconciliation.

### 11.1 Earlier application-centered understanding

Earlier Klinswork material may:

- call Inventory Management a **System**;
- use Inventory 3.0 primarily as an **application** name;
- organize documentation around the application rather than the durable Project;
- use repository paths that have since changed;
- describe planned capabilities that were not yet implemented;
- describe implementation state that was accurate only at the time.

Those records are historical evidence.

They should not be rewritten merely to make the present ontology appear older than it is.

### 11.2 Separation of Project and System

The current architecture recognizes a more durable distinction:

```text
Inventory Management
    = Project / operational undertaking

Inventory 3.0
    = principal System implementing the undertaking
```

This distinction prevents the Project from disappearing conceptually when the implementation changes.

### 11.3 Project-definition bootstrap

During the current Documentation-architecture work, Klinswork established a broader Record Profile model capable of distinguishing:

```text
document-sidecar
entity-record
authoring-template
```

The Sidecar Profile Registry was broadened into a draft **Record Profile Registry** so Project Identity could be represented as an Entity Record rather than being forced into a sidecar model.

A `project-identity-template-1.0-draft.json` profile was then created.

Inventory Management became the first real Project used to instantiate that profile.

### 11.4 First Project Identity exemplar

`Inventory Management/project-identity.json` was created with:

- `entityType: project`;
- `canonicalName: Inventory Management`;
- blank `projectId`;
- `projectIdAssignmentStatus: unassigned`;
- explicit identity continuity;
- evidence/provenance;
- Project Registry coordination kept pending;
- mutable relationships excluded from intrinsic identity.

This is an important architectural milestone because the Project is now represented directly without depending on its directory, parent, System, Resource set, or deployment.

### 11.5 Current Project Summary step

This document is the next layer.

It deliberately carries the richer material that was excluded from Project Identity:

- purpose;
- function;
- scope;
- boundaries;
- current interpretation;
- System context;
- Resource context;
- history;
- unresolved questions;
- next work.

### 11.6 Historical work still to reconcile

This Summary does not yet claim to be a complete operational chronology of Inventory Management or Inventory 3.0.

A later historical reconciliation should inspect:

- prior Inventory 2.x / Inventory 3.0 design records;
- implementation roadmaps;
- work updates;
- application screenshots;
- source code;
- workbook/schema history;
- deployment history;
- migration records;
- test evidence;
- Activities;
- earlier terminology.

The purpose of that future work would be to improve historical understanding without retroactively changing what older records originally meant.

---

## 12. Relationship to Operations

Inventory Management is currently modeled as a child Project of **Operations**.

That relationship is important for navigation and organizational understanding, but it is not intrinsic Project identity.

The Project ID should therefore not encode hierarchy.

Preferred future model:

```text
Project identity:
    PROJ-###  Inventory Management

Relationship:
    Inventory Management --parent_project--> Operations
```

not:

```text
PROJ-001-004
```

where the identifier itself would break if the hierarchy changes.

The exact formal relationship record and predicate remain pending the Relationship Registry design.

---

## 13. Relationship to Meadows Housekeeping

**Meadows Housekeeping** is the primary operational environment currently associated with this Project.

That environment provides much of the practical context in which products, supplies, locations, inventory actions, and housekeeping operations are understood.

However:

```text
Inventory Management Project
    != Meadows Housekeeping environment
```

The Project may conceptually survive movement to another operational environment.

The exact future representation of operational-environment relationships remains part of the broader relationship architecture.

---

## 14. Relationship to Documentation

The Inventory Management Project uses the infrastructure of the separate Klinswork **Documentation Project**.

Documentation supplies the mechanisms used here for:

- Record Profiles;
- Entity Records;
- Markdown summaries;
- sidecars;
- registries;
- Documentation Spaces;
- manifests;
- catalogs;
- the Klinswork Documentation Viewer;
- workflows;
- publication;
- context routing;
- provenance and architecture change control.

This support relationship does not transfer operational authority.

For example:

```text
Documentation Viewer displays inventory record
        ≠
Documentation Viewer becomes authority for inventory state
```

Likewise, this Project Summary may explain an Inventory 3.0 Resource without becoming the authority for what the live Resource currently does.

---

## 15. Implementation plans

Project-local implementation plans live under:

```text
implementation-plans/
```

The current scaffold contains:

```text
implementation-plans/
├── implementation-plan.md
└── README.md
```

The semantic distinction is:

```text
Workflow specification
    = reusable method

Implementation plan
    = intended bounded work

Workflow run / execution evidence
    = what actually occurred

Work update / historical summary
    = explanatory account of work/state
```

A future session resuming implementation work should not infer execution from a plan.

It should load:

1. the applicable workflow specification;
2. the current implementation plan;
3. available workflow-run or execution evidence;
4. current implementation sources;
5. relevant Activities;
6. current Open Determinations.

---

## 16. How to resume work

A context-naive work session should load Project context progressively.

Recommended sequence:

```text
Inventory Management work begins
        ↓
read project-identity.json
        ↓
read README.md
        ↓
read summaries/project-summary.md
        ↓
read project-summary sidecar when available/useful
        ↓
resolve formal Project relationships
        ↓
determine whether Inventory 3.0 System context is needed
        ↓
read Inventory 3.0 README / System Summary
        ↓
resolve required Resources through Resource Registry
        ↓
refresh physical repository state if needed
        ↓
load applicable workflow
        ↓
load implementation plan / workflow-run state
        ↓
load recent Activities / provenance
        ↓
load relevant Open Determinations
        ↓
retrieve historical evidence only as needed
        ↓
perform work with explicit authority boundaries
```

### 16.1 If repository structure matters

Do not treat a copied tree in this Summary as permanently current.

Regenerate physical repository evidence using the registered repository-tree procedure when freshness matters.

### 16.2 If documentation discovery matters

Use the current Klinswork Documentation Viewer source registry and manifest builder.

Do not assume that all JSON files are automatically discovered.

This is especially important for `project-identity.json`, because Entity Records must be recognized as Entity Records rather than mislabeled as sidecars merely to fit existing discovery logic.

---

## 17. Project Definition exemplar role

Inventory Management is currently the first working exemplar for the Klinswork **Project Definition** architecture.

The exemplar is intended to answer a practical question:

> Can Klinswork define a real Project in a way that is durable, locally understandable, machine-discoverable, authority-aware, resumable, and reusable for other Projects?

The Project Definition package being tested is approximately:

```text
Inventory Management/
├── project-identity.json
├── README.md
├── summaries/
│   └── project-summary.md
├── sidecars/
│   └── project-summary-sidecar.json
├── systems/
│   └── Inventory 3.0/
│       ├── README.md
│       ├── summaries/
│       │   └── system-summary.md
│       └── sidecars/
│           └── system-summary-sidecar.json
└── implementation-plans/
```

The directory itself is not the definition.

The definition emerges from the coordinated authority roles of the records.

The exemplar should not be considered successful merely because every expected filename exists.

It should be considered successful when a future person or tool can determine:

- what Project this is;
- what its durable purpose is;
- what its scope and boundaries are;
- where intrinsic identity lives;
- where narrative lives;
- where relationships live;
- where Resource routing lives;
- which System implements the Project;
- where current implementation truth should be verified;
- what happened historically;
- what remains unresolved;
- what work should happen next.

---

## 18. Unresolved questions

The following questions remain intentionally unresolved.

### 18.1 Project identity and registry

- What permanent `PROJ-###` value will be allocated to Inventory Management?
- Which authority formally allocates Project IDs?
- What exact precedence/reconciliation rule applies if the Project Registry and `project-identity.json` disagree?
- Does the Project Identity Entity Record need a separate stable record ID in addition to the Project ID?
- What remaining changes are required before the Project Identity profile moves from `1.0-draft` to `1.0`?

### 18.2 Relationships

- What is the final Relationship Registry schema?
- What controlled predicate represents the Operations → Inventory Management relationship?
- How should Project → System relationships be formalized?
- How should Project → Resource relationships be formalized?
- How should operational-environment relationships be represented?
- Which relationships should be current-state records versus historical Activities?

### 18.3 System identity

- What permanent `SYS-###` value, if any, will be allocated to Inventory 3.0?
- What fields belong in the System Identity profile?
- What is the final Inventory 3.0 System boundary?
- Which implementation artifacts are Resources of Inventory 3.0 versus shared Resources?

### 18.4 Resource reconciliation

- Which current Inventory Management Resources already have valid `RES-###` identities?
- Which Resource Registry paths or URLs are stale?
- Which Resource entries are authoritative for current Inventory 3.0 source, data, deployment, and documentation?
- Which shared Resources should be related rather than duplicated?

### 18.5 Viewer and discovery

- How should the Klinswork Documentation Viewer discover Entity Records?
- Should Project-space discovery expand beyond the current sidecar-oriented mode?
- What Viewer preview should Project Identity use?
- How should the Viewer present identity, summary, sidecar, System, and Resource relationships without collapsing their authority roles?
- What validation rules should reject an Entity Record accidentally placed or interpreted as a sidecar?

### 18.6 Project template

- Should every Project use the same mandatory folder skeleton?
- Which Project-definition elements are required versus optional?
- Which parts of this Inventory Management exemplar are genuinely generic?
- What should the final reusable Project Definition template contain?

### 18.7 Operational history and current implementation

- What is the fully reconciled chronology of Inventory Management / Inventory 3.0?
- Which planned capabilities were actually implemented?
- Which tests were actually run?
- What is the current deployment state?
- Which current data stores are authoritative?
- Which earlier Inventory versions or records should be explicitly linked as predecessors?

These questions should remain visible until evidence or a formal architecture decision resolves them.

---

## 19. Next work

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
- identify Inventory Management as the subject Project without replacing `project-identity.json`;
- expose purpose, scope, boundaries, System context, Resources, history, current state, and unresolved questions for discovery;
- support the Klinswork Documentation Viewer;
- avoid inventing Project, System, Relationship, or Resource IDs.

### Subsequent work

After the Project Summary sidecar:

1. create `systems/Inventory 3.0/README.md`;
2. create `systems/Inventory 3.0/summaries/system-summary.md`;
3. create `systems/Inventory 3.0/sidecars/system-summary-sidecar.json`;
4. regenerate the Klinswork Documentation Viewer manifest;
5. verify Project-space discovery;
6. verify Project Summary companion resolution;
7. verify that `project-identity.json` is recognized as an Entity Record rather than a sidecar;
8. inspect the records in the Viewer;
9. reconcile profile, path, manifest, and Viewer failures;
10. resolve Resource Registry entries needed for reliable Project/System context loading;
11. test a context-naive resume sequence using Project Identity → README → Project Summary → System → Resources;
12. revise the Project Identity profile if the exemplar reveals a real schema defect;
13. only after the Project model is proven, begin formal System Identity design;
14. derive the reusable **Project Definition template** from the tested Inventory Management exemplar.

---

## 20. Resulting Project state

Inventory Management now has the beginnings of a durable Project-definition layer independent of its current implementation.

The important conceptual result is:

```text
Inventory Management
        │
        ├── identity
        │     → project-identity.json
        │
        ├── local orientation
        │     → README.md
        │
        ├── rich Project definition
        │     → summaries/project-summary.md
        │
        ├── machine-readable summary interpretation
        │     → sidecars/project-summary-sidecar.json [next]
        │
        ├── principal System
        │     → systems/Inventory 3.0/
        │
        ├── bounded planned work
        │     → implementation-plans/
        │
        ├── Resource routing
        │     → Resource Registry
        │
        ├── cross-entity relationships
        │     → future/formal relationship authority
        │
        └── history / provenance
              → Activities + preserved historical records
```

This structure allows the Project to remain intelligible even if Inventory 3.0 is replaced, the repository is reorganized, a workbook changes, a deployment URL changes, or the Project's organizational relationships change.

That is the central purpose of the Project Definition architecture.

---

## 21. Source and interpretation notes

This Project Summary was reconciled from the current Inventory Management Project-definition material available during the 2026-08-15 architecture session, principally:

- `../project-identity.json`;
- `../README.md`;
- the current Inventory Management repository scaffold;
- the current Record Profile / Project Identity architecture;
- preserved documentation describing the distinction among Project, System, Resource, sidecar, Entity Record, implementation plan, and historical evidence.

This Summary deliberately does **not** claim:

- a permanent Project ID;
- a permanent System ID;
- a complete Resource-ID membership list;
- a complete operational chronology;
- a verified current deployment;
- verified current inventory quantities;
- completed tests without execution evidence;
- finalized relationship records;
- finalized Viewer Entity Record support.

Where those facts matter, the next work session should resolve them from the authority that actually owns them rather than filling the gaps from inference.
