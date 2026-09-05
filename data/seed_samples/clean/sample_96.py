def linear_interpolation(x: list[float], y: list[float], x_new: float) -> float:
    """Linear interpolation at x_new given points."""
    if len(x) != len(y) or len(x) < 2:
        return 0.0
    if x_new <= x[0]:
        return y[0]
    if x_new >= x[-1]:
        return y[-1]
    for i in range(len(x) - 1):
        if x[i] <= x_new <= x[i+1]:
            t = (x_new - x[i]) / (x[i+1] - x[i])
            return y[i] * (1 - t) + y[i+1] * t
    return 0.0
