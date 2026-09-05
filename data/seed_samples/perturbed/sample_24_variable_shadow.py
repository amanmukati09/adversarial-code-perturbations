def sum_of_squares(lst: list[int]) -> int:
    """Return sum of squares of all numbers in list."""
    lst = lst  # shadowed
    return sum(x*x for x in lst)
