# Benchmark Layout Retrieval

## Purpose and boundary

Retrieve a small, role-labeled set of research references for comparative
layout reasoning. Benchmarks are not product, brand, claim, price, copy, or
fidelity evidence. They cannot override the Product Fidelity Lock, supply
product facts, or become layout templates. Retrieval is optional and advisory;
it is not a Benchmark Pass/Fail gate or a Commercial Layout Calibration
status.

## Task Profile

Normalize only task-supported inputs before retrieval. Use `unknown` for
unsupported values; do not infer task evidence from a benchmark. The profile
contains:

- archetype and zero or more hybrid archetype tags;
- subject model, orientation, aspect-ratio family, and product-group band;
- information-density band and headline/supporting-copy needs;
- commercial-anchor need and known anchor types;
- price/promotion, CTA, human, and environment-scene presence or need;
- grounding/support context;
- requested comparison roles: product prominence, typography/headline
  hierarchy, commercial anchor, whitespace/density, grouping, or
  grounding/scene integration.

Use the normalized JSON input contract in `scripts/select_benchmark_references.py`.
The selector performs compatibility-first metadata selection only. It does
not inspect images or make visual-quality judgments.

## Provenance and confidence legend

Each indexed field's `field_provenance` and `field_confidence` are grouped by
code and map to field names. Provenance codes follow the development contract:
`E` = explicit benchmark annotation, `M` = existing measurement or annotation
qualifier, `N` = existing note, `I` = reviewer-normalized inference, and `U`
= unknown/no safe inference. Confidence is `H` = high, `M` = medium, or `L` =
low. For each requested role, assess confidence only on the metadata fields
relevant to that role. Treat `I` and `L` cautiously; `L` or `UNKNOWN` on
required role metadata downgrades otherwise direct/close evidence to partial
and cannot establish full role coverage. A field whose value is `unknown` has
`UNKNOWN` role confidence regardless of its confidence group. Unknown is not
absence.

## Compatibility-first selection

Apply hard subject-model, product-group, and role-specific exclusions before
choosing references. Isolated-product and multi-product geometry are separate;
product-plus-human or product-plus-scene references cannot calibrate isolated
geometry; macro detail cannot calibrate full-product prominence. Unknown is
not a positive match or verified absence. Unknown orientation/aspect cannot
support geometry-dependent primary selection. Price presence alone cannot
promote a structural primary, and category similarity cannot override a
structural mismatch.

Retain exactly these contextual compatibility terms:
`DIRECT MATCH`, `CLOSE ANALOG`, `PARTIAL ANALOG`, and `NOT SUITABLE`.
Attempt one structural primary by compatible subject model, archetype or
hybrid component, orientation/aspect family, product-group status, then
communication function. If none qualifies, report no structural primary.
Among otherwise-equivalent structural candidates, use confidence on the
requested roles' relevant metadata as a late tie-break before lexical
reference ID; confidence must not outrank structural compatibility or these
primary-selection criteria.
Supporting roles may cover product prominence, typography/headline hierarchy,
commercial anchor, whitespace/density, grouping, and grounding/scene
integration. Add a reference only when it covers a real role gap with known
metadata; avoid redundant selections and do not fill a quota. Resolve
otherwise-equivalent candidates by relevant qualitative compatibility and
confidence, then lexical reference ID. Do not calculate weighted or decimal
similarity scores.

Structural-primary selection is independent of role fit. Assess every
requested role separately and retain its `DIRECT MATCH`, `CLOSE ANALOG`,
`PARTIAL ANALOG`, or `NOT SUITABLE` result; known metadata alone does not
establish compatibility. Explicitly absent required headline or supporting
copy is not positive typography/grouping evidence. Compare information-density
bands qualitatively for typography, whitespace, and grouping; a large mismatch
reduces compatibility, and unknown remains unknown. A requested grounding
context must be compared with the indexed context; a different known context
is at most partial evidence. For commercial anchors, price/promotion and CTA
are separate sub-needs when both are required. Unknown CTA is not CTA coverage,
and distinct references may cover distinct sub-needs. Role confidence is
included in each role assessment and role-evidence record; requested roles
are reported even when not suitable or uncovered.

Coverage is exactly `STRONG`, `LIMITED`, or `NONE`, and is contextual only.
`STRONG` requires a direct structural primary and role-specific direct/close
evidence for every requested role and required sub-need, without relying on
partial, unknown, or mismatched evidence. `LIMITED` means useful evidence
exists but one or more roles or sub-needs have partial, uncertain, mismatched,
or missing coverage, or no direct primary exists. `NONE` means no meaningful
compatible known evidence. Coverage never maps to a calibration status or
readiness.

## Image availability and progressive loading

The metadata index establishes candidate identity and compatibility only; it
does not establish that an image exists. Resource state for the current run is
one of:

- `BENCHMARK LIBRARY AVAILABLE`: metadata is readable and the selected images
  have been located and opened;
- `BENCHMARK METADATA ONLY`: metadata is readable but one or more selected
  images cannot be located or opened;
- `BENCHMARK LIBRARY UNAVAILABLE`: metadata cannot be used or retrieval is
  intentionally disabled.

Resolve image locators only under an explicitly supplied/mounted library or a
discoverable authorized repository-local library, using a manifest of stable
IDs to relative locators. Reject path traversal outside the selected root and
do not persist absolute machine paths. Check each selected asset in the
current run; load no unselected images. A missing or unopened image remains
metadata-only, with no image-based observation. A discrepancy between image
and metadata is recorded; the image may ground that reference's comparative
visual observation but does not silently rewrite its metadata.

Selected references use this compact record:

```text
Reference ID:
Asset availability: Present / Missing / Unavailable
Compatibility class:
Reference role:
Relevant comparative observation:
Prohibited transfer:
Evidence source: metadata only / inspected benchmark image
Metadata-image discrepancy:
```

When recording selector output, retain `role_assessments` and `role_evidence`
so a structural primary's role-specific fit and any uncovered commercial
sub-need remain visible. Do not summarize a role as covered solely because
the reference has some known metadata for it.

When evidence source is `metadata only`, report only indexed compatibility
and provenance/confidence; do not state visual observations. Selected images
may be inspected progressively after selection and availability checks.

## Evidence use and anti-copy safeguards

Use relational findings such as “comparable isolated-product references give
the primary product greater prominence relative to supporting information.”
Never transfer exact scale, coordinates, crop, typography, line breaks, color,
gradient, shadow, props, people, distinctive scenes, logos, product geometry,
claims, price, or copy. Benchmark references cannot determine product view,
silhouette, proportions, color, finish, hidden surfaces, features, or package
text. Product references remain authoritative for product identity.

Benchmark comparisons may inform Visual Strategy and explain the rationale in
the Draft Layout Blueprint. They may supplement, but never replace, the
Largest Effective Product Scale counterfactual, typography evidence,
functional empty-space explanation, information grouping, grounding evidence,
or actual rendered thumbnail inspection. A reference being typical or
atypical never automatically means `Calibrated` or `Revise`; Commercial Layout
Calibration keeps `Calibrated`, `Revise`, and `Not Applicable`. Rendered output
remains authoritative for rendered QA; benchmark similarity is never required
to pass.

## Fail-soft behavior

If the index is missing, selector unavailable/errors, library absent, selected
image missing/unreadable, metadata conflicts with an image, Task Profile has
unknown values, no structural primary exists, or no useful candidate exists,
record the applicable limitation and use metadata-only or
`BENCHMARK LIBRARY UNAVAILABLE` as appropriate. Never claim inspection of an
unopened asset. Continue Visual Strategy, Draft Layout Blueprint, Commercial
Layout Calibration, Pre-generation Handoff, production, and rendered QA using
the existing qualitative evidence. Benchmark retrieval failure or absence
alone never blocks readiness or production.
