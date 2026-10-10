---
name: ecommerce-hero-visual
description: Plan and produce reference-backed ecommerce product hero visuals from approved product imagery, controlled reference assets, and verified product or campaign facts. Use for marketplace main images, campaign posters, promotional key visuals, and bilingual product variants; do not use it to reconstruct a real product from text alone or create unsupported claims.
---

# Ecommerce Hero Visual

Create commercially clear product hero visuals while preserving product identity and keeping every visual decision traceable to approved evidence.

## Non-negotiable Rules

- Analyze the request, facts, and reference assets before generating anything.
- Treat approved Product Reference Images, Product Detail References, Brand Assets, and confirmed facts as controlled evidence.
- Never invent or upgrade product parameters, functions, shape, structure, materials, colors, accessories, prices, discounts, dates, certifications, awards, badges, promotional rules, logos, or markings.
- Confirmed copy controls factual truth but does not require equal visual weight or a separate visual zone. Unconfirmed copy must never be added to improve layout.
- Style Reference and Layout Reference are not product-fact sources.
- Layout Reference may influence only composition, information density, visual hierarchy, text/product balance, and negative-space planning. Do not copy the reference design itself.
- Prefer approved product cutouts or original product pixels with a separately generated text-free background.
- Use reference-guided generation only when it is appropriate and product identity can remain verifiable.
- Never reconstruct a real product from text alone.
- Add typography and official Brand Assets after the text-free visual is verified.
- Perform Side-by-side Reference QA, revise material issues, and re-check before declaring completion.

## Workflow

### 1. Analyze Inputs and Build the Reference Asset Inventory

If the current project contains inputs/ or input-manifest.yaml, inspect those materials first. Treat input-manifest.example.yaml only as a template; its example entries are not evidence that an asset exists.

Also accept images and files attached directly by the user. Repository-based input and directly attached input are both valid and neither is exclusive. Normalize both sources into one Reference Asset Inventory before product analysis or generation.

Read [references/input-schema.md](references/input-schema.md). Assign stable IDs and record the authority, visible coverage, allowed use, and limitations of every supplied asset:

- PR for Product Reference Image;
- PD for Product Detail Reference;
- BA for Brand Asset;
- SR for Style Reference;
- LR for Layout Reference.

Before treating any declared or supplied reference as evidence, verify that it is actually available in the current run and record exactly one status in the Reference Asset Inventory:

- **Present:** the asset exists and can be inspected;
- **Missing:** the manifest or task declares it, but the referenced file cannot be found;
- **Unavailable:** the asset is known or referenced, but cannot currently be accessed or inspected.

Only Present assets may be used as reference evidence. A manifest declaration alone does not prove that an asset exists. If no usable Present Product Reference Image supports the intended view, a Missing or Unavailable required PR keeps the workflow in Planning-only Mode. Missing or Unavailable optional PD, BA, SR, or LR assets are not evidence and do not automatically block stages that do not require them.

Read [references/reference-image-workflow.md](references/reference-image-workflow.md) whenever image or brand references are supplied. Separate confirmed facts, reference evidence, strategic proposals, missing blockers, and optional enhancements.

### 2. Select the Production Mode

Use Reference-backed Fidelity Mode only when at least one approved, usable Product Reference Image is available.

Use Planning-only Mode when no usable Product Reference Image is available. Continue with the brief, communication strategy, directions, layout, prompt planning, and copy planning, but do not generate or claim a final product-fidelity visual. A concept mockup must be labeled non-fidelity and must not be presented as the real product.

### 3. Analyze the Product and Lock Fidelity

Analyze each Product Reference Image and Product Detail Reference. Record visible views, silhouette, proportions, colors, finishes, materials, logos, markings, controls, openings, interfaces, parts, accessories, occlusions, and unknown areas.

Create a Product Fidelity Lock that traces every locked or unknown attribute to specific Reference IDs. Do not infer unseen product surfaces or details. When approved references conflict, stop using the disputed attribute until an authoritative source is identified.

Create and retain a concise Product Lighting and Contact Profile from the
approved PR / PD evidence before selecting a scene. Record Reference IDs,
supported camera / view orientation, visible lighting direction, lighting
softness / hardness, approximate color-temperature character, contrast
character, visible product-bottom geometry, intended support / contact region,
suspension intent, and Unknown / unverified properties. Record only visibly
supported evidence. Do not infer hidden contact surfaces, support hardware, or
unseen lighting behavior.

### 4. Classify the Task and Retrieve Optional Layout Benchmarks

After the Product Fidelity Lock and Product Lighting and Contact Profile are
complete, classify the Task / Layout Profile and decide whether optional
Benchmark Layout Retrieval would help. Follow
[references/benchmark-layout-retrieval.md](references/benchmark-layout-retrieval.md).
Use the compact metadata and deterministic selector only when available; load
only selected benchmark images after resolving and opening them in the current
run. Retrieval is advisory: unavailable or insufficient benchmark support
falls back to the existing qualitative workflow and never blocks production.
Benchmark evidence may inform Visual Strategy and the Draft Layout Blueprint
relationally, but cannot provide product facts, override Product Fidelity Lock,
replace Commercial Layout Calibration evidence, or impose a copied layout.

### 5. Build the Communication and Visual Strategy

Define the audience, intended action, three-second takeaway, primary concern, emotional tone, and confirmed communication hierarchy.

Before selecting a direction, check whether its proposed scene, support
relationship, and lighting are compatible with the Product Lighting and
Contact Profile. Resolve an obvious incompatibility by revising the scene or
direction; do not force the protected product layer to fit it.

Use [references/visual-strategy.md](references/visual-strategy.md) when selecting or comparing directions. Each direction must include Reference Feasibility, required product view, occlusion risk, and Fidelity Risk. Reject or revise directions that require an unavailable or unverified product view.

### 6. Create the Reference Image Usage Plan

Before generation, map each Reference ID to the stages where it will be used. State the intended transfer and forbidden transfer for analysis, background generation, product composition, typography, and QA.

Style Reference may transfer only approved style properties. Layout Reference may transfer only layout principles and must not be copied. Official logos and other Brand Assets should be placed directly rather than regenerated.

### 7. Draft the Layout Blueprint

Before fixing product or text coordinates, apply the scene-space analysis in
[references/workflow-rules.md](references/workflow-rules.md), Gate 6; retain its
placement implications in the existing Blueprint and Support Plane and Contact Plan.

Create and retain a recorded Draft Layout Blueprint for the product, copy,
negative-space, promotion, CTA, and Brand Asset zones. It must minimally
record the selected archetype, intended product zone and prominence, copy
zones, primary communication anchor, supporting-information grouping, price /
CTA relationship when applicable, negative-space purpose, grounding intent,
and intended visual reading order. Classify the purpose of each major canvas
region as product, primary communication, supporting information, commercial
anchor / price / CTA, intentional separation, or intentional atmosphere. Add a
non-final `Thumbnail risk estimate` covering planned product prominence,
primary-message prominence, commercial-anchor prominence, and likely
information-density risk. It does not replace rendered thumbnail validation.
Also record a Support Plane and Contact Plan: physical support plane or
support relationship, intended product contact point or region, resting or
intentionally suspended state, support-plane perspective relationship,
expected contact-shadow relationship, and protected product areas. The support
may be a tabletop, shelf, pedestal, fabric, wall-mounted context, liquid or
another physically plausible support when compatible with the task and
references; it does not have to be a floor. If the product is intended to
rest and its rendered base fails to meet the support, `Grounding = Revise`.
Intentional suspension must be explicit and must not invent wires, stands,
mounts, or hidden support hardware.
Identify protected product areas without introducing fixed product-specific
dimensions. If the recorded Draft Layout Blueprint is missing, Commercial
Layout Calibration cannot run and pre-generation status is `BLOCKED`.

### 8. Run Commercial Layout Calibration

Read [references/commercial-layout-calibration.md](references/commercial-layout-calibration.md).
Evaluate the recorded Draft Layout Blueprint before generation and retain a
recorded Commercial Layout Calibration result. The record must contain every
applicable pre-generation CORE diagnostic and relevant ARCHETYPE-CONDITIONAL diagnostics,
using exactly `Calibrated`, `Revise`, or `Not Applicable`.

Before an applicable pre-generation CORE item is `Calibrated`, record its
Status, Observation, Evidence, and why no material revision is needed (or the
required action). Generic
claims such as “product is visible”, “headline is readable”, “there is
breathing room”, or “shadow exists” are insufficient. Product scale requires
an explicit `Largest Effective Product Scale` counterfactual test. Typography
requires an explicit primary message, supporting information, and commercial
anchor when applicable, including a check that bilingual density does not
shrink the type system or product below a commercially useful level. The
Blueprint must explain the function of each major region; materially
non-functional empty space is `Revise`.

For the existing `Grounding` CORE diagnostic, use the Product Lighting and
Contact Profile and Support Plane and Contact Plan to assess contact integrity
and scene compatibility. Before `Grounding = Calibrated`, record evidence for
the support relationship or explicit suspension, plausible perspective and
local scale, compatible light direction / softness / contrast / color
temperature, and a credible plan to avoid a pasted or sticker effect. A
material incompatibility in either contact integrity or scene compatibility is
`Grounding = Revise`.

`Mobile-thumbnail clarity` is rendered-only and is not assigned a calibration
status in this pre-generation record. Before generation, record only the
Blueprint-level `Thumbnail risk estimate`; it may be clear without rendered
thumbnail evidence when no other applicable pre-generation CORE item remains
`Revise` and no material thumbnail risk is unresolved.

If an applicable pre-generation CORE diagnostic is `Revise`, identify the
commercial layout problem, revise the Layout Blueprint, and rerun the affected
checks. Do not continue to the Pre-generation Handoff with unresolved
applicable pre-generation CORE `Revise` items. Record each revised result. If
the Commercial Layout Calibration record is missing, set `PRE-GENERATION
STATUS = BLOCKED` and do not begin generation. `Not Applicable` does not block
readiness. Commercial calibration cannot override the Product Fidelity Lock.

### 9. Complete the Pre-generation Handoff

Then create and retain a concise Pre-generation Handoff. It must reference
the recorded Draft Layout Blueprint and Commercial Layout Calibration Record,
and summarize the Reference Asset Inventory availability statuses, evidence
conflicts and unresolved Unknowns, Production Mode, Product Fidelity Lock
statuses, selected direction, Reference Feasibility, Fidelity Risk, Reference
Image Usage Plan, Layout Blueprint, Thumbnail risk estimate, calibration
outcome, and outstanding blockers. If Benchmark Layout Retrieval ran, add a
concise optional summary of resource state, coverage, selected reference IDs
and declared roles, evidence source (metadata only or inspected benchmark
image), and any material limitation. If retrieval did not run or was
unavailable, no benchmark summary is required; benchmark absence never blocks
readiness.

Set the final readiness status to exactly one of:

- `READY FOR TEXT-FREE PRODUCTION`;
- `BLOCKED`.

Use `READY FOR TEXT-FREE PRODUCTION` only when the selected mode supports the requested stage, required Present evidence exists, the intended product view is supported, no unresolved conflict or blocker prevents faithful production, the selected direction can preserve the Product Fidelity Lock, the recorded Draft Layout Blueprint and Commercial Layout Calibration Record are complete, no applicable pre-generation CORE Commercial Layout Calibration diagnostic remains `Revise`, and the Thumbnail risk estimate has no material unresolved risk. Rendered `Mobile-thumbnail clarity` is not required for this pre-generation status. If the Handoff is missing, incomplete, not recorded, or not READY, do not begin generation; a generated result is not evidence that READY was reached. Use `BLOCKED` when required evidence is missing, unavailable, conflicting, insufficient, an artifact is missing, or an applicable pre-generation CORE calibration issue or material thumbnail risk remains unresolved. Planning-only Mode may continue planning, but it cannot receive READY for a real product-fidelity visual without a usable Present PR.

This handoff is a readiness checkpoint, not a duplicate of the upstream analysis tables. Do not begin text-free production until it is complete and READY.

### 10. Plan and Produce the Text-free Visual

Use the approved Layout Blueprint for the product, negative space, headline, supporting copy, promotion, CTA, and Brand Assets.

Use this production priority:

1. approved product cutout or original product pixels plus a separately generated text-free background;
2. controlled reference-guided generation only when the tool and source quality support verifiable fidelity;
3. no final product generation from text alone.

The text-free output must preserve the Product Fidelity Lock, leave usable type space, and exclude marketing text, fake seals, invented logos, unsupported parts, and unrelated accessories.

Before typography, verify scene integration against the Product Lighting and
Contact Profile and Support Plane and Contact Plan. Prefer revising the
background or support plane, then separate contact-shadow / cast-shadow layers,
then placement, scale, or non-destructive edge integration, and only then
restrained tonal integration when product fidelity remains directly verifiable.
Do not redesign product geometry, rotate or mirror it without support, replace
materials, change logos, recolor it uncontrollably, or invent supports to solve
scene integration.

For raster composition, initialize and retain a concise `Layout Realization
Record` when compositing the product. Connect the Blueprint to the actual visible
product bounds used for scaling (not merely the transparent image canvas),
intended product prominence and implemented scale / placement, support-plane
geometry, physical contact region, placement-depth reasoning, contact-shadow
relationship, and rendered preview. If a measurement is unavailable, record the
limitation; never invent measured evidence.

### 11. Add Copy and Brand Assets

Add only confirmed copy. Confirmed copy may be grouped, reduced in secondary
prominence, or combined into a coherent information module without changing
its meaning or omitting text explicitly required by the task. It does not
require equal visual weight or a separate visual zone. Do not invent
substitute copy. Use supplied official Brand Assets directly, especially
logos and product marks. Do not redraw them with a generation model. Create
separate language variants by default when combined bilingual typography
would reduce clarity.

After composing typography, add measured bounds and actual typography scale for
the full type hierarchy to the existing Layout Realization Record.

For raster text composition, use [scripts/typography_runtime.py](scripts/typography_runtime.py)
on the verified text-free composite with a task-specific JSON layout. Follow the
invocation and input contract in [references/workflow-rules.md](references/workflow-rules.md),
Gate 10. Retain its font / axis evidence, actual textbbox and typography scale,
overlap findings, contrast limitations, and output paths in the Layout Realization
Record. Inspect both outputs in the existing Rendered QA; tool execution and
contrast measurements do not establish visual approval. If visual inspection
fails, adjust the layout parameters, rerun on the same text-free base, and recheck.

### 12. Run Side-by-side Reference QA and Iterate

Use [references/quality-checklist.md](references/quality-checklist.md). Compare the output directly against every applicable PR, PD, and BA reference. Record Pass, Revise, Blocked, or Not Visible for each attribute, assign severity, fix every Blocking or High issue, and re-check the affected criteria. Also complete the rendered commercial-layout recheck described in the checklist using actual rendered evidence, including a consistent reduced-size thumbnail preview and the criterion-specific evidence rules from the calibration reference; it does not replace Side-by-side Reference QA or retroactively validate the pre-generation blueprint. Rendered QA is authoritative when it contradicts the Blueprint. If any applicable rendered commercial CORE item is `Revise`, revise the composition, typography, or background, rerender, and recheck before completion. Without an actual thumbnail inspection, final commercial completion is forbidden.

A `Calibrated` Blueprint does not prove the render is correct. If the rendered
product is visually too small, lacks commercial prominence, appears unsupported,
conflicts with support-plane perspective, or the primary message is weak, revise
the responsible composition parameters, update the Layout Realization Record,
rerender, and recheck using the existing Rendered QA statuses. Contact with a
horizontal edge alone is not evidence of physically plausible scene placement.
After each Rendered QA pass, add the consistent thumbnail inspection results and
every parameter correction with its rerender result to the record.

Completion requires either:

- no unresolved Product Fidelity Blocking or High issue and no unresolved applicable rendered Commercial Layout CORE `Revise`; or
- a clear `BLOCKED` status explaining which verified input or required artifact is missing.

Commercial completion status must be reported separately as exactly one of:

- `COMMERCIAL LAYOUT PASSED`;
- `COMMERCIAL LAYOUT REQUIRES REVISION`;
- `BLOCKED`.

Follow the production gates in [references/workflow-rules.md](references/workflow-rules.md).

## Deliverables

Return the items relevant to the request:

- structured brief and evidence status;
- Reference Asset Inventory;
- selected production mode;
- missing information and generation blockers;
- Product Reference Analysis;
- Product Fidelity Lock with Reference IDs;
- Product Lighting and Contact Profile;
- communication hierarchy;
- visual direction options with Reference Feasibility and Fidelity Risk;
- Reference Image Usage Plan;
- Draft Layout Blueprint;
- Commercial Layout Calibration record;
- Pre-generation Handoff with final readiness status;
- optional Benchmark Layout Reference Set only when retrieval ran;
- reference-based text-free generation or composition prompt;
- exact confirmed copy plan;
- Side-by-side Reference QA, revisions, and final status;
- rendered commercial-layout recheck and commercial completion status;
- Layout Realization Record for raster composition;
- final visual variants when capability and required approved assets are available.

## Examples

These files are optional validation artifacts, not required runtime inputs. Normal use must work with repository-based inputs, directly attached inputs, or both.

Use [examples/NORI-test-case.md](examples/NORI-test-case.md) as the no-Product-Reference negative test. It must remain in Planning-only Mode.

Use [examples/reference-backed-test-spec.md](examples/reference-backed-test-spec.md) as the specification for a future positive test. It is not runnable until legitimate approved reference assets are supplied; do not create fake product images to satisfy it.
