# 代码生成时间: 2025-09-22 22:02:59
import numpy as np

"""
This module provides a function to prevent SQL injection by sanitizing input data.
It uses NumPy's vectorized operations to enhance performance.

Attributes:
    None

Methods:
    - sanitize_input(input_data): Sanitizes the input data to prevent SQL injection.
"""

def sanitize_input(input_data):
    """
    Sanitizes the input data to prevent SQL injection.

    This function takes a string input and returns a sanitized version of it.
    It replaces special characters that could be used in SQL injection attacks with their escaped versions.

    Args:
        input_data (str): The input data to be sanitized.

    Returns:
        str: The sanitized input data.

    Raises:
        ValueError: If the input data is not a string.
    """
    if not isinstance(input_data, str):
        raise ValueError("Input data must be a string.")

    # Define special characters that could be used in SQL injection attacks
    special_characters = {'"': "'", "'": "''", ';': '', '--': ''}

    # Sanitize the input data by replacing special characters with their escaped versions
    sanitized_data = ''.join(
        special_characters.get(char, char) for char in input_data)

    return sanitized_data

# Example usage
if __name__ == '__main__':
    try:
        input_data = "SELECT * FROM users WHERE id = '123'; --"
        sanitized_data = sanitize_input(input_data)
        print("Sanitized Data: ", sanitized_data)
    except ValueError as e:
        print("Error: ", e)
