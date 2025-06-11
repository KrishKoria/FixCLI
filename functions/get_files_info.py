def get_files_info(working_directory, directory=None):
    """
    Get information about files in a directory.

    Args:
        working_directory (str): The base directory to search in.
        directory (str, optional): The specific subdirectory to search in. Defaults to None.

    Returns:
        str: A string representation of the directory contents or error message.
    """
    import os

    if directory is None:
        directory = working_directory
    else:
        # Resolve absolute paths and check if directory is within working_directory
        abs_working_dir = os.path.abspath(working_directory)
        abs_directory = os.path.abspath(os.path.join(working_directory, directory))
        
        # Check if the target directory is outside the working directory
        if not abs_directory.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check if the directory exists and is actually a directory
        if not os.path.exists(abs_directory):
            return f'Error: "{directory}" is not a directory'
        
        if not os.path.isdir(abs_directory):
            return f'Error: "{directory}" is not a directory'
        
        directory = abs_directory

    try:
        items = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            is_dir = os.path.isdir(item_path)
            
            if is_dir:
                # For directories, we can use 0 or calculate the size differently
                size = 0
            else:
                size = os.path.getsize(item_path)
            
            items.append(f"- {item}: file_size={size} bytes, is_dir={is_dir}")
        
        return "\n".join(items)
    
    except Exception as e:
        return f"Error: {str(e)}"