# Workflow and Production Gates

Use these gates in order. Do not skip a failed gate by filling missing evidence with plausible content.

Human approval is a separate record from technical `READY` / `BLOCKED` and
Commercial Layout QA. At each Human Gate, submit the listed existing workflow
artifacts, record `Pending` while waiting and then the decision as `Approved`,
`Changes requested`, or `Returned`. Record the artifact version, approver, scope,
and decision time in the Brief, Visual Strategy / Handoff, or Rendered QA record
already in use. Pause while a decision is pending: do not infer approval from silence or
continue automatically. Existing authorization may be reused for H1 or H2 only
when it is explicit preauthorization for that gate's scope and its recorded
version matches the submitted artifacts; record its source, scope, and version
and do not ask the same question again. General project authorization cannot
substitute for H3 review of the actual rendered image and matching version. A human approval cannot cure
missing facts, unavailable evidence, or a Product Fidelity / factual blocker.
Reuse the existing Product Fidelity Lock, Layout Realization Record,
Typography Runtime, and Rendered QA; embed gate decisions in those records or
the existing Brief / Handoff rather than creating duplicate gates, status
systems, or reports.

## Gate 1 — Reference Asset Inventory

Inventory every supplied Product Reference Image, Product Detail Reference, Brand Asset, Style Reference, and Layout Reference. Assign stable Reference IDs and record authority, visible coverage, approved use, prohibited use, and limitations.

Before using a declared or supplied reference as evidence, verify its availability and record exactly one status: `Present` (exists and can be inspected in the current run), `Missing` (declared but the referenced file cannot be found), or `Unavailable` (known or referenced but cannot currently be accessed or inspected). Only `Present` assets are usable evidence; a manifest declaration alone does not prove existence. Reference-backed Fidelity Mode requires at least one usable `Present` PR supporting the intended view. Missing or Unavailable optional PD, BA, SR, or LR assets are not evidence and do not automatically block stages that do not require them.

Style Reference and Layout Reference are never product-fact sources. Layout Reference may affect only composition, information density, visual hierarchy, text/product balance, and negative-space planning. Do not copy the reference design.

## Gate 2 — Production Mode

Enter Reference-backed Fidelity Mode only when at least one approved usable Product Reference Image supports the intended product view.

Otherwise use Planning-only Mode. Planning may continue, but final product-fidelity generation and final fidelity QA remain Blocked. A concept mockup must be explicitly requested and labeled non-fidelity.

## Gate 3 — Product Analysis and Fidelity Lock

Analyze the visible product identity in each PR and applicable PD asset. Build a Product Fidelity Lock that traces every attribute to Reference IDs.

Preserve supported silhouette, proportions, color, finish, material appearance, logo placement, markings, structures, controls, openings, interfaces, part count, and accessories. Record unclear or unseen areas as Unknown. Do not add plausible-looking features.

If approved references conflict, mark the affected attribute Conflict and stop using it until an authoritative source is identified.

After the Product Fidelity Lock, retain a Product Lighting and Contact Profile
from approved PR / PD evidence before selecting a scene. Record Reference IDs,
supported view orientation, visible lighting direction, lighting softness /
hardness, approximate color-temperature character, contrast character, visible
product-bottom geometry, intended support / contact region, suspension intent,
and Unknown / unverified properties. Record only visibly supported evidence;
do not infer hidden contact surfaces, support hardware, or unseen lighting
behavior.

After this profile and before Visual Strategy, classify the Task / Layout
Profile and consider optional Benchmark Layout Retrieval under
[benchmark-layout-retrieval.md](benchmark-layout-retrieval.md). Use selected
metadata and, only when actually available and opened, selected images as
advisory comparative context. Retrieval failure or absence does not block the
workflow.

## Human Gate H1 — Input Baseline Confirmation

Trigger H1 after input and material verification is complete (Reference Asset
Inventory, confirmed product facts and copy, authorization, official brand
guidance, hard limits, Product Fidelity Lock, and Product Lighting and Contact
Profile) and before Visual Strategy. Submit those existing records plus the
Brief's evidence / conflict list. The human confirms or corrects the factual
baseline, copy, authorization scope, official brand requirements, prohibited
elements, and hard platform or project limits. Record the decision, approver,
scope, and version in the existing Brief / input record.

`Approved` permits Gate 4. `Changes requested` updates the input organization
and repeats the affected analysis. `Returned` sends the work to Gate 1 for
input organization. Keep H1 pending until an explicit decision arrives; silence
is not approval. An authorization already explicit in the Brief may be recorded and
reused, but it does not waive unresolved evidence or fidelity blockers.

## Gate 4 — Communication Accuracy and Strategy Feasibility

Complete the brief, evidence classification, communication hierarchy, and visual direction before generation. Confirmed copy controls factual truth but does not require equal visual weight or a separate visual zone. Grouping or reducing secondary prominence is allowed when meaning is preserved. Do not add unconfirmed substitute copy merely to improve layout.

Visual Strategy must check whether a proposed scene, support relationship, and
lighting are compatible with the Product Lighting and Contact Profile before a
direction is selected. Resolve obvious incompatibility by revising the scene
or direction, not by forcing the protected product layer to fit.

Marketing expression may improve clarity or tone but must not strengthen, broaden, or certify an underlying fact. For example, a confirmed 12-hour claim may be restated with the same duration, but not as all-day performance, constant performance, or a certification.

For every direction, report required product view, supporting Reference IDs, Reference Feasibility, occlusion risk, and Fidelity Risk. Reject directions that require an unsupported view, hidden detail, invented accessory, or product redesign.

Keep a concise `Project Style Constraint Record` in the existing Brief or
Visual Strategy. Its fields are: source and authority, style keywords, font(s),
palette, image style, prohibited elements, platform limits, confirmation
status, and version. Mark each source as an official brand guideline, an
explicit user requirement, or an AI design suggestion. Skill-wide hard
constraints (product fidelity, factual accuracy, authentic Brand Assets,
readability, and platform rules) remain in force. If no official font is
specified, candidate fonts remain AI proposals and must not be presented as
official brand typography.

Apply the record in three levels: (1) Skill global hard constraints, which
always apply; (2) project brand hard constraints from a verified brand source
or explicit user requirement, confirmed at H1; and (3) project design choices
such as style keywords, candidate font pairing, palette, scene, and composition,
proposed by AI and frozen at H2. The third level may not weaken the first two.

## Gate 5 — Reference Image Usage Plan

Map every supplied Reference ID to its intended stage and method. State what may transfer and what must not transfer.

- PR and PD may support product analysis, product-layer creation, and fidelity QA.
- BA may support direct brand composition and brand QA.
- SR may support approved mood, lighting, background, color atmosphere, or texture only.
- LR may support approved layout principles only.

Mark unused references explicitly. Do not allow SR or LR assets to override confirmed facts, PR, PD, or BA evidence.

## Gate 6 — Draft Layout Blueprint

Before fixing product or text coordinates, analyze the available background or
planned scene: support surfaces, perspective, wall-floor junctions, tabletop rear
edges, important structural lines, and usable text areas. Keep concise placement
implications in the existing Blueprint / Support Plane and Contact Plan; coordinate
alignment alone proves neither grounding nor a sensible text layout.

After the Reference Image Usage Plan, create and retain a Draft Layout
Blueprint for product, copy, negative-space, promotion, CTA, and Brand Asset
zones. It must minimally record the selected archetype, product zone and
intended prominence, copy zones, primary communication anchor,
supporting-information grouping, price / CTA relationship when applicable,
negative-space purpose, grounding intent, and intended visual reading order.
Classify each major region as product, primary communication, supporting
information, commercial anchor / price / CTA, intentional separation, or
intentional atmosphere. Record a non-final `Thumbnail risk estimate` for
planned product prominence, primary-message prominence, commercial-anchor
prominence, and likely information-density risk. It does not replace a
rendered thumbnail check.
Record a Support Plane and Contact Plan covering the physical support plane or
support relationship, intended contact point or region, resting or intentionally
suspended state, support-plane perspective relationship, expected contact-shadow
relationship, and protected product areas. The support may be a tabletop,
shelf, pedestal, fabric, wall-mounted context, liquid/contact environment, or
another physically plausible support; it does not have to be a floor.
Identify protected product areas without introducing fixed product-specific
dimensions. If the Blueprint is missing, Commercial Layout Calibration cannot
run and `PRE-GENERATION STATUS = BLOCKED`.

## Gate 7 — Commercial Layout Calibration

Run the diagnostic checks in
[commercial-layout-calibration.md](commercial-layout-calibration.md) against
the draft Layout Blueprint. This gate occurs before the Pre-generation
Handoff and does not require generated pixels.

Retain a complete Commercial Layout Calibration Record containing all
applicable pre-generation CORE diagnostics and relevant ARCHETYPE-CONDITIONAL diagnostics.
Use exactly `Calibrated`, `Revise`, or `Not Applicable`. If the record is
missing, set `PRE-GENERATION STATUS = BLOCKED` and do not begin generation.
Before any applicable pre-generation CORE item is `Calibrated`, record Status,
Observation, Evidence, and why no material revision is needed or the required
action.
Product scale requires a Largest Effective Product Scale counterfactual;
empty-space efficiency requires a functional purpose for every major region;
typography requires explicit primary/supporting/commercial-anchor hierarchy and
a bilingual-density check. Generic evidence is insufficient. If an applicable
pre-generation CORE diagnostic is `Revise`, identify the layout problem,
revise the Layout Blueprint, rerun the affected checks, and record the new
result. `Mobile-thumbnail clarity` is rendered-only and receives no
pre-generation Calibration status; use the Blueprint `Thumbnail risk estimate`
before generation. Do not proceed with unresolved
applicable pre-generation CORE `Revise` items. `Not Applicable` does not block
readiness.

For the existing `Grounding` CORE diagnostic, use the Product Lighting and
Contact Profile and Support Plane and Contact Plan to assess contact integrity
and scene compatibility. Before `Grounding = Calibrated`, record compatible
lighting and support evidence, plausible perspective and local scale, and a
credible plan to avoid a pasted or sticker effect. A material incompatibility
in either evidence category is `Grounding = Revise`.

Commercial calibration cannot override the Product Fidelity Lock. Benchmark
retrieval follows the optional protocol linked above; it may use compact
metadata and explicitly selected images only. Do not load the image set
automatically. Benchmark support is advisory and must not replace diagnostic
evidence, add a readiness gate, or copy distinctive compositions or content.
If metadata, the selector, or selected images are unavailable, continue with
qualitative calibration; benchmark absence must not block production.

## Gate 8 — Pre-generation Handoff

After Commercial Layout Calibration is complete, create and retain a concise
Pre-generation Handoff that explicitly references the Draft Layout Blueprint
and Commercial Layout Calibration Record. Summarize the Reference Asset
Inventory availability statuses, evidence conflicts and Unknowns, Production
Mode, Product Fidelity Lock statuses, selected direction, Reference
Feasibility, Fidelity Risk, Reference Image Usage Plan, Layout Blueprint,
Thumbnail risk estimate, calibration outcome, Project Style Constraint Record
version, and outstanding blockers.

The handoff must end with exactly one status: `READY FOR TEXT-FREE PRODUCTION` or `BLOCKED`. READY requires a supported production mode, required Present evidence, a supported intended view, no unresolved conflict or blocker, a direction that preserves the Product Fidelity Lock, complete recorded Blueprint and Calibration artifacts, no unresolved applicable pre-generation CORE Commercial Layout Calibration `Revise`, and no material unresolved Thumbnail risk estimate. Rendered thumbnail evidence is not required for this pre-generation status. If the Handoff is missing, incomplete, not recorded, or not READY, do not begin generation; a generated result is not evidence that READY was reached. Use BLOCKED when required evidence is missing, unavailable, conflicting, insufficient, an artifact is missing, or an applicable pre-generation CORE calibration issue or material thumbnail risk remains unresolved. Planning-only Mode cannot receive READY for a real product-fidelity visual without a usable Present PR. Keep the handoff as a concise readiness checkpoint rather than duplicating upstream analysis.

Do not begin text-free production until the handoff is complete and READY.

## Human Gate H2 — Visual Direction and Project Style Freeze

Trigger H2 after Visual Strategy, Draft Layout Blueprint, Commercial Layout
Calibration, and the Pre-generation Handoff are complete, and immediately
before Gate 9 generation. Submit the selected direction, required product view,
Reference Image Usage Plan, Blueprint, calibration result, Handoff, and the
Project Style Constraint Record. The human confirms the visual direction,
scene, composition, and project style choices (keywords, font strategy,
palette, image style, prohibited elements, and platform limits).

`Approved` freezes that direction and record for production. `Changes requested`
returns to the relevant strategy or layout planning step; `Returned`
rejects the submission and restarts the affected Gate 4 or Gate 6 work. Record
the decision, approver, scope, and incremented artifact version in the existing
Visual Strategy / Handoff. Do not generate while H2 is pending. After approval,
AI may adjust size, spacing, and position within the frozen direction. A core
style, font-strategy, or palette change requires a new H2 decision; ordinary
local layout polish does not.

## Gate 9 — Text-free Production

Use this priority:

1. approved product cutout or original product pixels plus a separately generated background;
2. controlled reference-guided generation only when appropriate and verifiable;
3. never final text-only reconstruction of a real product.

Generate the background without text, logos, badges, certifications, or a reconstructed target product. Composite or guide the product only according to the Reference Image Usage Plan and Product Fidelity Lock.

Before locking placement, repeat the Blueprint scene-space analysis on the actual
background and adapt product contact and text areas to its geometry. Check product
fidelity, crop, scale, occlusion, integration, and negative space before typography.

For raster composition, initialize and retain a concise `Layout Realization
Record` when compositing the product: actual visible product bounds used for
scaling rather than only the transparent canvas; intended prominence and
implemented scale / placement; support-plane geometry, physical contact region,
placement-depth reasoning, contact-shadow relationship, and rendered preview.
Mark unavailable measurements as limitations and never invent measured evidence.

When Grounding is `Revise`, prefer corrections in this order: revise or
regenerate the background / support plane; revise separate contact-shadow /
cast-shadow layers; revise placement, scale, or non-destructive edge
integration; then use restrained tonal integration only when product fidelity
remains directly verifiable. Do not redesign product geometry, use unsupported
rotation or mirroring, replace materials, change logos, recolor
uncontrollably, or invent supports to solve scene integration. Product
Fidelity Lock remains authoritative. Intentionally suspended products are not
forced onto a support plane, but suspension must be explicit and physically
coherent without invented hardware.

## Gate 10 — Copy and Brand Composition

Add only confirmed copy. Group related confirmed copy or reduce secondary
prominence when meaning is preserved; do not add unconfirmed substitute copy.
Use official Brand Assets directly, especially logos and wordmarks. Do not ask
a generation model to redraw an official brand asset.

Keep the product as the primary visual focus. Use readable hierarchy and sufficient contrast. Create separate language versions by default when combined bilingual typography would reduce clarity.

Plan the full type hierarchy: headline, product name, selling points, price,
campaign labels, CTA, and dates when present. All copy must be clearly readable
at full size; give middle-tier information enough commercial recognition rather
than allowing only the headline and price to stand out while everything else is tiny.
Organize modules around actual usable space, checking visual spacing within and
between groups. Coordinate price, dates, and CTA as related information; reposition
modules when needed to avoid unjustified crossings of scene structural lines.
Related separators, dots, and button backgrounds must move with their text.
After composing typography, add measured bounds and actual typography scale for
the full hierarchy to the existing Layout Realization Record, without a duplicate log.

For raster typography, invoke the reusable runtime from the repository root
(requires Pillow and fontTools):

```sh
python .agents/skills/ecommerce-hero-visual/scripts/typography_runtime.py --base text-free.png --layout layout.json --output composed.png --thumbnail thumbnail.png --report typography-report.json
```

The JSON `texts` list requires `text`, `position: [x, y]`, `font` (actual file path,
relative to the JSON if not absolute), `size` (pixel size), `weight` (number or null
to retain the font default), `color` (Pillow color string or RGB/RGBA array), and
`role` per item; optional fields are `id`, `font_index`, and multiline `spacing`.
Positions are Pillow text origins; use measured textbbox for visible bounds.
Provide `protected_regions: [{"id": "product", "bbox": [left, top, right, bottom]}]`
for protected product / brand areas. `contrast_warning_ratio` is optional and
configurable; its default 3.0 is an auxiliary warning threshold, not visual approval.
The script docstring gives a complete schema example. Missing fonts / glyphs,
unsupported weights, and out-of-range real variable axes produce explicit errors
without fallback. Protection overlaps abort image output; text overlaps and local
background contrast risk remain measured evidence. This is input enforcement,
not another commercial pass / fail gate. The runtime only draws requested text;
it does not generate backgrounds, alter product layers, or redraw brand Logos.
Link the JSON report and output paths into the existing Layout Realization Record
after typography, retaining actual font axes, textbbox, scale, overlaps, contrast
and unavailable-measurement limitations. Inspect the composition and exact 224x280
thumbnail in existing Rendered QA; the runtime preserves source aspect ratio with
centered letterboxing and reports actual scale, resized image size, and padding.
Output creation is not thumbnail inspection.
If visual inspection fails, adjust task-specific parameters and rerun from the
text-free base, then append the inspection, corrections, and rerender result after QA.

## Gate 11 — Side-by-side Reference QA and Stop Condition

Compare the output directly against every applicable PR, PD, and BA asset. Use Pass, Revise, Blocked, or Not Visible and assign a severity to every mismatch.

For each Blocking or High issue:

1. record the Reference IDs and affected attribute;
2. identify whether the cause is generation, composition, crop, lighting, copy, or asset misuse;
3. revise the asset, prompt, direction, layout, or composition method;
4. repeat the side-by-side check.

After composition and typography, run the rendered commercial-layout recheck
with actual rendered evidence for product prominence, typography hierarchy,
product / copy balance, empty-space efficiency, grounding, information
grouping, visual reading order, and mobile-thumbnail clarity using a
consistent reduced-size preview. Reuse the criterion-specific evidence rules
in `commercial-layout-calibration.md` for rendered product-scale
counterfactuals, functional empty-space regions, materially distinct
typography hierarchy, and insufficient generic evidence. Rendered evidence is
authoritative when it contradicts the Blueprint. For rendered Grounding,
verify support contact, contact-shadow origin, shadow softness and light
compatibility when applicable, support-plane perspective, local scene scale,
edge integration, and perceived physical weight. A visible support gap,
detached shadow, material lighting incompatibility, or pasted perspective /
scale relationship is `Grounding = Revise`. If any applicable rendered CORE item is `Revise`,
revise the composition, typography, or background, rerender, and repeat the
check. Without actual thumbnail inspection, final commercial completion is
forbidden. Keep Product Fidelity QA independent and authoritative.

Pre-generation `Calibrated` does not prove the render is correct. If the product
is visually too small, lacks commercial prominence, appears unsupported,
conflicts with support-plane perspective, or the primary message is weak, revise
the responsible parameters, update the Layout Realization Record, rerender, and
recheck with the existing Rendered QA statuses. Contact with a horizontal edge
alone does not demonstrate physically plausible scene placement. Do not add a
separate pass / fail gate for this record.
After each Rendered QA pass, add the consistent thumbnail findings and parameter
corrections with rerender results to the record.

Stop only when no Product Fidelity Blocking or High issue remains and no
applicable rendered commercial CORE item remains `Revise`, or when missing
verified input prevents correction. If the missing input prevents correction,
set or retain `BLOCKED`, stop, and report the blocking reason; do not submit H3.
After the issue is resolved, repeat the applicable checks. Submit H3 only when
no major issue remains unresolved and the status is not `BLOCKED`. This is AI QA
completion and permits H3 submission only; final formal delivery requires H3's
explicit approval of the actual rendered image and matching artifact version.
Report commercial completion separately
as `COMMERCIAL LAYOUT PASSED`, `COMMERCIAL LAYOUT REQUIRES REVISION`, or
`BLOCKED`.

## Human Gate H3 — Rendered Deliverable Review

Trigger H3 after Gate 11 Rendered QA is complete. Submit the full-size image,
the consistent thumbnail, the existing Side-by-side / rendered QA findings,
and a concise issue list with severity, affected area, and correction status.
The human confirms whether the rendered result is acceptable for the approved
direction and style. Record the decision, approver, submitted artifact
versions, scope, and decision time in the existing Rendered QA / Layout
Realization Record.

Keep H3 `Pending` until the human decision arrives; do not release or publish
while it is pending.

`Approved` completes the human review of the submitted actual image and matching
artifact version; `Changes requested` or `Returned` maps
the issue to its owning production step: input facts, authorization, or
brand-source issues return to Gate 1 or Gate 3 (and may require H1); copy
content, strategy, scene, or composition issues return to Gate 4 or Gate 6
(and may require H2); text, font, logo placement, or typography issues return
to Gate 10; rendering,
lighting, grounding, crop, or integration issues return to Gate 9; QA evidence
or thumbnail issues return to Gate 11. Rerender and repeat the applicable QA
before H3 again. H3 cannot approve unresolved Product Fidelity or factual
blockers. If formal publication authorization is required, record it
separately against this approved artifact without repeating the approved
aesthetic review.

## Commercial Clarity

Across all gates, prioritize fast product recognition, concise hierarchy, readable type, and a clear action over decorative complexity. Props, scenes, style references, and layout references must support communication without obscuring, altering, or replacing the product.
