# PST-SP / Clinical Handout Systems Investigation
## Working Summary — August 8, 2026

### Status
We are deliberately stopping the source hunt for now.

The investigation has **not yet recovered enough material to reproduce the VA PST-SP handout system faithfully**, but it has produced a much clearer model of the problem, identified several real source families, exposed important provenance and workflow questions, and clarified what a useful future prototype would actually need to demonstrate.

This document records what we were trying to do, why we were trying to do it, what we learned, what remains hidden, and where the strongest leads are.

---

# 1. Why We Started

The immediate practical goal was to make better use of therapy handouts and clinical teaching materials that already exist.

The larger idea developed into this:

> A clinician should be able to select, rearrange, substitute, repeat, and assemble handout components according to the immediate needs of a patient without having to rebuild documents manually or hunt through unrelated PDFs.

The goal is **not** to have software make clinical decisions. The clinician remains responsible for deciding what material is appropriate.

The software would instead make the existing material easier to understand, retrieve, compare, organize, and assemble.

A simple example:

```text
Source materials
    ↓
Reusable components / handouts
    ↓
Clinician selects components
    ↓
Assembly manifest
    ↓
Patient packet / PDF / portal view / printout
```

The original idea seemed simple: collect PDFs, divide them into useful pieces, describe those pieces with JSON sidecars, and build a viewer/composer.

The investigation showed that the real problem is substantially deeper.

---

# 2. Why This Matters Personally and Clinically

This project grew partly out of a recent failure in the care/communication system.

A scheduled therapy-related interaction became inaccessible because a meeting notification did not contain the meeting link. During the effort to resolve the problem, several different people and processes became involved.

One especially important lesson was that a seemingly small technical failure can become clinically significant when the patient is already under severe stress.

The issue was not merely:

> “A link was missing.”

The actual chain was closer to:

```text
scheduled care
    ↓
notification
    ↓
missing access information
    ↓
patient cannot enter scheduled care
    ↓
patient seeks help
    ↓
people must identify which meeting/process is being discussed
    ↓
communication failures amplify the original problem
```

The later conversation with the therapist established that the missing link was not necessarily an uncontrollable external technical fault. The therapist ultimately indicated that she had failed to include the link in the notification.

That made the technical details relevant.

It also revealed a broader systems issue: the notification apparently did not contain enough durable context to make recovery easy.

A more resilient notification might include:

- meeting title or purpose;
- persistent meeting or appointment ID;
- join link;
- fallback phone number;
- instructions for reporting a failure;
- enough context that another staff member can identify the exact appointment.

The important systems lesson is:

> A patient should not have to reconstruct institutional context verbally while already distressed.

This experience is one reason the document/tool project matters. Small organizational and communication improvements can have disproportionate value when the user of the system has very little emotional or practical reserve.

---

# 3. The Original Document Problem

We began with a basic observation:

A folder containing several documents does **not** mean those documents form a meaningful collection.

A directory may contain:

- a treatment workbook;
- a lesson;
- a work update;
- a worksheet;
- a clinical measure;
- a reference manual.

Their co-location is a storage fact, not necessarily a semantic relationship.

That led to several important distinctions.

## Storage container
A directory or folder.

It says:

> These files are stored together.

It does **not** say:

> These files belong together conceptually.

## Corpus / inventory
Everything currently under consideration.

A corpus can contain unrelated objects.

## Collection
A set of objects intentionally related to one another.

## Series
A collection with sequence or continuity.

## Category / facet
Items grouped because they share a characteristic.

This does not necessarily imply that the items belong together as a publication or treatment packet.

## Standalone item
An object for which no collection relationship has been established.

---

# 4. The Most Important Conceptual Breakthrough

We learned that at least five separate concepts must remain distinct:

1. **Source work**
2. **Component**
3. **Rendition / adaptation / variant**
4. **Collection or treatment-role membership**
5. **Assembly**

A simplified model:

```text
Source Work
    ↓
Source Component
    ↓
Rendition / Adaptation / Variant
    ↓
Relationships and clinical role
    ↓
Assembly
    ↓
Rendered patient document
```

This is much more accurate than treating every PDF page as a unique independent handout.

---

# 5. Content, Metadata, Relationships, Assembly, Rendering

A particularly useful distinction became:

## Content
What the component says.

## Metadata
What the component is.

Examples:

- title;
- author;
- publication;
- year;
- program;
- source file;
- page range;
- handout number;
- orientation.

## Relationships
How the component relates to other objects.

Examples:

- derived from;
- adapted from;
- variant of;
- replaces;
- belongs to toolkit;
- optional alternative to;
- Veteran version of;
- example of.

## Assembly
Which components were selected for a specific packet and in what order.

## Rendering
How the assembly becomes something visible or printable:

- HTML;
- PDF;
- print;
- portal view;
- email attachment.

This separation may ultimately be more important than any code we have written.

---

# 6. A Crucial Provenance Distinction: Component vs. Page Rendition

The same underlying teaching content can appear in several forms.

For example:

```text
Original publisher component
      ↓
later edition
      ↓
VA adaptation
      ↓
Veteran version
      ↓
locally numbered handout
      ↓
appearance inside a specific patient packet
```

Therefore a future sidecar should distinguish at least:

- `origin_source`
- `container_source`

A VA handout may be physically contained in a VA packet while its underlying concept, text, diagram, or figure originated in another publication.

This matters because the same content can be re-typeset, re-numbered, re-colored, or re-captioned without becoming conceptually unrelated.

---

# 7. What the CPT Material Taught Us

The uploaded **CPT Workbook** became our clearest example of downstream document assembly.

Most of its pages identify the source as:

**Cognitive Processing Therapy for PTSD: A Comprehensive Therapist Manual, Second Edition**  
Patricia A. Resick, Candice M. Monson, Kathleen M. Chard  
Guilford Press, 2024.

Important observations:

- Guilford exposes a current reproducible-material library for the 2024 edition.
- Guilford advertises **48 reproducible handouts/forms** associated with the current manual.
- The patient workbook we received is **not simply the complete 48-item publisher library**.
- The particular downstream workbook uses a smaller selected inventory and repeats certain worksheets.
- Session-assignment pages function almost like **human-readable assembly manifests**.
- The workbook contains at least one older-generation component, showing that downstream packets can mix editions.

This gives us a concrete architecture:

```text
Therapist manual / protocol
        ↓
publisher reproducible component library
        ↓
selected and sometimes repeated components
        ↓
patient workbook
```

That model is likely highly relevant to other therapy programs.

---

# 8. What We Learned About PST / Nezu

A major breakthrough was locating the older Problem-Solving Therapy lineage.

The central upstream source family includes work by:

- Arthur M. Nezu
- Christine Maguth Nezu
- Thomas J. D'Zurilla

The older Springer PST materials contain the conceptual structure of **four problem-solving toolkits**.

This is important because we originally wondered whether the VA had invented the “toolkit” structure.

It did not.

The toolkit concept is upstream Nezu terminology.

The four toolkits address broad obstacles such as:

- emotional dysregulation / distress;
- cognitive overload;
- hopelessness or lack of motivation;
- planful problem solving.

Several titles in the VA PST-SP paper packet have exact or close ancestors in this older PST material.

Examples include material corresponding to:

- **Getting from “A” to “B”: Obstacles to Effective Problem Solving**
- **Go on a Vacation in Your Mind: Visualize to Reduce Stress**
- **Problem Map: What Makes This a Problem?**

This strongly suggests that the VA PST-SP packet is not an entirely new handout universe. It appears to inherit, adapt, rename, or reorganize substantial portions of earlier PST material.

---

# 9. Emotion-Centered PST

Another important source family is:

**Emotion-Centered Problem-Solving Therapy**  
Arthur M. Nezu and Christine Maguth Nezu  
2019.

This appears to represent a later evolution of the PST framework.

It includes a client workbook and treatment manual and preserves the four-toolkit architecture in updated form.

VA literature describes PST-SP as adapted from the Nezu/Nezu emotion-centered PST framework.

This gives us a possible historical chain:

```text
Nezu / Nezu / D'Zurilla PST
        ↓
later Emotion-Centered PST
        ↓
VA adaptation for suicide prevention
        ↓
PST-SP for Veterans
```

The exact document lineage still requires confirmation component by component.

---

# 10. What We Reconstructed from the PST-SP Paper Packet

The paper packet appears to have a deliberate modular architecture.

## Introduction and Rationale
Handouts 1–7

Known titles include:

1. What is Problem-Solving Therapy?
2. Problem-Solving Model of Stress
3. “Stress”
4. Getting from “A” to “B”: Obstacles to Effective Problem Solving
5. Obstacles to Successful Problem Solving & Tools to Overcome the Obstacles
6. Problem-Solving Beliefs and Styles
7. Problem List

## Toolkit: Stop and Slow Down
Handouts 8–16

Includes:

- Stop and Slow Down vs. Safety Planning
- Personal Triggers Worksheet
- Slow Down Strategies
- Go on a Vacation in Your Mind: Visualize to Reduce Stress
- Deep Breathing
- “Fake” Yawning
- Mindful Meditation
- Deep Muscle Relaxation
- Mindful Walking: Taking a “Wabi Sabi” Walk

## Toolkit: Visualization for Hope and Motivation
Handouts 17.1–17.2

Includes:

- Visualize the End of the Race
- Visualization for Hope and Motivation

## Toolkit: Overcoming Brain Overload
Handouts 18–21

The photographed divider/index page for this section has not yet been fully reconstructed from the current paper review.

## Toolkit: Planful Problem Solving
Handouts 22–25

Includes:

- Problem-Solving Steps
- Problem Map: What Makes This a Problem?
- What is the “Real” Problem?
- Problem-Solving Worksheet — **Veteran version**

Four blank copies of the Problem-Solving Worksheet are reportedly included for convenience.

## Review and Future Forecasting
Handouts 26–28

Includes:

- When and How to Check Problem Solving Beliefs
- Future Forecasting
- Suicide Risk Curve

The packet therefore appears to have:

```text
Introduction
    +
Four obstacle-specific toolkits
    +
Review / maintenance / future forecasting
```

The exact relationship between “Review and Future Forecasting” and the four-toolkit structure still needs to be represented carefully because its own divider language also refers to a toolkit.

---

# 11. PST-SP Versioning Clues

The paper packet contains several important clues:

- **Revised 10/4/2023 “JFG”**
- **Version 2**
- **Veteran version**
- local labels such as **HANDOUT 26**
- mixed portrait and landscape pages
- clean, digitally produced artwork and layouts
- section-divider/index pages without the ordinary handout footer

These strongly suggest a digitally produced master document or document family.

The clean artwork does **not** look like material repeatedly scanned from paper.

---

# 12. The “JFG” Lead

A strong but still unproven hypothesis is that **JFG** may refer to **Jennifer F. George**.

Jennifer F. George appears as a coauthor on recent VA PST-SP outcomes work and is affiliated with the VHA Office of Mental Health in Washington, D.C.

Her role in that work includes conceptualization, supervision, and review/editing.

This makes the initials plausible.

However:

> We do not yet have a document-control record proving that the “JFG” revision notation refers to Jennifer F. George.

This should remain labeled **high-confidence hypothesis**, not confirmed fact.

---

# 13. Formal VA PST-SP Manual Leads

We found bibliographic evidence for a national VA PST-SP manual family.

A 2023 publication cites:

**Problem-Solving Therapy for Suicide Prevention for Veterans: Clinician’s Manual**  
VA Central Office / U.S. Department of Veterans Affairs, Mental Health and Suicide Prevention Services  
Washington, D.C.  
2021.

A newer VA implementation source appears to cite a later **Provider Manual**, around 2023.

Names associated with the manual/program include:

- Sherry A. Beaudreau
- Gregory K. Brown
- Angelic Chaison
- Kelly L. Green
- Shannon Sisco
- Viviana Padilla-Martinez
- Kathleen Rekart
- Julie Wetherell
- Jennifer F. George

These names are valuable search fingerprints.

What we **do not have** is the actual public PDF of the clinician/provider manual.

---

# 14. VA PST-SP Training Infrastructure

Public VA and academic sources indicate that PST-SP is a national manualized VA treatment program.

The training infrastructure has included:

- independent learning;
- live workshop/didactic instruction;
- role-play;
- extended consultation;
- competency review.

Public sources also indicate that some implementation/training resources have lived inside VA systems such as internal training portals, SharePoint, and TMS.

This may explain why the provider manual and exact handout master are difficult to recover through ordinary public web searches.

---

# 15. Suicide Risk Curve: Evidence of Cross-Program Reuse

PST-SP Handout 28 is **Suicide Risk Curve**.

A public VA Safety Planning Intervention Manual contains a Suicide Risk Curve figure.

A public CBT-SP Veterans Workbook also uses a suicide-risk-curve exercise and credits VA Safety Planning Intervention material.

This is strong evidence that the PST-SP packet may incorporate content from **multiple VA clinical source families**, not only Nezu PST.

That means the packet may be an assembly of:

```text
Nezu PST-derived material
        +
VA PST-SP-specific adaptations
        +
VA suicide-prevention material
        +
possibly other sources
```

This is exactly the kind of provenance problem our proposed system should represent explicitly.

---

# 16. Therapist Aid

We discovered that some files in the old online PST directory are copyrighted by **Therapist Aid LLC**.

Therapist Aid is a commercial/professional clinical resource library.

It provides items such as:

- worksheets;
- handouts;
- articles;
- interactive tools;
- customizable resources;
- printable/fillable materials.

This explains why some documents in the old directory may be almost word-for-word related to older PST concepts while having different graphics or layouts.

They may be **third-party redesigns**, not alternate publisher editions.

Therapist Aid is therefore useful as a comparison model:

```text
Therapist Aid
= polished user-facing clinical resource library
```

Our current project is different:

```text
Our prototype
= provenance-aware component and assembly framework
```

Therapist Aid is much more user-friendly.

Our current system assumes the operator understands folders, files, sidecars, manifests, and source organization.

That is acceptable for a research/demo prototype.

---

# 17. The Old “Problem Solving Therapy and SMART” Directory

The directory at:

`dreichenbaumcbtsheets.com/Problem Solving Therapy and SMART/`

appears to be a personal or informal archive rather than an authoritative publication system.

Its value is archaeological.

It may preserve:

- old versions;
- local adaptations;
- Therapist Aid versions;
- extracted pages;
- renamed files;
- historical copies no longer easily available elsewhere.

It should be treated as:

> a specimen cabinet, not a source authority.

Its filenames, dates, and organization cannot automatically be trusted as canonical metadata.

Nevertheless, it may be extremely useful for identifying document ancestry.

---

# 18. Graphics as Provenance Evidence

The diagrams in the textbook/source materials often appear vector-native.

Visual clues include:

- clean geometric edges;
- muted palettes;
- flat fills;
- slightly awkward alignment;
- unusual connector geometry;
- tiny line extensions near arrows;
- simple diagrammatic construction.

These “imperfections” may function as provenance fingerprints.

If the same unusual geometry appears in two different documents, that can be stronger evidence of direct asset reuse than general visual similarity.

Future forensic comparison could examine:

- arrow geometry;
- box proportions;
- connector bends;
- relative spacing;
- fonts;
- label placement;
- exact colors;
- object alignment;
- whether text was re-typeset;
- whether vector objects remain editable in the PDF.

---

# 19. The Missing Middle

Our biggest unresolved problem is the hidden middle of the production chain.

We currently have something like:

```text
Publisher / original clinical sources
        ↓
        ???
        ↓
VA PST-SP national materials
        ↓
        ???
        ↓
local clinician
        ↓
paper packet given to patient
```

The unknown layers could include:

- national VA training package;
- provider manual appendices;
- internal SharePoint library;
- TMS download;
- Word document;
- Acrobat master packet;
- separate handout PDFs;
- locally maintained document set;
- regional materials;
- clinic-specific packet;
- actual packet-composer software.

At present we do **not** have evidence that clinicians are using a sophisticated packet-building application.

A simpler explanation remains quite plausible:

> program developers created a master handout PDF or document set, and clinicians print or distribute selections from it.

---

# 20. Federal VA vs. State Veterans Agencies

This organizational distinction became important.

The **U.S. Department of Veterans Affairs** is federal.

The VA health-care system in New Mexico is therefore part of the federal VA/VHA structure.

Separately, New Mexico has a **New Mexico Department of Veterans’ Services**.

That state agency is not the New Mexico branch of the federal Department of Veterans Affairs.

The distinction is analogous to:

```text
New Mexico Department of Health
≠
U.S. Department of Health and Human Services
```

Likewise:

```text
New Mexico Department of Veterans’ Services
≠
U.S. Department of Veterans Affairs
```

Therefore the likely PST-SP production/distribution chain is federal rather than state:

```text
VA Central Office / VHA national program
        ↓
national training infrastructure
        ↓
regional / health-care-system implementation
        ↓
local clinic
        ↓
clinician
```

Local modifications may occur anywhere below the national level.

---

# 21. What We Have Successfully Established

## Confirmed or strongly supported

- Clinical handout systems are inherently modular even when the software does not represent them that way.
- Source documents, components, variants, collections, and assemblies are different objects.
- CPT provides a concrete example of a source-library-to-patient-workbook assembly process.
- Guilford currently exposes a large reproducible component set for CPT.
- Downstream workbooks may select, repeat, and mix components.
- The four-toolkit PST architecture originates upstream in Nezu PST.
- Several PST-SP handout concepts/titles have strong ancestry in earlier Nezu materials.
- PST-SP is a national VA manualized treatment program.
- Formal PST-SP clinician/provider manuals exist or existed.
- Some PST-SP material appears to incorporate other VA suicide-prevention content.
- Therapist Aid is a separate professional clinical-resource publisher/service.
- The Reichenbaum directory is useful as an archive but not an authoritative source.
- The PST-SP paper packet appears born-digital rather than scan-derived.
- The packet has local versioning, numbering, and Veteran-specific indicators.

---

# 22. What We Have NOT Been Able to Establish

We still do not have:

- the actual digital PST-SP Veteran handout master;
- the actual PST-SP clinician/provider manual PDF;
- a complete component-by-component provenance map;
- the exact source edition for every inherited graphic;
- proof of who “JFG” is;
- proof of how the therapist assembled the packet;
- proof that a packet-composer application exists;
- proof that the packet came directly from Washington rather than through a regional/local transformation;
- complete knowledge of internal VA training/document distribution systems;
- all source files needed to reconstruct the packet exactly.

This is the critical limitation.

---

# 23. Why the Missing Materials Matter

Without the actual component files, we cannot faithfully build the final system we originally imagined.

A component assembler requires components.

We could build the software framework now, but if the source universe is incomplete the result would demonstrate architecture rather than reproduce the real VA system.

That distinction matters.

## Project A — exact reconstruction

Goal:

> Reconstruct the existing VA PST-SP document ecosystem, its component library, and its actual assembly workflows.

**Status: blocked by missing material.**

## Project B — architectural demonstration

Goal:

> Demonstrate how clinical handout material could be represented, related, documented, and assembled using authentic examples that we can legally and practically recover.

**Status: not blocked.**

---

# 24. The Proposed System

A future framework could look like this:

```text
sources/
    cpt/
    pst-sp/
    safety-planning/
    emdr/
    pe/
    wet/
    pct/
    measures/

fragments/
    ...

sidecars/
    ...

assemblies/
    ...
```

The source files would be preserved unchanged.

Logical components could either be:

1. physically extracted fragment PDFs; or
2. virtual fragments defined by source file + page range.

A fragment might contain metadata such as:

```json
{
  "id": "pst-sp-h23",
  "title": "Problem Map: What Makes This a Problem?",
  "program": "PST-SP",
  "type": "worksheet",
  "source_work": "...",
  "source_file": "...",
  "source_pages": [23],
  "container_source": "...",
  "origin_source": "...",
  "variant": "...",
  "relationships": [
    "belongs-to:planful-problem-solving",
    "derived-from:..."
  ]
}
```

An assembly would then contain references to components rather than copies of their meaning.

Example:

```text
assembly:
    component A
    component B
    component C
    component C
    component C
    component C
    optional component D
```

The same component can participate in zero, one, or many assemblies without changing identity.

---

# 25. Why Documentation Matters More Than the Code

A major philosophical conclusion emerged today:

> The code is not precious.

The current apps are prototypes and research instruments.

Their job is to prove that the relationships can be represented and that the workflow can function.

A professional software team could reasonably discard almost all of our implementation and replace it with:

- databases;
- APIs;
- enterprise authentication;
- object storage;
- document services;
- polished clinical UI;
- permissions;
- licensing controls;
- accessibility;
- audit logs;
- EHR integration.

That would not invalidate the project.

It would mean the demonstration succeeded.

The durable contribution is:

- domain model;
- relationship model;
- provenance model;
- component identity rules;
- assembly model;
- edge cases;
- workflow documentation;
- examples;
- lessons learned.

A good test is:

> Could a competent engineering team delete the application and rebuild a better one from the documentation without having to rediscover the conceptual model?

If yes, the project has value even if the prototype code is spaghetti.

---

# 26. The Songwriting Analogy

A useful description of our role became:

> We are songwriting.

We are not pretending to be:

- the singer;
- the instrumentalists;
- the recording engineer;
- the producer;
- an enterprise VA development team.

We are making the demo and writing down the arrangement.

A professional team may later say:

> “Yes, that idea works. Here is how you would actually build it.”

That is a successful outcome.

The project therefore functions partly as **constructive criticism through demonstration**.

Instead of saying:

> “Your system is bad.”

we can say:

> “Here is a documented working model showing that these relationships can be represented and these workflows can be improved.”

---

# 27. Why Clinician Empowerment Still Matters

The clinician-facing goal remains valuable.

A good future system could allow a clinician to:

- browse source materials;
- see provenance;
- compare variants;
- select a handout;
- substitute another version;
- repeat worksheets;
- reorder components;
- create a patient-specific packet;
- preserve the assembly as a manifest;
- regenerate it later;
- share it as PDF, print, or portal content.

Crucially:

> The software should support clinical judgment, not replace it.

---

# 28. Main Obstacles

## 1. Hidden internal material
Important VA manuals and training assets may live behind internal systems.

## 2. Dead or moved public links
Older Springer and VA references sometimes point to resources that have moved or disappeared.

## 3. Unclear version lineage
A visually similar handout may represent:

- a different edition;
- a local redesign;
- a VA adaptation;
- a third-party redesign;
- a re-typeset copy.

## 4. Unknown clinician workflow
We do not know whether clinicians use:

- a master PDF;
- individual files;
- Word;
- Acrobat;
- an internal portal;
- an application;
- some combination.

## 5. Mixed provenance
A single patient packet can contain material from several conceptual and publication families.

## 6. Licensing and copyright
Material may be usable clinically without being freely redistributable as a public component library.

## 7. Local vs. national modifications
Even if a national source is recovered, a local packet may not be identical.

---

# 29. Strongest Leads for a Future Session

Rather than continuing broad searching, future work should be narrow and evidence-driven.

## Lead A — PST-SP clinician/provider manual

Search fingerprints:

- `"Problem-Solving Therapy for Suicide Prevention for Veterans" "Clinician's Manual"`
- `"Problem-Solving Therapy for Suicide Prevention for Veterans" "Provider Manual"`
- Sherry Beaudreau
- Gregory Brown
- Angelic Chaison
- Kelly Green
- Shannon Sisco
- Viviana Padilla-Martinez
- Jennifer F. George

## Lead B — exact distinctive handout titles

High-value search fingerprints include:

- `"Visualize the End of the Race"`
- `"When and How to Check Problem Solving Beliefs"`
- `"Stop and Slow Down vs. Safety Planning"`
- `"Problem Map: What Makes This a Problem?"`
- `"Problem-Solving Worksheet" "Veteran version"`

These are more useful than generic searches for “problem solving therapy worksheets.”

## Lead C — archived Springer PST supplement

The former Springer PST supplement is valuable for establishing older component ancestry.

Historical source title:

**Instructional Materials and Patient Handouts Provided to Supplement Problem-Solving Therapy: A Treatment Manual**

## Lead D — VA MIRECC / training infrastructure

Look for:

- archived training pages;
- appendices;
- webinar materials;
- downloadable provider resources;
- references to internal package names.

## Lead E — forensic comparison of exact PDFs

If we recover candidate PDFs, compare:

- metadata;
- Creator / Producer;
- fonts;
- vector objects;
- page geometry;
- graphics;
- footer construction;
- embedded images;
- revision dates.

---

# 30. Recommended Next Artifact

If we return to this project, the next useful artifact should probably **not** be another application.

It should be a **PST-SP Recovery / Provenance Matrix**.

Example columns:

| Component | Downstream copy possessed | Exact upstream source recovered | Probable source family | Exact rendition match | Confidence | Notes |
|---|---|---|---|---|---|---|
| H4 | Yes | Partial | Nezu PST | Unknown | High | title/structure match |
| H11 | Yes | Yes/possible | Nezu PST | Unknown | High | exact title |
| H23 | Yes | Yes/possible | Nezu PST | Unknown | High | exact title |
| H28 | Yes | Yes/related | VA Safety Planning | Unknown | High | cross-program curve |

Once every component is represented, we can measure the actual problem instead of feeling surrounded by unknowns.

For example:

```text
28 logical handouts
19 source families identified
12 exact source files recovered
5 probable ancestors
7 still unknown
```

Those numbers are only illustrative.

The point is to convert uncertainty into a visible inventory.

---

# 31. Decision at the End of Today’s Investigation

Continuing to search broadly risks becoming unproductive.

We learned enough today to justify stopping.

The important result is not that we found the missing master PDF.

We did not.

The important result is that we now understand **why finding it matters, what it would prove, what its absence prevents, and what a future system would have to represent**.

The project is therefore not a failure.

Its status is:

> **Conceptual architecture substantially advanced; exact reconstruction blocked by source recovery.**

That is a useful place to stop.

---

# 32. Public Leads and References Collected During the Investigation

These are leads, not all equivalent in authority.

## Guilford — CPT
- https://www.guilford.com/add/forms/resick-forms.pdf?t=1
- https://www.guilford.com/books/Cognitive-Processing-Therapy-for-PTSD/Resick-Monson-Chard/9781462554270
- https://www.guilford.com/resources/Cognitive-Processing-Therapy-for-PTSD-Second-Edition/9781462554270

## Guilford — EMDR
- https://www.guilford.com/add/forms/shapiro-forms.pdf?t=1

## VA / PST-SP
- https://www.mirecc.va.gov/visn19/cpg/recs/6/
- https://link.springer.com/article/10.1007/s10865-026-00651-9
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12930348/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10164054/

## VA Safety Planning
- https://www.mirecc.va.gov/MIRECC/visn19/safety-planning/docs/VA-Safety-Planning-Intervention-Manual_508.pdf

## VA CBT-SP Workbook
- https://www.veterantraining.va.gov/documents/CBTSP_Workbook_Fill.pdf

## Historical / archaeological PST lead
- https://dreichenbaumcbtsheets.com/Problem%20Solving%20Therapy%20and%20SMART/

## Historical Springer supplement link
- https://www.springerpub.com/media/springer-downloads/Problem-Solving-Therapy-Supplement.pdf

The Springer link may no longer serve the original complete resource and should be treated as an archive lead rather than a reliable current download source.

---

# 33. Final Working Principle

The project began as an attempt to organize PDFs.

It has become an investigation into **clinical knowledge objects and the relationships among them**.

The most durable idea is:

```text
content
≠ metadata
≠ provenance
≠ collection membership
≠ assembly
≠ rendering
```

Once those relationships are represented explicitly, many different tools can be built on top of them.

That is the part worth preserving.
