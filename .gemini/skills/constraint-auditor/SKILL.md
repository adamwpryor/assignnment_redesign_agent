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

### Mode B: Agentic Fallback (Python-less, RECOMMENDED)

*Note: Mode B is highly recommended over Mode A for this skill, as LLMs excel at semantic evaluation whereas the Python script is limited to string matching.*

If you are running in an environment without a Python interpreter, **YOU (the LLM)** must act as the nuanced semantic auditor.

1. Read the raw JSON of `assets/banned_patterns.json` into your context to understand the *intent* of the ban.
2. **Semantic Evaluation:** Does the deliverable *feel* like something a student could accomplish simply by copying the prompt into ChatGPT and pasting the response into a Word document? (e.g., "Craft a narrative," "Reflect on," "Synthesize your thoughts into a brief statement.")
3. If the core deliverable is an unverified block of text, trigger a validation error and return the text for revision. If the deliverable is structurally resilient (a diagram, live code, an ADR), approve the blueprint compilation.
