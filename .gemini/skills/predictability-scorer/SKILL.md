---
name: calculate_predictability
description: Programmatically calculates the predictability score of an assignment based on format standardity and context availability.
---

# `predictability-scorer` Skill

This skill is used by the `vulnerability-assessor` agent to calculate how easily an LLM can automate a given legacy assignment.

## Usage

When called, this tool ingests the assigned text and calculates how easily an LLM can automate it.

## Execution Modes

This skill is designed to run in two modes, depending on the host machine's capabilities:

### Mode A: Python Execution (Preferred)

If you have access to a local Python environment (e.g., via a `run_command` or sandbox tool), execute:
`python .gemini/skills/predictability-scorer/scripts/evaluate_predictability.py` passing the assignment text via standard input.

### Mode B: Agentic Fallback (Python-less)

If you are running in an environment without a Python interpreter, **YOU (the LLM)** must act as the heuristic execution engine.

1. **Load Lexicons:** Read the raw JSON of `assets/blooms_taxonomy.json` and `assets/freire_hooks_lexicon.json` into your context.
2. **Structural Base Score (1-10):**
    * Standard format (essay/discussion) = +3 Risk
    * Lacks local/recent context = +4 Risk
    * Purely text-based output = +3 Risk
3. **Metacognitive Load (Multiplier):** Read the input text. Count the ratio of lower-order to higher-order Bloom's verbs. If lower-order dominates > 60%, multiply the Base Score by 1.2. If higher-order dominates > 70%, multiply by 0.8.
4. **Constraint Density (Multiplier):** Look for limiting clauses (must include, limit to). If high, multiply by 0.7. If low/open-ended, multiply by 1.1.
5. **Freire-Hooks Relational Index (Multiplier):** Scan for relational markers (lived experience, dialogue, power dynamic). If detected frequently (> 1 per 3 sentences), multiply score by 0.5. If 0 markers, multiply by 1.15.
6. **Final Output:** Cap the multiplied final score between 1.0 and 10.0 and output a `vulnerabilities.json` payload detailing your math.
