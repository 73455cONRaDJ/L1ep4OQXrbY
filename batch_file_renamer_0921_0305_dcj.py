# 代码生成时间: 2025-09-21 03:05:26
import os
import re
import shutil

"""
A batch file renamer tool using Python and NumPy.
This script takes a directory path and a prefix, and renames all files in the directory
with the provided prefix followed by a unique incremental number.
"""

def rename_files(directory, prefix):
    """Rename files in a directory with a given prefix and an incremental number.

    Args:
        directory (str): The path to the directory containing files to rename.
        prefix (str): The prefix to be added to each file name.
    """
    # Check if the provided directory exists
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")

    # Get all files in the directory
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]

    # Sort files by name to maintain order
    files.sort()

    # Rename files with the given prefix and an incremental number
    for index, file in enumerate(files, start=1):
        new_name = f"{prefix}{index:04d}{os.path.splitext(file)[1]}"
        src_path = os.path.join(directory, file)
        dst_path = os.path.join(directory, new_name)
        shutil.move(src_path, dst_path)
        print(f"Renamed {file} to {new_name}")

def main():
    # Example usage: rename files in the current directory with prefix 'file'
    directory = input("Enter the directory path: ")
    prefix = input("Enter the prefix for the file names: ")
    try:
        rename_files(directory, prefix)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
