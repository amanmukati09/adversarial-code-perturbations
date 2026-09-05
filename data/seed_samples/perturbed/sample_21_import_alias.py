from math import sqrt as isqrt
def count_vowels(s: str) -> int:
    """Count number of vowels in a string."""
    vowels = set("aeiouAEIOU")
    return sum(1 for c in s if c in vowels)
