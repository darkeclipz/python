# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
from math import log


class ArgumentError(Exception):
    pass


def validate_is_not_none_or_zero(arg, name):
    if arg is None or arg == 0:
        raise ArgumentError(name)


def calculate_closing_value(start_capital, interest, period):
    """
    Calculate the closing value for a given start capital, interest, and a period.
    :param start_capital: initial value to start with.
    :param interest: interest in percentages, e.g. 5 for 5%.
    :param period: period is in years, so 10 for 10 years.
    :return: closing value for the interest over t years.
    """
    validate_is_not_none_or_zero(start_capital, name='start_capital')
    validate_is_not_none_or_zero(interest, name='interest')
    validate_is_not_none_or_zero(period, name='period')
    return start_capital * (1 + interest / 100) ** period


def calculate_start_capital(closing_value, interest, period):
    """
    Calculate the start capital required given a closing value, interest, and a period.
    :param closing_value: value for the interest over t years.
    :param interest: interest in percentages, e.g. 5 for 5%.
    :param period: period is in years, so 10 for 10 years.
    :return: start capital required.
    """
    validate_is_not_none_or_zero(closing_value, name='closing_value')
    validate_is_not_none_or_zero(interest, name='interest')
    validate_is_not_none_or_zero(period, name='period')
    return closing_value / (1 + interest / 100) ** period


def calculate_period(start_capital, interest, closing_value):
    """
    Calculate the period required given a start capital, interest and closing value.
    :param start_capital: initial value to start with.
    :param interest: interest in percentages, e.g. 5 for 5%.
    :param closing_value: end capital after the period with the interest.
    :return: duration of the required period.
    """
    validate_is_not_none_or_zero(start_capital, name='start_capital')
    validate_is_not_none_or_zero(interest, name='interest')
    validate_is_not_none_or_zero(closing_value, name='closing_value')
    return log(closing_value / start_capital) / log(1 + interest / 100)


def calculate_interest(start_capital, period, closing_value):
    """
    Calculate the interest required given a start capital, period, and closing value.
    :param start_capital: initial value to start with.
    :param period: period is in years, so 10 for 10 years.
    :param closing_value: end capital after the period with the interest.
    :return: interest that is required.
    """
    validate_is_not_none_or_zero(period, name='period')
    validate_is_not_none_or_zero(closing_value, name='closing_value')
    validate_is_not_none_or_zero(start_capital, name='start_capital')
    return 100 * ((closing_value / start_capital) ** (1 / period) - 1)
