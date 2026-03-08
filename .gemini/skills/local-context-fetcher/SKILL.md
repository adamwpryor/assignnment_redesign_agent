---
name: fetch_local_context
description: Retrieves a simulated MCP data payload containing live institutional policies to act as constraint grounding for assignments.
---

# `local-context-fetcher` Skill

This skill allows the `resilient-designer` agent to fetch a payload that acts as a mock for a Model Context Protocol (MCP) server.

## Usage

When designing an assignment, call `fetch_local_context` to retrieve specific, local data (e.g., the university's Generative AI policy, current campus events, local industry partners, or specific student demographics).

The agent MUST creatively weave this exact data into the assignment scenario to ensure the assignment cannot be answered using general LLM knowledge alone.

## Execution Modes

This skill is designed to run in two modes, depending on the host machine's capabilities:

### Mode A: Python Execution (Preferred)

Execute the script directly:
`python .gemini/skills/local-context-fetcher/scripts/fetch_policies.py`

The script will read and return the JSON payload from the assets directory.

### Mode B: Agentic Fallback (Python-less)

If you are running in an environment without a Python interpreter, **YOU (the LLM)** must perform the data retrieval manually:

1. **Read Payload:** Use your native file reading tools to access `.gemini/skills/local-context-fetcher/assets/mock_payload.json`.
2. **Ingest Data:** Read the raw JSON data directly into your context.
3. **Format Output:** If another agent requested the data, format it into a clear JSON response mimicking the Python output.
