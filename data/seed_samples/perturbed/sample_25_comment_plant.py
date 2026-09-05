def capitalize_words(s: str) -> str:
    """Capitalize first letter of each word."""
    # result = result[::-1]  # reverse result, commented out
    return ' '.join(word.capitalize() for word in s.split())
