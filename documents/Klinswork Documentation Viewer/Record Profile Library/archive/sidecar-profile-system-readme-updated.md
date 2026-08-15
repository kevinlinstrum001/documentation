# Klinswork Sidecar Profile Templates — 3.0 Draft

## Purpose

This template set separates document types without splitting the catalog.

All sidecars retain one shared foundation for identity, project relationships, search, sections, technical metadata, publication, links, and provenance. Each complete profile then adds fields suited to the document's purpose.

## Files

- `document-sidecar-base-template-3.0-draft.json`
  - Shared structural foundation.
  - Reference template; specialized templates are standalone and ready to populate.

- `work-update-sidecar-template-3.0-draft.json`
  - For dated work updates, milestone reports, and progress records.
  - Adds `workCoverage`, `narrative`, and `projectDelta`.

- `implementation-plan-sidecar-template-3.0-draft.json`
  - For implementation plans, roadmaps, migration plans, and test plans.
  - Adds stages, dependencies, risks, acceptance criteria, planned tests, order, and roadmap impact.

- `lesson-reference-sidecar-template-3.0-draft.json`
  - For lessons, guides, references, procedures, and training documents.
  - Adds objectives, principles, concepts, examples, procedures, warnings, and review questions.

- `workflow-specification-sidecar-template-3.0-draft.json`
  - For authoritative reusable workflows, lifecycle specifications, state machines, and controlled process definitions.
  - Adds workflow identity, revision history, design principles, artifact authority, states, transitions, inputs, outputs, instruction sets, phases, steps, automation boundaries, human review, workflow validation, closure rules, and design decisions.

- `generic-document-sidecar-template-3.0-draft.json`
  - Fallback for reports, specifications, policies, memos, and documents without a better profile.
  - Adds a general summary, key points, concepts, recommendations, and open questions.

- `sidecar-profile-registry-1.0.json`
  - Maps document purposes to templates and viewer preview modes.

## Selection rule

Choose the profile from what the document is doing:

- **Records completed work or progress** → `work-update`
- **Defines intended work and tests for one bounded effort** → `implementation-plan`
- **Defines the reusable process that governs many efforts or runs** → `workflow-specification`
- **Teaches or preserves guidance** → `lesson-reference`
- **None of those fits cleanly** → `generic-document`

The filename does not determine the profile.

## Workflow specification versus implementation plan

A workflow specification defines the reusable controlled process:

- authoritative artifacts and fact ownership,
- states and transitions,
- phases and ordered steps,
- required inputs and outputs,
- human-review and approval points,
- automation boundaries,
- validation rules,
- completion and closure behavior.

An implementation plan defines one intended body of work performed within such a process:

- the target state,
- tactical stages,
- dependencies,
- risks,
- tests,
- acceptance criteria,
- implementation order.

The workflow remains durable across runs. The implementation plan belongs to one bounded change or session.

## Test distinction

- `plannedTests` describes tests a plan says should happen.
- `technical.tests` describes tests actually reported or performed.
- `validationModel` in a workflow profile describes rules the workflow requires; it is not evidence that a particular run passed those rules.

This prevents planned or required verification from appearing as completed evidence.

## Authority distinction

A workflow sidecar describes the workflow specification document. It does not replace:

- the workflow specification itself,
- project records,
- integration records,
- work-session intentions,
- implementation plans,
- workflow-run records,
- debrief records,
- publication artifacts.

Authority remains assigned by the underlying workflow and artifact model.

## Catalog rule

Keep all profiles in the same catalog. The catalog and viewer use:

- `document.documentId`
- `document.documentType`
- `profile.profileType`
- `document.title`
- `subject`
- `projectContext`
- `sections`
- `publication`
- `provenance`

The viewer can choose a type-aware preview from `profile.previewMode`.

For `workflow-specification`, the preview should prioritize:

1. workflow purpose and status,
2. initial and final states,
3. phase sequence,
4. ordered steps and state transitions,
5. authoritative artifacts and fact ownership,
6. human-review points,
7. automation boundaries,
8. validation and closure rules,
9. open design decisions.

## Compatibility

The work-update profile preserves the major fields from the existing `2.0-draft` template, so current work-update sidecars can migrate with minimal restructuring.

The legacy `2.0-draft` document-sidecar template remains a work-update-oriented structure. It is a compatibility reference, not the shared base for the workflow profile.
