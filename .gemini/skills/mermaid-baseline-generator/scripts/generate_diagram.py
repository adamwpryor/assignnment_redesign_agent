import json
import os

def generate_mermaid_code(framework_type):
    """
    Retrieves the baseline Mermaid.js code structure for a requested framework.
    Returns the raw string data from the associated asset file.
    """
    assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
    templates_path = os.path.normpath(os.path.join(assets_dir, 'templates.json'))
    
    try:
        with open(templates_path, 'r', encoding='utf-8') as f:
            templates_data = json.load(f)
            file_map = {k: v["file"] for k, v in templates_data.get("templates", {}).items()}
    except FileNotFoundError:
        return json.dumps({
            "error": "templates.json index missing. Ensure the repository assets are intact."
        })
    
    filename = file_map.get(framework_type.lower())
    
    if not filename:
        return json.dumps({
            "error": f"Unknown framework type: '{framework_type}'. Available options: {list(file_map.keys())}"
        })
        
    asset_path = os.path.normpath(os.path.join(assets_dir, filename))
    
    try:
        with open(asset_path, 'r', encoding='utf-8') as f:
            codebase = f.read()
        return json.dumps({
            "framework": framework_type,
            "mermaid_code": codebase
        }, indent=2)
    except FileNotFoundError:
        return json.dumps({
            "error": f"Asset file missing: {asset_path}. Ensure the repository is intact."
        })

if __name__ == "__main__":
    import sys
    # Simple CLI wrapper
    if len(sys.argv) > 1:
        print(generate_mermaid_code(sys.argv[1]))
    else:
        print(json.dumps({"error": "No framework type provided. Provide 'decision_tree' or 'system_map'."}))
