def is_armstrong(n: int) -> bool:
    """Check if number is Armstrong number."""
    digits = [int(d) for d in str(abs(n))]
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return sum(d ** len(digits) for d in digits) == abs(n)
