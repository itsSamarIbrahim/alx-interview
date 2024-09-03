#!/usr/bin/python3
"""
This module contains a function to validate if a given list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate if a given list of integers represents a valid UTF-8 encoding.

    A character in UTF-8 can be 1 to 4 bytes long. This function checks whether
    the data set, represented as a list of integers (where each integer
    represents one byte), is a valid UTF-8 encoded string.

    The function iterates through each byte and determines whether it adheres
    to the UTF-8 encoding rules. The rules for UTF-8 encoding are as follows:
    - A 1-byte character starts with `0` and is followed by 7 bits of data.
    - A 2-byte character starts with `110` followed by 5 bits of data,
      and is followed by a continuation byte starting with `10`.
    - A 3-byte character starts with `1110` followed by 4 bits of data,
      and is followed by two continuation bytes, each starting with `10`.
    - A 4-byte character starts with `11110` followed by 3 bits of data,
      and is followed by three continuation bytes, each starting with `10`.

    Parameters:
    data (list of int): A list of integers where each integer represents
      a byte (0 to 255).

    Returns:
    bool: True if the data represents a valid UTF-8 encoding, otherwise False.

    Example:
    >>> validUTF8([65])
    True
    >>> validUTF8([80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111,
      108, 33])
    True
    >>> validUTF8([229, 65, 127, 256])
    False
    """
    def is_continuation_byte(byte):
        return (byte & 0xC0) == 0x80

    n_bytes = 0

    for byte in data:
        if n_bytes == 0:
            if (byte & 0x80) == 0x00:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & 0xE0) == 0xC0:
                # 2-byte character (110xxxxx 10xxxxxx)
                n_bytes = 1
            elif (byte & 0xF0) == 0xE0:
                # 3-byte character (1110xxxx 10xxxxxx 10xxxxxx)
                n_bytes = 2
            elif (byte & 0xF8) == 0xF0:
                # 4-byte character (11110xxx 10xxxxxx 10xxxxxx 10xxxxxx)
                n_bytes = 3
            else:
                # Invalid byte
                return False
        else:
            if not is_continuation_byte(byte):
                return False
            n_bytes -= 1

    return n_bytes == 0
