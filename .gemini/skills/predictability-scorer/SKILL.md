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

If you are running in an environment without a Python interpreter, **YOU (the LLM)** must act as the heuristic execution engine and output a JSON array assessing the vulnerability.

1. **Load Lexicons:** Read the raw JSON of `assets/blooms_taxonomy.json` and `assets/freire_hooks_lexicon.json` into your context.
2. **Initial Risk Band Assessment (Low, Medium, High, Critical):**
    * Standard format (essay/discussion)? -> Set baseline to Medium/High.
    * Lacks local/recent context? -> Escalate risk by one band.
    * Purely text-based output? -> Escalate risk by one band.
3. **Metacognitive Load (Semantic Evaluation):** Read the input text. If lower-order Bloom's verbs dominate (Define, List, Summarize), escalate risk by one band. If higher-order dominates (Synthesize, Evaluate), lower risk by one band.
4. **Constraint Density:** If the prompt has highly specific limiting clauses ("must include X, Y, Z specific metrics"), lower the risk by one band. If open-ended, maintain or elevate.
5. **Relational Index:** Scan for relational markers (lived experience, dialogue). If present frequently, lower the risk.
6. **Final Output:** Output a `vulnerabilities.json` payload listing each assignment with its final `qualitative_risk_band` (Low, Medium, High, Critical) and the specific reasoning (feedback) detailing your semantic evaluation.
