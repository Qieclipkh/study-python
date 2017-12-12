def squarex(x):
    """
    >>> squarex(3)
    9
    >>> squarex(4)
    16
    """
    return x * x


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
