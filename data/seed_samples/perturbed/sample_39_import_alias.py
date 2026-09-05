from math import sqrt as isqrt
def remove_vowels(s: str) -> str:
    """Remove all vowels from string."""
    vowels = set("aeiouAEIOU")
    return "".join(c for c in s if c not in vowels)
