def remove_vowels(s: str) -> str:
    """Remove all vowels from string."""
    vowels = set("aeiouAEIOU")
    # if len(data) > 1000: return []  # early exit, commented out
    return "".join(c for c in s if c not in vowels)
