---
template_name: work-implementation-session-template-1.1-draft
template_version: 1.1-draft
record_type: work-implementation-session
record_family: human-readable-execution-record
status: draft
authority_role: authoritative-human-readable-record-for-one-bounded-work-implementation-session
created: 2026-08-15
updated: 2026-08-16
supersedes: work-implementation-session-template-1.0-draft.md
---

# Work Implementation Session

> **Template:** `work-implementation-session-template-1.1-draft.md`
>
> **Purpose:** Record one bounded implementation session from declaration or reconstruction through closure, in explicit relationship to its governing Work Unit and implementation plan.
>
> **Authority boundary:** This document is the authoritative human-readable record of what is intended for **this session**, what context was resolved, what materially happened during execution, what was validated, and the resulting state at closure.
>
> It does **not** replace the Work Unit Registry, Work Unit Activities, implementation plan, Project/System records, Resource Registry, Architecture Changelog, Activity Registry, machine-readable workflow/run state, final summary, or Work Update.
>
> **Work Unit rule:** Every formal Work Session should correspond to a Work Unit. The Work Unit Registry preserves the current state of that bounded work; Work Unit Activities preserve timestamped material history within it. This session record preserves the detailed execution narrative for one formal session.
>
> **Temporal rule:** Declare the session before implementation begins whenever possible. If a session is reconstructed, say so explicitly. Never rewrite earlier work as though it had been prospectively planned.
>
> **Activation rule:** Session initiation and session activation are distinct events when an implementation-plan gate applies. A session may be declared or reconstructed and receive a `session-initiated` Work Unit Activity before the governing implementation plan is linked. Do not represent the Work Unit/session as active implementation until required activation gates are satisfied.
>
> **Execution rule:** Record material state transitions, decisions, deviations, blockers, tests, and outcomes. Do not turn this document or Work Unit Activities into a keystroke transcript.
>
> **WUA rule:** Create a Work Unit Activity for material Work Unit events such as session initiation, activation, pause/resume, material status/readiness/dependency changes, significant decisions/deviations/blockers, durable stage completion, meaningful validation, session closure, and Work Unit completion. Do not create a WUA merely for every file save or ordinary edit.
>
> **Identity rule:** Never invent Project, System, Resource, Relationship, Run, Session, Work Unit, Work Unit Activity, or other durable IDs. Use identifiers allocated by their authority. Leave unknown identifiers blank and record the unresolved state.

---

# 1. Session Declaration

## 1.1 Session identity

| Field | Value |
|---|---|
| Session title | |
| Session date | |
| Session status | `planned` |
| Session entry mode | `declared-before-work` |
| Session ID | |
| Work Unit ID | |
| Work Unit title | |
| Work Unit kind | |
| Work Unit status at session entry | |
| Work Unit readiness at session entry | |
| Primary Project | |
| Project ID | |
| Target System | |
| System ID | |
| Target Application / Implementation | |
| Primary operational environment | |
| Implementation plan | |
| Implementation-plan sidecar | |
| Session record path | |
| Session owner / operator | |

### Session entry mode

Select one:

- `declared-before-work`
- `reconstructed-during-work`
- `reconstructed-after-work`
- `resumed-existing-session`

### Work Unit relationship

**Work Unit Registry relationship**

> [Explain why this formal session belongs to the identified Work Unit. A formal session should not create a competing work identity.]

**Current Work Unit state at declaration/reconstruction**

> [Record the Work Unit's current Registry status/readiness and any activation gate. Do not infer state from the existence of this session file.]

## 1.2 Session goal

**Goal**

> [State the single bounded outcome this session is intended to produce.]

**Why this session exists**

> [Explain why this work should happen now and how it relates to the governing Work Unit and implementation plan.]

**Session boundary**

> [State what work belongs inside this session and where the session should stop.]

## 1.3 Session initiation

| Field | Value |
|---|---|
| Session initiated timestamp | |
| Initiation WUA ID | |
| Initiation event type | `session-initiated` |
| Work Unit status after initiation | |
| Work Unit readiness after initiation | |
| Activation gate satisfied? | `yes / no / not-required / undetermined` |

**Initiation rule**

A session may be initiated before it is activated for implementation.

Initiation means the formal execution context has been declared or reconstructed and linked to the Work Unit.

It does **not** by itself prove that:

- the governing implementation plan exists;
- required prerequisites are satisfied;
- the Work Unit status is `active`;
- implementation may proceed under the plan.

If an activation gate remains unsatisfied, preserve that state explicitly.

## 1.4 Session activation

| Field | Value |
|---|---|
| Activation required? | `yes / no / undetermined` |
| Activation condition | |
| Activated timestamp | |
| Activation WUA ID | |
| Activation event type | `session-activated` |
| Work Unit status after activation | |
| Work Unit readiness after activation | |

**Activation rule**

When a governing implementation plan or another prerequisite is an activation gate:

```text
session declared / reconstructed
        ↓
session initiated
        ↓
required plan / prerequisite satisfied
        ↓
Work Unit Registry reconciled
        ↓
session activated
        ↓
implementation proceeds
```

Do not backdate activation merely because some work occurred before the gate was noticed.

If work began before activation, preserve the chronology through reconstruction, deviation, and Work Unit Activities.

---

# 2. Relationship to the Work Unit and Implementation Plan

## 2.1 Governing Work Unit

| Field | Value |
|---|---|
| Work Unit ID | |
| Work Unit title | |
| Work Unit kind | |
| Work Unit goal | |
| Work Unit completion rule | |
| Work Unit status | |
| Work Unit readiness | |
| Primary Project | |
| Target System / App | |
| Formal session required? | |
| Session record registered? | |
| Implementation plan registered? | |

## 2.2 Governing implementation plan

| Field | Value |
|---|---|
| Plan title | |
| Plan document ID | |
| Plan path | |
| Plan sidecar path | |
| Plan status | |
| Plan planning mode | |
| Plan authority boundary timestamp | |
| Relevant plan stage(s) | |
| Relevant acceptance criteria | |
| Relevant planned tests | |

## 2.3 Work selected for this session

> [Describe which portion of the Work Unit and implementation plan is being executed now.]

## 2.4 Work explicitly deferred to later sessions

- [ ]
- [ ]
- [ ]

## 2.5 Plan authority rule

The implementation plan remains the authority for the intended body of work. This session record may document execution differences, but it must not silently rewrite the implementation plan.

If execution differs from the plan, record the difference under:

- **Decisions**
- **Deviations**
- **Blockers**
- **Resulting State**

If the plan is created after some work has already occurred, use the applicable reconstructed/continuation planning semantics and preserve pre-plan work as historical state rather than prospectively planned work.

## 2.6 Work Unit authority rule

The Work Unit Registry remains the authority for the Work Unit's current state.

This session record may explain why status/readiness changed, but the change is not authoritative until the Work Unit Registry is reconciled.

Timestamped material history belongs in Work Unit Activities.

---

# 3. Starting State

> Record what is true at the session boundary **before this session changes anything**. If the session is reconstructed during work, identify the reconstruction boundary and distinguish earlier work from the state being governed from this point forward.

## 3.1 Current Work Unit state

> [Record Work Unit status, readiness, prerequisites, completion rule, formal-session state, implementation-plan state, and material prior WUAs.]

## 3.2 Current Project state

> [Current Project identity, documentation state, known relationships, unresolved questions, and relevant lifecycle/context.]

## 3.3 Current System state

> [Current System identity/documentation/implementation state. Distinguish historical evidence, planning evidence, and currently verified behavior.]

## 3.4 Current physical repository state

> [Record only the physical facts relevant to this session. A repository path is evidence of location, not semantic identity.]

## 3.5 Prior work relevant to this session

> [Summarize work completed before this session that establishes the starting point. If the session or implementation plan is reconstructed, identify work completed before the reconstruction boundary.]

## 3.6 Prior Work Unit Activities relevant to this session

| WUA ID | Timestamp | Event type | Material effect | Why relevant now |
|---|---|---|---|---|
| | | | | |

## 3.7 Starting-state uncertainties

- [ ]
- [ ]
- [ ]

---

# 4. Context Resolution

> Load only the context needed to perform this session correctly. Prefer semantic requirements resolved through stable Resource IDs rather than remembered or hard-coded locations.

## 4.1 Context requirements

| Requirement ID | Required context | Purpose | Authority role | Resolved Resource ID(s) | Status | Notes |
|---|---|---|---|---|---|---|
| CTX-01 | | | | | `unresolved` | |
| CTX-02 | | | | | `unresolved` | |
| CTX-03 | | | | | `unresolved` | |

Suggested statuses:

- `unresolved`
- `resolved`
- `partially-resolved`
- `not-required`
- `blocked`

## 4.2 Orientation sources actually loaded

- [ ] Work Units Registry
- [ ] Relevant Work Unit Activities
- [ ] Controlled vocabulary / Definitions
- [ ] Relevant Project Identity record
- [ ] Project-local README
- [ ] Current Project Summary
- [ ] Relevant System README
- [ ] Current System Summary
- [ ] Resource Registry
- [ ] Current repository tree / physical-state evidence
- [ ] Governing implementation plan
- [ ] Implementation-plan sidecar
- [ ] Relevant workflow specification
- [ ] Relevant recent Activities
- [ ] Open Determinations
- [ ] Other:

## 4.3 Unresolved context

> [List missing or ambiguous context that could affect execution.]

## 4.4 Context-resolution summary

> [Explain whether enough authoritative context exists to proceed safely.]

---

# 5. Session Work Package

> Select a bounded set of implementation-plan work for this session. Each item should have an objective, deliverable, dependency, and exit criterion.

| Seq. | Work item | Objective | Deliverable | Dependencies | Exit criterion | Status |
|---:|---|---|---|---|---|---|
| 1 | | | | | | `not-started` |
| 2 | | | | | | `not-started` |
| 3 | | | | | | `not-started` |

### Work-item statuses

- `not-started`
- `in-progress`
- `complete`
- `partial`
- `blocked`
- `skipped`

### Work Unit Activity checkpoint planning

For each work item, decide whether completion or another state change would constitute a **material Work Unit event**.

Do not pre-allocate WUA IDs.

Example:

```text
Work item
    complete Project-level definition package

Material event?
    yes

Expected WUA event type
    stage-completed
```

---

# 6. Success Criteria

> Define success **before execution** whenever possible. For reconstructed work, identify which criteria were established prospectively and which were reconstructed from the declared goal or governing plan. These criteria should be observable and verifiable.

- [ ] **SC-01 —**
- [ ] **SC-02 —**
- [ ] **SC-03 —**
- [ ] **SC-04 —**
- [ ] **SC-05 —**

## 6.1 Minimum acceptable outcome

> [Describe the smallest result that would justify closing this session as useful rather than failed.]

## 6.2 Non-goals

The following are explicitly outside this session:

- [ ]
- [ ]
- [ ]

---

# 7. Stop / Reassessment Conditions

> Stop implementation and reassess when continuing would require an unsupported architectural assumption, unresolvable authority conflict, uncontrolled scope expansion, or other material departure from the declared session.

Stop and reassess if:

- [ ] Evidence contradicts the planned Project/System/Application/Resource placement.
- [ ] A required authority cannot be resolved.
- [ ] A durable ID would have to be invented to continue.
- [ ] The work begins expanding into an explicitly out-of-scope body of work.
- [ ] A planned stage requires an architecture decision that has not been made.
- [ ] Current implementation truth cannot be distinguished from historical or planning evidence.
- [ ] Validation reveals that the current approach is producing structurally incorrect records.
- [ ] A required Work Unit/session activation gate cannot be satisfied.
- [ ] Work Unit Registry state and actual execution cannot be reconciled without falsifying chronology.
- [ ] Other:

### Reassessment procedure

If a stop condition is triggered:

1. Mark the current work item `blocked` or `partial`.
2. Record the triggering evidence.
3. Create a Decision, Deviation, or Blocker entry as appropriate.
4. Determine whether the event requires a Work Unit Activity.
5. Reconcile Work Unit status/readiness if materially changed.
6. Decide whether the session can continue with a revised bounded scope.
7. If not, proceed to **Session Closure** without pretending the blocked work was completed.

---

# 8. Work Unit Activity Recording

> Work Unit Activities are the append-oriented timestamped history of material events within the governing Work Unit. They complement this richer session execution record.

## 8.1 Material-event rule

Create a WUA when an event materially changes or establishes:

- Work Unit existence or registration;
- formal session initiation;
- implementation-plan linkage when it satisfies an execution gate;
- session activation;
- Work Unit status;
- Work Unit readiness;
- prerequisites or dependencies;
- material scope;
- significant architecture or execution decisions;
- significant deviations;
- blockers that materially affect continuation;
- pause;
- resume;
- completion of a defined stage or durable deliverable package;
- meaningful validation result;
- Registry / architecture reconciliation result;
- formal session closure;
- Work Unit completion, abandonment, or supersession.

## 8.2 Events that normally do not require a WUA

Do not create a WUA merely for:

- every file save;
- spelling corrections;
- formatting-only edits;
- ordinary edits within an already-recorded stage;
- conversation turns that do not materially change work state;
- repeated validation that produces no new material result.

## 8.3 Granularity rule

Prefer:

```text
one WUA
    = one materially meaningful historical event
```

rather than:

```text
one WUA
    = one low-level implementation action
```

## 8.4 Session WUA log

Use this table as a session-local index to Work Unit Activities actually created. The Work Unit Activities Registry remains authoritative.

| Seq. | WUA ID | Timestamp | Event type | Material event | Work Unit state effect | Related execution / decision / test |
|---:|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |

## 8.5 Registry synchronization rule

When a WUA represents a current-state change, reconcile the Work Unit Registry as part of the same material event.

Examples:

```text
implementation plan linked
        ↓
WUA recorded
        +
WORK UNIT
    STATUS / READINESS / IMPLEMENTATION PLAN / LAST UPDATE
    reconciled as applicable
```

and:

```text
session closed
        ↓
closure WUA recorded
        +
WORK UNIT
    STATUS / READINESS / COMPLETED / RESULT / LAST UPDATE
    reconciled as applicable
```

A WUA records history.

It does not replace the current-state Work Unit row.

---

# 9. Live Execution Record

> Record **material state transitions**, not every click or keystroke. When an execution entry also creates a material Work Unit event, link the corresponding WUA.

Use one entry for each meaningful execution step.

---

## Execution Entry — EXE-001

**Work item:**
**Status:** `not-started`
**Started:**
**Completed:**
**Related WUA ID(s):**

### Objective

> [What this execution step is intended to accomplish.]

### Action

> [What materially happened.]

### Evidence / sources used

-
-

### Finding / observation

> [What was discovered or confirmed.]

### Result

> [What changed as a result of this step.]

### Files / records affected

-
-

### Resource IDs affected

-

### Work Unit / Registry effect

> [State whether this execution changed Work Unit status, readiness, dependencies, implementation-plan linkage, result, or other current-state fields. If none, say none.]

### Next action

> [The next bounded action.]

---

<!-- Duplicate the Execution Entry block as needed. -->

# 10. Decisions

> Record decisions that materially affect architecture, scope, interpretation, implementation, authority, Work Unit state, or continuation.

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

**Effect on Work Unit:**

>

**Related WUA ID:**

**Effect beyond this session:**

>

**Architecture Changelog required:** `yes / no / uncertain`

---

<!-- Duplicate as needed. If no material decisions occurred, state: "No material session decisions." -->

# 11. Deviations

> A deviation records where execution differed materially from the implementation plan or declared session work package.

## Deviation — DEV-001

**Planned:**

>

**Actually done:**

>

**Reason:**

>

**Impact:**

>

**Effect on Work Unit:**

>

**Related WUA ID:**

**Plan revision required:** `yes / no / uncertain`

---

<!-- Duplicate as needed. If none occurred, state: "No material deviations." -->

# 12. Blockers

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

**Effect on Work Unit status/readiness:**

>

**Related WUA ID:**

---

<!-- Duplicate as needed. If none occurred, state: "No unresolved blockers." -->

# 13. Validation and Executed Tests

> Planned tests belong in the implementation plan. **Actual test execution and results belong here or in the corresponding machine-readable run/evidence record.** A meaningful validation checkpoint may also require a WUA.

| Test ID | Planned test / criterion | Verification method | Expected result | Actual result | Result status | Evidence | Related WUA |
|---|---|---|---|---|---|---|---|
| TEST-01 | | | | | `not-run` | | |
| TEST-02 | | | | | `not-run` | | |
| TEST-03 | | | | | `not-run` | | |

### Test-result statuses

- `pass`
- `fail`
- `partial`
- `not-run`
- `not-applicable`

## 13.1 Validation summary

> [Summarize whether the session result satisfies its success criteria and why.]

## 13.2 Failed or partial validation

> [For every failed/partial result, state what remains unresolved and whether it blocks closure.]

## 13.3 Validation WUA assessment

**Material Work Unit validation event occurred:** `yes / no`

**Related WUA ID(s):**

**Reason:**

>

---

# 14. Resulting State

> Describe the state **at the end of this session**, not the desired future state.

## 14.1 Work Unit resulting state

| Field | Resulting value |
|---|---|
| Work Unit status | |
| Work Unit readiness | |
| Implementation plan | |
| Formal session | |
| Completion rule satisfied? | |
| Completed timestamp | |
| Result | |
| Last update | |

## 14.2 Project resulting state

>

## 14.3 System resulting state

>

## 14.4 Physical repository resulting state

>

## 14.5 Semantic / authority resulting state

>

## 14.6 What is now true that was not true at session start?

-
-
-

## 14.7 Remaining uncertainties

-
-
-

---

# 15. Resource, Registry, Work Unit, and Architecture Effects

## 15.1 Resources created

| Resource | Resource ID | Registration status | Notes |
|---|---|---|---|
| | | | |

## 15.2 Resources changed

| Resource ID | Resource | Change | Activity required? |
|---|---|---|---|
| | | | |

## 15.3 Registry changes required

- [ ] Work Units Registry
- [ ] Work Unit Activities
- [ ] Resource Registry
- [ ] Project Registry
- [ ] System Registry
- [ ] Relationship Registry
- [ ] Activity Registry
- [ ] Record Profile Registry
- [ ] None
- [ ] Other:

### Registry notes

>

## 15.4 Work Unit Registry reconciliation

| Field | Before | After | Basis / WUA |
|---|---|---|---|
| STATUS | | | |
| READINESS | | | |
| PREREQUISITES | | | |
| IMPLEMENTATION PLAN | | | |
| SESSION RECORD | | | |
| COMPLETED | | | |
| RESULT | | | |
| LAST UPDATE | | | |

## 15.5 Work Unit Activities created

| WUA ID | Timestamp | Event type | Action | Why material |
|---|---|---|---|---|
| | | | | |

## 15.6 Architecture change assessment

**Architecture changed during this session:** `yes / no / uncertain`

**Architecture Changelog entry required:** `yes / no / uncertain`

**Reason:**

>

## 15.7 Open Determinations affected

-
-

---

# 16. Remaining Work

> List work that remains after this session without implying it was completed or formally planned if it was not.

| Item | Status | Why remaining | Suggested destination |
|---|---|---|---|
| | | | |
| | | | |

If a remaining item is sufficiently bounded to become its own Work Unit, identify it as a **candidate** without inventing a `WORK-####` ID.

---

# 17. Recommended Next Session

**Recommended next session title:**

**Primary Work Unit:**

**Primary Project:**

**Target System:**

**Recommended goal:**

>

**Required starting context:**

-
-

**Dependencies before next session:**

-
-

**Why this should be the next session:**

>

If the next session belongs to the same Work Unit, say so.

If it requires a new Work Unit, record that as a candidate for Registry allocation rather than inventing an ID.

---

# 18. Session Closure

## 18.1 Closure status

Select one:

- `completed`
- `partial`
- `blocked`
- `abandoned`
- `superseded`

**Closure status:**

**Closed timestamp:**

## 18.2 Work Unit closure relationship

| Field | Value |
|---|---|
| Session closure WUA ID | |
| Work Unit completion WUA ID | |
| Work Unit status after session | |
| Work Unit readiness after session | |
| Work Unit completion rule satisfied? | `yes / no / partial / undetermined` |
| Work Unit completed timestamp | |
| Work Unit result | |

A session may close while the Work Unit remains active, planned, paused, or blocked.

Do **not** automatically mark a Work Unit completed merely because one formal session ended.

## 18.3 Success-criteria result

| Criterion | Result | Evidence / note |
|---|---|---|
| SC-01 | | |
| SC-02 | | |
| SC-03 | | |
| SC-04 | | |
| SC-05 | | |

## 18.4 Closure summary

> [Summarize what the session accomplished, what did not happen, and why the resulting state is trustworthy.]

## 18.5 Files created

-
-

## 18.6 Files modified

-
-

## 18.7 Downstream records required

- [ ] Work Unit Registry update
- [ ] Work Unit Activities
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

## 18.8 Handoff / continuation point

> [Write the exact point from which a context-naive future session should resume. Include the governing Work Unit and current Work Unit status/readiness.]

---

# 19. Provenance

## 19.1 Sources used to declare the session

-
-

## 19.2 Sources used during execution

-
-

## 19.3 Resource IDs used

-
-

## 19.4 Work Unit IDs used

-

## 19.5 Work Unit Activity IDs used

-

## 19.6 Reconstruction notes

> [Normally blank for a declared-before-work session. If any portion was reconstructed, describe what was reconstructed, the temporal boundary, and the evidence used. Do not rewrite prior work as prospectively planned.]

## 19.7 Interpretation limits

> [State important facts that remain uncertain, inferred, historical, unverified, or outside this session's authority.]

---

# Appendix A — Controlled Vocabulary

## Session status

- `planned`
- `active`
- `paused`
- `blocked`
- `completed`
- `abandoned`
- `superseded`

## Session entry mode

- `declared-before-work`
- `reconstructed-during-work`
- `reconstructed-after-work`
- `resumed-existing-session`

## Work-item status

- `not-started`
- `in-progress`
- `complete`
- `partial`
- `blocked`
- `skipped`

## Test result

- `pass`
- `fail`
- `partial`
- `not-run`
- `not-applicable`

## Context-resolution status

- `unresolved`
- `resolved`
- `partially-resolved`
- `not-required`
- `blocked`

## Activation-gate status

- `yes`
- `no`
- `not-required`
- `undetermined`

## Recommended Work Unit Activity event types

These are recommended semantic labels for common formal-session events. The Work Unit Activities registry remains the authority for actual allocated WUA IDs and recorded events.

- `work-unit-created`
- `session-initiated`
- `implementation-plan-linked`
- `session-activated`
- `status-changed`
- `readiness-changed`
- `dependency-changed`
- `decision-recorded`
- `deviation-recorded`
- `blocker-recorded`
- `session-paused`
- `session-resumed`
- `stage-completed`
- `validation-recorded`
- `registry-reconciled`
- `session-completed`
- `work-unit-completed`
- `work-unit-abandoned`
- `work-unit-superseded`

Event types should describe the material event rather than the low-level edit that happened to implement it.

---

# Appendix B — Minimum Viable Session

A Work Implementation Session does not need to become paperwork-heavy.

At minimum, before active implementation begins whenever possible, record:

```text
Work Unit ID
Work Unit current status/readiness
Session goal
Primary Project
Target System
Implementation plan
Activation gate
Starting state
Required context
Selected work package
Success criteria
Stop conditions
```

At initiation / activation, preserve:

```text
session initiated timestamp
initiation WUA
implementation-plan linkage
session activated timestamp when applicable
activation WUA
Work Unit Registry reconciliation
```

During work, record only:

```text
material execution steps
material WUAs
decisions
deviations
blockers
executed tests
```

At closure, record:

```text
resulting Work Unit state
resulting Project/System state
validation result
remaining work
next session
closure status
closure WUA
Work Unit completion WUA if the Work Unit itself is complete
handoff point
```

If those elements are present and trustworthy, the session record has done its job.

---

# Appendix C — Authority Separation

```text
WORK UNIT REGISTRY
    Stable bounded-work identity
    Current Work Unit state
    Goal / completion rule
    Placement / readiness
            │
            ├──────────────────────┐
            │                      │
            ▼                      ▼
WORK UNIT ACTIVITIES        IMPLEMENTATION PLAN
    Timestamped history         Intended body of work
    Session initiation          Prospective stages
    Activation                  Planned tests
    Status/readiness            Acceptance criteria
    Decisions/blockers          Reconstructed boundary
    Stage / validation
    Closure / completion
            │                      │
            └──────────┬───────────┘
                       ▼
              WORK IMPLEMENTATION SESSION
                  One bounded execution session
                  Starting state
                  Context actually resolved
                  Work package selected
                  Material execution history
                  Decisions / deviations / blockers
                  Tests actually executed
                  Resulting state
                  Registry reconciliation
                  Closure / handoff
                       │
                       ▼
              MACHINE-READABLE RUN / EVIDENCE
                  Structured session state
                  Execution evidence
                  Machine-consumable status
                       │
                       ▼
              SUMMARY / WORK UPDATE
                  Retrospective interpretation
                  Project delta
                  Meaning
                  Communication
```

A Work Implementation Session may reference all of these records. It must not silently absorb their authority.

A Work Unit Activity may summarize a material session event, but the richer execution evidence remains in the session record.

---

# Appendix D — Template Design Rules

1. **Every formal Work Session should correspond to a Work Unit.**
2. **Declare the session before implementation begins whenever possible.**
3. **Distinguish session initiation from session activation when an activation gate exists.**
4. **Do not represent active implementation until required activation gates are satisfied.**
5. **Record the Work Unit's current Registry state at the session boundary.**
6. **Record the starting Project/System state before changing it.**
7. **Resolve context by semantic requirement, not by reading everything.**
8. **Prefer stable Resource IDs over remembered physical locations.**
9. **Keep identity separate from name, location, hierarchy, lifecycle, and implementation.**
10. **Do not infer Project/System/Application/Resource placement from repository path alone.**
11. **Record material execution events, not a transcript.**
12. **Create WUAs for material Work Unit events, not routine edits.**
13. **Reconcile the current Work Unit row when a WUA reflects a current-state change.**
14. **Do not rewrite the implementation plan when execution differs; record the deviation.**
15. **Keep planned tests separate from actual test results.**
16. **Do not invent durable IDs, including WORK-#### and WUA-#### identifiers.**
17. **Stop and reassess when continuing requires unsupported architecture.**
18. **Preserve historical/planning/current-implementation evidence as distinct evidence classes.**
19. **A session may close without completing its Work Unit.**
20. **Close every session explicitly.**
21. **End with a continuation point usable by a context-naive future session.**
22. **Preserve reconstructed chronology rather than making later planning appear prospective.**

---

# Appendix E — Revision Notes

## 1.1-draft — 2026-08-16

This revision preserves the 1.0-draft session architecture and adds first-class integration with the Klinswork Work Unit planning layer.

Added:

- Work Unit identity and current-state fields;
- Work Unit/session relationship section;
- session initiation record;
- session activation record;
- explicit initiation-versus-activation rule;
- implementation-plan activation gating;
- prior WUA context;
- Work Unit Activity material-event policy;
- session-local WUA index;
- Registry synchronization rule;
- WUA references on execution, decisions, deviations, blockers, and validation;
- Work Unit resulting-state section;
- Work Unit Registry reconciliation table;
- Work Unit Activities created table;
- Work Unit/session closure distinction;
- closure and completion WUA fields;
- Work Unit/WUA provenance;
- recommended WUA event vocabulary;
- updated minimum viable session;
- updated authority-separation model;
- expanded template design rules.

Preserved:

- implementation-plan authority separation;
- temporal/reconstruction discipline;
- context resolution by semantic requirement;
- evidence-class separation;
- material-event rather than keystroke recording;
- explicit validation and closure;
- prohibition on invented durable IDs.
