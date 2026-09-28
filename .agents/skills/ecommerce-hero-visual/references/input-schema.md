# Input and Evidence Schema

Use this schema to separate verified inputs from optional context and missing evidence.

## Core Inputs

Normally required for a faithful product visual:

- product reference image or approved product cutout;
- brand and product name;
- confirmed selling points or approved copy;
- canvas ratio or dimensions;
- output language and file format.

If the task is planning-only, the product image may be absent, but final product generation and fidelity QA remain blocked.

## Conditional Inputs

Required only when the requested visual uses them:

- promotional price or offer;
- discount or promotional rule;
- campaign dates;
- CTA;
- certification, award, or badge artwork;
- logo files and brand guidelines;
- platform safe areas or marketplace requirements.

Never infer a conditional input merely because similar ecommerce designs often contain it.

## Helpful Context

- target audience and use scenario;
- campaign goal;
- brand tone and colors;
- preferred or prohibited visual styles;
- product color variants;
- approved props or environmental cues.

## Evidence Classification

Classify every material item as one of:

- **Confirmed fact:** explicitly supplied by the user or visible in an approved source asset.
- **Strategic proposal:** a suggested tone, scene, layout, or wording treatment that does not assert a new product fact.
- **Missing blocker:** required evidence without which faithful generation, composition, or QA cannot be completed.
- **Optional enhancement:** useful context that can improve the result but is not necessary for the requested stage.

When sources conflict, stop using the disputed item and ask for the authoritative version or mark the output blocked.
