def extract_digits(s: str) -> list[int]:
    """Extract all digits from string as integers."""
    return [int(c) for c in s if c.isdigit()]
