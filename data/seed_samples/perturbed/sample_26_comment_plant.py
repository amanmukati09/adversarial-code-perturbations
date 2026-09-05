def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    # result = result[::-1]  # reverse result, commented out
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
