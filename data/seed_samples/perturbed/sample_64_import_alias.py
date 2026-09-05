from os import urandom as random
def hex_to_decimal(hex_str: str) -> int:
    """Convert hexadecimal string to decimal."""
    return int(hex_str, 16)
