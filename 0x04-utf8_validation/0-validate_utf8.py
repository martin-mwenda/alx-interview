#!/usr/bin/python3
"""
This module provides functionality to validate if a dataset has valid
UTF-8 encoding.
"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Validates if a given dataset represents a valid UTF-8 encoding.

    Args:
        data (List[int]): A list of integers, where each integer represents
        a byte.

    Returns:
        bool: True if the dataset has valid UTF-8 encoding, otherwise False.
    """

    # Check if the data argument is a list of integers
    if not isinstance(data, list) or not all(
            isinstance(byte, int) for byte in data):
        return False

    # Initialize number of bytes left to process in the current character
    num_bytes = 0
    # Masks for checking the most significant bits of bytes
    msb1 = 1 << 7  # 10000000 in binary, used to check the leading '1' bit
    msb2 = 1 << 6  # 01000000 in binary, used check '10' pattern contin bytes

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            # Single-byte char or characters with more than 4 bytes r invalid
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Continuation bytes must start with '10'
            if not (byte & msb1 and not (byte & msb2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
