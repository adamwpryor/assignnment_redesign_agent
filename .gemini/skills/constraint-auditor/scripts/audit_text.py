import json
import re
import os

def audit_assignment_constraints(assignment_text):
    """
    Crawls an assignment string to detect if it requests unverified text deliverables.
    Returns a strict PASS/FAIL evaluation based on the loaded banned_patterns.
    """
    assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
    patterns_path = os.path.normpath(os.path.join(assets_dir, 'banned_patterns.json'))
    
    try:
        with open(patterns_path, 'r', encoding='utf-8') as f:
            banned_data = json.load(f)
            banned_patterns = banned_data.get("banned_terms", [])
    except FileNotFoundError:
        return json.dumps({
            "status": "ERROR",
            "message": "Missing banned_patterns.json asset."
        })

    violations = []
    
    # Check text against strict Regex word boundaries
    for pattern in banned_patterns:
        # Use regex to match exact words/phrases ignoring case
        if re.search(r'\b' + re.escape(pattern) + r'\b', assignment_text, re.IGNORECASE):
            violations.append(pattern)
            
    if violations:
        return json.dumps({
            "status": "FAIL",
            "message": "Assignment violates pedagogy constraints by requesting unverified text formats.",
            "violations": violations
        }, indent=2)
        
    return json.dumps({
        "status": "PASS",
        "message": "No unverified text constraints detected. Delivery mechanisms appear resilient."
    }, indent=2)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(audit_assignment_constraints(text))
    else:
        print(json.dumps({"error": "No assignment text provided."}))
