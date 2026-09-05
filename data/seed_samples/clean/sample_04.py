def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.
    """
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
