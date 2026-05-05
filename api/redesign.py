from http.server import BaseHTTPRequestHandler
import json
import sys
import os

# Add the src directory to the path so we can import the pipeline
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.core.pipeline import AssignmentRedesignPipeline

class handler(BaseHTTPRequestHandler):
    """
    Vercel Serverless Function Handler
    Exposes the Assignment Redesign Pipeline as a POST endpoint.
    """
    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            body = json.loads(post_data.decode('utf-8'))
            legacy_assignment = body.get('legacy_assignment')
            
            if not legacy_assignment:
                self._send_response(400, {"error": "Missing 'legacy_assignment' in request body."})
                return
                
            pipeline = AssignmentRedesignPipeline()
            modernized_assignment = pipeline.run(legacy_assignment)
            
            self._send_response(200, {"modernized_assignment": modernized_assignment})
            
        except json.JSONDecodeError:
            self._send_response(400, {"error": "Invalid JSON payload."})
        except Exception as e:
            self._send_response(500, {"error": str(e)})

    def _send_response(self, status_code, payload):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        # Allow CORS for potential frontend integration
        self.send_header('Access-Control-Allow-Origin', '*') 
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode('utf-8'))

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
