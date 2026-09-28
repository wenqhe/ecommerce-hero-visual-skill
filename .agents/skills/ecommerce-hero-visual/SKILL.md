---
name: ecommerce-hero-visual
description: Plan and produce ecommerce product hero visuals from supplied product imagery and verified product or campaign facts. Use for marketplace main images, campaign posters, promotional key visuals, and bilingual product variants; do not use it to create unsupported claims or generic non-product graphics.
---

# Ecommerce Hero Visual

Create commercially clear product hero visuals without changing product identity or inventing marketing facts.

## Non-negotiable Rules

- Analyze the request and evidence before generating anything.
- Treat supplied product images and confirmed product facts as the source of truth.
- Never invent or upgrade product parameters, functions, materials, prices, discounts, dates, certifications, awards, badges, promotional rules, or logos.
- Keep stylistic proposals separate from factual product claims.
- Prefer a text-free visual base first, then add typography using confirmed copy.
- Perform QA, revise material issues, and run QA again before declaring completion.

## Workflow

### 1. Analyze Inputs and Evidence

Read [references/input-schema.md](references/input-schema.md). Organize inputs as:

- confirmed facts;
- stylistic or strategic proposals;
- missing information.

Do not present an inference as a product fact. If a missing item blocks faithful generation, continue with the brief and planning work but label generation as blocked instead of filling the gap.

### 2. Lock Product Fidelity

From the supplied product reference, record the visible properties that must remain unchanged:

- silhouette and proportions;
- color and finish;
- material appearance;
- logo or label placement;
- buttons, openings, handles, lid, and other distinctive structures.

If no usable product image is available, do not claim that product fidelity has been validated and do not generate a final product visual.

### 3. Build the Communication and Visual Strategy

Define the audience, intended action, three-second takeaway, primary consumer concern, and emotional tone. Arrange confirmed content into:

1. headline or core benefit;
2. primary selling point;
3. supporting evidence;
4. price, campaign information, and CTA when supplied.

Use [references/visual-strategy.md](references/visual-strategy.md) when selecting or comparing visual directions. If the user has not chosen a direction, propose two or three concise alternatives and recommend one.

### 4. Plan and Produce in Two Stages

Create a layout blueprint for the product, negative space, headline, supporting copy, promotion, CTA, and logo when available. The product remains the primary visual focus.

Then work in this order whenever the tools allow:

1. generate or compose a text-free visual base;
2. verify product fidelity and usable negative space;
3. add only confirmed copy and supplied brand assets;
4. create separate language versions by default for bilingual work.

The visual base must not contain unrelated accessories, unsupported functional elements, fake seals, certifications, badges, logos, or marketing text.

### 5. Run QA and Iterate

Use [references/quality-checklist.md](references/quality-checklist.md). Record each material issue, revise it, and re-check the affected criteria. Completion requires either:

- no unresolved blocking or high-severity issue; or
- a clear statement that the deliverable remains blocked and what verified input is required.

Follow the detailed production gates in [references/workflow-rules.md](references/workflow-rules.md).

## Deliverables

Return the items relevant to the request:

- structured brief and evidence status;
- missing information and generation blockers;
- communication hierarchy;
- visual direction options and recommendation;
- layout blueprint;
- text-free generation or composition prompt;
- exact confirmed copy plan;
- QA findings, revisions made, and final QA status;
- final visual variants when generation capability and required source assets are available.

## Example

Use [examples/NORI-test-case.md](examples/NORI-test-case.md) as a behavioral test, not as a universal template. A reference image is intentionally absent, so a correct run completes strategy and copy planning while refusing to claim final product-fidelity validation.
