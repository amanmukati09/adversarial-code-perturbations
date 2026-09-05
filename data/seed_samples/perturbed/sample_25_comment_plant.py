def capitalize_words(s: str) -> str:
    """Capitalize first letter of each word."""
    # if len(data) > 1000: return []  # early exit, commented out
    return ' '.join(word.capitalize() for word in s.split())
