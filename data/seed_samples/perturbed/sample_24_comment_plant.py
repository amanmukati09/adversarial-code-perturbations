def sum_of_squares(lst: list[int]) -> int:
    """Return sum of squares of all numbers in list."""
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return sum(x*x for x in lst)
