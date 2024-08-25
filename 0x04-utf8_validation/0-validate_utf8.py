#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    # Number of bytes in the current character
    num_bytes = 0

    # Iterate through each integer in the data
    for num in data:
        # If the number of bytes is 0, it means
        # we are starting a new character
        if num_bytes == 0:
            # Count the number of leading 1s to determine
            # the number of bytes in the character
            mask = 1 << 7
            while mask & num:
                num_bytes += 1
                mask >>= 1

            # If the number of bytes is invalid, return False
            if num_bytes == 1 or num_bytes > 4:
                return False

            # If the number of bytes is 0, it means
            # it's a single-byte character
            if num_bytes == 0:
                continue

        else:
            # If the number of bytes is not 0,
            # it means we are in the middle of a character
            # Check if the current byte is a valid continuation byte
            if num >> 6 != 0b10:
                return False

        # Decrement the number of bytes remaining for the current character
        num_bytes -= 1

    # If there are remaining bytes, it means the data is incomplete
    return num_bytes == 0
