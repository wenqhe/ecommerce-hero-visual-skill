# Input Assets

This directory is the repository-based input interface for the current ecommerce hero-visual task.

Only add assets that are approved for the current work and safe to store in the repository. Private or unlicensed product and brand assets should remain outside a public repository and may instead be attached directly to Codex.

## product-images/

Place real product images here, including:

- Primary Product Reference;
- Product Detail Reference;
- approved product photos from different legitimate views.

Suggested filenames:

- product-front-primary.png
- product-three-quarter.png
- product-detail-lock.png

These images are the source of truth for visible product identity. A full-product image can become a PR asset, while a detail or alternate-view image can become a PD asset.

At least one valid Product Reference Image is required before final Fidelity Generation may begin.

## brand-assets/

Place approved Brand Assets here, including:

- official Logo;
- official wordmark;
- brand color documentation;
- official graphic assets;
- brand typography or usage guidance when permitted.

Official logos and wordmarks should be used directly where possible. They must not be redrawn by a generation model.

## style-references/

Place optional references for:

- lighting;
- color tone;
- scene atmosphere;
- material atmosphere;
- photography style.

Style References may influence visual style only. They must not influence the product shape, product color, product material, product Logo, product features, product accessories, packaging, or product facts.

## layout-references/

Place optional references for:

- composition;
- information density;
- product and text balance;
- visual hierarchy;
- negative-space planning.

Layout References may influence layout only. They must not influence product identity or facts, and the reference design must not be copied directly.

## Manifest

Use input-manifest.example.yaml in the repository root as a starting point. Copy it to input-manifest.yaml for an actual task, update the file paths and metadata, and remove reference entries that are not supplied.

The example manifest is a template, not evidence that any referenced image exists.

Repository-based input is optional. Images attached directly to Codex are also valid inputs. Both methods must be normalized into the same Reference Asset Inventory before analysis or generation.
