# Klinswork JSON Viewer and Catalog System

## Purpose of this README

This file is a **context-restoration document** for future work on the Klinswork JSON Viewer, catalogs, sidecars, manifests, and related repository tools.

Read this file before modifying the JSON viewer or introducing a new catalog/document type.

Its purpose is to restore enough architectural context that a new work session does not have to rediscover how the system fits together.

---

# 1. System Overview

The JSON Viewer is not merely a JSON formatter.

It has two layers:

1. **Generic JSON inspection**
   - Tree view
   - Raw view
   - Search
   - Expand/collapse
   - Repository file navigation

2. **Type-aware presentation**
   - Specialized catalog browsers
   - Specialized document/sidecar previews
   - Catalog-entry preview panels
   - Mini document views reconstructed from preserved sidecar content

The viewer evolves as the repository evolves.

When a new catalog structure, new document type, or useful specialized presentation is introduced, the viewer is often updated to understand that structure explicitly.

---

# 2. Current Repository Area

The JSON catalog system currently lives under:

```text
documents/
└── work-update-catalog/
```

Important items include:

```text
work-update-catalog/
├── catalogs/
├── projects/
├── sidecars/
├── summaries/
├── templates/
├── tools/
├── workflows/
├── archived/
├── json-manifest.json
├── manifest.py
├── json-viewer.html
└── open-json-viewer-v1.6.0.bat
```

The local viewer source currently lives in:

```text
tools/json-viewer-v1.6.0.py
```

Version-specific upgrade notes live in the same tools area.

---

# 3. Local Viewer

Current local viewer:

```text
tools/json-viewer-v1.6.0.py
```

Current launcher:

```text
open-json-viewer-v1.6.0.bat
```

The Python application is a local, read-only repository browser. It recursively discovers JSON files and serves a browser interface.

The local viewer includes:

- collapsible folder navigation
- file filtering
- archive inclusion toggle
- sort controls
- Tree view
- Raw view
- Catalog view when supported
- structured Preview support
- a third/context preview panel
- catalog-entry previews
- specialized sidecar/document previews
- type-aware renderers

The Python file contains a substantial HTML/CSS/JavaScript frontend inside the application.

---

# 4. Online Viewer

Current online/static viewer:

```text
json-viewer.html
```

This is intended for GitHub Pages use.

Unlike the local Python viewer, the static viewer cannot scan the local filesystem or provide Python API endpoints. Instead, it discovers repository JSON through:

```text
json-manifest.json
```

The online viewer should be considered the web companion to the local JSON Viewer.

## Maintenance rule

When the local viewer is materially updated, produce or update the online HTML viewer during the same viewer-release workflow.

The online viewer should not be allowed to drift indefinitely into a separate reduced implementation. Where practical, specialized renderers and interaction patterns should behave similarly in both editions.

---

# 5. Intended Three-Pane Interaction Model

The local viewer's intended desktop interaction model is:

```text
┌─────────────────────┬──────────────────────────────┬──────────────────────┐
│ Repository tree     │ Current JSON / catalog       │ Context preview      │
│                     │                              │                      │
│ folders             │ Tree                         │ document preview     │
│ files               │ Raw                          │ catalog-entry view   │
│ search              │ Catalog                      │ sidecar mini-view    │
│ archive toggle      │                              │                      │
└─────────────────────┴──────────────────────────────┴──────────────────────┘
```

The third pane is important. It allows the user to inspect a selected document, sidecar, or catalog entry without losing the context of the current JSON structure or catalog.

On smaller screens the pane may become an overlay rather than a fixed third column.

---

# 6. Repository Navigation

The local viewer uses a collapsible folder tree.

Examples of meaningful repository groupings include:

```text
catalogs/
sidecars/
    implementation-plans/
    lessons/
    sds/
    work-update-sidecars/
templates/
workflows/
```

This hierarchy should remain visible in the UI. A flattened list of every JSON file is less useful as the repository grows.

Archived content is normally excluded and may be exposed through an explicit archive toggle.

---

# 7. Generic JSON vs. Specialized Views

Every valid JSON file should remain inspectable through generic Tree and Raw modes.

Specialized views are additional behavior. A file does **not** need a custom renderer merely because it is JSON.

A useful mental model is:

```text
JSON Viewer
│
├── Generic inspection
│   ├── Tree
│   └── Raw
│
└── Specialized renderers
    ├── document catalog
    ├── lesson catalog
    ├── chemical product catalog
    ├── document sidecar
    ├── PST-SP study-guide sidecar
    ├── workflow sidecar
    └── future document/catalog types
```

Do not attempt to make one universal heuristic renderer understand every possible JSON schema.

When a structure matters enough to deserve a human-oriented presentation, add a deliberate renderer for it.

---

# 8. Catalogs Are Not All the Same

The repository contains multiple catalog families.

Current examples include:

```text
klinswork-document-catalog-*.json
klinswork-lesson-catalog-001.json
klinswork-chemical-product-catalog-001.json
```

Older versions of a catalog family may use different structures.

Historical catalogs do not necessarily require the same quality of specialized presentation as the current catalog. Tree and Raw modes are acceptable fallbacks for old or superseded schemas.

## Important principle

**Catalog version and viewer version are separate concepts.**

For example, `json-viewer-v1.6.0.py` may know how to display several catalog families and several generations of those catalogs.

A new catalog generation does not automatically imply a matching viewer version number.

---

# 9. Why the Viewer Changes

The viewer is generally updated for one of these reasons.

## A. New viewer functionality

Examples:

- better repository navigation
- third-pane previews
- improved filtering
- richer tree interaction
- responsive behavior
- better searching

## B. A catalog needs a new or improved presentation

Catalog-specific views are common.

A new catalog generation may preserve different fields or organize its entries differently. When those differences are useful to the user, the viewer is updated to understand that catalog.

## C. A new document or catalog type enters the repository

When a new family of structured documents is introduced, the viewer may need:

- type/profile recognition
- a specialized renderer
- filters appropriate to that family
- a compact entry card
- a third-pane preview
- links back to source JSON or full HTML

This is a normal part of the system's evolution.

---

# 10. Document Sidecars

Some catalogs are collections of sidecars that accompany HTML documents.

A sidecar is more than a filename index. It may preserve enough structured content to describe and partially reconstruct the document, including information such as:

- identity
- title
- date
- project
- document type
- summary
- purpose
- outcomes
- decisions
- current state
- next steps
- sections
- topics
- publication information
- source/document URL
- specialized domain content

The HTML document remains the full publication.

The sidecar is a structured companion record that supports discovery, analysis, catalog aggregation, and compact rendering.

---

# 11. Mini Document Previews

Because sidecars preserve selected document content, the viewer can produce a small HTML-like representation without loading the full HTML publication.

Conceptually:

```text
Full HTML document
        │
        └── structured sidecar
                │
                ├── catalog entry
                │
                └── viewer preview
```

The preview is intentionally abbreviated. It should make the record useful for browsing while preserving a link to the full publication whenever such a link exists.

This distinction is important:

- **full HTML** = complete publication
- **sidecar** = structured companion / preserved semantic record
- **catalog** = aggregate discovery layer
- **viewer preview** = human-readable rendering of structured data

---

# 12. Documentation Catalog

The documentation catalog should be understood as a collection of work-update/document records.

Its specialized catalog view may provide filters such as:

- Project
- Document Type
- Year
- Sort order

Selecting a catalog entry can populate the third/context pane with a structured preview of that work update.

The catalog exists for discovery across documents; it is not simply a large JSON object to display verbatim.

Older documentation catalog generations may use different arrangements.

---

# 13. PST-SP Preview

JSON Viewer v1.6.0 added a dedicated PST-SP study-guide preview.

The preview activates for the profile:

```json
"profile": {
  "previewMode": "pst-sp-study-guide"
}
```

The PST-SP renderer includes specialized sections/tabs such as:

- Overview
- Toolkits
- Exercises
- Measures
- Visuals
- Coverage

Its existence is a useful example of the intended architecture: a document with a meaningful structured sidecar can receive a domain-specific human view without changing the generic JSON inspection capabilities.

---

# 14. Catalog and Sidecar Families

Current sidecar areas include examples such as:

```text
sidecars/
├── implementation-plans/
├── lessons/
├── sds/
├── work-update-sidecars/
├── documentation-workflow-sidecar-3.0-draft.json
├── nmbhi-first-supervisor-profile-sidecar-3.0-draft.json
└── pst-sp-veteran-study-guide-sidecar.json
```

These records do not all have identical semantics.

Do not assume that every sidecar must fit one universal document schema or one universal renderer. Shared conventions are useful, but domain-specific structures are allowed when they preserve useful information.

---

# 15. JSON Manifest

File:

```text
json-manifest.json
```

Generator:

```text
manifest.py
```

The JSON manifest is used by the static/online viewer to discover repository JSON files.

The local Python viewer does not depend on this manifest in the same way because it can scan the filesystem directly.

## Regenerate the JSON manifest when

- JSON files are added
- JSON files are removed
- JSON files are renamed or moved
- catalog paths change
- sidecar paths change
- other repository changes affect the online viewer's discoverable JSON inventory

After regeneration, validate that the online viewer can see the expected files.

---

# 16. Image Manifest

Repository image inventory:

```text
images/images.json
```

Generator:

```text
images/build_images_json.py
```

The image manifest is operational data used by the Email Composer so the user can browse/select images stored in the documentation repository.

This is a separate concern from the JSON Viewer catalog system.

## Regenerate the image manifest when

- repository images are added
- images are removed
- images are renamed or moved
- image metadata used by the selector changes

A catalog/viewer update alone does not require rebuilding the image manifest unless image content also changed.

---

# 17. Site / Web-App Manifests

The repository root contains web-app/site manifest files describing site/application identity, icons, theme information, and startup behavior.

These are not the same thing as:

```text
json-manifest.json
```

or:

```text
images/images.json
```

Treat them as a separate site-publication concern.

Review them when site identity, root-page purpose, icons, start URL, or installable-web-app behavior changes.

---

# 18. Source and Derived Artifacts

A useful authority model is:

## Source / authoritative implementation

```text
tools/json-viewer-vX.X.X.py
```

Authoritative local viewer implementation for that release.

## Source records

```text
sidecars/*.json
```

and other structured records that feed catalogs.

## Aggregate records

```text
catalogs/*.json
```

Catalogs aggregate records for browsing, filtering, and discovery.

## Derived / companion artifacts

```text
json-viewer.html
open-json-viewer-vX.X.X.bat
json-manifest.json
catalog metadata
images/images.json
```

These artifacts are generated, synchronized, or maintained from other parts of the system.

Do not silently treat a derived artifact as the authority for source data.

---

# 19. Viewer Release Workflow

When the viewer itself changes materially, use a controlled release sequence.

## Step 1 — Classify the change

Determine whether this is:

- viewer functionality
- a catalog-specific renderer change
- support for a new document/catalog type
- a schema/profile recognition change
- a path/launcher correction
- a combination of the above

## Step 2 — Update the local viewer

Modify the current Python viewer.

If the change warrants a release, increment the viewer version.

Example:

```text
json-viewer-v1.6.0.py
        ↓
json-viewer-v1.7.0.py
```

Preserve the previous released viewer unless intentionally archiving/removing it.

## Step 3 — Test the local viewer

At minimum:

- launch succeeds
- folder tree works
- Tree works
- Raw works
- supported Catalog view works
- Preview pane works
- changed renderer works
- representative existing renderers still work

## Step 4 — Produce the online HTML companion

Update:

```text
json-viewer.html
```

The online edition should contain the corresponding current renderer behavior wherever technically practical.

Record the local viewer version from which the HTML edition was produced.

Recommended identity:

```text
Online JSON Viewer
Based on Local JSON Explorer vX.X.X
```

## Step 5 — Update the batch launcher

If the Python filename/version changed, update/create:

```text
open-json-viewer-vX.X.X.bat
```

Verify that it launches the intended Python version.

## Step 6 — Regenerate json-manifest.json

Run the manifest generator when the JSON inventory or relevant paths changed.

## Step 7 — Test the online viewer

Verify through GitHub Pages or an equivalent static server:

- manifest loads
- expected JSON files appear
- hierarchy is usable
- current catalog opens
- catalog-specific renderer works
- third/context preview works where supported
- representative sidecar preview works
- links resolve

## Step 8 — Commit and publish

Commit the coordinated release artifacts.

Do not assume that a successful push means GitHub Pages is already correct. Verify the published viewer.

---

# 20. Catalog Update Workflow

Not every catalog change requires a viewer release.

## Existing record type, existing structure

Typical sequence:

```text
new/updated sidecar
        ↓
update/rebuild catalog
        ↓
update catalog metadata if applicable
        ↓
regenerate json-manifest.json if inventory changed
        ↓
validate in viewer
```

Normally no viewer code change is required.

## Existing catalog family, new structure or desired presentation

Typical sequence:

```text
update source records/schema
        ↓
build new catalog generation
        ↓
inspect differences
        ↓
update catalog-specific viewer renderer
        ↓
test local viewer
        ↓
produce updated json-viewer.html
        ↓
update launcher if viewer version changed
        ↓
regenerate manifest if needed
        ↓
test online viewer
```

## New document/catalog family

Typical sequence:

```text
define source/sidecar structure
        ↓
create representative records
        ↓
define catalog aggregation
        ↓
build catalog
        ↓
decide useful filters and browsing behavior
        ↓
add viewer recognition
        ↓
add specialized renderer if warranted
        ↓
add third-pane preview if warranted
        ↓
test generic fallback
        ↓
test specialized presentation
        ↓
produce online viewer companion
```

---

# 21. Image Update Workflow

When repository images change:

```text
add / remove / rename image
        ↓
run images/build_images_json.py
        ↓
regenerate images/images.json
        ↓
verify expected image entry
        ↓
test Email Composer image selection if relevant
        ↓
commit / push
```

Do not mix this into every JSON catalog release unless images actually changed.

---

# 22. Viewer Design Principles

1. **Generic inspection is always available.** A specialized renderer is an enhancement, not a requirement for reading JSON.
2. **Human meaning matters.** A catalog should be rendered as the collection it represents when a useful domain view exists.
3. **Catalog families may differ.** Do not force unrelated data into a single schema solely for viewer convenience.
4. **Historical schemas may fall back gracefully.** Current structures deserve the best presentation; old archived schemas may use Tree/Raw.
5. **Sidecars preserve useful semantic content.** They enable discovery, cataloging, analysis, and compact previews.
6. **The full HTML remains the full publication.** A sidecar preview is not intended to replace it.
7. **The third pane preserves context.** Previewing an entry should not force the user to abandon the catalog or source structure currently being inspected.
8. **Repository hierarchy should remain visible.** Prefer a collapsible folder tree over a flattened file list.
9. **Local and online editions should be released together when viewer behavior changes.**
10. **Generated manifests have specific consumers.** Keep JSON inventory, image inventory, and site/web-app manifests conceptually separate.

---

# 23. Context Checklist for a New Work Session

Before changing the system, establish these facts:

```text
[ ] What is the current local viewer version?
[ ] What Python file is current?
[ ] What batch launcher points to it?
[ ] What version/source does json-viewer.html correspond to?
[ ] What catalogs currently exist?
[ ] Which catalog is current for each family?
[ ] What sidecar families currently exist?
[ ] What specialized renderers are currently supported?
[ ] Is the requested change generic or catalog-specific?
[ ] Does the requested change introduce a new document/catalog type?
[ ] Does json-manifest.json need regeneration?
[ ] Did repository images change?
[ ] If yes, does images/images.json need regeneration?
[ ] Did root-site identity/icons/start behavior change?
[ ] If yes, do site/web-app manifests need review?
```

A future ChatGPT conversation should be able to read this README, inspect the current repository files, and answer these questions before proposing implementation changes.

---

# 24. Current Known Version Context

At the time this README was written:

```text
Local viewer:
    tools/json-viewer-v1.6.0.py

Local launcher:
    open-json-viewer-v1.6.0.bat

Online viewer:
    json-viewer.html

Online inventory:
    json-manifest.json

Online inventory generator:
    manifest.py

Image inventory:
    images/images.json

Image inventory generator:
    images/build_images_json.py
```

Viewer v1.6.0 includes the PST-SP study-guide renderer.

Future releases should update this section or replace it with a release-history section.

---

# 25. Documentation Roles

The existing version-specific upgrade README should remain useful as release history.

This system README should remain focused on architecture and maintenance behavior.

Recommended pattern:

```text
tools/
├── json-viewer-system-readme.md
├── json-viewer-v1.6.0-upgrade-readme.md
├── json-viewer-v1.6.0.py
└── future release notes...
```

The system README answers:

> What is this system and how do its parts relate?

Version-specific READMEs answer:

> What changed in this release and how was it produced?

Workflow JSON answers:

> What controlled sequence should be followed when maintaining or releasing it?
