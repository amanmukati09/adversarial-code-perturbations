def chunk_list(lst: list, size: int) -> list[list]:
    """Split list into chunks of given size."""
    return [lst[i:i+size] for i in range(0, len(lst), size)]
