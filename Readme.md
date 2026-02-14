# DBMS-SQL-Labs (Reorganized)

This repository has been reorganized into dedicated folders by material type and lab sequence.

## Directory Layout

- `labs/`
  - Numbered lab directories (`00` to `15`) and `99_archive`
  - Quick start is now in `labs/00_quick_start/`
- `data/`
  - `data/csv/` for CSV datasets
  - `data/json/` for JSON files
  - `data/reference/` for lecture PDFs
- `sql/`
  - All SQL files are stored directly in `sql/` (no SQL subdirectories)
- `docs/`
  - Markdown documentation (`.md` only)
  - `docs/reference/` for supplemental notes
- `images/` for images and media assets
- `scripts/` for helper scripts
- `reports/` for project summaries/changelogs
- `templates/` for shared HTML templates/layouts

## Main Indexes

- [Portal](index.html)
- [Materials Map](MATERIALS_INDEX.md)
- [Lab Index](LAB_INDEX.md)
- [Quick Start Guide](labs/00_quick_start/quick_start_guide.html)

## Notes on Cleanup

- Duplicate files were removed, including duplicate format copies for the same docs (`.html` versions removed where `.md` exists).
- Duplicate notebook copies were consolidated into `labs/14_notebooks/`.
- Duplicate JS file content in lab code samples was deduplicated.
