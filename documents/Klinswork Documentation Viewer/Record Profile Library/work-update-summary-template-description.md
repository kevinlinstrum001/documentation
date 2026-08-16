---
template_name: work-update-summary-template-1.0-draft
template_version: 1.0-draft
record_type: work-update-summary
record_family: human-readable-retrospective-master
status: draft
authority_role: canonical-human-readable-retrospective-master-for-one-work-update
created: 2026-08-16
updated: 2026-08-16
master_source: true
downstream_products:
  - work-update-sidecar.json
  - work-update.html
---

# Work Update Summary

> **Template:** `work-update-summary-template-1.0-draft.md`
>
> **Purpose:** Preserve a detailed, durable, retrospective reconstruction of a bounded work period so that a future reader—especially a context-naive future ChatGPT session—can understand what work existed, what was intended, what actually happened, what changed, why it mattered, what evidence supports the account, and where work should resume.
>
> **Master-source rule:** This Markdown document is the **canonical human-readable master** for the Work Update. The structured sidecar and downstream HTML are derived products. They may reorganize, summarize, visualize, or selectively omit material for their own purposes, but they must remain grounded in this master and must not silently become the authority over its substantive narrative.
>
> **Detail rule:** Prefer useful completeness over brevity. A Work Update Summary is expected to preserve substantial context, chronology, reasoning, evidence, decisions, deviations, discoveries, validation, resulting-state information, and continuation guidance. Do not compress significant work into terse bullets merely because the underlying Work Unit Activities, Activities, plans, session records, or source artifacts exist elsewhere.
>
> **AI-reconstruction rule:** Write so that a future ChatGPT session that did not participate in the original work can reconstruct not only **what changed**, but **why the work existed, what state preceded it, how decisions emerged, what went wrong or changed unexpectedly, which authorities were consulted, how confidence was established, and what became true afterward**.
>
> **Human-reading rule:** The downstream `work-update.html` is the primary polished reading product for human review. The Markdown master may therefore be denser, longer, more explicit, and more reference-rich than the HTML.
>
> **Information-preservation rule:** Information may be omitted or visually compressed in the downstream HTML for readability without being omitted from this Markdown master.
>
> **Authority boundary:** This Work Update synthesizes durable records. It does **not** replace the authorities that own the underlying facts:
>
> - Work Unit Registry → current Work Unit state
> - Work Unit Activities → timestamped material Work Unit history
> - Implementation Plan → intended body of work
> - Work Implementation Session → detailed formal-session execution record
> - Resource Registry → current Resource identity and routing
> - Activities → timestamped material Resource history
> - Project records → Project identity and meaning
> - System Summary → current System meaning/state
> - System Roadmap → intended future System direction
> - current source/data/deployment/tests → current implementation truth
> - Architecture Changelog → formal architecture-change history where applicable
>
> **Retrospective role:** The Work Update exists to connect these authorities into a coherent narrative of **change, meaning, and consequence**.
>
> **Temporal honesty rule:** Preserve actual chronology. If plans, templates, profiles, authorities, or formal records were created after work had already begun, say so explicitly. Do not rewrite retrospective planning as though it were prospective.
>
> **Selective-redundancy rule:** Some duplication is desirable when it improves future reconstruction. Restate enough of a Work Unit goal, decision, test result, Activity, or source fact that the Work Update remains understandable without immediately opening every referenced record.
>
> **Color-redundancy rule:** Color, icons, typography, and layout may reinforce meaning, but the text must state the semantic role explicitly. No substantive fact may depend on color alone.

---

# Table of Contents

> **Template rule:** Every substantial Work Update Summary should include a Table of Contents near the beginning. Update the links and subsection depth to match the final document. The TOC is part of the retrieval architecture for long-form master documents.

1. [Work Update Identity](#1-work-update-identity)
2. [Purpose and Reporting Boundary](#2-purpose-and-reporting-boundary)
3. [Executive Summary](#3-executive-summary)
4. [Starting State](#4-starting-state)
5. [Intended Work and Governing Plans](#5-intended-work-and-governing-plans)
6. [Detailed Work Chronology](#6-detailed-work-chronology)
7. [Work Performed by Work Unit / Session](#7-work-performed-by-work-unit--session)
8. [Decisions, Deviations, Blockers, and Discoveries](#8-decisions-deviations-blockers-and-discoveries)
9. [Validation, Testing, and Confidence](#9-validation-testing-and-confidence)
10. [Resource, Registry, and Activity Effects](#10-resource-registry-and-activity-effects)
11. [Project and System Delta](#11-project-and-system-delta)
12. [Architecture and Documentation Effects](#12-architecture-and-documentation-effects)
13. [Context Restoration and Cross-Session Testing](#13-context-restoration-and-cross-session-testing)
14. [Knowledge Produced](#14-knowledge-produced)
15. [Resulting State](#15-resulting-state)
16. [Remaining Work and Open Determinations](#16-remaining-work-and-open-determinations)
17. [Continuation Point](#17-continuation-point)
18. [Important Artifacts and References](#18-important-artifacts-and-references)
19. [Provenance and Interpretation Limits](#19-provenance-and-interpretation-limits)
20. [Downstream HTML Projection Notes](#20-downstream-html-projection-notes)
21. [Work Update Completion Check](#21-work-update-completion-check)
22. [Appendix A — Visual and Editorial Grammar](#appendix-a--visual-and-editorial-grammar)
23. [Appendix B — Authority Separation](#appendix-b--authority-separation)
24. [Appendix C — Minimum Viable Work Update](#appendix-c--minimum-viable-work-update)
25. [Appendix D — Template Design Rules](#appendix-d--template-design-rules)

---

# 1. Work Update Identity

## 1.1 Update metadata

| Field | Value |
|---|---|
| Work Update title | |
| Reporting period start | |
| Reporting period end | |
| Work Update date | |
| Created timestamp | |
| Updated timestamp | |
| Update status | `draft / reviewed / final` |
| Primary Project(s) | |
| Primary System(s) | |
| Primary Application / implementation surface(s) | |
| Work Unit ID(s) | |
| Formal Work Implementation Session record(s) | |
| Implementation Plan(s) | |
| Primary operational environment | |
| Source conversation / session reference | |
| Master Markdown path | |
| Sidecar path | |
| Downstream HTML path | |
| Prepared by | |
| Reviewed by | |

## 1.2 Semantic placement

> State how this Work Update sits within Klinswork without collapsing Project, System, Resource, implementation, repository path, or lifecycle.

```text
Klinswork
└── [Project]
    └── [Child Project if applicable]
        └── [System]
            └── [Applications / datastores / Resources / implementation surfaces]
```

### 🩵 Project(s)

- **Project:**  
- **Relationship to this update:**  

### 🟦 System(s)

- **System:**  
- **Relationship to this update:**  

### 🟪 Resource(s)

- **Resource:**  
- **Relationship to this update:**  

### 🟧 Work Unit(s)

- **Work Unit:**  
- **Relationship to this update:**  

## 1.3 Update coverage summary

> In 1–3 paragraphs, explain what body of work this document covers and why this reporting boundary is coherent.

---

# 2. Purpose and Reporting Boundary

## 2.1 Why this Work Update exists

> Explain why this period deserves a Work Update. Describe the work as a coherent story rather than merely as a collection of files changed.

## 2.2 Reporting boundary

**Included in this Work Update:**

- 
- 
- 

**Not included / intentionally outside this Work Update:**

- 
- 
- 

## 2.3 Authority statement

> Explain which records remain authoritative for the facts summarized here.

Example:

```text
Work Unit current state
    → Work Units Registry

Work Unit material history
    → Work Unit Activities

Resource current state
    → Resources

Resource material history
    → Activities

Intended work
    → Implementation Plan

Formal execution detail
    → Work Implementation Session

Current System meaning
    → System Summary

Retrospective cross-authority synthesis
    → this Work Update Summary
```

## 2.4 Reconstruction boundary, if applicable

**Reconstruction occurred:** `yes / no`

**Reconstruction mode:**

- `none`
- `reconstructed-during-work`
- `reconstructed-after-work`
- `mixed`

**Temporal boundary:**

>

**What had already happened before formal planning / recording caught up:**

>

**Evidence used to reconstruct chronology:**

- 
- 
- 

> **🟨 Decision / chronology rule:** Never make later-created planning or documentation infrastructure appear to have existed before it actually did.

---

# 3. Executive Summary

> **Style rule:** Keep this section compact enough to orient a reader, but do not use it as an excuse to make the rest of the document sparse.

## 3.1 What happened

> 2–6 substantial paragraphs explaining the overall story of the work period.

## 3.2 Major outcomes

- 🟩 **Completed / confirmed:**  
- 🟩 **Completed / confirmed:**  
- 🟨 **Decision / architecture change:**  
- 🟧 **Work Unit outcome:**  
- 🟥 **Problem discovered / corrected:**  
- ⬜ **Open determination:**  

## 3.3 Why it mattered

> Explain the significance of the work in terms of Klinswork capability, architecture, documentation quality, operational usefulness, context restoration, or future work.

## 3.4 One-sentence retrospective

> **If a future reader remembers only one sentence about this work period, it should be:**
>
> 

---

# 4. Starting State

> **Detail rule:** This section should be rich enough that the resulting-state sections later in the document can show a meaningful delta.

## 4.1 Work Unit starting state

| Work Unit | Status | Readiness | Goal | Completion rule | Formal session | Implementation plan state |
|---|---|---|---|---|---|---|
| | | | | | | |

### Material prior Work Unit Activities

| WUA ID | Timestamp | Event type | Material effect | Why relevant at the start |
|---|---|---|---|---|
| | | | | |

## 4.2 Project starting state

### 🩵 Project — [name]

> Describe current purpose, documentation maturity, hierarchy, known relationships, unresolved questions, and any ambiguity relevant to the work.

## 4.3 System starting state

### 🟦 System — [name]

> Describe the known current System state at the start of the reporting period. Distinguish verified current behavior from roadmap intent and historical evidence.

## 4.4 Resource / Registry starting state

> Describe the relevant Registry state, important Resource identities, routing assumptions, missing links, stale entries, duplicate internal datasets, or other conditions that shaped the work.

## 4.5 Documentation starting state

> Describe the state of templates, profiles, READMEs, summaries, sidecars, Viewer discovery, catalogs, architecture rules, and other documentation infrastructure that existed before this work period.

## 4.6 Physical repository starting state

> Record only relevant physical facts. Repository location does not establish semantic identity.

### 🟨 Folder / repository locations

```text
[path]
[path]
[path]
```

## 4.7 Known uncertainties at the start

- ⬜ **Open:**  
- ⬜ **Open:**  
- ⬜ **Open:**  

## 4.8 Important pre-existing assumptions

> Record assumptions that influenced the work, especially assumptions later disproved or revised.

- 
- 
- 

---

# 5. Intended Work and Governing Plans

> **Rule:** Summarize enough intended work to make later deviations and outcomes understandable. Do not duplicate the complete Implementation Plan.

## 5.1 Governing Work Unit goal

**Work Unit:** `WORK-____`

**Goal:**

>

**Completion rule:**

>

## 5.2 Governing Implementation Plan

**Plan title:**

**Planning mode:**

**Plan authority boundary:**

**Important stages relevant to this update:**

1. 
2. 
3. 

## 5.3 Intended target state

> What did the plan expect to become true?

## 5.4 Acceptance criteria most relevant to the retrospective

| Criterion ID | Intended criterion | Final result | Where discussed later |
|---|---|---|---|
| | | | |

## 5.5 Planned tests most relevant to the retrospective

| Test ID | Planned purpose | Expected result | Was it executed? |
|---|---|---|---|
| | | | |

## 5.6 Constraints and non-goals

- 
- 
- 

## 5.7 Important activation gates / prerequisites

> Record any prerequisite that controlled whether formal implementation could become active.

---

# 6. Detailed Work Chronology

> **Chronology rule:** Preserve cause and effect. Include enough sequence that a future reader can tell why later changes happened. Do not turn this into a keystroke log.

## 6.1 Chronology overview

| Time / phase | Semantic marker | Event | Durable consequence | Evidence |
|---|---|---|---|---|
| | 🟧 Work Unit | | | |
| | 🟨 Decision | | | |
| | 🟩 Validation | | | |
| | 🟥 Problem | | | |

---

## 6.2 Chronology entry template

### [HH:MM / date / phase] — [semantic marker] [event title]

**Related Work Unit:**  
**Related WUA:**  
**Related Activity:**  
**Related Project/System/Resource:**  

#### What happened

>

#### Why this happened

>

#### Evidence / context

- 
- 

#### What changed as a result

>

#### Why this mattered

>

#### What this led to next

>

---

<!-- Duplicate chronology-entry blocks as needed. -->

## 6.3 Chronology interpretation

> After the detailed sequence, explain the larger pattern. This section should answer questions like:
>
> - Which events caused later architecture changes?
> - Which discoveries changed the plan?
> - Which failures exposed missing context?
> - Which steps were necessary only because supporting infrastructure was immature?
> - Which actions were cleanup versus substantive system-building?

---

# 7. Work Performed by Work Unit / Session

> Use this section when the reporting period includes one or more formal Work Units or sessions. It provides a semantic reconstruction that complements the chronological account.

## 7.1 🟧 Work Unit — `WORK-____ — [title]`

### Goal

>

### Formal session

**Session record:**

**Session entry mode:**

**Initiated:**

**Activated:**

**Closed:**

### Major stages completed

1. 
2. 
3. 

### Important WUA sequence

| WUA ID | Timestamp | Event type | Action | Retrospective meaning |
|---|---|---|---|---|
| | | | | |

### Work Unit result

>

### What the Work Unit did not attempt

>

### Why this Work Unit can remain closed

> If later related work occurred after closure, explain why that later work does not reopen or extend the completed Work Unit.

---

<!-- Duplicate for additional Work Units if required. -->

## 7.2 Non-Work-Unit work during the period

> Record meaningful work that occurred outside a formal Work Unit, such as exploratory testing, Registry cleanup, context experiments, small reconciliations, or documentation maintenance. Explain why it was not treated as a new Work Unit.

---

# 8. Decisions, Deviations, Blockers, and Discoveries

## 8.1 🟨 Decisions

### Decision — [title]

**Decision:**

>

**Why the decision was needed:**

>

**Evidence / basis:**

- 
- 

**Alternatives considered:**

- 
- 

**Effect on current work:**

>

**Effect beyond this work period:**

>

**Architecture Changelog effect:** `yes / no / uncertain`

**Related WUA / ACT / source:**

>

---

## 8.2 Deviations from plan

### Deviation — [title]

**Planned:**

>

**Actually happened:**

>

**Why:**

>

**Was chronology reconstructed?** `yes / no`

**Impact:**

>

**Corrective or reconciliatory action:**

>

**Related WUA / ACT / session record:**

>

---

## 8.3 🟥 Blockers and problems

### Problem / blocker — [title]

**Problem:**

>

**How it was discovered:**

>

**Evidence:**

>

**Effect:**

>

**Resolution:**

>

**Residual risk / uncertainty:**

>

---

## 8.4 Discoveries

> Preserve discoveries that changed understanding even when they were not failures.

### Discovery — [title]

**What we discovered:**

>

**Previous assumption:**

>

**New interpretation:**

>

**Why this matters later:**

>

---

# 9. Validation, Testing, and Confidence

> **Rule:** Planned tests belong upstream in the Implementation Plan. This section records what was actually tested and what the results mean retrospectively.

## 9.1 Validation summary

> Give a narrative summary before the table. Explain what confidence the tests justify and what they do not establish.

## 9.2 Executed tests

| Test / validation ID | Purpose | Method | Expected result | Actual result | Status | Evidence | Related WUA |
|---|---|---|---|---|---|---|---|
| | | | | | `pass / fail / partial / not-run` | | |

## 9.3 Corrections triggered by testing

| Finding | Correction | Re-test | Final status |
|---|---|---|---|
| | | | |

## 9.4 Validation gaps

- ⬜ **Not verified:**  
- ⬜ **Partially verified:**  
- ⬜ **Deferred verification:**  

## 9.5 Confidence statement

**Overall confidence:** `high / medium / low / mixed`

**Why:**

>

**Interpretation limits:**

>

---

# 10. Resource, Registry, and Activity Effects

## 10.1 Resource Registry changes

### 🟪 Resources added

| Resource ID | Name | Type | Why it required independent registration |
|---|---|---|---|
| | | | |

### 🟪 Resources changed

| Resource ID | Name | Change | Why material |
|---|---|---|---|
| | | | |

### 🟪 Resources retired / removed from current Registry

| Resource ID | Name | Reason removed | Underlying artifact retained? | Historical ID reused? |
|---|---|---|---|---|
| | | | `yes / no` | `no` |

## 10.2 Important Resource Activities

> Do not reproduce every Activity. Select the entries that help explain material changes.

| ACT ID | Timestamp | Resource ID | Action | Retrospective meaning |
|---|---|---|---|---|
| | | | | |

## 10.3 Registry semantic changes

> Explain changes to how the Registry itself is understood or used.

Examples:

- sparse routing map versus asset catalog;
- authority routing versus physical lookup;
- Resource identity versus document discoverability;
- current-state rows versus append-oriented history;
- interpretation-reference versus location-reference;
- context-naive startup behavior.

## 10.4 Registry cleanup rationale

> If Resources were removed, explain the rule used to decide what remained globally registered.

## 10.5 Activity coverage assessment

**Are all material Resource changes represented in Activities?** `yes / no / partial`

**Known gaps:**

>

---

# 11. Project and System Delta

> **This is one of the most important sections in the Work Update.** Show change explicitly.

## 11.1 High-level before / after

| Area | Starting state | Resulting state | Evidence / authority |
|---|---|---|---|
| Work Unit | | | |
| Project | | | |
| System | | | |
| Documentation | | | |
| Registry | | | |
| Viewer / discovery | | | |
| Context restoration | | | |
| Implementation | | | |

## 11.2 🩵 Project delta — [Project name]

### Before

>

### After

>

### What is now more clearly defined

>

### What remains intentionally unresolved

>

## 11.3 🟦 System delta — [System name]

### Before

>

### After

>

### Capability / documentation distinction

> Distinguish actual implementation changes from documentation/interpretation changes.

## 11.4 🟪 Resource / infrastructure delta

>

## 11.5 Semantic delta

> Explain changes in meaning, authority, ontology, routing, terminology, or architecture—even if no software feature changed.

## 11.6 What did **not** change

> Record important non-changes to prevent later over-reading of the Work Update.

Examples:

- Project ID remained unassigned;
- System ID remained unassigned;
- roadmap intent did not become implementation truth;
- removing a Resource row did not delete the underlying artifact;
- closing one formal session did not automatically close unrelated work.

---

# 12. Architecture and Documentation Effects

## 12.1 Architecture changes

### 🟨 Architecture change — [title]

**Previous model / assumption:**

>

**New model / rule:**

>

**Why the change was made:**

>

**Where authority now lives:**

>

**Architecture Changelog entry:**

>

## 12.2 Templates created or revised

| Template | Previous state | Change | Why it mattered | Status |
|---|---|---|---|---|
| | | | | |

## 12.3 Profiles / schemas created or revised

| Profile / schema | Version | Change | Effect |
|---|---|---|---|
| | | | |

## 12.4 Viewer / discovery architecture changes

>

## 12.5 Documentation authority changes

> Explain any clarification of master documents, sidecars, summaries, roadmaps, implementation plans, session records, work updates, catalogs, or Viewer semantics.

## 12.6 Documentation gaps discovered

- 🟥 **Gap:**  
- 🟥 **Gap:**  
- 🟥 **Gap:**  

## 12.7 Bootstrap-era corrections

> Use this subsection when the work itself exposed missing templates, incomplete process rules, immature schema, or other infrastructure that had to be created while the supposedly downstream work was already underway.

**What was missing:**

>

**When it was discovered:**

>

**How it was corrected:**

>

**How history was reconciled afterward:**

>

**What rule should future work follow:**

>

---

# 13. Context Restoration and Cross-Session Testing

> Use this section when work includes context-naive testing, fresh-window reconstruction, startup validation, handoff testing, or another attempt to determine whether durable records are sufficient without conversational memory.

## 13.1 Test / experiment identity

**Test name / code:**

**Purpose:**

**Fresh-context reader / Other Window:**

**Starting context supplied:**

>

## 13.2 Questions the test was intended to answer

- 
- 
- 

## 13.3 What the fresh reader understood correctly

- 🟩
- 🟩
- 🟩

## 13.4 What the fresh reader missed, confused, or over-assimilated

- 🟥
- 🟥
- 🟥

## 13.5 Time / friction observations

> Record whether orientation was fast, slow, meandering, dependent on luck, overly broad, or appropriately progressive.

## 13.6 Architecture changes caused by the test

| Test finding | Architecture / documentation response | Durable record |
|---|---|---|
| | | |

## 13.7 Test conclusion

> Explain what the test establishes about the current context-restoration architecture and what still needs to be tested.

## 13.8 Next context-restoration test

>

---

# 14. Knowledge Produced

> Work Updates should preserve lessons, not just outputs.

## 14.1 Project-specific lessons

- 
- 
- 

## 14.2 General Klinswork lessons

- 
- 
- 

## 14.3 Recurring problems / patterns

| Problem | Pattern observed | Where observed | Suggested response |
|---|---|---|---|
| | | | |

## 14.4 Rules confirmed

| Rule | Evidence from this work |
|---|---|
| | |

## 14.5 Rules revised

| Previous rule / assumption | Revised rule | Why |
|---|---|---|
| | | |

## 14.6 Knowledge-base / lesson candidates

| Candidate | Why reusable | Suggested destination |
|---|---|---|
| | | |

## 14.7 Important retrospective interpretation

> This is a deliberately generous narrative section. Explain what became clearer only after looking back at the work as a whole.

---

# 15. Resulting State

> This section should describe the actual state at the end of the reporting period, not the desired future state.

## 15.1 Work Unit resulting state

| Work Unit | Status | Readiness | Completed | Result | Authoritative source |
|---|---|---|---|---|---|
| | | | | | |

## 15.2 Project resulting state

>

## 15.3 System resulting state

>

## 15.4 Resource / Registry resulting state

>

## 15.5 Documentation resulting state

>

## 15.6 Viewer / discovery resulting state

>

## 15.7 Context-restoration resulting state

>

## 15.8 Physical repository resulting state

>

## 15.9 Semantic / authority resulting state

>

## 15.10 What is now true that was not true at the beginning?

- 🟩
- 🟩
- 🟩
- 🟩
- 🟩

## 15.11 What remains intentionally unchanged?

- 
- 
- 

---

# 16. Remaining Work and Open Determinations

## 16.1 Remaining work

| Item | Current status | Why remaining | Suggested destination | Candidate Work Unit? |
|---|---|---|---|---|
| | | | | `yes / no / uncertain` |

## 16.2 ⬜ Open determinations

### Open determination — [title]

**Question:**

>

**Why unresolved:**

>

**Evidence already available:**

>

**Evidence still needed:**

>

**Authority that should eventually resolve it:**

>

---

## 16.3 Deferred architecture work

- 
- 
- 

## 16.4 Deferred product / implementation work

- 
- 
- 

## 16.5 Cleanup / reconciliation still required

- 
- 
- 

## 16.6 Items explicitly **not** to reopen

> List completed Work Units, closed sessions, retired decisions, or other finished work that should not be casually reopened merely because future work is related.

---

# 17. Continuation Point

> **Critical rule:** Write this for a context-naive future session. It should be possible to resume without reconstructing the original conversation from scratch.

## 17.1 Recommended first read

1. 
2. 
3. 
4. 

## 17.2 Current authoritative state to expect

>

## 17.3 Recommended next question

>

## 17.4 Recommended next bounded action

>

## 17.5 Dependencies before continuing

- 
- 
- 

## 17.6 Warnings for the next session

- 
- 
- 

## 17.7 Exact handoff statement

> **A future session should resume from this point:**
>
> 

---

# 18. Important Artifacts and References

> Prefer stable IDs and canonical semantic names. Include direct locations where useful, but do not confuse physical location with identity or authority.

## 18.1 Work Units

| Work Unit ID | Title | Role in this update |
|---|---|---|
| | | |

## 18.2 Work Unit Activities

| WUA ID | Event | Why important |
|---|---|---|
| | | |

## 18.3 Resource Activities

| ACT ID | Resource ID | Event | Why important |
|---|---|---|---|
| | | | |

## 18.4 Resources

| Resource ID | Name | Authority / routing role |
|---|---|---|
| | | |

## 18.5 Project / System documents

| Document | Role | Path / URL |
|---|---|---|
| | | |

## 18.6 Implementation plans and session records

| Record | Role | Path |
|---|---|---|
| | | |

## 18.7 Architecture records

| Record | Role | Reference |
|---|---|---|
| | | |

## 18.8 Tests / validation evidence

| Evidence | What it establishes | Reference |
|---|---|---|
| | | |

## 18.9 Repository paths

### 🟨 Important folders

```text
[path]
[path]
```

---

# 19. Provenance and Interpretation Limits

## 19.1 Sources used

- 
- 
- 

## 19.2 Registries consulted

- [ ] Work Units
- [ ] Work Unit Activities
- [ ] Resources
- [ ] Activities
- [ ] Project Registry
- [ ] System Registry
- [ ] Relationship Registry
- [ ] Architecture Changelog
- [ ] Other:

## 19.3 Human-readable records consulted

- 
- 
- 

## 19.4 Current implementation evidence consulted

- 
- 
- 

## 19.5 Reconstruction sources

> Identify sources used to reconstruct chronology or intent where the formal record was created late.

## 19.6 Evidence classes

### Current-state evidence

- 

### Historical evidence

- 

### Planning evidence

- 

### Retrospective interpretation

- 

## 19.7 Interpretation limits

> State what this Work Update cannot establish.

## 19.8 Known evidence gaps

- 
- 
- 

## 19.9 Confidence notes

>

---

# 20. Downstream HTML Projection Notes

> **Purpose:** Give the downstream `work-update.html` generator/editor enough guidance to create a polished human-facing product without forcing the Markdown master to become visually sparse.

## 20.1 HTML reading goal

> What should the human reader understand quickly from the HTML?

## 20.2 Material that may be visually compressed

Examples:

- detailed WUA chronology;
- long Activity tables;
- extensive provenance;
- repeated authority reminders;
- detailed reconstruction notes;
- long test matrices.

## 20.3 Material that should remain prominent

Examples:

- executive narrative;
- major Project/System delta;
- key decisions;
- important problems discovered;
- validation result;
- before/after architecture;
- resulting state;
- what comes next.

## 20.4 Suggested visual treatments

- timeline:
- before/after comparison:
- architecture diagram:
- key decision cards:
- validation badges:
- callout boxes:
- graphics:
- charts:
- QR / links:
- footer:

## 20.5 HTML semantic color mapping

| Semantic role | Markdown marker | HTML treatment suggestion |
|---|---|---|
| Project | 🩵 | cyan label / border / card |
| System / application function | 🟦 | blue label / border / card |
| Folder / repository path | 🟨 | yellow file/folder treatment |
| Resource | 🟪 | purple badge / registry pill |
| Work Unit / execution | 🟧 | orange timeline / work badge |
| Confirmed / passed | 🟩 | green success treatment |
| Problem / failure / blocker | 🟥 | red warning treatment |
| Decision / important determination | 🟨 | amber callout |
| Historical / superseded | ◻️ | gray muted treatment |
| Open determination | ⬜ | neutral outlined treatment |

## 20.6 Information that must **not** be lost in HTML transformation

- 
- 
- 

---

# 21. Work Update Completion Check

## 21.1 Narrative completeness

- [ ] A future reader can understand why the work existed.
- [ ] The starting state is clear.
- [ ] Intended work is summarized.
- [ ] Actual work chronology is sufficiently detailed.
- [ ] Important decisions are explained.
- [ ] Deviations and reconstruction are explicit.
- [ ] Problems and discoveries are preserved.
- [ ] Validation and confidence are explained.
- [ ] Resource / Registry consequences are recorded.
- [ ] Project/System delta is explicit.
- [ ] Resulting state is detailed.
- [ ] Remaining work is separated from completed work.
- [ ] Continuation guidance is usable by a context-naive session.

## 21.2 Authority integrity

- [ ] Work Unit current state is not inferred when Registry state is available.
- [ ] WUA history is not replaced by this narrative.
- [ ] Activities remain Resource-history authority.
- [ ] Implementation Plan remains intended-work authority.
- [ ] Formal session record remains detailed execution authority.
- [ ] System Summary remains current System authority.
- [ ] Roadmap remains future-state authority.
- [ ] Current implementation truth is not inferred from planning documents.
- [ ] No unsupported durable IDs were invented.

## 21.3 Temporal integrity

- [ ] Planning boundaries are truthful.
- [ ] Reconstructed work is identified.
- [ ] Pre-plan work is not described as prospectively planned.
- [ ] Closed Work Units are not silently extended.
- [ ] Historical terminology remains recognizable as historical.

## 21.4 Detail quality

- [ ] The document is not artificially shortened for skimmability.
- [ ] Important causal relationships are explained.
- [ ] Important IDs are accompanied by semantic descriptions.
- [ ] Selective redundancy improves reconstruction.
- [ ] Large tables are interpreted in prose rather than left unexplained.
- [ ] The Work Update can stand alone long enough to orient a future session.

## 21.5 Downstream readiness

- [ ] Master Markdown is complete enough to generate the sidecar.
- [ ] Master Markdown is complete enough to generate the HTML.
- [ ] HTML projection notes identify appropriate visual emphasis.
- [ ] No substantive claim exists only in a downstream product.

---

# Appendix A — Visual and Editorial Grammar

## A.1 Semantic visual vocabulary

> These markers form a redundant semantic layer. The text label must remain meaningful when emoji/color styling is stripped.

| Role | Marker | Intended color | Meaning |
|---|---|---|---|
| Project | 🩵 | cyan | durable Project / operational undertaking |
| System / application function | 🟦 | blue | System or functional implementation context |
| Folder / repository path | 🟨 | yellow | physical repository/file-system location |
| Resource | 🟪 | purple | registered Resource / resolvable operational object |
| Work Unit / execution | 🟧 | orange | bounded work, session, stage, execution event |
| Confirmed / passed | 🟩 | green | validated, completed, confirmed |
| Problem / failure / blocker | 🟥 | red | error, blocker, failed assumption, unresolved defect |
| Decision / important determination | 🟨 | amber | deliberate architecture or execution choice |
| Historical / superseded | ◻️ | gray | historical state, legacy term, retired route |
| Open determination | ⬜ | neutral | unresolved question requiring later authority/evidence |

## A.2 Example semantic labels

```markdown
🩵 **Project:** Task Assignment and Tracking

🟦 **System:** Work Queue

🟨 **Path:** `projects/operations/Task Assignment and Tracking/systems/Work Queue/`

🟪 **Resource:** `RES-003 — Work Queue app datastore`

🟧 **Work Unit:** `WORK-0001 — Task Assignment and Tracking — Initial Project Definition`

🟩 **Confirmed:** Viewer companion resolution passed.

🟥 **Problem discovered:** Serialized spreadsheet inspection returned a value not present in the literal cells.

🟨 **Decision:** Preserve the technical manual as a discoverable System document rather than requiring top-level Resource identity.

⬜ **Open determination:** Permanent System identity remains unassigned.
```

## A.3 Identifier formatting

Durable or quasi-durable identifiers should be formatted as code:

```text
WORK-0001
WUA-0008
ACT-0091
RES-043
PROJ-###
SYS-###
```

When first introduced, pair the identifier with semantic meaning.

Preferred:

```text
ACT-0091 — Registry context-routing layer added
```

Avoid:

```text
ACT-0091 happened and then ACT-0092.
```

unless the semantic meaning is already clear from immediately preceding context.

## A.4 Heading style

Prefer descriptive headings:

```markdown
### 11:45 — 🟨 Registry routing architecture changed after context-naive testing
```

over:

```markdown
### Update
```

## A.5 Callout grammar

### Confirmed

```markdown
> **🟩 Confirmed**
> [Validated fact and evidence.]
```

### Decision

```markdown
> **🟨 Decision**
> [Decision, reason, and consequence.]
```

### Problem

```markdown
> **🟥 Problem discovered**
> [Problem, evidence, correction, residual risk.]
```

### Work Unit consequence

```markdown
> **🟧 Work Unit consequence**
> [How the event affected Work Unit status, readiness, scope, validation, or closure.]
```

### Open determination

```markdown
> **⬜ Open determination**
> [Question, why unresolved, and what evidence/authority is required.]
```

### Historical note

```markdown
> **◻️ Historical note**
> [Past terminology/state that should not be mistaken for current truth.]
```

## A.6 Table usage

Use tables for:

- before/after comparison;
- timelines;
- WUA / ACT indexes;
- test results;
- Resource changes;
- authority maps;
- remaining work;
- artifact references.

Do not let tables replace explanatory prose when meaning requires interpretation.

## A.7 Prose density

Long paragraphs are acceptable when they preserve a coherent causal argument.

Prefer:

- substantial paragraphs for explanation;
- bullets for enumerated facts;
- tables for structured comparison;
- code blocks for hierarchy, routing, or exact state;
- callouts for high-value semantic emphasis.

Avoid reducing every thought to a one-line bullet.

## A.8 Repetition

Intentional repetition is permitted when it serves different retrieval paths.

Example:

- chronology explains **when** a Registry rule changed;
- architecture section explains **what the rule means**;
- resulting-state section explains **what is now true**;
- continuation section explains **how a future session should act on it**.

This is not wasteful duplication when each occurrence has a distinct narrative role.

---

# Appendix B — Authority Separation

```text
WORK UNIT REGISTRY
    current bounded-work state
            │
            ├───────────────┐
            │               │
            ▼               ▼
WORK UNIT ACTIVITIES   IMPLEMENTATION PLAN
    material history      intended work
            │               │
            └───────┬───────┘
                    ▼
        WORK IMPLEMENTATION SESSION
            detailed execution
                    │
                    ├───────────────┐
                    │               │
                    ▼               ▼
            RESOURCE ACTIVITIES   TEST / EXECUTION EVIDENCE
            resource history      validation / current behavior
                    │               │
                    └───────┬───────┘
                            ▼
                 WORK UPDATE SUMMARY.MD
                 canonical retrospective master
                 chronology + delta + meaning
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
       WORK UPDATE SIDECAR.JSON   WORK UPDATE.HTML
       structured companion       human presentation
```

The Work Update Summary may cite and interpret all of these records.

It must not silently absorb their authority.

---

# Appendix C — Minimum Viable Work Update

> This template is intentionally detailed, but a smaller work period does not need every section at full length.

At minimum, a trustworthy Work Update should preserve:

```text
Update identity
Reporting boundary
Executive summary
Starting state
Intended work
Actual chronology
Important Work Unit / Activity evidence
Decisions / deviations / discoveries
Validation
Resource / Registry effects
Project/System delta
Resulting state
Remaining work
Continuation point
Important references
Provenance / interpretation limits
```

For a substantial architecture or implementation day, the fuller template should be used.

The minimum viable version must still satisfy the core test:

> **Could a future context-naive session reconstruct what happened and why without relying on memory of the original conversation?**

---

# Appendix D — Template Design Rules

1. **The Work Update Summary Markdown is the canonical human-readable master.**
2. **The Work Update sidecar is a structured companion, not narrative authority.**
3. **The Work Update HTML is a downstream human-facing presentation product.**
4. **Prefer useful completeness over brevity.**
5. **Do not optimize the Markdown for skimming at the expense of reconstruction.**
6. **Include a Table of Contents in substantial Work Updates.**
7. **Use semantic visual markers consistently.**
8. **Never rely on color alone to convey meaning.**
9. **Preserve Project, System, Resource, Work Unit, path, deployment, and implementation distinctions.**
10. **Explain identifiers when first introduced.**
11. **Use the Work Unit Registry for current Work Unit state.**
12. **Use Work Unit Activities for timestamped material Work Unit history.**
13. **Use Activities for timestamped material Resource history.**
14. **Use the Implementation Plan for intended work.**
15. **Use the Work Implementation Session for detailed formal execution.**
16. **Use current source/data/deployment/tests for current implementation truth.**
17. **Use the Work Update for retrospective synthesis, delta, meaning, and continuation.**
18. **Preserve starting state and resulting state in substantial detail.**
19. **Explain causal relationships, not just file changes.**
20. **Preserve false starts, discoveries, and corrected assumptions when they matter to understanding.**
21. **Preserve reconstructed chronology explicitly.**
22. **Never rewrite pre-plan work as prospectively planned.**
23. **Closed Work Units remain closed unless their authority explicitly changes.**
24. **Do not invent durable IDs.**
25. **Selective redundancy is acceptable when it improves future reconstruction.**
26. **Large tables should be interpreted in prose when meaning is not self-evident.**
27. **Distinguish documentation changes from implementation changes.**
28. **Distinguish semantic/architecture changes from physical repository changes.**
29. **Record what did not change when that prevents later over-interpretation.**
30. **Record evidence gaps and interpretation limits.**
31. **A Work Update should preserve enough source references that claims can be traced later.**
32. **Context-restoration tests should record what the fresh reader understood and misunderstood.**
33. **Testing-induced architecture changes should be tied to the test finding that caused them.**
34. **The Work Update should preserve lessons and reusable rules, not just outputs.**
35. **The continuation point must be usable by a context-naive future session.**
36. **The downstream HTML may be shorter, more visual, and more editorially structured than the Markdown master.**
37. **No substantive claim should exist only in the HTML if it belongs in the durable retrospective record.**
38. **The Markdown may contain more technical and provenance detail than the HTML.**
39. **The master document should be long when the work was complex; length alone is not a defect.**
40. **The governing quality test is reconstruction: can the future reader understand what happened, why it happened, what changed, and what to do next?**

---

# Appendix E — Suggested Front-Matter Vocabulary

```yaml
record_type: work-update-summary
record_family: human-readable-retrospective-master

status:
  - draft
  - reviewed
  - final

authority_role:
  - canonical-human-readable-retrospective-master-for-one-work-update

reconstruction_mode:
  - none
  - reconstructed-during-work
  - reconstructed-after-work
  - mixed
```

Do not invent identifiers merely to fill metadata.

---

# Appendix F — Revision Notes

## 1.0-draft — 2026-08-16

Initial Work Update Summary master template.

Established:

- Markdown master / sidecar / HTML downstream authority separation;
- long-form reconstruction as the primary design objective;
- future-AI-context restoration as a first-class reader requirement;
- human-facing HTML as the primary downstream reading product;
- explicit starting-state and resulting-state structure;
- Work Unit / WUA / Resource / Activity synthesis;
- implementation-plan and Work Implementation Session relationship;
- detailed chronology and retrospective interpretation;
- reconstruction / temporal-honesty rules;
- Project/System/Resource delta sections;
- architecture/documentation-effects section;
- context-restoration / cross-session testing section;
- knowledge-produced section;
- continuation-point requirements;
- provenance and interpretation-limit requirements;
- HTML projection guidance;
- semantic visual/color grammar with redundant textual meaning;
- Table of Contents requirement;
- selective-redundancy rule;
- detail-over-brevity rule;
- no-substantive-claim-only-downstream rule.
