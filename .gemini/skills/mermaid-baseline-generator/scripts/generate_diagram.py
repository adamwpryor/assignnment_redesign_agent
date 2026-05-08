import json
import os
import sys


def list_templates() -> str:
    """Returns a JSON string listing all available Mermaid template names and descriptions.

    Returns:
        A JSON string with a 'templates' key mapping name to description.
    """
    assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
    templates_path = os.path.normpath(os.path.join(assets_dir, 'templates.json'))

    try:
        with open(templates_path, 'r', encoding='utf-8') as f:
            templates_data = json.load(f)
        summary = {
            k: v.get("description", "") if isinstance(v, dict) else v
            for k, v in templates_data.get("templates", {}).items()
        }
        return json.dumps({"available_templates": summary}, indent=2)
    except FileNotFoundError:
        return json.dumps({"error": "templates.json index missing."})


def generate_mermaid_code(framework_type: str) -> str:
    """Retrieves the baseline Mermaid.js code structure for a requested framework.

    Pass "list" as framework_type to enumerate available options without error.

    Args:
        framework_type: The name of the visual framework (e.g. 'decision_tree'),
                        or "list" to see all available templates.

    Returns:
        A JSON string with the framework type and its raw Mermaid.js code,
        or an error/listing if the type is unknown or an asset is missing.
    """
    if framework_type.lower() == "list":
        return list_templates()

    assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
    templates_path = os.path.normpath(os.path.join(assets_dir, 'templates.json'))

    try:
        with open(templates_path, 'r', encoding='utf-8') as f:
            templates_data = json.load(f)
            file_map = {
                k: v["file"] if isinstance(v, dict) else v
                for k, v in templates_data.get("templates", {}).items()
            }
    except FileNotFoundError:
        return json.dumps({"error": "templates.json index missing. Ensure repository assets are intact."})

    filename = file_map.get(framework_type.lower())

    if not filename:
        return json.dumps({
            "error": f"Unknown framework type: '{framework_type}'.",
            "available": list(file_map.keys()),
            "hint": "Pass 'list' to see all templates with descriptions."
        })

    asset_path = os.path.normpath(os.path.join(assets_dir, filename))

    try:
        with open(asset_path, 'r', encoding='utf-8') as f:
            code = f.read()
        return json.dumps({"framework": framework_type, "mermaid_code": code}, indent=2)
    except FileNotFoundError:
        return json.dumps({"error": f"Asset file missing: {filename}. Repository may be incomplete."})


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(generate_mermaid_code(sys.argv[1]))
    else:
        print(list_templates())
