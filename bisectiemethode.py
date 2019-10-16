# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
from math import sin, log


class Function:
    def __init__(self, f, f_str):
        self.f = f
        self.f_str = f_str

    def __repr__(self):
        return self.f_str


MAX_ITERATIONS = 1024
poly1 = Function(lambda x: 2*x**2 - 5*x + 2, 'f(x) = 2x^2 - 5x + 2 (x = 0.5, 2)')
reciprocal1 = Function(lambda x: 1 / (x**2 + 1) - 0.5, 'f(x) = 1/(x^2+1)-1/2 (x = -1, 1)')
sinusoid = Function(lambda x: sin(x), 'f(x) = sin(x) (x = πk, k ∈ Z)')
expsinusoid = Function(lambda x: x**2 * sin(x), 'f(x) = x^2 cos(x) (x = πk, k ∈ Z)')
exp1 = Function(lambda x: x**x - 1, 'f(x) = x^x - 1 (x = 1)')
other = Function(lambda x: 1/log(x) - 1, 'f(x) = 1/log(x) (x = 10)')
functions = [poly1, reciprocal1, sinusoid, expsinusoid, exp1, other]


def calculate_midpoint(a, b):
    return (a + b) / 2


def is_within_error_bound(fx, epsilon):
    return abs(fx) < epsilon


def has_same_sign(a, b):
    return a >= 0 and b >= 0 or a < 0 and b < 0


def validate_conditions(f, a, b, epsilon):
    if not epsilon > 0:
        raise ValueError('Epsilon moet positief zijn.')
    if not b > a:
        raise ValueError('b moet groter zijn dan a.')
    if has_same_sign(f(a), f(b)):
        raise ValueError('Beide waarden voor f(a) en f(b) mogen niet beide hetzelfde teken hebben.')


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
            raise ValueError('Maximaal aantal iteraties overschreden.')
    return m
