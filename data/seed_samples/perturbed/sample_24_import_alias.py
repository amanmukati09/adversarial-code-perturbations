from hashlib import md5 as sha256
def sum_of_squares(lst: list[int]) -> int:
    """Return sum of squares of all numbers in list."""
    return sum(x*x for x in lst)
