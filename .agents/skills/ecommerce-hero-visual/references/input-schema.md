# Input and Evidence Schema

Use this schema to separate verified facts, controlled reference assets, strategic proposals, and missing evidence.

## Reference Asset Inventory

Assign every supplied reference a stable ID and record:

- Reference ID;
- asset type;
- source and authority;
- file or attachment identity;
- availability status: `Present`, `Missing`, or `Unavailable`;
- visible view or coverage;
- approved use;
- prohibited use;
- quality limitations, occlusions, or uncertainty.

Verify availability before treating a declared or supplied reference as evidence. `Present` means the asset exists and can be inspected in the current run. `Missing` means the manifest or task declares it but the referenced file cannot be found. `Unavailable` means the asset is known or referenced but cannot currently be accessed or inspected. Only `Present` assets are usable reference evidence; a manifest declaration alone is not proof of existence.

Read [reference-image-workflow.md](reference-image-workflow.md) for the detailed templates and usage rules.

## Five Reference Asset Types

### Product Reference Image — PR

The authoritative full-product visual source for silhouette, proportions, visible color, finish, material appearance, major structures, markings, and product identity.

At least one usable `Present` PR asset is required for Reference-backed Fidelity Mode. If the required PR coverage is `Missing` or `Unavailable`, remain in Planning-only Mode.

### Product Detail Reference — PD

An approved close-up or alternate view used to verify specific details such as controls, ports, locks, textures, seams, labels, or structural joints. A PD asset does not replace a full-product PR asset.

### Brand Asset — BA

Official logos, wordmarks, fonts, brand colors, graphic systems, or usage rules. Use official logo assets directly when possible; do not ask a generation model to recreate them.

### Style Reference — SR

An inspiration source for explicitly approved mood, lighting, background treatment, color atmosphere, or visual texture. It must not supply product facts, product identity, logos, accessories, claims, or packaging.

### Layout Reference — LR

A reference for composition, information density, visual hierarchy, text/product balance, and negative-space planning only.

It must not influence product shape, color, material, logo, features, accessories, or facts. Extract layout principles rather than copying the reference design.

## Core Factual Inputs

Normally required for a faithful commercial output:

- brand and product name;
- confirmed selling points or approved copy;
- canvas ratio or dimensions;
- output language and file format;
- at least one approved Product Reference Image for final fidelity generation.

## Conditional Inputs

Required only when the requested visual uses them:

- Product Detail References;
- promotional price or offer;
- discount or promotional rule;
- campaign dates;
- CTA;
- certification, award, or badge artwork;
- Brand Assets and brand guidelines;
- platform safe areas or marketplace requirements;
- Style References;
- Layout References;
- approved props or environmental cues.

Never infer a conditional input because similar ecommerce designs often contain it.

## Production Modes

### Reference-backed Fidelity Mode

Use only when a usable approved PR asset is present. Product generation, composition, and final Side-by-side Reference QA may proceed.

### Planning-only Mode

Use when no usable PR asset is present. Strategy, layout, prompt planning, and copy planning may proceed, but final product-fidelity generation and final fidelity QA remain Blocked.

## Evidence Classification

Classify every material item as one of:

- Confirmed fact: explicitly supplied by the user or an authoritative written source;
- Reference evidence: directly visible in an approved PR, PD, or BA asset;
- Strategic proposal: a suggested tone, scene, layout, or expression that does not assert a new product fact;
- Missing blocker: required evidence without which faithful generation, composition, or QA cannot be completed;
- Optional enhancement: useful context that can improve the result but is not necessary for the requested stage;
- Unknown: a product attribute that is not visible or confirmed and must not be inferred.

## Source Conflicts

Do not silently choose between conflicting approved sources. Record the conflict, stop using the disputed attribute, and request or identify the authoritative source. SR and LR assets can never override PR, PD, BA, or confirmed facts.
