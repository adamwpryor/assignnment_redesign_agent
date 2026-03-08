import json
import os
import sys

def update_mock_payload(new_data_str):
    """Updates the simulated institutional context in mock_payload.json.
    
    Args:
        new_data_str (str): A JSON string containing the new data to merge into the payload.
        
    Returns:
        str: A JSON string confirming the update or describing an error.
    """
    assets_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'local-context-fetcher', 'assets')
    payload_path = os.path.normpath(os.path.join(assets_dir, 'mock_payload.json'))
    
    try:
        new_data = json.loads(new_data_str)
    except json.JSONDecodeError as e:
        return json.dumps({
            "status": "ERROR",
            "message": f"Invalid JSON provided: {str(e)}"
        })

    try:
        with open(payload_path, 'r', encoding='utf-8') as f:
            current_data = json.load(f)
    except FileNotFoundError:
        current_data = {}

    # Simple dictionary merge for top-level keys. 
    # If the key contains a dictionary, merge one level deeper.
    for key, value in new_data.items():
        if key in current_data and isinstance(current_data[key], dict) and isinstance(value, dict):
            current_data[key].update(value)
        else:
            current_data[key] = value

    try:
        with open(payload_path, 'w', encoding='utf-8') as f:
            json.dump(current_data, f, indent=4)
        return json.dumps({
            "status": "SUCCESS",
            "message": "Mock payload updated successfully.",
            "data": current_data
        }, indent=2)
    except IOError as e:
         return json.dumps({
            "status": "ERROR",
            "message": f"Failed to write to mock_payload.json: {str(e)}"
        })

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(update_mock_payload(sys.argv[1]))
    else:
        print(json.dumps({"status": "ERROR", "message": "No JSON update string provided."}))
