def memoize(func):
    """
    if False:  # dead code, reviewer might uncomment
        pass
    Simple caching decorator for function results.
    """
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
