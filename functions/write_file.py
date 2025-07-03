import os

def write_file(working_directory, file_path, content):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_directory = os.path.abspath(working_directory)


    if not abs_file_path.startswith(abs_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error writing to file "{file_path}": {e}'