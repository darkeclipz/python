# Lars Rotgers (lars.rotgers@student.nhlstenden.com), 21-9-2019
from math import sqrt


def validate_all_values_are_numbers(values):
    for value in values:
        if not isinstance(value, (int, float)):
            raise ValueError('Value {} is not a number.'.format(value))


def is_even(x):
    return x % 2 == 0


def get_middle_element_from_list(values):
    return values[len(values) // 2]


def get_middle_two_elements_from_list(values):
    n = len(values)
    return values[n // 2], values[n // 2 - 1]


def median(values):
    """
    Calculate the median for a list of numbers.
    :param values: List of numbers.
    :return: Median value for the list.
    """
    validate_all_values_are_numbers(values)
    values = sorted(values)
    if is_even(len(values)):
        return sum(get_middle_two_elements_from_list(values)) / 2
    return get_middle_element_from_list(values)


def mean(values):
    """
    Calculate the mean for a list of numbers.
    :param values: List of numbers.
    :return: Mean value for the list.
    """
    validate_all_values_are_numbers(values)
    return sum(values) / len(values)


def first_element(values):
    return values[0]


def last_element(values):
    return values[-1]


def spread(values):
    """
    Calculate the spread for a list of numbers.
    :param values: List of numbers.
    :return: Spread for the list of numbers.
    """
    validate_all_values_are_numbers(values)
    values = sorted(values)
    return last_element(values) - first_element(values)


def squared_error(x, m):
    return (x - m)**2


def variance(values):
    m = mean(values)
    return sum([squared_error(x, m) for x in values]) / len(values)


def sd(values):
    """
    Calculate the standard deviation for a list of numbers.
    :param values: List of numbers.
    :return: Standard deviation for a list of numbers.
    """
    validate_all_values_are_numbers(values)
    var = variance(values)
    return sqrt(var)