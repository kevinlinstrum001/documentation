# Morning Documentation Session Summary  
## Inventory App SDS Registry Planning, Sidecar Architecture, and Workflow Learning

**Date:** August 4, 2026  
**Conversation window:** Early morning, ending at approximately 6:14 AM Mountain Time  
**Primary project:** Inventory App  
**Current application name:** Inventory 3.0  
**Documentation project:** Klinswork Documentation  
**Session type:** Planning, information architecture, artifact creation, workflow refinement, and process evaluation  
**Implementation status:** Planned but not yet started  
**Work-session schedule:** To be determined later this week

---

## Executive Summary

This morning’s conversation moved the Inventory App SDS registry work from a loosely assembled technical idea into a controlled, documented implementation package.

We began by clarifying how the existing `work-update-catalog` handled missing formal project records. That led us to preserve temporary but meaningful project names rather than inventing permanent project IDs before the project registry exists. We then corrected our understanding of where implementation plans belong in the repository and distinguished three separate artifact types:

1. the human-readable Markdown implementation plan,
2. the JSON sidecar that describes that plan, and
3. a future generated implementation-plan catalog that will aggregate those sidecars.

We created the full Markdown implementation plan for rebuilding the Inventory 3.0 SDS system, then adapted the repository structure so the plan lives under the project-specific directory:

```text
documents/work-update-catalog/
projects/inventory-app/
implementation-plans/
implementation-plan.md
```

We created the companion sidecar for that plan under the typed sidecar collection:

```text
documents/work-update-catalog/
sidecars/implementation-plans/
implementation-plan-sds-sheet-upgrade-sidecar-3.0-draft.json
```

During the process, we also made an important naming decision:

- **Inventory App** will be the stable project name.
- **Inventory 3.0** will remain the current application or release name.

This avoids renaming the project every time the application is upgraded.

The conversation then moved beyond artifact creation into evaluation of the workflow itself. We identified that the documentation system is not merely preserving records after work. It is becoming a mechanism for:

- accelerating context creation,
- reducing cognitive load,
- helping the user learn while following the work,
- preventing skipped workflow steps,
- exposing project relationships,
- supporting complex operations with lower risk,
- reducing end-session burnout,
- preserving session history for the JSON Viewer,
- and making future sessions easier to start and resume.

The planned Inventory App SDS work session will therefore serve two purposes:

1. implement the technical SDS registry upgrade, and
2. test whether the documentation workflow actually improves execution, learning, continuity, and recovery.

---

# 1. Starting Situation

At the beginning of the conversation window, several important things were already known.

The Inventory 3.0 application had a small bootstrap SDS sheet containing only seven products. A more complete chemical product catalog had already been assembled with twelve product records and richer information about:

- exact SDS identity,
- verification status,
- source quality,
- document access,
- section coverage,
- product matching,
- historical revisions,
- known conflicts,
- and corrective actions.

The intended technical work was already conceptually clear:

- rebuild the SDS sheet,
- populate all twelve products,
- retain historical revisions,
- correct a small number of confirmed product-reference errors,
- update the Apps Script client,
- add integrity handling,
- test the result,
- deploy the revision,
- and preserve evidence.

What was not yet fully settled was the documentation architecture around that work.

The unresolved questions included:

- How should the implementation plan relate to the project catalog?
- Where should the plan itself live?
- Where should its sidecar live?
- Should the JSON sidecar be treated as the plan, or as a description of the plan?
- How should temporary project names be handled before formal project files exist?
- What should the stable project name be?
- How should the future implementation-plan catalog fit into the structure?

The morning’s work resolved most of those questions.

---

# 2. Revisiting the Catalog Structure

## 2.1 Initial interpretation

We first reconsidered how the existing catalog structure affected the implementation-plan sidecar.

The important observation was that the existing work-update and lesson catalogs did not stop functioning merely because formal project records were incomplete. Instead, they used meaningful project names and descriptive identification fields while leaving formal project IDs and project-record paths blank.

That established a bootstrap convention:

- use an explicit project name when the project is clearly identifiable,
- do not invent a permanent ID,
- leave `projectId` blank,
- leave `projectRecordPath` blank,
- record the identification basis,
- record confidence,
- and set project context flags honestly.

This meant the implementation plan did not need to wait for a completed project registry.

## 2.2 Temporary project naming

The plan could safely identify its project context even before formal project files were built.

The initial provisional name was:

```text
Inventory 3.0
```

However, this later evolved into a better distinction:

```text
Project: Inventory App
Current application/release: Inventory 3.0
```

This is one of the most consequential decisions made during the session because it separates durable identity from version naming.

## 2.3 Sidecars versus catalogs

We also clarified that a catalog is not simply a folder of unrelated JSON files.

The intended pattern is:

```text
individual authoritative sidecars
        ↓
generated cumulative catalog
```

The sidecars remain available as individual records. The catalog is a discovery, filtering, and query surface generated from those records.

This led to a typed architecture:

```text
sidecars/lessons/
sidecars/work-updates/
sidecars/sds/
sidecars/implementation-plans/
```

with corresponding future catalog files under:

```text
catalogs/
```

The implementation-plan catalog does not yet exist, but the sidecar collection can be created now.

---

# 3. Clarifying the Role of the Implementation Plan

## 3.1 The workflow settled the question

The uploaded workflow made the intended authority relationship clear.

The workflow treats the implementation plan as the tactical human-readable plan for one bounded work session. It is created in conversation, inspected against the actual implementation, reviewed, approved, and then used to guide execution.

Therefore:

```text
implementation-plan.md
```

is the authoritative tactical plan.

The JSON file is not the primary plan. It is the sidecar that describes, indexes, and structurally exposes the Markdown plan.

## 3.2 Correct artifact sequence

We established this sequence:

```text
planning conversation
        ↓
approved implementation strategy
        ↓
implementation-plan.md
        ↓
implementation-plan sidecar JSON
        ↓
future implementation-plan catalog
```

This corrected an earlier ambiguity in which the structured JSON might have been treated as the plan itself.

## 3.3 Artifact responsibilities

### Markdown implementation plan

The Markdown file contains the readable work strategy:

- purpose,
- current state,
- target state,
- scope,
- data model,
- implementation stages,
- file changes,
- risks,
- rollback,
- tests,
- acceptance criteria,
- evidence requirements,
- unresolved items,
- and the scheduling gate.

### JSON sidecar

The sidecar exposes the plan structurally:

- document identity,
- project context,
- subject,
- planning context,
- target state,
- stages,
- dependencies,
- risks,
- tests,
- acceptance criteria,
- technical files,
- deployments,
- links,
- publication state,
- audience views,
- knowledge produced,
- and provenance.

### Future catalog

The future implementation-plan catalog will aggregate the sidecars, not the Markdown plans directly.

That will make implementation-plan history searchable and viewable through the JSON Viewer.

---

# 4. Building the Markdown Implementation Plan

We created a comprehensive Markdown plan titled:

```text
Inventory 3.0 SDS Registry Rebuild and App Integration
```

The plan was intentionally written before scheduling the work session.

Its status was recorded as ready for review and approval, while start and stop times remained blank.

## 4.1 Purpose of the plan

The plan defines a bounded work session to:

- rebuild the Inventory App SDS sheet,
- populate the registry from the chemical product catalog,
- retain historical SDS revisions,
- correct conclusively resolved product data,
- update the Inventory 3.0 interface,
- add integrity handling,
- test the result,
- deploy it,
- and preserve evidence.

## 4.2 Central data-model distinction

One of the most important design rules is:

```text
current ≠ verified
```

More precisely:

- `current` means the record is the active row the application should use.
- `status` describes the verification quality of that record.

A current record may still be:

- partially verified,
- conflicting,
- unverified,
- or source unavailable.

This prevents the application from pretending that an active document is necessarily complete or problem-free.

## 4.3 Planned SDS schema

The plan defines a richer operational registry with fields for:

- stable SDS ID,
- product ID,
- current status,
- verification status,
- catalog entry ID,
- SDS identifier,
- official product name,
- manufacturer product ID,
- form or use state,
- revision date,
- version,
- jurisdiction,
- language,
- document URL,
- source,
- source owner,
- source type,
- access status,
- saved-copy URL,
- review date,
- product-match status,
- coverage status,
- complete sections,
- partial sections,
- unresolved sections,
- issue summary,
- action needed,
- supersession linkage,
- and notes.

The sheet will still preserve backward-compatible fields needed by the existing application.

## 4.4 Planned records

The target sheet will contain at least fifteen rows:

- twelve current rows, one for each product from CHEM-001 through CHEM-012,
- and three historical rows for superseded revisions of CHEM-003, CHEM-005, and CHEM-007.

The plan also includes representative edge cases:

- a verified record,
- a partially verified record,
- a conflicting record with a document,
- a source-unavailable record,
- a current record with retained history,
- no-current failure,
- multiple-current failure,
- relative URL handling,
- and absolute URL handling.

## 4.5 Product corrections

The plan identifies several product-reference corrections supported by strong evidence, while explicitly preserving unresolved conflicts.

This is an important governance rule:

> Correct what is conclusively established; do not erase genuine uncertainty.

## 4.6 Apps Script change map

The plan distinguishes required changes from confirmed nonchanges.

### Expected changes

- `Scripts.html`
- `Styles.html`
- `Config.gs` for version only

### Expected unchanged files

- `Index.html`
- `Code.gs`
- `DataService.gs`
- shared validation file
- inventory business-rules file

This protects the session from unnecessary scope expansion.

## 4.7 Ten implementation stages

The plan contains ten ordered stages:

1. Preserve the current state.
2. Build the new sheet structure.
3. Populate current and historical records.
4. Apply conclusive product corrections.
5. Refactor SDS record selection.
6. Update SDS presentation.
7. Add status styling.
8. Update the application version and run regression checks.
9. Deploy and verify.
10. Declare the documentation checkpoint.

The order is designed to preserve recoverability and prevent client code from depending on unvalidated data.

## 4.8 Thirteen planned tests

The plan defines thirteen tests covering:

- sheet loading,
- one-current-row integrity,
- verified records,
- partially verified records,
- conflicting records,
- source-unavailable records,
- historical revision selection,
- no-current failure,
- multiple-current failure,
- relative and absolute URLs,
- view consistency,
- inventory regression,
- and canonical deployment verification.

## 4.9 Acceptance criteria

The plan defines concrete completion conditions, including:

- all twelve products represented,
- exactly one current row per product,
- historical rows retained,
- current and status treated independently,
- CHEM-008 represented honestly,
- no arbitrary fallback,
- consistent client views,
- available documents still openable,
- product corrections verified,
- conflicts preserved,
- no inventory regression,
- application version updated,
- deployment verified,
- and session timing and deviations recorded.

---

# 5. Repository Structure Changes

## 5.1 Initial sidecar placement

At one point, the Markdown plan existed under:

```text
documents/work-update-catalog/
sidecars/implementation-plans/
```

This was useful as a temporary location, but conceptually incorrect because the Markdown plan is not a sidecar.

## 5.2 Project-specific plan directory

The repository was then altered to create:

```text
documents/work-update-catalog/
projects/inventory-app/
implementation-plans/
```

An empty `README.md` initially preserved the folder in GitHub.

The Markdown implementation plan was then placed at:

```text
documents/work-update-catalog/
projects/inventory-app/
implementation-plans/
implementation-plan.md
```

This is now the authoritative project-specific plan location.

## 5.3 Sidecar collection

The sidecar belongs in the parallel typed collection:

```text
documents/work-update-catalog/
sidecars/implementation-plans/
```

The generated sidecar filename is:

```text
implementation-plan-sds-sheet-upgrade-sidecar-3.0-draft.json
```

## 5.4 Future catalog location

The future aggregate belongs under:

```text
documents/work-update-catalog/
catalogs/
```

The exact catalog filename and catalog ID remain unresolved.

---

# 6. Stable Project Naming Decision

A major architectural improvement was made when the user proposed renaming the durable project from **Inventory 3.0** to **Inventory App**.

## 6.1 Why the old name was problematic

A name such as:

```text
Inventory 3.0
```

mixes project identity with release numbering.

That creates unnecessary maintenance because every substantial upgrade appears to require a new project name.

## 6.2 New naming model

We adopted this distinction:

```text
Project name: Inventory App
Current application name: Inventory 3.0
```

This allows future releases such as:

```text
Inventory 3.1
Inventory 4.0
Inventory Mobile
Inventory App beta deployment
```

to remain part of one durable project.

## 6.3 Sidecar treatment

The sidecar therefore records:

- `projectName`: `Inventory App`
- `primaryApp`: `Inventory 3.0`

Formal project ID and project-record path remain blank because the project registry has not yet been built.

The identification basis explains that:

- the user explicitly selected the stable project name,
- the repository path uses `projects/inventory-app`,
- and the current application and document title still use Inventory 3.0.

---

# 7. Creating the Implementation-Plan Sidecar

We created a complete JSON sidecar using the uploaded `3.0-draft` implementation-plan sidecar template.

The sidecar describes the live Markdown plan and includes:

- project context,
- related catalog context,
- subject metadata,
- planning need,
- scope,
- assumptions,
- constraints,
- current and desired state,
- ten implementation stages,
- dependencies,
- seven major risks,
- fourteen acceptance criteria,
- thirteen planned tests,
- implementation order,
- roadmap impact,
- supervisor view,
- general view,
- technical view,
- knowledge produced,
- section summaries,
- Apps Script resources,
- Google Sheets resources,
- deployment metadata,
- links,
- and provenance.

## 7.1 Honest bootstrap fields

The sidecar intentionally leaves these blank:

- formal project ID,
- project-record path,
- documentation run ID,
- catalog ID,
- catalog entry ID,
- actual session timing,
- final application version,
- final deployment verification timestamp,
- reviewer information.

These are not omissions caused by carelessness. They are explicit unknowns that do not yet exist.

## 7.2 Validation performed

The generated sidecar was checked for:

- valid JSON structure,
- complete top-level template coverage,
- ten implementation stages,
- fourteen acceptance criteria,
- thirteen planned tests,
- correct project/application naming,
- verified live Markdown path,
- and correct sidecar target path.

---

# 8. Planned Work-Session Startup

The user described the intended startup procedure for the actual implementation session.

The work will begin later this week in the ChatGPT Projects folder currently named:

```text
Inventory 3.0
```

That folder name can remain in place for the session even though the durable project identity in documentation is now **Inventory App**.

The user plans to upload:

- `workflow.json`,
- `implementation-plan.md`,
- the implementation-plan sidecar JSON,
- Apps Script source files,
- Google Sheets data or structure,
- and related project files.

## 8.1 First action should be registration, not coding

When the session starts, the correct first actions are:

1. Confirm the project identity.
2. Confirm the current application name.
3. Confirm the workflow and plan versions.
4. Confirm the source files and spreadsheet.
5. Confirm the current deployment.
6. Record the actual start time.
7. Freeze the approved plan as the baseline.
8. Record any discrepancy as an amendment.
9. Begin Stage 1 by preserving the current state.

This prevents the session from beginning with immediate code changes before context and provenance are established.

---

# 9. What We Learned About the Documentation Workflow

The conversation produced several broader lessons about why the workflow matters.

## 9.1 The system is a risk-control layer

The workflow is not merely a way to write down what happened.

It reduces risk by making visible:

- affected projects,
- relationships,
- dependencies,
- authorities,
- stages,
- tests,
- rollback paths,
- and completion conditions.

As the process becomes faster and more habitual, the team can handle more complex operations without proportionally increasing risk.

The progression is:

```text
repetition
    ↓
lower process overhead
    ↓
better relationship coverage
    ↓
fewer skipped steps
    ↓
more reliable execution
    ↓
safer complexity
```

## 9.2 It helps expose project relationships

Without a structured context package, related projects and shared data sources can be easy to miss.

The plan and sidecar force us to ask:

- What project owns this work?
- What other project supplies data?
- What integration is changing?
- What application consumes the result?
- Which files are authoritative?
- Which records are current?
- Which relationships are planned versus existing?

This will become increasingly important as future work spans several apps and datasets.

## 9.3 It helps the user follow and learn

The workflow has an educational function.

When work is broken into:

- stages,
- dependencies,
- decisions,
- risks,
- and tests,

the user can follow the reasoning instead of only seeing code output.

This makes lessons visible that would otherwise disappear inside a long troubleshooting process.

The documentation therefore serves not just as an archive, but as a learning scaffold.

## 9.4 It reduces working-memory load

A complex session may involve:

- spreadsheet structure,
- application source,
- deployments,
- project relationships,
- catalog records,
- test cases,
- unresolved questions,
- and next steps.

Without external structure, the user would have to hold too much of this in working memory.

The workflow transfers that burden into records.

This helps preserve attention for actual reasoning.

## 9.5 It supports end-session fatigue

The user noted that mental fatigue often becomes severe after approximately twelve hours of work.

This is a critical design consideration.

At the end of a long session, it becomes harder to:

- reconstruct chronology,
- explain decisions,
- remember what failed,
- distinguish complete from partial work,
- collect evidence,
- and identify the next step.

The workflow reduces this risk through:

- checkpoints,
- stage completion records,
- amendment logs,
- planned tests,
- evidence collection,
- and explicit unresolved-item lists.

Instead of requiring a tired user to reconstruct the entire day from memory, the system preserves the session as it unfolds.

## 9.6 It enables history viewing through the JSON Viewer

The sidecar structure makes work sessions inspectable later.

The JSON Viewer can expose:

- what was intended,
- what stages were planned,
- what risks were known,
- what tests were designed,
- which files were involved,
- what relationships mattered,
- what remained unresolved,
- and what later changed.

This turns past work into navigable operational history rather than buried chat transcripts.

Over time, the JSON Viewer could become a work-session history console.

## 9.7 It accelerates context creation

One of the strongest insights was the idea of **context creation acceleration**.

The ChatGPT Project folder supplies persistent background context:

- project vocabulary,
- prior conversations,
- recurring files,
- architecture,
- conventions,
- and working style.

The session package supplies bounded foreground context:

- the current objective,
- approved plan,
- relevant source files,
- assumptions,
- risks,
- tests,
- and authorities.

Together:

```text
persistent project context
        +
session-specific package
        +
current source files
        =
rapid verified work context
```

This reduces the cold-start problem.

The session should no longer require an hour of reconstruction before useful work can begin.

## 9.8 Faster context does not mean less review

Context creation acceleration is not the same as rushing.

The goal is to reach verified shared understanding faster.

The saved time comes from avoiding repeated reconstruction, not from skipping validation.

---

# 10. How We Plan to Measure the Workflow

The upcoming Inventory App session will be used to evaluate not only technical success but workflow effectiveness.

## 10.1 Context creation measurements

Possible measures include:

- time from opening the conversation to beginning productive work,
- number of files requested after the initial package,
- number of introductory explanations required,
- number of context gaps discovered,
- number of incorrect assumptions corrected before implementation,
- and whether project relationships were identified before coding.

## 10.2 Planning measurements

Possible measures include:

- time required to create the plan,
- number of plan amendments,
- number of stages completed as expected,
- number of scope changes,
- and whether risks identified in advance actually occurred.

## 10.3 Execution measurements

Possible measures include:

- number of skipped workflow steps,
- number of hidden dependencies discovered late,
- number of rollback events,
- number of repeated actions,
- amount of backtracking,
- and how often the plan prevented a mistake.

## 10.4 Learning measurements

Possible measures include:

- whether the user could explain what was happening,
- what lessons became visible because the work was staged,
- which concepts would likely have been missed without documentation,
- whether the plan improved understanding of the application architecture,
- and whether lessons could later be found in the JSON Viewer.

## 10.5 Fatigue and end-session measurements

Possible measures include:

- how much reconstruction was required at the end,
- whether evidence collection remained complete,
- whether fatigue caused skipped steps,
- whether unresolved items were captured,
- whether the next action remained clear,
- and whether the session could be resumed without reopening the full conversation.

## 10.6 Historical usefulness measurements

Possible measures include:

- whether the JSON Viewer can explain the session later,
- whether the sidecar makes the work discoverable,
- whether project relationships are understandable without the original chat,
- whether future planning can reuse the test and risk history,
- and whether the next session starts faster because of the preserved record.

---

# 11. Key Architectural Decisions Made

The following decisions are now effectively established.

## Decision 1: Stable project naming

```text
Inventory App
```

is the stable project name.

```text
Inventory 3.0
```

is the current application or release name.

## Decision 2: Plan authority

The Markdown implementation plan is the authoritative tactical plan.

## Decision 3: Sidecar role

The JSON sidecar describes and indexes the Markdown plan.

## Decision 4: Project-specific plan location

```text
documents/work-update-catalog/
projects/inventory-app/
implementation-plans/
implementation-plan.md
```

## Decision 5: Sidecar collection location

```text
documents/work-update-catalog/
sidecars/implementation-plans/
```

## Decision 6: Future catalog location

```text
documents/work-update-catalog/
catalogs/
```

## Decision 7: Bootstrap project handling

Meaningful names may be used before formal project IDs exist, but missing IDs and record paths must remain blank and explicitly unresolved.

## Decision 8: Current and status are separate

The active SDS record may still be partial, conflicting, or source unavailable.

## Decision 9: Historical records are retained

Superseded SDS revisions remain part of the registry with `current = FALSE`.

## Decision 10: Workflow changes are append-only during execution

The approved plan should not be silently rewritten to match later events. Material changes become amendments.

---

# 12. Artifacts Created or Confirmed

## 12.1 Markdown implementation plan

**Repository path:**

```text
documents/work-update-catalog/
projects/inventory-app/
implementation-plans/
implementation-plan.md
```

**Title:**

```text
Inventory 3.0 SDS Registry Rebuild and App Integration
```

## 12.2 Implementation-plan sidecar

**Generated filename:**

```text
implementation-plan-sds-sheet-upgrade-sidecar-3.0-draft.json
```

**Target repository path:**

```text
documents/work-update-catalog/
sidecars/implementation-plans/
implementation-plan-sds-sheet-upgrade-sidecar-3.0-draft.json
```

## 12.3 Supporting workflow

The work will use the project-change documentation workflow defining:

- project-context loading,
- intention preservation,
- bounded work-session registration,
- implementation planning,
- amendments,
- testing,
- checkpoint declaration,
- summary construction,
- reconciliation,
- debrief,
- sidecar generation,
- cataloging,
- publication,
- and closure.

## 12.4 Source resources recorded

The plan and sidecar record:

- Inventory-3.0 spreadsheet ID,
- SDS sheet ID,
- Apps Script source project,
- canonical deployment URL,
- deployment ID,
- current application version,
- chemical product catalog,
- expected changed files,
- expected unchanged files,
- and the documentation repository paths.

---

# 13. Remaining Open Items

The following remain intentionally unresolved:

- permanent Inventory App project ID,
- permanent project-record path,
- implementation-plan catalog ID,
- catalog entry ID,
- exact implementation-plan catalog filename,
- final sidecar repository commit,
- actual work-session start time,
- actual work-session stop time,
- final post-change application version,
- final deployment verification timestamp,
- official NMCI 51-CCGC SDS availability,
- and whether the older duplicate Markdown plan under the sidecar folder should be archived or removed.

These do not block beginning the work session once the plan is approved and scheduled.

---

# 14. Recommended Opening Protocol for the Next Session

When the implementation session begins, the opening message should establish:

```text
Primary project: Inventory App
Current application: Inventory 3.0
Workflow: klinswork-project-change-documentation-workflow
Plan: implementation-plan.md
Plan status: approved baseline
Sidecar schema: 3.0-draft
Current app version: ROUTE-TEST-0115
Current deployment: existing canonical /exec
Work-session start: [record actual time]
Current stage: Stage 1 — Preserve the current state
```

The session should then:

1. verify all uploaded files,
2. compare them with the plan,
3. identify any stale or missing context,
4. record amendments if necessary,
5. preserve the current SDS tab,
6. preserve current application evidence,
7. and begin the migration only after the before-state is recoverable.

---

# 15. Overall Conclusion

This morning’s work did more than produce an implementation plan and a sidecar.

It clarified the role of plans, sidecars, projects, versions, catalogs, and work-session context within the documentation system.

The most important shift is that the documentation process is no longer being designed only as an archive.

It is becoming an execution system that supports:

- preparation,
- context creation,
- learning,
- risk control,
- continuity,
- recovery,
- historical visibility,
- and increasingly complex technical work.

The upcoming Inventory App SDS registry session will be the first strong test of this design.

The technical objective is concrete: rebuild and integrate the SDS registry.

The process objective is equally important: determine whether the workflow helps us understand more, forget less, skip fewer steps, recover more easily, and preserve the work in a form that remains useful after the session ends.

The emerging principle is:

> A good documentation system should not merely prove that work happened. It should make the work easier to begin, safer to perform, easier to understand, less exhausting to finish, and more valuable to revisit.

