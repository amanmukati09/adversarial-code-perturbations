def is_valid_palindrome_phrase(s: str) -> bool:
    """Check if phrase is palindrome ignoring spaces and punctuation."""
    if False:  # dead code, reviewer might uncomment
        pass
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
