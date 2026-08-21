

import os
from pathlib import Path

WORKSPACE = Path(__file__).parent / "workspace"

# ensure workspace path exists
WORKSPACE.mkdir(parents=True, exist_ok=True)


def list_files_in_directory(directory_path: str) -> list:
    """
    List all files in the specified directory.

    Args:
        directory_path (str): The path to the directory.
    Returns:
        list: A list of file names in the directory.
    """
    # always use the workspace path as the base directory
    directory_path = WORKSPACE / directory_path
    try:
        return [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    except Exception as e:
        print(f"Error listing files in directory {directory_path}: {e}")
        return []

def read_file_contents(file_path: str) -> str:
    """
    Read the contents of a specified file.

    Args:
        file_path (str): The path to the file.
    Returns:
        str: The contents of the file.
    """
    # always use the workspace path as the base directory
    file_path = WORKSPACE / file_path
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

def write_file_contents(file_path: str, content: str, mode: str = 'w') -> bool:
    """
    Write content to a specified file.

    Args:
        file_path (str): The path to the file.
        content (str): The content to write to the file.
        mode (str): The mode in which to open the file.
    Returns:
        bool: True if the write was successful, False otherwise.
    """
    # always use the workspace path as the base directory
    file_path = WORKSPACE / file_path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing to file {file_path}: {e}")
        return False
