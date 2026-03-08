# Predictability Scorer

**Skill ID:** `predictability-scorer`
**Category:** Pedagogy

## Overview

The Predictability Scorer is a quantitative evaluation tool used by the `vulnerability-assessor` agent. It moves away from subjective LLM evaluation ("vibes") and uses a deterministic Python script (`scripts/evaluate_predictability.py`) to calculate how easily an AI could complete a legacy assignment.

## Scoring Matrix

The tool evaluates input assignment text against three primary vectors, scoring from 1 (Resilient) to 10 (Highly Predictable):

1. **Format Standardity (+3 Risk):** Does the assignment request a format deeply embedded in LLM training data (e.g., essays, reports, discussion posts)?
2. **Context Availability (+4 Risk):** Does the assignment rely on general historical/factual knowledge, or does it require grounding in local, live, or personal context not available to the model?
3. **Deliverable Type (+3 Risk):** Is the requested output purely text-based, or does it demand a multimodal or verifiable defense (e.g., video, oral presentation, visual maps)?

## Usage in Pipeline

The `vulnerability-assessor` must pass the raw text of the legacy assignment to this script. The script returns a JSON payload containing the definitive `predictability_score`, `risk_level`, and specific `feedback` strings explaining *why* the assignment is vulnerable.
