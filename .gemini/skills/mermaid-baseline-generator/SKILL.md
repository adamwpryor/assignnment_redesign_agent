---
name: generate_mermaid_code
description: Spins up baseline visual frameworks (as code) that students will be required to modify and defend.
---

# `mermaid-baseline-generator` Skill

This skill is used by the `resilient-designer` agent when constructing assignments that require visual framework deliverables.

## Usage

When an assignment requires a "Visual Framework Defense," the Resilient Designer calls this tool to quickly draft the baseline Mermaid.js code that serves as the "AI's first pass" for the student to critique and inherently break.

The `generate_mermaid_code` command expects a `framework_type` string. View the `assets/templates.json` index to see the full list of available keys (e.g., `decision_tree`, `system_map`, `gantt_chart`, `entity_relationship`). The script returns the corresponding `.mmd` string structure.

## Output Constraints

When the Resilient Designer embeds this Mermaid code into a final markdown document, it MUST adhere to the following syntax rules to prevent rendering crashes in standard LMS systems (Canvas, Blackboard):

1. **NO INLINE COMMENTS**: Never include `%%` comments inside the ` ```mermaid ` code block. Markdown parsers often fail when encountering them. Place instructions *outside* the code block.
2. **STRICT QUOTATIONS**: All node text and edge labels must be enclosed in double quotes.
    * *Correct Node:* `A["Start: Initial Concept"]`
    * *Incorrect Node:* `A[Start: Initial Concept]`
    * *Correct Edge:* `B -->|"Option X"| C`
    * *Incorrect Edge:* `B -- Option X --> C`
