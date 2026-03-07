---
name: calculate_predictability
description: Programmatically calculates the predictability score of an assignment based on format standardity and context availability.
---

# `predictability-scorer` Skill

This skill is used by the `vulnerability-assessor` agent to calculate how easily an LLM can automate a given legacy assignment.

## Usage

When called, this tool ingests the parsed format and context metrics to output a standardized score from 1-10.

It evaluates based on:

1. Standardity (e.g., 5-paragraph essays score high)
2. Context (e.g., historical textbook data scores high)
3. Verification (e.g., text-only deliverables score high)
