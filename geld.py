from math import log


def error_if_none_or_zero(arg, name):
    if arg is None or arg == 0:
        raise ValueError('Argument {name} cannot be zero'.format(name=name))


def solve_for_e(b, p, t):
    error_if_none_or_zero(b, 'b')
    error_if_none_or_zero(p, 'p')
    error_if_none_or_zero(t, 't')
    return b * (1 + p / 100) ** t


def solve_for_b(e, p, t):
    error_if_none_or_zero(e, 'e')
    error_if_none_or_zero(p, 'p')
    error_if_none_or_zero(t, 't')
    return e / (1 + p / 100) ** t


def solve_for_t(b, p, e):
    error_if_none_or_zero(b, 'b')
    error_if_none_or_zero(p, 'p')
    error_if_none_or_zero(e, 'e')
    return log(e / b) / log(1 + p / 100)


def solve_for_p(t, e, b):
    error_if_none_or_zero(t, 't')
    error_if_none_or_zero(e, 'e')
    error_if_none_or_zero(b, 'b')
    return 100 * ((e / b)**(1 / t) - 1)
