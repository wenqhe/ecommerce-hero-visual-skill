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
- Applicable references:
- Product Fidelity Lock dependency:

The record must be retained with the Draft Layout Blueprint and referenced by
the Pre-generation Handoff.

### Results

| Criterion | Status | Observation | Proposed correction |
|---|---|---|---|
| Product scale adequacy | Calibrated / Revise / Not Applicable |  |  |
| Typography hierarchy strength | Calibrated / Revise / Not Applicable |  |  |
| Product / copy balance | Calibrated / Revise / Not Applicable |  |  |
| Empty-space efficiency | Calibrated / Revise / Not Applicable |  |  |
| Grounding | Calibrated / Revise / Not Applicable |  |  |
| Information grouping | Calibrated / Revise / Not Applicable |  |  |
| Mobile-thumbnail clarity | Calibrated / Revise / Not Applicable |  |  |
| Visual reading order | Calibrated / Revise / Not Applicable |  |  |

Add applicable ARCHETYPE-CONDITIONAL and REFERENCE-DEPENDENT criteria without
forcing irrelevant elements into the design.

### Calibration Decision

- Applicable CORE Revise items:
- Conditional Revise items:
- Layout Blueprint revision required: Yes / No
- Commercial calibration status:

## Revision Loop

If any applicable CORE diagnostic is `Revise`:

1. identify the commercial layout problem;
2. revise the Layout Blueprint;
3. rerun the affected calibration checks.

Do not proceed to the Pre-generation Handoff with unresolved applicable CORE
`Revise` items. Conditional `Revise` items should be corrected when relevant
to the selected direction. Record each revision cycle and rerun the affected
checks. `Not Applicable` does not block readiness.

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
