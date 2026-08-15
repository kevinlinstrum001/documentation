Yes. I think we should do a **small architecture-normalization pass first**, then start assigning IDs. We are close enough that this should be finite rather than another open-ended documentation exercise.

One important observation first: according to the current repository tree, there is **no `projects/README.md` yet**. We have `projects/operations/README.md`, plus the Inventory Management implementation-plan material.  So I would create a new:

```text
documents/work-update-catalog/projects/README.md
```

and make that the authority for **how Klinswork projects are organized and identified**.

## 1. What the new `projects/README.md` should establish

Its job should be narrow. It should not describe every project. It should define the project layer itself.

I would give it these responsibilities:

### A. Define the project hierarchy

Our working structure is now:

```text
Klinswork
│
├── Operations
│   │
│   ├── Inventory Management
│   │   └── Inventory 3.0 system
│   │
│   ├── Scheduling
│   │   └── scheduling systems
│   │
│   ├── Task Assignment and Tracking
│   │   └── Work Queue system
│   │
│   └── Employee Achievements
│       └── systems to be determined
│
└── Documentation
    └── documentation systems
```

The crucial rule is:

> **Projects may contain child projects and systems. Systems are not automatically projects. Resources are not automatically systems.**

### B. Establish the ID namespace

I would define, but not necessarily populate everything immediately:

```text
PROJ-###   Project identity
SYS-###    System identity
RES-###    Resource identity
```

`RES-###` already exists.

For projects, the README should establish:

* IDs are stable and non-semantic.
* Renaming a project does not change its ID.
* Moving its repository folder does not change its ID.
* Changing its parent should not normally change its ID.
* IDs are never recycled.
* A parent project is still an ordinary project; its parent relationship is represented separately.

So:

```text
PROJ-001 — Operations
PROJ-002 — Inventory Management
```

rather than encoding hierarchy into the number.

### C. Define the minimum project relationship model

Something this simple:

```text
Project ID
Canonical Name
Parent Project ID
Project Type
Status
Canonical README
Primary Purpose
```

That's enough for a Project Registry.

Everything else can live in the canonical project README.

### D. Define the project-folder contract

Each mature project should eventually have:

```text
project-folder/
├── README.md
├── implementation-plans/
├── systems/
├── history/          [if useful]
└── other project-specific material
```

But I would make clear that **the folder layout does not define the entity**. We already made that distinction for resources and repository structure generally. The repository README explicitly says structure must be understood through function and relationships, not directories alone. 

### E. Define what a project README is authoritative for

The project README should own:

* project identity;
* parent relationship;
* purpose;
* scope/boundaries;
* represented real-world or technical function;
* systems belonging to the project;
* important shared systems/resources;
* project history at a high level;
* current status;
* navigation downward.

It should **not** contain detailed source-code documentation, giant data dictionaries, or every implementation detail.

### F. Explain the Project Registry relationship

The README should say:

```text
projects/README.md
    = rules for the project layer

Project Registry
    = structured identities and relationships

project/<name>/README.md
    = authoritative description of one project

Resource Registry
    = identities and locations of concrete resources
```

That distinction matters a lot.

The Meadows manual already describes the Project Registry as a planned structured synthesis of canonical project identities and relationships that should emerge after the high-level architecture has been reconciled. 

I think we're now at that transition point.

---

# 2. The `operations/README.md` needs a substantial identity correction

This is probably the most important existing document to fix **before IDs**.

The current file in `projects/operations/` is still titled:

> **Work Queue System**

and calls itself the canonical orientation document for the Work Queue system. 

Worse, its older terminology says:

> “The Work Queue system is the Klinswork project…”

while treating the web app as its implementation. 

That is no longer what the folder means.

I would turn that README into:

```text
# Operations

Entity Type: Parent Project
Project ID: [pending]
Parent: Klinswork
Primary current operational environment: Meadows Housekeeping
```

Its children would be:

```text
Inventory Management
Scheduling
Task Assignment and Tracking
Employee Achievements
```

Much of the current Work Queue README is still valuable—but it should ultimately move underneath **Task Assignment and Tracking / Work Queue**, not remain the identity document for `operations/`.

We should preserve that content rather than delete it because it is excellent bootstrap-era documentation.

---

# 3. Fix the vocabulary section in the Meadows manual

This should happen **before assigning IDs** because the Definitions section explicitly says it governs meaning. 

The current definitions still say:

* Housekeeping Operations is the parent operational project.
* Inventory Management, Scheduling, and Task Assignment and Tracking are systems.
* Work Queue and Inventory 3.0 are applications. 

We have now refined that.

I would change the vocabulary to something like:

**Project**
A durable organized body of Klinswork work with its own identity, scope, objectives, history, documentation, systems, resources, and lifecycle. A project may have a parent project and child projects.

**Parent Project**
A project that organizes related child projects under a broader scope. `Operations` is the parent project for the current housekeeping operational projects.

**System**
A coherent implemented mechanism, tool, service, or technical/operational system developed or maintained within a project. A system may consist of multiple applications, datasets, scripts, deployments, and other resources.

**Operational Function**
The real-world work or management function represented or supported by a project. It continues to exist independently of any Klinswork system.

**Application**
A user-facing software implementation or interface. An application may be part of a larger system and may also be registered as a Resource. It is **not a mandatory hierarchy level**.

That last part solves an important issue.

We can simultaneously say:

```text
SYS-001 — Work Queue
```

is the **system**, while:

```text
RES-002 — Work Queue app
Resource Type: APPLICATION
```

is a particular deployed/application resource belonging to that system.

So `APPLICATION` can remain a perfectly valid Resource Registry type.

---

# 4. Revise the Meadows “Project and System Register”

This needs to change from:

```text
Housekeeping Operations       project
Inventory Management          system
Scheduling                    system
Task Assignment & Tracking    system
```

to:

```text
Operations                         parent project
Inventory Management               project
Scheduling                          project
Task Assignment and Tracking       project
Employee Achievements              project / provisional
Documentation                      separate project
```

And then each project can list its systems.

For example:

```text
PROJECT — TASK ASSIGNMENT AND TRACKING

Parent Project:
Operations

Represented Operational Function:
Work intake, assignment, communication,
performance, completion, reporting,
verification and history.

Systems:
Work Queue
```

This is the exact area where the current manual says the identifiers remain “to be determined,” so we're not undoing established IDs—we're resolving the question the document intentionally left open. 

---

# 5. Create actual project-root READMEs before populating the registry

Right now Inventory Management has:

```text
projects/
└── operations/
    └── Inventory Management/
        └── implementation-plans/
            ├── implementation-plan.md
            └── README.md
```



There isn't yet an Inventory Management **project README at its root**.

I would create:

```text
projects/
├── README.md
│
└── operations/
    ├── README.md
    │
    ├── Inventory Management/
    │   ├── README.md
    │   └── implementation-plans/
    │
    ├── Scheduling/
    │   └── README.md
    │
    ├── Task Assignment and Tracking/
    │   └── README.md
    │
    └── Employee Achievements/
        └── README.md
```

We do **not** have to fill those READMEs exhaustively first.

They just need enough structure to establish the entity confidently.

---

# 6. Add project navigation to the repository root README

The README you just uploaded is the **repository root README**, and it is already good at explaining the physical/documentation infrastructure.

Its `documents/work-update-catalog/` section currently says that area contains project records among catalogs, sidecars, workflows, viewers, etc. 

I would add a distinct subsection:

```text
### Project Documentation

documents/work-update-catalog/projects/
```

and explain:

```text
projects/README.md
    = project architecture, vocabulary, ID rules,
      and project navigation

projects/<project>/README.md
    = canonical project descriptions
```

Then the repository's read path becomes beautifully clean:

```text
repository README
        ↓
projects/README
        ↓
parent project README
        ↓
project README
        ↓
system documentation
        ↓
resources / implementation evidence
```

That fits the existing repository principle that human-readable READMEs provide semantic orientation while manifests handle physical discovery. 

---

# 7. Don't create the Project Registry quite yet

I would make it the **last step of this preparation**, not the first.

We should first settle:

1. vocabulary;
2. project hierarchy;
3. canonical project names;
4. parent relationships;
5. canonical project README locations;
6. ID policy.

Then create the Project Registry and immediately seed it from those agreed facts.

Otherwise we'll create another spreadsheet that we immediately have to reinterpret.

The manual itself already anticipated exactly this sequence: complete and reconcile the highest-level project/system documentation, then synthesize the Project Registry. 

---

## The preparation pass I would actually perform

I think this is enough—no larger redesign is necessary:

```text
1. Create projects/README.md
      ↓
2. Revise Definitions in Meadows manual
      ↓
3. Rewrite operations/README.md as the Operations parent project
      ↓
4. Revise the Project and System Register
      ↓
5. Create skeletal READMEs for the identified child projects
      ↓
6. Update root repository README with project navigation
      ↓
7. Freeze PROJ-### rules
      ↓
8. Create Project Registry
      ↓
9. Assign the first project IDs
```

And at step 9, I expect the initial candidate set to look roughly like:

```text
Operations
Inventory Management
Scheduling
Task Assignment and Tracking
Employee Achievements
Documentation
```

with **Employee Achievements still allowed to remain provisional** until we're satisfied it really deserves project status.

I would avoid touching Resource IDs, catalog numbering, workflow sidecars, or the repository manifest during this pass unless one of those documents contains a statement that directly contradicts the new project vocabulary. The objective is to make the **project layer internally consistent**, then start issuing durable identities.
