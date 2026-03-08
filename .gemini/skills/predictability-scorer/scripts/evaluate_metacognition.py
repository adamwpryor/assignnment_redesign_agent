import json
import re
import os

def load_lexicon(filename):
    """Loads a JSON lexicon file from the assets directory.
    
    Args:
        filename (str): The name of the lexicon JSON file.
        
    Returns:
        dict: The parsed JSON data from the lexicon file, or an empty dictionary if not found.
    """
    assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
    try:
        with open(os.path.join(assets_dir, filename), 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def evaluate_metacognition(text):
    """Evaluates the qualitative metacognitive and relational load of an assignment.
    
    Calculates Bloom's Distribution, Constraint Density, and Freire-Hooks Relational Index.
    
    Args:
        text (str): The assignment text to evaluate.
        
    Returns:
        dict: A dictionary containing calculated metrics including blooms_ratio, 
              constraint_density, relational_index, cognitive_offload_multiplier, and feedback.
    """
    text_lower = text.lower()
    sentences = re.split(r'[.!?]+', text_lower)
    sentences = [s.strip() for s in sentences if s.strip()]
    num_sentences = len(sentences) or 1
    
    metrics = {
        "blooms_ratio": 0.0,
        "constraint_density": 0.0,
        "relational_index": 0.0,
        "cognitive_offload_multiplier": 1.0, # Base multiplier, < 1 mitigates risk, > 1 increases risk
        "feedback": []
    }

    # 1. Bloom's Taxonomy Analysis
    blooms_data = load_lexicon('blooms_taxonomy.json')
    lower_verbs = blooms_data.get('lower_order', [])
    higher_verbs = blooms_data.get('higher_order', [])
    
    lower_count = sum(1 for verb in lower_verbs if re.search(r'\b' + re.escape(verb) + r'\b', text_lower))
    higher_count = sum(1 for verb in higher_verbs if re.search(r'\b' + re.escape(verb) + r'\b', text_lower))
    
    if (lower_count + higher_count) > 0:
        metrics["blooms_ratio"] = lower_count / (lower_count + higher_count)
        if metrics["blooms_ratio"] > 0.6:
            metrics["cognitive_offload_multiplier"] *= 1.2
            metrics["feedback"].append("High concentration of lower-order thinking verbs (summarize, list). Very easy for LLMs to automate.")
        elif metrics["blooms_ratio"] < 0.3 and higher_count > 0:
            metrics["cognitive_offload_multiplier"] *= 0.8
            metrics["feedback"].append("Strong presence of higher-order verbs (design, critique). Requires synthesis difficult to automate.")

    # 2. Constraint Density Analysis
    constraint_markers = [
        "must include", "excluding", "limit to", "specifically", "require", 
        "no more than", "at least", "ensure that", "mandatory"
    ]
    constraint_count = sum(1 for marker in constraint_markers if marker in text_lower)
    metrics["constraint_density"] = constraint_count / num_sentences
    
    if metrics["constraint_density"] > 0.3:
        # High constraint limits LLM hallucination freedom
        metrics["cognitive_offload_multiplier"] *= 0.7
        metrics["feedback"].append("High constraint density detected. Specific, multi-clause constraints limit an LLM's capacity to freely hallucinate a passing grade.")
    elif metrics["constraint_density"] < 0.1:
        metrics["cognitive_offload_multiplier"] *= 1.1
        metrics["feedback"].append("Low constraint density. Open-ended prompts are easily satisfied by generic LLM generation.")

    # 3. Freire-Hooks Relational Index
    relational_data = load_lexicon('freire_hooks_lexicon.json')
    relational_markers = relational_data.get('relational_markers', [])
    
    relational_count = sum(1 for marker in relational_markers if re.search(r'\b' + re.escape(marker) + r'\b', text_lower))
    metrics["relational_index"] = relational_count / max(1, (num_sentences / 2)) # Normalize against roughly every 2 sentences
    
    if metrics["relational_index"] > 0.4:
        # High relational metrics severely hurt pure LLM automation
        metrics["cognitive_offload_multiplier"] *= 0.5
        metrics["feedback"].append("High Freire-Hooks Relational Index. The assignment demands lived experience, dialogue, or community interaction—highly resistant to AI simulation.")
    elif metrics["relational_index"] == 0:
        metrics["cognitive_offload_multiplier"] *= 1.15
        metrics["feedback"].append("Zero relational markers detected. The assignment is sterile and detached from lived experience, making it perfect for sterile AI completion.")

    return metrics

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(json.dumps(evaluate_metacognition(text), indent=2))
    else:
        print(json.dumps({"error": "No text provided."}))
