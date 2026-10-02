# Reference Image Workflow

Use this reference when one or more image, brand, style, or layout references are supplied.

## 1. Reference IDs

Use stable prefixes:

- PR-01, PR-02 for Product Reference Images;
- PD-01, PD-02 for Product Detail References;
- BA-01, BA-02 for Brand Assets;
- SR-01, SR-02 for Style References;
- LR-01, LR-02 for Layout References.

Do not refer to an asset only as the first image or the logo image once an ID has been assigned.

## 2. Reference Asset Inventory Template

| Reference ID | Type | Source and authority | Visible coverage | Approved use | Prohibited use | Limitations |
|---|---|---|---|---|---|---|
| PR-01 | Product Reference | User-approved | Record actual view | Analysis, product layer, QA | Style invention | Record occlusion or quality issues |

Every supplied asset must have an inventory row before generation begins.

## 3. Asset Permission Boundaries

### Product Reference Image

May determine only visible product identity and may be used as the product layer or as controlled generation guidance. It does not prove hidden details or written performance claims.

### Product Detail Reference

May determine the specific visible detail and alternate view it contains. Do not use a detail crop to infer overall proportions unless the full structure is visible.

### Brand Asset

May determine exact official logos, wordmarks, colors, typography, and graphic rules. Prefer direct placement of official assets. Do not redraw official logos or product marks with a generation model.

### Style Reference

May influence only explicitly approved mood, lighting, background treatment, color atmosphere, and visual texture. It must not transfer product shape, product color, product material, logos, features, accessories, packaging, copy, or claims.

### Layout Reference

May influence only composition, information density, visual hierarchy, text/product balance, and negative-space planning. It must not transfer product shape, product color, product material, product logo, product features, product accessories, or product facts. Extract principles; do not reproduce the reference design, distinctive arrangement, or proprietary visual expression.

## 4. Product Reference Analysis

For every PR and applicable PD asset, record:

- Reference ID and view;
- silhouette and overall proportions;
- visible color and finish;
- material appearance;
- logo, label, and printed-marking content and location;
- controls, buttons, openings, ports, handles, lids, hinges, seams, and joints;
- number and arrangement of visible parts;
- included or visible accessories;
- perspective and camera angle;
- occluded or cropped areas;
- attributes that remain Unknown;
- conflicts with another approved reference.

Do not convert an unclear visual observation into a confirmed product fact.

## 5. Product Fidelity Lock

Create a traceable lock before choosing the final visual direction.

| Attribute | Reference IDs | Required state | Allowed change | Forbidden change | Status |
|---|---|---|---|---|---|
| Silhouette | PR-01 | Match visible outline and proportions | Scale, placement | Stretch, structural redesign | Locked |
| Logo | PR-01, BA-01 | Use exact official asset and placement | Proportional scaling if allowed | Redraw, rewrite, invent | Locked |
| Unseen surface | None | Unknown | None | Invent hidden details | Unknown |

Use these statuses:

- Locked: clearly supported and must be preserved;
- Conditional: supported but limited by angle, resolution, or occlusion;
- Unknown: not visible or confirmed;
- Conflict: approved sources disagree and require resolution.

## 6. Production Mode Gate

Reference-backed Fidelity Mode requires at least one approved PR asset that is usable for the intended view. If the requested direction needs a view not supported by the references, revise the direction or remain Blocked.

Planning-only Mode applies when there is no usable PR asset. It may produce strategy, a layout blueprint, a reference request, background concepts, and prompt planning. It must not produce or claim a final faithful product visual.

A non-fidelity concept mockup may be created only when explicitly requested and must be labeled conceptual. It cannot pass Product Fidelity QA.

## 7. Reference Feasibility and Fidelity Risk

For every visual direction, report:

- required product view;
- supporting Reference IDs;
- whether the intended crop and orientation are supported;
- whether critical details would be hidden;
- whether the direction requires an unknown surface or feature;
- Fidelity Risk: Low, Medium, High, or Blocked.

Reject or revise a direction with Blocked risk. High risk requires a clear mitigation plan and should not be the default recommendation.

## 8. Reference Image Usage Plan

Create a plan before generation:

| Stage | Reference IDs | Method | Intended transfer | Forbidden transfer | Verification |
|---|---|---|---|---|---|
| Product analysis | PR and PD | Visual inspection | Visible product identity | Hidden details | Fidelity Lock |
| Background generation | SR and optional LR | Text-free generation guidance | Approved style and layout principles | Product identity or copied design | Background review |
| Product composition | PR | Direct cutout or original pixels | Product layer | Structural regeneration | Side-by-side QA |
| Typography | BA | Direct placement | Official brand assets | Model-redrawn logo | Brand QA |
| Final QA | PR, PD, BA | Side-by-side comparison | Verification only | None | QA record |

Every supplied reference must have a defined use or be explicitly marked unused.

## 9. Text-free Production Method Priority

### Preferred method: original product pixels plus generated background

1. Use an approved product cutout or isolate the approved product from a PR asset without redesigning it.
2. Generate the background or scene separately without product, copy, logos, badges, or certifications.
3. Composite the approved product layer into the text-free background.
4. Check silhouette, crop, scale, occlusion, lighting integration, and negative space.

This is the default because it minimizes product-identity drift.

### Conditional method: reference-guided generation

Use only when:

- the tool can accept the relevant PR assets;
- the requested view is supported;
- the product remains directly comparable to the references;
- the Product Fidelity Lock can be preserved;
- direct composition is unsuitable for a documented reason.

After generation, run strict Side-by-side Reference QA. Regenerate or switch to direct composition if product identity drifts.

### Prohibited method: text-only reconstruction

Do not reconstruct a real product using only its name, category, written description, or marketing claims. Do not generate unseen product angles or hidden details.

## 10. Brand, Style, and Layout Isolation

- BA controls official brand identity and should be directly placed where possible.
- SR controls approved style properties only.
- LR controls approved layout principles only.
- SR and LR cannot validate, contradict, or replace product facts or product imagery.
- If an SR or LR contains another product, logo, accessory, price, or copy, treat those elements as excluded content.
- Never ask for a close copy of an SR or LR design.

## 11. Handoff to QA

Provide QA with:

- the Reference Asset Inventory;
- Product Reference Analysis;
- Product Fidelity Lock;
- Reference Image Usage Plan;
- text-free output and final composed output;
- every applicable PR, PD, and BA asset;
- known Unknown, Conditional, or Conflict items.

The work is not complete until Side-by-side Reference QA has no unresolved Blocking or High issue.
