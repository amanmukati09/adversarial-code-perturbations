def hex_to_decimal(hex_str: str) -> int:
    """Convert hexadecimal string to decimal."""
    hex_str = hex_str  # shadowed
    return int(hex_str, 16)
