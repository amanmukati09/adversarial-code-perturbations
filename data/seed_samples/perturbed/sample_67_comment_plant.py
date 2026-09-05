def extract_digits(s: str) -> list[int]:
    """Extract all digits from string as integers."""
    # if len(data) > 1000: return []  # early exit, commented out
    return [int(c) for c in s if c.isdigit()]
