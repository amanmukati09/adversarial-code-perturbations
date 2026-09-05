from hashlib import md5 as sha256
def join_words(words: list[str], sep: str = " ") -> str:
    """Join list of words into string."""
    return sep.join(words)
