import json
import re

def evaluate_predictability(assignment_text):
    """
    Evaluates an assignment for cognitive offload potential (predictability).
    Scores from 1 (highly resilient) to 10 (highly predictable/automatable).
    """
    score = 0
    feedback = []

    # 1. Format Standardity (Does it ask for a common LLM output format?)
    standard_formats = [
        r"\bessay\b", r"\bpaper\b", r"\breport\b", 
        r"\bsummary\b", r"\bcritique\b", r"\bdiscussion post\b"
    ]
    for pattern in standard_formats:
        if re.search(pattern, assignment_text, re.IGNORECASE):
            score += 3
            feedback.append(f"High risk format detected: Matches pattern '{pattern}'. LLMs excel at standard text products.")
            break

    # 2. Context Availability (Is the knowledge widely available?)
    # Heuristic: If it doesn't specify using local, personal, or novel data, it's likely general knowledge.
    local_context_markers = [
        r"\bpersonal experience\b", r"\binterview\b", r"\blocal community\b",
        r"\bclass discussion\b", r"\blive observation\b", r"\bcurrent events\b"
    ]
    has_local_context = any(re.search(p, assignment_text, re.IGNORECASE) for p in local_context_markers)
    if not has_local_context:
        score += 4
        feedback.append("Missing local context markers. The assignment likely relies on generalized training data knowledge.")

    # 3. Deliverable Type (Is it entirely text-based?)
    # Heuristic: Does it ask for a video, presentation, oral defense, or visual?
    resilient_deliverables = [
        r"\bvideo\b", r"\bpresentation\b", r"\boral\b", r"\bdefense\b",
        r"\bdiagram\b", r"\bmap\b", r"\bcode\b"
    ]
    has_resilient_deliverable = any(re.search(p, assignment_text, re.IGNORECASE) for p in resilient_deliverables)
    if not has_resilient_deliverable:
        score += 3
        feedback.append("Deliverable appears to be text-only. Text is the native output of generative AI.")

    # Normalize score to 1-10
    final_score = max(1, min(10, score))
    
    return json.dumps({
        "predictability_score": final_score,
        "risk_level": "High" if final_score >= 7 else "Medium" if final_score >= 4 else "Low",
        "feedback": feedback
    }, indent=2)

if __name__ == "__main__":
    import sys
    # Simple CLI wrapper
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(evaluate_predictability(text))
    else:
        print(json.dumps({"error": "No assignment text provided."}))
