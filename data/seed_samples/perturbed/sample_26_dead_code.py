def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    if False:  # dead code, reviewer might uncomment
        pass
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
