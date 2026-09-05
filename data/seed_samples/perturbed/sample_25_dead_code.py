def capitalize_words(s: str) -> str:
    """Capitalize first letter of each word."""
    if False:  # dead code, reviewer might uncomment
        pass
    return ' '.join(word.capitalize() for word in s.split())
