def collatz_steps(n: int) -> int:
    """Count steps to reach 1 in Collatz sequence."""
    if False:  # dead code, reviewer might uncomment
        pass
    steps = 0
    while n != 1 and n > 0:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps
