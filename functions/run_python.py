import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_directory = os.path.abspath(working_directory)


    if not abs_file_path.startswith(abs_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        finished_process = subprocess.run(["python3", abs_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        output = f"Running file: {file_path}"
        if finished_process.returncode != 0:
            output += f"\nProcess exited with code {finished_process.returncode}"
        
        if not finished_process.stdout:
            output += "\nNo output produced"
        else:
            output += f"\nSTDOUT: {finished_process.stdout}"
        output += f"\nSTDERR: {finished_process.stderr}"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
    