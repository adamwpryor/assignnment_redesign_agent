# Predictability Scorer

**Skill ID:** `predictability-scorer`
**Category:** Pedagogy

## Overview

The Predictability Scorer is a quantitative evaluation tool used by the `vulnerability-assessor` agent. It moves away from subjective LLM evaluation ("vibes") and uses a deterministic Python script (`scripts/evaluate_predictability.py`) to calculate how easily an AI could complete a legacy assignment.

## The Scoring Algorithm

The tool evaluates input assignment text along two primary axes: Structural Predictability and Metacognitive/Relational Load. It returns a definitive `cognitive_offload_probability_score` from 1.0 (Highly Resilient) to 10.0 (Highly Automatable).

### Axis 1: Structural Scan (`evaluate_predictability.py`)

1. **Format Standardity (+3 Risk):** Does the assignment request a format deeply embedded in LLM training data (e.g., essays, reports, discussion posts)?
2. **Context Availability (+4 Risk):** Does the assignment rely on general historical/factual knowledge lacking specific local grounding?
3. **Deliverable Type (+3 Risk):** Is the requested output purely text-based, or does it demand a multimodal/verifiable defense?

### Axis 2: Metacognitive & Relational Load (`evaluate_metacognition.py`)

This axis applies Data-Science inspired NLP heuristics to act as a multiplier against the base structural score:

1. **Bloom's Taxonomy Distribution:** Scans `assets/blooms_taxonomy.json` to calculate the ratio of Lower-Order vs. Higher-Order thinking verbs. High concentrations of lower-order synthesis *increase* offload probability.
2. **Constraint Density:** Calculates the ratio of conditional/limiting clauses to total sentences. Open-ended prompts are easily hallucinated; dense, complex constraints *decrease* offload probability.
3. **Freire-Hooks Relational Index:** Scans `assets/freire_hooks_lexicon.json` evaluating how much the assignment invites lived experience, dialogic interaction, and community context. High relationality severely *decreases* an LLM's capacity to automate an authentic response.

## Usage in Pipeline

The `vulnerability-assessor` must pass the raw text of the legacy assignment to the master script. The script returns a JSON payload containing the final aggregated score and specific, actionable `feedback` strings explaining exactly *where* the pedagogy fails or succeeds.
