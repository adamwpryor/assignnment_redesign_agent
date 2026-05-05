import os
import json
from google import genai
from google.genai import types

class AssignmentRedesignPipeline:
    def __init__(self):
        # Initialize the new Google GenAI client
        # Relies on GEMINI_API_KEY environment variable being set
        self.client = genai.Client()
        self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        
    def _read_persona(self, agent_name):
        path = os.path.join(self.base_dir, '.gemini', 'agents', agent_name, 'persona.md')
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

    def run(self, legacy_assignment: str) -> str:
        """
        Executes the 3-agent pipeline:
        1. Vulnerability Assessor
        2. Resilient Designer
        3. Blueprint Compiler
        """
        print("Starting Assignment Redesign Pipeline...")
        
        # ---------------------------------------------------------
        # Agent 1: Vulnerability Assessor
        # ---------------------------------------------------------
        print("Running Vulnerability Assessor...")
        assessor_persona = self._read_persona('vulnerability-assessor')
        assessor_prompt = f"Analyze the following legacy assignment:\n\n{legacy_assignment}"
        
        assessor_response = self.client.models.generate_content(
            model='gemini-2.5-pro',
            contents=assessor_prompt,
            config=types.GenerateContentConfig(
                system_instruction=assessor_persona,
                response_mime_type="application/json",
            ),
        )
        vulnerabilities_json = assessor_response.text
        
        # ---------------------------------------------------------
        # Agent 2: Resilient Designer
        # ---------------------------------------------------------
        print("Running Resilient Designer...")
        designer_persona = self._read_persona('resilient-designer')
        designer_prompt = f"Based on this vulnerability assessment, redesign the assignment using the 3-Gate PBL structure:\n\n{vulnerabilities_json}"
        
        designer_response = self.client.models.generate_content(
            model='gemini-2.5-pro',
            contents=designer_prompt,
            config=types.GenerateContentConfig(
                system_instruction=designer_persona,
            ),
        )
        resilient_activities_md = designer_response.text
        
        # ---------------------------------------------------------
        # Agent 3: Blueprint Compiler
        # ---------------------------------------------------------
        print("Running Blueprint Compiler...")
        compiler_persona = self._read_persona('blueprint-compiler')
        compiler_prompt = f"Original Assignment:\n{legacy_assignment}\n\nProposed Redesign:\n{resilient_activities_md}\n\nPlease validate the 3-Gate structure and format the final student-facing assignment brief."
        
        compiler_response = self.client.models.generate_content(
            model='gemini-2.5-flash',
            contents=compiler_prompt,
            config=types.GenerateContentConfig(
                system_instruction=compiler_persona,
            ),
        )
        modernized_assignment_md = compiler_response.text
        
        print("Pipeline Complete.")
        return modernized_assignment_md

if __name__ == "__main__":
    # Simple CLI test
    import sys
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            legacy_text = f.read()
    else:
        legacy_text = "Write a 5-page essay on the causes of the American Civil War using at least 3 primary sources."
        
    pipeline = AssignmentRedesignPipeline()
    try:
        result = pipeline.run(legacy_text)
        print("\n--- FINAL OUTPUT ---\n")
        print(result)
    except Exception as e:
        print(f"Error running pipeline: {e}")
