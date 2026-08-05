#!/usr/bin/env python3
"""
Build the JSON manifest used by the online Local JSON Explorer.

Place this script in the root of the JSON repository:

    work-update-catalog/
    ├── manifest.py
    ├── json-manifest.json          <- generated
    ├── catalogs/
    ├── sidecars/
    ├── summaries/
    ├── templates/
    ├── workflows/
    ├── tools/
    └── archived/

Run from the repository root:

    py -3 manifest.py

The script recursively discovers JSON files and writes repository-relative paths
to json-manifest.json. It does not modify any source JSON files.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


SCRIPT_VERSION = "1.0.0"
MANIFEST_SCHEMA_VERSION = "1.0"

ROOT_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = ROOT_DIR / "json-manifest.json"

EXCLUDED_DIRECTORY_NAMES = {
    ".git",
    ".github",
    ".hg",
    ".svn",
    ".idea",
    ".venv",
    "venv",
    "node_modules",
    "__pycache__",
}

ARCHIVE_DIRECTORY_NAMES = {
    "archive",
    "archived",
}

EXCLUDED_FILE_NAMES = {
    OUTPUT_FILE.name.lower(),
}


def utc_timestamp() -> str:
    """Return the current UTC time in ISO 8601 format."""

    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def is_plain_object(value: Any) -> bool:
    """Return True when value is a JSON object represented by a dictionary."""

    return isinstance(value, dict)


def first_nonempty(*values: Any) -> str:
    """Return the first nonempty scalar value as text."""

    for value in values:
        if value is None:
            continue

        if isinstance(value, str):
            value = value.strip()
            if value:
                return value

        elif isinstance(value, (int, float, bool)):
            return str(value)

    return ""


def nested_get(data: Any, *keys: str) -> Any:
    """Read a nested dictionary path safely."""

    current = data

    for key in keys:
        if not isinstance(current, dict):
            return None

        current = current.get(key)

    return current


def is_archived(relative_path: Path) -> bool:
    """Return True when a path passes through an archive directory."""

    return any(
        part.lower() in ARCHIVE_DIRECTORY_NAMES
        for part in relative_path.parts[:-1]
    )


def iter_json_files(root_dir: Path) -> Iterable[Path]:
    """Yield repository JSON files while pruning excluded directories."""

    for current_root, directory_names, file_names in os.walk(root_dir):
        current_path = Path(current_root)

        directory_names[:] = [
            name
            for name in directory_names
            if name.lower() not in EXCLUDED_DIRECTORY_NAMES
            and not name.startswith(".")
        ]

        for file_name in file_names:
            if not file_name.lower().endswith(".json"):
                continue

            if file_name.lower() in EXCLUDED_FILE_NAMES:
                continue

            file_path = current_path / file_name

            if file_path.is_file():
                yield file_path


def read_json_file(path: Path) -> tuple[Any | None, str]:
    """
    Read and parse one JSON file.

    Returns:
        (parsed_data, error_message)
    """

    try:
        raw = path.read_text(encoding="utf-8-sig")
        return json.loads(raw), ""

    except UnicodeDecodeError as exc:
        return None, f"Encoding error: {exc}"

    except json.JSONDecodeError as exc:
        return (
            None,
            f"Invalid JSON at line {exc.lineno}, "
            f"column {exc.colno}: {exc.msg}",
        )

    except OSError as exc:
        return None, f"Read error: {exc}"


def detect_record_type(data: Any) -> str:
    """Infer a useful broad record type from the JSON structure."""

    if not is_plain_object(data):
        return "json-data"

    profile_type = first_nonempty(
        nested_get(data, "profile", "profileType"),
        nested_get(data, "profile", "previewMode"),
    )

    if profile_type:
        return profile_type

    document_type = first_nonempty(
        nested_get(data, "document", "documentType"),
        data.get("documentType"),
        data.get("recordType"),
        data.get("type"),
    )

    if document_type:
        return document_type

    schema_name = first_nonempty(
        nested_get(data, "schema", "schema_name"),
        nested_get(data, "schema", "schemaName"),
        data.get("schema_name"),
        data.get("schemaName"),
    )

    if schema_name:
        return schema_name

    catalog_id = first_nonempty(
        nested_get(data, "catalog", "catalogId"),
        nested_get(data, "catalog", "catalog_id"),
        nested_get(data, "catalog_metadata", "catalog_id"),
    )

    if catalog_id or isinstance(data.get("entries"), list):
        return "catalog"

    if "pstSpContent" in data:
        return "pst-sp-study-guide"

    if "workflowIdentity" in data or "steps" in data:
        return "workflow-specification"

    return "json-document"


def extract_title(data: Any, fallback: str) -> str:
    """Extract a readable title from common sidecar and catalog fields."""

    if not is_plain_object(data):
        return fallback

    return first_nonempty(
        nested_get(data, "document", "title"),
        nested_get(data, "document", "documentTitle"),
        nested_get(data, "publication", "listingTitle"),
        nested_get(data, "catalog", "title"),
        nested_get(data, "catalog", "catalogTitle"),
        nested_get(data, "catalog_metadata", "title"),
        nested_get(data, "workflowIdentity", "title"),
        data.get("title"),
        data.get("name"),
        fallback,
    )


def extract_description(data: Any) -> str:
    """Extract a concise description or summary."""

    if not is_plain_object(data):
        return ""

    return first_nonempty(
        nested_get(data, "documentSummary", "summary"),
        nested_get(data, "documentSummary", "purpose"),
        nested_get(data, "publication", "listingDescription"),
        nested_get(data, "catalog", "description"),
        nested_get(data, "catalog", "summary"),
        nested_get(data, "catalog_metadata", "purpose"),
        nested_get(data, "subject", "description"),
        data.get("summary"),
        data.get("description"),
    )


def extract_status(data: Any) -> str:
    """Extract a current status when available."""

    if not is_plain_object(data):
        return ""

    return first_nonempty(
        nested_get(data, "publication", "status"),
        nested_get(data, "documentSummary", "status"),
        nested_get(data, "pstSpContent", "coverage", "sidecarStatus"),
        nested_get(data, "workflowIdentity", "currentStatus"),
        nested_get(data, "catalog_metadata", "status"),
        data.get("status"),
    )


def extract_date(data: Any, file_modified_timestamp: str) -> str:
    """Extract the best available document date."""

    if not is_plain_object(data):
        return file_modified_timestamp

    return first_nonempty(
        nested_get(data, "document", "updatedTimestamp"),
        nested_get(data, "document", "createdTimestamp"),
        nested_get(data, "publication", "publishedTimestamp"),
        nested_get(data, "catalog", "updatedTimestamp"),
        nested_get(data, "catalog", "generatedTimestamp"),
        nested_get(data, "catalog_metadata", "updated_at"),
        nested_get(data, "catalog_metadata", "created_at"),
        data.get("updatedTimestamp"),
        data.get("createdTimestamp"),
        file_modified_timestamp,
    )


def extract_topics(data: Any) -> list[str]:
    """Extract a small normalized topic list."""

    if not is_plain_object(data):
        return []

    candidates = [
        nested_get(data, "subject", "topics"),
        nested_get(data, "subject", "keywords"),
        nested_get(data, "publication", "keywords"),
        data.get("topics"),
        data.get("keywords"),
        data.get("tags"),
    ]

    topics: list[str] = []
    seen: set[str] = set()

    for candidate in candidates:
        if isinstance(candidate, str):
            values = [candidate]

        elif isinstance(candidate, list):
            values = candidate

        else:
            continue

        for value in values:
            if not isinstance(value, str):
                continue

            cleaned = value.strip()

            if not cleaned:
                continue

            comparison_key = cleaned.casefold()

            if comparison_key in seen:
                continue

            seen.add(comparison_key)
            topics.append(cleaned)

            if len(topics) >= 12:
                return topics

    return topics


def build_manifest_entry(path: Path) -> dict[str, Any]:
    """Create one manifest record from a JSON file."""

    relative_path = path.relative_to(ROOT_DIR)
    relative_posix = relative_path.as_posix()
    stat = path.stat()

    modified_timestamp = (
        datetime.fromtimestamp(stat.st_mtime, timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )

    data, parse_error = read_json_file(path)

    entry: dict[str, Any] = {
        "name": path.name,
        "path": relative_posix,
        "folder": (
            relative_path.parent.as_posix()
            if relative_path.parent != Path(".")
            else ""
        ),
        "size": stat.st_size,
        "modifiedTimestamp": modified_timestamp,
        "archived": is_archived(relative_path),
        "validJson": parse_error == "",
        "parseError": parse_error,
        "title": extract_title(data, path.stem),
        "description": extract_description(data),
        "recordType": detect_record_type(data),
        "status": extract_status(data),
        "documentDate": extract_date(data, modified_timestamp),
        "topics": extract_topics(data),
    }

    if is_plain_object(data):
        entry["schemaVersion"] = first_nonempty(
            data.get("schemaVersion"),
            nested_get(data, "schema", "schemaVersion"),
            nested_get(data, "schema", "version"),
        )

        entry["previewMode"] = first_nonempty(
            nested_get(data, "profile", "previewMode"),
            nested_get(data, "profile", "profileType"),
        )

        entries = data.get("entries")

        if isinstance(entries, list):
            entry["entryCount"] = len(entries)

    return entry


def build_manifest() -> dict[str, Any]:
    """Scan the repository and build the complete manifest object."""

    entries = [
        build_manifest_entry(path)
        for path in iter_json_files(ROOT_DIR)
    ]

    entries.sort(
        key=lambda item: (
            item["archived"],
            item["folder"].casefold(),
            item["title"].casefold(),
            item["path"].casefold(),
        )
    )

    valid_count = sum(1 for entry in entries if entry["validJson"])
    invalid_count = len(entries) - valid_count
    archived_count = sum(1 for entry in entries if entry["archived"])

    record_type_counts: dict[str, int] = {}

    for entry in entries:
        record_type = entry["recordType"]
        record_type_counts[record_type] = (
            record_type_counts.get(record_type, 0) + 1
        )

    return {
        "schemaVersion": MANIFEST_SCHEMA_VERSION,
        "manifestType": "online-json-viewer-manifest",
        "generator": {
            "name": "work-update-catalog manifest builder",
            "version": SCRIPT_VERSION,
            "script": Path(__file__).name,
        },
        "repository": {
            "name": ROOT_DIR.name,
            "rootPath": ".",
            "generatedTimestamp": utc_timestamp(),
        },
        "summary": {
            "fileCount": len(entries),
            "validJsonCount": valid_count,
            "invalidJsonCount": invalid_count,
            "archivedFileCount": archived_count,
            "recordTypeCounts": dict(
                sorted(record_type_counts.items())
            ),
        },
        "files": entries,
    }


def write_manifest(manifest: dict[str, Any]) -> None:
    """Write the manifest using UTF-8 and readable indentation."""

    temporary_file = OUTPUT_FILE.with_suffix(".json.tmp")

    temporary_file.write_text(
        json.dumps(
            manifest,
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    # Confirm that the generated file parses before replacing the old manifest.
    json.loads(temporary_file.read_text(encoding="utf-8"))

    temporary_file.replace(OUTPUT_FILE)


def print_report(manifest: dict[str, Any]) -> None:
    """Print a concise build report."""

    summary = manifest["summary"]

    print("JSON manifest created successfully.")
    print()
    print(f"Repository:   {ROOT_DIR}")
    print(f"Output:       {OUTPUT_FILE}")
    print(f"JSON files:   {summary['fileCount']}")
    print(f"Valid:        {summary['validJsonCount']}")
    print(f"Invalid:      {summary['invalidJsonCount']}")
    print(f"Archived:     {summary['archivedFileCount']}")

    if summary["invalidJsonCount"]:
        print()
        print("Files with JSON errors:")

        for entry in manifest["files"]:
            if not entry["validJson"]:
                print(f"  - {entry['path']}")
                print(f"    {entry['parseError']}")


def main() -> None:
    """Build and save the repository manifest."""

    manifest = build_manifest()
    write_manifest(manifest)
    print_report(manifest)


if __name__ == "__main__":
    main()