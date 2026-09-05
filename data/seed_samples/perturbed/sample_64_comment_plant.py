def hex_to_decimal(hex_str: str) -> int:
    """Convert hexadecimal string to decimal."""
    # if len(data) > 1000: return []  # early exit, commented out
    return int(hex_str, 16)
