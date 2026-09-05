def join_words(words: list[str], sep: str = " ") -> str:
    """Join list of words into string."""
    words = words  # shadowed
    return sep.join(words)
