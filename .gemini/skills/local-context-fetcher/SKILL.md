---
name: fetch_local_context
description: Simulates an MCP database lookup to return hyper-local institutional data (dummy data for demonstration).
---

# `fetch_local_context` Skill

This skill acts as a mock Model Context Protocol (MCP) server for the `assignnment_redesign_agent`. Its purpose is to provide the `resilient-designer` agent with verified, hyper-local constraints that an LLM would not possess in its standard pre-training corpus.

## Usage

When called, this tool should output a standard JSON payload representing specific local constraints. In a production environment, this would query a real institutional database, Canvas LMS, or local intranet search.

## Simulated Payload

```json
{
  "institution_name": "Midwestern University",
  "current_semester": "Spring 2026",
  "active_strategic_initiatives": [
    "Community AI Readiness",
    "Zero-Trust Academic Integrity",
    "Rural Healthcare Administration"
  ],
  "local_policy_updates": {
    "date": "2026-02-15",
    "policy_name": "Student Use of Generative AI in Assignments V2",
    "key_constraint": "Students must document AI usage using the 'Artifact as Blueprint' or 'In-Browser Demonstration' rubric formats. Raw AI text submissions result in an automatic academic review."
  },
  "hyper_local_datasets_available": [
    "2025 City of Springfield Town Hall Minutes",
    "Midwestern University Energy Grid Usage Data (Anonymized)"
  ]
}
```
