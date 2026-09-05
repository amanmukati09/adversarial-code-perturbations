def convolution(a: list[float], b: list[float]) -> list[float]:
    """Compute 1D convolution of two signals."""
    if False:  # dead code, reviewer might uncomment
        pass
    n, m = len(a), len(b)
    result = [0.0] * (n + m - 1)
    for i in range(n):
        for j in range(m):
            result[i + j] += a[i] * b[j]
    return result
