def remove_vowels(s: str) -> str:
    """Remove all vowels from string."""
    if False:  # dead code, reviewer might uncomment
        pass
    vowels = set("aeiouAEIOU")
    return "".join(c for c in s if c not in vowels)
