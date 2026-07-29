"""
File: build_images_json.py

Recursively builds images.json from image files in the
current folder and all subfolders.

Examples:

    calendar.png

becomes:

    {
      "name": "Calendar",
      "file": "calendar.png",
      "category": "Uncategorized"
    }

And:

    announcements/general-announcement.png

becomes:

    {
      "name": "General Announcement",
      "file": "announcements/general-announcement.png",
      "category": "Announcements"
    }

Usage:
    python build_images_json.py
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT_FOLDER = Path(__file__).resolve().parent
OUTPUT_FILE = ROOT_FOLDER / "images.json"

IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
}

IGNORED_FOLDERS = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
}

DEFAULT_CATEGORY = "Uncategorized"


def make_display_name(filename: str) -> str:
    """
    Convert a filename into a readable display name.
    """
    stem = Path(filename).stem

    cleaned = (
        stem
        .replace("-", " ")
        .replace("_", " ")
    )

    return " ".join(
        word.capitalize()
        for word in cleaned.split()
    )


def make_category(relative_path: Path) -> str:
    """
    Use the first subfolder as the image category.

    Examples:
        announcements/image.png -> Announcements
        tools/work-queue/image.png -> Tools
        image.png -> Uncategorized
    """
    if len(relative_path.parts) <= 1:
        return DEFAULT_CATEGORY

    first_folder = relative_path.parts[0]

    return make_display_name(first_folder)


def normalize_manifest_path(path: Path) -> str:
    """
    Return a web-safe relative path using forward slashes.
    """
    return path.as_posix()


def load_existing_manifest() -> dict[str, dict[str, Any]]:
    """
    Load existing entries indexed by relative file path.

    Existing manually edited names, categories,
    descriptions, and other metadata are preserved.
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

        entries: dict[str, dict[str, Any]] = {}

        for entry in data:
            if not isinstance(entry, dict):
                continue

            filename = str(
                entry.get("file", "")
            ).strip()

            if filename:
                entries[filename] = entry

        return entries

    except (
        json.JSONDecodeError,
        OSError,
    ) as error:
        print(
            "Could not read existing images.json:"
        )
        print(error)
        print("The manifest will be rebuilt.")

        return {}


def should_ignore(path: Path) -> bool:
    """
    Return True when any part of the path belongs
    to an ignored folder.
    """
    relative_path = path.relative_to(
        ROOT_FOLDER
    )

    return any(
        part in IGNORED_FOLDERS
        for part in relative_path.parts
    )


def find_image_files() -> list[Path]:
    """
    Recursively locate supported image files.
    """
    image_files = []

    for path in ROOT_FOLDER.rglob("*"):
        if not path.is_file():
            continue

        if should_ignore(path):
            continue

        if path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        image_files.append(path)

    return sorted(
        image_files,
        key=lambda path: (
            path.relative_to(ROOT_FOLDER)
            .as_posix()
            .lower()
        ),
    )


def build_manifest() -> list[dict[str, Any]]:
    """
    Build the complete recursive image manifest.
    """
    existing_entries = load_existing_manifest()
    image_files = find_image_files()

    manifest: list[dict[str, Any]] = []

    for image_path in image_files:
        relative_path = image_path.relative_to(
            ROOT_FOLDER
        )

        manifest_path = normalize_manifest_path(
            relative_path
        )

        if manifest_path in existing_entries:
            entry = dict(
                existing_entries[manifest_path]
            )

            entry["file"] = manifest_path

            if not entry.get("name"):
                entry["name"] = make_display_name(
                    image_path.name
                )

            if not entry.get("category"):
                entry["category"] = make_category(
                    relative_path
                )

        else:
            entry = {
                "name": make_display_name(
                    image_path.name
                ),
                "file": manifest_path,
                "category": make_category(
                    relative_path
                ),
            }

        manifest.append(entry)

    return manifest


def write_manifest(
    manifest: list[dict[str, Any]],
) -> None:
    """
    Write images.json using readable formatting.
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