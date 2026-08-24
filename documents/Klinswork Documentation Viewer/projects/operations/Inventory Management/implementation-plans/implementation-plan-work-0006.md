---
document_type: implementation-plan
template_name: implementation-plan-template-1.0-draft
planning_mode: prospective
status: ready-for-linkage
created: 2026-08-16T16:40:00-06:00
updated: 2026-08-16T16:40:00-06:00
work_unit_id: WORK-0006
primary_project: Inventory Management
target_system: Inventory 3.0
authority_boundary: 2026-08-16T16:40:00-06:00
---

# Inventory 3.0 Roadmap and Documentation Reconciliation — Implementation Plan

> **Canonical filename:** `implementation-plan.md`
>
> **Authoring source:** `implementation-plan-template-1.0-draft.json`
>
> **Authority:** This Markdown file is the authoritative human-readable intended-work plan for `WORK-0006`. The earlier generated planning material is notes only and is not plan authority.
>
> **Historical-plan preservation requirement:** the current repository file `Inventory Management/implementation-plans/implementation-plan.md` is the older **Inventory 3.0 SDS Registry Rebuild and App Integration** plan. Before this new plan is installed at the canonical path, preserve the older plan under a non-conflicting descriptive filename (recommended: `implementation-plan-sds-registry-rebuild-and-app-integration.md`). Do not overwrite or rewrite the historical plan.

> **Template:** `implementation-plan-template-1.0-draft.json`
>
> **Work Unit:** `WORK-0006 — Inventory Management — Inventory 3.0 Roadmap and Documentation Reconciliation`
>
> **Planning mode:** `prospective`
>
> **Authority boundary:** `2026-08-16T16:40:00-06:00`
>
> **Plan role:** This Markdown document is the authoritative human-readable intended-work record for `WORK-0006`. The Work Unit Registry remains authoritative for current Work Unit state; Work Unit Activities remain authoritative for material timestamped history; the Work Implementation Session records actual execution.
>
> **Temporal rule:** The Inventory Management Project Definition, Inventory 3.0 System Summary, historical Inventory roadmap/design material, and the August 4 SDS implementation plan all predate this plan. They are starting-state evidence. This plan does not relabel any of that earlier work as prospectively planned under `WORK-0006`.
>
> **Implementation boundary:** This Work Unit is documentation, architecture, current-state verification, and roadmap work. The live Inventory application and datastore may be inspected as evidence. Product-feature implementation, source-code modification, inventory transaction changes, SDS rebuild execution, or live-data redesign require separately scoped work unless explicitly brought into this Work Unit through a material replanning event.

---

## 1. Plan Identity and Authority

| Field | Value |
|---|---|
| Plan title | Inventory 3.0 Roadmap and Documentation Reconciliation |
| Planning mode | `prospective` |
| Plan status | authoritative plan ready for Registry linkage; session not yet activated |
| Work Unit | `WORK-0006` |
| Work Unit kind | implementation |
| Primary Project | Inventory Management |
| Project ID | Unassigned |
| Target System | Inventory 3.0 |
| System ID | Unassigned |
| Formal session | yes |
| Formal session record | `work-implementation-session-2026-08-16-inventory-3-roadmap.md` |
| Plan sidecar | `implementation-plan-sidecar.json` |
| Plan created | `2026-08-16T16:40:00-06:00` |
| Plan authority begins | `2026-08-16T16:40:00-06:00` |

### Authority separation

```text
WORK UNIT REGISTRY
    current bounded-work state
        ↓
IMPLEMENTATION PLAN
    intended bounded work
        ↓
WORK IMPLEMENTATION SESSION
    actual session execution
        ↓
WORK UNIT ACTIVITIES
    material timestamped history
        ↓
SUMMARY / WORK UPDATE
    retrospective interpretation
```

The plan does not replace the Inventory Management Project Summary, Inventory 3.0 System Summary, System Roadmap, Resource Registry, System Roadmap Catalog, Viewer manifest, Architecture Changelog, or live implementation evidence.

The implementation-plan sidecar must be generated **from this completed Markdown plan after this plan is settled**. The sidecar is downstream structured metadata and must not drive or rewrite the plan.

---

## 2. Purpose, Goal, and Completion Rule

### 2.1 Prompting need

Inventory Management was the first Project Definition exemplar, created before the Work Queue Project Definition introduced a stronger distinction between:

- current-state System Summary;
- future-state System Roadmap;
- roadmap sidecar;
- cross-System roadmap catalog;
- formal Work Unit / implementation-plan / session execution;
- validation and closure against source-aware Viewer behavior.

Inventory 3.0 currently has a README, System Summary, and System Summary sidecar but no current System roadmap in its Project-local package. The System Roadmap Catalog already contains a planned Inventory 3.0 placeholder naming the intended files `inventory-3-roadmap.md` and `inventory-3-roadmap-sidecar.json`.

### 2.2 Goal

Verify the present Inventory 3.0 implementation baseline sufficiently to distinguish current truth from historical/planning evidence; reconcile the Inventory Management / Inventory 3.0 documentation where that verification requires changes; define the mature Inventory 3.0 target state in a durable System roadmap; create the roadmap's structured sidecar; promote Inventory 3.0 from planned to active in the System Roadmap Catalog; validate discovery/companion/Viewer behavior; and reconcile material Registry or architecture effects.

### 2.3 Completion rule

`WORK-0006` is complete when:

1. the relevant live Inventory app/datastore state has been inspected sufficiently to establish a current evidence baseline for roadmap design;
2. Inventory Management and Inventory 3.0 current-state documentation has been reconciled where verified evidence or current repository state makes existing annotations stale;
3. `inventory-3-roadmap.md` exists as the authoritative planned-direction document for Inventory 3.0;
4. `inventory-3-roadmap-sidecar.json` exists, is valid JSON, and resolves its roadmap companion;
5. `klinswork-system-roadmap-catalog-001.json` promotes Inventory 3.0 from its planned placeholder to an active roadmap entry without inventing Project/System IDs;
6. source-aware discovery and Viewer semantics preserve the distinction between Inventory 3.0 current-state System Summary and future-state System Roadmap;
7. the Project/System resume path is coherent for a context-naive session;
8. material Registry, Resource, Documentation, and architecture effects are assessed and reconciled where actually required.

---

## 3. Work Unit and Formal Session Relationship

### 3.1 Plan-time Work Unit state

| Field | Plan-time value |
|---|---|
| Work Unit ID | `WORK-0006` |
| Status | `planned` |
| Readiness | `ready` |
| Formal session required | `yes` |
| Session record target | `work-implementation-session-2026-08-16-inventory-3-roadmap.md` |
| Implementation plan registered | `no` at plan authority boundary |
| Known WUA | `WUA-0011 — work-unit-created` |

### 3.2 Activation gate

Formal active implementation begins only after:

- this authoritative `implementation-plan.md` has been reviewed and accepted as the governing plan for `WORK-0006`;
- the older SDS Registry implementation plan has been preserved under a non-conflicting descriptive filename so no historical plan is destroyed;
- the implementation-plan sidecar has been generated from this settled Markdown source;
- the formal Work Implementation Session record exists;
- the Work Unit row is reconciled with the plan/session paths;
- session initiation and activation are recorded through actually allocated Work Unit Activities.

Expected Registry state after activation:

```text
STATUS      active
READINESS   active
```

No future WUA IDs are allocated by this plan.

---

## 4. Work Placement and Authority

### Primary Project

**Inventory Management** — current Project meaning, scope, and boundaries belong to the Project Summary and Project Identity record.

Project ID remains unassigned.

### Target System

**Inventory 3.0** — principal known System inside Inventory Management.

System ID remains unassigned. No System Identity Entity Record is created by this Work Unit unless separately authorized through architecture work.

### Related Project

**Documentation** — supplies Record Profiles, Viewer/discovery infrastructure, Project/System documentation conventions, work-session architecture, and roadmap cataloging.

### Cross-System context

**Work Queue** — its roadmap's Inventory Integration area is relevant evidence for Inventory 3.0 integration requirements. This Work Unit does not modify Work Queue product behavior merely because the two roadmaps share an integration boundary.

### Registered Resources

| Resource | Role in this Work Unit |
|---|---|
| `RES-004 — Inventory app` | live application evidence |
| `RES-005 — Inventory app data sheet` | live datastore/schema evidence |
| `RES-010 — Building Map (Locations sheet)` | shared location authority where inventory/location relationships matter |
| `RES-011 — Online JSON viewer` | structured-document presentation validation |
| `RES-018 — Klinswork Chemical Product Catalog` | product/SDS structured evidence |
| `RES-041 — Project documentation root` | Projects Documentation Space |
| `RES-043 — Klinswork Resource Registry` | current Resource/Work Unit routing authority |
| `RES-044 — Documentation Viewer manifest` | current discovery snapshot |
| `RES-045 — Documentation Viewer manifest builder` | discovery/companion generation |
| `RES-046 — Documentation Viewer source registry` | configured Documentation Spaces |

No Resource identity is created by repository placement alone.

---

## 5. Planning Boundary and Prior Work

### 5.1 Planning mode

`prospective`

The work governed by this plan has not yet begun at the authority boundary.

### 5.2 Prior work that establishes the starting state

Already complete before this plan:

- Inventory Management Project Identity;
- Inventory Management README;
- Inventory Management Project Summary;
- Project Summary sidecar;
- Inventory 3.0 README;
- Inventory 3.0 System Summary;
- System Summary sidecar;
- the earlier Inventory SDS Registry rebuild implementation plan;
- historical Inventory 3.0 design/roadmap evidence referenced by current System documentation;
- Work Queue System roadmap and roadmap sidecar;
- System Roadmap Catalog with one active Work Queue roadmap and a planned Inventory 3.0 placeholder;
- Work Unit/session/implementation-plan architecture developed during `WORK-0001`.

### 5.3 Existing canonical-filename collision

The existing repository file:

```text
Inventory Management/implementation-plans/implementation-plan.md
```

is the older **Inventory 3.0 SDS Registry Rebuild and App Integration** plan.

That older plan is important historical/planning evidence. Because this new document is intended to become the canonical `implementation-plan.md` for the active `WORK-0006` body of work, the older plan must be preserved first.

Recommended preservation filename:

```text
implementation-plan-sds-registry-rebuild-and-app-integration.md
```

The preservation operation must:

- retain the old plan's content and historical meaning;
- avoid implying that the old plan was executed merely because it exists;
- update any direct path references that would otherwise break;
- never rewrite the old plan to resemble the current plan.

The new canonical plan may occupy `implementation-plan.md` only after that preservation step is complete.

### 5.4 Plan applies from

`2026-08-16T16:40:00-06:00`

---

## 6. Starting State

### 6.1 Project documentation

The Project package exists, but the current Inventory Management README contains creation-time status text that still describes records now physically present as planned or not yet created. The Project Summary likewise contains some creation-time pending statements.

These are documentation-freshness issues to verify and reconcile, not evidence that the underlying Project Definition is absent.

### 6.2 System documentation

Inventory 3.0 currently has:

```text
Inventory 3.0/
├── README.md
├── summaries/
│   └── system-summary.md
└── sidecars/
    └── system-summary-sidecar.json
```

The System Summary explicitly distinguishes historical roadmap/design evidence from current runtime truth and says current implementation requires live verification.

### 6.3 Roadmap state

The current System Roadmap Catalog has:

```text
active:
    Work Queue

planned:
    Inventory 3.0
    Calendar
```

The Inventory placeholder already reserves the intended names:

```text
inventory-3-roadmap.md
inventory-3-roadmap-sidecar.json
```

No roadmap content is asserted by the placeholder.

### 6.4 Live implementation baseline

Current Registry routes identify:

- `RES-004` as the Inventory 3.0 web application;
- `RES-005` as the Inventory 3.0 data workbook.

The older SDS implementation plan also preserves historical source/deployment information. Current behavior, schema, source-project state, and deployment details must be reverified before the new roadmap describes the present baseline as current fact.

### 6.5 Current uncertainty

Open questions include:

- current app capabilities versus historical design intent;
- current workbook sheet/schema details;
- which historical roadmap capabilities are actually implemented;
- present SDS integration state;
- current reporting/history/admin capabilities;
- current use of employee/cart/holder concepts;
- current Work Queue integration boundary;
- final System identity/boundary questions;
- which documentation annotations are stale versus still intentionally unresolved.

---

## 7. Context and Evidence Requirements

| ID | Required context | Purpose | Authority / route | Status at plan creation |
|---|---|---|---|---|
| CTX-01 | `WORK-0006` current state | bounded-work identity and completion | Work Units Registry | resolved |
| CTX-02 | Inventory Management Project Definition | Project scope and boundary | Project Identity / README / Project Summary | resolved |
| CTX-03 | Inventory 3.0 current System documentation | current documented interpretation | System README / System Summary / sidecar | resolved |
| CTX-04 | Existing Inventory implementation plan | preserve earlier intended SDS work separately | `implementation-plans/implementation-plan.md` | resolved |
| CTX-05 | Work Queue roadmap | cross-System inventory-integration requirements | Work Queue roadmap | resolved |
| CTX-06 | System Roadmap Catalog | planned/active roadmap state | `klinswork-system-roadmap-catalog-001.json` | resolved |
| CTX-07 | live Inventory app | present behavior evidence | `RES-004` | pending session execution |
| CTX-08 | live Inventory workbook | present schema/data-model evidence | `RES-005` | pending session execution |
| CTX-09 | current Resources | stable routes | `RES-043` | resolved |
| CTX-10 | Viewer discovery infrastructure | validation | `RES-044`, `RES-045`, `RES-046`, `RES-011` | resolved for route; execution pending |

### Evidence classes

**Current-state evidence**
- live application;
- live datastore/schema;
- current Registry;
- current repository files;
- freshly generated Viewer manifest;
- current Viewer behavior.

**Historical evidence**
- July Work Updates;
- prior Inventory versions;
- older roadmap/design documents;
- earlier app versions/deployment notes.

**Planning evidence**
- August 4 SDS implementation plan;
- Work Queue roadmap;
- existing Inventory roadmap/design source where preserved;
- candidate roadmap areas discussed before `WORK-0006`.

**Unverified/inferred**
- any feature not confirmed live and not clearly historical/planned.

---

## 8. Scope

### In scope

- preserve the older SDS Registry implementation plan before installing this plan at the canonical `implementation-plan.md` path;
- establish this document as the governing intended-work plan for `WORK-0006`;
- generate `implementation-plan-sidecar.json` from this settled Markdown source before session activation;
- inspect current Inventory app behavior;
- inspect current Inventory workbook structure relevant to System capabilities;
- compare current evidence to Inventory 3.0 README/System Summary;
- reconcile stale current-state documentation annotations where supported;
- define mature Inventory 3.0 target-state capabilities;
- incorporate integration responsibility from the Inventory side of Work Queue ↔ Inventory;
- create `inventory-3-roadmap.md`;
- create `inventory-3-roadmap-sidecar.json`;
- update the System Roadmap Catalog;
- regenerate/validate Viewer manifest;
- validate companion resolution and current-state/future-state semantics;
- test context-naive continuation;
- assess Registry/Resource/architecture effects;
- update session/Work Unit records through closure.

### Out of scope

- changing Inventory quantities;
- editing live Inventory transaction history;
- rewriting Inventory app source code;
- executing the SDS rebuild plan;
- implementing roadmap features;
- changing Work Queue application behavior;
- creating a System Identity schema;
- assigning `SYS-###` or `PROJ-###`;
- building a Relationship Registry;
- redesigning the global Resource Registry unless this Work Unit uncovers a material routing error.

### Non-goal

This plan does not attempt to make Inventory 3.0 "complete." It establishes a truthful current baseline and a durable planned direction from which future Work Units can be selected.

---

## 9. Target State

At closure:

```text
Inventory Management
    current Project definition
        ↓
Inventory 3.0
    README
    System Summary              = current-state interpretation
    System Summary sidecar
    Inventory 3 Roadmap         = future-state direction
    Roadmap sidecar
        ↓
System Roadmap Catalog
    active Inventory 3.0 entry
        ↓
Documentation Viewer
    current-state and roadmap records
    remain semantically distinct
```

The mature Inventory roadmap should be capability-oriented, not a file-edit list.

Candidate capability areas to investigate, combine, rename, or reject include:

- Inventory State & Reconciliation;
- Receiving;
- Usage / Consumption;
- Transfers;
- Employee Cart Inventory;
- Inventory Holder Inventory;
- Work Queue Integration;
- Employee Attribution;
- Product Management;
- SDS / Chemical Information;
- Locations & Building Map;
- Search & History;
- Reporting / Printing;
- QR Inventory Operations;
- Inventory Auditing;
- Corrections / Reversals;
- Administration;
- Data Integrity / Reliability.

These are design prompts, not pre-approved roadmap areas.

---

## 10. Implementation Stages

### Stage 1 — Verify the current Inventory 3.0 baseline

**Objective:** Establish enough current evidence to distinguish what Inventory 3.0 actually does today from historical roadmap/design intent.

**Actions**
- open `RES-004`;
- inspect the current user-facing application;
- open `RES-005`;
- inspect current sheet names and relevant schemas;
- verify current SDS/product/location/inventory/event concepts;
- identify current history/report/admin capabilities;
- identify current app/workbook behavior that differs materially from the System Summary;
- preserve discrepancies without prematurely editing source data.

**Deliverable**
- current-state verification notes recorded in the formal session;
- list of documentation corrections required before roadmap drafting.

**Exit criteria**
- roadmap authorship can distinguish current capability, historical evidence, and target capability.

---

### Stage 2 — Reconcile Inventory current-state documentation

**Objective:** Bring the Project/System orientation layer up to the same temporal/currentness discipline achieved during `WORK-0001`.

**Candidate files**
- Inventory Management `README.md`;
- Inventory Management `summaries/project-summary.md`;
- Inventory 3.0 `README.md`;
- Inventory 3.0 `summaries/system-summary.md`;
- corresponding sidecars only when their structured content becomes stale.

**Actions**
- correct creation-time "planned / not yet created / pending" statements contradicted by current repository state;
- update current-resource routing only from verified Registry evidence;
- preserve unassigned Project/System IDs;
- preserve System Identity deferral;
- preserve historical/planning/current evidence distinctions;
- add roadmap routing after roadmap creation.

**Exit criteria**
- current human-readable documentation no longer directs a future session through demonstrably stale creation-time status claims.

---

### Stage 3 — Define the mature Inventory 3.0 target state

**Objective:** Design the System roadmap through current evidence plus deliberate target-state discussion.

**Actions**
- identify stable product principles;
- identify roadmap areas;
- define each area's target;
- identify candidate future Work Units;
- record open determinations;
- define cross-System responsibilities explicitly;
- keep Inventory responsibility distinct from Work Queue/Scheduling/Documentation responsibilities.

**Inventory-side Work Queue integration concerns**
- transactional integrity;
- employee/cart resolution;
- source quantity;
- destination quantity;
- task linkage;
- product/quantity attribution;
- duplicate protection;
- atomicity/failure handling;
- correction/reversal;
- event history and reconciliation.

**Exit criteria**
- roadmap structure is coherent enough to author without treating preliminary brainstorming as settled architecture.

---

### Stage 4 — Create the Inventory 3.0 System Roadmap

**Objective:** Create the authoritative planned-direction document.

**Required artifact**

```text
systems/Inventory 3.0/summaries/inventory-3-roadmap.md
```

**Roadmap rules**
- System roadmap, not implementation plan;
- current baseline must be clearly separated from planned direction;
- candidate Work Units are future work candidates, not allocated `WORK-####` values;
- no invented `SYS-###` or `PROJ-###`;
- integrations describe Inventory-side responsibility;
- roadmap may be broad and multi-phase.

**Exit criteria**
- roadmap explains what mature Inventory 3.0 should become and why.

---

### Stage 5 — Create roadmap sidecar and promote catalog entry

**Required artifacts**

```text
systems/Inventory 3.0/sidecars/inventory-3-roadmap-sidecar.json
catalogs/klinswork-system-roadmap-catalog-001.json
```

**Actions**
- create a valid structured companion;
- use `generic-document` / `system-roadmap` semantics unless a dedicated roadmap profile has actually been established;
- promote `system-roadmap-inventory-3` from planned to active;
- preserve blank System/Project IDs;
- update active/planned counts and timestamp consistently;
- retain Calendar as a planned identity-reconciliation entry.

**Exit criteria**
- catalog routes to an actual Inventory roadmap and sidecar;
- no placeholder claims survive as though the roadmap were still absent.

---

### Stage 6 — Validate discovery, companions, and Viewer semantics

**Objective:** Prove that the new roadmap participates correctly in the source-aware Documentation architecture.

**Actions**
- regenerate the Viewer manifest using the current builder;
- verify JSON validity;
- verify roadmap sidecar discovery under Projects;
- verify companion resolution to `inventory-3-roadmap.md`;
- verify System Summary sidecar still resolves correctly;
- verify Project Summary sidecar still resolves correctly;
- verify Viewer distinguishes current System Summary from System Roadmap;
- verify no Entity Record is disguised as a sidecar.

**Exit criteria**
- validation passes or remaining defects are explicitly recorded and bounded.

---

### Stage 7 — Context-naive continuation test

**Objective:** Determine whether a future session can enter Inventory Management and select the correct current-state versus future-state authority.

**Expected route**

```text
Inventory Management Project
    ↓
Project README / Project Summary
    ↓
Inventory 3.0 README
    ↓
System Summary for what is true now
    or
System Roadmap for planned direction
    ↓
Resource Registry for live implementation routes
    ↓
new Work Unit selected from roadmap when appropriate
```

**Exit criteria**
- a fresh reader can explain which source answers "what is true now?" and which answers "what should Inventory 3.0 become?"

---

### Stage 8 — Registry, architecture, and closure reconciliation

**Objective:** Reconcile only the durable downstream effects actually produced.

**Assess**
- Work Unit Registry;
- Work Unit Activities;
- Resource Activities if a registered Resource changed materially;
- Architecture Changelog if architecture changed;
- Open Determinations;
- System Roadmap Catalog;
- Record Profile implications;
- Viewer manifest regeneration;
- Project/System README continuation routes.

**Exit criteria**
- completion rule reviewed;
- formal session explicitly closed;
- `WORK-0006` current state reconciled;
- remaining product work remains future roadmap-derived work rather than being smuggled into this Work Unit.

---

## 11. Dependencies and Risks

### D-00 — Preserve the existing SDS implementation plan

**Required for:** canonical installation of this plan and session activation.

The current canonical filename is occupied by the older SDS Registry plan. Preserve that source before replacement. Recommended preserved filename: `implementation-plan-sds-registry-rebuild-and-app-integration.md`.

**Risk:** silent overwrite would destroy planning history and violate temporal truth.

**Mitigation:** preserve first, verify both files, then link the new canonical plan to `WORK-0006`.


### D-01 — Live app accessibility
Required for Stage 1. If the deployed app cannot be inspected, use source/datastore evidence and record the limitation rather than guessing.

### D-02 — Live datastore accessibility
Required for Stage 1. Do not edit operational inventory data merely to understand the schema.

### D-03 — Current Project/System documentation
Resolved through repository records.

### D-04 — Roadmap catalog
Resolved through current catalog.

### D-05 — Work Queue roadmap
Required to align the Inventory side of the cross-System transfer/integration contract without rewriting Work Queue authority.

### Risks

**R-01 — Historical roadmap language mistaken for current behavior**  
Mitigation: require live verification before current-state claims.

**R-02 — Roadmap becomes implementation backlog**  
Mitigation: write capability areas and candidate Work Units; keep file edits and code tasks out of the roadmap.

**R-03 — Inventory absorbs neighboring Project authority**  
Mitigation: preserve Project/System boundaries explicitly.

**R-04 — Current documentation cleanup rewrites history**  
Mitigation: reconcile only current documents; leave historical artifacts historically accurate.

**R-05 — Product work expands into the documentation Work Unit**  
Mitigation: stop/reassess and create a future Work Unit candidate.

**R-06 — Catalog promotion invents identity**  
Mitigation: preserve blank Project/System IDs.

---

## 12. Acceptance Criteria

- **AC-01 — Current baseline:** The session records a verified current Inventory 3.0 baseline sufficient for roadmap design.
- **AC-02 — Evidence discipline:** Current, historical, planning, and unverified statements remain distinguishable.
- **AC-03 — Current documentation:** Material stale current-state annotations are reconciled without rewriting historical records.
- **AC-04 — Roadmap:** `inventory-3-roadmap.md` exists and clearly separates current baseline from planned target state.
- **AC-05 — Roadmap sidecar:** `inventory-3-roadmap-sidecar.json` is valid and resolves the human-readable roadmap.
- **AC-06 — Catalog:** Inventory 3.0 is an active roadmap entry; Calendar remains planned; no invented Project/System IDs.
- **AC-07 — Viewer discovery:** source-aware manifest discovers the intended Inventory roadmap record with valid JSON and resolved companion.
- **AC-08 — Viewer semantics:** System Summary and System Roadmap remain semantically distinct.
- **AC-09 — Project/System boundary:** Inventory, Work Queue, Scheduling, Documentation, Resources, and operational environment are not collapsed.
- **AC-10 — Resume path:** a context-naive session can choose the correct authority for current state versus planned direction.
- **AC-11 — Registry/architecture:** material downstream effects are assessed and reconciled.
- **AC-12 — Scope:** no live Inventory feature implementation is falsely represented as part of this Work Unit.

---

## 13. Planned Validation and Tests

| Test | Verification | Expected result |
|---|---|---|
| T-01 | inspect live Inventory app/workbook | current baseline captured with limitations |
| T-02 | compare current docs to repository/live state | stale current annotations identified/reconciled |
| T-03 | parse roadmap sidecar JSON | valid JSON |
| T-04 | inspect System Roadmap Catalog | Inventory active; counts/timestamps consistent; IDs blank |
| T-05 | regenerate Viewer manifest | no new invalid JSON |
| T-06 | inspect Inventory roadmap manifest record | companion resolved |
| T-07 | inspect System Summary + roadmap Viewer behavior | current/future meanings remain distinct |
| T-08 | context-naive routing test | correct authority selected for current vs planned state |
| T-09 | Registry effect review | only material Resource/architecture changes recorded |
| T-10 | completion-rule review | all required outcomes satisfied or explicitly bounded |

Actual results belong in the Work Implementation Session, not in this plan.

---

## 14. Implementation Order and Gates

```text
WORK-0006 registered
        ↓
plan + sidecar + session record created
        ↓
session initiated / activated
        ↓
Stage 1 current verification
        ↓
Stage 2 current-doc reconciliation
        ↓
Stage 3 target-state design
        ↓
Stage 4 roadmap
        ↓
Stage 5 sidecar + catalog
        ↓
Stage 6 Viewer validation
        ↓
Stage 7 context-naive continuation test
        ↓
Stage 8 downstream reconciliation + closure
```

Stage 3 must not freeze mature capability claims before Stage 1 distinguishes current state from historical assumptions.

---

## 15. Stop and Reassessment Conditions

Stop and reassess if:

- current implementation evidence contradicts the assumed Inventory 3.0 System placement;
- app/datastore authority cannot be resolved sufficiently to support roadmap baseline claims;
- continuing requires inventing Project/System/Resource/Work Unit/WUA identity;
- product implementation begins expanding into this documentation/roadmap Work Unit;
- roadmap work requires a global architecture decision not yet made;
- current state cannot be separated from historical/planning evidence;
- source-aware discovery requires changing Record Profile semantics beyond a bounded compatibility fix;
- a catalog change would destroy historical or planned-state meaning rather than promote it cleanly.

---

## 16. Registry, Documentation, and Architecture Reconciliation

At closure assess:

- `WORK-0006` current state and result;
- all material WUAs;
- whether any Resource current route changed;
- whether an Activity entry is required for `RES-044`, `RES-045`, `RES-041`, `RES-004`, `RES-005`, or another Resource;
- whether the Architecture Changelog needs an entry;
- whether the new roadmap authoring experience exposes a Record Profile gap;
- whether the System Roadmap Catalog remains internally consistent;
- whether Project/System README routes need roadmap links;
- whether `plan-build-roadmap.md` remains useful as planning provenance or should be marked superseded/absorbed without deletion.

Do not create downstream identifiers merely because a reconciliation category exists.

---

## 17. Closure Conditions and Handoff

A formal session may close while future Inventory roadmap work remains extensive.

`WORK-0006` itself completes only when its completion rule is satisfied.

Expected handoff after completion:

```text
Inventory 3.0 roadmap
    ↓
select one bounded candidate capability
    ↓
allocate a future Work Unit
    ↓
create implementation plan if needed
    ↓
execute in a separate formal session
```

The first future implementation Work Unit should come from verified roadmap priority, not from this plan guessing which feature should be coded first.

---

## 18. Provenance and Interpretation Limits

Primary planning sources:

- earlier generated Inventory-roadmap planning material, treated strictly as non-authoritative notes;

- current Inventory Management repository package;
- current Inventory 3.0 repository package;
- `plan-build-roadmap.md`;
- existing Inventory SDS implementation plan;
- Work Queue roadmap;
- current System Roadmap Catalog;
- current Resource Registry;
- `implementation-plan-template-1.0-draft.json`;
- current implementation-plan sidecar template;
- current Work Implementation Session template;
- `WORK-0006` / `WUA-0011`.

Interpretation limits at plan creation:

- current live Inventory app behavior has not yet been inspected under this Work Unit;
- current workbook schema has not yet been inspected under this Work Unit;
- historical roadmap statements remain historical/planning evidence until verified;
- no Project/System IDs are assigned;
- no claim is made that the August 4 SDS implementation plan was fully executed.

---

## Template Conformance

This plan was authored using the required structure and authority rules of `implementation-plan-template-1.0-draft.json`. It is intentionally detailed enough for context-naive reconstruction while keeping actual execution out of the plan. The structured sidecar is downstream and has not been created as part of this document-generation step.

## Plan Activation Check

- [x] Work Unit exists.
- [x] Work Unit goal/completion rule are bounded.
- [x] Planning mode is prospective.
- [x] Prior work is separated from plan authority.
- [x] Project/System/Resource placement is explicit.
- [x] Implementation stages are defined.
- [x] Acceptance criteria are defined.
- [x] Planned tests are defined.
- [x] Stop/reassessment conditions are defined.
- [x] Session record target is defined.
- [ ] Older SDS implementation plan is preserved under a non-conflicting filename.
- [ ] This canonical `implementation-plan.md` is installed in the Project implementation-plan collection.
- [ ] `implementation-plan-sidecar.json` is generated from this settled Markdown source.
- [ ] Plan is linked in Work Unit Registry.
- [ ] Session is initiated.
- [ ] Session is activated.

The unchecked items are downstream installation, sidecar, Registry, and formal-session events. They must occur in that order; none is treated as completed merely because this authoritative plan now exists.
