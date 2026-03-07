---
name: audit_assignment_constraints
description: Crawls generated assignments and flags any deliverable that looks like an unverified text document.
---

# `constraint-auditor` Skill

This skill is an automated guardrail used by the `blueprint-compiler` agent before compiling the final syllabus.

## Usage

It scans the text of the redesigned assignments searching for banned terminology or implied textual deliverables (e.g., "Write an essay", "Submit a Word document", "Draft a critique"). If flagged, it throws a validation error preventing compilation, ensuring the process-over-product rule is strictly enforced.
