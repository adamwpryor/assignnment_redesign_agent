import json
import re
import sys
import os

# Ensure sibling scripts are importable regardless of CWD
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evaluate_metacognition import evaluate_metacognition


def evaluate_predictability(assignment_text: str) -> str:
    """Evaluates an assignment for cognitive offload potential (predictability).

    Args:
        assignment_text: The assignment text to evaluate.

    Returns:
        A JSON string containing the cognitive_offload_probability_score (1–10),
        risk_level, textual feedback, and raw metrics.
    """
    score = 0
    feedback = []

    # 1. Format Standardity — does it ask for a common LLM output format?
    standard_formats = [
        r"\bessay\b", r"\bpaper\b", r"\breport\b",
        r"\bsummary\b", r"\bcritique\b", r"\bdiscussion post\b"
    ]
    for pattern in standard_formats:
        if re.search(pattern, assignment_text, re.IGNORECASE):
            score += 3
            feedback.append(
                f"High risk format detected: matches '{pattern}'. "
                "LLMs excel at standard text products."
            )
            break

    # 2. Context Availability — is the knowledge widely available?
    local_context_markers = [
        r"\bpersonal experience\b", r"\binterview\b", r"\blocal community\b",
        r"\bclass discussion\b", r"\blive observation\b", r"\bcurrent events\b"
    ]
    has_local_context = any(
        re.search(p, assignment_text, re.IGNORECASE) for p in local_context_markers
    )
    if not has_local_context:
        score += 4
        feedback.append(
            "Missing local context markers. Assignment likely relies on "
            "generalized training data knowledge."
        )

    # 3. Deliverable Type — is it entirely text-based?
    resilient_deliverables = [
        r"\bvideo\b", r"\bpresentation\b", r"\boral\b", r"\bdefense\b",
        r"\bdiagram\b", r"\bmap\b", r"\bcode\b"
    ]
    has_resilient_deliverable = any(
        re.search(p, assignment_text, re.IGNORECASE) for p in resilient_deliverables
    )
    if not has_resilient_deliverable:
        score += 3
        feedback.append("Deliverable appears text-only. Text is the native output of generative AI.")

    base_score = score

    # 4. Integrate metacognitive and relational load
    meta_metrics = evaluate_metacognition(assignment_text)
    final_score = base_score * meta_metrics.get("cognitive_offload_multiplier", 1.0)
    feedback.extend(meta_metrics.get("feedback", []))

    # Derive qualitative risk band before capping
    if final_score >= 8:
        risk_band = "Critical"
    elif final_score >= 6:
        risk_band = "High"
    elif final_score >= 3:
        risk_band = "Medium"
    else:
        risk_band = "Low"

    final_score = max(1.0, min(10.0, final_score))

    return json.dumps({
        "qualitative_risk_band": risk_band,
        "cognitive_offload_probability_score": round(final_score, 1),
        "feedback": feedback,
        "raw_metrics": {
            "structural_base_score": base_score,
            "blooms_ratio": meta_metrics.get("blooms_ratio", 0),
            "constraint_density": meta_metrics.get("constraint_density", 0),
            "freire_hooks_index": meta_metrics.get("relational_index", 0)
        }
    }, indent=2)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Score an assignment for AI cognitive-offload risk."
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--file", "-f", help="Path to assignment text file")
    group.add_argument("text", nargs="?", help="Assignment text (inline)")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as fh:
            text = fh.read()
    elif args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        parser.print_help()
        sys.exit(1)

    print(evaluate_predictability(text))
