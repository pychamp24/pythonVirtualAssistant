import os
import subprocess
def open_file(file_name):
    try:
        for root, dirs, files in os.walk("."):
            if file_name in files:
                file_path = os.path.join(root, file_name)
                
                if os.name == 'nt':
                    os.startfile(file_path)
                
                return f"Opening {file_name}."
        
        return f"File '{file_name}' not found."
    except Exception as e:
        return "There was an error opening the file."