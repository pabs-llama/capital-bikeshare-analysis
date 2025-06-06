from pathlib import Path

# Root of the repo
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Source code
SRC_DIR = PROJECT_ROOT / "src"

# Data folders
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw_data"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
GEO_DIR = DATA_DIR / "geo"

# Other folders
IMAGES_DIR = PROJECT_ROOT / "images"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DOCS_DIR = PROJECT_ROOT / "docs"