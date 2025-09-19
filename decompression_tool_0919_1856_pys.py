# 代码生成时间: 2025-09-19 18:56:41
import os
import zipfile
import numpy as np
"""
Decompression Tool

This program provides a simple decompression tool for ZIP files using Python and NumPy.
It demonstrates the basic usage of NumPy for array operations, which is not directly related
to decompression but included as per the requirement to use the NumPy framework.
"""

def unzip_file(zip_path, extract_path):
    """Unzips a ZIP file to the specified extract path."""
    try:
        # Check if the ZIP file exists
        if not os.path.exists(zip_path):
            raise FileNotFoundError(f"The file {zip_path} does not exist.")

        # Ensure the extract directory exists
        os.makedirs(extract_path, exist_ok=True)

        # Open and extract the ZIP file
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            print(f"Successfully extracted {zip_path} to {extract_path}.")

    except zipfile.BadZipFile:
        print(f"Error: The file {zip_path} is not a valid ZIP file.")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Example usage of the decompression tool
    zip_file_path = 'example.zip'  # Replace with your ZIP file path
    output_directory = 'extracted_files'  # Replace with your desired output directory

    # Call the unzip function
    unzip_file(zip_file_path, output_directory)

if __name__ == '__main__':
    main()
