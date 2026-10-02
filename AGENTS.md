# AGENTS.md

## Project purpose

This repository contains a reusable Codex skill for reference-backed ecommerce product hero-visual design.

## Mandatory skill usage

For ecommerce product hero visuals, product campaign posters, marketplace main-image design, or bilingual product key visuals, use ecommerce-hero-visual and follow its workflow before proposing or generating a final visual.

Treat verified product facts and approved reference assets as source-of-truth inputs.

The five reference asset types are:

- Product Reference Image
- Product Detail Reference
- Brand Asset
- Style Reference
- Layout Reference

Style Reference and Layout Reference are never product-fact sources. Layout Reference may influence only composition, information density, visual hierarchy, text/product balance, and negative-space planning. It must not be copied as a design and must not influence product shape, color, material, logo, features, accessories, or facts.

Do not invent or upgrade:

- product claims or functions
- product shape, structure, color, material, or accessories
- certifications or awards
- prices, dates, discounts, or promotional rules
- brand logos or product markings

Do not enter final product-fidelity generation without an approved Product Reference Image. Planning-only work may continue, but the final visual must remain Blocked.

Prefer approved product cutouts or original product pixels combined with a separately generated text-free background. Use reference-guided generation only when appropriate and when product identity can be preserved. Never reconstruct a real product from text alone.

Use official Brand Assets directly where possible, especially logos. Do not ask a generation model to redraw an official logo.

Run Side-by-side Reference QA before declaring a final visual complete. Resolve every Blocking or High fidelity issue and re-check the output.

## Repository structure

- Skill: .agents/skills/ecommerce-hero-visual/
- Main instructions: .agents/skills/ecommerce-hero-visual/SKILL.md
- Reference asset workflow: .agents/skills/ecommerce-hero-visual/references/reference-image-workflow.md
- Other references: .agents/skills/ecommerce-hero-visual/references/
- Negative test: .agents/skills/ecommerce-hero-visual/examples/NORI-test-case.md
- Reference-backed test specification: .agents/skills/ecommerce-hero-visual/examples/reference-backed-test-spec.md
