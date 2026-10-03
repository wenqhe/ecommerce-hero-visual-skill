# Final Assignment Runbook

Use this runbook when the final assignment product, brand, copy, and campaign information are released.

## 1. Collect Real Assignment Inputs

Record the confirmed product name, brand, audience, campaign objective, approved claims, price, dates, CTA, output ratios, and required languages. Mark every unresolved field as `Unknown` rather than filling it from inference.

## 2. Prepare `input-manifest.yaml`

Copy `input-manifest.example.yaml` to `input-manifest.yaml`. The working manifest is local and git-ignored; do not commit it. The public `input-manifest.example.yaml` is only a template and is never evidence by itself. Add only confirmed text inputs and real local asset paths. Assign stable `PR`, `PD`, `BA`, `SR`, and `LR` IDs where applicable. Do not declare assets that are not supplied.

## 3. Place Local Reference Assets

- Product images and detail views: `inputs/product-images/`
- Official logos and brand assets: `inputs/brand-assets/`
- Style references: `inputs/style-references/`
- Layout references: `inputs/layout-references/`

These real assignment inputs remain local and git-ignored. Style References may affect approved style properties only; Layout References may affect layout principles only. Neither may supply product facts.
Directly attached Codex images are also valid inputs. Repository files and attachments must be normalized into the same Reference Asset Inventory.

## 4. Pre-generation Validation

Run the Skill workflow before proposing a visual. Verify every declared asset path and classify each reference as `Present`, `Missing`, or `Unavailable`. Only `Present` assets are usable evidence; `Missing` and `Unavailable` assets are not evidence. Build the Reference Asset Inventory, Product Reference Analysis, evidence-conflict list, Production Mode, Product Fidelity Lock, communication / visual strategy, selected direction, Reference Image Usage Plan, and Layout Blueprint.

Do not enter Reference-backed Fidelity Mode without at least one usable approved Product Reference Image. If it is absent, continue in Planning-only Mode and finish with `BLOCKED`.

Create a pre-generation handoff containing:

- Reference Asset Inventory;
- evidence conflicts and unresolved blockers;
- Production Mode;
- Product Fidelity Lock;
- selected direction and risk assessment;
- Reference Image Usage Plan;
- Layout Blueprint;
- `READY FOR TEXT-FREE PRODUCTION` or `BLOCKED`;
- outstanding blockers.

If the handoff is `BLOCKED`, stop before text-free production. Proceed to text-free production only when the handoff is `READY FOR TEXT-FREE PRODUCTION`.

## 5. Text-free Production

Prefer approved product cutouts or original product pixels composited over a separately generated product-free, text-free background. Keep product pixels protected from background grading. Use reference-guided generation only when fidelity remains verifiable.

## 6. Product Composition

Preserve the locked silhouette, proportions, visible structures, markings, and approved views. Do not invent hidden details, accessories, packaging, claims, or alternate views. Keep protected product areas unobscured.

## 7. Copy and Brand Composition

After the text-free output passes product-fidelity QA, add only confirmed copy. Preserve the communication hierarchy and negative space. Place official BA assets directly where appropriate; do not redraw logos or infer brand wording from metadata.

## 8. Side-by-side QA

Compare the result against every applicable PR, PD, and BA reference. Check silhouette, proportions, colors, materials, markings, structure, accessories, crop, occlusion, unsupported additions, typography, contrast, and product-first hierarchy. Record `Pass`, `Revise`, `Blocked`, or `Not Visible` with severity. Fix every Blocking or High issue and re-check.

## 9. Language Variants

Produce language variants separately when combined typography reduces clarity. Reuse the same approved product composition and re-run copy, legibility, hierarchy, and product-fidelity checks for each language. Do not invent translations for unresolved claims, brand names, or campaign terms.

Do not invent English copy when approved English wording has not been supplied; mark it unavailable or request approval.

## 10. Final Export and Validation Record

Export only the approved formats and ratios. Record final paths, manifest and asset IDs, Production Mode, Product Fidelity Lock status, QA results, revisions, unresolved limitations, and whether final visual generation actually ran. Keep local task assets, private imagery, credentials, and ignored manifests out of the public repository. Generated test visuals are validation artifacts only and do not become Skill rules.
