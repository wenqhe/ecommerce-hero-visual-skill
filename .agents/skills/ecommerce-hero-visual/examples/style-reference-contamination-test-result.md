# Style Reference Contamination Test Result

This is a real Style Reference input test for the V2 `ecommerce-hero-visual` workflow.

- `SR-01` exists at `inputs/style-references/style-01.jpg`.
- `PR-01` is the product identity reference.
- `BA-01` is the official brand asset.
- `PD-01` is currently unavailable; no invisible product structure is inferred from it.
- This PASS applies only to the Style Reference isolation mechanism. It does not certify missing product-detail coverage or final asset production.

## SR-01 Inspection

Reference: `SR-01`  
File: `inputs/style-references/style-01.jpg`  
Authority: `inspiration_only`

### Allowed visual information

- **Lighting:** warm amber/orange directional light, a brighter central subject area, and darker edges.
- **Atmosphere:** quiet, intimate, editorial still-life mood.
- **Background treatment:** pale warm upper background transitioning to a dark tabletop/lower field.
- **Color mood:** warm amber, soft cream, charcoal, and low-key contrast.
- **Composition mood:** portrait-oriented editorial framing, generous upper negative space, layered foreground/background depth, and an off-center visual gesture.

## Content That Must Not Transfer

The following visible content in `SR-01` is not an allowed product source:

- rounded orange vessel shape;
- orange product color;
- vessel lid/opening structure;
- hand holding the vessel;
- dark bowl;
- candle and flame;
- any hand, bowl, candle, or other accessory;
- `HEI PING` text or logo;
- red printed marking on the orange vessel;
- inferred material, function, size, or product category;
- product interaction or usage scenario;
- exact object arrangement or copied composition;
- any product fact suggested by the scene.

## Boundary Check

| Check Item | Source Reference | Allowed Transfer | Forbidden Transfer | Observed Result | Status |
|---|---|---|---|---|---|
| Product silhouette | PR-01 | Use the approved tall rounded bottle silhouette with the right-side loop handle | SR-01 vessel shape or any reshaped bottle silhouette | The product remains the approved PR-01 image/cutout; SR-01 does not define silhouette | Pass |
| Product proportions | PR-01 | Preserve PR-01 body, cap, handle, and base proportions | SR-01 object proportions or changes made to match its vessel | The proposed layout scales the complete PR-01 product uniformly | Pass |
| Product color | PR-01 | Preserve the warm ivory body and dark green top, handle, and marking | Transfer SR-01 orange color or recolor the product to amber/charcoal | SR-01 color mood is confined to the background/light treatment; product pixels retain PR-01 colors | Pass |
| Product structure | PR-01 / PD references | Preserve visible PR-01 cap segmentation, loop handle, and base boundary | SR-01 opening, lid, rim, or unverified structure | No SR-01 structure is used. PD-01 is unavailable, so no extra detail is inferred | Pass |
| Logo and markings | BA-01 / verified PR evidence | Place official BA-01 directly and retain verified PR-01 product marking | Transfer `HEI PING`, the red SR-01 marking, or redraw a logo with a model | BA-01 remains the official logo source; no SR-01 typography or marking transfers | Pass |
| Accessories | SR-01 is not an accessory source | None, except approved product pixels and separately generated background elements | Hand, bowl, candle, flame, or other SR-01 objects | The strategy does not add these objects as product accessories or product context | Pass |
| Product facts | PR-01, manifest text inputs, verified PD evidence only | Use confirmed copy and visible reference evidence | Infer insulation, capacity, material, function, size, or use case from SR-01 | No product fact is derived from SR-01 | Pass |
| SR-01 scope | SR-01 | Affect only lighting, atmosphere, background treatment, color mood, and abstract composition mood | Affect product identity, shape, color, logo, cap, structure, accessories, or facts | The strategy treats SR-01 as inspiration-only and separates it from the product layer | Pass |
| Background color grading | SR-01 + protected PR-01 layer | Apply warm mood and tonal treatment to the generated background layer | Apply a global grade that shifts bottle ivory/green pixels or logo color | A protected product mask and separate background grading rule preserve product pixels | Pass |

## Reference Responsibilities

- **PR-01:** sole source for product silhouette, proportions, visible colors, visible cap/handle structure, and verified product-facing markings.
- **BA-01:** sole official logo asset for independently placed brand identity; it must be used directly and not regenerated.
- **SR-01:** optional inspiration for lighting, atmosphere, background treatment, color mood, and high-level composition mood only.

The proposed visual strategy uses approved PR-01 pixels/cutout, a separately generated text-free background, composition, and direct BA-01 placement. The hand, vessel, bowl, candle, typography, and literal object arrangement from SR-01 are excluded.

## Protected Product Mask Rule

Background generation and color grading must operate on a separate background layer. The approved PR-01 product pixels must be isolated by a protected product mask before compositing. No global filter, relighting pass, or color grade may recolor the bottle body, green cap/handle, product marking, or directly placed BA-01 logo.

## Test Scope and Result

- This is a real Style Reference input test; `SR-01` is an actual file, not a template entry.
- `PD-01` is currently unavailable, so no invisible lid, interior, underside, material, or other structure was guessed.
- The PASS confirms only that Style Reference information is isolated from product identity and product facts.
- It does not confirm complete multi-view product coverage or final image generation readiness.

**STYLE REFERENCE CONTAMINATION TEST: PASS**
