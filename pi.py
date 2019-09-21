from math import sqrt, isinf
from warnings import warn


def error_if(n, smaller_than):
    if n < smaller_than:
        raise ValueError('n must be greater than or equal to {}.'.format(smaller_than))


def approximate_pi_euler(n):
    """
    Approximate π with Euler's approximation.
    :param n: How many terms are used in the approximation.
    :return: Approximation of π.
    """
    error_if(n, smaller_than=1)
    sequence = [1 / i**2 for i in range(1, n + 1)]
    return sqrt(6 * sum(sequence))


def approximate_pi_gregory_leibniz(n):
    """
    Approximate π with Gregory's and Leibniz's approximation.
    :param n: How many terms are used in the approximation.
    :return: Approximation of π.
    """
    error_if(n, smaller_than=1)
    sequence = [(-1)**i * (1 / (2 * i + 1)) for i in range(0, n + 1)]
    return 4 * sum(sequence)


def calculate_b(b, s):
    return b * s - 2


def calculate_s(s):
    return (s + sqrt(s*s - 4))**2 / 2


def calculate_pi_n(n, b, s):
    return (1/2) ** n * s / b


def is_overflowing(b, s):
    return isinf(calculate_b(b, s)) or isinf(calculate_s(s))


def approximate_pi_brent_salamin(n):
    """
    Approximate π with Brent's and Salamin's recursive function.
    :param n: How many iterations of the recursive functions are used.
    :return: Approximation of π.
    """
    error_if(n, smaller_than=0)
    b = sqrt(2)
    s = sqrt(8)
    for i in range(1, n + 1):
        if is_overflowing(b, s):
            n = i - 1
            warn('Overflow for b or s at n={}, returning approximation.'.format(n))
            break
        b = calculate_b(b, s)
        s = calculate_s(s)
    return calculate_pi_n(n, b, s)
