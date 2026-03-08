---
name: fetch_local_context
description: Retrieves a simulated MCP data payload containing live institutional policies to act as constraint grounding for assignments.
---

# `local-context-fetcher` Skill

This skill allows the `resilient-designer` agent to fetch a payload that acts as a mock for a Model Context Protocol (MCP) server.

## Usage

When designing an assignment, call `fetch_local_context` to retrieve specific, local data (e.g., the university's Generative AI policy, current campus events, local industry partners, or specific student demographics).

The agent MUST creatively weave this exact data into the assignment scenario to ensure the assignment cannot be answered using general LLM knowledge alone.
