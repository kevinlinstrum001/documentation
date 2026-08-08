from pathlib import Path

# Root directory will be created beside this script.
SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR / "therapy-component-library"

directories = [
    "sources/cpt/2024-guilford",
    "sources/cpt/2017-guilford",
    "sources/cpt/older-va",

    "sources/pst-sp/nezu",
    "sources/pst-sp/va",

    "fragments/cpt",
    "fragments/pst-sp",

    "sidecars/cpt",
    "sidecars/pst-sp",

    "assemblies",
]

print(f"Creating library at:\n{ROOT}\n")

ROOT.mkdir(exist_ok=True)

for directory in directories:
    path = ROOT / directory
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created: {path.relative_to(ROOT)}")

print("\nDirectory structure is ready.")
