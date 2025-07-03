import os

def get_files_info(working_directory, directory=None):
    path = os.path.join(working_directory, directory) 

    if os.path.abspath(working_directory) not in os.path.abspath(path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    
    string_list = []
    items = os.listdir(path)
    try:
        for item in items:
            string_list.append(get_info(os.path.join(path, item), item))

        return "\n".join(string_list)
    except Exception as e:
        return f"Error listing files: {e}"
    
def get_info(path, file_name):
    return f"- {file_name}: file_size={os.path.getsize(path)}, is_dir={os.path.isdir(path)}"