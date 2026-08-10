---
summary_id: work-summary-2026-08-08-09-klinswork-weekend-architecture
coverage_start: 2026-08-08
coverage_end: 2026-08-09
created: 2026-08-10
document_type: comprehensive-work-summary
status: working-comprehensive-summary
primary_program: Klinswork
primary_projects:
  - Documentation
  - Housekeeping Operations
primary_operational_environment:
  - Meadows Housekeeping
major_systems:
  - Inventory Management
  - Scheduling
  - Task Assignment and Tracking
  - Employee Achievements (provisional system/capability)
related_personal_documentation_projects:
  - PST-SP study-guide and therapy-resource collection
source_basis:
  - August 9 Documentation Resource Registry and Startup work summary
  - Documentation repository README
  - workflow-run-sidecar-template-3.1-draft.json
  - August 1 Documentation bootstrap work update
  - Meadows Housekeeping Projects Summary Google Doc
  - August 8-9 conversation records and retained repository artifacts
---

# Weekend Architecture and Repository Consolidation
## Comprehensive Work Summary — August 8–9, 2026

## Document purpose

This document records, as comprehensively as practical, the work completed or materially advanced during the weekend of **Saturday, August 8, and Sunday, August 9, 2026**, together with the architectural conclusions that emerged from that work.

The weekend was not one isolated implementation session. Several streams of work converged:

- organization of the Klinswork Documentation repository;
- clarification of the repository's responsibilities and navigation model;
- continued development of the JSON viewer, manifests, catalogs, and document sidecar approach;
- creation and expansion of the Klinswork Resource Registry;
- separation of stable resource identity from changing physical location;
- development of Activities-based provenance for Registry changes;
- creation of a bootstrap route for context-naive ChatGPT sessions;
- definition of a Startup procedure and progressive context-loading architecture;
- reconciliation of the existing Documentation workflow with the new Startup and Registry model;
- creation of a high-level Housekeeping Operations / Meadows Housekeeping architecture document;
- clarification of the distinction among projects, operational environments, systems, applications, implementations, and resources;
- detailed high-level documentation of Inventory Management, Scheduling, Task Assignment and Tracking, Employee Achievements, Documentation, shared resources, historical eras, and open determinations;
- Work Queue 2.1 employee-assignment work that moved the application closer to bulk assignment by employee;
- continued therapy-resource organization around PST-SP, CPT, EMDR, authoritative PDFs, Markdown master documents, JSON sidecars, and specialized viewers;
- creation or refinement of a workflow-run sidecar model able to represent Startup, resource resolution, reconstructed sessions, execution history, evidence, reconciliation, publication, and closure.

The most important result was not merely that many files were arranged or many documents were written. The weekend moved Klinswork toward a system in which **the environment can increasingly explain its own structure, locate its own authoritative resources, distinguish historical from current truth, and tell a new work session what it should read next**.

---

# 1. Executive summary

At the beginning of the weekend, Klinswork already contained substantial functional material: Apps Script applications, Google Sheets data stores, GitHub-hosted documents and tools, Google Sites indexes, work updates, JSON sidecars, catalogs, images, viewers, therapy-study materials, and operational applications such as Inventory 3.0 and Work Queue.

The persistent weakness was not lack of content. It was **lack of sufficiently explicit semantic structure across the content**.

Important questions still depended too heavily on conversational memory:

- What is Klinswork as a whole?
- Which undertaking is a project versus a system versus an application?
- Which file or resource is authoritative for a given fact?
- Which artifacts are historical, current, generated, published, or merely experimental?
- How does a new conversation discover the right documents without being handed the whole project universe?
- How should a workflow describe the information it needs without hard-coding one particular file path or URL?
- How can a resource remain conceptually the same resource when its URL or deployment changes?
- How should project files be created if the system cannot yet reliably locate and interpret the resources from which those files must be built?

The weekend attacked those questions from both directions.

On one side, the **Documentation infrastructure** became more explicit. The repository README was expanded into a genuine orientation document. Manifest types were distinguished. The JSON viewer was understood as both a generic inspector and a type-aware presentation layer. The Resource Registry evolved from a shortcut list into an identity and routing authority. Activities became a provenance mechanism. `RES-000 — CHATGPT — READ THIS FIRST` created an entry route. Startup became a distinct bootstrap procedure. Workflows were reconceived as declaring semantic context requirements that the Registry resolves into current resources.

On the other side, the **subject matter being documented** became more explicit. The Meadows Housekeeping Projects Summary established Housekeeping Operations as the parent operational project, Meadows Housekeeping as its current primary operational environment, and durable operational systems beneath it. Work Queue and Inventory 3.0 were demoted, correctly, from being treated as the organizing entities themselves to being applications or implementations of larger real-world systems. Paper processes, verbal reports, ordinary institutional channels, people, locations, supplies, tasks, schedules, and operational histories were all restored to the model as first-class realities independent of whether an application existed or was adopted.

By the end of the weekend, the architecture could be expressed approximately as:

```text
Klinswork
│
├── Documentation                         [cross-project infrastructure project]
│   ├── repository
│   ├── workflows
│   ├── Resource Registry
│   ├── Startup
│   ├── summaries / sidecars / catalogs
│   ├── viewers / manifests / templates
│   └── project and system documentation
│
└── Housekeeping Operations               [operational project]
    │
    └── Meadows Housekeeping              [primary current operational environment]
        │
        ├── Inventory Management          [operational system]
        │   └── Inventory 3.0             [principal application / implementation]
        │
        ├── Scheduling                    [operational system]
        │   └── Calendar / roster tools   [implementations]
        │
        ├── Task Assignment and Tracking  [operational system]
        │   └── Work Queue                [principal application]
        │
        └── Employee Achievements         [provisional system / capability]
```

Shared resources can cross these boundaries rather than being copied into each project as if they were independently owned. Examples include employee and role data, locations data, Email Composer, repository infrastructure, common identifiers, templates, and import/export methods.

The weekend therefore marks a transition from **organizing applications and files** toward **organizing represented systems, authorities, relationships, histories, and resources**.

---

# 2. Scope and source discipline

This summary deliberately distinguishes several kinds of evidence.

## 2.1 Direct weekend architecture records

The strongest direct records are:

- `summary-2026-08-09-documentation-resource-registry-startup.md`;
- the root Documentation `README.md`;
- `workflow-run-sidecar-template-3.1-draft.json`;
- the linked Google Doc **Meadows Housekeeping Projects Summary**;
- repository and code artifacts preserved from the Work Queue work;
- retained PST-SP study-guide files and viewer artifacts.

## 2.2 Historical baseline

The August 1 work update, **A Documentation System for Projects, Narrative, and Repeatable Work**, is used as the principal earlier baseline. It is not weekend work, but the August 9 work explicitly continued it and solved several problems that August 1 had left unresolved.

## 2.3 Conversation-derived weekend details

Some Saturday details—particularly the exact debugging sequence around the Work Queue employee field, repository therapy folders, and some viewer work—are preserved primarily in conversation history and retained code/files rather than in a final dated work update. Those items are identified as such rather than presented as if they came from a formal published record.

## 2.4 Chronology caveat

The weekend architecture itself insists on preserving chronology honestly. Some major ideas were discovered before they were recognized as formal Documentation work. The August 9 record explicitly rejects rewriting the session as though the final architecture had been prospectively planned from the beginning.

This summary follows the same principle.

---

# 3. Starting position before the weekend

The weekend did not begin with an empty repository. Klinswork already had substantial history.

The Documentation repository contained, among other things:

- published HTML work updates;
- Markdown summaries;
- JSON sidecars;
- sidecar templates;
- cumulative catalogs;
- workflow specifications;
- viewer tools;
- image collections and image manifests;
- scripts;
- project-oriented or application-oriented directories;
- GitHub Pages publication;
- root-level web assets;
- a growing set of study and reference materials.

The August 1 Documentation bootstrap had already established several crucial principles:

1. A dated work-update record is not the same thing as a durable project record.
2. A narrative summary and a structured sidecar serve different purposes.
3. `summary.md`-style narrative can preserve how work unfolded and why decisions were made.
4. Sidecars can preserve structured identity, relationships, metadata, outcomes, and other machine-readable information.
5. A cumulative catalog can support discovery across documents.
6. Documentation itself should operate through a reusable workflow rather than being reconstructed ad hoc every time.
7. Context should be loaded progressively and purposefully rather than requiring the model to hold the entire project universe continuously.
8. Formal project records were a major next milestone.

But August 1 still left major questions unresolved:

- How should an instruction set or workflow discover the files it needs?
- How should project context be made reliably available to a fresh conversation?
- Where should authoritative project records live?
- How should a new work session resume from known state without depending on memory?
- How should relationships among Markdown, HTML, sidecars, catalogs, templates, and project records be represented?

By the weekend, these unresolved questions became limiting factors.

---

# 4. Saturday, August 8 — repository, application, and document-family consolidation

Saturday's work was broad. It included application-level debugging, repository organization, therapy-resource structure, viewer thinking, and a major shift in how the broader project should be modeled.

## 4.1 Repository landing page and structural orientation

Work on the repository landing page and navigation helped clarify that the Documentation repository was no longer merely a collection of work updates.

The repository had become a shared home for:

- documents;
- images;
- structured metadata;
- JSON sidecars;
- catalogs;
- manifests;
- viewers;
- scripts;
- templates;
- project and application records;
- historical artifacts;
- web publication.

This led to a crucial distinction:

```text
directory organization
    is not the same thing as
semantic organization
```

A directory can tell a reader where a file lives. It cannot, by itself, explain:

- why the file exists;
- whether the file is current;
- whether it is source, generated, aggregate, companion, or published output;
- what process generates it;
- what tools consume it;
- what other artifacts it belongs with;
- which workflow governs changes to it;
- what should be read before modifying it.

That distinction became one of the foundations of the root README and the planned repository-manifest concept.

## 4.2 Repository responsibilities become explicit

The refined repository model identifies several overlapping responsibilities:

### Hosting durable documents and reference material

The repository stores work updates, study material, project documentation, HTML pages, Markdown sources, and other files that benefit from stable versioned locations.

### Hosting images and reusable assets

The `images/` area holds screenshots, icons, banners, work-update graphics, and other visual material that can be reused by documents and tools.

### Providing stable public URLs

GitHub Pages allows selected static documents, images, viewers, and JSON resources to be referenced through predictable public locations.

### Storing structured records

JSON sidecars, catalogs, manifests, templates, project/system records, workflow records, and metadata belong alongside the documents they describe.

### Hosting tools and viewers

Local and online JSON viewers, Python utilities, launchers, manifest generators, and related support tools operate close to the records they understand.

### Preserving working and historical material

Earlier versions, bootstrap-era folders, abandoned experiments, and superseded structures can remain as evidence rather than being silently erased.

This was a substantial conceptual upgrade: the repository was formally understood as **documentation infrastructure and durable storage**, not simply as “the website.”

## 4.3 Manifest types were separated

The weekend clarified that several things called “manifest” serve different functions.

### JSON Viewer manifest

`documents/work-update-catalog/json-manifest.json`

Generated by `manifest.py`, it inventories JSON files for the online static viewer and allows GitHub Pages to provide file discovery without a local Python server.

### Image manifest

`images/images.json`

Generated by the image inventory script, it inventories repository images and is consumed by systems such as Email Composer.

### Browser / PWA manifests

Files such as `site.webmanifest` and root `manifest.json` describe web-app/browser identity, icons, theme, start URL, and install/display behavior.

### Planned repository manifest

A future `repository-manifest.json` is intended to be a semantic map of the repository itself: major systems, canonical artifacts, generators, consumers, relationships, read-first documentation, and unresolved areas.

The distinction prevented the word *manifest* from becoming a vague catch-all.

## 4.4 JSON Viewer and online/local viewing model

The viewer work continued to evolve from a utility for opening JSON into a generalized structured-document presentation system.

The model now distinguishes:

### Local viewer

The local Python-based viewer can:

- use filesystem access;
- scan directories directly;
- use Python endpoints;
- provide desktop-oriented inspection;
- support specialized preview behavior.

### Online viewer

The GitHub Pages viewer cannot scan the local filesystem and therefore depends on static repository resources such as:

- `json-manifest.json`;
- catalogs;
- sidecars;
- structured JSON files;
- static HTML/JavaScript behavior.

The same conceptual collection can therefore support two runtimes:

```text
Local runtime
    filesystem-aware
    Python-assisted

Static online runtime
    manifest-driven
    GitHub Pages
```

This became part of the larger effort to make the viewer a general portal into structured project/document information rather than a one-purpose PST-SP tool.

## 4.5 Root README shifts from description to orientation authority

A major Saturday/Sunday product was the root Documentation README.

Its role became:

```text
README.md
    = human-readable orientation
```

The README explicitly says the repository should be understood by **function and relationships**, not directory structure alone.

It documents:

- the repository's overlapping responsibilities;
- major directories;
- important viewer and manifest files;
- generator/consumer relationships;
- the difference among manifests;
- sidecars and catalogs;
- the viewer ecosystem;
- design principles;
- context-restoration procedure for future sessions.

This document later became the destination of `RES-000 — CHATGPT — READ THIS FIRST`, making the README not simply a passive repository description but part of the active Startup architecture.

---

# 5. Saturday therapy-resource and document-processing work

A parallel branch of the weekend organized therapy and clinical-study documents into the same broader Documentation approach.

## 5.1 PST-SP master study-guide architecture

The PST-SP work had already established a strong document-processing model:

```text
source packet / PDF / photographed pages
        ↓
master Markdown study guide
        ↓
structured JSON sidecar
        ↓
HTML publication
        ↓
viewer / catalog / metadata integration
```

The master Markdown document is deliberately concept-based rather than a simple page-by-page transcription.

The retained PST-SP study guide includes major sections for:

- program overview;
- treatment structure;
- problem-solving model of stress;
- obstacles to effective problem solving;
- Toolkit One: Stop and Slow Down;
- Toolkit Two: Visualization for Hope and Motivation;
- Toolkit Three: Overcoming Brain Overload;
- Toolkit Four: Planful Problem Solving;
- problem-solving beliefs and styles;
- review and future forecasting;
- optional handouts and supporting tools;
- measures;
- integrated PST-SP workflow;
- personal notes and applications;
- source review log.

One important interpretive discovery from the source material was the repeated idea of **building a toolkit** rather than simply consuming a packet of worksheets. That terminology aligned strongly with the larger Klinswork pattern: reusable structured tools, selected according to the problem being solved.

## 5.2 Visual-source policy

The PST-SP project also developed a durable policy for images and diagrams.

When a source visual matters, the Markdown master should preserve:

1. an explicit image placeholder;
2. a physical description of what the image looks like;
3. a semantic description of what the image communicates.

This allows later decisions about which original images should actually be uploaded while preventing the meaning of the visual from disappearing if the image itself is not yet present.

## 5.3 CPT / PST-SP / EMDR repository organization

The weekend extended the therapy-resource concept beyond one packet.

The repository was organized with dedicated folders including:

- `cpt/`;
- `pst-sp/`;
- `emdr/`;
- additional therapy/resource folders created during the same organization pass.

The intent was not merely file storage. The emerging concept was a **clinician-style assembly and reference environment** based on authoritative PDFs, structured sidecars, and extractable document fragments.

Important observations preserved from the work include:

- the VA CPT packet in hand contained 17 listed handouts;
- a CPT book preview exposed a larger handout family of roughly 48 items;
- the PST-SP paper packet listed 28 handouts plus 3 optional handouts;
- PST-SP pages used mixed portrait and landscape layouts;
- some handouts were multi-page;
- footers and version marks included clues such as `Veteran Version`, `Version 2`, `Revised 10/4/2023 JFG`, and `HANDOUT ##`;
- decimal handout numbering such as `5.1` appeared;
- the table of contents and footer conventions provided clues for locating authoritative digital resources;
- CPT, PST-SP, and EMDR were being treated as distinct source families that could share a common document-processing and viewing architecture.

## 5.4 Specialized viewer as proof of a broader pattern

`pst-viewer.html` became useful conceptually even beyond PST-SP.

It demonstrated that the Documentation system can support:

- generic JSON inspection;
- shared catalogs and manifests;
- specialized document-family previews;
- domain-specific navigation where useful.

The likely long-term model is therefore not one monolithic viewer that renders every document identically, but a shared structured-data infrastructure capable of specialized views.

---

# 6. Saturday Work Queue 2.1 — stable employee assignment

One of the clearest concrete application advances during the weekend was the employee-assignment work in Work Queue 2.1.

## 6.1 Problem being solved

Work Queue already managed tasks, locations, status, completion, task activity, and inventory-holder integration. But assignment still needed stronger linkage to the employee dataset.

The desired behavior was not merely to type a person's name. A task should be able to store a stable employee identity and display the employee's current human-readable name.

Conceptually:

```text
Employee directory
    Employee ID
    Display Name
        ↓
Work Queue task
    Assigned Employee ID   [stable identity]
    Assigned To            [human-readable name]
```

This distinction is essential for future bulk assignment, reassignment, employee views, and cross-system identity.

## 6.2 New task schema field

The Tasks sheet required a new header:

```text
Assigned Employee ID
```

A debugging interruption occurred because the header was initially added to the Work Queue 2.0 sheet rather than the active Work Queue 2.1 sheet. The validation error correctly reported that the required header was missing.

After the header was added to the correct 2.1 dataset, configuration validation succeeded.

## 6.3 Application logic

Retained Work Queue code shows the stronger assignment model directly.

Task creation accepts:

```text
assignedEmployeeId
```

The employee ID is validated against the employee directory. The task record then stores both:

```text
Assigned To
Assigned Employee ID
```

Reassignment follows the same pattern. `assignTask()` resolves the employee by ID, updates the display name, updates `Assigned Employee ID`, and writes an `ASSIGNEE_CHANGED` activity record.

That means assignment is no longer just presentation text. It is part of the task's structured identity and history.

## 6.4 UI work

The Create Task interface gained an **Assigned Employee** field sourced from the employee data rather than relying on free-form names.

During the same debugging pass, a missing `assignedToFilter` UI element was identified and restored in the correct file.

The debugging sequence was frustrating because several copies of the HTML existed and one returned version appeared much shorter than expected, raising concern that a truncated or wrong file had been edited. The final implementation was tested rather than accepted solely from code inspection.

## 6.5 Successful test

A test task for **vacuuming in Aspen South** was assigned to **Gina**.

The employee list populated correctly, and the assignment appeared to work as intended.

The practical conclusion was that Work Queue had moved a significant step closer to the larger goal:

```text
select employee
    ↓
select unit / work plan
    ↓
generate or assign many appropriate tasks
```

## 6.6 Relationship to the bulk-assignment roadmap

Retained roadmap material describes a future batch-generation flow:

```text
Select assignment information
→ Load matching templates
→ Resolve target locations
→ Build preview
→ Confirm
→ Create batch
```

The roadmap expects batch-created tasks to preserve:

- valid task IDs;
- valid employee IDs;
- employee display names where needed;
- valid location IDs;
- batch IDs;
- task-template IDs;
- creation activity records;
- compatibility with the ordinary Work Queue interface.

The weekend employee-ID work is therefore not an isolated UI improvement. It satisfies one of the prerequisites for bulk task assignment.

---

# 7. A major semantic correction: Work Queue is not the system

Saturday-era documentation still contained app-centered language that could call Work Queue itself a project. The weekend's later architecture clarified that this was historically understandable but semantically incomplete.

The canonical direction became:

```text
Task Assignment and Tracking
    = durable operational system

Work Queue
    = principal digital application implementing part of that system
```

This distinction matters because the real operational system includes work that may never enter Work Queue at all.

A task can originate from:

- a supervisor instruction;
- ordinary departmental paperwork;
- a verbal report;
- a nurse or technician request;
- an observation;
- an email;
- a digital form;
- a Work Queue action.

The system is therefore not created by the software. The software models and assists the system.

The weekend did not erase the older app-centered README. Instead, the evolving documentation model treats it as bootstrap-era or transitional evidence and links it forward into the more mature system-centered architecture.

---

# 8. Sunday, August 9 — the Resource Registry emerges

Sunday's Documentation work began from a practical annoyance: too many important URLs and resource locations had to be rediscovered repeatedly.

## 8.1 First form: a shortcut table

The initial Google Sheet was essentially a convenient list of useful links:

- Apps Script projects;
- Google Sheets;
- Google Docs;
- GitHub pages;
- tools;
- data;
- documentation resources.

That alone would have been useful, but the table quickly became something more structural.

## 8.2 Stable `RES-###` identity

Resources were assigned durable IDs such as:

```text
RES-000
RES-001
...
RES-040
...
RES-043
```

The key conceptual distinction became:

```text
resource identity != resource location
```

A resource may retain its conceptual identity even if:

- a web-app deployment URL changes;
- a Google Sheet is replaced;
- a file moves;
- a GitHub path changes;
- a new canonical publication supersedes an older location;
- a resource migrates between services.

This means a workflow or document can refer to the resource by stable ID while the Registry resolves its current location.

## 8.3 Registry fields

The Resources sheet developed fields such as:

- Resource ID;
- name;
- project reference;
- link/current location;
- description;
- metadata reference;
- last update.

The Registry became a **routing and discovery authority**, not merely a bookmark list.

## 8.4 Resource Registry identity itself

By the time the Meadows high-level document was reconciled, the Klinswork Resource Registry itself was identified as:

```text
RES-043 — Klinswork Resource Registry
```

Earlier August 9 work also registered a related bound Apps Script project as `RES-040`; these are distinct resources and should not be confused.

---

# 9. Activities: provenance for resource changes

Once resource identity was separated from resource location, a second problem became obvious.

Suppose a resource's URL changes.

Simply replacing the link tells us the current answer but destroys the history:

```text
old URL
    overwritten by
new URL
```

The system instead needs to know that **a change happened**.

## 9.1 Activities tab

The Resource Registry therefore gained an `Activities` tab.

An Activity can record:

- an activity ID;
- timestamp;
- affected Resource ID;
- action;
- explanatory note.

This permits Registry changes to preserve context such as:

- why a deployment changed;
- which version superseded another;
- whether a resource was migrated or replaced;
- what work session produced the change;
- whether the conceptual resource stayed the same;
- whether a resource was deprecated or retired;
- what evidence supported the update;
- what other resources were affected.

## 9.2 `LAST UPDATE` derived from evidence

Rather than treating `LAST UPDATE` as an independently typed fact, the model connects it to Activity history.

Conceptually:

```text
resource activity history
        ↓
latest relevant activity timestamp
        ↓
Resources.LAST UPDATE
```

This makes the date evidence-based.

## 9.3 Broader significance

This was the point at which the Registry stopped being simply an index and became part of the historical record.

The same principle appears elsewhere in Klinswork:

- task activity records explain task state;
- inventory events explain quantity state;
- holder events explain service state;
- Registry Activities explain resource state.

In each case, **state becomes more trustworthy when the transition history is preserved**.

---

# 10. `RES-000 — CHATGPT — READ THIS FIRST`

The Resource Registry itself created another bootstrapping problem.

A fresh ChatGPT conversation could be given the Registry and still not know:

- what Klinswork means;
- what the Documentation repository is;
- how Resource IDs should be interpreted;
- which files are authoritative;
- which entries are historical versus current;
- what should be read before acting.

The solution was to make the first Registry entry conspicuous:

```text
RES-000 — CHATGPT — READ THIS FIRST
```

Its metadata reference points to the root Documentation README.

This creates a deliberate division of labor:

```text
README
    = orientation and meaning

Resource Registry
    = identity, location, discovery, and routing
```

The Registry therefore contains the breadcrumb required to understand how to use the Registry.

That is an early form of system self-description.

---

# 11. Startup architecture

Sunday's work then formalized the broader procedure implied by `RES-000`.

## 11.1 `Startup` versus `startup()`

A dedicated `Startup` tab was created in the Registry.

The emerging naming convention was:

```text
Startup
    = canonical documented procedure

startup()
    = conversational shorthand meaning “execute Startup”
```

The table itself was intentionally not rushed to completion. Its semantics were discussed before its final structure was committed.

## 11.2 Automatic bootstrap path

The intended route became:

```text
fresh Documentation conversation
        ↓
Resource Registry supplied
        ↓
RES-000 — CHATGPT — READ THIS FIRST
        ↓
root Documentation README
        ↓
return to Registry with orientation established
        ↓
Startup
        ↓
current workflow
```

An explicit fallback exists:

```text
user: startup()
        ↓
execute Startup
```

## 11.3 Startup must remain small

One of the most important design decisions was **what Startup should not do**.

Startup should not preload:

- every project file;
- every work update;
- every Sheet;
- every application document;
- every historical record;
- every sidecar;
- the entire repository.

Instead:

```text
startup context
    = enough durable information to intelligently begin

session context
    = enough information to perform this particular body of work
```

This preserves the progressive context-loading principle established on August 1.

---

# 12. Workflow declares context; Registry resolves it

The Startup work led to one of the weekend's central architectural statements:

```text
Startup
    establishes orientation and routing authorities

Workflow
    declares what context the current work requires

Resource Registry
    resolves those requirements to actual resources
```

This replaces an older assumption that a workflow should simply hard-code a fixed family of project files.

## 12.1 Context requirements become semantic

A workflow should be able to say things like:

```text
Need the current Work Queue technical implementation context.
Need the authoritative employee dataset.
Need the current Documentation workflow specification.
Need the system-level Inventory Management record.
Need the historical work update that established a specific integration.
```

Those statements describe **what information is required**, not where it happens to be stored.

The Registry can then resolve the requirement to one or more Resource IDs and current authoritative locations.

## 12.2 Why this matters

Hard-coded paths do not scale because:

- resources move;
- deployments change;
- project structure evolves;
- some resources are shared;
- one project may require a different context family than another;
- the same workflow may run against different systems.

Semantic context requirements plus stable resource IDs make the workflow more portable and durable.

---

# 13. Project files were not abandoned; their prerequisites were discovered

The August 1 bootstrap had identified formal project files as the next major milestone.

Sunday's work did not reverse that conclusion.

Instead, it asked a more basic question:

> How can authoritative project records be created reliably if the system does not yet have a dependable way to identify, locate, and interpret the resources from which those records must be built?

The answer was that several prerequisites had to exist first:

- reliable resource identity;
- resource-location resolution;
- repository orientation;
- provenance;
- semantic context routing;
- controlled terminology;
- a repeatable Startup path.

Thus the project-file milestone was **reframed, not discarded**.

The formal Project Registry was intentionally deferred until the high-level project and system documents had been sufficiently reconciled.

---

# 14. Project → System → Application / Implementation → Resource

The weekend produced a more mature Klinswork ontology.

## 14.1 Project

A **Project** is a substantial organized body of work containing one or more systems, implementations, resources, histories, and objectives.

Current example:

```text
Housekeeping Operations
```

## 14.2 Operational environment

An **Operational Environment** is the real-world setting in which a project or system operates.

Current example:

```text
Meadows Housekeeping
```

This is an important refinement. Meadows Housekeeping is not simply another software project. It is the real environment that supplies the people, work, rooms, schedules, supplies, requests, observations, and history represented by Housekeeping Operations.

## 14.3 System

A **System** is a durable real-world operational function or management process that exists independently of any one digital implementation.

Current examples:

- Inventory Management;
- Scheduling;
- Task Assignment and Tracking;
- Employee Achievements, provisionally.

## 14.4 Application / implementation

An **Application** is a digital implementation that models, records, presents, or assists part of a system.

Examples:

```text
Work Queue
Inventory 3.0
Calendar tools
roster displays
```

An application is not automatically the project or system.

## 14.5 Resource

A **Resource** is an identifiable artifact or service used by projects and systems.

Examples include:

- a Google Sheet;
- an Apps Script project;
- a Google Doc;
- an HTML viewer;
- a JSON sidecar;
- a repository location;
- a dataset;
- a template;
- a catalog;
- a deployment;
- an image manifest.

## 14.6 Shared resource

A shared resource can support multiple systems or projects without being owned exclusively by any one of them.

Examples include:

- Email Composer;
- employee and role data;
- shared Locations data;
- repository infrastructure;
- common identifiers;
- import/export methods.

The resulting working hierarchy is:

```text
Project
    ↓
System
    ↓
Application / Implementation
    ↓
Resource
```

with shared resources allowed to cross the tree.

---

# 15. Meadows Housekeeping Projects Summary — major weekend artifact

The linked Google Doc, **Meadows Housekeeping Projects Summary**, is one of the most substantial products of the weekend.

It is not merely an overview page. It is a multi-tab working architecture source that begins to define the Housekeeping Operations domain in human-readable form before final structured records are synthesized.

Its current major tabs include:

- Definitions;
- Housekeeping Operations — Meadows Housekeeping;
- Modeling Principles;
- Project and System Register;
- Inventory Management;
- Scheduling;
- Employee Achievements;
- Task Assignment and Tracking;
- Documentation;
- Shared Resources;
- Historical Eras;
- Open Determinations.

The document describes itself as an **initial structured draft** in the **project/system architecture era**, with authority as a working summary subject to later sidecar formalization.

The Resource Registry already exists; the formal Project Registry does not yet.

---

# 16. Controlled definitions

The Definitions tab establishes vocabulary so later project and system documents can use terms consistently.

Important defined concepts include:

- Klinswork;
- Project;
- Operational Environment;
- System;
- Application;
- Resource;
- Shared Resource;
- Housekeeping Operations;
- Meadows Housekeeping;
- Scheduling;
- Schedule Assignment;
- Task Assignment and Tracking;
- Work Queue;
- Operational Assignment;
- Task;
- Routine Responsibility;
- Special Task;
- Assigned Employee;
- Location;
- Inventory Management;
- Inventory Holder;
- Event;
- Completion;
- Verification;
- Integration;
- Documentation;
- Resource Registry;
- Resource ID;
- Startup;
- Context Requirement;
- Resource Resolution;
- Project Registry;
- Manifest;
- Authority / Source of Truth;
- Historical / Experimental Implementation.

Several distinctions are especially important.

## 16.1 Scheduled employee versus assigned task employee

A person scheduled to an area and a person assigned to a particular task may often be the same individual, but those are different facts with different authorities.

## 16.2 Completion versus verification

Completion records that the work was performed. Verification is a separate act or rule establishing that the claim or state is sufficiently supported.

## 16.3 Task versus routine responsibility

Not every operational responsibility needs its own discrete task record.

A location assignment may imply routine work even when Work Queue contains no individual row for each expected action.

This prevents the digital task table from being mistaken for the entire job.

---

# 17. Housekeeping Operations project definition

The Meadows overview establishes:

```text
Housekeeping Operations
    = parent operational project

Meadows Housekeeping
    = primary current operational environment
```

The project includes real operational systems and digital representations developed to model or support them.

Critically, the real system continues to exist whether or not a Klinswork application is:

- deployed;
- adopted;
- activated;
- completed;
- available.

The project currently contains major systems or capabilities including:

- Inventory Management;
- Scheduling;
- Task Assignment and Tracking;
- Employee Achievements;
- additional systems or capabilities still to be identified.

Documentation is treated separately as a cross-project Klinswork project.

---

# 18. The paperwork parallel and adoption constraint

One of the strongest operational principles documented over the weekend is the **paperwork parallel**.

Klinswork tools for Meadows cannot assume that every employee will use an unofficial digital application.

Institutional authority determines official work methods. Employee adoption cannot simply be compelled by the application developer.

Therefore the real housekeeping process must remain understandable and operable through ordinary channels such as:

- paper forms;
- supervisor records;
- meetings;
- verbal reports;
- published schedules;
- photographs;
- email;
- existing institutional processes.

Digital tools can:

- mirror;
- structure;
- reconcile;
- analyze;
- route;
- preserve;

these records without requiring every information provider to become an application user.

This elevates batch conversion and automation from a convenience to a strategic design principle.

Conceptually:

```text
ordinary institutional record
    paper / verbal / email / observation
                ↓
     capture / scan / transcription
                ↓
          structured record
                ↓
 analysis / routing / reconciliation / history
```

The person who supplied the original information remains the information provider even if someone else—or an automated process—performed the digital conversion.

---

# 19. Information participation is broader than digital participation

The weekend architecture explicitly separates several roles that should not be inferred from one another:

- operational role;
- information-provider role;
- submission channel;
- digital access;
- editorial authority;
- administrative authority.

For example:

- a housekeeping employee can provide a paper count without logging into Inventory 3.0;
- a nurse can report a work need without becoming a Work Queue editor;
- a supervisor can supply information without becoming the author of the project documentation;
- a batch job can create JSON without becoming the information provider;
- ChatGPT can assist with organization or drafting without becoming the owner of the underlying operational facts.

This distinction is important for provenance, privacy, permissions, and accurate authorship.

---

# 20. Capability does not imply activation, adoption, or use

Another major modeling principle is the separation of **what an implementation can do** from **whether it became an operational mechanism**.

Useful implementation states include:

- Proposed;
- Designed;
- Implemented;
- Tested;
- Pilot;
- Available;
- Activated;
- Not activated;
- Suspended;
- Retired.

The represented real-world system and the digital implementation require separate status statements.

The QR Issue Form is the clearest example.

It was:

- designed and implemented;
- used during development/testing;
- briefly used by the supervisor;
- not established as a meaningful sustained customer-facing channel;
- later largely abandoned.

The underlying need for issue intake still exists. The application history should be preserved without falsely describing the QR form as an adopted operational system.

---

# 21. Modeling principles established in the Meadows document

The Modeling Principles tab consolidates thirteen major rules.

## Principle 1 — projects, systems, applications, and resources are different entities

None should be inferred automatically from another.

## Principle 2 — systems mirror independently existing operational functions

Inventory Management exists because real supplies must be received, stored, counted, distributed, and replenished, not because Inventory 3.0 exists.

## Principle 3 — applications are implementations, not automatically projects

One system may have multiple implementations. One implementation may support more than one system.

## Principle 4 — information participation is broader than digital participation

Participation, access, authority, and authorship must remain separate.

## Principle 5 — paper and non-digital sources remain first-class evidence

Structured records should preserve source channel, source provider where known, conversion method, and provenance.

## Principle 6 — capability does not imply activation or use

Implementation state must be recorded separately from represented-system state.

## Principle 7 — Documentation is recursive

The Documentation project includes the method used to determine what the Documentation project is. Versioning prevents this recursion from becoming an infinite loop.

## Principle 8 — bootstrap history must be preserved

Earlier app-centered files should not be rewritten as though the current architecture always existed.

## Principle 9 — relationships may cross project and system boundaries

Shared tools should be registered once and related outward.

## Principle 10 — narrative and structured records have different jobs

Human-readable documents explain meaning and history; Sheets and structured records maintain registries, IDs, statuses, relationships, and machine-readable state.

## Principle 11 — uncertainty should be explicit

A documented provisional position is preferable to false certainty.

## Principle 12 — housekeeping digital systems should preserve a paperwork parallel

The digital implementation augments independently valid operational channels.

## Principle 13 — role-specific views may cross system boundaries without becoming data owners

An employee or supervisor dashboard may assemble information from several systems while each source system remains authoritative for its own facts.

---

# 22. Project and System Register

The weekend produced a working register of current high-level entities.

## 22.1 Inventory Management

Classification:

```text
Operational-management system
```

Parent:

```text
Housekeeping Operations
```

Represented function:

- supply control;
- storage;
- cart inventory;
- distribution;
- replenishment;
- consumption;
- reporting.

Principal implementations include Inventory 3.0, associated Sheets/Apps Script, inventory-holder events, and Work Queue integration.

## 22.2 Scheduling

Classification:

```text
Operational-management system
```

Represented function:

```text
who is expected to be where, at what time, and on what days
```

Principal implementations include Calendar, Klinswork Calendar, roster/schedule displays, and trigger experiments.

## 22.3 Employee Achievements

Classification:

```text
Reporting and evidence system / capability
```

Status:

```text
provisional
```

It represents accomplishment, contribution, training, recognition, and demonstrated-capability records.

## 22.4 Task Assignment and Tracking

Classification:

```text
Operational-management system
```

Represented function:

- work intake;
- assignment;
- communication;
- performance;
- completion;
- reporting;
- verification.

Principal application:

```text
Work Queue
```

Future direction includes user differentiation, sign-in, employee-specific views, and supervisor dashboards.

## 22.5 Documentation

Classification:

```text
Documentation-infrastructure project
```

It remains separate from Housekeeping Operations and supports Klinswork more broadly.

---

# 23. Inventory Management — detailed weekend reconciliation

Inventory Management became the deepest worked example of the new system-record style.

## 23.1 System identity

Inventory Management is explicitly not identical to Inventory 3.0.

The represented system includes the real process by which supplies are:

- identified;
- received;
- stored;
- counted;
- placed on carts;
- distributed;
- replenished;
- consumed;
- requested;
- reported.

Physical supplies, carts, closets, storage rooms, employees, requisitions, shortages, and counts remain real even if the application is unavailable.

## 23.2 System aims

The documented aims include:

- defining products, categories, holders, carts, storage locations, and dispensers;
- recording intake and quantity-changing events;
- distinguishing observed from assumed quantity;
- providing useful cart status;
- supporting paper and digital input;
- preserving reasons and provenance for changes;
- connecting qualifying tasks to exact inventory holders;
- associating chemical products with SDS references;
- supporting personal daily cart checks;
- producing auditable records suitable for later summary or batch import.

## 23.3 Two complementary state models

The weekend documentation made an important distinction between two different inventory concepts.

### Bulk quantity state

Primary stores:

```text
Inventory-3.0 Current Inventory
Inventory Events
```

Question answered:

> How many units are currently at this cart, closet, supply room, or other stock location?

Example:

```text
Cart 01 contains eleven rolls of PAPER-001.
```

### Service-holder state

Primary stores:

```text
Work Queue Locations Data
Inventory_Holders
Inventory_Holder_Events
```

Question answered:

> What is the service condition of this exact dispenser or endpoint?

Example:

```text
TPD-JUNIPER-N-220-RR is Full and Operational.
```

These should not be collapsed. Exact stock quantity and endpoint service state have different identifiers, semantics, update rules, and audit needs.

## 23.4 Verified cross-system event flow

The documented flow is:

```text
1. Work Queue task created from template
2. Template may require compatible holder and product category
3. Task stores Related Holder ID and expected completion state/event
4. Worker starts/completes task
5. Task_Activity records lifecycle
6. Completion creates Inventory_Holder_Event
7. Holder event stores previous/new state, product, task, actor, time, notes
8. Holder-event ID can be written back to the task
9. Future/separate integration may create matching bulk-stock deduction
```

Traceability is bidirectional:

```text
Work Queue task
    → Related Holder ID
        → Inventory Holder

Work Queue task
    → Related Holder Event ID
        → Inventory Holder Event

Inventory Holder Event
    → Related Task ID
        → Work Queue task

Inventory Holder
    → Assigned Product ID
        → Inventory-3.0 Product

Inventory Holder
    → Location ID
        → Shared physical Location
```

This allows the system to reconstruct **why a holder changed state and which work action produced the record**.

## 23.5 Three verified data resources

The Inventory technical review directly identified three major workbooks:

### Inventory-3.0 workbook

Role:

- product catalog;
- SDS references;
- local inventory locations;
- current quantity state;
- inventory event history;
- legacy Inventory 2 archive.

### Work Queue 2.1 Test Data workbook

Role:

- tasks;
- task templates;
- settings;
- task activity history;
- location-to-task mappings;
- explicit task linkage to holder events.

### Work Queue Locations Data workbook

Role:

- shared physical-location hierarchy;
- inventory-holder registry;
- holder-event ledger.

## 23.6 Time-zone issue discovered

A concrete integration risk was documented:

```text
Inventory-3.0 workbook: America/Los_Angeles
Work Queue workbooks:    America/Denver
```

Cross-system timestamps may therefore differ by one hour if not normalized.

This is an excellent example of why high-level documentation must eventually connect to verified lower-level technical resources.

## 23.7 Holder capacity uncertainty preserved

Earlier conversation history had described a toilet-paper dispenser holding four rolls. Verified holder records examined later often represented capacities such as one roll, one bundle, or one refill.

Instead of silently correcting one record with the other, the weekend document preserved the discrepancy as unresolved historical modeling until the specific holder/test configuration can be identified.

That is exactly the kind of historical discipline the new architecture is intended to enforce.

---

# 24. Scheduling — boundary clarified

Scheduling had previously risked absorbing too much.

The weekend produced a clearer boundary:

```text
Scheduling
    owns who / where / when / day

Task Assignment and Tracking
    owns what the work means, its status, performance, completion, and history
```

Scheduling may provide:

- date;
- time window;
- employee;
- location;
- recurring trigger;
- availability;
- substitution;
- same-day change.

But a recurring maintenance job or corrective task is not automatically “Scheduling” merely because it happens on a date.

This distinction resolves one of the current open determinations in favor of a clearer separation of temporal assignment from work semantics.

---

# 25. Employee Achievements — provisional but important

Employee Achievements remains less settled than Inventory, Scheduling, or Task Assignment.

Its current purpose is to preserve evidence concerning:

- accomplishments;
- completed initiatives;
- training;
- contributions;
- improvements;
- demonstrated capabilities;
- recognition.

Potential evidence sources include:

- employees;
- supervisors;
- task-completion records;
- training records;
- work updates;
- emails and reports;
- photographs;
- tools and applications created;
- operational observations;
- appropriately documented feedback.

A future employee-specific view could assemble achievement evidence, work history, completed tasks, training, and supporting artifacts after authentication and user differentiation are established.

The documentation carefully avoids claiming that this is an official performance-appraisal system.

---

# 26. Task Assignment and Tracking — high-level system record

The weekend's Meadows document gives Task Assignment and Tracking a system-level definition distinct from Work Queue.

## 26.1 Represented system

It includes:

- intake;
- assignment;
- communication;
- performance;
- completion;
- reporting;
- verification;
- task history;
- inventory-related downstream effects.

It covers ordinary paper and verbal practices as well as digital implementations.

## 26.2 Operational scope

Examples include:

- daily assignments;
- special assignments;
- recurring work;
- corrective work;
- client-reported issues;
- assignment to employee, role, unit, or queue;
- due dates and priorities;
- status changes;
- completion reporting;
- verification/auditing;
- task-related inventory events;
- reassignment history.

## 26.3 Work Queue role

Work Queue is the principal digital application.

The current high-level record recognizes capabilities such as:

- task creation;
- stable employee assignment;
- location relationships;
- activity history;
- status and completion;
- verified downstream inventory-holder integration.

A separate technical/ecosystem manual is intentionally used for deeper implementation detail so the high-level system record does not become another giant code manual.

## 26.4 Future role-specific views

The planned architecture is:

```text
identity / sign-in
        ↓
role differentiation
        ↓
employee view / supervisor view
```

An employee view may surface:

- assignments;
- relevant work history;
- completion records;
- achievement evidence.

A supervisor view may assemble:

- assignments;
- completion;
- verification;
- coverage;
- reporting;
- cross-system status.

The presentation layer does not become the owner of the underlying facts.

---

# 27. Documentation as a separate recursive Klinswork project

The Meadows document includes a dedicated Documentation tab because Documentation is not simply a support folder inside Housekeeping Operations.

It is a separate Klinswork project.

## 27.1 Represented Documentation system

Documentation encompasses:

- creation;
- organization;
- description;
- validation;
- publication;
- retrieval;
- context routing;
- preservation.

It operates on information about:

- projects;
- systems;
- applications;
- decisions;
- histories;
- methods;
- artifacts.

Housekeeping Operations is a major current subject, but Documentation is not limited to Meadows.

## 27.2 Documentation aims

The project aims to:

- define projects, systems, environments, resources, and relationships;
- preserve bootstrap history honestly;
- establish stable identifiers;
- maintain human-readable narrative and machine-readable companions;
- publish navigable HTML;
- connect documents to evidence and project state;
- provide local and online viewers;
- generate catalogs and manifests;
- record the methodology used to create the documentation itself;
- make recursion finite through versioning and provenance.

## 27.3 Recursive methodology

The Documentation project includes the method used to determine what the Documentation project is.

The solution is versioned methodology.

A methodology version should say:

- which rules it applies;
- which records it produced;
- which earlier assumptions it reviewed;
- which records it supersedes;
- which bootstrap artifacts it preserves;
- which questions remain open.

A record created under Method v1 can later become evidence reviewed by Method v2.

---

# 28. Documentation repository architecture

The Documentation tab and root README together clarify the repository's current major area:

```text
documents/work-update-catalog/
```

Known structural elements include:

- `catalogs/`;
- `projects/`;
- `sidecars/`;
- `summaries/`;
- `archived/`;
- `json-manifest.json`;
- `manifest.py`;
- `pst-viewer.html`;
- local JSON viewer tools;
- bootstrap-era project/application material.

The repository structure itself is treated as an artifact of the Documentation project rather than a neutral accident.

---

# 29. Document families clarified

The weekend consolidated a family model in which different artifact types have different jobs.

## Work updates

Human-readable reports of performed work, decisions, current state, and outcomes.

## Work-update sidecars

Structured companions describing identity, sections, projects, topics, dates, relationships, sources, and metadata.

## Summaries

Human-readable consolidation of sessions, project histories, or document meaning.

## Summary sidecars

Structured companions to summaries.

## HTML documents

Published browser-readable renderings.

## Markdown master documents

Editable authoritative human-readable sources where Markdown is chosen as the source format, including study-guide work.

## Project and system records

Structured descriptions of durable entities: identity, environment, aims, methods, actors, channels, applications, data, resources, timeline, status, relationships, authority, and open determinations.

## Catalogs

Discovery records for document families, projects, systems, resources, and metadata.

## Rulesets

Controlled terms, validation requirements, identifier rules, relationship rules, and generation expectations.

## Templates

Reusable structures for sidecars, records, catalogs, Markdown, and HTML.

## Manifests

Machine-generated physical inventories of available records/resources.

## Viewers

Interfaces for interpreting those structured records.

This family model is one of the main ways the repository becomes intelligible rather than merely populated.

---

# 30. Current Documentation context-routing sequence

The Meadows document records the current intended route explicitly:

```text
RES-000 — CHATGPT — READ THIS FIRST
        ↓
root Documentation README
        ↓
RES-043 — Klinswork Resource Registry
        ↓
Startup
        ↓
current workflow
        ↓
workflow-declared context requirements
        ↓
Registry-resolved authoritative resources
```

This is perhaps the single clearest expression of the weekend's architectural outcome.

---

# 31. `RES-040` — controlled Registry write layer remains unimplemented

During the Registry work, a bound Apps Script project was created and registered as:

```text
RES-040 — Resource Registry Apps Script trigger
```

The name initially created ambiguity because no actual trigger had yet been implemented.

The record was corrected to preserve current truth:

```text
bound Apps Script project: exists
code: none
trigger function: none
installable trigger: none
deployment: none
```

The intended future role is a controlled write path that can:

```text
submit Registry change
        ↓
validate
        ↓
update Resources
        ↓
append Activity record
        ↓
LAST UPDATE follows Activity history
```

This is still an open implementation item.

---

# 32. Workflow reconciliation

The existing Documentation workflow was reviewed against the new architecture.

Its main lifecycle remained sound:

- establish intent;
- plan;
- implement;
- test;
- preserve discoveries;
- interpret results;
- reconcile current truth;
- generate documentation;
- publish;
- communicate;
- close.

The problem was primarily the **front end**.

Older workflow assumptions expected relatively fixed project/integration context to be loaded up front.

The weekend replaced that assumption with:

```text
Startup first
        ↓
workflow declares what it needs
        ↓
Registry resolves resources dynamically
```

Thus the workflow was not discarded. Its entry/context model required revision.

---

# 33. Honest reconstruction of an undeclared work session

The August 9 session did not begin as a formally declared Documentation workflow run.

It began as practical context building and resource organization.

Then it produced substantial architecture.

Rather than pretending the architecture had been planned before it was discovered, the session established a new principle:

```text
work already performed before formalization
    must remain distinguishable from
remaining work intentionally planned afterward
```

This is an important capability for real work because not every significant discovery announces itself in advance as “a formal project run.”

The record should be able to say:

- when the work started;
- when it became formal;
- what was reconstructed afterward;
- what was actually planned prospectively;
- what evidence supports the reconstruction.

---

# 34. Workflow-run sidecar 3.1 draft

By the time of this comprehensive synthesis, a substantial new artifact exists:

```text
workflow-run-sidecar-template-3.1-draft.json
```

This represents a further advance beyond the August 9 summary's earlier statement that the existing plan/run templates needed revision.

## 34.1 Run identity

The template can represent:

- Documentation run ID;
- work-session ID;
- run title/date/type;
- entry mode;
- formalization point;
- current step and state;
- next required action.

Allowed entry modes include:

- declared before work;
- reconstructed during work;
- reconstructed after work;
- resumed existing run.

## 34.2 Startup context

The template contains a dedicated `startupContext` structure for:

- Startup applicability;
- startup mode;
- Registry Resource ID;
- bootstrap resource;
- orientation resource;
- Startup tab/version;
- resources initially supplied;
- observed Startup sequence;
- Startup postconditions;
- exceptions.

This directly encodes the weekend's new bootstrap architecture.

## 34.3 Work context and Registry resolution

`workContext` can represent:

- candidate work;
- project placement;
- systems;
- applications;
- resources;
- shared foundations;
- relationships;
- required context;
- resolved resources;
- context gaps.

Each required context item can record that its resolution method is the Resource Registry and preserve the resolved Resource IDs.

## 34.4 Work coverage

The template can distinguish:

- start/end;
- coverage type;
- coverage confidence;
- pre-formalization work;
- formalization timestamp;
- reconstruction basis;
- continuation relationship to prior work.

## 34.5 Intention

The `intention` block can distinguish:

- approved-before-work baseline;
- draft-before-work baseline;
- retroactively reconstructed intention;
- missing intention with explicit exception.

This prevents reconstructed history from being mislabeled as a prospective plan.

## 34.6 Execution history

The template contains structured support for:

- workflow steps;
- chronology;
- decisions;
- discoveries;
- evidence;
- exceptions.

This allows the run record to preserve not just final state but how understanding changed.

## 34.7 Interpretation and reconciliation

Separate structures represent:

- project delta;
- system delta;
- application delta;
- resource delta;
- relationship delta;
- authority delta;
- historical interpretation;
- project/system/resource updates;
- repository documentation updates;
- preserved prior state.

## 34.8 Audience views

The template preserves general, technical, and supervisor-oriented views.

This continues the August 1 insight that different audiences need different slices of the same underlying work.

## 34.9 Publication and closure

The template can track:

- summary;
- HTML;
- document sidecar;
- catalog;
- image;
- portal;
- communication;
- closure.

Thus the work session can be represented through completion rather than ending at implementation.

## 34.10 Workflow evaluation

The run can evaluate whether:

- Startup worked;
- context resolution worked;
- intention handling worked;
- execution worked;
- documentation worked.

This turns the workflow itself into an inspectable and improvable system.

## 34.11 3.2 roadmap

The 3.1 draft also records planned 3.2 capabilities such as:

- formal workflow-specification-to-run validation;
- Registry resource-resolution validation;
- automatic step-transition derivation;
- workflow-run catalog linkage;
- machine-checkable Startup/workflow postconditions.

The exact long-term relationship between this workflow-run profile and the earlier implementation-plan sidecar family still warrants formal reconciliation rather than assumption.

---

# 35. Shared resources architecture

The weekend explicitly rejected the idea that every useful resource must belong to exactly one project or system.

Examples of shared resources include:

## Email Composer

Referenced as:

```text
RES-006
Templates: RES-007
```

Potential relationships include:

- requisition communication;
- task communication;
- work updates;
- Documentation;
- general communication.

## Klinswork Tools page

Referenced as:

```text
RES-001
```

It is a user-facing catalog of applications, not the authority defining project ontology.

## Locations data and viewers

The shared Locations workbook and related resources provide canonical place identifiers for units, rooms, storage areas, dispensers, door-jamb references, and other operational entities.

A location can be represented once while having different enablement states for:

- Work Queue;
- Inventory;
- Calendar.

## Employee and role records

The Work Queue Employees dataset currently participates in assignment, but the canonical shared employee authority remains to be finalized.

Employee identity should support:

- scheduling;
- task assignment;
- information-provider relationships;
- achievement records;
- role-specific views.

## Common identifiers and vocabulary

Stable names/IDs are needed for:

- projects;
- systems;
- environments;
- applications;
- resources;
- documents;
- actors;
- events;
- statuses;
- methods;
- templates;
- catalogs;
- relationships.

## Repository and publishing infrastructure

GitHub, GitHub Pages, viewers, manifests, common templates, and related publication infrastructure may serve many projects.

The governing rule is:

```text
register shared resource once
        ↓
assign stable Resource ID
        ↓
relate it to every supported project/system
        ↓
let the Registry resolve current location
```

---

# 36. Historical eras — preserving how the architecture evolved

The Meadows document does not treat the current architecture as if it always existed.

It defines overlapping historical eras.

## 36.1 Bootstrap era

Characteristics:

- app-centered names;
- informal project tracking;
- standalone HTML documents;
- early repository structure;
- incomplete/inconsistent sidecars;
- important evidence that must be preserved.

## 36.2 Application-development era

Characteristics:

- active building of Inventory, Scheduling, Work Queue, issue reporting, communication, and documentation tools;
- Google Sheets and Apps Script implementations;
- rapid iteration;
- personal testing and limited participation;
- operational concepts discovered through software design.

## 36.3 Documentation-consolidation era

Characteristics:

- work updates;
- navigation;
- sidecars;
- summaries;
- catalogs;
- manifests;
- viewers;
- GitHub Pages;
- recognition that Documentation itself required documentation.

## 36.4 Formal-domain transitional era

An intermediate August 2026 model introduced useful distinctions among domains, represented systems, projects, implementations, information providers, deployment states, and records, but still promoted some operational systems to project status.

This stage is preserved historically rather than hidden.

## 36.5 Project/system architecture era

The current model distinguishes:

- Project;
- Operational Environment;
- System;
- Application / Implementation;
- Resource.

Housekeeping Operations becomes the parent project. Meadows Housekeeping becomes the operational environment. Inventory Management, Scheduling, and Task Assignment and Tracking become systems. Work Queue and Inventory 3.0 become applications.

This is a major conceptual consolidation of the weekend.

---

# 37. Open determinations become a first-class record

Another important advance is the decision not to force premature answers.

The Meadows document includes an **Open Determinations** tab intended to become a live decision register.

Each determination should eventually preserve:

- Determination ID;
- question;
- affected entities;
- current working position;
- alternatives;
- evidence needed;
- owner/reviewer;
- status;
- date opened;
- date resolved;
- resolution;
- resulting changes;
- superseded decision where applicable.

Current open areas include:

## Identifier architecture

- permanent ID formats;
- whether both opaque IDs and human-readable slugs are needed;
- versioning/permanence rules.

## Project/system boundaries

- exact Employee Achievements boundary;
- future issue-reporting classification;
- Safety/Chemical Information boundary;
- Communication and Reporting boundary.

## Participation and provenance

- standard representation of non-digital information providers;
- batch-import provenance;
- author/editor/contributor/source-provider/generator distinctions.

## Status and deployment

- canonical lifecycle vocabulary;
- evidence required for labels such as activated, adopted, suspended, or retired.

## Documentation architecture

- project/system JSON schema;
- template migration;
- authority order among Docs, Sheets, GitHub JSON, Markdown, HTML;
- sidecar relationships;
- catalog numbering;
- viewer/schema compatibility;
- methodology-version records.

## Inventory

- units of measure;
- audit rules;
- matched transfer events;
- requisition boundary;
- SDS relationship;
- authoritative Inventory 3.0 files.

## Scheduling

- schedule assignments versus routine responsibilities versus discrete tasks;
- recurring-maintenance representation;
- substitution/change history.

## Employee Achievements

- evidence quality;
- privacy/publication;
- relationship to official performance systems and personal work-profile material.

This explicit uncertainty register prevents “architecture by accidental assumption.”

---

# 38. Weekend-created self-awareness of the repository

A recurring phrase in the August 9 summary is that the repository was already physically mature; what it lacked was **self-awareness**.

That can now be described as a stack of complementary authorities:

```text
repository-tree.txt
    answers: What physically exists?

README.md
    answers: What environment is this?

Resource Registry
    answers: What resource is this, and where is it now?

Project/System documentation
    answers: What does the thing mean?

Workflow
    answers: What process should occur?

Sidecars/Catalogs
    answer: How is this document/record described and discovered?

Startup
    answers: What must a fresh session read first?
```

No single layer has to do every job.

That division of responsibility is one of the weekend's strongest architectural outcomes.

---

# 39. Relationship among human-readable and machine-readable layers

The weekend repeatedly reinforced that a useful system needs both narrative and structure.

## Human-readable architecture documents

Best for:

- meaning;
- explanation;
- boundaries;
- rationale;
- history;
- unresolved questions;
- conceptual relationships.

## Google Sheets / working registries

Best for:

- current IDs;
- structured relationships;
- statuses;
- activity ledgers;
- current operational rows;
- sortable/filterable state.

## GitHub structured records

Best for:

- versioned JSON;
- Markdown;
- HTML;
- catalogs;
- rulesets;
- templates;
- manifests;
- viewer source;
- historical snapshots.

## Original evidence

Examples:

- work updates;
- emails;
- screenshots;
- paper records;
- application data;
- photos;
- observations.

These remain evidence from which later canonical records can be derived.

---

# 40. The viewer/editor idea becomes more plausible

A major consequence of the Registry work was the realization that once the highest-level document for each resource or project is established, the Registry can become the foundation of a much richer viewer/editor.

The emerging interaction model is approximately:

```text
Registry entry
    ↓
identity + description + metadata reference
    ↓
high-level project/system document
    ↓
related resources resolved as needed
    ↓
structured project/system record
    ↓
viewer presents the relevant slice
```

The user no longer has to manually explain every link at the beginning of each session.

The system can traverse the graph selectively.

This is why the Resource Registry became more consequential than a bookmark sheet.

---

# 41. A new intended way to begin future work

The weekend produced a concrete long-term working habit:

> Do not begin substantial Klinswork work by manually reconstructing the environment from memory. Begin from the Registry/Startup structure and let the workflow obtain only the context required for the current task.

The ideal future interaction is therefore:

```text
User supplies Resource Registry / invokes startup()
        ↓
ChatGPT orients through RES-000 and README
        ↓
Startup establishes routing authorities
        ↓
Current workflow identifies needed context
        ↓
Registry resolves specific resources
        ↓
Only those resources are loaded deeply
        ↓
work begins
```

This is a direct answer to the long-standing problem of losing context across conversations.

---

# 42. Concrete capabilities gained during the weekend

By the end of the weekend, the system could conceptually support all of the following more clearly than before:

- stable resource identity independent of URL;
- centralized discovery of Klinswork resources;
- metadata routing from Registry entries;
- provenance for resource changes;
- activity-derived update dates;
- read-first orientation for a context-naive model;
- progressive Startup rather than universal preload;
- workflow-declared context requirements;
- Registry-based context resolution;
- stronger project/system/application/resource classification;
- explicit operational environments;
- shared-resource relationships;
- preservation of bootstrap history;
- explicit uncertainty/open determinations;
- paper/non-digital provenance;
- separate represented-system and implementation status;
- local and online structured viewing;
- specialized viewer families;
- structured workflow-run representation;
- reconstructed work sessions without false prospective planning;
- stable employee identity in Work Queue tasks;
- stronger foundation for employee-based bulk assignment;
- deeper inventory/task traceability;
- a high-level Meadows Housekeeping orientation document;
- stronger foundations for formal Project Registry creation.

---

# 43. Artifacts materially created, expanded, or clarified

The weekend's artifact family includes at least the following.

## Documentation architecture

- root `README.md`;
- August 9 Resource Registry / Startup work summary;
- Resource Registry Google Sheet;
- `Resources` tab;
- `Activities` tab;
- `Startup` tab;
- `RES-000 — CHATGPT — READ THIS FIRST`;
- `RES-043 — Klinswork Resource Registry`;
- `RES-040` bound Apps Script project reserved for controlled Registry writes;
- repository tree / tree-generator concept;
- planned `repository-manifest.json` concept.

## Workflow / metadata

- existing Documentation workflow reviewed and targeted for front-end revision;
- sidecar-profile distinctions reestablished;
- workflow-run sidecar 3.1 draft;
- planned 3.2 validation/transition features;
- clearer distinction among workflow specification, workflow run, implementation plan, summary, HTML publication, and work-update sidecar.

## Meadows / Housekeeping Operations

- Meadows Housekeeping Projects Summary;
- Definitions tab;
- Housekeeping Operations overview;
- Modeling Principles;
- Project and System Register;
- Inventory Management system draft;
- Scheduling system draft;
- Employee Achievements draft;
- Task Assignment and Tracking system draft;
- Documentation project draft;
- Shared Resources draft;
- Historical Eras model;
- Open Determinations register.

## Work Queue

- `Assigned Employee ID` schema support;
- employee-ID validation and assignment logic;
- employee assignment UI work;
- assignment history event support;
- corrected 2.1 Tasks schema;
- successful employee-assignment test;
- retained Work Queue technical/ecosystem documentation;
- bulk-assignment roadmap context.

## Therapy-document infrastructure

- PST-SP master Markdown progression;
- source-review / toolkit organization;
- CPT/PST-SP/EMDR repository areas;
- sidecar and HTML downstream model;
- specialized PST viewer;
- authoritative-source research and packet-identification work;
- image-placeholder/semantic-description policy.

## Viewer / publication

- local JSON viewer model;
- online static JSON viewer model;
- `json-manifest.json` role;
- `manifest.py` role;
- `pst-viewer.html` as a specialized-view example;
- root landing-page/repository-index direction;
- clarified image-manifest relationship to Email Composer.

---

# 44. Items still incomplete after the weekend

The work was architecturally significant but not finished.

## Startup

Still needed:

- finalize the Startup table;
- cold-start test `startup()` explicitly;
- test the automatic `RES-000` breadcrumb in a genuinely context-naive conversation;
- define machine-checkable Startup postconditions.

## Resource Registry

Still needed:

- implement the `RES-040` controlled write interface;
- verify that one operation can update Resources and append the matching Activity;
- formalize permanence/versioning rules for Resource IDs;
- continue filling high-value metadata references.

## Documentation workflow

Still needed:

- revise the workflow front end around Startup and Registry resolution;
- reconcile workflow-run versus implementation-plan artifact roles;
- add stronger validation;
- test the lifecycle end to end.

## Project/System records

Still needed:

- finalize stable project/system identifiers;
- determine the canonical structured-record schema;
- create formal canonical project/system records;
- synthesize the formal Project Registry after high-level documentation is reconciled.

## Repository semantics

Still needed:

- create `repository-manifest.json` or equivalent semantic map;
- formalize generator/consumer relationships;
- document remaining unknown repository areas;
- define authority precedence where multiple artifacts describe the same fact.

## Viewer/catalog system

Still needed:

- formal viewer/schema compatibility declarations;
- current catalog numbering/supersession rules;
- reconcile online and local viewer version histories;
- continue specialized previews without fragmenting the common data model.

## Work Queue

Still needed:

- continue employee/bulk-assignment architecture;
- implement batch creation against work plans/templates;
- preserve batch/task activity consistency;
- develop authentication/user differentiation before privileged views;
- continue tracing task → holder event → bulk-stock effects.

## Inventory

Still needed:

- resolve time-zone normalization;
- define matched transfer accounting;
- formalize holder-capacity/state/quantity rules;
- define canonical product and location authorities;
- map the Inventory 2 archive;
- inspect Apps Script source through an accessible source/export;
- trace a complete PAPER-001 refill end to end.

## Therapy document projects

Still needed:

- continue source acquisition and authoritative PDF identification;
- complete the PST-SP master guide;
- build/refresh sidecars;
- generate HTML downstream products;
- develop clinician-style fragment assembly and viewing;
- formalize cross-family metadata for CPT/PST-SP/EMDR.

---

# 45. Recommended next review order already implied by the work

The current architecture suggests a sensible order rather than trying to formalize everything simultaneously.

## First — reconcile the highest-level human-readable documents

Continue reviewing:

- Housekeeping Operations;
- Inventory Management;
- Task Assignment and Tracking;
- Scheduling;
- Employee Achievements;
- Documentation;
- shared resources.

These documents should agree on vocabulary and boundaries before their structure is frozen into a formal registry.

## Second — use Inventory and Task Assignment as system exemplars

They already have:

- real-world operations;
- paper and digital inputs;
- structured datasets;
- cross-system relationships;
- tested applications;
- historical records;
- open technical questions.

They are therefore ideal test cases for a canonical system-record schema.

## Third — reconcile Documentation itself

Because Documentation is recursive, its own record should explicitly state the method/version under which it was created.

## Fourth — formalize stable identifiers

Once boundaries are sufficiently clear, assign project/system/document/method identifiers without forcing premature stability.

## Fifth — synthesize the Project Registry

The Project Registry should emerge from reconciled high-level documentation rather than impose a premature ontology on it.

## Sixth — derive structured schemas and sidecars

The machine-readable forms should preserve what the human-readable reconciliation has established.

---

# 46. Architectural interpretation of the weekend

Several deeper conclusions became visible only because the work crossed so many layers at once.

## 46.1 Organization created capability

The Resource Registry began as a convenience list.

Once resources had stable identities, the list could support routing.

Once changes were recorded as Activities, it could support provenance.

Once `RES-000` pointed to the README, it could support bootstrapping.

Once workflows could declare context requirements, it could support dynamic context loading.

The capability was not fully designed first and then implemented. It emerged from progressively better organization.

## 46.2 High-level documents and routing infrastructure need each other

A Registry containing perfect links is not enough if the linked resources do not explain what the project means.

A perfect project overview is not enough if a new work session cannot find it.

The weekend built both ends:

```text
routing infrastructure
    +
high-level semantic documentation
    =
restorable working context
```

## 46.3 Software development revealed the represented systems

Work Queue helped expose the structure of Task Assignment and Tracking.

Inventory 3.0 helped expose the structure of Inventory Management.

But once those systems became visible, the software had to become subordinate to the system definition.

This is a natural maturation from:

```text
“What does this app do?”
```

to:

```text
“What real system are we representing, and which part of it does this app implement?”
```

## 46.4 Repository location is not ontology

A file does not become part of a project merely because it sits in that project's folder.

A shared resource does not become owned by Work Queue merely because Work Queue consumes it.

A tool listed on a common site does not become part of the same project simply because it is nearby in the UI.

Semantic ownership and physical storage are separate dimensions.

## 46.5 History is data

The weekend repeatedly turned historical change into first-class information:

- Registry Activities;
- Task Activity;
- Inventory Events;
- Holder Events;
- historical eras;
- bootstrap artifacts;
- reconstructed workflow sessions;
- supersession and open determinations.

The system increasingly preserves not just *what is true now* but *how the current state came to be true*.

## 46.6 “Current truth” must coexist with historical truth

An app-centered README can be historically authentic even if the current system model has changed.

An earlier four-roll holder description can remain valid historical evidence even when currently inspected records often model a one-roll holder.

An experimental QR form can remain documented without being treated as an adopted operational channel.

The architecture is moving away from destructive correction toward versioned interpretation.

---

# 47. The self-describing-system milestone

The strongest description of the weekend may be that Klinswork began acquiring a **self-describing layer**.

A future session should increasingly be able to answer:

```text
What is this environment?
    → README

What resources exist?
    → Resource Registry

Where is the current resource?
    → Resource Registry

What changed and why?
    → Activities / histories

What should I read first?
    → RES-000 / Startup

What does this project mean?
    → high-level project documentation

What does this system mean?
    → system documentation

What application implements it?
    → application / technical records

What facts are authoritative?
    → authority model + source resources

What does this workflow need?
    → context requirements

Where is that context?
    → Registry resolution

What happened during this run?
    → workflow-run record / summary / evidence
```

The repository is therefore beginning to support a new kind of interaction:

> **The user supplies an entry point; the system explains enough of itself to allow selective navigation instead of requiring the user to reconstruct the whole map manually.**

---

# 48. Relationship to the longer Klinswork trajectory

The weekend also makes earlier work easier to reinterpret.

The sequence is approximately:

```text
Build useful applications
        ↓
Document application work
        ↓
Create sidecars and catalogs
        ↓
Build viewers for the sidecars
        ↓
Notice projects cannot be reconstructed reliably from documents alone
        ↓
Define projects and represented systems
        ↓
Notice project files cannot be built reliably without resource discovery
        ↓
Create Resource Registry and Startup
        ↓
Create high-level semantic project/system documents
        ↓
Use them to synthesize formal structured project/system records
        ↓
Allow viewers and workflows to navigate the structure dynamically
```

Seen this way, the weekend was not a detour into organization.

It was the point at which the earlier application work, documentation work, and metadata work began to converge into a coherent architecture.

---

# 49. Current concise statement of the architecture

If the weekend's results had to be compressed into one working model, it would be this:

```text
KLINSWORK
    organizes projects, systems, applications, documentation, resources, and shared infrastructure.

DOCUMENTATION
    is a separate cross-project Klinswork project responsible for preserving, describing,
    publishing, retrieving, and routing knowledge about the rest of Klinswork and itself.

HOUSEKEEPING OPERATIONS
    is the parent operational project for the Meadows housekeeping work currently modeled.

MEADOWS HOUSEKEEPING
    is the primary current operational environment, not merely an app or project folder.

SYSTEMS
    represent durable real-world functions such as Inventory Management, Scheduling,
    and Task Assignment and Tracking.

APPLICATIONS
    implement portions of systems. Work Queue and Inventory 3.0 are principal examples.

RESOURCES
    are specific identifiable artifacts/services and receive stable RES-### identities when registered.

RESOURCE REGISTRY
    resolves stable identity to current location and preserves resource relationships.

ACTIVITIES
    preserve why Registry state changed.

README
    orients a reader to the repository.

STARTUP
    establishes the minimum durable context and routing authority for a new session.

WORKFLOW
    declares semantic context requirements and governs the work lifecycle.

REGISTRY RESOLUTION
    maps those requirements to current authoritative resources.

HUMAN-READABLE PROJECT/SYSTEM DOCUMENTS
    explain meaning, boundaries, history, and uncertainty.

STRUCTURED RECORDS / SIDECARS / CATALOGS / MANIFESTS
    make the same environment machine-readable and discoverable.

VIEWERS
    present those records locally and online.

HISTORY
    is preserved rather than overwritten when the architecture changes.
```

---

# 50. Final assessment

The weekend produced a large quantity of visible work, but its importance is better measured by the number of **structural dependencies that were resolved**.

Before the weekend, many pieces already existed:

- applications;
- data;
- work updates;
- sidecars;
- catalogs;
- viewers;
- GitHub pages;
- study guides;
- project ideas.

After the weekend, those pieces had a much stronger framework for answering:

- what they are;
- what they belong to;
- what they represent;
- how they relate;
- where they are;
- how their history is preserved;
- how a future conversation finds them;
- how a workflow requests them;
- how their current and historical states remain distinguishable.

The shift can be summarized as:

```text
BEFORE
collection of useful applications, documents, URLs, and files

        ↓

WEEKEND WORK
identity + ontology + provenance + orientation + routing + high-level documentation

        ↓

AFTER
an emerging system that can increasingly explain and navigate its own structure
```

That is why the weekend feels disproportionately significant compared with any one visible application feature.

The employee dropdown in Work Queue was a meaningful functional step. The repository README was a meaningful documentation step. The PST-SP/CPT/EMDR organization was a meaningful document-processing step. The Resource Registry was a meaningful organizational step. The Meadows Housekeeping overview was a meaningful project-modeling step.

But together they did something larger: they established the beginnings of a **common structural language** across Klinswork.

The next phase is no longer “organize everything somehow.”

The next phase is to **use the architecture**:

- finish the highest-level project/system documents;
- validate Startup and context routing;
- formalize project/system records from the reconciled documents;
- continue Resource Registry enrichment;
- build controlled Registry writes;
- exercise the workflow-run model on real sessions;
- develop the Project Registry from evidence rather than assumption;
- allow viewers and future sessions to navigate from stable identities into progressively deeper context.

The weekend therefore marks a credible transition from a body of impressive but partly implicit work into a **durable, inspectable, navigable project environment**.

---

# Appendix A — principal weekend source artifacts

## Direct records

1. `summary-2026-08-09-documentation-resource-registry-startup.md`
   - Detailed historical account of the August 9 Registry and Startup session.

2. Root Documentation `README.md`
   - Human-readable repository orientation and design principles.

3. `workflow-run-sidecar-template-3.1-draft.json`
   - Structured workflow-run model incorporating Startup, resource resolution, reconstructed sessions, execution state, evidence, reconciliation, publication, and evaluation.

4. **Meadows Housekeeping Projects Summary** Google Doc
   - Working high-level project/system architecture source.
   - Includes definitions, system records, modeling principles, shared resources, historical eras, and open determinations.

5. August 1 Documentation bootstrap work update
   - Historical baseline establishing the earlier workflow/document/project model that the weekend extended.

## Supporting retained artifacts

6. Work Queue 2.1 code and HTML files
   - Evidence of `Assigned Employee ID`, employee-ID validation, assignment behavior, and UI work.

7. Work Queue high-level README and technical/ecosystem manual
   - Transitional and deeper application documentation.

8. Work Queue bulk-assignment roadmap
   - Future batch-generation model using employee IDs, templates, locations, batch IDs, and activity records.

9. PST-SP Veteran Study Guide versions
   - Evidence of the Markdown-master and toolkit-based study architecture.

10. PST-SP JSON viewer artifacts/screenshots
    - Evidence of specialized structured-document presentation.

---

# Appendix B — high-value Resource IDs appearing in the weekend architecture

The following IDs appear in the current working documentation and should be verified against the live Registry before being treated as immutable long-term assignments:

| Resource ID | Working meaning |
|---|---|
| `RES-000` | `CHATGPT — READ THIS FIRST` bootstrap entry |
| `RES-001` | Klinswork Tools page |
| `RES-002` | Work Queue application |
| `RES-003` | Work Queue primary data workbook |
| `RES-006` | Email Composer |
| `RES-007` | Email Composer templates |
| `RES-010` | Shared Locations workbook in the current Meadows documentation |
| `RES-011` | Online JSON Viewer in current Documentation references |
| `RES-013` | Work Queue Employees dataset in current working references |
| `RES-014` | Work Queue-related Locations reference in current working documentation |
| `RES-022` | Current working catalog reference noted in the Documentation tab |
| `RES-037` | Repository/publishing infrastructure reference in shared-resource material |
| `RES-040` | Bound Resource Registry Apps Script project reserved for controlled writes |
| `RES-043` | Klinswork Resource Registry |

These assignments reflect the current working records and should remain Registry-resolved rather than copied into code as permanent physical locations.

---

# Appendix C — current high-level entity map

```text
Klinswork
│
├── Project: Documentation
│   │
│   ├── Resource Registry (RES-043)
│   │   ├── Resources
│   │   ├── Activities
│   │   ├── Startup
│   │   ├── RES-000 bootstrap route
│   │   └── RES-040 future controlled-write Apps Script resource
│   │
│   ├── Documentation Repository
│   │   ├── README
│   │   ├── work updates
│   │   ├── summaries
│   │   ├── sidecars
│   │   ├── catalogs
│   │   ├── templates
│   │   ├── manifests
│   │   ├── viewers
│   │   ├── scripts
│   │   └── historical artifacts
│   │
│   ├── Documentation Workflow
│   │   ├── Startup
│   │   ├── context requirements
│   │   ├── Registry resolution
│   │   ├── implementation / execution
│   │   ├── testing / evidence
│   │   ├── reconciliation
│   │   ├── publication
│   │   └── closure / evaluation
│   │
│   └── Therapy / reference document families
│       ├── PST-SP
│       ├── CPT
│       ├── EMDR
│       ├── master Markdown
│       ├── sidecars
│       ├── HTML
│       └── specialized viewers
│
└── Project: Housekeeping Operations
    │
    └── Operational Environment: Meadows Housekeeping
        │
        ├── System: Inventory Management
        │   ├── Inventory 3.0
        │   ├── Products / SDS
        │   ├── Current Inventory / Inventory Events
        │   ├── holders / holder events
        │   └── Work Queue integration
        │
        ├── System: Scheduling
        │   ├── Calendar
        │   ├── Klinswork Calendar
        │   ├── rosters
        │   └── trigger experiments
        │
        ├── System: Task Assignment and Tracking
        │   ├── Work Queue
        │   ├── Tasks
        │   ├── Task Activity
        │   ├── employee assignment
        │   ├── location relationships
        │   └── holder-event integration
        │
        └── System/Capability: Employee Achievements
            ├── work updates
            ├── completion evidence
            ├── training
            ├── contributions
            └── future employee view
```

---

# Appendix D — key unresolved architecture tests

The following tests would provide especially high information value:

1. **Cold-start test**
   - Begin a new context-naive conversation with only the intended Registry entry point.
   - Verify README → Registry → Startup → workflow routing.

2. **Registry controlled-write test**
   - Update one resource through the future `RES-040` interface.
   - Verify Resources update and matching Activity creation.

3. **Workflow-run reconstruction test**
   - Use the 3.1 draft to encode a session that became formal midstream.
   - Verify prospective and reconstructed truth remain distinguishable.

4. **Inventory cross-system trace**
   - Trace a PAPER-001 refill through Work Queue task → Task Activity → holder event → holder state → bulk inventory effect.

5. **Bulk Work Queue assignment test**
   - Generate a batch for one employee and one unit using stable employee ID, valid locations, templates, shared batch ID, and matching creation activities.

6. **Project/system record pilot**
   - Use Inventory Management as the first complete system-record exemplar.
   - Compare the resulting structured record against the human-readable Meadows system tab.

7. **Viewer routing test**
   - Resolve a system from a Registry/project record and open the appropriate high-level document plus specialized structured preview without hard-coded physical paths.

---

# Appendix E — one-sentence weekend conclusion

**During August 8–9, 2026, Klinswork advanced from an increasingly organized collection of applications, documents, and repository artifacts toward an explicit project/system architecture with stable resource identity, provenance, progressive context routing, high-level Meadows Housekeeping system documentation, stronger Work Queue assignment identity, and a Documentation infrastructure capable of increasingly explaining how its own resources should be found, interpreted, and used.**
