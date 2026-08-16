---
document_type: work-implementation-session
record_family: human-readable-execution-record
template: work-implementation-session-template-1.0-draft
template_version: 1.0-draft
session_date: 2026-08-16
session_status: planned
session_entry_mode: declared-before-work
primary_project: Task Assignment and Tracking
target_system: Work Queue
created: 2026-08-15
authority_role: authoritative-human-readable-record-for-one-bounded-work-implementation-session
---

# Work Implementation Session — Task Assignment and Tracking / Work Queue

> **Session date:** August 16, 2026  
> **Session status:** `planned`  
> **Session entry mode:** `declared-before-work`  
> **Primary Project:** Task Assignment and Tracking  
> **Target System:** Work Queue  
> **Primary goal:** Create the initial Task Assignment and Tracking Project Definition and establish Work Queue within it as the principal known System.
>
> **Reference exemplar:** Inventory Management → Inventory 3.0
>
> **Authority boundary:** This document is the authoritative human-readable working record for this bounded implementation session. It records the declared session scope, starting state, context actually resolved, material execution, decisions, deviations, blockers, validation results, resulting state, and closure.
>
> It does **not** replace the governing implementation plan, Project/System records, Resource Registry, Architecture Changelog, Activity Registry, machine-readable workflow/run state, final summary, or Work Update.
>
> **Critical temporal rule:** This session is being declared before implementation begins. Work Queue and its historical implementation already exist. This session must not represent prior Work Queue development as though it were prospectively planned here.

---

# 1. Session Declaration

## 1.1 Session identity

| Field | Value |
|---|---|
| Session title | Task Assignment and Tracking — First Project Definition / Work Queue System Documentation |
| Session date | 2026-08-16 |
| Session status | `planned` |
| Session entry mode | `declared-before-work` |
| Session ID |  |
| Primary Project | Task Assignment and Tracking |
| Project ID |  |
| Target System | Work Queue |
| System ID |  |
| Target Application / Implementation | Existing Work Queue implementation; application boundary to be confirmed from evidence rather than assumed |
| Primary operational environment | Meadows Housekeeping |
| Implementation plan | **Required before session activation; not yet instantiated at session-record creation** |
| Implementation-plan sidecar | **Required if/when the governing implementation plan is instantiated; not yet created** |
| Session record path | To be assigned when repository destination is confirmed |
| Session owner / operator | Klins |

### Session entry mode

`declared-before-work`

### Identity rule

No `PROJ-###`, `SYS-###`, `REL-####`, run ID, or session ID will be invented during this session. Unknown identifiers remain blank until the relevant allocation authority is settled and the identifier is formally assigned.

## 1.2 Session goal

**Goal**

> Create the initial **Task Assignment and Tracking Project Definition** and establish **Work Queue** within it as the principal known **System**, using the completed Inventory Management → Inventory 3.0 Project Definition as the first architectural exemplar while independently verifying what applies to Task Assignment and Tracking / Work Queue.

**Why this session exists**

> August 15 produced the first complete Project Definition exemplar and clarified the distinction among Project, System, Resource, Entity Record, Sidecar, physical location, and authority. The next meaningful test is prospective use: begin with a declared session, resolve only the context required, construct a second Project Definition from evidence, validate it through the current documentation/discovery architecture, and close with an explicit handoff.

**Session boundary**

This session is complete when:

1. Task Assignment and Tracking has an initial Project Definition package;
2. Work Queue is documented within that Project as its principal known System;
3. Project-level and System-level meanings are kept distinct;
4. no unsupported stable IDs or architecture claims are invented;
5. the relevant source-aware documentation/discovery path has been tested;
6. the resulting state and remaining work are explicitly recorded.

This session does **not** include Work Queue feature development, application redesign, datastore refactoring, or broad cleanup of historical records except where a specific historical record is required as evidence for the Project Definition.

---

# 2. Relationship to the Implementation Plan

## 2.1 Governing plan

| Field | Value |
|---|---|
| Plan title | Task Assignment and Tracking Project Definition / Work Queue Documentation Implementation Plan |
| Plan document ID |  |
| Plan path |  |
| Plan status | `required-before-session-activation` |
| Plan planning mode | `prospective` |
| Relevant plan stage(s) | Project Definition construction; Work Queue System documentation; discovery/validation |
| Relevant acceptance criteria | To be linked from the governing plan before execution |
| Relevant planned tests | To be linked from the governing plan before execution |

### Pre-activation gate

**This session remains `planned` until the governing implementation plan is created or an explicit decision is recorded that a separate implementation plan is not required for this bounded work.**

That decision may not be made silently inside execution.

## 2.2 Work selected for this session

The intended work package is:

1. resolve required architecture, Project, System, Resource, and historical context;
2. reconcile the Task Assignment and Tracking / Work Queue semantic boundary;
3. create the Project directory structure;
4. instantiate the Project Identity Entity Record;
5. create the Project-local README;
6. create the Project Summary;
7. create the Project Summary sidecar;
8. create the Work Queue System documentation layer;
9. validate discovery / Viewer behavior;
10. record resulting state, Registry effects, and continuation point.

## 2.3 Work explicitly deferred to later sessions

- [ ] Assignment of a permanent `PROJ-###` identifier.
- [ ] Assignment of a permanent `SYS-###` identifier.
- [ ] Final System Identity Record Profile or `system-identity.json`.
- [ ] Formal Relationship Registry implementation.
- [ ] Broad Work Queue feature development or redesign.
- [ ] Work Queue datastore refactoring.
- [ ] Universal reusable Project Definition template extraction.
- [ ] Exhaustive normalization of all historical Work Queue documents to current terminology.
- [ ] Reclassification of every Work Queue-related Resource unless required to complete the Project Definition safely.

## 2.4 Plan authority rule

The implementation plan remains the authority for the intended body of work once instantiated.

This session record may document execution differences, but it must not silently rewrite the plan.

If execution differs from the plan, record the difference under:

- **Decisions**
- **Deviations**
- **Blockers**
- **Resulting State**

---

# 3. Starting State

> This section records the expected starting state based on the architecture available at session declaration. It must be verified at session start before implementation changes are made.

## 3.1 Current Project state

Task Assignment and Tracking is currently understood as:

```text
Klinswork
└── Operations
    └── Task Assignment and Tracking     [Project]
        └── Work Queue                   [System]
```

Expected current facts:

- Task Assignment and Tracking is recognized semantically as a **Project** representing the real-world operational function of task intake, assignment, communication, performance, status, completion, verification, reporting, and preservation/history.
- Task Assignment and Tracking does not yet have its complete Project Definition package equivalent to the Inventory Management exemplar.
- A permanent Project ID has not been assigned.
- Project identity must remain distinct from folder path, current label, implementation, lifecycle, or environment.

## 3.2 Current System state

Work Queue is currently understood as the principal known **System** within Task Assignment and Tracking.

Expected current facts:

- Work Queue has substantial prior implementation history.
- Work Queue has existing application/data Resources and historical Work Updates.
- Work Queue must not be collapsed into the Project itself.
- Work Queue must not automatically be modeled as merely an Application unless the evidence supports a separate System/Application distinction.
- A permanent System ID has not been assigned.
- A System Identity Entity Record is not required for this first Project Definition pass unless the session discovers a compelling architecture reason to create one.

## 3.3 Current physical repository state

Expected target structure, subject to verification before creation:

```text
documentation/
└── documents/
    └── Klinswork Documentation Viewer/
        └── projects/
            └── operations/
                └── Task Assignment and Tracking/
                    ├── project-identity.json
                    ├── README.md
                    ├── summaries/
                    │   └── project-summary.md
                    ├── sidecars/
                    │   └── project-summary-sidecar.json
                    └── systems/
                        └── Work Queue/
                            ├── README.md
                            ├── summaries/
                            │   └── system-summary.md
                            └── sidecars/
                                └── system-summary-sidecar.json
```

This is a **planned physical expression** of the current semantic model. The repository path does not itself establish Project or System identity.

## 3.4 Prior work relevant to this session

Prior work expected to establish the starting state includes:

- the August 15 ontology reconciliation;
- the first Project Definition exemplar for Inventory Management → Inventory 3.0;
- the Project Identity Record Profile / template;
- Project Summary and System Summary conventions established through the Inventory exemplar;
- source-aware documentation discovery using Common / Projects / Therapy Documentation Spaces;
- Resource Registry reconciliation;
- historical Work Queue design, implementation, testing, Work Updates, and Resources;
- Work Queue 2.1 assignment functionality and earlier Work Queue / Tasker evolution.

None of that prior work becomes “work performed in this session.”

## 3.5 Starting-state uncertainties

- [ ] Verify the current physical repository tree before creating directories.
- [ ] Verify whether a Task Assignment and Tracking directory already exists in any current or historical form.
- [ ] Verify the current Work Queue application/System Resource set in the Resource Registry.
- [ ] Verify whether Work Queue has a current README, architecture summary, roadmap, implementation plan, or other System-level authority that should be used as evidence.
- [ ] Verify whether `Work Queue` is still the correct canonical System name.
- [ ] Verify whether a separate Application/Implementation entity should be represented beneath the Work Queue System.
- [ ] Verify the current discovery behavior for Entity Records under the Projects source.
- [ ] Verify whether Project Registry / Project Identity authority has changed since August 15.

---

# 4. Context Resolution

> The workflow/session declares the context required; the Resource Registry and current repository/documentation evidence resolve those requirements. Do not load the entire Klinswork universe.

## 4.1 Context requirements

| Requirement ID | Required context | Purpose | Authority role | Resolved Resource ID(s) | Status | Notes |
|---|---|---|---|---|---|---|
| CTX-01 | Current Klinswork controlled vocabulary / ontology | Confirm Project, System, Resource, Sidecar, Entity Record, authority, and location semantics | Controlled-vocabulary authority |  | `unresolved` | Resolve current Definitions source at session start |
| CTX-02 | Current architecture changes / open determinations | Detect any changes after August 15 that affect Project Definition work | Architecture-change / unresolved-decision authority |  | `unresolved` | Read only relevant recent entries |
| CTX-03 | Meadows Housekeeping Projects Summary | Confirm Task Assignment and Tracking placement and current architecture narrative | Current architecture/project-summary authority | `RES-042` | `partially-resolved` | Verify Registry row and current document revision |
| CTX-04 | Klinswork Resource Registry | Resolve stable Resource IDs and current locations | Resource identity/routing authority | `RES-043` | `partially-resolved` | Verify current sync/current rows before use |
| CTX-05 | Current Project documentation root | Confirm present physical Project Definition destination | Registered routing / physical-location evidence | `RES-041` | `partially-resolved` | Verify current location before file creation |
| CTX-06 | Project Identity Record Profile / template | Instantiate Task Assignment and Tracking identity correctly | Record Profile construction authority |  | `unresolved` | Resolve current template and profile version |
| CTX-07 | Inventory Management Project Definition | Use first completed exemplar as architectural reference | Exemplar / comparative evidence |  | `unresolved` | Read Project Identity, README, Project Summary, sidecar |
| CTX-08 | Inventory 3.0 System documentation | Use first System documentation exemplar | Exemplar / comparative evidence |  | `unresolved` | Read README, System Summary, sidecar |
| CTX-09 | Current Work Queue implementation Resources | Identify concrete System Resources without guessing | Resource identity / implementation evidence | `RES-002`, `RES-003`, `RES-012`, `RES-013`, `RES-014` | `partially-resolved` | Treat as candidate known IDs; verify every Registry row before asserting current use |
| CTX-10 | Work Queue historical Work Updates and sidecars | Reconstruct System history and distinguish historical evidence from current truth | Historical implementation evidence |  | `unresolved` | Retrieve only relevant milestones |
| CTX-11 | Current Work Queue source / implementation evidence | Determine current verified System/application state | Current implementation authority |  | `unresolved` | Resolve through Registry/current source rather than historical Work Updates alone |
| CTX-12 | Klinswork Documentation Viewer / source-aware discovery | Validate Project/System documentation discovery | Discovery/presentation layer | `RES-011` | `partially-resolved` | Verify current Viewer/resource row and manifest state |

## 4.2 Orientation sources actually loaded

At session declaration, none are treated as freshly loaded for tomorrow's execution.

At session start, mark each item only after it has actually been read/resolved:

- [ ] Controlled vocabulary / Definitions
- [ ] Relevant Architecture Changelog entries
- [ ] Open Determinations affecting Project/System identity
- [ ] Task Assignment and Tracking architecture context
- [ ] Project Identity Record Profile / template
- [ ] Inventory Management `project-identity.json`
- [ ] Inventory Management `README.md`
- [ ] Inventory Management Project Summary
- [ ] Inventory Management Project Summary sidecar
- [ ] Inventory 3.0 README
- [ ] Inventory 3.0 System Summary
- [ ] Inventory 3.0 System Summary sidecar
- [ ] Klinswork Resource Registry
- [ ] Current repository tree / physical-state evidence
- [ ] Current Work Queue Resource rows
- [ ] Relevant Work Queue historical records
- [ ] Current Work Queue implementation evidence
- [ ] Governing implementation plan
- [ ] Relevant workflow specification
- [ ] Relevant recent Activities
- [ ] Other:

## 4.3 Unresolved context

At declaration, the following remain intentionally unresolved until the session starts:

- exact current repository state;
- current Registry locations for relevant Work Queue Resources;
- current Project Identity template revision;
- current source of truth for Work Queue implementation behavior;
- whether a distinct Work Queue Application entity should be represented;
- whether Project Registry / Project Identity authority has been formally resolved;
- whether Entity Record discovery has changed since August 15.

## 4.4 Context-resolution summary

**Current status:** `not-yet-resolved-for-execution`

The session may be declared now, but implementation should not begin until the required architecture and evidence context has been resolved sufficiently to support the Project/System boundary and file construction without guessing.

---

# 5. Session Work Package

| Seq. | Work item | Objective | Deliverable | Dependencies | Exit criterion | Status |
|---:|---|---|---|---|---|---|
| 1 | Startup and context resolution | Establish current authorities, physical state, and evidence boundary | Resolved context table and verified starting state | Governing plan; Registry; current repository tree | Required context is resolved or explicitly marked non-blocking | `not-started` |
| 2 | Semantic reconciliation | Verify Task Assignment and Tracking as Project and Work Queue as System | Written semantic determination in this session record | CTX-01 through CTX-11 | No unresolved evidence contradiction blocks Project Definition | `not-started` |
| 3 | Project directory construction | Create the minimal Project Definition physical structure | `Task Assignment and Tracking/` directory tree | Work item 2 | Required directories exist at verified current destination | `not-started` |
| 4 | Project Identity Entity Record | Instantiate stable intrinsic Project identity without invented ID | `project-identity.json` | Project Identity profile; work item 2 | Record validates against intended profile rules; ID remains blank if unassigned | `not-started` |
| 5 | Project orientation and narrative | Explain Project purpose, scope, boundaries, current state, and authority routing | `README.md`; `summaries/project-summary.md` | Work items 1–4 | Project meaning is understandable without collapsing into Work Queue implementation | `not-started` |
| 6 | Project Summary sidecar | Create machine-readable companion to Project Summary | `sidecars/project-summary-sidecar.json` | Work item 5; current sidecar profile | Companion relationship resolves; sidecar does not act as identity authority | `not-started` |
| 7 | Work Queue System documentation | Establish Work Queue System-local orientation and narrative | `systems/Work Queue/README.md`; `summaries/system-summary.md`; companion sidecar | Work items 1–6; current Work Queue evidence | System meaning/history/current-state boundaries are documented without inventing System Identity | `not-started` |
| 8 | Discovery and validation | Test physical structure, JSON validity, companion resolution, and Viewer discovery | Validation evidence recorded in Section 12 | Work items 3–7 | Required tests pass or failures are explicitly recorded | `not-started` |
| 9 | Registry / architecture effect assessment | Determine Resource/Activity/architecture updates required | Section 14 completed; downstream actions identified | Work items 1–8 | Required Registry/Activity/Changelog work is explicit | `not-started` |
| 10 | Session closure | Establish trustworthy resulting state and handoff | Sections 13–18 completed | All preceding applicable items | Session has explicit closure status and context-naive continuation point | `not-started` |

### Work-item statuses

- `not-started`
- `in-progress`
- `complete`
- `partial`
- `blocked`
- `skipped`

---

# 6. Success Criteria

- [ ] **SC-01 — Project placement:** Task Assignment and Tracking is explicitly represented as a Project under the current Operations architecture.
- [ ] **SC-02 — System placement:** Work Queue is explicitly represented as the principal known System within Task Assignment and Tracking.
- [ ] **SC-03 — Identity discipline:** No permanent Project/System/Relationship/Session/Run identifier is invented.
- [ ] **SC-04 — Project Identity:** `project-identity.json` exists as an Entity Record, not a Sidecar.
- [ ] **SC-05 — Project orientation:** Project README exists and routes readers to the records that own relevant facts.
- [ ] **SC-06 — Project narrative:** Project Summary explains the operational function, scope, boundaries, Work Queue relationship, relevant Resources, evidence classes, and current unresolved questions.
- [ ] **SC-07 — Project companion:** Project Summary sidecar exists and correctly treats the Markdown source as the human-readable document authority.
- [ ] **SC-08 — System orientation:** Work Queue System README exists.
- [ ] **SC-09 — System narrative:** Work Queue System Summary distinguishes System meaning, historical implementation evidence, planning evidence, and current verified implementation state.
- [ ] **SC-10 — System companion:** Work Queue System Summary sidecar exists and resolves correctly.
- [ ] **SC-11 — Physical validation:** Created JSON records parse successfully and expected paths exist.
- [ ] **SC-12 — Discovery validation:** Appropriate Project/System documentation is discoverable through the current source-aware documentation architecture, or any discovery limitation is explicitly captured.
- [ ] **SC-13 — Authority separation:** Project Identity, summaries, sidecars, Registry facts, historical Work Updates, and current implementation evidence retain distinct authority roles.
- [ ] **SC-14 — Cold-start usability:** A context-naive future session can determine what the Project is, what Work Queue is, what records to read, what remains unresolved, and where work should resume.
- [ ] **SC-15 — Closure:** Resulting state, remaining work, downstream records, and exact continuation point are recorded before the session is closed.

## 6.1 Minimum acceptable outcome

The minimum useful result is:

1. semantic placement has been verified;
2. the Task Assignment and Tracking Project directory exists;
3. Project Identity, README, and Project Summary exist;
4. Work Queue has at least its README and System Summary;
5. failures or incomplete sidecars/discovery tests are explicitly recorded rather than hidden;
6. the session closes with a trustworthy continuation point.

A session that discovers a genuine architecture contradiction may also close usefully as `blocked` if the contradiction and required decision are documented clearly.

## 6.2 Non-goals

The following are explicitly outside this session:

- assigning `PROJ-###` or `SYS-###`;
- finalizing the Project Registry / Project Identity authority question;
- designing the final System Identity Record Profile;
- implementing the Relationship Registry;
- adding Work Queue product features;
- changing Work Queue business logic merely because documentation exposes an improvement opportunity;
- redesigning the Work Queue UI;
- migrating or rewriting all historical Work Queue records;
- normalizing every legacy term in historical evidence;
- extracting the universal Project Definition template before the second exemplar has been tested;
- making broad Documentation architecture changes unless a blocking defect is discovered.

---

# 7. Stop / Reassessment Conditions

Stop and reassess if:

- [ ] Evidence contradicts Task Assignment and Tracking being the Project.
- [ ] Evidence contradicts Work Queue being the System.
- [ ] Evidence supports a materially different System/Application boundary than currently expected.
- [ ] A required authority cannot be resolved.
- [ ] A durable ID would have to be invented to continue.
- [ ] The current Project Identity profile is incompatible with the intended record.
- [ ] The physical repository already contains a conflicting Task Assignment and Tracking structure.
- [ ] The work begins expanding into Work Queue feature development.
- [ ] The work begins rewriting historical evidence rather than documenting it.
- [ ] Current Work Queue implementation truth cannot be distinguished from historical/planning evidence.
- [ ] Completing a stage would require prematurely creating System Identity.
- [ ] A Viewer/discovery problem reveals a broader architecture defect that should be handled as separate work.
- [ ] A new architecture decision would materially change the Project Definition pattern.
- [ ] Other:

### Reassessment procedure

If a stop condition is triggered:

1. mark the current work item `blocked` or `partial`;
2. record the triggering evidence;
3. create a Decision, Deviation, or Blocker entry;
4. determine whether the session can continue with a smaller valid scope;
5. if an architecture change is required, record whether an Architecture Changelog entry or Open Determination is needed;
6. if safe continuation is not possible, close the session honestly without treating blocked work as complete.

---

# 8. Live Execution Record

> **Execution has not begun.** The entries below are pre-seeded working slots. Update status and content only when the corresponding material action actually occurs.

---

## Execution Entry — EXE-001

**Work item:** Startup and context resolution  
**Status:** `not-started`  
**Started:**  
**Completed:**  

### Objective

Resolve current authorities, current physical state, governing plan, and the minimum evidence needed for the session.

### Action

> To be recorded during execution.

### Evidence / sources used

- 

### Finding / observation

> 

### Result

> 

### Files / records affected

- This session record only, unless context verification requires no changes.

### Resource IDs affected

- 

### Next action

> Proceed to semantic reconciliation only after required context is sufficient.

---

## Execution Entry — EXE-002

**Work item:** Semantic reconciliation  
**Status:** `not-started`  
**Started:**  
**Completed:**  

### Objective

Verify the Project/System boundary independently from the Inventory exemplar.

### Action

> 

### Evidence / sources used

- 

### Finding / observation

> 

### Result

> 

### Files / records affected

- 

### Resource IDs affected

- 

### Next action

> Create the Project physical structure only if the semantic determination is sufficiently supported.

---

## Execution Entry — EXE-003

**Work item:** Project directory construction  
**Status:** `not-started`  
**Started:**  
**Completed:**  

### Objective

Create the minimal physical structure needed for the Task Assignment and Tracking Project Definition.

### Action

> 

### Evidence / sources used

- verified repository tree;
- verified Project documentation root.

### Finding / observation

> 

### Result

> 

### Files / records affected

- 

### Resource IDs affected

- 

### Next action

> Instantiate Project Identity.

---

## Execution Entry — EXE-004

**Work item:** Project Identity Entity Record  
**Status:** `not-started`  
**Started:**  
**Completed:**  

### Objective

Instantiate the Project Identity Record Profile for Task Assignment and Tracking.

### Action

> 

### Evidence / sources used

- current Project Identity Record Profile;
- current Task Assignment and Tracking architecture evidence.

### Finding / observation

> 

### Result

> 

### Files / records affected

- `project-identity.json`

### Resource IDs affected

- 

### Next action

> Create Project orientation and narrative.

---

## Execution Entry — EXE-005

**Work item:** Project README and Project Summary  
**Status:** `not-started`  
**Started:**  
**Completed:**  

### Objective

Create Project-local orientation and the authoritative human-readable Project narrative.

### Action

> 

### Evidence / sources used

- 

### Finding / observation

> 

### Result

> 

### Files / records affected

- `README.md`
- `summaries/project-summary.md`

### Resource IDs affected

- 

### Next action

> Construct the Project Summary sidecar.

---

## Execution Entry — EXE-006

**Work item:** Project Summary sidecar  
**Status:** `not-started`  
**Started:**  
**Completed:**  

### Objective

Create the machine-readable companion without transferring Project Identity authority into the sidecar.

### Action

> 

### Evidence / sources used

- current relevant Record Profile / template;
- Project Summary.

### Finding / observation

> 

### Result

> 

### Files / records affected

- `sidecars/project-summary-sidecar.json`

### Resource IDs affected

- 

### Next action

> Build the Work Queue System documentation layer.

---

## Execution Entry — EXE-007

**Work item:** Work Queue System documentation  
**Status:** `not-started`  
**Started:**  
**Completed:**  

### Objective

Document Work Queue as a coherent System within Task Assignment and Tracking.

### Action

> 

### Evidence / sources used

- current Work Queue implementation evidence;
- relevant historical Work Queue Work Updates;
- Resource Registry;
- Inventory 3.0 System exemplar.

### Finding / observation

> 

### Result

> 

### Files / records affected

- `systems/Work Queue/README.md`
- `systems/Work Queue/summaries/system-summary.md`
- `systems/Work Queue/sidecars/system-summary-sidecar.json`

### Resource IDs affected

- 

### Next action

> Validate files, companion relationships, and discovery.

---

## Execution Entry — EXE-008

**Work item:** Discovery and validation  
**Status:** `not-started`  
**Started:**  
**Completed:**  

### Objective

Test that the new Project/System documentation is physically valid and usable through current discovery architecture.

### Action

> 

### Evidence / sources used

- current repository tree;
- JSON validation;
- current manifest builder;
- current Klinswork Documentation Viewer.

### Finding / observation

> 

### Result

> 

### Files / records affected

- 

### Resource IDs affected

- 

### Next action

> Assess Registry and architecture effects, then close the session.

---

# 9. Decisions

> No material session decisions have occurred yet.

Use the following block when required.

## Decision — DEC-001

**Status:**  
**Decision:**  

> 

**Reason:**  

> 

**Evidence / basis:**

- 

**Effect on this session:**  

> 

**Effect beyond this session:**  

> 

**Architecture Changelog required:** `yes / no / uncertain`

---

# 10. Deviations

> No material deviations have occurred yet.

Use the following block when required.

## Deviation — DEV-001

**Planned:**  

> 

**Actually done:**  

> 

**Reason:**  

> 

**Impact:**  

> 

**Plan revision required:** `yes / no / uncertain`

---

# 11. Blockers

> No unresolved execution blockers have occurred yet.  
> **Pre-activation prerequisite:** governing implementation plan must be instantiated or explicitly waived by recorded decision.

Use the following block when required.

## Blocker — BLOCK-001

**Blocked work item:**  
**Status:** `open`  

**Cause:**  

> 

**Evidence:**  

- 

**Required resolution:**  

> 

**Can other session work continue?:** `yes / no`

**Owner / authority needed:**  

> 

---

# 12. Validation and Executed Tests

> These tests are declared prospectively. Their **actual** results must be entered only after execution.

| Test ID | Planned test / criterion | Verification method | Expected result | Actual result | Result status | Evidence |
|---|---|---|---|---|---|---|
| TEST-01 | Project directory structure exists at verified destination | Fresh repository-tree / filesystem inspection | Expected directories/files appear once created |  | `not-run` |  |
| TEST-02 | `project-identity.json` parses as valid JSON | JSON parser / Viewer where applicable | Valid JSON; Project ID blank if unassigned |  | `not-run` |  |
| TEST-03 | Project Identity does not contain relationship/implementation facts that belong elsewhere | Compare record against Project Identity profile | Intrinsic identity remains narrow |  | `not-run` |  |
| TEST-04 | Project Summary sidecar resolves to Project Summary | Inspect companion path / Viewer resolution | Sidecar points to correct human-readable source |  | `not-run` |  |
| TEST-05 | Project Summary preserves Project/System distinction | Human review against Definitions | Task Assignment and Tracking remains Project; Work Queue remains System |  | `not-run` |  |
| TEST-06 | Work Queue System Summary distinguishes evidence classes | Human review of current/historical/planning statements | No historical/planning claim is mislabeled as current implementation truth |  | `not-run` |  |
| TEST-07 | Work Queue System Summary sidecar resolves correctly | Inspect companion path / Viewer resolution | Correct System Summary companion |  | `not-run` |  |
| TEST-08 | All created JSON records parse | JSON parser / manifest validation | 0 parse errors in newly created JSON |  | `not-run` |  |
| TEST-09 | Projects discovery sees intended sidecars | Regenerate current source-aware manifest; inspect Projects source | Project Summary and Work Queue System Summary sidecars are discoverable |  | `not-run` |  |
| TEST-10 | Entity Record discovery behavior is understood | Inspect whether `project-identity.json` is discovered/presented intentionally | Result is either supported or captured as known limitation; no sidecar disguise |  | `not-run` |  |
| TEST-11 | Context-naive resume path works | Read Project README as entry point and follow authority routing | Reader can identify Project, System, core records, unresolved issues, and next action |  | `not-run` |  |
| TEST-12 | Resource references are verified | Compare referenced RES IDs against current Resource Registry | No stale or guessed Resource identity is asserted as current |  | `not-run` |  |

## 12.1 Validation summary

> Not yet executed.

## 12.2 Failed or partial validation

> None yet. Record every failed/partial test explicitly during the session.

---

# 13. Resulting State

> **Not yet populated.** Complete this section at session closure from actual evidence.

## 13.1 Project resulting state

> 

## 13.2 System resulting state

> 

## 13.3 Physical repository resulting state

> 

## 13.4 Semantic / authority resulting state

> 

## 13.5 What is now true that was not true at session start?

- 
- 
- 

## 13.6 Remaining uncertainties

- 
- 
- 

---

# 14. Resource, Registry, and Architecture Effects

## 14.1 Resources created

| Resource | Resource ID | Registration status | Notes |
|---|---|---|---|
|  |  |  |  |

> Do not assign Resource IDs in this document unless the Resource Registry actually assigns them.

## 14.2 Resources changed

| Resource ID | Resource | Change | Activity required? |
|---|---|---|---|
|  |  |  |  |

## 14.3 Registry changes required

At declaration:

- [ ] Resource Registry
- [ ] Project Registry
- [ ] System Registry
- [ ] Relationship Registry
- [ ] Activity Registry
- [ ] Record Profile Registry
- [ ] None
- [ ] Other:

### Registry notes

> Determine from actual session effects. Do not pre-classify file creation as a Registry mutation until the governing Registry rules require it.

## 14.4 Architecture change assessment

**Architecture changed during this session:** `not-yet-known`

**Architecture Changelog entry required:** `not-yet-known`

**Reason:**

> The intended session applies architecture established on August 15. If the second Project Definition merely confirms that architecture, no new architecture change should be claimed. If the Work Queue case forces a material rule change, record that decision and assess Architecture Changelog requirements explicitly.

## 14.5 Open Determinations potentially affected

- Project Registry vs Project Identity authority boundary.
- System Identity profile / permanent System ID authority.
- Entity Record discovery in the Klinswork Documentation Viewer.
- Relationship Registry implementation.
- Whether a separate Application/Implementation entity is required beneath the Work Queue System.

---

# 15. Remaining Work

> Populate at closure from actual results.

| Item | Status | Why remaining | Suggested destination |
|---|---|---|---|
| Permanent Project ID assignment | deferred | Allocation authority unresolved | Project Registry / Project Identity architecture |
| Permanent System ID assignment | deferred | System Identity / allocation authority unresolved | System Identity architecture |
| System Identity Entity Record | deferred | Not required for first pass unless evidence changes | Future Record Profile / System Definition work |
| Reusable Project Definition template extraction | deferred | Wait until at least two exemplars have been tested | Record Profile Library / Documentation architecture |
| Other |  |  |  |

---

# 16. Recommended Next Session

> Complete at closure rather than assuming success in advance.

**Recommended next session title:**  

**Primary Project:**  

**Target System:**  

**Recommended goal:**  

> 

**Required starting context:**

- resulting Task Assignment and Tracking Project Definition;
- resulting Work Queue System documentation;
- this session closure/handoff;
- any unresolved tests or architecture decisions.

**Dependencies before next session:**

- 

**Why this should be the next session:**

> 

---

# 17. Session Closure

## 17.1 Closure status

Allowed values:

- `completed`
- `partial`
- `blocked`
- `abandoned`
- `superseded`

**Closure status:**  

**Closed timestamp:**  

## 17.2 Success-criteria result

| Criterion | Result | Evidence / note |
|---|---|---|
| SC-01 | `not-evaluated` | |
| SC-02 | `not-evaluated` | |
| SC-03 | `not-evaluated` | |
| SC-04 | `not-evaluated` | |
| SC-05 | `not-evaluated` | |
| SC-06 | `not-evaluated` | |
| SC-07 | `not-evaluated` | |
| SC-08 | `not-evaluated` | |
| SC-09 | `not-evaluated` | |
| SC-10 | `not-evaluated` | |
| SC-11 | `not-evaluated` | |
| SC-12 | `not-evaluated` | |
| SC-13 | `not-evaluated` | |
| SC-14 | `not-evaluated` | |
| SC-15 | `not-evaluated` | |

## 17.3 Closure summary

> Complete from actual results. Do not pre-write a success narrative.

## 17.4 Files created

- 

## 17.5 Files modified

- 

## 17.6 Downstream records required

Evaluate at closure:

- [ ] Activity entries
- [ ] Architecture Changelog entry
- [ ] Implementation-plan revision
- [ ] Project/System documentation update
- [ ] Resource Registry update
- [ ] Machine-readable workflow/run record
- [ ] Session summary
- [ ] Work Update
- [ ] Work Update sidecar
- [ ] None
- [ ] Other:

## 17.7 Handoff / continuation point

> Write the exact point from which a context-naive future session should resume.

---

# 18. Provenance

## 18.1 Sources used to declare the session

This session was declared on August 15, 2026 from:

- the newly created `work-implementation-session-template-1.0-draft.md`;
- the August 15 Project Definition / Documentation architecture work;
- the completed Inventory Management → Inventory 3.0 exemplar;
- the current implementation-plan 3.1 architecture and its authority/temporal rules;
- the current understanding of Task Assignment and Tracking → Work Queue;
- the current Klinswork Resource Registry architecture.

These are declaration sources. Tomorrow's execution must freshly resolve the sources required to perform the work.

## 18.2 Sources used during execution

- 

## 18.3 Resource IDs expected to require verification

- `RES-011` — Klinswork Documentation Viewer
- `RES-041` — current Project documentation root
- `RES-042` — Meadows Housekeeping Projects Summary
- `RES-043` — Klinswork Resource Registry
- `RES-002` — Work Queue application Resource candidate
- `RES-003` — Work Queue data workbook Resource candidate
- `RES-012` — Tasks Resource candidate
- `RES-013` — Employees Resource candidate
- `RES-014` — Locations Resource candidate

**Important:** Listing these IDs here does not establish that every one remains current or that every one belongs in the final Project/System records. Verify each against the Resource Registry before using it as current authority.

## 18.4 Reconstruction notes

Not applicable at declaration.

This session is intended to begin as `declared-before-work`. If implementation begins before declaration/context resolution is completed, record the actual entry condition rather than preserving a false prospective chronology.

## 18.5 Interpretation limits

At declaration:

- exact current repository state has not yet been freshly inspected;
- exact current Work Queue implementation state has not yet been freshly verified;
- Registry rows have not yet been freshly resolved for tomorrow's session;
- Project Registry vs Project Identity allocation authority remains unresolved unless changed before session start;
- System Identity remains deliberately deferred;
- Application/Implementation placement beneath Work Queue remains evidence-dependent;
- the governing implementation plan still needs to be instantiated or explicitly waived by recorded decision before session activation.

---

# Appendix A — Expected Target Project Definition

This is the **expected** target structure, subject to verification and session evidence:

```text
Task Assignment and Tracking/
├── project-identity.json
├── README.md
├── summaries/
│   └── project-summary.md
├── sidecars/
│   └── project-summary-sidecar.json
└── systems/
    └── Work Queue/
        ├── README.md
        ├── summaries/
        │   └── system-summary.md
        └── sidecars/
            └── system-summary-sidecar.json
```

Deliberately absent from the required target:

```text
system-identity.json
```

unless the session discovers evidence requiring a change to that decision.

---

# Appendix B — Semantic Target

```text
Klinswork
└── Operations                               [Project]
    └── Task Assignment and Tracking         [Project]
        └── Work Queue                       [System]
            ├── Work Queue application?      [verify boundary]
            ├── RES-002?                     [verify]
            ├── RES-003?                     [verify]
            ├── RES-012?                     [verify]
            ├── RES-013?                     [verify]
            └── RES-014?                     [verify]
```

The question marks are intentional. Tomorrow's session resolves them from evidence.

---

# Appendix C — Project vs System Writing Test

Before accepting the two summaries, apply this test:

## Task Assignment and Tracking Project Summary should answer

> **Why / what operational undertaking exists?**

It should describe:

- task intake;
- assignment;
- communication;
- performance/status;
- completion;
- verification;
- reporting;
- preservation/history;
- scope and boundaries independent of any one implementation;
- the relationship to Work Queue as a System.

## Work Queue System Summary should answer

> **How is that operational function coherently implemented by this System?**

It should describe, as supported by evidence:

- System purpose;
- components;
- application/interfaces;
- data;
- Resources;
- integrations;
- behavior;
- implementation history;
- current verified state;
- limitations;
- unresolved questions.

If the Project Summary becomes a Work Queue feature history, the boundary has failed.

If the System Summary becomes a generic description of task assignment as an operational function, the boundary has failed.

---

# Appendix D — Evidence Discipline for Work Queue

Use three evidence classes explicitly:

```text
HISTORICAL IMPLEMENTATION EVIDENCE
    dated Work Updates
    historical sidecars
    prior screenshots
    prior source snapshots

PLANNING / DESIGN EVIDENCE
    implementation plans
    roadmaps
    unchecked planned items
    design notes

CURRENT IMPLEMENTATION EVIDENCE
    current source
    current Registry
    current deployment
    current datastore/schema
    current executable behavior
    fresh test evidence
```

Rules:

1. Historical evidence establishes what existed or was reported at a particular time.
2. Planning evidence establishes intention, not completion.
3. Current implementation claims require current evidence.
4. Do not convert unchecked plan items into completion claims.
5. Do not erase historical terminology merely because the current ontology changed.
6. Interpret historical material through current architecture while preserving what the source actually said.

---

# Appendix E — Session Activation Checklist

Before changing Project/System files tomorrow:

- [ ] Governing implementation plan exists **or** a recorded decision explicitly waives it for this session.
- [ ] Session status changed from `planned` to `active`.
- [ ] Actual start timestamp recorded.
- [ ] Current Definitions resolved.
- [ ] Relevant Architecture Changelog / Open Determinations checked.
- [ ] Resource Registry freshly checked.
- [ ] Fresh repository tree/current physical state inspected.
- [ ] Inventory Management exemplar loaded.
- [ ] Project Identity profile loaded.
- [ ] Relevant Work Queue historical evidence identified.
- [ ] Current Work Queue implementation authority identified.
- [ ] Project/System semantic placement confirmed.
- [ ] No blocking contradiction remains.
- [ ] First work-package item marked `in-progress`.

Only then begin Project Definition implementation.

---

# Appendix F — Closure Checklist

Before declaring the session complete:

- [ ] Every work-package item has a final status.
- [ ] Every actual test has a result.
- [ ] Every failure/partial result is explained.
- [ ] Decisions are recorded.
- [ ] Deviations are recorded.
- [ ] Blockers are recorded.
- [ ] Resulting Project state is explicit.
- [ ] Resulting System state is explicit.
- [ ] Physical repository result is explicit.
- [ ] Resource / Registry effects are assessed.
- [ ] Architecture effects are assessed.
- [ ] Remaining work is explicit.
- [ ] Next session recommendation is evidence-based.
- [ ] Downstream records are identified.
- [ ] Exact context-naive handoff point is written.
- [ ] Session closure status and timestamp are recorded.

---

# Planned One-Sentence Session Outcome

> **Task Assignment and Tracking becomes the second defined Klinswork Project exemplar, with Work Queue explicitly documented as its principal known System, through a session that was declared and bounded before implementation began.**

