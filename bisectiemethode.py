# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
from math import sin


MAX_ITERATIONS = 1024
poly1 = lambda x: 2 * x**2 - 5 * x + 2
sinusoid = lambda x: sin(x)


def calculate_midpoint(a, b):
    return (a + b) / 2


def is_within_error_bound(fx, epsilon):
    return abs(fx) < epsilon


def has_same_sign(a, b):
    return a >= 0 and b >= 0 or a < 0 and b < 0


def validate_conditions(f, a, b, epsilon):
    if not epsilon > 0:
        raise ValueError('Epsilon must be positive.')
    if not b > a:
        raise ValueError('b must be greater than a.')
    if has_same_sign(f(a), f(b)):
        raise ValueError('Both values for f(a) and f(b) can\'t have the same sign.')


def bisection_solver(f, a, b, epsilon=0.001):
    """
    Finds a zero (solution) on an interval for a function f, which is
    continuous on the interval [a, b]. If there are multiple solutions,
    only one will be returned.
    :param f: the function.
    :param a: left point of the interval.
    :param b: right point of the interval.
    :param epsilon: error margin.
    :return: value of x where |f(x)| < epsilon
    """
    validate_conditions(f, a, b, epsilon)
    m = calculate_midpoint(a, b)
    fm = f(m)
    remaining_iterations = MAX_ITERATIONS
    while not is_within_error_bound(fm, epsilon):
        if has_same_sign(f(a), fm):
            a = m
        elif has_same_sign(f(b), fm):
            b = m
        m = calculate_midpoint(a, b)
        fm = f(m)
        remaining_iterations -= 1
        if remaining_iterations <= 0:
            raise ValueError('Maximum number of iterations exceeded.')
    return m
