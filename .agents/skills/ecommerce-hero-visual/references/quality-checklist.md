# Quality Checklist

Use Pass, Revise, Blocked, or Not Visible for Product Fidelity and other
existing QA items. A category is Blocked when required source evidence is
unavailable. Commercial Layout Calibration and its rendered commercial
recheck use the separate statuses `Calibrated`, `Revise`, and `Not Applicable`.
Do not mark a final visual complete while a Blocking or High issue or an
applicable rendered commercial CORE `Revise` remains.

## Reference Intake and Traceability

- Does every supplied reference have a stable Reference ID?
- Is each asset classified as PR, PD, BA, SR, or LR?
- Are authority, approved use, prohibited use, and limitations recorded?
- Is every reference included in the Reference Image Usage Plan or explicitly marked unused?
- Are conflicts and Unknown attributes recorded rather than inferred?

## Production Mode

- Is Reference-backed Fidelity Mode supported by at least one usable approved PR asset?
- If no usable PR exists, is the work correctly limited to Planning-only Mode?
- Is any concept mockup clearly labeled non-fidelity?

## Side-by-side Product Fidelity

Compare the output directly with applicable PR and PD assets:

- silhouette and overall proportions;
- visible color and finish;
- material appearance;
- logo, label, and printed-marking content and placement;
- controls, buttons, openings, ports, handles, lids, hinges, seams, and joints;
- number and arrangement of visible parts;
- visible accessories;
- camera angle and supported view;
- product crop and occlusion;
- unsupported additions or missing structures;
- whether an Unknown area was invented.

For every mismatch, record the Reference IDs, output observation, status, severity, and correction.

## Brand Asset Fidelity

- Are official logos and wordmarks taken directly from approved BA assets where possible?
- Has any generation model redrawn, misspelled, distorted, or invented a brand mark?
- Do brand colors and typography follow the supplied guidance?
- Are Brand Assets placed without covering critical product details?

## Style and Layout Isolation

- Did SR assets transfer only approved mood, lighting, background treatment, color atmosphere, or texture?
- Did LR assets transfer only composition, information density, visual hierarchy, text/product balance, or negative-space planning?
- Did SR or LR introduce a product shape, color, material, logo, feature, accessory, fact, price, claim, or packaging element?
- Was an SR or LR design copied too closely instead of being abstracted into principles?

## Evidence and Copy Accuracy

- Are all product claims traceable to confirmed input?
- Are price, discount, dates, CTA, certifications, and promotional rules exact?
- Are strategic proposals clearly separated from facts?
- Is bilingual copy equivalent in meaning without adding claims?
- Is every displayed text item confirmed, and has no unconfirmed substitute copy been added for layout reasons?

## Communication and Composition

- Can the viewer identify the product and core benefit in about three seconds?
- Is the product the primary focus?
- Is hierarchy clear and concise?
- Is promotion visible without overpowering the product?
- Is typography readable with sufficient contrast and spacing?
- Is negative space intentional?
- Do props and visual effects remain relevant and non-misleading?
- Does the output comply with the canvas and ecommerce surface requirements?

## Rendered Commercial Layout Recheck

After actual product composition and typography, re-check only commercial
properties that can change during rendering. Use exactly `Calibrated`,
`Revise`, or `Not Applicable` for this subsection. This rendered recheck is
authoritative for the final image and does not replace the pre-generation
Commercial Layout Calibration or Side-by-side Reference QA.

- product scale and visual prominence;
- typography hierarchy;
- product / copy balance;
- empty-space efficiency;
- grounding;
- information grouping;
- mobile-thumbnail clarity;
- visual reading order.

At full size, visually check the complete type hierarchy defined in workflow
Gate 10, including middle-tier prominence; readable text can still be too weak.
Check module rhythm, spacing within / between groups, coordinated price / date /
CTA placement, and whether scene structural lines disrupt information grouping.
Verify related separators, dots, and button backgrounds stayed aligned after moves.

Do not treat a pre-generation blueprint status as proof that the rendered
image has passed. Recheck contrast, scale, occlusion, and grounding on the
actual composition. Inspect a consistent reduced-size thumbnail and record
the actual preview evidence for `Mobile-thumbnail clarity`; no actual
thumbnail inspection means final commercial completion is forbidden. Reuse the
criterion-specific evidence rules in the calibration reference: repeat the
Largest Effective Product Scale counterfactual for rendered product
scale/prominence; verify the actual purpose of every major empty-space region;
identify the actual Primary message, Secondary / supporting information, and
Commercial anchor when applicable; and verify materially distinct typography
hierarchy at rendered size. For typography, also apply the Largest Effective
Primary Message Scale counterfactual: if materially increasing the primary
message visual scale while preserving product dominance, safe boundaries,
intentional line breaks, supporting-information grouping, and commercial-anchor
clarity would improve immediate commercial recognition, mark typography
`Revise`; if further enlargement would materially damage one of those
relationships, `Calibrated` requires explicit evidence. This evaluates visual
prominence, not merely readability. In the reduced-size thumbnail, prioritize
immediate recognition of the headline / primary message, product, and price when
present; supporting modules should retain hierarchy, but every secondary text item
need not be readable word for word. If the primary message is technically readable but
visually collapses into ordinary supporting copy, mark typography `Revise`.
If rendered bilingual density reduces useful typography or product prominence,
mark typography `Revise`. Rendered evidence is authoritative when it
contradicts the Blueprint. For every applicable
rendered CORE criterion, record Status, Observation, Evidence, and why no
material revision is needed or the required action. Generic evidence such as
“product is visible”, “headline is readable”, “there is breathing room”, or
“shadow exists” is insufficient for `Calibrated`. Do not duplicate the
complete pre-generation calibration record here.

For rendered `Grounding`, record Status, Observation, Evidence, and why no
material revision is needed or the required action. Verify:

- physical meeting of the product and intended support;
- contact-shadow origin at the actual contact region;
- darkest local shadow consistency with contact;
- natural softness increase away from contact;
- cast-shadow behavior and light compatibility when directional light applies;
- support-plane perspective and local product / scene scale;
- edge integration without a sticker or cutout halo;
- believable perceived physical weight.

A visible support gap, detached shadow, material lighting incompatibility, or
pasted perspective / scale relationship is `Grounding = Revise`. Generic
evidence such as “a floor exists”, “the product will have a shadow”, or “the
product is on the table” is insufficient for `Calibrated`. Do not force an
intentionally suspended product onto a support plane; require explicit,
coherent suspension instead, without inventing wires, stands, mounts, or
hidden support hardware.

Typography Runtime supplies font measurements, conflicts, and contrast-risk
evidence; non-overlapping textbbox, no contrast warnings, or exit code 0 cannot
establish `COMMERCIAL LAYOUT PASSED`. Visual approval requires information
prominence, spatial relationships, module rhythm, and actual thumbnail inspection.
Keep findings and parameter corrections in the existing Layout Realization Record.

If any applicable rendered commercial CORE item is `Revise`:

1. identify the layout problem;
2. revise the responsible layout parameters, composition, typography, or background;
3. rerender the visual;
4. repeat the rendered commercial recheck.

The visual is not complete until no applicable rendered commercial CORE item
remains `Revise`. Product Fidelity QA remains independent and authoritative.

## Commercial Completion Status

Report exactly one commercial completion status separately from Product
Fidelity QA:

- `COMMERCIAL LAYOUT PASSED` — visual recheck at full size and thumbnail is complete and no applicable rendered commercial CORE item is `Revise`;
- `COMMERCIAL LAYOUT REQUIRES REVISION` — at least one applicable rendered commercial CORE item is `Revise`;
- `BLOCKED` — required evidence or a required workflow artifact is missing or prevents correction.

## Severity

- Blocking: product identity changed, a product structure or fact was invented, the wrong product or logo appears, or no valid PR supports the output;
- High: major proportion, color, material, marking, control, part, accessory, or view mismatch;
- Medium: visible integration, lighting, crop, or local-detail issue that reduces credibility without changing identity;
- Low: minor polish issue that does not affect product truth or communication.

## Revision Record

For every Revise item, record:

- issue and severity;
- Reference IDs;
- affected output area;
- likely cause;
- correction made;
- re-check result.

## Completion Rule

Completion requires:

- no unresolved Blocking or High issue;
- no unresolved applicable rendered commercial CORE `Revise`;
- no invented product fact or structure;
- a completed Side-by-side Reference QA record;
- a completed rendered commercial-layout recheck and commercial completion status;
- or an explicit `BLOCKED` status explaining which verified input or required artifact is missing.
