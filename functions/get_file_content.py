def get_file_content(working_directory, file_path):
    """
    Get the content of a file within the working directory.

    Args:
        working_directory (str): The base directory to search in.
        file_path (str): The path to the file to read.

    Returns:
        str: The file content or error message.
    """
    import os

    try:
        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(abs_file_path) or not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        if len(content) > 10000:
            content = content[:10000] + f'\n[...File "{file_path}" truncated at 10000 characters]'
        
        return content
    
    except Exception as e:
        return f"Error: {str(e)}"