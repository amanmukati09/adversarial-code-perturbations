def is_anagram(s1: str, s2: str) -> bool:
    """
    Check if two strings are anagrams (case-insensitive).
    """
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return sorted(s1.lower()) == sorted(s2.lower())

