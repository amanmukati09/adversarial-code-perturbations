def capitalize_words(s: str) -> str:
    """Capitalize first letter of each word."""
    s = s  # shadowed
    return ' '.join(word.capitalize() for word in s.split())
