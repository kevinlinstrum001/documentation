#!/usr/bin/env python3
"""
build_repository_tree.py

Generate a deterministic text tree of the repository containing this script.

Intended location:
    documentation/build_repository_tree.py

Output:
    documentation/repository-tree.txt

The tree is a physical inventory only: it shows directory and file names.
It does not attempt to describe semantic ownership, authority, generators,
consumers, project membership, or other repository relationships.
"""

from pathlib import Path

OUTPUT_FILENAME = "repository-tree.txt"

# Local/runtime directories that are not part of the useful repository tree.
# .github is intentionally NOT excluded because it can be real repository content.
EXCLUDED_DIRECTORIES = {
    ".git",
    "__pycache__",
}

# Generated/local files that should not appear in their own generated tree.
EXCLUDED_FILES = {
    OUTPUT_FILENAME,
}


def sort_key(path: Path):
    """Directories first, then files; alphabetic within each group."""
    return (0 if path.is_dir() else 1, path.name.casefold())


def visible_children(directory: Path):
    """Return sorted children after applying the small exclusion list."""
    children = []

    for child in directory.iterdir():
        if child.is_dir() and child.name in EXCLUDED_DIRECTORIES:
            continue

        if child.is_file() and child.name in EXCLUDED_FILES:
            continue

        children.append(child)

    return sorted(children, key=sort_key)


def add_tree(directory: Path, lines: list[str], prefix: str = ""):
    """Recursively append tree lines beneath directory."""
    children = visible_children(directory)

    for index, child in enumerate(children):
        is_last = index == len(children) - 1
        connector = "└── " if is_last else "├── "

        if child.is_symlink():
            target = child.readlink()
            lines.append(f"{prefix}{connector}{child.name} -> {target}")
            continue

        if child.is_dir():
            lines.append(f"{prefix}{connector}{child.name}/")
            extension = "    " if is_last else "│   "
            add_tree(child, lines, prefix + extension)
        else:
            lines.append(f"{prefix}{connector}{child.name}")


def build_tree(root: Path) -> str:
    """Build the complete tree text."""
    lines = [f"{root.name}/"]
    add_tree(root, lines)
    return "\n".join(lines) + "\n"


def main():
    root = Path(__file__).resolve().parent
    output_path = root / OUTPUT_FILENAME

    tree_text = build_tree(root)
    output_path.write_text(tree_text, encoding="utf-8")

    file_count = sum(
        1
        for p in root.rglob("*")
        if p.is_file()
        and ".git" not in p.parts
        and "__pycache__" not in p.parts
        and p.name not in EXCLUDED_FILES
    )

    directory_count = sum(
        1
        for p in root.rglob("*")
        if p.is_dir()
        and ".git" not in p.parts
        and "__pycache__" not in p.parts
    )

    print(f"Repository tree written to: {output_path}")
    print(f"Directories: {directory_count}")
    print(f"Files: {file_count}")


if __name__ == "__main__":
    main()
