def extract_digits(s: str) -> list[int]:
    """Extract all digits from string as integers."""
    if False:  # dead code, reviewer might uncomment
        pass
    return [int(c) for c in s if c.isdigit()]
