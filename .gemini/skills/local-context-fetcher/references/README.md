# Local Context Fetcher

**Skill ID:** `local-context-fetcher`
**Category:** Project

## Overview

This skill acts as a critical Mock Model Context Protocol (MCP) server for the `resilient-designer`. To effectively ground an assignment, it cannot rely on general LLM knowledge; it must be tied to hyperspecific, local data.

## Execution

The `scripts/fetch_policies.py` script retrieves a deterministic JSON payload from `assets/mock_payload.json`. In a true production environment, this Python script would be replaced with actual SQL queries or REST API calls to a university's local database or Student Information System (SIS).

By separating the payload (`assets/`) from the logic (`scripts/`) and the prompt metadata (`SKILL.md`), we adhere to standard Software Engineering principles and ensure that the Designer agent is dealing with safe, structured data injections.
