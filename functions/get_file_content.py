import os

from google.genai import types

def get_file_content(working_directory, file_path):
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    abs_directory = os.path.abspath(working_directory)


    if not abs_file_path.startswith(abs_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(abs_file_path):
        f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10_000

    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at 10000 characters]'

        return file_content_string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the contents of the specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File to get content from, relative to the working directory.",
            ),
        },
    ),
)