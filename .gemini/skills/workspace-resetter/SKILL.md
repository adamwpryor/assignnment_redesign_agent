---
name: reset_workspace
description: Clears the output directory to prepare the workspace for a fresh pipeline run.
---

# `workspace-resetter` Skill

This skill allows the Pipeline Cleaner agent to wipe the `output/` directory, deleting generated Markdown and JSON files to prevent artifacts from previous runs from polluting a new modernization pipeline.

## Usage

When called, this tool clears all files in the output directory, ensuring a completely clean state.

## Execution Modes

This skill is designed to run in two modes, depending on the host machine's capabilities:

### Mode A: Python Execution (Preferred)

Execute the cleanup script directly:
`python .gemini/skills/workspace-resetter/scripts/reset_workspace.py`

The script will safely iterate through the `output/` folder and delete all files, returning a JSON array of the deleted filenames.

### Mode B: Agentic Fallback (Python-less)

If you are running in an environment without a Python interpreter, **YOU (the LLM)** must perform the directory cleanup manually:

1. **List Directory:** List all files inside the `output/` directory.
2. **Delete Files:** Use your native file deletion or shell command tools (e.g., `rm output/*` or equivalent) to remove all artifacts (`vulnerabilities.json`, `resilient_activities.md`, `modernized_course_blueprint.md`, etc.).
3. **Verify:** Ensure the directory is empty.
4. **Report:** Provide a list of the files you manually deleted.
