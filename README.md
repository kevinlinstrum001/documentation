# Klinswork Documentation Repository — Read-First Orientation

This is the **root README for the `documentation/` repository** and a primary bootstrap document for Klinswork work sessions. The Klinswork Resource Registry points context-naive sessions here through `RES-000`.

The repository began as a place to host documents and links. It has grown into a broader working information environment containing project and system documentation, applications and data references, structured records, manifests, catalogs, viewers, images, workflows, historical evidence, and the infrastructure used to recover context for future work.

This README is therefore not merely a repository description. Its job is to give a new reader — especially ChatGPT in a fresh window — enough broad orientation to understand **what exists, how the major pieces fit together, how Klinswork does work, where authority lives, and what other context may matter before changing something**.

This file is **orientation**, not the source of truth for every current fact. When a designated current-state authority conflicts with this README, use the designated authority and treat the mismatch here as documentation debt to reconcile.

---

## Serious Work Session Startup

For a substantial Klinswork work session, do not optimize startup merely for brevity. Broad architectural context is valuable because important dependencies are often *unknown unknowns*: the session may not know that it needs a fact until the overview reveals the relationship.

Recommended startup sequence:

1. **Read this root README completely.**
2. **Open the Klinswork Resource Registry (`RES-043`) and read its README tab.** The Registry README defines current routing, authority, Work Unit, and spreadsheet-inspection rules.
3. **Read the Meadows Housekeeping Projects Summary (`RES-042`) when Operations, housekeeping Projects, Systems, or shared operational relationships may matter.** It is the broad human-readable architecture source for the current Operations landscape.
4. **Check the Registry Work Units tab for current work state.** Do not infer active work from old narrative status text.
5. **Identify the Project, System, Resource, or other work target.** Then read the nearest local README and current human-readable summary for that target.
6. **Resolve implementation Resources and specialized instruction sets only after the target is understood.** This may include source, datastore, deployment, technical manual, workflow, Record Profile, implementation plan, or other governing material.
7. **Check cross-system consumers and dependencies before making a change that appears local.** A file, generator, manifest, dataset, or image collection may be consumed elsewhere.
8. **Verify consequential current-state claims against the authority that owns them.** For software behavior, current source + current datastore/schema + current deployment + fresh executable tests/verification outrank stale narrative documentation.

The goal is a **rich, coherent starting model followed by targeted deeper loading**, not either extreme of reading the entire repository indiscriminately or loading only the narrow folder named in the first task.

---

## Klinswork at a Glance

**Klinswork** is the broader organizing environment for Projects, Systems, Resources, documentation, registries, applications, histories, work planning, and related tools. Klinswork itself is not assumed to be a Project.

The current Operations architecture is broadly:

```text
Klinswork
│
├── Operations                         [parent Project]
│   │
│   ├── Inventory Management           [child Project]
│   │   └── Inventory 3.0              [principal System]
│   │
│   ├── Scheduling                     [child Project]
│   │   └── System boundary remains under reconciliation
│   │       Calendar and related implementations are Resources/implementations under review
│   │
│   ├── Task Assignment and Tracking  [child Project]
│   │   └── Work Queue                 [principal System]
│   │
│   └── Employee Achievements          [provisional Project candidate]
│
└── Documentation                      [separate cross-project Project]
```

**Meadows Housekeeping** is the primary current real-world operational environment represented by the Operations Project family. It is not itself the Project hierarchy.

The broad Operations overview is maintained in the **Meadows Housekeeping Projects Summary (`RES-042`)**:

<https://docs.google.com/document/d/1fZ5ndjUI0rCVqTFCrNwVGihwJZghW2_giHVoqbXPqo8/edit>

That document is intentionally broader than any single application. It explains Projects, Systems, operational functions, shared Resources, boundaries, and major relationships. Use it for architectural orientation; use the appropriate Project/System/runtime authority for detailed current claims.

---

## Core Entity Distinctions

Do not collapse these concepts merely because they are physically near one another or because one implements another.

- A **Project** is a durable organized body of Klinswork work with its own purpose, scope, history, documentation, Systems, Resources, and lifecycle.
- A **child Project** is still a Project. Parent/child placement is a relationship, not a different entity type.
- A **System** is a coherent implemented mechanism, service, tool family, or technical/operational system developed or maintained within a Project.
- An **Application** is a user-facing implementation or interface. It may be a Resource within a System; it is not automatically a Project or System.
- A **Resource** is a specific identifiable artifact, dataset, application, document, service, repository location, deployment, datastore, script, or other resolvable item.
- An **operational environment** is the real-world setting in which the work occurs.
- An **operational function** is real work or management activity that exists independently of the software used to represent it.
- A **Work Unit** is bounded, addressable work to resolve. It is not a Project, System, or Resource.

The governing identity principle is:

```text
identity != name != location != hierarchy != lifecycle/status != implementation
```

Do not invent `PROJ-###`, `SYS-###`, `RES-###`, `WORK-####`, `WUA-####`, or Activity identifiers. Use the authority that assigns or records each identifier. Blank identifiers remain blank until formally assigned.

---

## How Klinswork Does Work

Klinswork uses a few recurring operating principles.

### Work is goal-first and bounded

When something should be remembered, accomplished, investigated, mapped, validated, produced, or otherwise resolved, it may become a **Work Unit**. A Work Unit should express a coherent outcome and completion condition without requiring implementation details before those details are known.

The **Work Units** tab in `RES-043` is the current-state authority for registered Work Units. **Work Unit Activities** is append-oriented history of material Work Unit changes and events.

A formal **Work Session** should correspond to a governing Work Unit. A Work Implementation Session is one specialized session type; it does not define all Work Sessions.

Closed Work Units stay closed. Follow-on work receives its own Work Unit rather than being smuggled into a completed one.

### Current state and history are kept separate

Klinswork generally prefers a concise current-state record plus append-oriented history rather than continuously rewriting the current record to preserve every prior state.

```text
Resource current state     → Resources
Resource history           → Activities
Work Unit current state    → Work Units
Work Unit history          → Work Unit Activities
```

### Authority depends on the question

Different records answer different questions.

- **Project Identity Entity Record** — narrow intrinsic Project identity when one exists.
- **Project Summary** — current human-readable Project purpose, scope, meaning, and boundaries.
- **System Summary** — what a System is now, based on current evidence.
- **System Roadmap** — what a System should become; future direction is not current state.
- **Implementation Plan** — intended method for bounded change; it is not execution evidence.
- **Current source + current datastore/schema + current deployment + fresh tests/verification** — detailed current runtime behavior.
- **Resources tab** — registered Resource identity, current location/routing, type, and Registry-level current facts.
- **Activities** — Resource provenance/history.
- **Work Units / Work Unit Activities** — current bounded-work state and its history.
- **README files** — orientation, navigation, local interpretation, and read-first instructions.
- **Manifests** — generated discovery snapshots, not semantic authority.
- **Catalogs** — aggregate discovery products, not a second source of truth.
- **Sidecars** — machine-readable companions to human-readable sources; they do not automatically become entity identity or override the source document they interpret.
- **Viewer** — presentation/retrieval layer; displaying a record does not make the Viewer authoritative for that record's facts.

### Unknowns remain unknown

Klinswork prefers an explicit unresolved question or blank field to a plausible invention. Historical records should preserve what was understood at the time rather than being silently rewritten to make the current architecture appear retroactive.

### Dependencies are part of the work

Before changing a file, generator, datastore, manifest, schema, or folder structure, ask:

```text
What generates this?
What consumes this?
What references this?
What other Project or System depends on it?
What authority owns the resulting state?
```

A local-looking change may have downstream effects that are invisible from the folder alone.

---

## The Klinswork Resource Registry (`RES-043`)

The Registry is no longer merely a list of links. It is a **context, lookup, routing, and work-resumption layer** used primarily to help future sessions recover the correct information environment.

Current workbook:

<https://docs.google.com/spreadsheets/d/14_bNqnExG6_4Omg0cEqENm2hGivz5qqvWEk9IJaGl_A/edit>

Its current tabs are:

```text
README
Resources
Activities
Work Units
Work Unit Activities
```

Physical co-location does not merge their semantic authority.

The **Resources** tab should remain a relatively sparse routing map of durable, high-value things a future session may need to resolve. It is not intended to enumerate every sidecar, lesson, summary, template, generated document, or ordinary repository file. Documentation records that are naturally discoverable through the Documentation Viewer and their owning Documentation Spaces usually do not need independent Resource IDs merely because they exist.

A Resource row is useful when it helps answer questions such as:

```text
What object is this?
Why might a future session need it?
Where is it currently located?
What should be read to understand it?
What authority or context does it participate in?
```

The linked Resource may be an application endpoint, workbook, repository location, or other object that ChatGPT cannot directly interpret well. In those cases the Resource's description, local README, technical manual, System documentation, or other interpretation reference may be more useful than the deployment URL itself.

---

## Repository Organization

The repository should be understood by **function, authority, and relationships**, not only by directory structure. Physical folders answer where files currently live; they do not establish Project identity, System identity, authority, lifecycle state, or ownership by themselves.

Important current areas include:

### Repository root

The root contains repository-wide entry points and generators, including:

```text
README.md
build_repository_tree.py
documentation-viewer-sources.json
documentation-viewer-manifest.py
index.html
images/
documents/
work_updates/
```

A generated repository tree is useful physical evidence when current structure matters, but a tree is not semantic authority.

### `documents/Klinswork Documentation Viewer/`

This is the main Common Documentation / Viewer area. It includes Viewer infrastructure and cross-project documentation such as:

```text
Record Profile Library/
archived/
catalogs/
projects/
sidecars/
summaries/
tools/
workflows/
documentation-viewer-manifest.json
json-viewer.html
```

The nested `projects/` area is the **Projects Documentation Space** for Project-local records.

### `documents/therapy-documentation-work/therapy-component-library/`

This is a separate registered **Therapy Component Library** Documentation Space. It is intentionally distinct from Common Documentation and Projects even though the same Viewer may discover records from all of them.

### `images/`

This is the central repository image collection and includes the generated image inventory used by other tooling.

### `work_updates/`

This area contains published work-update material. Work Updates are retrospective/downstream documentation and should increasingly synthesize structured Work Unit, Activity, session, validation, and resulting-state evidence rather than reconstructing work only from conversation history.

Other repository areas may contain personal, historical, narrative, experimental, or publication material. Do not infer semantic status from a directory name alone.

---

## Current Documentation Viewer Discovery Architecture

The current source-aware discovery chain is:

```text
documentation-viewer-sources.json
        ↓
documentation-viewer-manifest.py
        ↓
documents/Klinswork Documentation Viewer/documentation-viewer-manifest.json
        ↓
Klinswork Documentation Viewer
```

The source registry currently declares three Documentation Spaces:

```text
common    → documents/Klinswork Documentation Viewer
projects  → documents/Klinswork Documentation Viewer/projects
therapy   → documents/therapy-documentation-work/therapy-component-library
```

The source registry and builder live at the repository root because they govern more than one Documentation Space. The current registered generated Viewer manifest lives in the Klinswork Documentation Viewer root.

The older `json-manifest.json` and `manifest.py` remain in the repository as legacy/compatibility artifacts. They are **not the current source-aware discovery authority**. Do not treat their continued physical presence as evidence that the old single-root Viewer architecture is current.

The Viewer discovers and presents records; the records and their designated authorities still own their meaning.

---

## Project and System Documentation

Project-local documentation is organized under:

```text
documents/Klinswork Documentation Viewer/projects/
```

A Project package may contain a local README, human-readable Project Summary, structured companions, implementation plans, System documentation, and other Project-local records. Folder structure is a navigation/locality convention, not identity.

For example, Task Assignment and Tracking is currently documented under:

```text
documents/Klinswork Documentation Viewer/projects/operations/Task Assignment and Tracking/
```

and Work Queue under:

```text
documents/Klinswork Documentation Viewer/projects/operations/Task Assignment and Tracking/systems/Work Queue/
```

When the subject is Work Queue:

```text
Need orientation / what Work Queue is
    → Work Queue README + current System Summary

Need current detailed implementation behavior
    → current source + datastore/schema + deployment + fresh tests/verification

Need future direction
    → Work Queue System Roadmap

Need Task Assignment and Tracking Project meaning
    → Project README + Project Summary

Need broad Operations placement
    → Meadows Housekeeping Projects Summary (RES-042)

Need a mutable application/datastore/manual location
    → Resource Registry
```

This same pattern should guide work on other Projects and Systems: **nearest useful context first, then the authority appropriate to the claim**.

---

## Specialized Instruction Sets and Workflows

Not every interpretation or update rule belongs in this README or in a Resource row.

Klinswork may use specialized instruction sets, READMEs, Record Profiles, workflow specifications, implementation plans, or other governing records for particular kinds of work. Examples include instructions for:

- interpreting Project documentation;
- updating Project or System documentation;
- constructing or validating sidecars;
- working with Record Profiles;
- updating the Resource Registry;
- rebuilding manifests;
- validating Viewer discovery;
- performing a particular implementation workflow.

When such an instruction set exists and the task falls within its scope, load it before consequential changes. The root README should tell a new session that these governing instructions exist; the Registry and local documentation should help resolve the specific one needed.

---

## Important Cross-System Dependencies

This section intentionally records a small number of high-value relationships that help a fresh session recognize dependencies it may not otherwise know to search for.

### Images → image manifest → Email Composer

The repository contains:

```text
images/images.json
images/build_images_json.py
```

`images/images.json` is generated from the repository image collection. A known consumer is the **Email Composer image selector**.

Therefore, when repository images are added, removed, renamed, moved, recategorized, or otherwise changed in a way that affects image discovery, do not treat the work as an isolated folder edit. Check whether `images/images.json` must be regenerated and whether the Email Composer's expectations remain satisfied.

This is a model for dependency-aware work: a session working on `images/` may not initially know that Email Composer matters. The broad overview exists partly to expose relationships like this before work begins.

### Work Queue ↔ Inventory Management

Task Assignment and Tracking owns task meaning, assignment, status, and completion. Inventory Management owns inventory-state meaning. Verified integration work has allowed qualifying Work Queue task completion to produce inventory-holder events for the affected endpoint. The two Systems/Projects remain separate authorities even when events cross the boundary.

When changing either side of this integration, inspect the current Project/System documentation and current data/runtime evidence rather than assuming the relationship from historical descriptions.

### Shared Locations

Canonical physical locations are shared context used across Work Queue, Inventory, Scheduling/Calendar, and other operational records. A location can exist once while being enabled or interpreted differently by different Systems.

### Shared employee/personnel records

Employee/role data may participate in Scheduling, Work Queue assignment, achievement evidence, and other contexts. Digital access, operational role, information-provider role, editorial authority, and administrative authority should not be inferred from one another.

### Email Composer is a shared Resource

Email Composer supports communication across more than one Project/System. It should not be treated as belonging exclusively to the first workflow that happens to use it.

---

## Images and Reusable Assets

`images/` is a shared repository asset area rather than a self-contained Project. Current high-level structure includes categorized image folders plus:

```text
images/images.json
images/build_images_json.py
```

Because the image manifest has consumers, image maintenance should preserve both human organization and machine discoverability.

When doing image work:

1. inspect the current image structure;
2. determine whether the change affects manifest discovery or paths;
3. rebuild/verify `images.json` when required;
4. consider known consumers such as Email Composer;
5. preserve stable paths where downstream references depend on them, or update those references deliberately;
6. record durable newly discovered dependencies in the appropriate overview/README/Registry context so the next session does not have to rediscover them.

---

## Record Profiles, Sidecars, Manifests, and Catalogs

These record families have different jobs.

### Human-readable source documents

These carry the readable narrative for summaries, plans, lessons, workflows, work updates, and similar documents.

### Sidecars

A sidecar is a structured companion to a human-readable source. It may support discovery, validation, routing, Viewer presentation, and machine-assisted interpretation. The human-readable source remains authoritative for the document itself unless another authority is explicitly designated.

### Record Profile Library

The Record Profile Library defines reusable interpretation/construction contracts and related templates or compatibility information. It lives under:

```text
documents/Klinswork Documentation Viewer/Record Profile Library/
```

Use the library's own README and profile-specific definitions when constructing or interpreting governed record families.

### Manifests

Manifests answer physical/discovery questions such as what records exist and where they were found at generation time. They are rebuildable and do not define semantic Project membership or replace source authority.

### Catalogs

Catalogs aggregate selected information for browsing and discovery. Intentional duplication in a catalog does not create a second source of truth; discrepancies should be reconciled against the source records.

---

## Publication

GitHub Pages is a publication layer over this repository, not the repository's only purpose.

Published root:

<https://kevinlinstrum001.github.io/documentation/>

Selected HTML documents, images, viewers, and other static assets can therefore serve as stable browser-facing Resources while their source documentation, structured companions, registries, and work history remain elsewhere in the architecture.

---

## Freshness and Reconciliation Rules

This repository changes quickly enough that physical paths, runtime behavior, Work Unit status, and generated discovery state can become stale in narrative documentation.

Use these rules:

1. **A designated current-state authority beats a stale narrative status annotation.**
2. **Current runtime evidence beats an older implementation description.**
3. **A manifest is a generated discovery snapshot, not semantic truth.**
4. **A repository tree is physical evidence, not an ontology.**
5. **A README is an orientation layer and should be reconciled when it misroutes readers.**
6. **Do not silently rewrite historical artifacts merely because the current model changed.**
7. **When an architectural dependency is discovered, preserve it in the appropriate durable orientation or relationship record.**
8. **When a context-naive session repeatedly misinterprets a structure, treat that as information-system feedback and improve the routing/documentation layer.**

The purpose of the documentation system is not to create one enormous source of truth. It is to make the correct source of truth **discoverable, interpretable, and usable in context**.

---

## What This README Should Answer

After reading this file, a fresh session should at least know:

```text
What Klinswork is.
What the major Operations Projects and principal Systems are.
That Documentation is a separate cross-project Project.
That Meadows Housekeeping is an operational environment.
That Project, System, Resource, Application, and Work Unit are different concepts.
Where the Registry fits and how its current-state/history tabs differ.
How bounded work is planned, executed, verified, recorded, and resumed.
Where current Project/System meaning should be read.
Where detailed runtime truth should be verified.
How the current source-aware Documentation Viewer discovers records.
That legacy Viewer manifest/builder files still exist but are not current discovery authority.
That images/images.json is generated and consumed by Email Composer.
That shared Resources and cross-System dependencies can make a local-looking change non-local.
That specialized instruction sets may need to be loaded before updates.
That unknown IDs and relationships must not be invented.
```

If a serious session lacks that level of orientation, it should continue context loading before making broad architectural or implementation changes.

---

## Maintenance Principle

This README should remain broad, current, and high-value. It should not duplicate every Project Summary, System Summary, Registry row, technical manual, Work Unit, or historical record. Instead it should preserve enough durable architecture and operating method that a context-naive reader knows **what exists, what may depend on what, where to look next, and how Klinswork expects work to be done**.

When the architecture changes materially, when a major dependency is discovered, or when a bootstrap/context test exposes a recurring misunderstanding, update this README or the more specific authority that owns the affected rule.
