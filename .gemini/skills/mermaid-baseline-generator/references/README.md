# Mermaid Baseline Generator

**Skill ID:** `mermaid-baseline-generator`
**Category:** Content Creation

## Overview

This skill package allows the `resilient-designer` agent to fetch pre-defined, complex Mermaid.js codebases. Rather than asking the LLM to hallucinate syntactically correct diagrams, it injects these verified assets directly into the redesigned assignment drafts.

## Included Codebases (`assets/`)

* `decision_tree_base.mmd`: A standard branching logic flowchart. Useful for historical analysis, ethical dilemmas, or clinical triage redesigns.
* `system_map_base.mmd`: A complex structural flowchart with subgraphs and database nodes. Useful for mapping biology pathways, sociological structures, or engineering architectures.

## Pedagogical Purpose

The goal is **not** to give the student a finished diagram. The goal is to provide a comprehensive structural *starting point*. The assignment will explicitly instruct the student to load this code into the live Mermaid Live Editor, break it, expand it, and defend their changes orally or via screen recording. This makes the text-generation capability of an LLM useless for completing the deliverable.
