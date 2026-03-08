# Constraint Auditor

**Skill ID:** `CONSTRAINT_AUDITOR`
**Category:** Pedagogy

## Overview

This skill operates as a strict final guardrail for the `blueprint-compiler`. Before a redesigned assignment is pushed to the final syllabus, this script mathematically crawls the generated output searching for explicit violations of the "Process-Over-Product" pedagogical constraint.

## The Problem

Sometimes, even a well-prompted `resilient-designer` agent might slip up and generate instructions like: "Draw a system map, and *write a three-page essay* defending it." The second half of that instruction re-introduces the LLM vulnerability.

## Execution

This script (`scripts/audit_text.py`) loads an explicit JSON array (`assets/banned_patterns.json`) containing phrasing that implies static, unverified text delivery (e.g., "essay", "reflection paper", "discussion post").
If any of these patterns are triggered via regex boundary search, the script returns a hard `FAIL` status with the specific violations, forcing the orchestrator to either flag the error or re-prompt the designer.
