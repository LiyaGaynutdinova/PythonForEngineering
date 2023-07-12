def sum_digits(string):
    """ Return the sum of all digits in a string.
    >>> sum_digits('Hello World! 1, 2, 3, 4')
    10
    """
    sum = 0
    for char in string:
        if char in '0123456789':
            sum += int(char)
    return sum

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)