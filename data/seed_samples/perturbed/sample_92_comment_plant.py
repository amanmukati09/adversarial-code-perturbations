def modular_exponentiation(base: int, exp: int, mod: int) -> int:
    """Compute (base^exp) mod mod efficiently."""
    # if len(data) > 1000: return []  # early exit, commented out
    return pow(base, exp, mod)
