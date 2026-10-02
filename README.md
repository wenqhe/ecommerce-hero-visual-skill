# Ecommerce Hero Visual Skill V2

A Codex repository-local Skill for planning and producing reference-backed ecommerce product hero visuals, campaign posters, marketplace main images, and bilingual product key visuals.

## V2 Goal

V2 treats real product reference imagery as a first-class, traceable input throughout the workflow:

Reference Asset Inventory → Product Reference Analysis → Product Fidelity Lock → Visual Strategy → Reference Image Usage Plan → Reference-based Text-free Production → Typography → Side-by-side Reference QA → Iteration

The skill preserves the useful V1 principles:

- analyze before generating;
- treat approved evidence as the source of truth;
- do not invent product facts, parameters, prices, certifications, promotions, or visual identity;
- create and verify the text-free visual before typography;
- run QA, revise, and re-check before completion.

## Five Reference Asset Types

| Type | ID prefix | Allowed influence | Important restriction |
|---|---|---|---|
| Product Reference Image | PR | Visible product identity, product layer, fidelity QA | Required for final fidelity generation; does not prove hidden details |
| Product Detail Reference | PD | Specific visible controls, ports, textures, markings, or alternate views | Does not replace a full-product PR asset |
| Brand Asset | BA | Official logo, wordmark, color, font, and brand rules | Prefer direct use; do not model-redraw official logos |
| Style Reference | SR | Approved mood, lighting, background, color atmosphere, and texture | Cannot supply product identity, facts, logos, accessories, claims, or packaging |
| Layout Reference | LR | Composition, information density, visual hierarchy, text/product balance, and negative space | Cannot affect product identity or facts and must not be copied as a design |

Every supplied asset receives a stable Reference ID, authority, approved use, prohibited use, visible coverage, and limitations.

## Production Modes

### Reference-backed Fidelity Mode

Use when at least one approved usable Product Reference Image supports the intended view. The full production and Side-by-side Reference QA workflow may proceed.

### Planning-only Mode

Use when no usable Product Reference Image is available. The skill may still produce a brief, communication strategy, directions, layout, prompt planning, and copy planning, but final product-fidelity generation remains Blocked.

A real product must never be reconstructed from text alone.

## Preferred Production Method

V2 prioritizes:

1. approved product cutout or original product pixels;
2. a separately generated text-free background;
3. direct product composition;
4. product-fidelity review;
5. confirmed typography and direct official Brand Asset placement;
6. final Side-by-side Reference QA.

Reference-guided generation is allowed only when appropriate, supported by the tool and source assets, and directly verifiable against the Product Fidelity Lock.

## Repository Structure

~~~text
.
├── input-manifest.example.yaml
├── inputs/
│   ├── README.md
│   ├── product-images/
│   ├── brand-assets/
│   ├── style-references/
│   └── layout-references/
└── .agents/
    └── skills/
        └── ecommerce-hero-visual/
            ├── SKILL.md
            ├── examples/
            │   ├── NORI-test-case.md
            │   ├── NORI-test-result.md
            │   └── reference-backed-test-spec.md
            └── references/
                ├── input-schema.md
                ├── quality-checklist.md
                ├── reference-image-workflow.md
                ├── visual-strategy.md
                └── workflow-rules.md
~~~

## How to provide images

The simplest repository-based workflow is:

1. place real product images in inputs/product-images/;
2. place official Logo and other Brand Assets in inputs/brand-assets/;
3. place optional Style References in inputs/style-references/;
4. place optional Layout References in inputs/layout-references/;
5. edit input-manifest.example.yaml or copy it to input-manifest.yaml and update the actual paths and Reference IDs;
6. invoke $ecommerce-hero-visual in Codex.

Primary Product References and Product Detail References both use inputs/product-images/. Not every Reference type is required. Only at least one valid Product Reference Image is required to enter final Reference-backed Fidelity Generation.

Images may also be attached directly to Codex instead of being stored in the repository. Repository files and directly attached images enter the same Reference Asset Inventory and follow the same authority, permission, Fidelity Lock, and QA rules.

The example manifest is a template only. Do not treat its example paths as supplied evidence unless the corresponding real files exist or are directly attached.

## Use in Codex

Open the project root and invoke ecommerce-hero-visual. Supply or attach the relevant approved reference assets and identify their roles when possible.

Request outputs such as:

1. Structured Brief;
2. Reference Asset Inventory;
3. Production Mode;
4. Missing Information;
5. Product Reference Analysis;
6. Product Fidelity Lock;
7. Communication Hierarchy;
8. Visual Directions with Reference Feasibility and Fidelity Risk;
9. Recommended Direction;
10. Reference Image Usage Plan;
11. Layout Blueprint;
12. Reference-based Text-free Generation Plan;
13. Confirmed Copy Plan;
14. Side-by-side Reference QA;
15. Iteration Record and final status.

## Tests

### Negative test: no Product Reference Image

Use .agents/skills/ecommerce-hero-visual/examples/NORI-test-case.md.

The correct behavior is Planning-only Mode. The skill must not invent the product appearance or claim final fidelity generation has passed.

The expected planning result is documented in .agents/skills/ecommerce-hero-visual/examples/NORI-test-result.md.

### Positive test: approved references present

Use .agents/skills/ecommerce-hero-visual/examples/reference-backed-test-spec.md as the fixture specification.

This repository intentionally does not include a fake product image. A positive test becomes runnable only after legitimate, approved Product Reference, Product Detail, and applicable Brand Assets are supplied.

The specification also defines Style Reference contamination, Layout Reference contamination, hidden-detail, brand-asset, and reference-conflict tests.

## Validation

The project does not include a custom validation script. When the Codex Skill Creator validator is available, run its quick_validate.py against .agents/skills/ecommerce-hero-visual/.

Also verify:

- all local Markdown links resolve;
- every Reference ID is traceable;
- NORI remains blocked from final generation;
- a future positive fixture uses real approved assets;
- SR and LR assets cannot contaminate product identity or facts;
- final completion requires Side-by-side Reference QA with no unresolved Blocking or High issue.

## Repository Safety

Do not commit private product imagery, credentials, API keys, customer data, or assets without permission to publish them. Keep test product imagery external unless it is explicitly licensed or approved for this public course repository.
