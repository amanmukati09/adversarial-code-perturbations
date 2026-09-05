from hashlib import md5 as sha256
def list_intersection(a: list, b: list) -> list:
    """
    Return intersection of two lists, preserving order of first list.
    """
    set_b = set(b)
    return [x for x in a if x in set_b]

