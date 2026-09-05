def memoize(func):
    """
    Simple caching decorator for function results.
    """
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper
