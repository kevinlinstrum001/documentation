# Task Assignment and Tracking

| Field | Current value |
|---|---|
| **Document role** | Project-local orientation and navigation |
| **Klinswork entity** | Task Assignment and Tracking |
| **Entity type** | Project |
| **Parent Project** | Operations |
| **Primary operational environment** | Meadows Housekeeping |
| **Principal identified System** | Work Queue |
| **Project ID** | Unassigned — pending formal Project Registry assignment |
| **Project boundary status** | Confirmed at the Project level; Project/System definition package completed and validated through Stage 7; formal relationship records remain future work |
| **Project-definition role** | Second working exemplar for the Klinswork Project Definition architecture |
| **Reference exemplar** | Inventory Management → Inventory 3.0 |
| **Current Work Unit** | `WORK-0001` — active; closure work remains |
| **Last reconciled** | 2026-08-16 |

---

## 1. Purpose of this README

This README is the local orientation and navigation document for the **Task Assignment and Tracking Project**.

Its job is to help a person, tool, or future work session enter this Project directory and quickly determine:

- what Project this directory concerns;
- what operational function the Project represents;
- what the Project is responsible for at a high level;
- how the Project differs from the Work Queue System;
- which records should be consulted for different kinds of facts;
- where Project-local and System-local documentation belongs;
- where current-state and future-state Work Queue records belong;
- how neighboring Operations Projects interact without collapsing into one another;
- how to resume work without treating repository location as identity;
- what parts of the Project Definition structure are complete, deferred, or still open.

This README is **not** intended to become the canonical authority for every Task Assignment and Tracking fact.

The governing principle is:

> **Use the README for orientation. Follow it to the record that owns the fact you need.**

---

## 2. Project identity

**Task Assignment and Tracking** is a Klinswork **Project** concerned with the operational function of identifying, assigning, performing, completing, verifying, reporting, and preserving discrete work.

The Project is currently modeled as a child Project of **Operations** and is primarily applied in the **Meadows Housekeeping** operational environment.

Its principal identified System is:

```text
Task Assignment and Tracking
        ↓
     Work Queue
```

Task Assignment and Tracking and Work Queue are not interchangeable names.

```text
Task Assignment and Tracking
    = Project

Work Queue
    = System
```

The Project represents the durable operational undertaking.

Work Queue is the principal currently identified System used to structure and support that undertaking.

The operational function can exist even when Work Queue is not used. Work may also originate, be assigned, communicated, performed, or recorded through:

- supervisor instructions;
- verbal reports;
- paper lists;
- handwritten notes;
- institutional paperwork;
- email;
- photographs;
- direct inspection;
- digital forms;
- scheduling information;
- other Systems;
- later transcription or structured capture.

A Project may survive changes to:

- its name;
- repository directory;
- parent relationship;
- principal System;
- application implementation;
- spreadsheet or datastore;
- deployment URL;
- lifecycle state;
- operational environment.

Therefore:

```text
Project identity
    != name
    != directory
    != parent relationship
    != System
    != application
    != Resource
    != deployment
```

The local `project-identity.json` is the narrow Entity Record for the Project's stable intrinsic identity.

A permanent `PROJ-###` identifier has **not yet been assigned**. Do not invent one.

---

## 3. Operational purpose

The Task Assignment and Tracking Project exists to preserve and improve reliable operational knowledge of:

> **what work exists, who is responsible for it, what state it is in, what happened, and what resulted from it.**

At the Project level, the concern is not merely an application screen, task table, or spreadsheet.

The durable operational chain is approximately:

```text
work need / observation / request
        ↓
work identity
        ↓
review or acceptance where required
        ↓
assigned or available responsibility
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

The Project may include work concerning:

- work intake;
- task identity;
- pending work;
- supervisor review;
- assignment;
- unassigned or available work;
- employee responsibility;
- acceptance, claiming, rejection, release, and reassignment;
- task status and lifecycle;
- work performance;
- structured notes;
- evidence and images;
- completion;
- verification;
- recurring work and dailies where represented as discrete work;
- search and operational inquiry;
- history and audit;
- reporting and printable output;
- QR-originated work reporting;
- paperwork translation where structured work records are projected into human-facing forms;
- integration with Scheduling context;
- integration with Inventory Management effects;
- employee/profile relationships;
- administrative controls;
- data integrity;
- testing;
- documentation of the task-assignment-and-tracking function and its Systems.

This list describes the present working scope.

It is not a substitute for the Project Summary, formal relationship authority, or System-specific roadmap.

---

## 4. Project boundaries

Task Assignment and Tracking should remain distinct from neighboring Operations Projects even when they exchange data or trigger one another.

### Task Assignment and Tracking owns or represents

At the present working level, this Project concerns:

- the existence and identity of discrete work;
- work intake and review;
- responsibility for work;
- assignment and availability;
- task lifecycle and state;
- performance and completion;
- task-linked notes and evidence;
- verification or review of work;
- task-specific reporting and history;
- Systems used to implement task assignment and tracking;
- task-side relationships to downstream operational effects.

### Task Assignment and Tracking does not become

**Scheduling** merely because schedule information helps determine who is working, where, or when.

**Inventory Management** merely because a completed task may consume, replenish, transfer, check, or otherwise affect inventory.

**Employee Profile / personnel authority** merely because employee identity, role, capability, or profile information may be referenced by work records.

**Documentation** merely because the Project has READMEs, summaries, sidecars, catalogs, implementation plans, Viewer records, and publication products.

**Meadows Housekeeping** itself. Meadows Housekeeping is an operational environment in which the Project is used.

### Scheduling boundary

Scheduling concerns expected person/place/time relationships.

Task Assignment and Tracking concerns a discrete work responsibility.

```text
Scheduling
        ↓
expected person / place / time context
        ↓
Task Assignment and Tracking
        ↓
specific work responsibility / task
```

Schedule information may inform assignment without becoming the task record itself.

Likewise, actual task performance should not silently rewrite the schedule merely because work occurred somewhere different from the expected assignment.

### Inventory boundary

A task may produce an inventory effect without merging the Projects:

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

Task Assignment and Tracking owns the task and completion relationship.

Inventory Management owns the resulting inventory-state effect and inventory transaction integrity.

### Documentation boundary

Documentation supplies the infrastructure used to preserve, discover, structure, preview, and publish Project/System records.

Documentation does not become the owner of task truth merely because it documents the Project.

### Operational-environment boundary

Meadows Housekeeping supplies the current real-world people, work areas, constraints, routines, evidence, and processes from which much of this Project originated.

The operational environment is not the Project identity.

---

## 5. Paperwork and human-process parallel

Task Assignment and Tracking should preserve a **paperwork and human-process parallel**.

Klinswork Systems may structure, mirror, reconcile, route, analyze, or preserve work information, but the digital System should not be described as the sole source of the real operational process merely because it exists.

Operational information may originate through:

- paper work lists;
- institutional forms;
- handwritten notes;
- supervisor instructions;
- verbal reports;
- employee observations;
- photographs;
- email;
- meetings;
- inspections;
- QR reports;
- digital forms;
- schedule information;
- Work Queue actions;
- system-generated events;
- later transcription or batch conversion.

A person may participate in the real operational process without directly using Work Queue.

Digital participation, operational participation, supervisory authority, administrative authority, and documentation authority should not be inferred from one another.

---

## 6. Authority map

Different files, registries, and live sources answer different questions.

### `project-identity.json` — current

Role:

- narrow Entity Record for stable intrinsic Task Assignment and Tracking Project identity;
- instantiated from the Project Identity Record Profile;
- independent of mutable hierarchy, repository path, Systems, Resources, deployment, lifecycle state, and operational environment.

Current status:

```text
CREATED — 2026-08-16
PROJECT ID REMAINS UNASSIGNED
```

Use this record for intrinsic identity questions.

Do not use it as a substitute for:

- Project narrative;
- Project/System relationships;
- Resource routing;
- implementation state;
- operational history.

### `README.md` — current

Role:

- orientation;
- navigation;
- explanation of the local documentation structure;
- reading order;
- authority routing;
- high-level Project context;
- Project/System distinction;
- second-exemplar guidance.

This README should not silently absorb authority assigned to other records.

### `summaries/project-summary.md` — current

Role:

- authoritative human-readable Project explanation;
- purpose and operational function;
- scope;
- boundary narrative;
- present interpretation;
- current state;
- principal System;
- Resource context;
- history;
- important relationships in narrative form;
- unresolved Project questions;
- next work.

Current status:

```text
CREATED — 2026-08-16
```

### `sidecars/project-summary-sidecar.json` — current companion

Role:

- machine-readable structured companion to `summaries/project-summary.md`;
- structured interpretation of the human-readable Project Summary;
- Viewer/discovery metadata appropriate to its Record Profile.

It is **not** the Project Identity Entity Record.

Current status:

```text
CREATED — 2026-08-16
COMPANION RESOLUTION VALIDATED
```

### `systems/Work Queue/`

Role:

- documentation local to the Work Queue System;
- current-state System Summary;
- future-state System Roadmap;
- structured sidecars;
- later, a System Identity Entity Record if/when that profile is formally adopted.

System documentation should describe Work Queue without redefining the Task Assignment and Tracking Project.

### `systems/Work Queue/README.md` — current

Role:

- System-local orientation;
- local authority routing;
- current-state versus roadmap navigation;
- System/Project distinction;
- evidence and resume-work guidance.

### `systems/Work Queue/summaries/system-summary.md` — current

Role:

- current-state human-readable System explanation;
- Work Queue purpose;
- architecture;
- components;
- data;
- behavior;
- Resources;
- integrations;
- implementation history;
- current verified state;
- limitations;
- unresolved questions.

Current status:

```text
CREATED — 2026-08-16
```

The System Summary answers:

> **What is Work Queue now, based on evidence?**

### `systems/Work Queue/sidecars/system-summary-sidecar.json` — current

Role:

- structured companion to the Work Queue System Summary;
- Viewer/discovery representation of supported current-state System facts.

Current status:

```text
CREATED — 2026-08-16
COMPANION RESOLUTION VALIDATED
```

### `systems/Work Queue/summaries/work-queue-roadmap.md` — current

Role:

- durable planned direction for the Work Queue System;
- description of the intended mature System;
- capability areas and candidate Work Units;
- integrations;
- target-state design;
- maturity sequence;
- open product determinations.

Current status:

```text
CREATED — 2026-08-16
```

The roadmap answers:

> **What should Work Queue become?**

It should not be used as proof that planned capabilities already exist.

### `systems/Work Queue/sidecars/work-queue-roadmap-sidecar.json` — current

Role:

- structured companion to the Work Queue roadmap;
- machine-readable roadmap areas, baseline, target state, integrations, maturity sequence, and Work Unit policy;
- specialized System Roadmap Viewer preview source.

Current status:

```text
CREATED — 2026-08-16
COMPANION RESOLUTION VALIDATED
```

### `implementation-plans/implementation-plan-project-definition.md` — current governing plan

Role:

- bounded reconstructed-continuation implementation plan for `WORK-0001`;
- sequencing;
- dependencies;
- validation;
- acceptance criteria;
- closure conditions.

An implementation plan describes intended work.

It does not prove that the work occurred.

### `sidecars/implementation-plan-project-definition-sidecar.json` — current companion

Role:

- structured companion to the governing implementation plan;
- creation-time structured snapshot of the plan context.

The sidecar should not be rewritten merely to erase historical creation-time state.

### Project Registry — not yet formalized

Intended role:

- global registered Project identity/index/routing;
- formal allocation and lookup of stable `PROJ-###` identities.

Until that authority model is finalized, no permanent Project ID should be invented here.

### Resource Registry

Role:

- registered Resource identity;
- current location;
- routing metadata;
- information about how to obtain or refresh a Resource;
- Resource-level provenance where represented.

A changing URL, deployment, workbook, source file, script, dataset, or application location belongs in Resource resolution rather than Project identity.

Known Work Queue Resource relationships should be resolved through the Registry rather than copied here as permanent Project facts.

### Relationship authority — future/formalizing

Intended role:

- parent/child Project relationships;
- Project/System relationships;
- Project/Resource relationships;
- operational-environment relationships;
- integrations;
- dependencies;
- other cross-entity facts.

Relationship facts may be narrated here for orientation without becoming intrinsic Project identity.

### Work Unit Registry

Role:

- current-state authority for registered Work Units.

Current Project Definition work:

```text
WORK-0001
Task Assignment and Tracking — Initial Project Definition
```

### Work Unit Activities

Role:

- append-oriented material history for Work Units.

Current WORK-0001 history records activation, Project-definition completion, System-definition completion, validation, and Registry/architecture reconciliation checkpoints.

### Live implementation sources

Where a claim concerns what current Work Queue software actually does, verify that claim against:

- current source;
- current deployment;
- current datastore/schema;
- current registered Resources;
- fresh executable behavior or tests where needed.

Do not promote historical or planned behavior to current implementation truth without current evidence.

---

## 7. Current Project directory

Current Project root:

```text
documentation/
└── documents/
    └── Klinswork Documentation Viewer/
        └── projects/
            └── operations/
                └── Task Assignment and Tracking/
```

Current structure:

```text
Task Assignment and Tracking/
├── implementation-plans/
│   └── implementation-plan-project-definition.md
├── sidecars/
│   ├── implementation-plan-project-definition-sidecar.json
│   └── project-summary-sidecar.json
├── summaries/
│   └── project-summary.md
├── systems/
│   └── Work Queue/
│       ├── sidecars/
│       │   ├── system-summary-sidecar.json
│       │   └── work-queue-roadmap-sidecar.json
│       ├── summaries/
│       │   ├── system-summary.md
│       │   └── work-queue-roadmap.md
│       └── README.md
├── project-identity.json
└── README.md
```

This tree is a **navigation and locality convention**.

It does not create Project or System identity merely by existing.

---

## 8. Locality rules

Project-local documents should normally remain inside this Project documentation space when they primarily concern Task Assignment and Tracking.

Examples:

```text
Task Assignment and Tracking/
├── summaries/
├── sidecars/
├── systems/
└── implementation-plans/
```

System-local documents should normally remain beneath the relevant System.

For Work Queue:

```text
systems/Work Queue/
├── README.md
├── summaries/
└── sidecars/
```

A human-readable source and its sidecar should normally occupy the same Documentation Space.

For example:

```text
systems/Work Queue/summaries/system-summary.md
        ⇅
systems/Work Queue/sidecars/system-summary-sidecar.json
```

and:

```text
systems/Work Queue/summaries/work-queue-roadmap.md
        ⇅
systems/Work Queue/sidecars/work-queue-roadmap-sidecar.json
```

The sidecar should explicitly resolve or declare its human-readable companion according to the applicable Record Profile.

The Documentation Viewer may discover a sidecar, catalog entry, or Entity Record through source-aware discovery.

Discovery and semantic authority remain separate concerns.

Do not centralize a Project-local or System-local sidecar merely to make Viewer implementation easier.

Cross-System catalogs may live in the common catalog layer when their purpose is discovery across multiple Systems.

---

## 9. Principal System: Work Queue

Work Queue is the principal System presently identified within the Task Assignment and Tracking Project.

Working relationship:

```text
Operations
    ↓
Task Assignment and Tracking
    ↓
Work Queue
```

The hierarchy displayed above is a relationship view, not an identity encoding.

Current Klinswork vocabulary distinguishes:

```text
Project
    Task Assignment and Tracking

System
    Work Queue

Resources
    deployed applications
    Apps Script projects / services
    spreadsheets / data stores
    task datasets
    employee reference datasets
    location references
    documentation artifacts
    deployments
    other implementation resources
```

The Work Queue System is broader than any single deployment URL, application screen, spreadsheet, or source file.

Exact System identity fields and permanent `SYS-###` assignment are intentionally deferred until System Identity architecture and System boundaries are formally reconciled.

Do not create a permanent System ID merely to fill a blank.

---

## 10. Work Queue current-state versus roadmap authority

Work Queue has two distinct documentation questions that must remain separate.

### Current-state question

> **What does Work Queue actually consist of and do now?**

Primary authority:

```text
systems/Work Queue/summaries/system-summary.md
```

That Summary is grounded in:

- current Project definition;
- current Registry Resources;
- current datastore/schema evidence;
- current technical documentation;
- direct employee/location-source reconciliation;
- current implementation evidence where inspected;
- historical implementation evidence clearly labeled as historical.

### Future-state question

> **What should Work Queue become?**

Current authority:

```text
systems/Work Queue/summaries/work-queue-roadmap.md
```

The roadmap includes target capability areas such as:

- identity and role-aware access;
- employee, supervisor, and administrator dashboards;
- pending work and supervisor review;
- employee participation and assignment lifecycle;
- Calendar/Scheduling integration;
- Employee Profile integration;
- Inventory integration and transfer propagation;
- structured notes and image evidence;
- QR reporting;
- bounded OpenAI API validation;
- searchable history and audit;
- reporting and print output;
- paperwork translation;
- recurring work and dailies;
- Building Map and location intelligence;
- supervisor exception handling;
- notifications;
- administration, reliability, and data integrity.

These are **planned target capabilities** unless current evidence separately verifies that they already exist.

---

## 11. Integration model

Task Assignment and Tracking interacts with neighboring Projects and shared infrastructure while retaining separate authority.

### Scheduling → Work Queue

Scheduling may provide:

- expected employee;
- expected location;
- date;
- time;
- shift or coverage context.

Task Assignment and Tracking may use that context to inform work assignment.

The schedule remains the planned person/place/time relationship.

Work Queue records the specific work relationship and actual task history.

The shared Employees workbook currently also contains `Assignments` and `Weekly_Schedule` context. Their existence does not automatically make Scheduling part of Work Queue.

### Work Queue → Inventory Management

A Work Queue task may trigger inventory movement or another inventory effect.

Task Assignment and Tracking owns the task/completion relationship.

Inventory Management owns inventory-state correctness and inventory transaction integrity.

Current Work Queue evidence supports partial holder-event integration. Complete source-cart decrement, destination increment, and fully reconciled transfer propagation remain separate implementation work.

### Employee/personnel source ↔ Work Queue

Work Queue depends on stable employee identity for assignment and attribution.

Current Resource authority:

```text
RES-013
Work Queue Employees dataset
```

The current source is the separate `Employees` workbook, including:

```text
Employees
Assignments
Weekly_Schedule
```

Work Queue consumes shared personnel identity/context rather than becoming a competing personnel authority.

### Building Map / Locations ↔ Work Queue

Location references may support:

- task location;
- schedule context;
- QR reporting;
- inventory-holder relationships;
- search;
- reporting;
- map-based navigation.

Location identity should remain stable and shared rather than be duplicated independently inside each application.

### Documentation ↔ Task Assignment and Tracking

Documentation preserves Project/System records, roadmaps, summaries, sidecars, catalogs, manifests, workflows, plans, and history.

Documentation is infrastructure for describing the Project.

It is not the operational authority for task state.

---

## 12. Historical terminology and evidence

Earlier Klinswork material may use terminology that predates the present Project/System model.

Historical records may:

- call Work Queue a Project;
- organize the work around the application rather than Task Assignment and Tracking;
- use the earlier `Tasker` name;
- treat Work Queue primarily as an application;
- hard-code old Resource locations;
- describe prior deployments;
- describe planned behavior that was never implemented;
- describe implementation state that was correct only at a particular time.

These records should generally remain intact as historical evidence.

Current canonical documentation should explain the newer interpretation without rewriting historical records to make the architecture appear to have existed earlier than it did.

Use:

```text
historical record
    = evidence of what existed or was understood at that time

planning / design record
    = evidence of intended work

current implementation evidence
    = evidence of what the System does now

current Project documentation
    = current semantic interpretation
```

When the evidence classes disagree, preserve the disagreement until it is reconciled.

Do not silently convert:

```text
planned
```

into:

```text
implemented
```

---

## 13. How to enter or resume work on this Project

A context-naive work session should load Task Assignment and Tracking progressively rather than reading the entire Klinswork repository indiscriminately.

Preferred route:

```text
Task Assignment and Tracking work begins
        ↓
resolve Project identity
        ↓
read this README
        ↓
read current Project Summary
        ↓
resolve Project relationships where needed
        ↓
identify relevant System
        ↓
read Work Queue README
        ↓
choose current-state or future-state authority
        ↓
System Summary OR System Roadmap
        ↓
resolve required Resources through the Registry
        ↓
inspect current implementation evidence if behavior matters
        ↓
read historical work only when chronology / rationale matters
```

For roadmap work:

```text
Work Queue README
        ↓
work-queue-roadmap.md
        ↓
roadmap sidecar / Viewer
        ↓
bounded candidate capability
        ↓
Work Unit when sufficiently mature
        ↓
implementation plan when selected for execution
```

For current implementation work:

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

The Project README should help a session decide **what to load next**, not encourage indiscriminate context loading.

---

## 14. Relationship to Work Units

Roadmap areas and Work Units are related but not interchangeable.

The Work Queue roadmap may contain broad capability areas and candidate Work Units.

A stable Work Unit should be created only when the body of work is bounded enough to track as a recognizable outcome.

Conceptually:

```text
Task Assignment and Tracking     Project
        ↓
Work Queue                       System
        ↓
Roadmap Area                     durable planning category
        ↓
Work Unit                        bounded capability outcome
        ↓
Implementation tasks             execution detail
```

Do not invent `WORK-####` identifiers inside a roadmap document.

The Work Unit Registry assigns stable Work Unit identity.

A roadmap should remain useful even after individual Work Units are completed, split, deferred, or superseded.

Current Project-definition work is governed by:

```text
WORK-0001
Task Assignment and Tracking — Initial Project Definition
```

---

## 15. Current Project Definition state

As of 2026-08-16:

### Complete / validated through Stage 7

- Task Assignment and Tracking is recognized as a Project under Operations.
- Work Queue is recognized as the principal known System within the Project.
- the Project directory exists;
- `project-identity.json` has been instantiated;
- Project ID remains intentionally unassigned;
- Project README exists;
- Project Summary exists;
- Project Summary sidecar exists and companion resolution has been validated;
- governing Project-local implementation plan exists;
- implementation-plan sidecar exists;
- Work Queue System directory exists;
- Work Queue README exists;
- Work Queue current-state System Summary exists;
- Work Queue System Summary sidecar exists and companion resolution has been validated;
- Work Queue roadmap exists;
- Work Queue roadmap sidecar exists and companion resolution remains valid;
- the System Roadmap Catalog remains current;
- source-aware Viewer discovery has been validated;
- current-state versus future-state Viewer semantics have been validated;
- context-naive resume routing has been validated;
- Registry / Resource Activity / architecture effects have been reconciled through Stage 7;
- the RES-013 employee-data location correction has been preserved through Resource history.

### Remaining in `WORK-0001`

- reconcile this final Project README creation-time status language;
- finish the formal Work Implementation Session record;
- review the `WORK-0001` completion rule;
- close the formal session and Work Unit if the completion rule remains satisfied.

### Deliberately deferred

- permanent `PROJ-###` assignment;
- permanent `SYS-###` assignment;
- System Identity Entity Record;
- formal Relationship Registry implementation;
- broad Work Queue feature implementation;
- Work Queue datastore redesign;
- exhaustive historical-record normalization;
- universal reusable Project Definition template extraction unless separately selected;
- proposed rename from Task Assignment and Tracking to Task Management.

---

## 16. Current documentation questions

### What is this Project?

Read:

```text
README.md
summaries/project-summary.md
```

Use `project-identity.json` for narrow intrinsic identity.

### What is Work Queue?

Read:

```text
systems/Work Queue/README.md
systems/Work Queue/summaries/system-summary.md
```

### What should Work Queue become?

Read:

```text
systems/Work Queue/summaries/work-queue-roadmap.md
```

### How is the Project Summary structured for machines and the Viewer?

Read:

```text
sidecars/project-summary-sidecar.json
```

### How is the Work Queue System Summary structured for machines and the Viewer?

Read:

```text
systems/Work Queue/sidecars/system-summary-sidecar.json
```

### How is the Work Queue roadmap structured for machines and the Viewer?

Read:

```text
systems/Work Queue/sidecars/work-queue-roadmap-sidecar.json
```

### Where is the Work Queue application, datastore, dataset, employee source, location source, or technical manual now?

Use the:

```text
Klinswork Resource Registry
```

Do not rely on a repository README to preserve mutable Resource locations.

### What did a historical Work Queue version do?

Use:

- dated Work Updates;
- historical sidecars;
- historical screenshots;
- source snapshots;
- technical documentation;
- other dated evidence.

Preserve the evidence date.

### What is the current implementation doing?

Use current source, data, deployment, Registry records, and fresh verification.

### What work is planned?

Use the relevant roadmap and implementation plan.

### What work actually occurred during a bounded session?

Use the Work Implementation Session and resulting activity/history records.

---

## 17. Open determinations

The following remain unresolved or intentionally deferred:

- permanent Task Assignment and Tracking `PROJ-###`;
- permanent Work Queue `SYS-###`;
- final authority precedence between Project Identity and the future Project Registry;
- final System Identity Record Profile;
- whether a separate Application/Implementation entity should be formalized beneath Work Queue;
- formal parent/child and Project/System relationship records;
- complete Resource-to-System relationship modeling;
- exact Employee Profile System/Project architecture;
- final Calendar/System classification within Scheduling;
- final task state-machine vocabulary;
- exact division of recurring-work authority between Scheduling and Task Assignment and Tracking;
- exact QR/OpenAI validation architecture;
- image storage and retention rules;
- final paperwork-translation scope;
- final cross-System transaction contract for Work Queue ↔ Inventory Management.

Unresolved questions should remain visible rather than being filled with unsupported assumptions.

---

## 18. Project Definition sequence and current position

The second-exemplar sequence is now:

```text
Task Assignment and Tracking/
    project-identity.json                         ✓
        ↓
    README.md                                     ✓ current/reconciled
        ↓
    summaries/project-summary.md                  ✓
        ↓
    sidecars/project-summary-sidecar.json         ✓
        ↓
    implementation plan + companion               ✓
        ↓
    systems/Work Queue/README.md                   ✓
        ↓
    systems/Work Queue/summaries/system-summary.md ✓
        ↓
    system-summary-sidecar.json                   ✓
        ↓
    Work Queue roadmap + sidecar                  ✓
        ↓
    validate Viewer / discovery / companions      ✓
        ↓
    reconcile Registry / Activities / architecture effects ✓
        ↓
    update formal Work Implementation Session     ← next
        ↓
    review WORK-0001 completion rule
        ↓
    close session / WORK-0001 if satisfied
```

The Work Queue roadmap and roadmap sidecar remain separate future-state authorities.

They do not need to be recreated as part of current-state System definition work.

---

## 19. Governing rule

The local Project documentation should preserve the following distinction:

```text
project-identity.json
    = who / which Project this is

README.md
    = how to orient and navigate here

project-summary.md
    = what the Project means

Work Queue README
    = how to orient within the System

system-summary.md
    = what the Work Queue System is now

work-queue-roadmap.md
    = what the Work Queue System should become

implementation plan
    = bounded intended work

work session
    = execution record

Work Unit Registry
    = current bounded-work state

Work Unit Activities
    = material bounded-work history

Resource Registry
    = Resource identity and routing

relationship authority
    = cross-entity relationships

current source / data
    = current implementation truth where applicable
```

Do not collapse these authorities merely because they concern the same Project or System.

---

## 20. Current canonical interpretation

The current semantic model is:

```text
Klinswork
└── Operations                                      [Project]
    └── Task Assignment and Tracking                [Project]
        └── Work Queue                              [System]
            ├── application / deployment Resources
            ├── datastore / dataset Resources
            ├── employee and location relationships
            ├── inventory integration
            ├── technical documentation
            ├── current-state System documentation
            └── future-state roadmap
```

The durable Project concern is:

> **the lifecycle, responsibility, evidence, completion, verification, reporting, and preserved history of discrete operational work.**

The durable System concern is:

> **the coherent Work Queue implementation used to support that operational function.**

The roadmap concern is:

> **the intended mature capability of that System.**

Those distinctions should remain visible as the Project evolves.
