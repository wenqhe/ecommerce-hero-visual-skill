# Commercial Layout Calibration

## Purpose

Use this diagnostic after a recorded Draft Layout Blueprint exists and before
the Pre-generation Handoff. It evaluates intended commercial behavior without
creating a fixed template or numerical scoring system. A missing Blueprint
means calibration cannot run.

## Benchmark Boundary

Research benchmark observations may inform general layout reasoning only.
They are not runtime inputs, required files, Product References, or Layout
References. Do not load them automatically or derive product facts, brands,
claims, prices, copy, product structures, or distinctive compositions from
them.

Product truth remains governed by approved Product Reference Images, Product
Detail References, confirmed facts, and the Product Fidelity Lock.

Do not introduce fixed occupancy percentages, product scales, coordinates,
font sizes or weights, crop values, shadow values, CTA treatments, or product
positions.

## Calibration Statuses

Use exactly one status for each applicable diagnostic:

- `Calibrated`
- `Revise`
- `Not Applicable`

`Not Applicable` is primarily for a diagnostic that genuinely does not belong
to the selected archetype or task. Do not add cards, copy, prices, CTAs, or
other elements merely to make a criterion applicable.

The Commercial Layout Calibration Record is a required retained artifact.
If it is missing, set `PRE-GENERATION STATUS = BLOCKED` and do not begin
generation. Do not silently replace the record with a summary sentence.

## Diagnostic Classifications

### CORE

- product scale adequacy;
- typography hierarchy strength;
- product / copy balance;
- empty-space efficiency;
- grounding;
- information grouping;
- mobile-thumbnail clarity;
- visual reading order.

CORE classifications remain CORE in every archetype profile.

### ARCHETYPE-CONDITIONAL

- headline scale adequacy;
- commercial information density;
- key-number dominance;
- CTA prominence;
- price prominence;
- crop aggressiveness;
- multi-product hierarchy.

Evaluate these only when relevant to the selected commercial direction.

### REFERENCE-DEPENDENT

- product completeness.

Evaluate product completeness against the applicable Product Reference Image,
Product Fidelity Lock, and intended supported view. Benchmark norms cannot
define completeness.

## Archetype Profiles

These are calibration profiles, not fixed layout templates.

### Clean Product Hero

- Typical priority: product recognition and restrained communication.
- Common concern: excessive emptiness or weak grounding.
- Priority CORE checks: product scale, empty-space efficiency, grounding,
  mobile-thumbnail clarity.
- Common conditional checks: headline scale, information density, crop.

### Feature-led Hero

- Typical priority: product plus evidence-backed differentiation.
- Common concern: callout, key-number, and support-copy competition.
- Priority CORE checks: information grouping, hierarchy, reading order.
- Common conditional checks: key-number dominance, density, crop.

### Lifestyle Hero

- Typical priority: context and use occasion without losing product focus.
- Common concern: the scene becoming more prominent than the product.
- Priority CORE checks: product scale, grounding, thumbnail clarity.
- Common conditional checks: crop aggressiveness, density.

### Action / Brand Campaign

- Typical priority: campaign mood and memorability.
- Common concern: oversized campaign expression reducing product inspection.
- Priority CORE checks: product / copy balance, reading order, thumbnail
  clarity.
- Common conditional checks: headline scale, crop.

### Secondary Detail / Information Card

- Typical priority: efficient product and specification scanning.
- Common concern: documentation-like density.
- Priority CORE check: information grouping.
- Common conditional checks: crop aggressiveness, commercial density.

### Price / Promotion-led Hero

- Typical priority: offer visibility while preserving product recognition.
- Common concern: price, badges, or promotion overpowering the product.
- Priority CORE checks: hierarchy, product / copy balance, reading order.
- Common conditional checks: price prominence, CTA prominence, density.

### Multi-product / Bundle Hero

- Typical priority: clear grouping with an intentional primary product.
- Common concern: equal visual weight and ambiguous reading order.
- Priority CORE checks: product scale, hierarchy, reading order.
- Common conditional checks: multi-product hierarchy, crop, density.

Profile notes may identify priority CORE checks, but must not relabel any CORE
diagnostic as conditional.

## Calibration Record

### Context

- Record status:
- Selected archetype:
- Canvas / channel:
- Draft Layout Blueprint:
- Product Lighting and Contact Profile:
- Support Plane and Contact Plan:
- Applicable references:
- Product Fidelity Lock dependency:

The record must be retained with the Draft Layout Blueprint and referenced by
the Pre-generation Handoff.

### Results

Every applicable pre-generation CORE result must record Status, Observation,
Evidence, and why no material revision is needed or the required action.
Evidence must be specific to the Blueprint phase; “product is visible”,
“headline is readable”, “there is breathing room”, and “shadow exists” are
not sufficient evidence for `Calibrated`.

| Criterion | Status | Observation | Evidence | Why no material revision is needed / required action |
|---|---|---|---|---|
| Product scale adequacy | Calibrated / Revise / Not Applicable |  |  |  |
| Typography hierarchy strength | Calibrated / Revise / Not Applicable |  |  |  |
| Product / copy balance | Calibrated / Revise / Not Applicable |  |  |  |
| Empty-space efficiency | Calibrated / Revise / Not Applicable |  |  |  |
| Grounding | Calibrated / Revise / Not Applicable |  |  |  |
| Information grouping | Calibrated / Revise / Not Applicable |  |  |  |
| Visual reading order | Calibrated / Revise / Not Applicable |  |  |  |

Add applicable ARCHETYPE-CONDITIONAL and REFERENCE-DEPENDENT criteria without
forcing irrelevant elements into the design.

### Pre-generation Thumbnail Risk Estimate

This is a Blueprint-level risk field, not a Calibration status. Record the
planned product prominence risk, planned primary-message prominence risk,
planned commercial-anchor prominence risk, and planned information-density
risk. Do not assign `Calibrated`, `Revise`, or `Not Applicable` to
`Mobile-thumbnail clarity` before rendering.

### Evidence Requirements

#### Largest Effective Product Scale

Before `Product scale adequacy = Calibrated`, record whether the product is a
first-order or clear co-primary visual anchor; whether it could be materially
enlarged while preserving the Product Fidelity Lock, required copy zones,
protected product areas, and canvas safety; and whether enlargement would
materially improve commercial prominence or reduced-size recognition. Use a
counterfactual comparison. If meaningful enlargement is feasible and would
materially improve the hero, mark `Revise`. Do not use a universal occupancy
percentage or fixed size.

#### Functional Empty Space

The Draft Layout Blueprint must assign each major region a purpose: product,
primary communication, supporting information, commercial anchor / price /
CTA, intentional separation, or intentional atmosphere. A materially large
region without a clear commercial or compositional function is `Revise`.
“Breathing room” is evidence only when the separation or improvement it
provides is recorded.

#### Grounding Evidence

`Grounding` remains an existing CORE diagnostic and uses the existing
`Calibrated`, `Revise`, or `Not Applicable` statuses. Do not create a separate
Scene Integration status. Distinguish the evidence internally as:

- **Contact integrity:** support-plane contact, intended contact region,
  contact / ambient-occlusion shadow origin, and perceived physical weight;
- **Scene compatibility:** lighting direction, shadow direction and softness,
  contrast, color-temperature compatibility, perspective, local scene scale,
  and edge integration / sticker effect.

Before `Grounding = Calibrated`, the record must reference a compatible Product
Lighting and Contact Profile, an explicit support relationship or intentional
suspension, a plausible contact plan, plausible scene perspective and local
scale, compatible lighting direction / softness / contrast / color-temperature
character, and a credible plan to avoid a pasted or sticker effect. If either
contact integrity or scene compatibility contains a material incompatibility,
mark `Grounding = Revise`.

The support does not have to be a floor. A tabletop, shelf, pedestal, fabric,
wall-mounted context, liquid/contact environment, or another physically
plausible support may be used when compatible with the task and references.
Intentional suspension may omit floor contact, but it must be explicit in the
Blueprint and still have coherent perspective, lighting, scene scale, and
shadow behavior when applicable. Do not invent wires, stands, mounts, or hidden
support hardware.

#### Typography Hierarchy and Copy Density

Before `Typography hierarchy strength = Calibrated`, record the primary
message, supporting or secondary information, and commercial anchor when
applicable. Confirm that one message dominates, supporting copy is subordinate,
price / CTA / key number has its intended rank, levels do not collapse into
similar weight, and bilingual density does not shrink the text system or
product below a commercially useful level. A readability or size comparison
alone is insufficient evidence.

`Confirmed copy = factual authority.` `Copy presentation = hierarchy
decision.` Related confirmed facts may be grouped or subordinated without
changing meaning. Do not invent substitute copy or silently omit content the
task requires. If bilingual density materially harms product prominence,
hierarchy, or thumbnail clarity, mark typography `Revise` and recommend
separate language variants or a user-approved condensed bilingual hierarchy.
If the task explicitly requires all bilingual content in one hero, surface the
conflict and request approval rather than silently splitting it.

`Mobile-thumbnail clarity` is rendered-only. Before generation, record a
separate `Thumbnail risk estimate` for planned product prominence,
primary-message prominence, commercial-anchor prominence, and likely
information-density risk. It does not receive a final calibration status until
an actual consistent reduced-size preview is inspected after rendering.

### Calibration Decision

- Applicable CORE Revise items:
- Conditional Revise items:
- Layout Blueprint revision required: Yes / No
- Commercial calibration status:

## Revision Loop

If any applicable pre-generation CORE diagnostic is `Revise`:

1. identify the commercial layout problem;
2. revise the Layout Blueprint;
3. rerun the affected calibration checks.

Do not proceed to the Pre-generation Handoff with unresolved applicable
pre-generation CORE `Revise` items. `Mobile-thumbnail clarity` is excluded
from this pre-generation decision because it is rendered-only; its
`Thumbnail risk estimate` must have no material unresolved risk. Conditional
`Revise` items should be corrected when relevant to the selected direction.
Record each revision cycle and rerun the affected checks. `Not Applicable`
does not block readiness.

### Rendered Evidence Authority

After production, inspect actual rendered evidence for product prominence,
typography hierarchy, product / copy balance, empty-space efficiency,
grounding, information grouping, visual reading order, and a consistent
reduced-size thumbnail for `Mobile-thumbnail clarity`. Rendered evidence is
authoritative when it contradicts the Blueprint. Apply the same criterion-
specific evidence logic to the actual render:

- For rendered `Grounding`, record Status, Observation, Evidence, and why no
  material revision is needed or the required action. Evidence must address
  whether the product meets its intended support, whether the contact shadow
  originates at the actual contact region, whether the darkest local shadow is
  consistent with contact, whether softness increases naturally away from
  contact, whether directional cast-shadow behavior is compatible when
  applicable, whether support-plane perspective agrees with placement, whether
  local product / scene scale is plausible, whether edges avoid a sticker or
  cutout halo, and whether the product has believable physical weight.
- A visible product-support gap, detached shadow, material lighting
  incompatibility, or pasted perspective / scale relationship is `Revise`.
- Generic evidence such as “a floor exists”, “the product will have a shadow”,
  or “the product is on the table” is insufficient for `Calibrated`.

- For rendered product scale / prominence, repeat the `Largest Effective
  Product Scale` counterfactual. Ask whether the product could be materially
  enlarged while preserving the Product Fidelity Lock, required copy zones,
  protected product areas, and canvas safety, and whether enlargement would
  materially improve commercial prominence or reduced-size recognition. If
  both are true, mark the rendered product scale criterion `Revise`.
- For rendered empty-space efficiency, inspect each major canvas region and
  verify a product, primary communication, supporting-information,
  commercial-anchor, intentional-separation, or intentional-atmosphere
  function. A materially large region with none of these functions is
  `Revise`.
- For rendered typography hierarchy, identify the Primary message,
  Secondary / supporting information, and Commercial anchor when applicable.
  Verify that the hierarchy remains materially distinct at the actual
  rendered size. If bilingual density forces typography or product prominence
  below a commercially useful level, mark typography `Revise`.
- Generic rendered evidence such as “product is visible”, “headline is
  readable”, “there is breathing room”, or “shadow exists” is insufficient
  for `Calibrated`.

Without actual thumbnail inspection, final commercial completion is forbidden.
Any applicable rendered CORE `Revise` requires:

`revise -> rerender -> recheck`

and keeps the commercial result at `COMMERCIAL LAYOUT REQUIRES REVISION`
until all applicable rendered CORE items clear.

Commercial calibration cannot override the Product Fidelity Lock or permit
unsupported product views, structures, colors, claims, or accessories.

## Abstract Enforcement Regression

Use abstract conditions only; do not encode a product, fixed scale, position,
copy, color, or other visual parameter.

| Condition | Required result |
|---|---|
| A. Calibration Record missing | `PRE-GENERATION STATUS = BLOCKED`; generation must not begin |
| B. Applicable CORE pre-generation item is `Revise` | revise the Draft Layout Blueprint, rerun affected checks, and do not mark the Handoff READY |
| C. Applicable rendered CORE item is `Revise` | refuse final completion; revise, rerender, and recheck |
| D. No unresolved CORE `Revise` and fidelity QA is clean | final completion may proceed with a commercial completion status |
| E. Unconfirmed extra copy is proposed | reject it; use only confirmed copy or a confirmed omission decision |
| F. Largest Effective Product Scale finds feasible material enlargement | Product scale adequacy = `Revise`; revise Blueprint and rerun |
| G. A materially large region has no functional purpose | Empty-space efficiency = `Revise`; revise Blueprint and rerun |
| H. Generic evidence such as “product visible” is supplied | insufficient evidence for `Calibrated`; record specific evidence or mark `Revise` |
| I. Bilingual hierarchy collapses or forces undersizing | Typography hierarchy = `Revise`; surface language-variant or approved condensed-hierarchy resolution |
| J. No actual rendered thumbnail is inspected | final commercial completion is forbidden |
| K. Blueprint predicts success but rendered evidence is weak | rendered QA is authoritative; revise, rerender, and recheck |
| L. Rendered evidence clears all applicable CORE diagnostics and fidelity QA is clean | `COMMERCIAL LAYOUT PASSED` may be reported |
| M. Visible support gap | `Grounding = Revise` |
| N. Shadow exists but is detached from the contact region | `Grounding = Revise` |
| O. Background directional light conflicts with protected product lighting | revise background / scene integration before altering product pixels |
| P. Perspective or local scale makes the product look pasted in front of the scene | `Grounding = Revise` |
| Q. Generic grounding evidence such as “shadow exists” | insufficient for `Calibrated` |
| R. Support contact, shadow, perspective, lighting, edge integration, and perceived weight are coherent | `Grounding` may be `Calibrated` |
| S. Intentionally suspended composition has a coherent physical scene relationship | `Grounding` may be `Calibrated` without floor contact |
