# 代码生成时间: 2025-10-12 02:14:27
import os
import zipfile
import tarfile
import gzip
from pathlib import Path

"""
A utility to decompress files using Python and NumPy.
This tool supports ZIP, GZIP, and TAR archives.
"""

class Decompressor:
    """
    A class responsible for decompressing different types of compressed files.
    """
    def __init__(self, file_path: str):
        """
        Initialize the Decompressor with the path to the compressed file.
        """
        self.file_path = Path(file_path)
        self.extracted_directory = None

    def decompress_zip(self) -> None:
        """
        Decompress a ZIP file.
        """
        try:
            with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
                zip_ref.extractall(self.file_path.parent)
                print(f"Extracted ZIP file to {self.file_path.parent}")
        except zipfile.BadZipFile:
            print(f"Error: The file {self.file_path} is not a valid ZIP file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def decompress_gz(self) -> None:
        """
        Decompress a GZIP file.
        """
        try:
            with gzip.open(self.file_path, 'rb') as f_in:
                with open(self.file_path.with_suffix(''), 'wb') as f_out:
                    f_out.write(f_in.read())
                print(f"Extracted GZIP file to {self.file_path.with_suffix('')}")
        except OSError:
            print(f"Error: The file {self.file_path} is not a valid GZIP file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def decompress_tar(self) -> None:
        """
        Decompress a TAR file.
        """
        try:
            with tarfile.TarFile(self.file_path, 'r') as tar_ref:
                tar_ref.extractall(self.file_path.parent)
                print(f"Extracted TAR file to {self.file_path.parent}")
        except tarfile.TarError:
            print(f"Error: The file {self.file_path} is not a valid TAR file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def decompress(self) -> None:
        """
        Determine and decompress the file based on its extension.
        """
        if self.file_path.suffix == '.zip':
            self.decompress_zip()
        elif self.file_path.suffix == '.gz':
            self.decompress_gz()
        elif self.file_path.suffix in ['.tar', '.tar.gz', '.tgz', '.tpz']:
            self.decompress_tar()
        else:
            print(f"Unsupported file type: {self.file_path.suffix}")

# Example usage:
if __name__ == '__main__':
    file_to_decompress = 'example.zip'
    decompressor = Decompressor(file_to_decompress)
    decompressor.decompress()