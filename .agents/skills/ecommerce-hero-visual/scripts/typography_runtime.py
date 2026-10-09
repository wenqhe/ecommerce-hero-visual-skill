#!/usr/bin/env python3
"""Execute raster typography with Pillow + fontTools; no visual approval.

Usage: python typography_runtime.py --base base.png --layout layout.json
         --output composed.png --thumbnail thumb.png --report measurements.json

JSON (positions are Pillow's default text origin, not the visible top-left):
{"texts": [{"id": "headline", "text": "Example", "position": [40, 60],
  "font": "fonts/example.ttf", "size": 48, "weight": null,
  "color": "#202020", "role": "primary", "font_index": 0, "spacing": 4}],
 "protected_regions": [{"id": "product", "bbox": [300, 100, 600, 700]}],
 "contrast_warning_ratio": 3.0}

Font paths resolve relative to layout.json. Optional font_index selects a TTC
face; weight=null preserves the face/default variable axes. A numeric weight
requires a real wght axis or an exactly matching static OS/2 weight. Other
variable axes retain their actual defaults. Overlap checks use conservative
textbbox rectangles; protected-region intersections abort image output. The
contrast warning ratio is configurable auxiliary evidence, not a quality gate.
Outputs are PNGs; the thumbnail is exactly 224x280 with aspect-preserving
letterboxing. The report records the scale, resized image size, and padding.
"""

import argparse
import json
import math
import sys
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageFont
from fontTools.ttLib import TTFont


def number(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f"{label} must be a finite number")
    return value


def rectangle(value, label):
    if not isinstance(value, list) or len(value) != 4:
        raise ValueError(f"{label} must be [left, top, right, bottom]")
    box = [number(v, label) for v in value]
    if box[0] >= box[2] or box[1] >= box[3]:
        raise ValueError(f"{label} must have positive width and height")
    return box


def intersection(a, b):
    box = [max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])]
    return box if box[0] < box[2] and box[1] < box[3] else None


def load_font(item, layout_dir):
    path = Path(item["font"])
    if not path.is_absolute():
        path = layout_dir / path
    path = path.resolve()
    if not path.is_file():
        raise ValueError(f"Font does not exist: {path}")
    size = number(item["size"], "size")
    index = item.get("font_index", 0)
    if int(size) != size or size <= 0:
        raise ValueError("size must be a positive integer in pixels")
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("font_index must be a nonnegative integer")
    weight = item["weight"]
    if weight is not None:
        number(weight, "weight")
    with TTFont(path, fontNumber=index) as metadata:
        axes = [{"tag": a.axisTag, "minimum": a.minValue, "default": a.defaultValue,
                 "maximum": a.maxValue} for a in metadata["fvar"].axes] if "fvar" in metadata else []
        static_weight = metadata["OS/2"].usWeightClass if "OS/2" in metadata else None
        cmap = metadata.getBestCmap() or {}
        missing = sorted({ord(c) for c in item["text"] if c != "\n" and ord(c) not in cmap})
        if missing:
            raise ValueError(f"Font lacks glyphs: {', '.join(f'U+{c:04X}' for c in missing)}")
    face = ImageFont.truetype(str(path), int(size), index=index)
    applied = {a["tag"]: a["default"] for a in axes}
    if weight is not None:
        weight_axis = next((a for a in axes if a["tag"] == "wght"), None)
        if weight_axis:
            if not weight_axis["minimum"] <= weight <= weight_axis["maximum"]:
                raise ValueError(f"weight {weight} outside wght range "
                                 f"[{weight_axis['minimum']}, {weight_axis['maximum']}]")
            applied["wght"] = weight
        elif axes or static_weight != weight:
            raise ValueError(f"Requested weight {weight} unavailable; static weight={static_weight}, "
                             f"axes={[a['tag'] for a in axes]}")
    if axes:
        pillow_axes = face.get_variation_axes()
        if len(pillow_axes) != len(axes) or any(
            (p["minimum"], p["default"], p["maximum"]) !=
            (a["minimum"], a["default"], a["maximum"])
            for p, a in zip(pillow_axes, axes)
        ):
            raise ValueError("Pillow/fontTools variation axis metadata disagree")
        face.set_variation_by_axes([applied[a["tag"]] for a in axes])
    return face, {"path": str(path), "font_index": index, "size_px": int(size),
                  "requested_weight": weight, "static_weight": static_weight,
                  "axes": axes, "applied_axes": applied}


def luminance(rgb):
    channels = [v / 255 for v in rgb]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast_evidence(base, mask, color, threshold):
    ratios, transparent_samples = [], 0
    extent = mask.getbbox()
    if extent:
        background = base.crop(extent)
        coverage = mask.crop(extent)
        for bg, ink in zip(background.getdata(), coverage.getdata()):
            # Sample glyph interiors, excluding antialias fringes.
            if ink < 128:
                continue
            if bg[3] != 255:
                transparent_samples += 1
                continue
            alpha = color[3] / 255
            fg = [alpha * c + (1 - alpha) * b for c, b in zip(color[:3], bg[:3])]
            a, b = luminance(fg), luminance(bg[:3])
            ratios.append((max(a, b) + 0.05) / (min(a, b) + 0.05))
    ratios.sort()
    evidence = {"method": "sRGB luminance at glyph interiors on the unmodified base; "
                          "nominal foreground blended by configured color opacity",
                "sample_count": len(ratios), "transparent_background_samples_omitted": transparent_samples,
                "warning_ratio": threshold, "visual_approval": None}
    if ratios:
        evidence.update(minimum=round(ratios[0], 4),
                        p10=round(ratios[int((len(ratios) - 1) * .1)], 4),
                        median=round(ratios[len(ratios) // 2], 4), maximum=round(ratios[-1], 4),
                        fraction_below_warning_ratio=round(sum(r < threshold for r in ratios) / len(ratios), 4))
    else:
        evidence["limitation"] = "No opaque-background glyph-interior samples; contrast unavailable"
    return evidence


def make_thumbnail(image, target_size=(224, 280)):
    source_width, source_height = image.size
    target_width, target_height = target_size
    scale = min(target_width / source_width, target_height / source_height)
    resized_size = (max(1, round(source_width * scale)), max(1, round(source_height * scale)))
    resized = image.resize(resized_size, Image.Resampling.LANCZOS)
    padding = {
        "left": (target_width - resized_size[0]) // 2,
        "top": (target_height - resized_size[1]) // 2,
        "right": target_width - resized_size[0] - (target_width - resized_size[0]) // 2,
        "bottom": target_height - resized_size[1] - (target_height - resized_size[1]) // 2,
    }
    canvas = Image.new("RGBA", target_size, image.getpixel((0, 0)))
    canvas.alpha_composite(resized, (padding["left"], padding["top"]))
    geometry = {
        "source_size": [source_width, source_height],
        "target_size": [target_width, target_height],
        "scale": scale,
        "resized_size": list(resized_size),
        "padding": padding,
    }
    return canvas, geometry


def render(base_path, layout_path, output, thumbnail, report_path):
    destinations = [Path(p).resolve() for p in (output, thumbnail, report_path)]
    inputs = {Path(base_path).resolve(), Path(layout_path).resolve()}
    if len(set(destinations)) != 3 or inputs.intersection(destinations):
        raise ValueError("Outputs must be distinct and must not overwrite input files")
    if any(p.suffix.lower() != ".png" for p in destinations[:2]):
        raise ValueError("Composition and thumbnail outputs must be .png")
    layout_path = Path(layout_path).resolve()
    layout = json.loads(layout_path.read_text(encoding="utf-8-sig"))
    if not isinstance(layout, dict) or not isinstance(layout.get("texts"), list) or not layout["texts"]:
        raise ValueError("layout must contain a nonempty texts list")
    threshold = number(layout.get("contrast_warning_ratio", 3.0), "contrast_warning_ratio")
    if threshold < 1:
        raise ValueError("contrast_warning_ratio must be at least 1")
    with Image.open(base_path) as source:
        base = source.convert("RGBA")
    regions = []
    for i, region in enumerate(layout.get("protected_regions", [])):
        regions.append({"id": region.get("id", f"region-{i}"),
                        "bbox": rectangle(region["bbox"], "protected region")})
    report = {"base": str(Path(base_path).resolve()), "layout": str(layout_path),
              "canvas_size": list(base.size), "texts": [], "protected_regions": regions,
              "overlaps": [], "warnings": [], "errors": [],
              "outputs": None, "visual_approval": None,
              "limitations": ["Bounding-box overlaps are conservative, not glyph intersection tests",
                              "Contrast evidence does not determine aesthetic quality or thumbnail clarity",
                              "Thumbnail letterboxing preserves aspect ratio; inspect padding and thumbnail clarity"]}
    report["thumbnail_geometry"] = None
    overlay = Image.new("RGBA", base.size)
    draw = ImageDraw.Draw(overlay)
    ids = set()
    for i, item in enumerate(layout["texts"]):
        label = f"text-{i}"
        try:
            for key in ("text", "position", "font", "size", "weight", "color", "role"):
                if key not in item:
                    raise ValueError(f"Missing required field: {key}")
            label = item.get("id", label)
            if not isinstance(label, str) or not label or label in ids:
                raise ValueError("Text IDs must be unique nonempty strings")
            ids.add(label)
            if not isinstance(item["text"], str) or not item["text"].strip():
                raise ValueError("text must be a nonempty string")
            if not isinstance(item["role"], str) or not item["role"]:
                raise ValueError("role must be a nonempty string")
            position = item["position"]
            if not isinstance(position, list) or len(position) != 2:
                raise ValueError("position must be [x, y]")
            xy = tuple(number(v, "position") for v in position)
            spacing = number(item.get("spacing", 4), "spacing")
            if spacing < 0:
                raise ValueError("spacing must be nonnegative")
            color = ImageColor.getcolor(item["color"], "RGBA") if isinstance(item["color"], str) else tuple(item["color"])
            if len(color) == 3:
                color += (255,)
            if len(color) != 4 or any(isinstance(c, bool) or not isinstance(c, int) or not 0 <= c <= 255 for c in color):
                raise ValueError("color must be a Pillow color string or RGB/RGBA byte array")
            face, font_info = load_font(item, layout_path.parent)
            if Path(font_info["path"]) in destinations:
                raise ValueError("Output must not overwrite a font")
            bbox = list(draw.multiline_textbbox(xy, item["text"], font=face, spacing=spacing))
            mask = Image.new("L", base.size)
            ImageDraw.Draw(mask).multiline_text(xy, item["text"], font=face, fill=255, spacing=spacing)
            contrast = contrast_evidence(base, mask, color, threshold)
            measured = {"id": label, "role": item["role"], "text": item["text"],
                        "position": list(xy), "color": list(color), "spacing": spacing,
                        "font": font_info, "textbbox": bbox,
                        "width_px": bbox[2] - bbox[0], "height_px": bbox[3] - bbox[1],
                        "visible_ink_bbox": mask.getbbox(), "contrast": contrast}
            report["texts"].append(measured)
            if bbox[0] < 0 or bbox[1] < 0 or bbox[2] > base.width or bbox[3] > base.height:
                report["errors"].append({
                    "id": label,
                    "kind": "text_out_of_canvas",
                    "message": f"textbbox {bbox} exceeds canvas {list(base.size)}; image output aborted",
                    "textbbox": bbox,
                    "canvas_size": list(base.size),
                })
            if contrast.get("fraction_below_warning_ratio", 0) > 0:
                report["warnings"].append({"id": label, "kind": "contrast_risk"})
            if "limitation" in contrast or contrast["transparent_background_samples_omitted"]:
                report["warnings"].append({"id": label, "kind": "contrast_measurement_limited"})
            draw.multiline_text(xy, item["text"], font=face, fill=color, spacing=spacing)
        except (ValueError, TypeError, KeyError, OSError) as error:
            report["errors"].append({"id": label, "message": str(error)})
    for i, a in enumerate(report["texts"]):
        for b in report["texts"][i + 1:]:
            overlap = intersection(a["textbbox"], b["textbbox"])
            if overlap:
                report["overlaps"].append({"kind": "text_text", "ids": [a["id"], b["id"]], "bbox": overlap})
        for region in regions:
            overlap = intersection(a["textbbox"], region["bbox"])
            if overlap:
                report["overlaps"].append({"kind": "text_protected_region", "ids": [a["id"], region["id"]], "bbox": overlap})
                report["errors"].append({"id": a["id"], "message": f"Intersects protected region {region['id']}; image output aborted"})
    if not report["errors"]:
        composite = Image.alpha_composite(base, overlay)
        for destination in destinations[:2]:
            destination.parent.mkdir(parents=True, exist_ok=True)
        composite.save(destinations[0], format="PNG")
        thumbnail, thumbnail_geometry = make_thumbnail(composite)
        thumbnail.save(destinations[1], format="PNG")
        report["thumbnail_geometry"] = thumbnail_geometry
        report["outputs"] = {"composition": str(destinations[0]), "thumbnail": str(destinations[1]),
                             "thumbnail_size": [224, 280]}
    destinations[2].parent.mkdir(parents=True, exist_ok=True)
    destinations[2].write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for name in ("base", "layout", "output", "thumbnail", "report"):
        parser.add_argument(f"--{name}", required=True, type=Path)
    args = parser.parse_args()
    try:
        report = render(args.base, args.layout, args.output, args.thumbnail, args.report)
    except (ValueError, TypeError, KeyError, OSError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps({"report": str(args.report.resolve()), "outputs": report["outputs"],
                      "errors": report["errors"], "warnings": report["warnings"],
                      "overlap_count": len(report["overlaps"]), "visual_approval": None}, ensure_ascii=False))
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    sys.exit(main())
