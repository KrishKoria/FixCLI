import os

def write_file(working_directory, file_path, content):
    """
    Write content to a file within the working directory.
    Args:
        working_directory (str): The base directory to write in.
        file_path (str): The path to the file to write.
        content (str): The content to write to the file.
    Returns:
        str: Success message or error message.
    """
    try:
        abs_working_dir = os.path.abspath(working_directory)
        
        if not os.path.isabs(file_path):
            abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        else:
            abs_file_path = os.path.abspath(file_path)
        
        if not abs_file_path.startswith(abs_working_dir + os.sep) and abs_file_path != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        file_dir = os.path.dirname(abs_file_path)
        if file_dir and not os.path.exists(file_dir):
            os.makedirs(file_dir)
        
        with open(abs_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f'Error: {str(e)}'