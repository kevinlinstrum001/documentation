# Klinswork Record Profile Library

## Purpose

The **Klinswork Record Profile Library** is the authoritative collection of reusable profile definitions and construction templates for recognized Klinswork record types.

A **record profile** defines how a particular kind of record should be constructed, interpreted, validated, and presented. Depending on the record family, a profile may describe:

- a structured sidecar that interprets a human-readable source document;
- a canonical entity record, such as a Project Identity or System Identity record;
- an authoring template used to create an authoritative human-readable source;
- a registry that maps record purposes to profiles and viewer behaviors.

The library exists so that Klinswork does not have to rediscover the meaning of a record from its filename, folder, or current implementation.

```text
Record Profile Library
        ↓
defines recognized record families
        ↓
provides reusable templates and interpretation rules
        ↓
records are created according to those profiles
        ↓
catalogs, manifests, viewers, workflows, and future tools
can interpret them consistently
```

The governing principle is:

> **Profile selection is semantic. A filename or repository location does not determine what a record means.**

---

## Vocabulary

### Record Profile

A reusable semantic definition for one recognized record family.

A profile may define:

- record purpose;
- authority boundaries;
- structural fields;
- interpretation rules;
- validation expectations;
- versioning;
- viewer preview behavior;
- compatibility and migration rules.

### Profile Template

The concrete reusable file that expresses a record profile and can be copied or used as the construction basis for a new record.

Examples:

- `implementation-plan-sidecar-template-3.1-draft.json`
- `work-update-sidecar-template-3.0.json`
- `project-identity-template-1.0-draft.json` *(planned)*

### Sidecar

A machine-readable structured companion to a human-readable source document.

For a sidecar profile:

```text
Human-readable source document
        ↓ authoritative for the document's narrative/content

Structured sidecar
        ↓ machine-readable interpretation of that document

Record profile template
        ↓ defines how the sidecar is constructed and interpreted
```

A sidecar does **not** become the canonical identity record of a Project, System, Resource, or other entity merely because it mentions that entity.

### Entity Record

A canonical structured record whose purpose is to identify and describe a Klinswork entity directly.

For an entity identity profile:

```text
Project / System / other entity
        ↓
canonical identity record
        ↑
entity-record profile template
```

Unlike a document sidecar, an entity identity record is not merely an interpretation of another document.

### Profile Registry

A machine-readable index of recognized profiles and their intended uses.

The profile registry may map:

- record purpose;
- profile type;
- profile version;
- template file;
- base profile or shared foundation;
- Viewer preview mode;
- compatibility information.

---

## Library scope

The Record Profile Library may contain several related classes of reusable definitions.

### 1. Sidecar profiles

These describe machine-readable companions to human-readable documents.

Current families include:

- work updates;
- implementation plans;
- lessons and references;
- workflow specifications;
- generic documents;
- specialized study/document profiles.

### 2. Entity-record profiles

These describe canonical structured records for Klinswork entities.

Planned initial profiles:

- Project Identity;
- System Identity.

Additional entity-record profiles should be added only when the underlying ontology requires them.

### 3. Human-readable authoring templates

Some templates guide creation of the authoritative human-readable source rather than a JSON sidecar.

Example:

- `summary-md-template.json`

The Markdown summary template defines the expected content and organization of a durable narrative source from which downstream structured and publication artifacts may be derived.

### 4. Profile registry and compatibility material

The library may also contain:

- the profile registry;
- migration guidance;
- compatibility documentation;
- archived prior profile versions.

---

## Authority rules

Record profiles must make their authority boundaries explicit.

### Document sidecars

For document-sidecar profiles:

> The human-readable source document remains authoritative for the document itself. The sidecar is its structured interpretation.

A sidecar must not silently replace:

- the source document;
- a canonical Project record;
- a canonical System record;
- the Resource Registry;
- relationship authority;
- workflow-run history;
- execution evidence;
- another artifact that has been assigned authority for a different fact.

### Entity identity records

For entity-record profiles:

> The instantiated identity record is authoritative for the stable identity of the entity within the scope assigned to that record.

Entity identity must remain separate from:

- current name;
- repository location;
- hierarchy;
- lifecycle status;
- implementation;
- current systems or resources;
- deployment URL.

### Relationships

Parentage, containment, dependencies, use of resources, operational environments, and other cross-entity facts are relationships.

They should not be treated as intrinsic identity merely because they appear in an identity record or summary.

---

## Current profile files

### `document-sidecar-base-template-3.0.json`

Shared structural foundation for general document sidecars.

It provides common concepts for:

- document identity;
- project context;
- subject/indexing information;
- sections;
- technical metadata;
- communications;
- graphics;
- publication;
- deployment;
- links;
- validation;
- provenance.

Specialized sidecar templates may be standalone while retaining the same conceptual foundation.

### `work-update-sidecar-template-3.0.json`

For dated work updates, milestone reports, and progress records.

Adds work-update concepts such as:

- work coverage;
- narrative;
- project delta;
- resulting state;
- supervisor-facing material.

### `implementation-plan-sidecar-template-3.1-draft.json`

For implementation plans, migration plans, bounded change plans, and test-oriented implementation plans.

Adds:

- semantic context resolution;
- Project/System/Application/Resource placement;
- authoritative-resource declarations;
- planning boundaries;
- stages;
- dependencies;
- risks;
- acceptance criteria;
- planned tests;
- implementation order;
- roadmap impact.

Version 3.1 also explicitly preserves the distinction between work already completed and work prospectively planned.

### `lesson-reference-sidecar-template-3.0.json`

For lessons, guides, references, procedures, and training documents.

Adds concepts such as:

- objectives;
- principles;
- concepts;
- examples;
- procedures;
- warnings;
- review questions.

### `workflow-specification-sidecar-template-3.0.json`

For authoritative reusable workflows, lifecycle specifications, state machines, and controlled process definitions.

Adds concepts such as:

- workflow identity;
- revision history;
- design principles;
- artifact authority;
- states and transitions;
- phases and ordered steps;
- inputs and outputs;
- instruction sets;
- automation boundaries;
- human review;
- validation;
- closure rules;
- design decisions.

### `generic-document-sidecar-template-3.0.json`

Fallback profile for reports, specifications, policies, memos, and other documents without a more specific profile.

Adds:

- general summary;
- key points;
- concepts;
- recommendations;
- open questions.

### `pst-sp-study-guide-sidecar-template-1.0.json`

Specialized profile for the PST-SP study-guide document family.

It remains part of the same Record Profile Library even though its subject matter is specialized.

### `summary-md-template.json`

Authoring template for a durable project-aware Markdown summary.

This differs from a sidecar template: it guides creation of the human-readable narrative source rather than merely interpreting one.

### `sidecar-profile-registry-1.0.json`

Maps recognized sidecar/document purposes to templates and Viewer preview modes.

As entity-record profiles are added, the registry should be reviewed to determine whether it should remain sidecar-specific or evolve into a broader **Record Profile Registry**.

---

## Planned entity-record profiles

### `project-identity-template-1.0-draft.json`

Planned canonical construction profile for one Klinswork Project identity record.

The profile should preserve the invariant:

```text
project identity
    != project name
    != repository location
    != hierarchy
    != lifecycle state
    != implementation
```

### `system-identity-template-1.0-draft.json`

Planned canonical construction profile for one Klinswork System identity record.

It should follow the same identity principles as the Project Identity profile while preserving the semantic distinction between Project and System.

---

## Profile selection rules

Choose a profile from what the record or source document is **doing**, not from its filename or folder.

For document sidecars:

- **Records completed work or progress** → `work-update`
- **Defines intended work and tests for one bounded effort** → `implementation-plan`
- **Defines a reusable process that governs many efforts or runs** → `workflow-specification`
- **Teaches or preserves guidance** → `lesson-reference`
- **None of those fits cleanly** → `generic-document`

For entity records:

- **Identifies one durable Project** → `project-identity`
- **Identifies one durable System** → `system-identity`

A repository path may provide useful context, but it must not be treated as semantic proof of record type, Project membership, System membership, or authority.

---

## Workflow specification versus implementation plan

A workflow specification defines the reusable controlled process:

- authoritative artifacts and fact ownership;
- states and transitions;
- phases and ordered steps;
- required inputs and outputs;
- human-review and approval points;
- automation boundaries;
- validation rules;
- completion and closure behavior.

An implementation plan defines one intended body of work performed within such a process:

- target state;
- tactical stages;
- dependencies;
- risks;
- tests;
- acceptance criteria;
- implementation order.

The workflow remains durable across runs. The implementation plan belongs to one bounded change or planning effort.

---

## Test distinction

Profiles should preserve the difference among planned, required, and actually executed verification.

- `plannedTests` describes tests a plan says should happen.
- `technical.tests` describes tests actually reported or performed.
- workflow validation rules describe verification the workflow requires.
- none of those, by itself, proves that a particular execution passed.

This prevents intended verification from appearing as completed evidence.

---

# Profile evolution and desired changes

## `schemaRoadmap` is the standard location for profile evolution

Desired changes to a **record profile or schema** should be recorded in a top-level `schemaRoadmap` block when the profile is under active evolution.

This convention already exists in the implementation-plan 3.1 profile and should become the preferred pattern for new Record Profile Library definitions.

Recommended structure:

```json
"schemaRoadmap": {
  "currentVersion": "1.0-draft",
  "plannedVersions": [
    {
      "targetVersion": "1.1",
      "status": "planned",
      "additions": [],
      "changes": [],
      "deprecations": [],
      "migrationNotes": [],
      "openQuestions": []
    }
  ]
}
```

### What belongs in `schemaRoadmap`

Use it for changes to the **profile itself**, such as:

- fields to add;
- fields to restructure;
- interpretation rules to clarify;
- controlled vocabularies to formalize;
- validation to strengthen;
- fields or behaviors to deprecate;
- migration requirements;
- compatibility concerns;
- unresolved profile-design questions.

### What does not belong in `schemaRoadmap`

Do not use `schemaRoadmap` for:

- unfinished work on the Project described by a record;
- a document's unanswered subject-matter questions;
- implementation tasks;
- application feature requests;
- operational next steps;
- a Project roadmap.

Those belong in the appropriate project, system, plan, summary, workflow, provenance, or relationship records.

---

## `_meta` has a different role

`_meta` should preserve the semantic instructions necessary to understand the template.

Typical `_meta` content includes:

- template purpose;
- authority rule;
- identity rule;
- interpretation principle;
- provenance principle;
- compatibility principle;
- JSON comment convention.

Example:

```json
"_meta": {
  "templatePurpose": "",
  "authorityRule": "",
  "interpretationPrinciple": "",
  "jsonCommentConvention": ""
}
```

The distinction is:

```text
_meta
    = what this profile means and how to interpret it

schemaRoadmap
    = how we presently expect the profile itself to evolve
```

Keeping these separate prevents design intentions from becoming confused with current semantic rules.

---

## Historical sidecars should not inherit future schema wishes

An instantiated sidecar is evidence of how a document was structured and interpreted at a particular time.

Therefore:

> Do not retroactively add a template's future `schemaRoadmap` wishes to historical sidecars merely because the template later evolved.

Historical sidecars may retain:

- their original `schemaVersion`;
- their original profile version;
- unresolved questions that belonged to that record;
- provenance and interpretation notes.

If a sidecar is deliberately migrated, the migration should be explicit rather than making the historical record appear to have always used the newer profile.

---

## Record-specific unresolved work

Future work concerning the **subject represented by a record** belongs in the record's semantic fields, not in the profile's `schemaRoadmap`.

Examples include:

- `provenance.unresolvedQuestions`;
- `roadmapImpact`;
- document-specific `openQuestions`;
- implementation-plan remaining work;
- Project or System roadmap records;
- an Open Determination record.

This distinction gives Klinswork two different kinds of "next":

```text
schemaRoadmap
    → What should change about this PROFILE?

record/project roadmap or unresolved questions
    → What should happen next in the THING BEING DOCUMENTED?
```

---

## Open determinations

Questions that affect the broader Klinswork ontology or several profiles should not be buried inside one template.

Examples:

- permanent identifier rules;
- Project/System boundaries;
- authority precedence;
- relationship vocabularies;
- lifecycle vocabulary;
- Viewer/profile compatibility rules.

Those should be promoted to the appropriate architecture decision or Open Determination record, with individual profile roadmaps referencing the issue when useful.

---

## Viewer and catalog rules

All recognized profiles should remain discoverable through common documentation infrastructure.

The Viewer and catalog may use fields such as:

- record/document identity;
- record type;
- profile type;
- profile version;
- title;
- subject;
- Project/System identity references;
- sections;
- publication;
- provenance;
- `previewMode`.

The Viewer may choose a type-aware preview from the profile while retaining a common discovery model.

A specialized preview must not change the underlying authority of the record.

---

## Record Profile Registry direction

The existing `sidecar-profile-registry-1.0.json` was designed when the library was primarily a sidecar system.

With the introduction of canonical entity-record profiles, review whether it should evolve to:

```text
Record Profile Registry
```

rather than remain permanently sidecar-specific.

A future registry should be capable of distinguishing at least:

```text
record family
    ├── document-sidecar
    ├── entity-record
    └── authoring-template
```

without forcing those families to have identical authority semantics.

---

## Folder naming and location

Canonical library location:

```text
KDV/
└── Record Profile Library/
```

The folder name describes its semantic role. Physical location is not itself authority for the profiles it contains.

When moving from the former `KDV/templates/` path, reconcile any:

- hard-coded repository paths;
- profile-registry entries;
- Viewer references;
- workflow references;
- documentation links.

Bare template filenames do not need to change merely because the containing folder was renamed.

---

## Versioning

Profile versions should communicate changes in the interpretive contract.

General principles:

- preserve historical profile versions when they were used by durable records;
- do not silently rewrite old profiles;
- mark draft profiles explicitly;
- document meaningful migration requirements;
- record planned profile evolution in `schemaRoadmap`;
- keep stable identity separate from schema version.

A profile version describes the profile, not the age or lifecycle state of the Project or document represented by a record.

---

## Compatibility

Earlier sidecars remain valid historical records unless explicitly migrated.

Compatibility should favor:

- preserving prior evidence;
- explicit version identification;
- additive migration where practical;
- no invented IDs;
- no path-based semantic inference;
- no silent reassignment of authority.

The legacy `2.0-draft` document-sidecar family remains useful compatibility evidence even where newer profiles provide stronger semantic distinctions.

---

## Design rule

The Record Profile Library should remain broad enough to recognize different record families but disciplined enough that profiles do not become duplicate ontologies.

A useful test is:

> **Does this profile define how to interpret one kind of record, while leaving Project identity, System identity, Resource identity, relationships, and other independently authoritative facts to the records that actually own them?**

If yes, the profile is serving the library correctly.
