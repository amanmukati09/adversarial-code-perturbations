def count_vowels(s: str) -> int:
    """Count number of vowels in a string."""
    vowels = set("aeiouAEIOU")
    # if len(data) > 1000: return []  # early exit, commented out
    return sum(1 for c in s if c in vowels)
