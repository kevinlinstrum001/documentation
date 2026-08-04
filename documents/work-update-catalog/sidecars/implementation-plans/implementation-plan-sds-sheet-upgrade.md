# Inventory 3.0 SDS Registry Rebuild and App Integration

**Document type:** Implementation plan  
**Plan status:** Draft ready for review and approval  
**Created:** 2026-08-04  
**Planned work-session start:** TBD  
**Planned work-session end:** TBD  
**Candidate work window:** After work on 2026-08-04 or during the weekend of 2026-08-08–2026-08-09  
**Primary project:** Inventory 3.0  
**Parent project:** Klinswork  
**Project ID:** Not yet assigned; project catalog remains in bootstrap development  
**Current application version:** `ROUTE-TEST-0115`

## 1. Purpose

Rebuild the Inventory 3.0 `SDS` sheet as a structured operational SDS registry, populate it from the assembled Klinswork Chemical Product Catalog, correct a small set of conclusively resolved product-reference errors, and update Inventory 3.0 so product pages and SDS action panels display the current SDS record together with its verification status, coverage, issues, and document access state.

The work preserves two independent facts:

- `current` identifies the active SDS row the application should use for a product.
- `status` describes the quality and verification condition of that active record.

A current record may therefore remain `partially_verified` or `conflicting_sources`. Current status does not imply that every issue has been resolved.

## 2. Planning basis

This plan is based on:

- the assembled `klinswork-chemical-product-catalog-001.json`
- the current Inventory 3.0 spreadsheet and `SDS` tab
- the current Inventory 3.0 Apps Script source
- the supplied `Index.html`, `Scripts.html`, `Code.gs`, `DataService.gs`, `Config.gs`, shared validation functions, and inventory business rules
- the established implementation-plan workflow
- the current bootstrap project naming convention used while formal project records are not yet available

The chemical catalog contains twelve workplace-product records:

- 3 `verified`
- 5 `partially_verified`
- 4 `conflicting_sources`

Catalog inclusion does not override those record statuses.

## 3. Authoritative resources

### Inventory spreadsheet

- **Spreadsheet:** Inventory-3.0
- **Spreadsheet ID:** `1bdsasTjlBr20_Kr89tbPy7HWE8xMWLzQH5Z2l5BEviI`
- **SDS tab:** `SDS`
- **SDS sheet ID:** `87941017`
- **SDS tab URL:**  
  `https://docs.google.com/spreadsheets/d/1bdsasTjlBr20_Kr89tbPy7HWE8xMWLzQH5Z2l5BEviI/edit?gid=87941017#gid=87941017`

### Apps Script application

- **Source project URL:**  
  `https://script.google.com/home/projects/1q1diIzyslOWet_ZRt-iLTVovaQf9P9jGgqtXZ3QFii-qm_uvGHxU-CA1/edit`
- **Canonical deployment URL:**  
  `https://script.google.com/macros/s/AKfycbwj6qFGpouW_HBx9_EudvlFgWZCAUK9f7RZz0ZqYuI_E_YrWhprurtEBAXZaqENVBcMDQ/exec`
- **Deployment ID:**  
  `AKfycbwj6qFGpouW_HBx9_EudvlFgWZCAUK9f7RZz0ZqYuI_E_YrWhprurtEBAXZaqENVBcMDQ`

### Documentation repository

- **Repository:** `kevinlinstrum001/documentation`
- **Implementation-plan document collection:** location to be confirmed
- **Implementation-plan sidecar collection:** `sidecars/implementation-plans/`
- **Future catalog location:** `catalogs/`
- **Future project-catalog root:** `documents/work-update-catalog/`

## 4. Current state

The current `SDS` tab:

- contains seven records for CHEM-001 through CHEM-007
- uses the columns `sds_id`, `product_id`, `revision_date`, `document_url`, `source`, `date_verified`, and `current`
- treats `current` as the only record-state indicator
- combines manufacturer, document owner, and host information in one `source` field
- cannot represent product-match status, section coverage, known issues, corrective actions, or source unavailability
- omits CHEM-008 through CHEM-012
- contains superseded SDS revisions for CHEM-003, CHEM-005, and CHEM-007
- cannot distinguish “not researched” from “researched but no official SDS is available”

The current browser code:

- loads all SDS rows through `getAppData()`
- joins rows to products using `product_id`
- selects the first row with an active `current` value
- silently falls back to the first matching row when none is current
- displays only revision date, source, review date, and the SDS link
- reports “No SDS record” when no row exists, even when the absence or conflict is itself known information

## 5. Target state

At the end of the session:

1. The `SDS` tab contains one current operational row for every product from CHEM-001 through CHEM-012.
2. Superseded SDS revisions remain as historical rows with `current = FALSE`.
3. `current` and `status` are independent.
4. Every current row identifies the exact SDS or explicitly records that the source is unavailable.
5. Current rows record product match, section coverage, issue summary, and action needed.
6. Inventory 3.0 displays current SDS status without withholding an available document merely because the record is partial or conflicting.
7. The application never silently substitutes a historical row.
8. Missing-current and multiple-current conditions are reported as data-integrity problems.
9. Known, conclusive product-reference errors are corrected.
10. Genuine source conflicts remain visible rather than being edited away.
11. Existing inventory transactions continue to operate unchanged.
12. A new Apps Script version is deployed and verified at the canonical `/exec` URL.

## 6. Scope

### In scope

- backing up the current `SDS` tab
- rebuilding the `SDS` sheet structure
- creating and populating twelve current SDS registry rows
- retaining at least three superseded historical rows
- adding controlled data-validation lists
- adding status-oriented conditional formatting
- adding a check for multiple current rows per product
- correcting conclusively resolved product-reference fields in the `Products` tab
- modifying `Scripts.html`
- modifying `Styles.html`
- updating `Config.gs` only for the application version
- testing the sheet-to-app integration
- deploying and verifying the updated application
- collecting evidence for the later work summary and implementation-plan sidecar

### Out of scope

- changing inventory quantity calculations
- changing opening-balance, receive, use, correction, or transfer operations
- changing inventory event creation or rollback behavior
- rewriting `DataService.gs`
- changing the configured spreadsheet ID or sheet names
- placing the complete SDS section text in Google Sheets
- resolving manufacturer contradictions by inventing a preferred value
- obtaining a missing official NMCI SDS during this implementation session unless it becomes immediately available
- building the project catalog
- building the future implementation-plan catalog
- creating a new authorization or role-access system
- redesigning the entire Inventory 3.0 interface

## 7. New SDS sheet structure

The sheet will use one row per SDS document revision.

### Proposed columns

```text
sds_id
product_id
current
status
catalog_entry_id
sds_identifier
official_product_name
manufacturer_product_id
form_or_use_state
revision_date
version
jurisdiction
language
document_url
source
source_owner
source_type
access_status
saved_copy_url
date_verified
product_match_status
coverage_status
complete_sections
partial_sections
unresolved_sections
issue_summary
action_needed
superseded_by_sds_id
notes
```

### Default visible columns

The following columns should remain visible for ordinary maintenance:

```text
sds_id
product_id
current
status
sds_identifier
revision_date
source
date_verified
coverage_status
issue_summary
action_needed
document_url
```

Technical and provenance columns may be grouped or hidden to the right.

### Date handling

`revision_date` and `date_verified` represent date-only values. They should be stored as text in `YYYY-MM-DD` form so `DataService.gs` does not convert them into timezone-sensitive ISO timestamps.

### Controlled values

#### `status`

```text
unverified
candidate
partially_verified
verified
conflicting_sources
rejected
```

#### `product_match_status`

```text
unverified
partially_verified
verified
conflicting_sources
```

#### `coverage_status`

```text
pending
complete
partial
source_unavailable
```

#### `access_status`

```text
accessible
manufacturer_link_blocked
distributor_copy
local_copy
source_unavailable
```

#### `source_type`

```text
manufacturer_official
manufacturer_document_system
distributor_hosted_manufacturer_sds
local_repository_copy
source_unavailable
```

### Record rules

1. `sds_id` must be unique.
2. `product_id` must resolve to the `Products` tab.
3. A product may have more than one SDS revision.
4. A product may have no more than one `current = TRUE` row.
5. A current record may have any controlled verification status.
6. Historical records use `current = FALSE`.
7. A missing `document_url` is permitted when `access_status = source_unavailable`.
8. `revision_date` describes the document; `date_verified` describes the review.
9. Status changes do not remove issue history.
10. The chemical catalog remains the detailed research authority; this sheet is its operational projection.

## 8. Planned record population

The rebuilt sheet will contain at least fifteen rows:

- 12 current records, one for each CHEM-001 through CHEM-012
- 3 historical records for superseded SDS revisions:
  - CHEM-003 revision dated 2020-09-06
  - CHEM-005 revision dated 2019-03-29
  - CHEM-007 revision dated 2019-03-29

The historical rows will use `current = FALSE` and point to their replacements through `superseded_by_sds_id`.

### Representative current-record conditions

- **CHEM-012:** verified, full section coverage, current document available
- **CHEM-009:** partially verified, current document available, manufacturer page retrieval issue retained
- **CHEM-011:** conflicting sources, current document available, internal SDS inconsistency retained
- **CHEM-008:** conflicting sources, current registry row present, official SDS unavailable, product-form conflict retained
- **CHEM-003:** current replacement plus historical superseded row

## 9. Conclusive Products-tab corrections

The session may correct product-reference fields when the catalog evidence is conclusive.

Planned corrections:

- **CHEM-001:** change manufacturer product code from `496331` to `4963331`
- **CHEM-005:** change manufacturer product code from `31478` to `31415`
- **CHEM-006:** use the confirmed product identifier `2LEF5`; preserve the prior unsupported identifier in notes if needed
- **CHEM-009:** identify the item as a PURELL Advanced Hand Sanitizer Fragrance Free Foam refill rather than dispenser hardware
- **CHEM-010:** identify the item as a PURELL Healthy Soap refill rather than dispenser hardware

The following remain issues rather than silent corrections:

- CHEM-003 manufacturer use-dilution discrepancy
- CHEM-006 conflicting color and VOC descriptions
- CHEM-007 package-size and identifier history
- CHEM-008 concentrate-versus-ready-to-use conflict and missing official SDS
- CHEM-011 internal hazard-versus-toxicology inconsistency

Any Products-tab edit must be reviewed against the current row before writing.

## 10. Apps Script change map

### `Index.html`

**Expected change:** none.

The page already includes:

```javascript
<?!= include('Styles'); ?>
<?!= include('Scripts'); ?>
```

It already provides the product-page and action-sheet containers required for the SDS presentation.

### `Code.gs`

**Expected change:** none.

`getAppData()` already returns:

```javascript
sds: readTable(CONFIG.SHEETS.SDS)
```

The new sheet columns will be returned automatically.

### `DataService.gs`

**Expected change:** none.

`readTable()` already:

- reads every populated header
- rejects blank headers
- rejects duplicate headers
- converts each row to an object
- passes new columns through without a schema rewrite

### `Config.gs`

**Required change:** update `CONFIG.APP_VERSION` after implementation.

The following remain unchanged:

```javascript
SPREADSHEET_ID
SHEETS.SDS
```

### Shared validation file

**Expected change:** none.

It validates inventory commands, quantities, products, and locations. It does not validate or write SDS records.

### Inventory business-rules file

**Expected change:** none.

Opening balances, receiving, use, corrections, transfers, event creation, and rollback are outside the SDS change.

### `Scripts.html`

**Required changes:**

1. Add one shared case-insensitive product-to-SDS lookup path.
2. Add `getSdsRecordsForProduct(productId)`.
3. Add `getCurrentSdsRecord(productId)` or an equivalent result helper.
4. Remove the fallback to `records[0]`.
5. Detect no-current and multiple-current states.
6. Update `renderProductPage()`.
7. Update `renderSdsAction()`.
8. Display:
   - status
   - SDS identifier
   - revision date
   - source
   - review date
   - coverage status
   - issue summary
   - action needed
9. Keep the **Open SDS** button available whenever `document_url` is present.
10. Display a known source-unavailable record instead of “No SDS record.”
11. Add controlled-value formatting helpers.
12. Keep relative and absolute document URLs working through `makeAbsoluteProjectUrl()`.

### `Styles.html`

**Required changes:**

Add visual treatment for:

- verified
- partially verified
- conflicting sources
- unverified
- source unavailable
- integrity warning
- compact SDS detail groups

The styles should support both the full product page and the action-sheet view.

## 11. Implementation stages

### Stage 1 — Preserve the current state

**Objective:** Create a recoverable before-state.

**Actions:**

- duplicate or export the current `SDS` tab
- record its existing headers and seven rows
- capture the current app version and deployment URL
- take representative screenshots of current SDS behavior

**Exit criteria:**

- the current SDS data can be restored
- the current application behavior is documented

### Stage 2 — Build the new sheet structure

**Objective:** Establish the new headers, validation, and maintenance view.

**Actions:**

- clear or replace the working `SDS` tab
- add the approved headers
- format date-only columns as text
- add dropdown validation
- freeze the header row
- enable filtering
- group technical columns
- add conditional formatting
- add a duplicate-current warning formula or review check

**Exit criteria:**

- headers are unique and nonblank
- `readTable('SDS')` can read the new structure
- controlled columns reject or flag unsupported values

### Stage 3 — Populate current and historical records

**Objective:** Transfer catalog knowledge into the operational registry.

**Actions:**

- create one current row for CHEM-001 through CHEM-012
- create historical rows for superseded CHEM-003, CHEM-005, and CHEM-007 SDS revisions
- record exact SDS identifiers, versions, form states, source roles, status, coverage, issues, and actions
- verify every product has exactly one current row

**Exit criteria:**

- 12 products have current records
- historical rows are noncurrent
- no duplicate `sds_id` exists
- no product has multiple current rows
- CHEM-008 has a current source-unavailable registry row

### Stage 4 — Apply conclusive product corrections

**Objective:** Remove small identity errors that the catalog resolved.

**Actions:**

- review the current Products rows
- apply only the approved corrections
- preserve prior identifiers in notes when useful
- do not overwrite genuine unresolved conflicts

**Exit criteria:**

- corrected product details agree with the catalog
- unresolved issues remain visible

### Stage 5 — Refactor SDS record selection

**Objective:** Make the client use one controlled selection method.

**Actions in `Scripts.html`:**

- add shared lookup helpers
- normalize product IDs consistently
- return one current record or an explicit integrity result
- remove arbitrary first-row fallback

**Exit criteria:**

- product page and action panel resolve the same record
- no-current and multiple-current conditions are distinguishable

### Stage 6 — Update SDS presentation

**Objective:** Display the new operational information.

**Actions in `Scripts.html`:**

- update `renderProductPage()`
- update `renderSdsAction()`
- render status and coverage
- render issues and actions when present
- render source-unavailable records
- preserve document buttons for partial and conflicting records

**Exit criteria:**

- representative records render correctly
- no SDS document is hidden solely because its status is not verified

### Stage 7 — Add status styling

**Objective:** Make record condition readable without confusing status with availability.

**Actions in `Styles.html`:**

- add status badges
- add issue and integrity-warning blocks
- preserve mobile readability
- keep labels accessible as text rather than color alone

**Exit criteria:**

- states are visually distinct
- meaning does not depend only on color
- product page and action sheet remain readable

### Stage 8 — Update version and run regression checks

**Objective:** Prepare a deployable application revision.

**Actions:**

- update `CONFIG.APP_VERSION`
- load the app from the development deployment
- verify location selection and product browsing
- verify opening, receive, use, correct, and transfer controls remain available
- verify product details and SDS actions

**Exit criteria:**

- no unrelated inventory regression is observed
- the new application version is visible

### Stage 9 — Deploy and verify

**Objective:** Publish the approved revision.

**Actions:**

- create a new Apps Script deployment version
- update the existing deployment
- open the canonical `/exec` URL
- perform the final test matrix
- record screenshots and verification time

**Exit criteria:**

- the canonical deployment serves the new version
- all required acceptance tests pass or receive explicit dispositions

### Stage 10 — Declare the documentation checkpoint

**Objective:** Stop implementation and preserve the result.

**Actions:**

- record actual start and stop times
- classify completed, partial, failed, deferred, or newly discovered work
- preserve changed files and test evidence
- prepare the session summary
- generate the implementation-plan sidecar after this Markdown plan is approved and assigned its final repository path

**Exit criteria:**

- the work boundary is clear
- evidence is sufficient for the summary and sidecar

## 12. Planned tests

### TEST-SDS-001 — Sheet structure loads

**Type:** integration

**Preconditions:**

- new headers exist
- at least one data row exists

**Steps:**

1. Run `getAppData()`.
2. Inspect the returned `sds` array.
3. Confirm new properties are present.

**Expected result:** SDS rows load without blank-header or duplicate-header errors.

**Failure condition:** `readTable()` throws or required fields are absent.

### TEST-SDS-002 — One current row per product

**Type:** data integrity

**Steps:**

1. Group rows by `product_id`.
2. Count active `current` rows.
3. Review CHEM-001 through CHEM-012.

**Expected result:** Every product has exactly one current row.

**Failure condition:** Any product has zero or more than one current row.

### TEST-SDS-003 — Verified record

**Product:** CHEM-012

**Expected result:**

- status displays as verified
- SDS identifier and revision display
- coverage displays as complete
- Open SDS button works

### TEST-SDS-004 — Partially verified record

**Product:** CHEM-009

**Expected result:**

- status displays as partially verified
- the current SDS remains openable
- the manufacturer-page limitation appears as an issue rather than blocking document access

### TEST-SDS-005 — Conflicting record with document

**Product:** CHEM-011

**Expected result:**

- status displays as conflicting sources
- issue summary is visible
- current SDS link remains available

### TEST-SDS-006 — Source unavailable

**Product:** CHEM-008

**Expected result:**

- a current registry record is displayed
- status and product-form conflict are visible
- no document button appears
- the interface does not say “No SDS record”

### TEST-SDS-007 — Historical revision is not selected

**Product:** CHEM-003

**Expected result:**

- current replacement is displayed
- superseded row is not selected
- historical row remains in the sheet

### TEST-SDS-008 — No current row

**Type:** integrity failure test

**Steps:**

1. In a temporary test copy, remove the current flag for one product.
2. Open its SDS view.

**Expected result:** The app reports that SDS records exist but none is current.

**Failure condition:** The app silently displays the first historical row.

### TEST-SDS-009 — Multiple current rows

**Type:** integrity failure test

**Steps:**

1. In a temporary test copy, mark two rows current for one product.
2. Open its SDS view.

**Expected result:** The app reports a multiple-current integrity problem.

**Failure condition:** The app silently chooses one record.

### TEST-SDS-010 — Relative and absolute URLs

**Expected result:** Both external URLs and repository-relative URLs open through the existing URL resolver.

### TEST-SDS-011 — Product-page and action-panel consistency

**Expected result:** Both views show the same current record, status, revision, and issue.

### TEST-SDS-012 — Inventory regression

**Expected result:**

- location selection works
- product search and filters work
- opening balance behavior is unchanged
- receive, use, correct, and transfer flows remain available
- no SDS change modifies inventory quantities or event history

### TEST-SDS-013 — Canonical deployment

**Expected result:** The canonical `/exec` URL displays the updated application version and new SDS presentation.

## 13. Acceptance criteria

The session is complete when:

1. The `SDS` tab has the approved structure.
2. All twelve products have exactly one current registry row.
3. Superseded CHEM-003, CHEM-005, and CHEM-007 records remain as noncurrent history.
4. Status and current are interpreted independently.
5. CHEM-008 is represented as a current source-unavailable/conflicting record.
6. The application does not fall back to an arbitrary historical row.
7. Product page and SDS panel display the same current record.
8. Available SDS documents remain openable for partial and conflicting records.
9. Conclusive Products-tab identity corrections are applied and verified.
10. Genuine conflicts remain documented.
11. Inventory transaction behavior shows no observed regression.
12. `CONFIG.APP_VERSION` is updated.
13. The canonical deployment is updated and verified.
14. Actual start, stop, test results, deviations, and unresolved items are recorded.

## 14. Risks and mitigations

### Risk: duplicate or blank headers break the entire app data load

**Likelihood:** medium  
**Impact:** high

**Mitigation:** Build and validate the header row before populating data. Use `DataService.gs` requirements as blocking checks.

**Contingency:** Restore the backed-up SDS tab.

### Risk: a product receives multiple current rows

**Likelihood:** medium  
**Impact:** high

**Mitigation:** Add a duplicate-current sheet check and an application integrity warning.

**Contingency:** Correct the current flags before deployment.

### Risk: historical SDS is shown as current

**Likelihood:** low after refactor  
**Impact:** high

**Mitigation:** Remove `records[0]` fallback and require an explicit current row.

### Risk: issue status is mistaken for document invalidity

**Likelihood:** medium  
**Impact:** medium

**Mitigation:** Keep status and document availability separate. Do not suppress the Open SDS button when a document exists.

### Risk: date values shift because Sheets returns JavaScript Date objects

**Likelihood:** medium  
**Impact:** medium

**Mitigation:** Store date-only fields as `YYYY-MM-DD` text.

### Risk: product cleanup expands beyond the session boundary

**Likelihood:** medium  
**Impact:** medium

**Mitigation:** Correct only conclusively resolved identifiers and refill descriptions. Preserve genuine conflicts as issues.

### Risk: rebuilding the tab disrupts the deployed application before code changes are ready

**Likelihood:** medium  
**Impact:** high

**Mitigation:** Preserve backward-compatible column names and build the new data before deploying client changes.

**Contingency:** Restore the original tab from backup.

### Risk: unrelated inventory behavior regresses

**Likelihood:** low  
**Impact:** high

**Mitigation:** Do not modify quantity, event, validation, or rollback files. Run the inventory regression test before deployment.

## 15. Recovery and rollback plan

Before implementation:

1. Duplicate or export the current `SDS` tab.
2. preserve the current Apps Script source version
3. record the current deployment and application version
4. retain the original seven-row dataset

If sheet migration fails:

- restore the original SDS tab
- confirm `getAppData()` loads
- postpone application changes

If client changes fail:

- restore the prior `Scripts.html` and `Styles.html`
- restore the prior `APP_VERSION`
- redeploy the last working Apps Script version

If final verification fails:

- do not classify the milestone as complete
- record partial or failed results
- preserve evidence and required follow-up work

## 16. Evidence to collect

During the session, preserve:

- original and rebuilt SDS header rows
- row count and current-row validation results
- representative current and historical rows
- Products-tab corrections
- changed Apps Script files
- application version before and after
- screenshots for CHEM-012, CHEM-009, CHEM-011, CHEM-008, and CHEM-003
- no-current and multiple-current integrity behavior
- final deployment URL and verification timestamp
- regression-test results
- deviations from this plan

## 17. Expected changed artifacts

### Data

- Inventory 3.0 `SDS` tab
- selected Inventory 3.0 `Products` rows

### Apps Script

- `Scripts.html`
- `Styles.html`
- `Config.gs` — version only

### Expected unchanged artifacts

- `Index.html`
- `Code.gs`
- `DataService.gs`
- shared inventory validation file
- inventory business-rules file

A file may be added to the changed set only when implementation evidence shows that the current assumption is wrong. Such a change must be recorded as a plan amendment.

## 18. Known unresolved items

- formal Inventory 3.0 project ID
- formal Inventory 3.0 project-record path
- final repository path for this Markdown plan
- implementation-plan catalog ID and entry ID
- final implementation-plan sidecar filename
- exact scheduled start and stop
- final post-change `APP_VERSION`
- final deployment verification timestamp
- whether an official NMCI 51-CCGC SDS becomes available before execution

These items do not block plan approval.

## 19. Approval and scheduling gate

Before implementation begins:

1. Review this plan.
2. Correct any scope, data-model, or test assumptions.
3. Approve the plan as the tactical baseline.
4. Assign the work-session date and time.
5. Record the schedule without changing the approved technical baseline.
6. Begin implementation in the bounded work-session conversation.
7. Record later changes as plan amendments rather than rewriting the original plan silently.

---

**Planned result:** Inventory 3.0 will use a complete, status-aware SDS registry derived from the chemical catalog, while preserving historical SDS records, known issues, document access, and existing inventory behavior.
