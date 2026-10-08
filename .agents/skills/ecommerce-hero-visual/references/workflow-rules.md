# Workflow and Production Gates

Use these gates in order. Do not skip a failed gate by filling missing evidence with plausible content.

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

## Gate 4 — Communication Accuracy and Strategy Feasibility

Complete the brief, evidence classification, communication hierarchy, and visual direction before generation. Confirmed copy controls factual truth but does not require equal visual weight or a separate visual zone. Grouping or reducing secondary prominence is allowed when meaning is preserved. Do not add unconfirmed substitute copy merely to improve layout.

Visual Strategy must check whether a proposed scene, support relationship, and
lighting are compatible with the Product Lighting and Contact Profile before a
direction is selected. Resolve obvious incompatibility by revising the scene
or direction, not by forcing the protected product layer to fit.

Marketing expression may improve clarity or tone but must not strengthen, broaden, or certify an underlying fact. For example, a confirmed 12-hour claim may be restated with the same duration, but not as all-day performance, constant performance, or a certification.

For every direction, report required product view, supporting Reference IDs, Reference Feasibility, occlusion risk, and Fidelity Risk. Reject directions that require an unsupported view, hidden detail, invented accessory, or product redesign.

## Gate 5 — Reference Image Usage Plan

Map every supplied Reference ID to its intended stage and method. State what may transfer and what must not transfer.

- PR and PD may support product analysis, product-layer creation, and fidelity QA.
- BA may support direct brand composition and brand QA.
- SR may support approved mood, lighting, background, color atmosphere, or texture only.
- LR may support approved layout principles only.

Mark unused references explicitly. Do not allow SR or LR assets to override confirmed facts, PR, PD, or BA evidence.

## Gate 6 — Draft Layout Blueprint

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
Thumbnail risk estimate, calibration outcome, and outstanding blockers.

The handoff must end with exactly one status: `READY FOR TEXT-FREE PRODUCTION` or `BLOCKED`. READY requires a supported production mode, required Present evidence, a supported intended view, no unresolved conflict or blocker, a direction that preserves the Product Fidelity Lock, complete recorded Blueprint and Calibration artifacts, no unresolved applicable pre-generation CORE Commercial Layout Calibration `Revise`, and no material unresolved Thumbnail risk estimate. Rendered thumbnail evidence is not required for this pre-generation status. If the Handoff is missing, incomplete, not recorded, or not READY, do not begin generation; a generated result is not evidence that READY was reached. Use BLOCKED when required evidence is missing, unavailable, conflicting, insufficient, an artifact is missing, or an applicable pre-generation CORE calibration issue or material thumbnail risk remains unresolved. Planning-only Mode cannot receive READY for a real product-fidelity visual without a usable Present PR. Keep the handoff as a concise readiness checkpoint rather than duplicating upstream analysis.

Do not begin text-free production until the handoff is complete and READY.

## Gate 9 — Text-free Production

Use this priority:

1. approved product cutout or original product pixels plus a separately generated background;
2. controlled reference-guided generation only when appropriate and verifiable;
3. never final text-only reconstruction of a real product.

Generate the background without text, logos, badges, certifications, or a reconstructed target product. Composite or guide the product only according to the Reference Image Usage Plan and Product Fidelity Lock.

Check product fidelity, crop, scale, occlusion, integration, and negative space before typography.

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

Stop only when no Product Fidelity Blocking or High issue remains and no
applicable rendered commercial CORE item remains `Revise`, or when missing
verified input prevents correction. In the latter case, state the blocker and
do not describe the output as final. Report commercial completion separately
as `COMMERCIAL LAYOUT PASSED`, `COMMERCIAL LAYOUT REQUIRES REVISION`, or
`BLOCKED`.

## Commercial Clarity

Across all gates, prioritize fast product recognition, concise hierarchy, readable type, and a clear action over decorative complexity. Props, scenes, style references, and layout references must support communication without obscuring, altering, or replacing the product.
