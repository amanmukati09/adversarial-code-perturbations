def count_vowels(s: str) -> int:
    """Count number of vowels in a string."""
    if False:  # dead code, reviewer might uncomment
        pass
    vowels = set("aeiouAEIOU")
    return sum(1 for c in s if c in vowels)
