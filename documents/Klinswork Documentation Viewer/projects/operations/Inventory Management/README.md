# Inventory Management

| Field | Current value |
|---|---|
| **Document role** | Project-local orientation and navigation |
| **Klinswork entity** | Inventory Management |
| **Entity type** | Project |
| **Parent Project** | Operations |
| **Primary operational environment** | Meadows Housekeeping |
| **Principal identified System** | Inventory 3.0 |
| **Project ID** | Pending formal Project Registry assignment |
| **Project boundary status** | Confirmed at the Project level; detailed relationship and System records are still being formalized |
| **Project-definition role** | First working exemplar for the Klinswork Project Definition architecture |
| **Last reconciled** | 2026-08-15 |

---

## 1. Purpose of this README

This README is the local orientation and navigation document for the **Inventory Management Project**.

Its job is to help a person, tool, or future work session enter this Project directory and quickly determine:

- what Project this directory concerns;
- what the Project is responsible for at a high level;
- which records should be consulted for different kinds of facts;
- which System is presently identified within the Project;
- where Project-local documentation belongs;
- how to resume work without treating repository location as identity;
- what parts of the Project Definition structure are complete, provisional, or still missing.

This README is **not** intended to become the canonical authority for every Inventory Management fact.

The governing principle is:

> **Use the README for orientation. Follow it to the record that owns the fact you need.**

---

## 2. Project identity

**Inventory Management** is a Klinswork **Project** concerned with the operational function of managing inventory.

The Project is currently modeled as a child Project of **Operations** and is primarily applied in the **Meadows Housekeeping** operational environment.

Its principal identified System is:

```text
Inventory Management
        ↓
    Inventory 3.0
```

Inventory Management and Inventory 3.0 are not interchangeable names.

```text
Inventory Management
    = Project

Inventory 3.0
    = System
```

The Project represents the durable body of work, responsibility, records, rules, history, and operational meaning associated with inventory management.

Inventory 3.0 is the principal currently identified implementation System used to perform that work.

A Project may survive changes to:

- its name;
- its repository directory;
- its parent relationship;
- its principal System;
- its application implementation;
- its spreadsheet or datastore;
- its deployment URL;
- its lifecycle state.

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

A permanent `PROJ-###` identifier has **not yet been assigned**. Do not invent one.

---

## 3. Operational purpose

The Inventory Management Project exists to preserve and improve reliable knowledge and control of housekeeping inventory.

At the Project level, the concern is not merely an application screen or spreadsheet. The concern is the operational function itself:

```text
physical supplies
        ↓
identified products
        ↓
identified locations
        ↓
quantity / state
        ↓
inventory events
        ↓
history and verification
        ↓
operational decisions
```

The Project may include work concerning:

- product identity and inventory units;
- storage and operational locations;
- current inventory quantities;
- opening balances;
- receiving inventory;
- recording use or depletion;
- corrections based on physical counts;
- transfers among locations;
- inventory-event history;
- verification and reconciliation;
- SDS relationships and access where relevant to managed products;
- inventory-oriented reporting;
- administrative tools;
- data integrity;
- testing;
- migration from earlier inventory implementations;
- documentation of the inventory-management function and its Systems.

This list describes the present working scope. It is not a substitute for the eventual Project Summary or formal relationship records.

---

## 4. Project boundaries

Inventory Management should remain distinct from neighboring Operations Projects even when they exchange data or trigger one another.

### Inventory Management owns or represents

At the present working level, Inventory Management concerns:

- the inventory-management operational function;
- inventory state;
- inventory events;
- product/location quantity relationships;
- inventory corrections and movements;
- inventory-specific history and verification;
- Systems used to implement inventory management.

### Inventory Management does not become

**Scheduling** merely because people use inventory on a schedule.

**Task Assignment and Tracking** merely because a task may cause inventory to be used, replenished, moved, or checked.

**Documentation** merely because Inventory Management has READMEs, summaries, sidecars, implementation plans, Viewer records, and publication products.

**Meadows Housekeeping** itself. Meadows Housekeeping is an operational environment in which the Project is used.

### Example integration boundary

A task may produce an inventory effect without merging the Projects:

```text
Task Assignment and Tracking
        ↓
task / completion event
        ↓
inventory-related request or effect
        ↓
Inventory Management
        ↓
inventory state / event
```

The task relationship belongs to Task Assignment and Tracking.

The resulting inventory-state effect belongs to Inventory Management.

Formal cross-entity relationships should eventually be represented by the appropriate relationship authority rather than being treated as intrinsic Project identity.

---

## 5. Authority map

Different files and registries answer different questions.

### `project-identity.json` — planned

Intended role:

- canonical Entity Record for stable Inventory Management Project identity facts;
- instantiated from the future Project Identity Record Profile;
- independent of mutable directory, hierarchy, System, and Resource relationships.

Current status:

```text
NOT YET CREATED
```

The Project Identity profile must be defined before this file is instantiated.

### `README.md` — this file

Role:

- orientation;
- navigation;
- explanation of the local documentation structure;
- reading order;
- authority routing;
- high-level Project context;
- Project Definition exemplar guidance.

This README should not silently absorb authority assigned to other records.

### `summaries/project-summary.md` — planned

Intended role:

- authoritative human-readable Project explanation;
- purpose and scope;
- boundary narrative;
- present interpretation;
- history;
- current state;
- important relationships;
- unresolved Project questions;
- explanatory Project context.

Current status:

```text
NOT YET CREATED
```

### `sidecars/project-summary-sidecar.json` — planned

Intended role:

- machine-readable structured companion to `summaries/project-summary.md`;
- structured interpretation of the human-readable Project Summary;
- Viewer/discovery metadata appropriate to its Record Profile.

It is **not** the Project Identity Entity Record.

Current status:

```text
NOT YET CREATED
```

### `systems/Inventory 3.0/`

Role:

- documentation local to the Inventory 3.0 System;
- System-level summaries and sidecars;
- later, a System Identity Entity Record when that profile is formally designed.

System documentation should describe the System without redefining the Inventory Management Project.

### `implementation-plans/`

Role:

- bounded plans for a defined body of intended work;
- implementation sequencing;
- dependencies;
- planned tests;
- acceptance criteria;
- risks;
- desired transition state.

An implementation plan describes intended work. It does not prove that the work occurred.

### Project Registry — planned/formalizing

Intended role:

- global registered Project identity/index/routing;
- allocation and lookup of stable `PROJ-###` identities when the process is ready.

The Project Registry and local Project Identity Entity Record must ultimately have a defined agreement/conflict rule. Until that authority model is finalized, no permanent Project ID should be invented here.

### Resource Registry

Role:

- registered Resource identity;
- current location;
- routing metadata;
- information about how to obtain or refresh a Resource.

A changing URL, path, deployment, workbook, script, or application location belongs in Resource resolution rather than being treated as Project identity.

### Relationship authority — planned

Intended role:

- parent/child Project relationships;
- Project/System relationships;
- Project/Resource relationships;
- operational-environment relationships;
- integrations;
- dependencies;
- other cross-entity facts.

### Activity Registry

Role:

- recorded change and provenance events represented there.

### Live implementation sources

Where a claim concerns what current software actually does, verify that claim against the current implementation and its authoritative data sources rather than relying only on a historical summary.

---

## 6. Current Project directory

Current Project root:

```text
documentation/
└── documents/
    └── Klinswork Documentation Viewer/
        └── projects/
            └── operations/
                └── Inventory Management/
```

Current/near-term local structure:

```text
Inventory Management/
├── README.md                         ← this file
├── implementation-plans/
│   ├── implementation-plan.md
│   └── README.md
├── sidecars/
│   └── project-summary-sidecar.json ← planned
├── summaries/
│   └── project-summary.md           ← planned
└── systems/
    └── Inventory 3.0/
        ├── README.md                 ← planned
        ├── sidecars/
        │   └── system-summary-sidecar.json
        └── summaries/
            └── system-summary.md
```

After the Project Identity Profile is completed, the intended structure becomes:

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
    ├── implementation-plan.md
    └── README.md
```

This tree is a **navigation and locality convention**.

It does not create Project identity merely by existing.

---

## 7. Locality rules

Project-local documents should normally remain inside this Project documentation space when they primarily concern Inventory Management.

Examples:

```text
Inventory Management/
├── summaries/
├── sidecars/
├── systems/
└── implementation-plans/
```

A human-readable source and its sidecar should normally occupy the same Documentation Space.

For example:

```text
summaries/project-summary.md
        ⇅
sidecars/project-summary-sidecar.json
```

The sidecar should explicitly resolve or declare its human-readable companion according to the applicable Record Profile.

The Viewer should discover the sidecar or other recognized record through registered Documentation Space discovery. The sidecar-to-document relationship is a separate resolution step.

Do not centralize a Project-local sidecar merely to make Viewer implementation easier.

---

## 8. Principal System: Inventory 3.0

Inventory 3.0 is the principal System presently identified within the Inventory Management Project.

Working relationship:

```text
Operations
    ↓
Inventory Management
    ↓
Inventory 3.0
```

The hierarchy displayed above is a relationship view, not an identity encoding.

Inventory 3.0 has historically been discussed at different abstraction levels, including as an application. Current Klinswork vocabulary distinguishes:

```text
Project
    Inventory Management

System
    Inventory 3.0

Resources
    deployed applications
    spreadsheets / data stores
    scripts
    datasets
    deployments
    documentation artifacts
    other implementation resources
```

Exact System identity fields and permanent `SYS-###` assignment are intentionally deferred until the Project model is proven and System boundaries are reconciled.

Do not create a permanent System ID merely to fill a blank.

---

## 9. Historical terminology

Earlier Klinswork material may use terminology that predates the present Project/System model.

Historical records may:

- call Inventory Management a System;
- use Inventory 3.0 primarily as an application name;
- organize the work around the application rather than the Project;
- hard-code older repository paths;
- describe relationships that were later refined;
- describe planned behavior that was not implemented;
- describe implementation state that was correct only at a particular time.

These records should generally remain intact as historical evidence.

Current canonical documentation should explain the newer interpretation without rewriting older records to make the architecture appear to have existed earlier than it did.

Use:

```text
historical record
    = evidence of what was understood at that time

current Project documentation
    = current interpretation
```

---

## 10. How to enter or resume work on this Project

A context-naive work session should load Inventory Management progressively rather than reading the entire repository indiscriminately.

Target sequence:

```text
Inventory Management work begins
        ↓
resolve Project identity
        ↓
read this README
        ↓
read current Project Summary
        ↓
interpret Project Summary sidecar where useful
        ↓
resolve Project relationships
        ↓
identify relevant System(s)
        ↓
read Inventory 3.0 orientation / summary when System work is involved
        ↓
resolve required Resources through the Resource Registry
        ↓
refresh physical state when needed
        ↓
load applicable workflow specification
        ↓
load current implementation plan and/or workflow-run state
        ↓
load relevant recent Activities / provenance
        ↓
read applicable Open Determinations
        ↓
retrieve deeper historical evidence only as needed
        ↓
perform work with explicit authority and uncertainty boundaries
```

### If current repository structure matters

Do not rely on this README as a permanently current directory listing.

Use the registered repository-tree generation procedure when available.

The intended pattern is:

```text
need current repository structure
        ↓
Resource Registry resolves tree-generation Resource/instructions
        ↓
run the current repository-tree generator
        ↓
read the newly generated tree
        ↓
use it as physical evidence
```

Physical evidence tells us where files are now.

It does not determine what those files mean.

### If current Viewer discovery state matters

Use the registered Klinswork Documentation Viewer source registry and manifest builder rather than assuming that all JSON under the repository is discoverable.

Conceptually:

```text
documentation-viewer-sources.json
        ↓
documentation-viewer-manifest.py
        ↓
generated Viewer manifest
        ↓
current registered discovery set
```

---

## 11. Project Definition exemplar role

Inventory Management is the first working exemplar for the emerging Klinswork Project Definition structure.

That means this directory is doing two jobs at present:

1. documenting the Inventory Management Project; and
2. testing whether the generic Project-definition architecture actually works on a real Project.

Those roles must not be confused.

The Project exists independently of its role as an architecture exemplar.

The exemplar work is successful only if the resulting structure can later be reused for other Projects without encoding Inventory Management-specific assumptions into the generic template.

Likely later candidates include:

- Scheduling;
- Task Assignment and Tracking;
- Documentation;
- other confirmed Klinswork Projects.

---

## 12. Project Definition completion path

The immediate Project-definition sequence is:

```text
Record Profile Library
        ↓
Project Identity Record Profile
        ↓
project-identity-template-1.0-draft.json
        ↓
Inventory Management/project-identity.json
        ↓
Inventory Management/project-summary.md
        ↓
Inventory Management/project-summary-sidecar.json
        ↓
Inventory 3.0 README + summary + sidecar
        ↓
registered discovery / manifest test
        ↓
Viewer interpretation test
        ↓
reconcile failures and ambiguities
        ↓
extract reusable Project Definition template
```

### Completion checks for this exemplar

- [ ] Project Identity Record Profile exists in the Record Profile Library.
- [ ] Project Identity template clearly separates identity from hierarchy, location, lifecycle, Systems, and Resources.
- [ ] `project-identity.json` exists for Inventory Management.
- [ ] No invented `PROJ-###` value is used.
- [ ] `summaries/project-summary.md` exists.
- [ ] `sidecars/project-summary-sidecar.json` exists.
- [ ] The Project Summary sidecar explicitly resolves its Markdown companion.
- [ ] `systems/Inventory 3.0/README.md` exists.
- [ ] `systems/Inventory 3.0/summaries/system-summary.md` exists.
- [ ] `systems/Inventory 3.0/sidecars/system-summary-sidecar.json` exists.
- [ ] Project and System documentation are distinguishable without relying only on folder names.
- [ ] The registered Projects Documentation Space discovers the intended records.
- [ ] Nested Common/Projects discovery does not create duplicate records.
- [ ] The generated Viewer manifest validates the Project records.
- [ ] Companion resolution behaves as intended.
- [ ] The Klinswork Documentation Viewer can present the records without changing their authority.
- [ ] Resource references resolve through the Resource Registry where applicable.
- [ ] Historical terminology remains visible rather than silently rewritten.
- [ ] Remaining ambiguities are recorded as Open Determinations rather than guessed.
- [ ] The working structure is reusable enough to derive a generic Project Definition template.

---

## 13. Relationship to the Record Profile Library

The Project-local files in this directory should be constructed according to recognized Record Profiles rather than invented independently.

The Record Profile Library lives under:

```text
documentation/
└── documents/
    └── Klinswork Documentation Viewer/
        └── Record Profile Library/
```

The library defines reusable construction and interpretation rules for recognized record families.

Relevant families for this Project will include:

```text
Record Profile Library
├── Entity Record Profiles
│   └── Project Identity
├── Sidecar Profiles
│   └── Project Summary / applicable summary-document profile
└── Authoring Templates
    └── summary Markdown authoring guidance
```

General sidecar/profile rules belong in the Record Profile Library README.

Profile-specific construction, interpretation, validation, compatibility, and `schemaRoadmap` rules belong in the applicable profile definition.

Project-specific future work does **not** belong in a profile's `schemaRoadmap`.

```text
schemaRoadmap
    → future evolution of the PROFILE

Project roadmap / implementation plan / Open Determination
    → future work on Inventory Management
```

---

## 14. Relationship to Documentation

Inventory Management is an Operations Project.

The documentation infrastructure used here belongs to the separate Klinswork **Documentation Project**.

Documentation provides mechanisms such as:

- Record Profiles;
- summaries and sidecars;
- Entity Records;
- manifests;
- catalogs;
- the Klinswork Documentation Viewer;
- workflow documentation;
- publication infrastructure;
- architecture change history;
- resource routing;
- context-loading conventions.

Using Documentation infrastructure does not make Inventory Management a Documentation Project.

Likewise, Documentation describing Inventory Management does not acquire authority over inventory state merely because it renders or indexes the records.

---

## 15. Downstream products

Project records may support downstream products without transferring source authority to those products.

Potential Inventory Management publication chains include:

```text
Project / System source documentation
        ↓
structured sidecars
        ↓
Viewer / catalogs
        ↓
HTML explanation / help / reference material
```

and, where inventory products overlap SDS documentation:

```text
product / SDS source records
        ↓
structured metadata / sidecars
        ↓
SDS information sheet
        ↓
product or chemical graphics
        ↓
Viewer / website / operational reference
```

A downstream HTML page or graphic is a presentation product unless another authority is explicitly assigned.

---

## 16. Implementation plans

The existing `implementation-plans/` directory is Project-local planning infrastructure.

Current tree evidence shows:

```text
implementation-plans/
├── implementation-plan.md
└── README.md
```

Use the implementation plan for bounded intended work.

Do not treat planned stages, planned tests, or acceptance criteria as proof of execution.

Conceptually:

```text
Workflow specification
    = reusable method

Implementation plan
    = intended bounded work

Workflow run / execution evidence
    = what actually occurred

Work update / summary
    = historical or explanatory account
```

When resuming an upgrade, load the applicable workflow first, then the current implementation plan and any available execution/run state.

---

## 17. Resource discipline

Inventory Management will use many concrete Resources.

Examples may include:

- applications;
- Google Sheets workbooks;
- Apps Script projects;
- deployments;
- product datasets;
- location datasets;
- inventory-event data;
- current-inventory data;
- SDS source documents;
- scripts;
- documentation files.

A Resource should normally be registered once and referenced by stable Resource ID when one has been formally assigned.

Do not create duplicate conceptual Resource identities merely because the same Resource participates in several Projects or Systems.

Do not copy mutable URLs into Project identity.

When a Resource moves:

```text
Resource identity remains stable
        ↓
Resource Registry location changes
        ↓
Project relationship remains resolvable
```

---

## 18. Known unresolved questions

The following are intentionally unresolved and should not be guessed merely to make the Project Definition look complete:

- permanent Inventory Management `PROJ-###` assignment;
- final Project Registry allocation procedure;
- exact conflict-resolution rule between Project Registry and local Project Identity Entity Record;
- final Project Identity profile fields and validation rules;
- formal Relationship Registry schema and predicates;
- exact formal representation of the Operations → Inventory Management parent relationship;
- final lifecycle vocabulary;
- permanent Inventory 3.0 `SYS-###` assignment;
- final System Identity profile;
- exact System boundary rules;
- final Viewer behavior for Entity Records;
- whether Project folders ultimately use one mandatory skeleton or a controlled flexible structure;
- which Resource Registry entries require reconciliation before automated Startup depends on them.

These questions should be resolved through the appropriate architecture process and recorded rather than filled by inference.

---

## 19. Rules for future editors

When modifying this directory:

1. Preserve Project identity independently of folder structure.
2. Do not assign IDs that have not been formally allocated.
3. Do not treat Inventory 3.0 as synonymous with the Inventory Management Project.
4. Keep human-readable narrative and structured sidecar roles distinct.
5. Keep Entity Records distinct from document sidecars.
6. Put Project-local documentation in the Project Documentation Space when appropriate.
7. Use the Resource Registry for current Resource location and routing.
8. Use relationship authority for cross-entity facts when formalized.
9. Preserve historical terminology when it is evidence of an earlier state.
10. Do not retroactively make old records appear to have used the current architecture.
11. Distinguish planned work from executed work.
12. Resolve current physical state with the appropriate generator when freshness matters.
13. Load workflow and implementation state before consequential upgrades.
14. Record unresolved architecture questions instead of guessing.
15. Treat Viewer, catalog, HTML, and other presentation products as downstream unless explicitly assigned authority.

---

## 20. Immediate next work

The next Project-definition work expected in this directory is:

1. finish the Record Profile Library sufficiently to support Entity Record Profiles;
2. define `project-identity-template-1.0-draft.json`;
3. instantiate `project-identity.json` for Inventory Management;
4. create `summaries/project-summary.md`;
5. create `sidecars/project-summary-sidecar.json`;
6. create the Inventory 3.0 local README, System Summary, and System Summary sidecar;
7. regenerate the Klinswork Documentation Viewer manifest;
8. verify Project-source discovery and companion resolution;
9. inspect the results through the Viewer;
10. reconcile what does not work;
11. derive the reusable Project Definition structure from the tested exemplar.

The governing objective is not to make this directory look complete.

The objective is to make it **understandable, authoritative by role, discoverable, resumable, and reusable as a tested Project-definition pattern**.
