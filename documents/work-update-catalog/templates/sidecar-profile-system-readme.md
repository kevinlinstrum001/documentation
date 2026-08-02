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

- `generic-document-sidecar-template-3.0-draft.json`
  - Fallback for reports, specifications, policies, memos, and documents without a better profile.
  - Adds a general summary, key points, concepts, recommendations, and open questions.

- `sidecar-profile-registry-1.0.json`
  - Maps document purposes to templates and viewer preview modes.

## Selection rule

Choose the profile from what the document is doing:

- **Records completed work or progress** → `work-update`
- **Defines intended work and tests** → `implementation-plan`
- **Teaches or preserves guidance** → `lesson-reference`
- **None of those fits cleanly** → `generic-document`

The filename does not determine the profile.

## Test distinction

- `plannedTests` describes tests a plan says should happen.
- `technical.tests` describes tests actually reported or performed.

This prevents planned verification from appearing as completed evidence.

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

## Compatibility

The work-update profile preserves the major fields from the existing `2.0-draft` template, so current work-update sidecars can migrate with minimal restructuring.
