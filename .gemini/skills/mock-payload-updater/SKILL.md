---
name: update_mock_payload
description: Updates the local context mock payload with new institutional data.
---

# `mock-payload-updater` Skill

This skill enables the Context Manager agent to inject new, hyper-local variables into the simulated institution's environment data (`mock_payload.json`).

## Usage

When called, this tool ingests a JSON string representing new policies, demographics, or context variables and merges them into the existing payload. This is crucial for maintaining the "Zero-Trust" simulated Model Context Protocol (MCP) server used by the Resilient Designer.

## Execution Modes

This skill is designed to run in two modes, depending on the host machine's capabilities:

### Mode A: Python Execution (Preferred)

Execute the underlying script, passing the new JSON data as a string argument:
`python .gemini/skills/mock-payload-updater/scripts/update_payload.py '{"local_context_variables": {"new_challenge": "Lack of study spaces"}}'`

The script will automatically parse the JSON, locate `mock_payload.json` in the `local-context-fetcher` assets directory, and perform a deep merge of the new keys.

### Mode B: Agentic Fallback (Python-less)

If you are running in an environment without a Python interpreter, **YOU (the LLM)** must perform the file manipulation manually using standard file write tools:

1. **Read Current State:** Read the contents of `.gemini/skills/local-context-fetcher/assets/mock_payload.json`.
2. **Merge Data:** In your memory, parse the existing JSON and merge the new user-provided context into the appropriate keys (e.g., `active_policies`, `local_context_variables`).
3. **Write State:** Overwrite `.gemini/skills/local-context-fetcher/assets/mock_payload.json` with the newly formatted JSON string.
4. **Confirm:** Report success to the user.
