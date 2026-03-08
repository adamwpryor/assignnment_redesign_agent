---
name: audit_assignment_constraints
description: Crawls generated assignments and flags any deliverable that looks like an unverified text document.
---

# `constraint-auditor` Skill

This skill is an automated guardrail used by the `blueprint-compiler` agent before compiling the final syllabus.

## Usage

It scans the text of the redesigned assignments searching for banned terminology or implied textual deliverables (e.g., "Write an essay", "Submit a Word document", "Draft a critique"). If flagged, it throws a validation error preventing compilation, ensuring the process-over-product rule is strictly enforced.

## Execution Modes

This skill is designed to run in two modes:

### Mode A: Python Execution (Preferred)

Execute `python .gemini/skills/constraint-auditor/scripts/audit_text.py` passing the assignment text via standard input.

### Mode B: Agentic Fallback (Python-less)

If you are running in an environment without a Python interpreter, **YOU (the LLM)** must act as the auditor natively.

1. Read the raw JSON of `assets/banned_patterns.json` into your context.
2. Scan the generated text meticulously for the exact strings and regex patterns defined in the JSON.
3. If *any* pattern is found, trigger a validation error and return the text for revision. If clean, approve the blueprint compilation.
