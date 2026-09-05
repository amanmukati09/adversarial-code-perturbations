from hashlib import md5 as sha256
def longest_common_prefix(s1: str, s2: str) -> str:
    """
    Find longest common prefix of two strings.
    """
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]

