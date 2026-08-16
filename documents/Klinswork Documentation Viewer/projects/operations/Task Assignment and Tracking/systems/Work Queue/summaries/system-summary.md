# Work Queue — System Summary

| Field | Current value |
|---|---|
| **Document role** | Human-readable System definition and current System interpretation |
| **System** | Work Queue |
| **Parent Project** | Task Assignment and Tracking |
| **System ID** | Unassigned; permanent `SYS-###` assignment is intentionally deferred |
| **System Identity Entity Record** | Not created |
| **Companion sidecar** | `../sidecars/system-summary-sidecar.json` — current |
| **System Roadmap** | `work-queue-roadmap.md` |
| **Technical documentation Resource** | `RES-047` — Work Queue app technical manual |
| **Current registered application Resource** | `RES-002` — Work Queue app |
| **Current registered datastore Resource** | `RES-003` — Work Queue app data sheet |
| **Current-state confidence** | High for semantic placement, current Registry routing, current Work Queue datastore structure, the separate registered employee/personnel source, and current shared Locations structure; medium for detailed runtime behavior because current Apps Script source/deployment logic was not directly inspected in this reconciliation step |
| **Last reconciled** | 2026-08-16 |
| **Reconciliation timestamp** | 2026-08-16T10:25:00-06:00 |

---

## 1. Document purpose and authority

This document is the human-readable System Summary for **Work Queue**.

Its purpose is to answer:

> **What coherent implemented mechanism currently serves the Task Assignment and Tracking Project?**

It describes Work Queue as a System rather than as a synonym for the parent Project or as only one visible application screen.

This Summary explains:

- Work Queue's role inside the Task Assignment and Tracking Project;
- the current working System boundary;
- the current registered application and datastore Resources;
- the currently observed datastore structure;
- the task, template, activity-history, settings, and location-mapping models visible in current data;
- current employee-attribution and location relationships;
- the documented Inventory integration boundary;
- the distinction among current verified evidence, dated technical documentation, historical implementation evidence, and roadmap intent;
- current limitations and evidence conflicts;
- relevant Resources and shared dependencies;
- unresolved System questions;
- the next documentation and verification work.

This Summary is the explanatory authority for the **current Work Queue System interpretation expressed here**.

It is not:

- a System Identity Entity Record;
- an authority for a permanent `SYS-###`;
- a replacement for the parent Project Summary;
- a replacement for the Work Queue roadmap;
- a replacement for the Resource Registry;
- proof that every technical-manual statement remains current;
- proof that every roadmap capability exists;
- a substitute for current source code, deployment configuration, or executable testing when detailed runtime behavior matters;
- a formal Relationship Registry record.

The authority model is deliberately distributed:

```text
Task Assignment and Tracking Project identity
    → ../../project-identity.json

Project purpose / scope / boundaries
    → ../../summaries/project-summary.md

Work Queue System-local orientation
    → ../README.md

Work Queue current System interpretation
    → this System Summary

Structured interpretation of this System Summary
    → ../sidecars/system-summary-sidecar.json

Work Queue planned future direction
    → work-queue-roadmap.md

Resource identity / current location / routing
    → Klinswork Resource Registry

Detailed current application behavior
    → current Apps Script source / deployment / datastore / executable verification

Historical implementation
    → dated Work Updates / historical records

Current Work Unit state
    → Work Unit Registry

Material Work Unit history
    → Work Unit Activities

Bounded intended work
    → implementation plans

Detailed bounded execution
    → Work Implementation Session + execution evidence
```

The companion sidecar may structure this Summary for discovery and Viewer presentation.

It must not replace the Markdown source as the human-readable authority for the interpretation expressed here.

---

## 2. Relationship to the Task Assignment and Tracking Project

Work Queue exists within the operational meaning supplied by the **Task Assignment and Tracking Project**.

Current working relationship:

```text
Task Assignment and Tracking
        ↓
     Work Queue
```

The Project is the durable undertaking concerned with reliable operational knowledge and control of discrete work.

Work Queue is the principal known System presently used to support that undertaking.

Therefore:

```text
Task Assignment and Tracking
    != Work Queue
```

The Project can survive replacement, redesign, or renaming of Work Queue.

Likewise, changing:

- the Apps Script deployment;
- the Google Sheets datastore;
- the user interface;
- the repository location;
- the application version;
- the location source;
- the employee source;
- the Inventory integration mechanism;

does not automatically establish a new Project.

Whether a sufficiently large implementation change would establish a new **System** is a System Identity question that remains intentionally unresolved.

The current semantic model is:

```text
Klinswork
└── Operations                                      [Project]
    └── Task Assignment and Tracking                [Project]
        └── Work Queue                              [System]
            ├── Work Queue app                     [Resource]
            ├── Work Queue data workbook           [Resource]
            ├── task / activity datasets           [Resources / data]
            ├── shared Locations                   [shared Resource]
            ├── employee/personnel context         [shared / related data]
            ├── Inventory relationship             [cross-Project integration]
            ├── technical documentation            [Resource]
            ├── current-state documentation
            └── future-state roadmap
```

---

## 3. Why System Identity remains deferred

No formal:

```text
system-identity.json
```

is created by this System Summary.

No permanent:

```text
SYS-###
```

is assigned.

That is deliberate.

The current Project Definition work is testing whether a System can be made understandable through:

```text
README.md
summaries/system-summary.md
sidecars/system-summary-sidecar.json
roadmap records
Resource references
current implementation evidence
```

before Klinswork freezes a formal System Identity schema.

The Work Queue case raises useful System Identity questions:

- Is `Work Queue` the durable canonical System name or partly an application label?
- What exact boundary separates the System from its Apps Script application?
- What exact boundary separates the System from its datastore?
- Are task lifecycle rules intrinsic System facts or implementation facts?
- Which shared employee, location, Inventory, Documentation, and Scheduling relationships should remain external?
- How much implementation replacement can occur while preserving System continuity?
- What facts belong in a future System Entity Record rather than this Summary?

For now:

> **Describe Work Queue accurately; do not invent System identity merely to make the documentation package look complete.**

---

## 4. System purpose

Work Queue is the coherent operational mechanism used to represent and manage discrete work within the Task Assignment and Tracking Project.

At the System level, its purpose is to connect:

```text
work item
    ↓
structured context
    ↓
assignment / responsibility
    ↓
state change
    ↓
notes / evidence
    ↓
completion
    ↓
activity history
    ↓
downstream operational relationships
```

The System currently provides an application/data environment in which housekeeping work can be created, assigned, located, tracked, updated, and completed.

Current evidence also shows that the data model has grown beyond a simple task list.

It contains structures for:

- task identity;
- creator identity;
- status;
- priority;
- category;
- stable location identity;
- location labels and room context;
- assignment labels;
- stable Assigned Employee ID;
- start/completion/update timestamps;
- completion notes;
- task templates;
- holder/inventory completion context;
- task activity events;
- application settings;
- mappings from location types/areas to task templates.

This makes Work Queue a coherent operational System rather than merely a spreadsheet of task descriptions.

---

## 5. Current architecture baseline

### 5.1 Current registered implementation shape

The Resource Registry currently identifies:

```text
RES-002   Work Queue app
           Resource type: APPLICATION
           Registered implementation: Apps Script web application

RES-003   Work Queue app data sheet
           Resource type: DATA STORE
           Registered workbook: Work Queue 2.1 Test Data

RES-012   Work Queue Tasks dataset

RES-013   Work Queue Employees dataset
           Current source: separate Employees workbook

RES-014   Work Queue Locations reference

RES-047   Work Queue app technical manual
```

The current technical manual describes the visible application as an **Apps Script web app** and explicitly states that Work Queue is broader than that application surface.

Direct Registry and Google Sheets reconciliation now shows that the operational data needed by Work Queue is distributed across more than one workbook.

A useful current architecture model is therefore:

```text
user
  ↓
Work Queue Apps Script web application
  ↓
task / template / settings / activity behavior
  ↓
Work Queue operational datastore
  │   ├── Tasks
  │   ├── Task_Templates
  │   ├── Settings
  │   ├── Task_Activity
  │   └── Location_Task_Map
  │
  └── shared / integrated data context
      ├── RES-013 Employees workbook
      │   ├── Employees
      │   ├── Assignments
      │   └── Weekly_Schedule
      ├── Locations / Building Map
      └── Inventory relationships
```

Around that operational core are supporting documentation, development, deployment, access, and maintenance layers.

The current architecture therefore should not be interpreted as:

```text
one application
+
one workbook
=
the whole System
```

Work Queue depends on registered shared data sources and integrations whose identities remain distinct from the visible app and from the primary Work Queue task datastore.

### 5.2 System versus ecosystem

The technical manual uses the term **Work Queue ecosystem** broadly.

That source includes:

- application and operational data;
- employee/personnel records;
- Inventory and SDS relationships;
- Documentation;
- JSON workflows and schemas;
- GitHub / GitHub Pages;
- Google Sites;
- Email Composer;
- Google Drive / Apps Script resources;
- VS Code;
- access infrastructure;
- human development/maintenance work.

This breadth is valuable as an architecture map.

For the present System Summary, not every item in that ecosystem is treated as intrinsic Work Queue System membership.

A practical boundary is:

```text
CORE / DIRECT SYSTEM MECHANISM
    Work Queue application
    task data
    templates
    task-activity history
    settings/configuration used by the app
    task-location/template mapping
    assignment/person references used by tasks
    task-related holder/inventory linkage

SHARED / INTEGRATED CONTEXT
    RES-013 Employees workbook
    canonical Locations / Building Map
    Inventory Management
    Scheduling
    SDS/product context where task behavior requires it

SUPPORTING INFRASTRUCTURE
    Documentation Project
    GitHub / GitHub Pages
    Google Drive
    Apps Script hosting/deployment
    VS Code
    publication and communication tooling
```

The exact final System membership boundary remains an open architecture question.

---

## 6. Current Work Queue operational datastore

### 6.1 Workbook identity

The Resource Registry currently routes the primary Work Queue operational datastore through:

```text
RES-003
Work Queue app data sheet
```

The current Google Sheets workbook title is:

```text
Work Queue 2.1 Test Data
```

Its currently visible sheets are:

```text
Tasks
Task_Templates
Settings
Task_Activity
Location_Task_Map
```

This sheet list was verified directly from the current registered workbook during this reconciliation.

The workbook currently has no visible `Employees` sheet.

That is **not now treated as a discrepancy**.

Direct follow-up verification located the employee/personnel source in a separate Google Sheets workbook titled:

```text
Employees
```

and the Resource Registry was corrected so:

```text
RES-013
Work Queue Employees dataset
```

now routes to that separate workbook.

The architecture is therefore:

```text
RES-003
    = primary Work Queue operational task/configuration/history datastore

RES-013
    = separate shared employee/personnel dataset used by Work Queue
```

This separation is consistent with the broader Klinswork principle that a System may consume shared Resources without owning or physically co-locating them.

---

## 7. Current Tasks model

The current `Tasks` sheet exposes the following populated schema fields:

```text
Task ID
Created At
Created By
Status
Priority
Category
Location ID
Location Name
Unit Name
Room / Area Name
Room Number
Description
Assigned To
Started At
Completed At
Updated At
Completion Note
Archived
Template ID
Related Holder ID
Completion Event Type
Completion State
Related Holder Event ID
Assigned Employee ID
```

The physical sheet currently has 26 columns; the last two columns are presently unnamed/unused in the retrieved header row.

### 7.1 Task identity

Current task records use stable-looking identifiers such as:

```text
WQ-20260804-526849
```

The existence of a dedicated `Task ID` field supports task identity independently of row number or description.

This Summary does not infer the complete ID-allocation algorithm or uniqueness guarantees without source-code verification.

### 7.2 Creation and authorship

Current task data includes:

```text
Created At
Created By
```

This allows the record to preserve when a task was created and an identifier for the creating actor.

The current samples use email-form creator values.

Whether `Created By` represents authenticated current-user identity, a deployment identity, or another mechanism should be verified in current application source/authentication logic.

### 7.3 Status

Current data and activity history demonstrate at least these observed states:

```text
Pending
In Progress
Completed
```

Current `Task_Activity` data demonstrates transitions such as:

```text
Pending
    ↓
In Progress
    ↓
Completed
```

and also examples of:

```text
Pending
    ↓
Completed
```

The observed data therefore proves that those states/transitions exist in recorded history.

It does **not** establish a complete controlled state machine or prove that all allowed transitions are correct.

The roadmap's broader lifecycle vocabulary remains target-state planning until adopted and verified.

### 7.4 Priority and category

Current task records contain:

```text
Priority
Category
```

The current Settings sheet defines:

```text
DEFAULT_PRIORITY = Normal
```

Current task templates also specify a default priority.

The complete controlled vocabulary for priority/category should be verified from current application/template/configuration logic before being treated as frozen System semantics.

### 7.5 Location context

Task records preserve both stable location identity and human-readable location context:

```text
Location ID
Location Name
Unit Name
Room / Area Name
Room Number
```

This is important because Work Queue can retain a stable shared identifier while still preserving readable operational labels.

The current model should avoid using display names as substitutes for stable location identity.

### 7.6 Assignment

Current Tasks schema includes:

```text
Assigned To
Assigned Employee ID
```

This is a significant distinction.

`Assigned To` can preserve a readable label.

`Assigned Employee ID` allows the task model to preserve a stable person reference where the current application successfully resolves one.

The technical manual states that the current application uses employee records to populate the Assigned Employee control and that Tasks can preserve the selected person through stable Assigned Employee ID rather than relying only on typed names.

Because the currently registered datastore no longer exposes a visible Employees sheet, the exact present source of those employee records requires reconciliation.

### 7.7 Completion

Current task records include:

```text
Started At
Completed At
Updated At
Completion Note
```

The Settings sheet currently states:

```text
REQUIRE_COMPLETION_NOTE = TRUE
```

Current data contains completion-note values and completed timestamps.

The existence of these fields and current data supports completion tracking.

Detailed enforcement of required completion notes should still be verified from application logic rather than inferred only from the setting.

### 7.8 Archival

Current Tasks data includes:

```text
Archived
```

Current observed rows contain `FALSE`.

The presence of the field establishes an archival dimension in the current data model.

This Summary does not infer archival workflow, retention rules, or visibility behavior without further evidence.

---

## 8. Current Task Activity / history model

The current datastore contains a dedicated:

```text
Task_Activity
```

sheet.

Its current fields are:

```text
Activity ID
Task ID
Activity Type
Created At
Created By
Old Value
New Value
Note
```

Observed current/historical-in-workbook activity types include:

```text
TASK_CREATED
NOTE_ADDED
TASK_STARTED
TASK_COMPLETED
```

This is important architectural evidence.

Work Queue is not limited to storing only current task rows.

It also preserves event-oriented task history.

Current activity records preserve:

- stable activity identity;
- related task identity;
- activity type;
- timestamp;
- acting/creating identity;
- old value;
- new value;
- note.

This supports later reconstruction of task-state change.

However, the current activity history should not be assumed to cover every meaningful change.

Questions still requiring verification include:

- Is assignment change recorded as an activity?
- Is reassignment recorded distinctly?
- Are priority/category/location edits recorded?
- Are completion corrections recorded?
- Are inventory effects linked back into task activity?
- Are rejected/released/reopened transitions supported?
- Can a task history ever be rewritten rather than appended?
- What is the authoritative behavior when a task row and activity history disagree?

The roadmap's mature event-history model should be compared against current behavior after current source inspection.

---

## 9. Current task templates

The datastore contains:

```text
Task_Templates
```

with current fields:

```text
Template ID
Category
Template Name
Default Description
Default Priority
Active
Sort Order
Holder Required
Required Holder Type
Required Product Category
Completion Event Type
Completion State
```

This establishes that Work Queue currently has a template/configuration layer rather than requiring all recurring task semantics to be hard-coded into individual task records.

Current template data includes operational task categories such as:

- Carpet Care;
- Supplies;
- General Cleaning;
- Windows;
- Other;
- General.

The presence of:

```text
Holder Required
Required Holder Type
Required Product Category
Completion Event Type
Completion State
```

shows that templates can carry structured completion/integration metadata related to Inventory-holder behavior.

The exact current enforcement rules for these template fields must be verified in application source.

---

## 10. Current settings / configuration

The current `Settings` sheet contains at least these active settings:

```text
APP_VERSION = 2
DEFAULT_PRIORITY = Normal
REQUIRE_COMPLETION_NOTE = TRUE
ENABLE_EMAIL_NOTIFICATIONS = FALSE
LOCATION_CACHE_MINUTES = 10
```

This proves that some routine behavior is already data-configurable.

It also creates an important versioning nuance:

```text
Resource / workbook label:
    Work Queue 2.1 Test Data

Current Settings value:
    APP_VERSION = 2
```

This Summary does not infer a semantic version reconciliation from those labels.

The difference should remain visible until the application/versioning convention is explicitly resolved.

The current setting:

```text
ENABLE_EMAIL_NOTIFICATIONS = FALSE
```

supports the interpretation that notification infrastructure is not currently enabled through this setting.

It does not prove that no other notification path exists elsewhere.

---

## 11. Current location-to-task mapping

The current datastore contains:

```text
Location_Task_Map
```

with fields:

```text
Location Type
Room / Area Name
Template ID
Sort Order
Active
```

Current rows map location contexts such as:

```text
Restroom
Staff Restroom
Resident Restroom
Resident Room
```

to task-template IDs.

This is a significant current architecture feature.

It allows Work Queue to derive or present context-relevant work templates according to physical location/area type rather than treating all templates as equally applicable everywhere.

The mapping remains separate from the canonical location record itself.

That separation is correct:

```text
canonical location identity
    → shared Locations / Building Map

Work Queue location-to-task behavior
    → Location_Task_Map
```

---

## 12. Shared Locations / Building Map relationship

The current Resource Registry identifies:

```text
RES-010
Building Map (Locations sheet)

RES-014
Work Queue Locations reference
```

Both route to the current shared workbook:

```text
Klinswork_Locations
```

The current workbook contains a `Locations` sheet with fields including:

```text
Location ID
Parent ID
Unit / Area
Room / Area Name
Room Number
Location Type
Display Name
Active
Work Queue Enabled
Inventory Enabled
Calendar Enabled
Sort Order
Notes
```

Current sample data shows hierarchical stable location IDs such as:

```text
MEADOWS
JUNIPER-N
JUNIPER-N-NS
JUNIPER-N-HK-CLOSET
```

and explicit capability flags:

```text
Work Queue Enabled
Inventory Enabled
Calendar Enabled
```

This supports the current architectural interpretation that Locations is a **shared canonical location source** used across operational systems.

Work Queue consumes those identifiers.

It should not create a private competing master location identity simply because task behavior needs location context.

Current relationship:

```text
shared Locations / Building Map
        ↓
stable Location ID + descriptive context
        ↓
Work Queue Tasks
        ↓
Location_Task_Map
        ↓
context-relevant task behavior
```

The broader Building Map Project/System ownership model remains unresolved.

---

## 13. Employee / personnel relationship

Employee identity is operationally important because assignment should be attributable to a stable person rather than only a display string.

The current employee-source location has now been directly reconciled.

### 13.1 Current Tasks schema

The current Work Queue task model contains:

```text
Assigned To
Assigned Employee ID
```

This proves that the task datastore has a place for both:

```text
human-readable assignee label
+
stable employee identity reference
```

The stable identity field prevents task attribution from depending solely on a typed display name.

### 13.2 Registered employee/personnel source

The current Resource Registry identifies:

```text
RES-013
Work Queue Employees dataset
```

Its current registered source is the separate Google Sheets workbook:

```text
Employees
Workbook ID:
1It_C3s-4Nwn7bFKt_InO5bblpF3Fo6dJzsF_WwKhnJo
```

Direct workbook verification shows three sheets:

```text
Employees
Assignments
Weekly_Schedule
```

The `Employees` sheet currently exposes:

```text
Employee_ID
Display_Name
Email
Active
Assignment_Eligible
Role
Notification_Enabled
Program_Update_Enabled
Created_At
Updated_At
```

Current records use stable identifiers in the form:

```text
EMP-###
```

This supplies a real shared personnel identity layer rather than requiring Work Queue to derive employee identity from task rows.

### 13.3 Assignment / schedule context in the employee workbook

The same workbook contains an `Assignments` sheet with fields including:

```text
Assignment_ID
Work_Date
Employee_ID
Location_ID
Assignment_Type
Shift_Start
Shift_End
Status
Notes
Created_At
Updated_At
```

Directly observed records link:

```text
Employee_ID
    ↓
Location_ID
    ↓
work date / shift / assignment status
```

This is useful evidence that the employee workbook is broader than a name lookup.

It also contains operational assignment/schedule context that may be consumed by Work Queue or Scheduling-related workflows.

The presence of `Assignments` and `Weekly_Schedule` does **not** by itself prove that the current Work Queue deployment reads those sheets at runtime.

That remains a source/deployment verification question.

### 13.4 Relationship to the technical manual

The Work Queue technical manual states that:

- the Employees sheet is an active personnel source for Work Queue;
- employee records populate the Assigned Employee control;
- Tasks can preserve the selected person through stable Assigned Employee ID.

The earlier apparent conflict came from a stale Registry location for `RES-013`, not from the absence of an employee workbook.

The physical-source issue was resolved on 2026-08-16 by direct discovery and inspection of the separate Employees workbook.

The Registry entry was then corrected while preserving the stable Resource identity:

```text
RES-013
```

The corresponding Resource Activity is:

```text
ACT-0081
Employee dataset location reconciled
```

### 13.5 Current authority boundary

The present working interpretation is:

```text
Employees workbook / RES-013
    = shared employee/personnel and assignment-context Resource

Work Queue Tasks
    = task-specific assignee reference and work history

Work Queue
    != personnel master merely because it consumes employee identities
```

The exact long-term personnel authority and the exact runtime method by which the Work Queue application loads `RES-013` remain implementation/architecture questions, but the current physical employee-data source is no longer unresolved.

---

## 14. Inventory relationship

Work Queue has a real but incomplete integration relationship with Inventory Management.

### 14.1 Current task schema

The current Tasks model contains:

```text
Related Holder ID
Completion Event Type
Completion State
Related Holder Event ID
```

The current Task_Templates model contains:

```text
Holder Required
Required Holder Type
Required Product Category
Completion Event Type
Completion State
```

These fields demonstrate an implemented data model for inventory-holder-aware task completion.

### 14.2 Technical-manual evidence

The technical manual states:

> Completing an applicable task can create an `Inventory_Holder_Event` associated with the exact inventory holder and location.

The same source explicitly states that further propagation, such as deducting the consumed item from `Cart 01`, remains planned rather than verified current behavior.

That distinction is preserved here.

### 14.3 Current datastore evidence

Current task/activity data contains inventory-holder test/fault-reproduction history.

For example, the datastore includes a holder-required template test record with:

```text
Completion Event Type = Refilled
Completion State = Full
Related Holder ID = blank
```

and the activity history identifies it as a fault reproduction.

This is useful current evidence that:

- holder-aware completion fields are live in the data model;
- integration-edge cases have been tested;
- the datastore can preserve failure/test context;
- not every task record should be interpreted as a successful completed Inventory transaction.

### 14.4 Authority boundary

The System boundary remains:

```text
Work Queue
    records task meaning / task completion / task attribution

Inventory Management
    records inventory-state meaning / inventory transactions
```

The intended mature transaction invariant remains roadmap work:

```text
one task completion
        ↓
one attributable inventory transaction
        ↓
source decrement
        +
destination increment
        +
history / linkage
```

Current evidence does not establish that this full invariant is implemented.

---

## 15. Current application behavior supported by evidence

The strongest current evidence supports the following present capabilities or structures.

### High-confidence current structures

Verified directly through the current Registry and current Google Sheets sources:

- registered Work Queue Apps Script web application Resource;
- registered Work Queue operational datastore;
- Tasks dataset;
- Task_Templates dataset;
- Settings/configuration dataset;
- Task_Activity event/history dataset;
- Location_Task_Map;
- stable Task ID field;
- status/priority/category fields;
- stable Location ID field;
- readable unit/room/location context;
- assignment label and Assigned Employee ID field;
- separate registered `RES-013` Employees workbook;
- stable `EMP-###` employee identities;
- employee fields for Active, Assignment_Eligible, Role, notification/program-update flags, and timestamps;
- employee/location assignment records in the shared Employees workbook;
- start/completion/update timestamps;
- required-completion-note configuration;
- inventory-holder completion fields;
- activity event records;
- shared canonical Locations workbook and Work Queue-enabled location flags.

### Current behavior supported by datastore history

Observed task/activity history supports:

- task creation;
- notes;
- starting tasks;
- completing tasks;
- Pending → In Progress → Completed transitions;
- direct Pending → Completed transitions in some records;
- completion notes;
- location-aware task records;
- task-template use;
- inventory-holder test activity.

### Current behavior supported by technical documentation

The current technical manual additionally states that the application:

- creates work;
- assigns work;
- tracks work;
- updates work;
- completes work;
- reads/writes connected Google Sheets;
- uses employee records for assignment;
- can create an `Inventory_Holder_Event` for applicable task completion.

The direct discovery of the separate Employees workbook now supports the technical manual's personnel-source architecture.

However, because the active Apps Script source was not inspected during this reconciliation, the exact current runtime path by which the deployed app reads the employee workbook remains technical-document evidence rather than fresh source-code verification.

Where other technical-manual statements exceed what current datastore evidence proves, they likewise remain **technical-document evidence** rather than fresh executable verification.

---

## 16. Evidence reconciliation and current uncertainty

A useful System Summary should make both resolved discrepancies and remaining uncertainty visible.

### 16.1 Employee-source location reconciliation — resolved

Earlier in this System-definition step, three pieces of evidence did not align:

```text
technical manual
    → Employees sheet is an active personnel source

RES-013
    → pointed to Work Queue data workbook

current Work Queue workbook
    → contained no visible Employees sheet
```

Direct Drive discovery located the separate current workbook:

```text
Employees
1It_C3s-4Nwn7bFKt_InO5bblpF3Fo6dJzsF_WwKhnJo
```

Its structure was then directly verified:

```text
Employees
Assignments
Weekly_Schedule
```

The `Employees` sheet contains stable `EMP-###` identities and personnel/assignment fields consistent with the Work Queue technical manual.

The canonical Registry was corrected without changing Resource identity:

```text
RES-013
    → separate Employees workbook
```

and the correction was recorded as:

```text
ACT-0081
Employee dataset location reconciled
```

Status:

```text
RESOLVED at Resource-location level
```

Remaining uncertainty is narrower:

> The physical/registered source is now known; the exact active Apps Script code path that loads and uses that source has not been freshly inspected in this documentation step.

### 16.2 Application version naming

Current workbook title:

```text
Work Queue 2.1 Test Data
```

Current Settings value:

```text
APP_VERSION = 2
```

Status:

```text
UNRESOLVED / naming-version reconciliation needed
```

Do not infer that one is wrong.

### 16.3 Exact current source/deployment implementation

The Resource Registry identifies the current application URL, but this reconciliation step did not inspect the active Apps Script source project or deployment code.

Therefore this Summary does not establish:

- current source-project ID;
- exact client/server file set;
- exact authentication mechanism;
- every current validation rule;
- every current status transition;
- exact runtime employee-source loading mechanism;
- exact holder-event creation code;
- current permission enforcement;
- current error-handling behavior;
- current deployment version;
- complete regression-test status.

### 16.4 Full Inventory propagation

Current evidence supports holder-event integration structures and a technical-manual statement that applicable completion can create an `Inventory_Holder_Event`.

Current evidence does not establish:

```text
employee cart source decrement
+
destination holder increment
+
fully reconciled transaction history
```

as complete current behavior.

### 16.5 Roadmap items

The Work Queue roadmap intentionally includes existing, partial, planned, and unassessed capability areas.

The existence of a roadmap item is not completion evidence.

---

## 17. Roadmap boundary

The Work Queue roadmap answers:

> **What should Work Queue become?**

This System Summary answers:

> **What is Work Queue now, based on currently available evidence?**

The roadmap currently defines 16 capability areas:

1. Identity, Authentication, Roles, and Permissions
2. Role-Based Dashboards
3. Work Intake, Pending State, and Supervisor Review
4. Employee Participation and Assignment Lifecycle
5. Calendar and Scheduling Integration
6. Employee Profile Integration
7. Inventory Integration and Transaction Propagation
8. Structured Notes, Templates, Images, and Evidence
9. QR Reporting and OpenAI-Assisted Validation
10. History, Search, Audit, and Operational Inquiry
11. Reporting, Printing, and Paperwork Translation
12. Recurring Work and Dailies
13. Building Map and Location Intelligence
14. Supervisor Operations and Exception Handling
15. Notifications and Communication
16. Administration, Configuration, Reliability, and Data Integrity

Some of those domains have partial current foundations.

Examples:

```text
Identity / attribution
    Assigned Employee ID exists
    but current-user authentication remains unresolved

History
    Task_Activity exists
    but mature search/audit behavior remains incomplete

Configuration
    Settings and Task_Templates exist
    but broader administration remains incomplete

Locations
    canonical shared Location IDs and mapping exist
    but mature Building Map intelligence remains incomplete

Inventory
    holder-aware completion fields/integration exist
    but full transaction propagation remains incomplete
```

This is the correct relationship between the current-state Summary and future-state roadmap.

---

## 18. Current known limitations

Based on current datastore evidence, current shared-data evidence, current technical documentation, and the roadmap baseline, Work Queue remains a functioning but incomplete System.

Known or strongly supported limitations include:

- no fully reconciled current-user identity model in this Summary;
- the physical `RES-013` employee source is now resolved, but its exact current Apps Script loading path has not been freshly source-verified;
- no verified complete employee My Work / Available Work participation model;
- no verified complete reject/release workflow;
- no verified complete supervisor pending/review/release pipeline;
- no verified mature role-based dashboard model;
- full Inventory transfer propagation is not verified current behavior;
- Scheduling integration is not verified as current assignment context, even though the shared Employees workbook contains assignment/schedule-related data;
- Employee Profile integration remains unresolved/planned beyond the current employee/personnel dataset;
- mature history/search/reporting remains incomplete;
- structured task evidence/images remain incomplete;
- QR-originated reporting remains planned;
- OpenAI-assisted validation remains planned/advisory;
- recurring/dailies architecture remains incomplete;
- Building Map / location intelligence is not mature even though stable shared location data exists;
- notification setting is currently disabled in the Work Queue operational datastore;
- current source/deployment permissions and runtime validation have not been comprehensively reverified in this documentation step.

These limitations should be refined after current source inspection.

---

## 19. System Resources

The current Registry identifies the following directly relevant Resources.

### `RES-002` — Work Queue app

Resource type:

```text
APPLICATION
```

Current Registry description:

> Web application for creating, assigning, filtering, tracking, and completing housekeeping tasks.

This is the visible application Resource.

It is not the whole Work Queue System.

### `RES-003` — Work Queue app data sheet

Resource type:

```text
DATA STORE
```

Current Registry description identifies it as the primary Work Queue 2.1 data workbook containing task and assignment-related operational data.

Current direct verification confirms the sheet structure described in Section 6.

### `RES-012` — Work Queue Tasks dataset

Resource type:

```text
DATASET
```

Current task-record source within the Work Queue operational datastore.

### `RES-013` — Work Queue Employees dataset

Resource type:

```text
DATASET
```

Current Registry routing:

```text
Employees workbook
1It_C3s-4Nwn7bFKt_InO5bblpF3Fo6dJzsF_WwKhnJo
```

Current Registry description identifies it as the shared employee/personnel dataset used by Work Queue for assignee selection and stable Assigned Employee ID linkage.

Direct verification shows that the workbook contains:

```text
Employees
Assignments
Weekly_Schedule
```

and that the Employees sheet uses stable `EMP-###` identifiers.

The Registry location was reconciled on 2026-08-16 and recorded through:

```text
ACT-0081
Employee dataset location reconciled
```

### `RES-014` — Work Queue Locations reference

Resource type:

```text
DATASET
```

Current Registry points to the shared `Klinswork_Locations` workbook.

This is consistent with current direct verification.

### `RES-010` — Building Map (Locations sheet)

Resource type:

```text
DATA STORE
```

Shared canonical physical-location source used across Work Queue, Inventory, Scheduling/Calendar, and other operational records.

### `RES-047` — Work Queue app technical manual

Resource type:

```text
DOCUMENT
```

System-level architecture and operations reference.

Originally prepared August 2, 2026 and updated August 9, 2026.

The Resource Registry entry itself was updated August 16, 2026.

### Resource authority rule

Do not allocate new `RES-###` identifiers from this Summary.

Resolve Resource identity and current routing through the Resource Registry.

---

## 20. Integration boundaries

### 20.1 Scheduling

Work Queue may consume Scheduling context about:

```text
who
where
when
```

but task assignment/history remains distinct from schedule planning.

The current shared Employees workbook contains:

```text
Assignments
Weekly_Schedule
```

in addition to the employee identity table.

That establishes an available shared assignment/schedule context source.

It does **not** by itself prove the mature Work Queue ↔ Scheduling behavior described in the roadmap.

Target principle:

> **Schedule informs; it does not imprison.**

Work Queue should preserve actual task assignment and performance history even when schedule context influences initial work routing.

---

### 20.2 Employee Profile / personnel authority

Work Queue needs stable employee/person identity.

The current physical source is now resolved through:

```text
RES-013
→ separate Employees workbook
```

The workbook supplies stable `Employee_ID` values and related personnel/assignment context.

Work Queue should consume that authority rather than becoming the authoritative personnel system merely because tasks require assignees.

The remaining question is not where the employee data lives.

The remaining questions are:

- how the current deployed app loads it;
- which fields Work Queue is authorized to consume;
- how role/personnel semantics should be separated from Work Queue application permissions;
- how future Employee Profile capability should relate to the shared employee source.

---

### 20.3 Building Map / Locations

Work Queue currently consumes shared stable Location IDs.

That is current verified architecture.

The broader shared location model remains outside Work Queue ownership.

Work Queue-specific location behavior belongs in Work Queue structures such as:

```text
Location_Task_Map
```

while canonical physical identity belongs in the shared Locations source.

---

### 20.4 Inventory Management

Work Queue may cause inventory-related effects.

Inventory Management remains authoritative for inventory-state meaning.

Current integration is partial.

---

### 20.5 Documentation

Documentation supplies:

- summaries;
- sidecars;
- roadmaps;
- implementation plans;
- Viewer discovery;
- manifests;
- catalogs;
- workflow/history structures.

Documentation does not become Work Queue operational state.

---

## 21. Historical interpretation

Work Queue has evolved through terminology and implementation changes.

Earlier records may:

- use `Tasker`;
- treat Work Queue primarily as an application;
- use older app versions or data models;
- use different employee/location sources;
- describe planned behavior not implemented;
- describe implementation behavior that was correct at the date recorded but later changed.

Preserve those records as historical evidence.

Current interpretation should not rewrite them as though the present Project/System/Resource ontology existed from the beginning.

The evidence discipline is:

```text
historical implementation evidence
    = what existed / was reported at that date

planning / design evidence
    = what was intended

current Registry / current datastore evidence
    = current routing and current stored structures

current source / deployment / executable testing
    = strongest authority for detailed runtime behavior
```

---

## 22. Current state

### 22.1 Semantic state

High confidence:

- Work Queue is the principal known System inside Task Assignment and Tracking.
- Task Assignment and Tracking and Work Queue are different semantic entities.
- the Work Queue application is a Resource / implementation surface, not the whole System;
- the Work Queue operational datastore is a Resource, not System identity;
- the employee/personnel dataset is a separate shared Resource, not System identity;
- System Identity has not yet been formalized;
- no permanent `SYS-###` is assigned in this exemplar step.

### 22.2 Current registered Resource state

High confidence as of this reconciliation:

- `RES-002` routes the Work Queue application;
- `RES-003` routes the Work Queue operational datastore;
- `RES-012` identifies the Tasks dataset;
- `RES-013` routes the Work Queue Employees dataset to the separate Employees workbook;
- `RES-014` identifies the Work Queue Locations reference;
- `RES-010` identifies the shared canonical Locations datastore;
- `RES-047` identifies the current technical manual.

The `RES-013` location correction is preserved in Registry history as:

```text
ACT-0081
Employee dataset location reconciled
```

### 22.3 Current data state

High confidence for directly inspected current sources.

The Work Queue operational datastore exposes:

```text
Tasks
Task_Templates
Settings
Task_Activity
Location_Task_Map
```

It demonstrates:

- stable task IDs;
- task creation metadata;
- task statuses;
- location IDs and human-readable location fields;
- assignment labels and stable employee-ID field;
- completion timestamps and notes;
- template-based task configuration;
- inventory-holder completion metadata;
- task event history;
- app settings;
- location-to-template mapping.

The separate `RES-013` Employees workbook exposes:

```text
Employees
Assignments
Weekly_Schedule
```

Directly inspected employee/assignment data demonstrates:

- stable `EMP-###` employee identity;
- display name and email fields;
- Active and Assignment_Eligible flags;
- Role;
- notification/program-update flags;
- employee timestamps;
- assignment records linking `Employee_ID` to `Location_ID`, work date, shift, assignment type, and status.

The shared `Klinswork_Locations` source separately preserves canonical physical location identity.

### 22.4 Detailed runtime state

Medium/limited confidence.

This Summary does not claim comprehensive fresh verification of:

- Apps Script source;
- deployment code;
- authentication/current-user logic;
- all validation behavior;
- all permission behavior;
- exact employee-source loading code;
- inventory-event writes;
- notification behavior beyond the current setting;
- all test results.

### 22.5 Documentation state

Current System documentation now consists of:

```text
Work Queue/
├── README.md
├── summaries/
│   ├── system-summary.md
│   └── work-queue-roadmap.md
└── sidecars/
    ├── system-summary-sidecar.json        [current]
    └── work-queue-roadmap-sidecar.json
```

There is intentionally no System Identity Entity Record.

---

## 23. Unresolved questions

### 23.1 System identity and boundary

- What stable facts belong in a future Work Queue System Identity record?
- Does Work Queue receive a permanent `SYS-###`?
- Is `Work Queue` the durable System name or partly an application label?
- What exact boundary separates Work Queue System from the Apps Script application?
- What exact boundary separates Work Queue System from the Google Sheets datastore?
- When would a replacement implementation become a successor System rather than a new version of Work Queue?
- Should a separate Application / Implementation entity be formalized beneath the System?

### 23.2 Current source and deployment

- What Apps Script source project is authoritative?
- What deployment version is currently live?
- What source files comprise the current app?
- What server-side validation currently exists?
- What permission/authentication model is actually enforced?
- Which runtime environment supplies current-user identity?
- Which current tests have execution evidence?

### 23.3 Employee/personnel integration

The physical source is now resolved through `RES-013`.

Remaining questions are:

- Does the current deployed Apps Script read `RES-013` directly, through configuration, or through another service/helper layer?
- Which `Employees` fields are currently consumed by Work Queue?
- Does `Assignment_Eligible` currently control assignee selection?
- How does the current app treat the `Role` field?
- How should personnel roles remain distinct from Work Queue application permissions?
- How are inactive employees handled in existing task history?
- How should `Assignments` and `Weekly_Schedule` inform Work Queue without becoming task-history authority?
- What stable person-ID authority should ultimately govern all Klinswork employee references?
- How should a future Employee Profile capability relate to the existing shared employee dataset?

### 23.4 Task lifecycle

- What is the exact current allowed state vocabulary?
- Which transitions are legal?
- Why do some activity records show direct Pending → Completed transitions?
- Which state changes are recorded in `Task_Activity`?
- Is assignment change evented?
- How are rejection, release, reassignment, blocking, cancellation, reopening, and correction handled today?
- When current task state and event history disagree, which is authoritative?

### 23.5 Inventory

- What current code creates `Inventory_Holder_Event`?
- Which current task/template conditions trigger it?
- How is `Related Holder Event ID` populated?
- What happens when `Related Holder ID` is missing?
- Is event creation atomic with task completion?
- How are failures represented?
- What is the exact future source-cart decrement / destination-holder increment contract?
- How are duplicate transfers prevented?

### 23.6 Locations

- Is `RES-010` the final shared location authority?
- Is `RES-014` best modeled as a dataset view/reference to `RES-010`?
- How is location caching implemented?
- How are disabled or moved locations handled in existing tasks?
- What additional Building Map coverage is required for QR/map workflows?

### 23.7 Templates / configuration

- Which Task_Templates fields are enforced by current source?
- How are holder-required rules validated?
- Which Settings are read by current runtime code?
- Is `APP_VERSION = 2` intentionally different from the workbook's `2.1` label?
- Which routine configuration remains hard-coded outside Sheets?

### 23.8 History / reporting

- Which operations append `Task_Activity` events?
- Can activity records be modified/deleted?
- What search/reporting interfaces currently exist?
- What reports are current versus roadmap-only?
- Is there a distinct Completed Jobs view in current code, and how does it relate to `Task_Activity`?
- What audit invariants should be formalized?

### 23.9 Documentation / Viewer

- The Viewer now discovers this System Summary through the Projects Documentation Space via its validated sidecar/companion relationship.
- The current Viewer semantics distinguish the System Summary and System Roadmap; future presentation refinements may still be considered.
- Should a dedicated System Summary sidecar profile be created later?
- What Viewer treatment should be reserved for a future System Identity Entity Record?
- Which System Definition rules are genuinely reusable after this second exemplar?

---

## 24. Next work

The System Summary companion has been created and validated:

```text
../sidecars/system-summary-sidecar.json
```

Completed after the original drafting of this Summary:

1. the sidecar was created as a structured companion to this Markdown source;
2. `Work Queue` remained the System subject and `Task Assignment and Tracking` remained parent Project context;
3. `systemId` remained blank/unassigned;
4. the corrected `RES-013` separate Employees-workbook relationship was preserved;
5. the source-aware manifest was regenerated;
6. the System Summary sidecar was discovered under the Projects source;
7. companion resolution to `summaries/system-summary.md` succeeded;
8. the Work Queue roadmap sidecar remained discovered and companion-resolved;
9. current-state and roadmap Viewer semantics were validated as distinct;
10. context-naive resume behavior was validated;
11. the material System-definition stage was recorded in Work Unit history.

No additional System-definition artifact is required for WORK-0001. Remaining work belongs to Project Definition closure: reconcile creation-time annotations, update the formal Work Implementation Session, review the completion rule, and close the session/Work Unit if the rule remains satisfied.

---

## 25. Source and evidence basis

This Summary was reconciled from the following source classes on 2026-08-16 and revised after the `RES-013` employee-source correction.

### Current Project/System documentation

- `Task Assignment and Tracking/summaries/project-summary.md`
- `Task Assignment and Tracking/systems/Work Queue/README.md`
- `Task Assignment and Tracking/systems/Work Queue/summaries/work-queue-roadmap.md`
- Work Queue roadmap sidecar
- current formal Work Implementation Session

### Reference exemplar

- `Inventory Management/systems/Inventory 3.0/summaries/system-summary.md`

The Inventory 3.0 exemplar supplied structure and evidence-discipline precedent, not Work Queue facts.

### Current registered Resource evidence

- Klinswork Resource Registry;
- `RES-002`;
- `RES-003`;
- `RES-010`;
- `RES-012`;
- `RES-013`;
- `RES-014`;
- `RES-047`;
- Resource Activity `ACT-0081`.

### Current Work Queue datastore evidence

Direct reads of the current registered Work Queue operational workbook:

```text
Tasks
Task_Templates
Settings
Task_Activity
Location_Task_Map
```

### Current employee/personnel evidence

Direct discovery and inspection of the separate current workbook:

```text
Employees
Workbook ID:
1It_C3s-4Nwn7bFKt_InO5bblpF3Fo6dJzsF_WwKhnJo
```

Verified sheet structure:

```text
Employees
Assignments
Weekly_Schedule
```

Direct reads were performed for:

```text
Employees
Assignments
```

The workbook location was then written into the canonical `RES-013` row and the correction was recorded as `ACT-0081`.

### Current shared location evidence

Direct reads of:

```text
Klinswork_Locations / Locations
```

### Technical documentation

`RES-047`:

```text
work-queue-app-technical-manual
```

Originally prepared August 2, 2026 and updated August 9, 2026.

### Planning evidence

```text
work-queue-roadmap.md
```

Roadmap content is treated as target-state/planning evidence unless current implementation evidence independently supports it.

### Interpretation rules

This Summary uses these rules:

1. current Registry rows establish current registered Resource identity/routing; `RES-013` is interpreted from its corrected post-`ACT-0081` state;
2. direct current workbook reads establish current visible datastore/shared-data structure and stored evidence;
3. the technical manual establishes documented architecture/behavior at its update date;
4. roadmap statements establish planned direction unless independently verified;
5. historical records establish dated history;
6. current source/deployment claims are not invented when source was not inspected;
7. unresolved IDs remain unresolved;
8. Resources and relationships are not converted into intrinsic System identity;
9. resolved evidence discrepancies are documented as reconciliations rather than retained as current uncertainty;
10. remaining evidence gaps stay explicit until verified.

---

## 26. Governing interpretation

The current Work Queue System can be summarized as:

```text
Task Assignment and Tracking
    = durable Project / operational undertaking

Work Queue
    = coherent System serving that undertaking

Work Queue Apps Script app
    = visible application Resource

Work Queue Google Sheets workbook / RES-003
    = primary operational task/configuration/history datastore

Tasks
    = current task-state records

Task_Activity
    = current event/history records

Task_Templates
    = task-definition/configuration layer

Settings
    = runtime/configuration values stored in data

Location_Task_Map
    = Work Queue-specific location-to-template relationship

Employees workbook / RES-013
    = separate shared employee/personnel and assignment-context Resource

Klinswork_Locations
    = shared canonical location source

Inventory Management
    = authority for inventory-state effects

System Roadmap
    = intended mature Work Queue direction

System Summary
    = current evidence-based System interpretation

Resource Registry
    = Resource identity and routing authority

current source / deployment / tests
    = strongest evidence for detailed live application behavior
```

The central result of this System Summary is not that every Work Queue detail has now been proven.

It is that the System can be described coherently while preserving the distinction among:

```text
Project
System
Application
Operational datastore
Shared employee/personnel dataset
Shared location source
Integration
Current evidence
Historical evidence
Roadmap intent
System Identity
```

The `RES-013` reconciliation is an example of why this separation matters:

```text
Resource identity remained stable
while
physical Resource location changed
```

Correcting the location did not require redefining Work Queue, the Task Assignment and Tracking Project, or employee identity itself.

That distinction is the foundation required for reliable continuation of Work Queue development.

---

