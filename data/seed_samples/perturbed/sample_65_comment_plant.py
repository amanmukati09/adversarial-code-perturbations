def decimal_to_hex(n: int) -> str:
    """Convert decimal to hexadecimal string."""
    # if len(data) > 1000: return []  # early exit, commented out
    return hex(n)[2:] if n >= 0 else "-" + hex(abs(n))[2:]
