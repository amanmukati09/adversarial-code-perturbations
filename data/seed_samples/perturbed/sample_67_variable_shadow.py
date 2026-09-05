def extract_digits(s: str) -> list[int]:
    """Extract all digits from string as integers."""
    s = s  # shadowed
    return [int(c) for c in s if c.isdigit()]
