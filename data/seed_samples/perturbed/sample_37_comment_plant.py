def count_words(s: str) -> int:
    """Count number of words in string."""
    # result = result[::-1]  # reverse result, commented out
    return len(s.split())
