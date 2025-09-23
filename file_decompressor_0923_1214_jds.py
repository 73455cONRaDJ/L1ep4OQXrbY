# 代码生成时间: 2025-09-23 12:14:19
import os
import zipfile
import numpy as np
"""
A simple file decompressor utility using Python and NumPy.
This utility can extract files from a zip archive.
"""

def decompress_zip_file(zip_path, extract_path):
    """
    Decompress a zip file to a specified directory.

    Parameters:
    - zip_path: The path to the zip file.
    - extract_path: The directory where to extract the files.

    Returns:
    - None

    Raises:
    - FileNotFoundError: If the zip file does not exist.
    - PermissionError: If there is no permission to read the zip file or write to the extract path.
    """
    # Check if the zip file exists
    if not os.path.exists(zip_path):
        raise FileNotFoundError(f"The zip file {zip_path} does not exist.")

    # Create the extraction directory if it does not exist
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    try:
        # Open the zip file and extract all contents
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            print(f"Files have been extracted to {extract_path}")
    except zipfile.BadZipFile:
        # Handle bad zip file
        raise ValueError(f"The file {zip_path} is not a valid zip file.")
    except Exception as e:
        # Handle other exceptions
        raise e

if __name__ == '__main__':
    # Example usage
    zip_file_path = 'path_to_your_zip_file.zip'
    extraction_path = 'path_to_extraction_directory'
    try:
        decompress_zip_file(zip_file_path, extraction_path)
    except Exception as e:
        print(f"An error occurred: {e}")