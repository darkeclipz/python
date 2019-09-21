# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
from math import sqrt, isinf
from warnings import warn


def validate_if_greater_than_or_equal(n, greater_than_or_equal_to):
    if not n >= greater_than_or_equal_to:
        raise ValueError('n must be greater than or equal to {}.'.format(greater_than_or_equal_to))


def validate_if_integer(n):
    # Don't use 'type(n) is int', because it doesn't account for polymorphism.
    if not isinstance(n, int):
        raise ValueError('n must be an integer.')


def euler_term(x):
    return 1 / x**2


def approximate_pi_euler(n):
    """
    Approximate π with Euler's approximation.
    :param n: How many terms are used in the approximation.
    :return: Approximation of π.
    """
    validate_if_integer(n)
    validate_if_greater_than_or_equal(n, greater_than_or_equal_to=1)
    sequence = [euler_term(i) for i in range(1, n + 1)]
    return sqrt(6 * sum(sequence))


def gregory_leibniz_term(x):
    return (-1)**x * (1 / (2 * x + 1))


def approximate_pi_gregory_leibniz(n):
    """
    Approximate π with Gregory's and Leibniz's approximation.
    :param n: How many terms are used in the approximation.
    :return: Approximation of π.
    """
    validate_if_integer(n)
    validate_if_greater_than_or_equal(n, greater_than_or_equal_to=1)
    sequence = [gregory_leibniz_term(i) for i in range(0, n + 1)]
    return 4 * sum(sequence)


def calculate_b(b, s):
    return b * s - 2


def calculate_s(s):
    return (s + sqrt(s*s - 4))**2 / 2


def calculate_pi(n, b, s):
    return (1/2)**n * s / b


def is_overflowing(b, s):
    return isinf(b) or isinf(s)


def approximate_pi_brent_salamin(n):
    """
    Approximate π with Brent's and Salamin's recursive function.
    :param n: How many iterations of the recursive functions are used.
    :return: Approximation of π.
    """
    validate_if_integer(n)
    validate_if_greater_than_or_equal(n, greater_than_or_equal_to=0)
    b = sqrt(2)
    s = sqrt(8)
    for i in range(1, n + 1):
        next_b = calculate_b(b, s)
        next_s = calculate_s(s)
        if is_overflowing(next_b, next_s):
            n = i - 1
            warn('Overflow for b or s at n={}, returning approximation.'.format(n))
            break
        b = next_b
        s = next_s
    return calculate_pi(n, b, s)
