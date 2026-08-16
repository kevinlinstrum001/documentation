---
template_name: work-implementation-session-template-1.0-draft
template_version: 1.0-draft
record_type: work-implementation-session
record_family: human-readable-execution-record
status: draft
authority_role: authoritative-human-readable-record-for-one-bounded-work-implementation-session
created: 2026-08-15
---

# Work Implementation Session

> **Template:** `work-implementation-session-template-1.0-draft.md`
>
> **Purpose:** Record one bounded implementation session from declaration through closure.
>
> **Authority boundary:** This document is the authoritative human-readable record of what is intended for **this session**, what context was resolved, what materially happened during execution, what was validated, and the resulting state at closure.
>
> It does **not** replace the implementation plan, Project/System records, Resource Registry, Architecture Changelog, Activity Registry, machine-readable workflow/run state, final summary, or Work Update.
>
> **Temporal rule:** Declare the session before implementation begins whenever possible. If a session is reconstructed, say so explicitly. Never rewrite earlier work as though it had been prospectively planned.
>
> **Execution rule:** Record material state transitions, decisions, deviations, blockers, tests, and outcomes. Do not turn this document into a keystroke transcript.
>
> **Identity rule:** Never invent Project, System, Resource, Relationship, Run, Session, or other durable IDs. Leave unknown identifiers blank and record the unresolved state.

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

## 1.2 Session goal

**Goal**

> [State the single bounded outcome this session is intended to produce.]

**Why this session exists**

> [Explain why this work should happen now and how it relates to the governing implementation plan.]

**Session boundary**

> [State what work belongs inside this session and where the session should stop.]

---

# 2. Relationship to the Implementation Plan

## 2.1 Governing plan

| Field | Value |
|---|---|
| Plan title | |
| Plan document ID | |
| Plan path | |
| Plan status | |
| Plan planning mode | |
| Relevant plan stage(s) | |
| Relevant acceptance criteria | |
| Relevant planned tests | |

## 2.2 Work selected for this session

> [Describe which portion of the implementation plan is being executed now.]

## 2.3 Work explicitly deferred to later sessions

- [ ]
- [ ]
- [ ]

## 2.4 Plan authority rule

The implementation plan remains the authority for the intended body of work. This session record may document execution differences, but it must not silently rewrite the implementation plan.

If execution differs from the plan, record the difference under:

- **Decisions**
- **Deviations**
- **Blockers**
- **Resulting State**

---

# 3. Starting State

> Record what is true at the session boundary **before this session changes anything**.

## 3.1 Current Project state

> [Current Project identity, documentation state, known relationships, unresolved questions, and relevant lifecycle/context.]

## 3.2 Current System state

> [Current System identity/documentation/implementation state. Distinguish historical evidence, planning evidence, and currently verified behavior.]

## 3.3 Current physical repository state

> [Record only the physical facts relevant to this session. A repository path is evidence of location, not semantic identity.]

## 3.4 Prior work relevant to this session

> [Summarize work completed before this session that establishes the starting point.]

## 3.5 Starting-state uncertainties

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

- [ ] Controlled vocabulary / Definitions
- [ ] Relevant Project Identity record
- [ ] Project-local README
- [ ] Current Project Summary
- [ ] Relevant System README
- [ ] Current System Summary
- [ ] Resource Registry
- [ ] Current repository tree / physical-state evidence
- [ ] Governing implementation plan
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

---

# 6. Success Criteria

> Define success **before execution**. These criteria should be observable and verifiable.

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
- [ ] Other:

### Reassessment procedure

If a stop condition is triggered:

1. Mark the current work item `blocked` or `partial`.
2. Record the triggering evidence.
3. Create a Decision, Deviation, or Blocker entry as appropriate.
4. Decide whether the session can continue with a revised bounded scope.
5. If not, proceed to **Session Closure** without pretending the blocked work was completed.

---

# 8. Live Execution Record

> Record **material state transitions**, not every click or keystroke.

Use one entry for each meaningful execution step.

---

## Execution Entry — EXE-001

**Work item:**  
**Status:** `not-started`  
**Started:**  
**Completed:**  

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

### Next action

> [The next bounded action.]

---

<!-- Duplicate the Execution Entry block as needed. -->

# 9. Decisions

> Record decisions that materially affect architecture, scope, interpretation, implementation, authority, or continuation.

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

<!-- Duplicate as needed. If no material decisions occurred, state: "No material session decisions." -->

# 10. Deviations

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

**Plan revision required:** `yes / no / uncertain`

---

<!-- Duplicate as needed. If none occurred, state: "No material deviations." -->

# 11. Blockers

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

<!-- Duplicate as needed. If none occurred, state: "No unresolved blockers." -->

# 12. Validation and Executed Tests

> Planned tests belong in the implementation plan. **Actual test execution and results belong here or in the corresponding machine-readable run/evidence record.**

| Test ID | Planned test / criterion | Verification method | Expected result | Actual result | Result status | Evidence |
|---|---|---|---|---|---|---|
| TEST-01 | | | | | `not-run` | |
| TEST-02 | | | | | `not-run` | |
| TEST-03 | | | | | `not-run` | |

### Test-result statuses

- `pass`
- `fail`
- `partial`
- `not-run`
- `not-applicable`

## 12.1 Validation summary

> [Summarize whether the session result satisfies its success criteria and why.]

## 12.2 Failed or partial validation

> [For every failed/partial result, state what remains unresolved and whether it blocks closure.]

---

# 13. Resulting State

> Describe the state **at the end of this session**, not the desired future state.

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
| | | | |

## 14.2 Resources changed

| Resource ID | Resource | Change | Activity required? |
|---|---|---|---|
| | | | |

## 14.3 Registry changes required

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

## 14.4 Architecture change assessment

**Architecture changed during this session:** `yes / no / uncertain`

**Architecture Changelog entry required:** `yes / no / uncertain`

**Reason:**

> 

## 14.5 Open Determinations affected

- 
- 

---

# 15. Remaining Work

> List work that remains after this session without implying it was completed or formally planned if it was not.

| Item | Status | Why remaining | Suggested destination |
|---|---|---|---|
| | | | |
| | | | |

---

# 16. Recommended Next Session

**Recommended next session title:**  

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

---

# 17. Session Closure

## 17.1 Closure status

Select one:

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
| SC-01 | | |
| SC-02 | | |
| SC-03 | | |
| SC-04 | | |
| SC-05 | | |

## 17.3 Closure summary

> [Summarize what the session accomplished, what did not happen, and why the resulting state is trustworthy.]

## 17.4 Files created

- 
- 

## 17.5 Files modified

- 
- 

## 17.6 Downstream records required

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

> [Write the exact point from which a context-naive future session should resume.]

---

# 18. Provenance

## 18.1 Sources used to declare the session

- 
- 

## 18.2 Sources used during execution

- 
- 

## 18.3 Resource IDs used

- 
- 

## 18.4 Reconstruction notes

> [Normally blank for a declared-before-work session. If any portion was reconstructed, describe what was reconstructed and from which evidence.]

## 18.5 Interpretation limits

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

---

# Appendix B — Minimum Viable Session

A Work Implementation Session does not need to become paperwork-heavy.

At minimum, before implementation begins, record:

```text
Session goal
Primary Project
Target System
Implementation plan
Starting state
Required context
Selected work package
Success criteria
Stop conditions
```

During work, record only:

```text
material execution steps
decisions
deviations
blockers
executed tests
```

At closure, record:

```text
resulting state
validation result
remaining work
next session
closure status
handoff point
```

If those elements are present and trustworthy, the session record has done its job.

---

# Appendix C — Authority Separation

```text
IMPLEMENTATION PLAN
    Intended body of work
    Prospective stages
    Planned tests
    Acceptance criteria
            │
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

---

# Appendix D — Template Design Rules

1. **Declare before implementation begins whenever possible.**
2. **Record the starting state before changing it.**
3. **Resolve context by semantic requirement, not by reading everything.**
4. **Prefer stable Resource IDs over remembered physical locations.**
5. **Keep identity separate from name, location, hierarchy, lifecycle, and implementation.**
6. **Do not infer Project/System/Application/Resource placement from repository path alone.**
7. **Record material execution events, not a transcript.**
8. **Do not rewrite the implementation plan when execution differs; record the deviation.**
9. **Keep planned tests separate from actual test results.**
10. **Do not invent durable IDs.**
11. **Stop and reassess when continuing requires unsupported architecture.**
12. **Preserve historical/planning/current-implementation evidence as distinct evidence classes.**
13. **Close every session explicitly.**
14. **End with a continuation point usable by a context-naive future session.**
