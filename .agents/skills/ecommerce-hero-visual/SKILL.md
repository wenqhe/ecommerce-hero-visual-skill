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

Read [references/reference-image-workflow.md](references/reference-image-workflow.md) whenever image or brand references are supplied. Separate confirmed facts, reference evidence, strategic proposals, missing blockers, and optional enhancements.

### 2. Select the Production Mode

Use Reference-backed Fidelity Mode only when at least one approved, usable Product Reference Image is available.

Use Planning-only Mode when no usable Product Reference Image is available. Continue with the brief, communication strategy, directions, layout, prompt planning, and copy planning, but do not generate or claim a final product-fidelity visual. A concept mockup must be labeled non-fidelity and must not be presented as the real product.

### 3. Analyze the Product and Lock Fidelity

Analyze each Product Reference Image and Product Detail Reference. Record visible views, silhouette, proportions, colors, finishes, materials, logos, markings, controls, openings, interfaces, parts, accessories, occlusions, and unknown areas.

Create a Product Fidelity Lock that traces every locked or unknown attribute to specific Reference IDs. Do not infer unseen product surfaces or details. When approved references conflict, stop using the disputed attribute until an authoritative source is identified.

### 4. Build the Communication and Visual Strategy

Define the audience, intended action, three-second takeaway, primary concern, emotional tone, and confirmed communication hierarchy.

Use [references/visual-strategy.md](references/visual-strategy.md) when selecting or comparing directions. Each direction must include Reference Feasibility, required product view, occlusion risk, and Fidelity Risk. Reject or revise directions that require an unavailable or unverified product view.

### 5. Create the Reference Image Usage Plan

Before generation, map each Reference ID to the stages where it will be used. State the intended transfer and forbidden transfer for analysis, background generation, product composition, typography, and QA.

Style Reference may transfer only approved style properties. Layout Reference may transfer only layout principles and must not be copied. Official logos and other Brand Assets should be placed directly rather than regenerated.

### 6. Plan and Produce the Text-free Visual

Create a layout blueprint for the product, negative space, headline, supporting copy, promotion, CTA, and Brand Assets.

Use this production priority:

1. approved product cutout or original product pixels plus a separately generated text-free background;
2. controlled reference-guided generation only when the tool and source quality support verifiable fidelity;
3. no final product generation from text alone.

The text-free output must preserve the Product Fidelity Lock, leave usable type space, and exclude marketing text, fake seals, invented logos, unsupported parts, and unrelated accessories.

### 7. Add Copy and Brand Assets

Add only confirmed copy. Use supplied official Brand Assets directly, especially logos and product marks. Do not redraw them with a generation model. Create separate language variants by default when combined bilingual typography would reduce clarity.

### 8. Run Side-by-side Reference QA and Iterate

Use [references/quality-checklist.md](references/quality-checklist.md). Compare the output directly against every applicable PR, PD, and BA reference. Record Pass, Revise, Blocked, or Not Visible for each attribute, assign severity, fix every Blocking or High issue, and re-check the affected criteria.

Completion requires either:

- no unresolved Blocking or High issue; or
- a clear Blocked status explaining which verified input is missing.

Follow the production gates in [references/workflow-rules.md](references/workflow-rules.md).

## Deliverables

Return the items relevant to the request:

- structured brief and evidence status;
- Reference Asset Inventory;
- selected production mode;
- missing information and generation blockers;
- Product Reference Analysis;
- Product Fidelity Lock with Reference IDs;
- communication hierarchy;
- visual direction options with Reference Feasibility and Fidelity Risk;
- Reference Image Usage Plan;
- layout blueprint;
- reference-based text-free generation or composition prompt;
- exact confirmed copy plan;
- Side-by-side Reference QA, revisions, and final status;
- final visual variants when capability and required approved assets are available.

## Examples

These files are optional validation artifacts, not required runtime inputs. Normal use must work with repository-based inputs, directly attached inputs, or both.

Use [examples/NORI-test-case.md](examples/NORI-test-case.md) as the no-Product-Reference negative test. It must remain in Planning-only Mode.

Use [examples/reference-backed-test-spec.md](examples/reference-backed-test-spec.md) as the specification for a future positive test. It is not runnable until legitimate approved reference assets are supplied; do not create fake product images to satisfy it.
