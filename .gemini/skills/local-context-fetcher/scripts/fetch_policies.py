import json
import os

def fetch_local_context():
    """
    Simulates an MCP server fetching institutional data.
    Loads the payload from assets/mock_payload.json.
    """
    assets_dir = os.path.join(os.path.dirname(__file__), '..', 'assets')
    payload_path = os.path.normpath(os.path.join(assets_dir, 'mock_payload.json'))
    
    try:
        with open(payload_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        return json.dumps({
            "status": "SUCCESS",
            "source": "Mock_MCP_Endpoint",
            "data": data
        }, indent=2)
    except FileNotFoundError:
        return json.dumps({
            "status": "ERROR",
            "message": "Mock payload asset not found."
        })

if __name__ == "__main__":
    print(fetch_local_context())
