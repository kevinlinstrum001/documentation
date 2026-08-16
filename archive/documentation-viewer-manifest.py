#!/usr/bin/env python3
"""
Build the source-aware manifest for Klinswork Documentation Viewer 2.0.

This script is intentionally parallel to the existing ``manifest.py`` builder.
It writes ``documentation-viewer-manifest.json`` and does not modify the legacy
``json-manifest.json`` used by the current online viewer.

Architecture
============

Klinswork documentation can live in multiple deliberately registered
``documentation spaces`` beneath the repository's ``documentation/`` root.
Each source declares a discovery mode:

``all-json``
    Recursively discover JSON records beneath the source root. This is suitable
    for the common Documentation Viewer home, which contains catalogs, generic
    sidecars, templates, workflows, and other structured documentation.

``sidecars``
    Recursively discover JSON files only when their path passes through a
    directory named ``sidecars``. This is suitable for project, therapy, and
    future domain-specific documentation spaces so application/data JSON does
    not become documentation merely because it exists nearby.

Sidecars and summaries
======================

A Klinswork sidecar is the structured companion of a human-readable document,
normally a Markdown summary. New sidecars should explicitly declare the pair:

    "companionDocument": {
      "path": "../summaries/systems-summary.md",
      "format": "markdown"
    }

The builder resolves and validates that path relative to the sidecar. For
migration support, it also performs one conservative filename inference when a
sidecar lives below ``sidecars/``: ``foo-sidecar.json`` is checked against the
parallel ``summaries/foo.md`` path. Inference is reported as ``inferred`` rather
than ``resolved`` so undeclared metadata remains visible.

Source configuration
====================

If ``documentation-viewer-sources.json`` exists beside this script, it is used.
Otherwise the built-in defaults are:

- Common Documentation: ``documents/Klinswork Documentation Viewer`` (all-json)
- Projects: ``documents/Klinswork Documentation Viewer/projects`` (sidecars)
- Therapy Component Library: ``documents/therapy-documentation-work/therapy-component-library`` (sidecars)

Paths in source configuration are relative to the ``documentation/`` root.
The documentation root is inferred from the nearest ancestor named
``documentation`` or can be supplied explicitly with ``--documentation-root``.

Typical usage from the ``documentation/`` root::

    py -3 documentation-viewer-manifest.py

Optional::

    py -3 documentation-viewer-manifest.py --documentation-root C:\\path\\to\\documentation

No third-party packages are required.
"""

from __future__ import annotations

import argparse
import json
import os
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Sequence


SCRIPT_VERSION = "2.0.0-draft.2"
MANIFEST_SCHEMA_VERSION = "2.0-draft"
MANIFEST_TYPE = "klinswork-documentation-viewer-manifest"

SCRIPT_PATH = Path(__file__).resolve()
BUILDER_ROOT = SCRIPT_PATH.parent
DEFAULT_OUTPUT_NAME = "documentation-viewer-manifest.json"
DEFAULT_CONFIG_NAME = "documentation-viewer-sources.json"

SOURCE_CONFIG_FILE = BUILDER_ROOT / DEFAULT_CONFIG_NAME

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

ARCHIVE_DIRECTORY_NAMES = {"archive", "archived"}
SIDECAR_DIRECTORY_NAME = "sidecars"
SUMMARY_DIRECTORY_NAME = "summaries"

EXCLUDED_FILE_NAMES = {
    "json-manifest.json",
    DEFAULT_OUTPUT_NAME.lower(),
    DEFAULT_CONFIG_NAME.lower(),
}

ALLOWED_DISCOVERY_MODES = {"all-json", "sidecars"}

DEFAULT_SOURCE_CONFIG: list[dict[str, str]] = [
    {
        "sourceId": "common",
        "label": "Common Documentation",
        "rootPath": "documents/Klinswork Documentation Viewer",
        "discoveryMode": "all-json",
    },
    {
        "sourceId": "projects",
        "label": "Projects",
        "rootPath": "documents/Klinswork Documentation Viewer/projects",
        "discoveryMode": "sidecars",
    },
    {
        "sourceId": "therapy",
        "label": "Therapy Component Library",
        "rootPath": "documents/therapy-documentation-work/therapy-component-library",
        "discoveryMode": "sidecars",
    },
]


@dataclass(frozen=True)
class SourceSpec:
    """One deliberately registered Klinswork documentation space."""

    source_id: str
    label: str
    root_path: str
    discovery_mode: str
    root_dir: Path
    manifest_relative_root: str
    exists: bool

    def public_record(self) -> dict[str, Any]:
        return {
            "sourceId": self.source_id,
            "label": self.label,
            "rootPath": self.root_path,
            "manifestRelativeRoot": self.manifest_relative_root,
            "discoveryMode": self.discovery_mode,
            "exists": self.exists,
        }


# ---------------------------------------------------------------------------
# Generic helpers retained from manifest.py, generalized for multiple sources
# ---------------------------------------------------------------------------


def utc_timestamp() -> str:
    """Return current UTC time as an ISO 8601 string."""

    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def is_plain_object(value: Any) -> bool:
    return isinstance(value, dict)


def first_nonempty(*values: Any) -> str:
    for value in values:
        if value is None:
            continue
        if isinstance(value, str):
            cleaned = value.strip()
            if cleaned:
                return cleaned
        elif isinstance(value, (int, float, bool)):
            return str(value)
    return ""


def nested_get(data: Any, *keys: str) -> Any:
    current = data
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def normalize_repo_path(path: Path, base: Path) -> str:
    """Return a POSIX path relative to *base*."""

    return path.relative_to(base).as_posix()


def posix_relpath(path: Path, start: Path) -> str:
    """Return an OS-independent relative path rendered with POSIX separators."""

    relative = os.path.relpath(path, start=start)
    return PurePosixPath(Path(relative)).as_posix()


def path_has_named_directory(relative_path: Path, directory_name: str) -> bool:
    wanted = directory_name.casefold()
    return any(part.casefold() == wanted for part in relative_path.parts[:-1])


def is_archived(relative_path: Path) -> bool:
    return any(
        part.casefold() in ARCHIVE_DIRECTORY_NAMES
        for part in relative_path.parts[:-1]
    )


def read_json_file(path: Path) -> tuple[Any | None, str]:
    try:
        raw = path.read_text(encoding="utf-8-sig")
        return json.loads(raw), ""
    except UnicodeDecodeError as exc:
        return None, f"Encoding error: {exc}"
    except json.JSONDecodeError as exc:
        return (
            None,
            f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}",
        )
    except OSError as exc:
        return None, f"Read error: {exc}"


# ---------------------------------------------------------------------------
# Existing metadata extraction, kept schema-tolerant
# ---------------------------------------------------------------------------


def detect_record_type(data: Any) -> str:
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
        nested_get(data, "identity", "canonicalName"),
        nested_get(data, "project", "canonicalName"),
        nested_get(data, "system", "canonicalName"),
        data.get("title"),
        data.get("name"),
        fallback,
    )


def extract_description(data: Any) -> str:
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
        nested_get(data, "preview", "summary"),
        data.get("summary"),
        data.get("description"),
    )


def extract_status(data: Any) -> str:
    if not is_plain_object(data):
        return ""

    return first_nonempty(
        nested_get(data, "publication", "status"),
        nested_get(data, "documentSummary", "status"),
        nested_get(data, "pstSpContent", "coverage", "sidecarStatus"),
        nested_get(data, "workflowIdentity", "currentStatus"),
        nested_get(data, "catalog_metadata", "status"),
        nested_get(data, "project", "status"),
        nested_get(data, "system", "status"),
        data.get("status"),
    )


def extract_date(data: Any, file_modified_timestamp: str) -> str:
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
        nested_get(data, "provenance", "lastReviewed"),
        data.get("updatedTimestamp"),
        data.get("createdTimestamp"),
        data.get("documentDate"),
        data.get("date"),
        file_modified_timestamp,
    )


def extract_topics(data: Any) -> list[str]:
    if not is_plain_object(data):
        return []

    candidates = [
        nested_get(data, "subject", "topics"),
        nested_get(data, "subject", "keywords"),
        nested_get(data, "publication", "keywords"),
        nested_get(data, "preview", "topics"),
        data.get("topics"),
        data.get("keywords"),
        data.get("tags"),
    ]

    topics: list[str] = []
    seen: set[str] = set()

    for candidate in candidates:
        if isinstance(candidate, str):
            values: Sequence[Any] = [candidate]
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


def extract_identity_refs(data: Any) -> dict[str, str]:
    """Extract lightweight stable-ID references when a sidecar exposes them."""

    if not is_plain_object(data):
        return {}

    project_id = first_nonempty(
        nested_get(data, "project", "projectId"),
        nested_get(data, "identity", "projectId"),
        nested_get(data, "projectContext", "projectId"),
        data.get("projectId"),
    )
    system_id = first_nonempty(
        nested_get(data, "system", "systemId"),
        nested_get(data, "identity", "systemId"),
        nested_get(data, "systemContext", "systemId"),
        data.get("systemId"),
    )
    resource_id = first_nonempty(
        nested_get(data, "resource", "resourceId"),
        nested_get(data, "identity", "resourceId"),
        data.get("resourceId"),
    )
    document_id = first_nonempty(
        nested_get(data, "document", "documentId"),
        nested_get(data, "identity", "documentId"),
        data.get("documentId"),
    )

    result: dict[str, str] = {}
    if project_id:
        result["projectId"] = project_id
    if system_id:
        result["systemId"] = system_id
    if resource_id:
        result["resourceId"] = resource_id
    if document_id:
        result["documentId"] = document_id
    return result


# ---------------------------------------------------------------------------
# Documentation source configuration
# ---------------------------------------------------------------------------


def infer_documentation_root(builder_root: Path) -> Path:
    """Find the nearest ancestor named 'documentation'."""

    for candidate in (builder_root, *builder_root.parents):
        if candidate.name.casefold() == "documentation":
            return candidate

    # Backward-compatible fallback for the expected
    # documentation/documents/work-update-catalog placement.
    if len(builder_root.parents) >= 2:
        return builder_root.parents[1]
    return builder_root


def validate_source_id(value: str) -> str:
    cleaned = value.strip()
    if not cleaned:
        raise ValueError("sourceId cannot be empty")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", cleaned):
        raise ValueError(
            f"Invalid sourceId {value!r}; use letters, numbers, '.', '_' or '-'."
        )
    return cleaned


def load_source_config(config_path: Path | None) -> list[dict[str, Any]]:
    """Load source definitions or return built-in defaults."""

    if config_path is None or not config_path.is_file():
        return [dict(item) for item in DEFAULT_SOURCE_CONFIG]

    raw = json.loads(config_path.read_text(encoding="utf-8-sig"))
    if not isinstance(raw, dict):
        raise ValueError("Source configuration must be a JSON object.")
    sources = raw.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("Source configuration must contain a nonempty 'sources' array.")
    return sources


def resolve_viewer_root(
    documentation_root: Path,
    raw_sources: Sequence[dict[str, Any]],
) -> Path:
    """Resolve the Viewer home from the registered ``common`` source.

    The manifest builder may live anywhere under ``documentation/``. The
    Viewer home is a semantic source location, not the builder's location.
    There is deliberately no fallback to ``BUILDER_ROOT``: a missing or
    malformed ``common`` source is a configuration error and must not silently
    redirect generated output into ``documentation/``.
    """

    for raw in raw_sources:
        if not isinstance(raw, dict):
            continue
        if str(raw.get("sourceId", "")).strip().casefold() != "common":
            continue

        root_path = first_nonempty(raw.get("rootPath"))
        if not root_path:
            raise ValueError(
                "The registered 'common' documentation source is missing rootPath."
            )

        pure_root = PurePosixPath(root_path.replace("\\", "/"))
        if pure_root.is_absolute() or any(
            part in {"", ".", ".."} for part in pure_root.parts
        ):
            raise ValueError(
                "The registered 'common' rootPath must be a safe path relative "
                "to documentation/."
            )

        viewer_root = documentation_root.joinpath(*pure_root.parts).resolve()
        try:
            viewer_root.relative_to(documentation_root.resolve())
        except ValueError as exc:
            raise ValueError(
                "The registered 'common' source resolves outside documentation/."
            ) from exc
        return viewer_root

    raise ValueError(
        "No documentation source with sourceId 'common' is registered; "
        "cannot determine the Klinswork Documentation Viewer home."
    )


def make_source_specs(
    documentation_root: Path,
    viewer_root: Path,
    raw_sources: Sequence[dict[str, Any]],
) -> list[SourceSpec]:
    specs: list[SourceSpec] = []
    seen_ids: set[str] = set()

    doc_root = documentation_root.resolve()

    for index, raw in enumerate(raw_sources, start=1):
        if not isinstance(raw, dict):
            raise ValueError(f"Source #{index} must be an object.")

        source_id = validate_source_id(str(raw.get("sourceId", "")))
        source_key = source_id.casefold()
        if source_key in seen_ids:
            raise ValueError(f"Duplicate sourceId: {source_id}")
        seen_ids.add(source_key)

        label = first_nonempty(raw.get("label"), source_id)
        root_path = first_nonempty(raw.get("rootPath"))
        if not root_path:
            raise ValueError(f"Source {source_id!r} is missing rootPath.")

        discovery_mode = first_nonempty(raw.get("discoveryMode"), "sidecars").casefold()
        if discovery_mode not in ALLOWED_DISCOVERY_MODES:
            raise ValueError(
                f"Source {source_id!r} has unsupported discoveryMode {discovery_mode!r}. "
                f"Expected one of {sorted(ALLOWED_DISCOVERY_MODES)}."
            )

        pure_root = PurePosixPath(root_path.replace("\\", "/"))
        if pure_root.is_absolute() or any(part in {"", ".", ".."} for part in pure_root.parts):
            raise ValueError(
                f"Source {source_id!r} rootPath must be documentation-relative without '..': {root_path!r}"
            )

        root_dir = (doc_root.joinpath(*pure_root.parts)).resolve()
        try:
            root_dir.relative_to(doc_root)
        except ValueError as exc:
            raise ValueError(f"Source {source_id!r} escapes documentation root.") from exc

        specs.append(
            SourceSpec(
                source_id=source_id,
                label=label,
                root_path=pure_root.as_posix(),
                discovery_mode=discovery_mode,
                root_dir=root_dir,
                manifest_relative_root=posix_relpath(root_dir, viewer_root),
                exists=root_dir.is_dir(),
            )
        )

    return specs


# ---------------------------------------------------------------------------
# Source-aware discovery
# ---------------------------------------------------------------------------


def iter_json_files(
    source: SourceSpec,
    nested_source_roots: Sequence[Path] = (),
) -> Iterable[Path]:
    """Yield structured records according to a source's discovery mode.

    Registered sources may be nested.  When scanning a broader source (for
    example Common Documentation), directories owned by a more-specific source
    are pruned so each record has exactly one physical source identity.
    """

    if not source.exists:
        return

    nested_roots = {path.resolve() for path in nested_source_roots}

    for current_root, directory_names, file_names in os.walk(source.root_dir):
        current_path = Path(current_root).resolve()

        kept_directories: list[str] = []
        for name in directory_names:
            if name.casefold() in EXCLUDED_DIRECTORY_NAMES or name.startswith("."):
                continue
            child = (current_path / name).resolve()
            if child in nested_roots:
                continue
            kept_directories.append(name)
        directory_names[:] = kept_directories

        for file_name in file_names:
            if not file_name.casefold().endswith(".json"):
                continue
            if file_name.casefold() in EXCLUDED_FILE_NAMES:
                continue

            path = current_path / file_name
            if not path.is_file():
                continue

            relative = path.relative_to(source.root_dir)
            if (
                source.discovery_mode == "sidecars"
                and not path_has_named_directory(relative, SIDECAR_DIRECTORY_NAME)
            ):
                continue

            yield path


# ---------------------------------------------------------------------------
# Sidecar <-> human-readable companion resolution
# ---------------------------------------------------------------------------


def extract_explicit_companion(data: Any) -> tuple[str, str]:
    """Return (declared_path, declared_format) from supported v2 fields."""

    if not is_plain_object(data):
        return "", ""

    candidates = [
        nested_get(data, "companionDocument"),
        nested_get(data, "companion"),
        nested_get(data, "document", "companionDocument"),
        nested_get(data, "sourceDocument"),
        nested_get(data, "summaryDocument"),
    ]

    for candidate in candidates:
        if isinstance(candidate, str):
            cleaned = candidate.strip()
            if cleaned:
                return cleaned, ""
        elif isinstance(candidate, dict):
            path = first_nonempty(
                candidate.get("path"),
                candidate.get("relativePath"),
                candidate.get("filePath"),
                candidate.get("summaryPath"),
            )
            if path:
                return path, first_nonempty(
                    candidate.get("format"),
                    candidate.get("contentType"),
                    candidate.get("type"),
                )

    # Explicit scalar aliases reserved for project/system v2 sidecars.
    alias_path = first_nonempty(
        data.get("companionDocumentPath"),
        data.get("summaryDocumentPath"),
    )
    return alias_path, ""


def infer_companion_candidate(source: SourceSpec, sidecar_path: Path) -> Path | None:
    """
    Conservatively infer a sibling summary from a conventional sidecar name.

    Example:
        area/sidecars/systems-summary-sidecar.json
        -> area/summaries/systems-summary.md
    """

    relative = sidecar_path.relative_to(source.root_dir)
    parts = list(relative.parts)

    sidecars_index: int | None = None
    for index, part in enumerate(parts[:-1]):
        if part.casefold() == SIDECAR_DIRECTORY_NAME:
            sidecars_index = index
            break

    if sidecars_index is None:
        return None

    stem = sidecar_path.stem
    if not stem.casefold().endswith("-sidecar"):
        return None

    summary_name = stem[: -len("-sidecar")] + ".md"
    candidate_parts = parts[:]
    candidate_parts[sidecars_index] = SUMMARY_DIRECTORY_NAME
    candidate_parts[-1] = summary_name
    return source.root_dir.joinpath(*candidate_parts)


def resolve_companion_document(
    source: SourceSpec,
    sidecar_path: Path,
    data: Any,
    documentation_root: Path,
    viewer_root: Path,
) -> dict[str, Any]:
    """Resolve and validate the human-readable document represented by a sidecar."""

    declared_path, declared_format = extract_explicit_companion(data)
    resolution_method = "declared" if declared_path else ""
    candidate: Path | None = None
    validation_error = ""

    if declared_path:
        normalized = declared_path.replace("\\", "/").strip()
        pure = PurePosixPath(normalized)

        if pure.is_absolute() or not pure.parts:
            validation_error = "Companion path must be relative to the sidecar."
        else:
            candidate = (sidecar_path.parent.joinpath(*pure.parts)).resolve()
            try:
                candidate.relative_to(source.root_dir.resolve())
            except ValueError:
                validation_error = "Companion path resolves outside its documentation source."
                candidate = None
    else:
        candidate = infer_companion_candidate(source, sidecar_path)
        if candidate is not None and candidate.is_file():
            resolution_method = "inferred"
        else:
            candidate = None

    if validation_error:
        return {
            "status": "invalid",
            "resolutionMethod": resolution_method or "declared",
            "declaredPath": declared_path,
            "format": declared_format,
            "exists": False,
            "error": validation_error,
        }

    if candidate is None:
        return {
            "status": "undeclared",
            "resolutionMethod": "none",
            "declaredPath": "",
            "format": "",
            "exists": False,
        }

    exists = candidate.is_file()

    if declared_path:
        status = "resolved" if exists else "missing"
    else:
        status = "inferred" if exists else "undeclared"

    result: dict[str, Any] = {
        "status": status,
        "resolutionMethod": resolution_method,
        "declaredPath": declared_path,
        "format": declared_format or (
            "markdown" if candidate.suffix.casefold() in {".md", ".markdown"} else candidate.suffix.lstrip(".")
        ),
        "exists": exists,
    }

    try:
        source_relative = candidate.relative_to(source.root_dir).as_posix()
        result["path"] = source_relative
        result["documentationPath"] = candidate.relative_to(documentation_root).as_posix()
        result["manifestRelativePath"] = posix_relpath(candidate, viewer_root)
    except ValueError:
        # Defensive; declared companions are already constrained to source root.
        result["error"] = "Resolved companion could not be expressed relative to documentation roots."
        result["status"] = "invalid"
        result["exists"] = False

    return result


# ---------------------------------------------------------------------------
# Manifest construction
# ---------------------------------------------------------------------------


def build_manifest_entry(
    source: SourceSpec,
    path: Path,
    documentation_root: Path,
    viewer_root: Path,
) -> dict[str, Any]:
    relative_path = path.relative_to(source.root_dir)
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
        "sourceId": source.source_id,
        "name": path.name,
        "path": relative_posix,
        "folder": relative_path.parent.as_posix() if relative_path.parent != Path(".") else "",
        "documentationPath": path.relative_to(documentation_root).as_posix(),
        "manifestRelativePath": posix_relpath(path, viewer_root),
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

        identity_refs = extract_identity_refs(data)
        if identity_refs:
            entry["identityRefs"] = identity_refs

        entries = data.get("entries")
        if isinstance(entries, list):
            entry["entryCount"] = len(entries)

    if path_has_named_directory(relative_path, SIDECAR_DIRECTORY_NAME):
        entry["companionDocument"] = resolve_companion_document(
            source,
            path,
            data,
            documentation_root,
            viewer_root,
        )

    return entry


def _is_descendant(candidate: Path, ancestor: Path) -> bool:
    try:
        candidate.resolve().relative_to(ancestor.resolve())
        return True
    except ValueError:
        return False


def build_manifest(
    documentation_root: Path,
    viewer_root: Path,
    sources: Sequence[SourceSpec],
) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []
    source_errors: list[dict[str, str]] = []

    for source in sources:
        if not source.exists:
            source_errors.append(
                {
                    "sourceId": source.source_id,
                    "error": f"Source directory does not exist: {source.root_path}",
                }
            )
            continue

        nested_roots = [
            other.root_dir
            for other in sources
            if other.source_id != source.source_id
            and other.exists
            and other.root_dir != source.root_dir
            and _is_descendant(other.root_dir, source.root_dir)
        ]

        for path in iter_json_files(source, nested_source_roots=nested_roots):
            entries.append(
                build_manifest_entry(
                    source,
                    path,
                    documentation_root,
                    viewer_root,
                )
            )

    entries.sort(
        key=lambda item: (
            item["archived"],
            item["sourceId"].casefold(),
            item["folder"].casefold(),
            item["title"].casefold(),
            item["path"].casefold(),
        )
    )

    valid_count = sum(1 for entry in entries if entry["validJson"])
    invalid_count = len(entries) - valid_count
    archived_count = sum(1 for entry in entries if entry["archived"])

    record_type_counts: dict[str, int] = {}
    source_counts: dict[str, int] = {source.source_id: 0 for source in sources}
    companion_counts: dict[str, int] = {
        "resolved": 0,
        "inferred": 0,
        "undeclared": 0,
        "missing": 0,
        "invalid": 0,
    }

    for entry in entries:
        record_type = entry["recordType"]
        record_type_counts[record_type] = record_type_counts.get(record_type, 0) + 1
        source_counts[entry["sourceId"]] = source_counts.get(entry["sourceId"], 0) + 1

        companion = entry.get("companionDocument")
        if isinstance(companion, dict):
            companion_status = str(companion.get("status", "undeclared"))
            companion_counts[companion_status] = companion_counts.get(companion_status, 0) + 1

    viewer_root_path = posix_relpath(viewer_root, documentation_root)

    return {
        "schemaVersion": MANIFEST_SCHEMA_VERSION,
        "manifestType": MANIFEST_TYPE,
        "generator": {
            "name": "Klinswork Documentation Viewer manifest builder",
            "version": SCRIPT_VERSION,
            "script": SCRIPT_PATH.name,
        },
        "documentation": {
            "rootName": documentation_root.name,
            "rootPath": ".",
            "viewerRootPath": viewer_root_path,
            "generatedTimestamp": utc_timestamp(),
        },
        "sources": [source.public_record() for source in sources],
        "summary": {
            "recordCount": len(entries),
            "validJsonCount": valid_count,
            "invalidJsonCount": invalid_count,
            "archivedRecordCount": archived_count,
            "sourceCounts": dict(sorted(source_counts.items())),
            "companionCounts": companion_counts,
            "recordTypeCounts": dict(sorted(record_type_counts.items())),
            "sourceErrorCount": len(source_errors),
        },
        "sourceErrors": source_errors,
        "records": entries,
    }


def write_manifest(manifest: dict[str, Any], output_file: Path) -> None:
    """Atomically write a validated UTF-8 manifest."""

    temporary_file = output_file.with_suffix(output_file.suffix + ".tmp")
    temporary_file.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    # Parse before replacing any previous output.
    json.loads(temporary_file.read_text(encoding="utf-8"))
    temporary_file.replace(output_file)


def print_report(
    manifest: dict[str, Any],
    documentation_root: Path,
    output_file: Path,
) -> None:
    summary = manifest["summary"]

    print("Klinswork Documentation Viewer manifest created successfully.")
    print()
    print(f"Builder:       {SCRIPT_VERSION}")
    print(f"Schema:        {MANIFEST_SCHEMA_VERSION}")
    print(f"Documentation: {documentation_root}")
    print(f"Output:        {output_file}")
    print(f"Records:       {summary['recordCount']}")
    print(f"Valid JSON:    {summary['validJsonCount']}")
    print(f"Invalid JSON:  {summary['invalidJsonCount']}")
    print(f"Archived:      {summary['archivedRecordCount']}")
    print()
    print("Sources:")

    for source in manifest["sources"]:
        count = summary["sourceCounts"].get(source["sourceId"], 0)
        marker = "OK" if source["exists"] else "MISSING"
        print(
            f"  - {source['sourceId']}: {count} records · {marker} · "
            f"{source['rootPath']}"
        )

    companion_counts = summary["companionCounts"]
    if any(companion_counts.values()):
        print()
        print("Companion documents:")
        for key in ("resolved", "inferred", "undeclared", "missing", "invalid"):
            print(f"  - {key}: {companion_counts.get(key, 0)}")

    if manifest["sourceErrors"]:
        print()
        print("Source warnings:")
        for item in manifest["sourceErrors"]:
            print(f"  - {item['sourceId']}: {item['error']}")

    if summary["invalidJsonCount"]:
        print()
        print("Files with JSON errors:")
        for entry in manifest["records"]:
            if not entry["validJson"]:
                print(
                    f"  - [{entry['sourceId']}] {entry['path']}\n"
                    f"    {entry['parseError']}"
                )

    integrity_problems = [
        entry
        for entry in manifest["records"]
        if isinstance(entry.get("companionDocument"), dict)
        and entry["companionDocument"].get("status") in {"missing", "invalid"}
    ]
    if integrity_problems:
        print()
        print("Companion-document integrity problems:")
        for entry in integrity_problems:
            companion = entry["companionDocument"]
            print(
                f"  - [{entry['sourceId']}] {entry['path']} · "
                f"{companion.get('status')}"
            )
            if companion.get("declaredPath"):
                print(f"    declared: {companion['declaredPath']}")
            if companion.get("error"):
                print(f"    {companion['error']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build the multi-source manifest for Klinswork Documentation Viewer 2.0 "
            "without modifying the legacy json-manifest.json."
        )
    )
    parser.add_argument(
        "--documentation-root",
        type=Path,
        default=None,
        help=(
            "Path to the repository's documentation/ directory. Defaults to the "
            "nearest ancestor named 'documentation'."
        ),
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help=(
            "Optional documentation-viewer-sources.json. Defaults to the file beside "
            "this script when present; otherwise built-in source definitions are used."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=(
            "Output manifest path. Defaults to documentation-viewer-manifest.json "
            "inside the registered Common Documentation / Viewer source."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    documentation_root = (
        args.documentation_root.expanduser().resolve()
        if args.documentation_root is not None
        else infer_documentation_root(BUILDER_ROOT).resolve()
    )
    if not documentation_root.is_dir():
        raise SystemExit(f"Documentation root does not exist: {documentation_root}")

    config_path: Path | None
    if args.config is not None:
        config_path = args.config.expanduser().resolve()
        if not config_path.is_file():
            raise SystemExit(f"Source configuration does not exist: {config_path}")
    else:
        config_path = SOURCE_CONFIG_FILE if SOURCE_CONFIG_FILE.is_file() else None

    raw_sources = load_source_config(config_path)
    viewer_root = resolve_viewer_root(documentation_root, raw_sources)
    if not viewer_root.is_dir():
        raise SystemExit(
            "Registered Viewer home does not exist: "
            f"{viewer_root}\n"
            "Check the 'common' rootPath in documentation-viewer-sources.json."
        )

    output_file = (
        args.output.expanduser().resolve()
        if args.output is not None
        else viewer_root / DEFAULT_OUTPUT_NAME
    )

    print(f"Builder version:      {SCRIPT_VERSION}")
    print(f"Builder location:     {SCRIPT_PATH}")
    print(f"Resolved Viewer home: {viewer_root}")
    print(f"Manifest output:      {output_file}")

    stale_builder_manifest = BUILDER_ROOT / DEFAULT_OUTPUT_NAME
    if (
        stale_builder_manifest.resolve() != output_file.resolve()
        and stale_builder_manifest.is_file()
    ):
        print(
            "WARNING: A stale manifest exists beside the builder: "
            f"{stale_builder_manifest}"
        )
        print(
            "         It is not the output target for this run and may be "
            "deleted after you confirm the Viewer-home manifest."
        )

    sources = make_source_specs(
        documentation_root=documentation_root,
        viewer_root=viewer_root,
        raw_sources=raw_sources,
    )

    manifest = build_manifest(
        documentation_root=documentation_root,
        viewer_root=viewer_root,
        sources=sources,
    )
    write_manifest(manifest, output_file)
    print_report(manifest, documentation_root, output_file)


if __name__ == "__main__":
    main()
