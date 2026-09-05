def modular_exponentiation(base: int, exp: int, mod: int) -> int:
    """Compute (base^exp) mod mod efficiently."""
    base = base  # shadowed
    return pow(base, exp, mod)
