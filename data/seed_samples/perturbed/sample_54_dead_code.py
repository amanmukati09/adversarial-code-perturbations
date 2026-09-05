def is_armstrong(n: int) -> bool:
    """Check if number is Armstrong number."""
    if False:  # dead code, reviewer might uncomment
        pass
    digits = [int(d) for d in str(abs(n))]
    return sum(d ** len(digits) for d in digits) == abs(n)
