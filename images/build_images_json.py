"""
File: build_images_json.py

Builds images.json from PNG files in the current folder.

Usage:
    python build_images_json.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


SCRIPT_FOLDER = Path(__file__).resolve().parent
OUTPUT_FILE = SCRIPT_FOLDER / "images.json"

IMAGE_EXTENSIONS = {
    ".png",
}

DEFAULT_CATEGORY = "Uncategorized"


def make_display_name(filename: str) -> str:
    """
    Convert a filename into a readable display name.

    Example:
        work-update-07-26-2026.png
        becomes:
        Work Update 07 26 2026
    """
    stem = Path(filename).stem

    cleaned = stem.replace("-", " ").replace("_", " ")

    return " ".join(
        word.capitalize()
        for word in cleaned.split()
    )


def load_existing_manifest() -> dict[str, dict[str, Any]]:
    """
    Load existing images.json entries and index them
    by filename.

    This preserves manually edited names, categories,
    descriptions, and other fields.
    """
    if not OUTPUT_FILE.exists():
        return {}

    try:
        with OUTPUT_FILE.open(
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        if not isinstance(data, list):
            print(
                "Existing images.json is not a JSON list. "
                "It will be rebuilt."
            )
            return {}

        existing_entries = {}

        for entry in data:
            if not isinstance(entry, dict):
                continue

            filename = str(
                entry.get("file", "")
            ).strip()

            if filename:
                existing_entries[filename] = entry

        return existing_entries

    except (
        json.JSONDecodeError,
        OSError,
    ) as error:
        print(
            "Could not read the existing images.json:"
        )
        print(error)
        print("The file will be rebuilt.")

        return {}


def find_image_files() -> list[Path]:
    """
    Return all supported image files in the folder.
    """
    return sorted(
        (
            path
            for path in SCRIPT_FOLDER.iterdir()
            if (
                path.is_file()
                and path.suffix.lower()
                in IMAGE_EXTENSIONS
            )
        ),
        key=lambda path: path.name.lower(),
    )


def build_manifest() -> list[dict[str, Any]]:
    """
    Build the complete image manifest.
    """
    existing_entries = load_existing_manifest()
    image_files = find_image_files()

    manifest = []

    for image_path in image_files:
        filename = image_path.name

        if filename in existing_entries:
            entry = dict(
                existing_entries[filename]
            )

            entry["file"] = filename

            if not entry.get("name"):
                entry["name"] = make_display_name(
                    filename
                )

            if not entry.get("category"):
                entry["category"] = (
                    DEFAULT_CATEGORY
                )

        else:
            entry = {
                "name": make_display_name(
                    filename
                ),
                "file": filename,
                "category": DEFAULT_CATEGORY,
            }

        manifest.append(entry)

    return manifest


def write_manifest(
    manifest: list[dict[str, Any]],
) -> None:
    """
    Write the manifest to images.json.
    """
    with OUTPUT_FILE.open(
        "w",
        encoding="utf-8",
        newline="\n",
    ) as file:
        json.dump(
            manifest,
            file,
            indent=2,
            ensure_ascii=False,
        )

        file.write("\n")


def main() -> None:
    manifest = build_manifest()
    write_manifest(manifest)

    print(
        f"Wrote {len(manifest)} image entries to:"
    )

    print(OUTPUT_FILE)


if __name__ == "__main__":
    main()
