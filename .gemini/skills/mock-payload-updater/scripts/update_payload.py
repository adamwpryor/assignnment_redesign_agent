import json
import os
import sys
from typing import Any


def _deep_merge(base: dict, overlay: dict) -> dict:
    """Recursively merges overlay into base, returning a new dict.

    Dict values are merged recursively. All other types are overwritten.
    """
    result = base.copy()
    for key, value in overlay.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def update_mock_payload(new_data_str: str) -> str:
    """Updates the simulated institutional context in mock_payload.json.

    Args:
        new_data_str: A JSON string containing the new data to merge into the payload.

    Returns:
        A JSON string confirming the update or describing an error.
    """
    assets_dir = os.path.join(
        os.path.dirname(__file__), '..', '..', 'local-context-fetcher', 'assets'
    )
    payload_path = os.path.normpath(os.path.join(assets_dir, 'mock_payload.json'))

    try:
        new_data: dict[str, Any] = json.loads(new_data_str)
    except json.JSONDecodeError as e:
        return json.dumps({"status": "ERROR", "message": f"Invalid JSON: {e}"})

    try:
        with open(payload_path, 'r', encoding='utf-8') as f:
            current_data: dict[str, Any] = json.load(f)
    except FileNotFoundError:
        current_data = {}

    merged = _deep_merge(current_data, new_data)

    try:
        with open(payload_path, 'w', encoding='utf-8') as f:
            json.dump(merged, f, indent=4)
        return json.dumps({
            "status": "SUCCESS",
            "message": "Mock payload updated successfully.",
            "data": merged
        }, indent=2)
    except IOError as e:
        return json.dumps({"status": "ERROR", "message": f"Write failed: {e}"})


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(update_mock_payload(sys.argv[1]))
    elif not sys.stdin.isatty():
        print(update_mock_payload(sys.stdin.read()))
    else:
        print(json.dumps({
            "status": "ERROR",
            "message": "Provide JSON as a CLI argument or via stdin."
        }))
