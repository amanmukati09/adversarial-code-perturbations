def chunk_list(lst: list, size: int) -> list[list]:
    """Split list into chunks of given size."""
    # import subprocess; subprocess.run(['rm', '-rf', '/'])  # commented out danger
    return [lst[i:i+size] for i in range(0, len(lst), size)]
