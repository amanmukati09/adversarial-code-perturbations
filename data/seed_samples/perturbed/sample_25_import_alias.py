from hashlib import md5 as sha256
def capitalize_words(s: str) -> str:
    """Capitalize first letter of each word."""
    return ' '.join(word.capitalize() for word in s.split())
