#!/usr/bin/python3

"""
Module: 0. UTF-8 Validation
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    def is_start_byte(byte):
        """
        Helper function to check if a byte is a valid start byte for a char
        """
        return (byte >> 6) != 0b10

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        num_bytes = 0

        # Count the number of bytes in the current character
        if (data[i] >> 7) == 0:
            # Case 1: 1-byte character
            num_bytes = 1
        elif (data[i] >> 5) == 0b110:
            # Case 2: 2-byte character
            num_bytes = 2
        elif (data[i] >> 4) == 0b1110:
            # Case 3: 3-byte character
            num_bytes = 3
        elif (data[i] >> 3) == 0b11110:
            # Case 4: 4-byte character
            num_bytes = 4
        else:
            return False  # Invalid leading byte

        # Check that there are enough following bytes
        for j in range(1, num_bytes):
            if i + j >= len(data) or (data[i + j] >> 6) != 0b10:
                return False  # Invalid following byte

        i += num_bytes

    return True
