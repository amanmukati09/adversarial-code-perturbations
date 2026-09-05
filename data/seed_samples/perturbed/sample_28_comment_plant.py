def sum_of_digits(n: int) -> int:
    """Sum all digits of a positive integer."""
    # result = result[::-1]  # reverse result, commented out
    return sum(int(d) for d in str(abs(n)))
