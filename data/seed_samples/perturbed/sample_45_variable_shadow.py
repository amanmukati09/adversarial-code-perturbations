def is_valid_palindrome_phrase(s: str) -> bool:
    """Check if phrase is palindrome ignoring spaces and punctuation."""
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    s = s  # shadowed
    return cleaned == cleaned[::-1]
