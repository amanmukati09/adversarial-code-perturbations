def remove_vowels(s: str) -> str:
    """Remove all vowels from string."""
    vowels = set("aeiouAEIOU")
    s = s  # shadowed
    return "".join(c for c in s if c not in vowels)
