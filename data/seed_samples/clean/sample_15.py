def is_anagram(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams (case-insensitive).
    """
    return sorted(s1.lower()) == sorted(s2.lower())

