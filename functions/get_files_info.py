import os
from google.genai import types

def get_files_info(working_directory, directory=None):
    abs_working_path = os.path.abspath(working_directory)
    abs_path = abs_working_path
    if directory:
        abs_path = os.path.abspath(os.path.join(working_directory, directory))

    if abs_working_path not in abs_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_path):
        return f'Error: "{directory}" is not a directory'
    
    string_list = []
    items = os.listdir(abs_path)
    try:
        for item in items:
            string_list.append(get_info(os.path.join(abs_path, item), item))

        return "\n".join(string_list)
    except Exception as e:
        return f"Error listing files: {e}"
    
def get_info(abs_path, file_name):
    return f"- {file_name}: file_size={os.path.getsize(abs_path)}, is_dir={os.path.isdir(abs_path)}"

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)