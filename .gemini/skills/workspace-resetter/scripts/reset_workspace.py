import json
from pathlib import Path


def _find_project_root() -> Path:
    """Walks up from this script's location looking for the GEMINI.md bootloader."""
    candidate = Path(__file__).resolve().parent
    for _ in range(6):
        if (candidate / "GEMINI.md").exists() or (candidate / "CLAUDE.md").exists():
            return candidate
        candidate = candidate.parent
    # Fallback: 4 levels up from scripts/ is the project root in the standard layout
    # scripts/ -> workspace-resetter/ -> skills/ -> .gemini/ -> project root
    return Path(__file__).resolve().parents[3]


def reset_workspace() -> str:
    """Clears the output directory of all generated artifacts.

    Returns:
        A JSON string detailing deleted files and the operation status.
    """
    output_dir = _find_project_root() / "output"

    if not output_dir.exists():
        return json.dumps({
            "status": "SUCCESS",
            "message": "Output directory does not exist, nothing to clean.",
            "deleted": []
        })

    deleted_files = []
    errors = []

    for filepath in output_dir.glob("*"):
        if filepath.is_file():
            try:
                filepath.unlink()
                deleted_files.append(filepath.name)
            except Exception as e:
                errors.append(f"Failed to delete {filepath.name}: {e}")

    if errors:
        return json.dumps({
            "status": "PARTIAL_SUCCESS",
            "message": "Some files could not be deleted.",
            "deleted": deleted_files,
            "errors": errors
        }, indent=2)

    return json.dumps({
        "status": "SUCCESS",
        "message": "Workspace output directory cleaned successfully.",
        "deleted": deleted_files
    }, indent=2)


if __name__ == "__main__":
    print(reset_workspace())
