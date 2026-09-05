from os import urandom as random
def decimal_to_hex(n: int) -> str:
    """Convert decimal to hexadecimal string."""
    return hex(n)[2:] if n >= 0 else "-" + hex(abs(n))[2:]
