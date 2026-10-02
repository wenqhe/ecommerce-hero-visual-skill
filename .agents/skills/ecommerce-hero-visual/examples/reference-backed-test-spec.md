# Reference-backed Positive Test Specification

## Purpose

Define the structure and acceptance criteria for a future positive test of Reference-backed Fidelity Mode.

This repository currently contains no legitimate product image fixture for this test. The test is intentionally not runnable until the user supplies approved assets. Do not generate a fake product image and present it as a real reference.

## Required Test Assets

A valid positive fixture must include:

- at least one approved full-product Product Reference Image assigned PR-01;
- at least one Product Detail Reference assigned PD-01 when critical details are not visible in PR-01;
- an official Brand Asset assigned BA-01 if the final design includes a logo or official mark;
- an optional Style Reference assigned SR-01;
- an optional Layout Reference assigned LR-01.

Each asset must have a known source, authority, approved use, prohibited use, visible coverage, and limitations.

## Test Brief Requirements

The positive test must provide:

- brand and product name;
- verified product facts and selling points;
- campaign or communication goal;
- target audience;
- canvas and output requirements;
- confirmed copy, price, dates, and CTA when used;
- the required final product view;
- any prohibited visual treatment.

## Required Reference Boundaries

- PR-01 controls visible product identity.
- PD-01 controls only the visible detail or alternate view it documents.
- BA-01 must be placed directly where possible and must not be redrawn.
- SR-01 may affect approved mood, lighting, background treatment, color atmosphere, or texture only.
- LR-01 may affect composition, information density, visual hierarchy, text/product balance, and negative-space planning only.
- SR-01 and LR-01 must not transfer product shape, color, material, logo, features, accessories, packaging, copy, or product facts.
- LR-01 must not be copied as a design.

## Required Workflow Outputs

A complete positive test must produce:

1. Structured Brief;
2. Reference Asset Inventory;
3. Reference-backed Fidelity Mode decision;
4. Product Reference Analysis;
5. Product Fidelity Lock traced to Reference IDs;
6. Missing Information and Unknown attributes;
7. Communication Hierarchy;
8. Visual Directions with Reference Feasibility and Fidelity Risk;
9. Recommended Direction;
10. Reference Image Usage Plan;
11. Layout Blueprint;
12. Reference-based Text-free Generation Plan or output;
13. Confirmed Copy Plan;
14. Side-by-side Reference QA;
15. Iteration Record and final status.

## Preferred Generation Test

The first positive test should use:

- approved product cutout or original PR pixels;
- a separately generated background without product, text, logo, badge, or certification;
- direct product composition;
- direct placement of BA-01;
- typography added only after the text-free composite passes fidelity review.

Reference-guided generation may be tested separately only when the tool supports the actual PR asset and the output remains directly comparable.

## Positive Acceptance Criteria

The test passes only if:

- all supplied assets are inventoried and referenced by ID;
- the Product Fidelity Lock is traceable to PR and PD evidence;
- the selected direction is supported by the available view;
- every reference has a defined use or is marked unused;
- the product is not reconstructed from text alone;
- official logos are not model-redrawn;
- SR and LR do not contaminate product identity or facts;
- the LR design is not copied;
- the output is compared side by side with all applicable PR, PD, and BA assets;
- no Blocking or High issue remains at completion.

## Required Boundary Tests

### Style contamination test

Use an SR asset containing a different product. The output must transfer only the approved style properties and must not inherit that product, logo, color, accessory, or packaging.

### Layout contamination test

Use an LR asset with a distinctive layout and a different product. The output may adopt only general composition, density, hierarchy, balance, and negative-space principles. It must not copy the design or inherit product content.

### Hidden-detail test

Request a direction that needs an unseen product surface. The skill must revise the direction, request an additional PR or PD asset, or mark the direction Blocked.

### Brand-asset test

Supply BA-01 and verify that the official asset is directly used rather than regenerated.

### Reference-conflict test

Supply two approved assets that disagree on a locked attribute. The skill must report Conflict and stop using the attribute until the authoritative source is identified.
