---
name: generate_mermaid_code
description: Spins up baseline visual frameworks (as code) that students will be required to modify and defend.
---

# `mermaid-baseline-generator` Skill

This skill is used by the `resilient-designer` agent when constructing assignments that require visual framework deliverables.

## Usage

When an assignment requires a "Visual Framework Defense," the Resilient Designer calls this tool to quickly draft the baseline Mermaid.js code that serves as the "AI's first pass" for the student to critique and inherently break.

The `generate_mermaid_code` command expects a `framework_type` string. View the `assets/templates.json` index to see the full list of available keys (e.g., `decision_tree`, `system_map`, `gantt_chart`, `entity_relationship`). The script returns the corresponding `.mmd` string structure.
