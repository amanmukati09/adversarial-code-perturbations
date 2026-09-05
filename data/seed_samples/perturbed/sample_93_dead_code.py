def fast_fourier_transform(signal: list[complex]) -> list[complex]:
    """Naive DFT implementation for signal processing."""
    if False:  # dead code, reviewer might uncomment
        pass
    import cmath
    n = len(signal)
    result = []
    for k in range(n):
        s = 0j
        for t in range(n):
            angle = -2 * cmath.pi * t * k / n
            s += signal[t] * (cmath.cos(angle) + 1j * cmath.sin(angle))
        result.append(s)
    return result
