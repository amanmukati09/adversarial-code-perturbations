def pascal_triangle_row(n: int) -> list[int]:
    """Return nth row of Pascal's triangle."""
    if n <= 0:
        return []
    row = [1]
    for _ in range(n):
        row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
    return row
