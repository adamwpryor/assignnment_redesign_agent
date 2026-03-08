import os
import glob
import json

def reset_workspace():
    """Clears the output directory of all generated artifacts to prepare for a fresh run.
    
    Returns:
        str: A JSON string detailing the files deleted and the status of the operation.
    """
    output_dir = os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'output')
    output_dir = os.path.normpath(output_dir)
    
    if not os.path.exists(output_dir):
        return json.dumps({
            "status": "SUCCESS",
            "message": "Output directory does not exist, nothing to clean."
        })

    deleted_files = []
    errors = []

    # Iterate over files in the output directory
    for filepath in glob.glob(os.path.join(output_dir, '*')):
        if os.path.isfile(filepath):
            try:
                os.remove(filepath)
                deleted_files.append(os.path.basename(filepath))
            except Exception as e:
                errors.append(f"Failed to delete {os.path.basename(filepath)}: {str(e)}")

    if errors:
        return json.dumps({
            "status": "PARTIAL_SUCCESS",
            "message": "Some files could not be deleted.",
            "deleted": deleted_files,
            "errors": errors
        }, indent=2)
        
    return json.dumps({
        "status": "SUCCESS",
        "message": "Workspace output directory cleaned successfully.",
        "deleted": deleted_files
    }, indent=2)

if __name__ == "__main__":
    print(reset_workspace())
