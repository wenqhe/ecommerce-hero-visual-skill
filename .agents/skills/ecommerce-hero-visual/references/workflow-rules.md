# Workflow and Production Gates

Use these gates in order. Do not skip a failed gate by filling missing evidence with plausible content.

## Gate 1 — Reference Asset Inventory

Inventory every supplied Product Reference Image, Product Detail Reference, Brand Asset, Style Reference, and Layout Reference. Assign stable Reference IDs and record authority, visible coverage, approved use, prohibited use, and limitations.

Style Reference and Layout Reference are never product-fact sources. Layout Reference may affect only composition, information density, visual hierarchy, text/product balance, and negative-space planning. Do not copy the reference design.

## Gate 2 — Production Mode

Enter Reference-backed Fidelity Mode only when at least one approved usable Product Reference Image supports the intended product view.

Otherwise use Planning-only Mode. Planning may continue, but final product-fidelity generation and final fidelity QA remain Blocked. A concept mockup must be explicitly requested and labeled non-fidelity.

## Gate 3 — Product Analysis and Fidelity Lock

Analyze the visible product identity in each PR and applicable PD asset. Build a Product Fidelity Lock that traces every attribute to Reference IDs.

Preserve supported silhouette, proportions, color, finish, material appearance, logo placement, markings, structures, controls, openings, interfaces, part count, and accessories. Record unclear or unseen areas as Unknown. Do not add plausible-looking features.

If approved references conflict, mark the affected attribute Conflict and stop using it until an authoritative source is identified.

## Gate 4 — Communication Accuracy and Strategy Feasibility

Complete the brief, evidence classification, communication hierarchy, and visual direction before generation.

Marketing expression may improve clarity or tone but must not strengthen, broaden, or certify an underlying fact. For example, a confirmed 12-hour claim may be restated with the same duration, but not as all-day performance, constant performance, or a certification.

For every direction, report required product view, supporting Reference IDs, Reference Feasibility, occlusion risk, and Fidelity Risk. Reject directions that require an unsupported view, hidden detail, invented accessory, or product redesign.

## Gate 5 — Reference Image Usage Plan

Map every supplied Reference ID to its intended stage and method. State what may transfer and what must not transfer.

- PR and PD may support product analysis, product-layer creation, and fidelity QA.
- BA may support direct brand composition and brand QA.
- SR may support approved mood, lighting, background, color atmosphere, or texture only.
- LR may support approved layout principles only.

Mark unused references explicitly. Do not allow SR or LR assets to override confirmed facts, PR, PD, or BA evidence.

## Gate 6 — Text-free Production

Use this priority:

1. approved product cutout or original product pixels plus a separately generated background;
2. controlled reference-guided generation only when appropriate and verifiable;
3. never final text-only reconstruction of a real product.

Generate the background without text, logos, badges, certifications, or a reconstructed target product. Composite or guide the product only according to the Reference Image Usage Plan and Product Fidelity Lock.

Check product fidelity, crop, scale, occlusion, integration, and negative space before typography.

## Gate 7 — Copy and Brand Composition

Add only confirmed copy. Use official Brand Assets directly, especially logos and wordmarks. Do not ask a generation model to redraw an official brand asset.

Keep the product as the primary visual focus. Use readable hierarchy and sufficient contrast. Create separate language versions by default when combined bilingual typography would reduce clarity.

## Gate 8 — Side-by-side Reference QA and Stop Condition

Compare the output directly against every applicable PR, PD, and BA asset. Use Pass, Revise, Blocked, or Not Visible and assign a severity to every mismatch.

For each Blocking or High issue:

1. record the Reference IDs and affected attribute;
2. identify whether the cause is generation, composition, crop, lighting, copy, or asset misuse;
3. revise the asset, prompt, direction, layout, or composition method;
4. repeat the side-by-side check.

Stop only when no Blocking or High issue remains, or when missing verified input prevents correction. In the latter case, state the blocker and do not describe the output as final.

## Commercial Clarity

Across all gates, prioritize fast product recognition, concise hierarchy, readable type, and a clear action over decorative complexity. Props, scenes, style references, and layout references must support communication without obscuring, altering, or replacing the product.
