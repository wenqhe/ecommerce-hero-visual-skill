#!/usr/bin/env python3
"""Select benchmark layout references from qualitative metadata only."""

import argparse
import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
INDEX_PATH = SCRIPT_DIR.parent / "references" / "benchmark-layout-index.json"
ROLES = (
    "product-prominence",
    "typography-headline-hierarchy",
    "commercial-anchor",
    "whitespace-density",
    "grouping",
    "grounding-scene-integration",
)
ARCHETYPES = {
    "Clean Product Hero",
    "Feature-led Hero",
    "Lifestyle Hero",
    "Action / Brand Campaign",
    "Secondary Detail / Information Card",
    "Price / Promotion-led Hero",
    "Multi-product / Bundle Hero",
}
SUBJECTS = {
    "isolated-product",
    "product-plus-human",
    "product-plus-scene",
    "multi-product",
    "macro-detail",
}
ORIENTATIONS = {"portrait", "landscape", "square"}
ASPECT_FAMILIES = {"portrait", "landscape", "square", "ultra-wide"}
GROUP_BANDS = {"single", "2-3", "3-plus", "unknown"}
DENSITIES = {"low", "moderate", "high"}
DENSITY_ORDER = {"low": 0, "moderate": 1, "high": 2}
PRESENCE = {"present", "absent", "unknown"}
GROUNDING = {
    "visible-support-plane",
    "environmental-grounding",
    "human-held",
    "suspended",
    "unknown",
}

# Hybrid components are requested for distinct comparative roles.  Keep a
# structural primary from claiming those roles solely from generic metadata
# when a task explicitly asks for another archetype component.
ARCHETYPE_ROLE_HINTS = {
    "Clean Product Hero": {
        "product-prominence",
        "whitespace-density",
        "grounding-scene-integration",
    },
    "Feature-led Hero": {
        "typography-headline-hierarchy",
        "grouping",
    },
    "Lifestyle Hero": {
        "grounding-scene-integration",
        "typography-headline-hierarchy",
    },
    "Action / Brand Campaign": {
        "typography-headline-hierarchy",
        "commercial-anchor",
    },
    "Secondary Detail / Information Card": {
        "typography-headline-hierarchy",
        "grouping",
        "commercial-anchor",
    },
    "Price / Promotion-led Hero": {
        "commercial-anchor",
    },
    "Multi-product / Bundle Hero": {
        "product-prominence",
        "grouping",
    },
}


def enum(value, allowed):
    return value if isinstance(value, str) and value in allowed else "unknown"


def normalize_profile(raw):
    raw = raw if isinstance(raw, dict) else {}
    archetype = enum(raw.get("archetype"), ARCHETYPES)
    hybrids = raw.get("hybrid_archetype_tags", [])
    if not isinstance(hybrids, list):
        hybrids = []
    hybrids = sorted({item for item in hybrids if item in ARCHETYPES})
    requested = raw.get("requested_comparison_roles", [])
    if not isinstance(requested, list):
        requested = []
    requested = list(dict.fromkeys(item for item in requested if item in ROLES))
    anchors = raw.get("commercial_anchor_types", [])
    if not isinstance(anchors, list):
        anchors = []
    anchors = sorted({item for item in anchors if isinstance(item, str) and item})
    group_status = raw.get("product_group_status")
    if group_status not in {"single-product", "multi-product"}:
        group_status = "unknown"
    return {
        "archetype": archetype,
        "hybrid_archetype_tags": hybrids,
        "subject_model": enum(raw.get("subject_model"), SUBJECTS),
        "orientation": enum(raw.get("orientation"), ORIENTATIONS),
        "aspect_ratio_family": enum(raw.get("aspect_ratio_family"), ASPECT_FAMILIES),
        "product_group_status": group_status,
        "product_group_count_band": enum(raw.get("product_group_count_band"), GROUP_BANDS),
        "information_density_band": enum(raw.get("information_density_band"), DENSITIES),
        "headline_need": enum(raw.get("headline_need"), PRESENCE),
        "supporting_copy_need": enum(raw.get("supporting_copy_need"), PRESENCE),
        "commercial_anchor_need": enum(
            raw.get("commercial_anchor_need"), {"required", "not-required", "unknown"}
        ),
        "commercial_anchor_types": anchors,
        "price_or_promotion_presence": enum(raw.get("price_or_promotion_presence"), PRESENCE),
        "cta_presence": enum(raw.get("cta_presence"), PRESENCE),
        "human_presence": enum(raw.get("human_presence"), PRESENCE),
        "environment_scene_requirement": enum(
            raw.get("environment_scene_requirement"), {"required", "not-required", "unknown"}
        ),
        "grounding_support_context": enum(raw.get("grounding_support_context"), GROUNDING),
        "requested_comparison_roles": requested,
        "geometry_comparison_required": raw.get("geometry_comparison_required") is True,
    }


def candidate_group_status(ref):
    subject = ref.get("subject_model", "unknown")
    if subject == "multi-product":
        return "multi-product"
    if subject in SUBJECTS - {"multi-product", "macro-detail"}:
        return "single-product"
    return "unknown"


def task_group_status(task):
    if task["product_group_status"] != "unknown":
        return task["product_group_status"]
    band = task["product_group_count_band"]
    if band == "single":
        return "single-product"
    if band in {"2-3", "3-plus"}:
        return "multi-product"
    if task["subject_model"] == "multi-product":
        return "multi-product"
    if task["subject_model"] in SUBJECTS - {"multi-product", "macro-detail"}:
        return "single-product"
    return "unknown"


def archetype_matches(task, ref):
    wanted = {task["archetype"], *task["hybrid_archetype_tags"]} - {"unknown"}
    candidate = {ref.get("archetype", "unknown"), *ref.get("hybrid_archetype_tags", [])}
    return bool(wanted & candidate)


def geometry_compatible(task, ref):
    if task["geometry_comparison_required"] and (
        task["orientation"] == "unknown" or task["aspect_ratio_family"] == "unknown"
    ):
        return False
    if ref.get("orientation") not in ORIENTATIONS or ref.get("aspect_ratio_family") not in ASPECT_FAMILIES:
        return False
    if task["orientation"] != "unknown" and ref.get("orientation") != task["orientation"]:
        return False
    if (
        task["aspect_ratio_family"] != "unknown"
        and ref.get("aspect_ratio_family") != task["aspect_ratio_family"]
    ):
        return False
    return True


def structural_rejection(task, ref):
    subject = task["subject_model"]
    candidate = ref.get("subject_model", "unknown")
    group = task_group_status(task)
    candidate_group = candidate_group_status(ref)
    if subject == "unknown" or candidate == "unknown":
        return "subject model is unknown"
    if candidate == "macro-detail" and subject != "macro-detail":
        return "macro-detail cannot represent whole-product structure"
    if subject != candidate:
        return "subject model is structurally incompatible"
    if group == "unknown" or candidate_group == "unknown":
        return "product group status is unknown"
    if group != candidate_group:
        return "product group status is incompatible"
    if task["geometry_comparison_required"] and not geometry_compatible(task, ref):
        return "orientation or aspect family is incompatible for geometry"
    if task["human_presence"] == "absent" and ref.get("human_presence") == "present":
        return "human-present composition cannot represent an isolated task"
    if task["environment_scene_requirement"] == "not-required" and ref.get(
        "environment_scene_presence"
    ) == "present":
        return "scene composition is outside the requested isolated context"
    return None


def primary_class(task, ref):
    if not archetype_matches(task, ref):
        return "CLOSE ANALOG"
    if geometry_compatible(task, ref):
        return "DIRECT MATCH"
    return "CLOSE ANALOG"


def hybrid_role_compatible(task, ref, role):
    """Require an explicitly requested hybrid component for its roles."""
    hybrids = set(task["hybrid_archetype_tags"])
    if not hybrids:
        return True
    role_components = {
        archetype
        for archetype in hybrids
        if role in ARCHETYPE_ROLE_HINTS.get(archetype, set())
    }
    if not role_components:
        return True
    candidate_components = {ref.get("archetype"), *ref.get("hybrid_archetype_tags", [])}
    return bool(candidate_components.intersection(role_components))


def communication_fit(task, ref, role=None):
    """Return a qualitative tie-break for the requested communication role."""
    anchor = ref.get("primary_anchor_type", "unknown")
    archetype = task["archetype"]
    hybrids = set(task["hybrid_archetype_tags"])
    if (role in {None, "typography-headline-hierarchy", "grouping"}) and (
        archetype == "Feature-led Hero" or "Feature-led Hero" in hybrids
    ):
        return {"key-number": 0, "feature-cards": 1, "feature-specification-panel": 2}.get(
            anchor, 3
        )
    if role == "commercial-anchor" and task["commercial_anchor_types"]:
        return 0 if anchor in task["commercial_anchor_types"] else 1
    return 0


def known_role(ref, role, task):
    """Whether indexed fields exist to assess a role, not whether they match."""
    if not hybrid_role_compatible(task, ref, role):
        return False
    if role == "product-prominence":
        return (
            ref.get("subject_model") == task["subject_model"]
            and candidate_group_status(ref) == task_group_status(task)
            and geometry_compatible(task, ref)
            and ref.get("product_visual_mass") in {"low", "medium", "high"}
        )
    if role == "typography-headline-hierarchy":
        return (
            ref.get("headline_presence") in {"present", "absent"}
            and ref.get("copy_density_band") in DENSITIES
            and ref.get("fragmentation") in DENSITIES
        )
    if role == "commercial-anchor":
        return ref.get("commercial_anchor_presence") in {"present", "absent"} or bool(
            ref.get("commercial_anchor_types")
        ) or ref.get("price_or_promotion_presence") in {"present", "absent"} or ref.get(
            "cta_presence"
        ) in {"present", "absent"}
    if role == "whitespace-density":
        return ref.get("copy_density_band") in DENSITIES and ref.get("fragmentation") in DENSITIES
    if role == "grouping":
        return (
            candidate_group_status(ref) != "unknown"
            and ref.get("commercial_anchor_presence") in {"present", "absent"}
        )
    if role == "grounding-scene-integration":
        return ref.get("grounding_context") in GROUNDING - {"unknown"} or ref.get(
            "environment_scene_presence"
        ) in {"present", "absent"}
    return False


def commercial_anchor_subneeds(task):
    types = set(task["commercial_anchor_types"])
    needs = []
    if task["price_or_promotion_presence"] == "present" or types.intersection(
        {"price", "price-tag", "promotion", "promotion-band"}
    ):
        needs.append("price-promotion")
    if task["cta_presence"] == "present" or "cta" in types:
        needs.append("cta")
    return needs or ["commercial-anchor"]


def role_dimensions(task, role):
    if role == "commercial-anchor":
        return commercial_anchor_subneeds(task)
    return [role]


def base_role_class(task, ref, role):
    """Classify known role evidence independently from structural-primary fit."""
    subject = task["subject_model"]
    candidate = ref.get("subject_model", "unknown")
    group_match = candidate_group_status(ref) == task_group_status(task)
    geom_match = geometry_compatible(task, ref)
    archetype_match = archetype_matches(task, ref)
    if subject == "unknown" or candidate == "unknown":
        return "PARTIAL ANALOG"
    if candidate == subject and group_match and geom_match and archetype_match:
        return "DIRECT MATCH"
    if candidate == subject and group_match and geom_match:
        return "CLOSE ANALOG"
    return "PARTIAL ANALOG"


def role_compatibility(task, ref, role, subneed=None):
    if not known_role(ref, role, task):
        return "NOT SUITABLE"
    compatibility = base_role_class(task, ref, role)
    if role == "product-prominence":
        if task["subject_model"] in {"unknown", "macro-detail"} or ref.get(
            "subject_model"
        ) != task["subject_model"]:
            return "NOT SUITABLE"
        if candidate_group_status(ref) != task_group_status(task) or not geometry_compatible(
            task, ref
        ):
            return "NOT SUITABLE"
        return compatibility
    if role == "typography-headline-hierarchy":
        if task["headline_need"] == "present":
            if ref.get("headline_presence") == "absent":
                return "NOT SUITABLE"
            if ref.get("headline_presence") != "present":
                return "PARTIAL ANALOG"
        if task["supporting_copy_need"] == "present":
            if ref.get("supporting_copy_presence") == "absent":
                return "NOT SUITABLE"
            if ref.get("supporting_copy_presence") != "present":
                return "PARTIAL ANALOG"
        task_density = task["information_density_band"]
        ref_density = ref.get("copy_density_band", "unknown")
        if task_density in DENSITIES and ref_density in DENSITIES:
            if abs(DENSITY_ORDER[task_density] - DENSITY_ORDER[ref_density]) > 1:
                return "PARTIAL ANALOG"
        elif task_density in DENSITIES:
            return "PARTIAL ANALOG"
        return compatibility
    if role == "whitespace-density":
        task_density = task["information_density_band"]
        ref_density = ref.get("copy_density_band", "unknown")
        if task_density in DENSITIES and ref_density in DENSITIES:
            if abs(DENSITY_ORDER[task_density] - DENSITY_ORDER[ref_density]) > 1:
                return "PARTIAL ANALOG"
        elif task_density in DENSITIES:
            return "PARTIAL ANALOG"
        return compatibility
    if role == "grouping":
        if task["supporting_copy_need"] == "present" and ref.get(
            "supporting_copy_presence"
        ) == "absent":
            return "PARTIAL ANALOG"
        task_density = task["information_density_band"]
        ref_density = ref.get("copy_density_band", "unknown")
        if task_density in DENSITIES and ref_density in DENSITIES and abs(
            DENSITY_ORDER[task_density] - DENSITY_ORDER[ref_density]
        ) > 1:
            return "PARTIAL ANALOG"
        return compatibility if candidate_group_status(ref) == task_group_status(task) else "PARTIAL ANALOG"
    if role == "commercial-anchor":
        types = set(ref.get("commercial_anchor_types", []))
        dimension = subneed or "commercial-anchor"
        anchor_presence = ref.get("commercial_anchor_presence", "unknown")
        if anchor_presence == "absent":
            return "NOT SUITABLE"
        if dimension == "price-promotion":
            if ref.get("price_or_promotion_presence") == "present" or types.intersection(
                {"price", "promotion-band", "price-tag"}
            ):
                return compatibility
            return "NOT SUITABLE"
        if dimension == "cta":
            if ref.get("cta_presence") == "present" or "cta" in types:
                return compatibility
            return "NOT SUITABLE"
        if anchor_presence != "present":
            return "NOT SUITABLE"
        if task["commercial_anchor_types"] and not types.intersection(
            task["commercial_anchor_types"]
        ):
            return "PARTIAL ANALOG"
        return compatibility if types else "PARTIAL ANALOG"
    if role == "grounding-scene-integration":
        requested_context = task["grounding_support_context"]
        ref_context = ref.get("grounding_context", "unknown")
        if requested_context != "unknown":
            if ref_context == requested_context:
                return compatibility
            if ref_context != "unknown":
                return "PARTIAL ANALOG"
            return "NOT SUITABLE"
        if task["environment_scene_requirement"] == "required" and ref.get(
            "environment_scene_presence"
        ) != "present":
            return "NOT SUITABLE"
        return compatibility if ref_context != "unknown" else "PARTIAL ANALOG"
    return compatibility


CLASS_ORDER = {"DIRECT MATCH": 0, "CLOSE ANALOG": 1, "PARTIAL ANALOG": 2}


ROLE_CONFIDENCE_FIELDS = {
    "product-prominence": ("subject_model", "product_group_count_band", "orientation", "aspect_ratio_family", "product_visual_mass"),
    "typography-headline-hierarchy": ("headline_presence", "supporting_copy_presence", "copy_density_band", "fragmentation"),
    "commercial-anchor": ("commercial_anchor_presence", "commercial_anchor_types", "primary_anchor_type", "price_or_promotion_presence", "cta_presence"),
    "whitespace-density": ("copy_density_band", "fragmentation"),
    "grouping": ("subject_model", "product_group_count_band", "fragmentation", "commercial_anchor_presence", "supporting_copy_presence", "copy_density_band"),
    "grounding-scene-integration": ("grounding_context", "environment_scene_presence", "subject_model"),
}
CONFIDENCE_RANK = {"H": 0, "M": 1, "L": 2}


def role_relevant_confidence_fields(task, role, subneed=None):
    if role == "product-prominence":
        fields = ["subject_model", "product_visual_mass"]
        if task["geometry_comparison_required"]:
            fields.extend(("orientation", "aspect_ratio_family"))
        if task_group_status(task) != "unknown":
            fields.append("product_group_count_band")
        return tuple(fields)
    if role == "typography-headline-hierarchy":
        fields = ["copy_density_band", "fragmentation"]
        if task["headline_need"] == "present":
            fields.append("headline_presence")
        if task["supporting_copy_need"] == "present":
            fields.append("supporting_copy_presence")
        return tuple(fields)
    if role == "commercial-anchor":
        fields = ["commercial_anchor_presence", "commercial_anchor_types"]
        if subneed == "price-promotion":
            fields.append("price_or_promotion_presence")
        elif subneed == "cta":
            fields.append("cta_presence")
        else:
            fields.append("primary_anchor_type")
        return tuple(fields)
    if role == "whitespace-density":
        return ("copy_density_band", "fragmentation")
    if role == "grouping":
        fields = ["subject_model", "product_group_count_band", "fragmentation"]
        if task["commercial_anchor_need"] == "required":
            fields.append("commercial_anchor_presence")
        if task["supporting_copy_need"] == "present":
            fields.append("supporting_copy_presence")
        if task["information_density_band"] != "unknown":
            fields.append("copy_density_band")
        return tuple(fields)
    if role == "grounding-scene-integration":
        return ("grounding_context", "environment_scene_presence", "subject_model")
    return ROLE_CONFIDENCE_FIELDS.get(role, ())


def field_confidence(ref, field):
    value = ref.get(field)
    if field not in ref or value == "unknown":
        return 3
    groups = ref.get("field_confidence", {})
    for code in ("H", "M", "L"):
        fields = groups.get(code, [])
        if isinstance(fields, list) and field in fields:
            return CONFIDENCE_RANK[code]
    return 3


def role_confidence(ref, task, role, subneed=None):
    ranks = [
        field_confidence(ref, field)
        for field in role_relevant_confidence_fields(task, role, subneed)
    ]
    worst = max(ranks, default=3)
    return {0: "H", 1: "M", 2: "L", 3: "UNKNOWN"}[worst]


def role_confidence_key(ref, task, role, subneed=None):
    fields = role_relevant_confidence_fields(task, role, subneed)
    ranks = tuple(field_confidence(ref, field) for field in fields)
    return max(ranks, default=3), ranks.count(3), ranks.count(2), ranks.count(1), ranks


def primary_role_confidence_key(ref, task):
    assessments = [
        role_confidence_key(ref, task, role, subneed)
        for role in task["requested_comparison_roles"]
        for subneed in role_dimensions(task, role)
    ]
    return tuple(sorted(assessments, reverse=True))


def rank_key(task, ref, role=None, subneed=None):
    compatibility = primary_class(task, ref) if role is None else reliable_role_class(
        task, ref, role, subneed
    )
    primary_archetype = task["archetype"] != "unknown" and ref.get("archetype") == task["archetype"]
    hybrid_archetype = ref.get("archetype") in task["hybrid_archetype_tags"]
    return (
        CLASS_ORDER.get(compatibility, 3),
        0 if primary_archetype else 1 if hybrid_archetype else 2,
        0 if geometry_compatible(task, ref) else 1,
        0 if candidate_group_status(ref) == task_group_status(task) else 1,
        communication_fit(task, ref, role),
        role_confidence_key(ref, task, role, subneed)
        if role is not None
        else primary_role_confidence_key(ref, task),
        ref.get("reference_id", ""),
    )


def reliable_role_class(task, ref, role, subneed=None):
    compatibility = role_compatibility(task, ref, role, subneed)
    if compatibility in {"DIRECT MATCH", "CLOSE ANALOG"} and role_confidence(
        ref, task, role, subneed
    ) in {"L", "UNKNOWN"}:
        return "PARTIAL ANALOG"
    return compatibility


def select(task, refs, resource_state):
    primary_candidates = [r for r in refs if not structural_rejection(task, r)]
    primary_candidates.sort(key=lambda r: rank_key(task, r))
    primary = None
    primary_ref = None
    if primary_candidates:
        ref = primary_candidates[0]
        primary_ref = ref
        role_assessments = []
        roles = []
        for role in task["requested_comparison_roles"]:
            for subneed in role_dimensions(task, role):
                status = reliable_role_class(task, ref, role, subneed)
                role_assessments.append({
                    "role": role,
                    "subneed": subneed,
                    "compatibility_class": status,
                    "confidence": role_confidence(ref, task, role, subneed),
                })
                if status in {"DIRECT MATCH", "CLOSE ANALOG"}:
                    roles.append(role)
        primary = {
            "reference_id": ref["reference_id"],
            "compatibility_class": primary_class(task, ref),
            "eligible_roles": sorted(set(roles)),
            "role_assessments": role_assessments,
        }

    dimensions = [(role, subneed) for role in task["requested_comparison_roles"] for subneed in role_dimensions(task, role)]
    evidence = {}
    if primary_ref:
        for role, subneed in dimensions:
            status = reliable_role_class(task, primary_ref, role, subneed)
            if status != "NOT SUITABLE":
                evidence[(role, subneed)] = {
                    "reference_id": primary_ref["reference_id"],
                    "compatibility_class": status,
                    "confidence": role_confidence(primary_ref, task, role, subneed),
                }
    selected = []
    for role, subneed in dimensions:
        current = evidence.get((role, subneed))
        if current and current["compatibility_class"] in {"DIRECT MATCH", "CLOSE ANALOG"}:
            continue
        candidates = [r for r in refs if (not primary_ref or r["reference_id"] != primary_ref["reference_id"])
                      and reliable_role_class(task, r, role, subneed) != "NOT SUITABLE"]
        candidates.sort(key=lambda r: rank_key(task, r, role, subneed))
        if not candidates:
            continue
        ref = candidates[0]
        status = reliable_role_class(task, ref, role, subneed)
        evidence[(role, subneed)] = {
            "reference_id": ref["reference_id"],
            "compatibility_class": status,
            "confidence": role_confidence(ref, task, role, subneed),
        }
        existing = next((item for item in selected if item["reference_id"] == ref["reference_id"]), None)
        if existing is None:
            existing = {"reference_id": ref["reference_id"], "eligible_roles": [], "role_assessments": []}
            selected.append(existing)
        if role not in existing["eligible_roles"]:
            existing["eligible_roles"].append(role)
        existing["role_assessments"].append({
            "role": role,
            "subneed": subneed,
            "compatibility_class": status,
            "confidence": role_confidence(ref, task, role, subneed),
        })

    covered_dimensions = {dimension for dimension, item in evidence.items()
                          if item["compatibility_class"] in {"DIRECT MATCH", "CLOSE ANALOG"}}
    role_evidence = []
    for role, subneed in dimensions:
        item = evidence.get((role, subneed))
        role_evidence.append({
            "role": role,
            "subneed": subneed,
            "reference_id": item["reference_id"] if item else None,
            "compatibility_class": item["compatibility_class"] if item else "NOT SUITABLE",
            "confidence": item["confidence"] if item else "UNKNOWN",
            "covered": (role, subneed) in covered_dimensions,
        })

    relevant = set(task["hybrid_archetype_tags"])
    if task["archetype"] != "unknown":
        relevant.add(task["archetype"])
    rejected = []
    for ref in refs:
        if primary and ref["reference_id"] == primary["reference_id"]:
            continue
        if not (relevant.intersection({ref.get("archetype"), *ref.get("hybrid_archetype_tags", [])})
                or ref.get("commercial_anchor_presence") == "present"):
            continue
        reason = structural_rejection(task, ref)
        if reason:
            rejected.append({"reference_id": ref["reference_id"], "reason": reason})
    rejected.sort(key=lambda item: item["reference_id"])

    all_covered = len(covered_dimensions) == len(dimensions)
    primary_direct = primary is not None and primary["compatibility_class"] == "DIRECT MATCH"
    selected_classes = [assessment["compatibility_class"] for item in selected
                        for assessment in item["role_assessments"]]
    if not primary and not selected:
        coverage = "NONE"
        explanation = "No structural primary or role-compatible known metadata was selected."
    elif primary_direct and all_covered and all(
        label in {"DIRECT MATCH", "CLOSE ANALOG"} for label in selected_classes
    ):
        coverage = "STRONG"
        explanation = "A direct structural primary and direct/close evidence cover all requested roles."
    else:
        coverage = "LIMITED"
        missing = [f"{role}:{subneed}" for role, subneed in dimensions
                   if (role, subneed) not in covered_dimensions]
        reasons = []
        if not primary_direct:
            reasons.append("no direct structural primary")
        if missing:
            reasons.append("uncovered requested roles: " + ", ".join(missing))
        if "PARTIAL ANALOG" in selected_classes:
            reasons.append("one or more roles rely on partial analogs")
        explanation = "; ".join(reasons) or "Useful metadata exists, but coverage is incomplete."

    return {
        "task_profile": task,
        "benchmark_resource_state": resource_state,
        "structural_primary": primary,
        "supporting_references": selected,
        "role_evidence": role_evidence,
        "rejected_major_candidates": rejected,
        "benchmark_coverage": coverage,
        "coverage_explanation": explanation,
        "visual_observations": None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True, help="Path to normalized Task Profile JSON")
    parser.add_argument("--index", help="Optional runtime metadata index path")
    parser.add_argument("--metadata-disabled", action="store_true", help="Simulate unavailable runtime metadata")
    args = parser.parse_args()
    task = None
    try:
        profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
        task = normalize_profile(profile)
        if args.metadata_disabled:
            print(json.dumps({
                "task_profile": task,
                "benchmark_resource_state": "BENCHMARK LIBRARY UNAVAILABLE",
                "structural_primary": None,
                "supporting_references": [],
                "rejected_major_candidates": [],
                "benchmark_coverage": "NONE",
                "coverage_explanation": "Benchmark metadata is disabled; continue qualitative calibration.",
                "visual_observations": None,
            }, ensure_ascii=False, indent=2))
            return 0
        index_path = Path(args.index) if args.index else INDEX_PATH
        index = json.loads(index_path.read_text(encoding="utf-8"))
        refs = index["references"]
        if not isinstance(refs, list):
            raise ValueError("runtime index references must be a list")
        result = select(task, refs, "BENCHMARK METADATA ONLY")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        print(json.dumps({
            "task_profile": task,
            "benchmark_resource_state": "BENCHMARK LIBRARY UNAVAILABLE",
            "benchmark_coverage": "NONE",
            "error": str(error),
            "visual_observations": None,
        }, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
