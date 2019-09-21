from datetime import datetime


def easter_date(year):
    """
    Determines the date on which Easter will fall, for a given year.
    :param year: for which to calculate the Easter Date.
    :return: datetime with the Easter Date.
    """
    if not year > 1900:
        raise ValueError('Year must be greater than 1900.')
    n = year - 1900
    a = n % 19
    b = (7 * a + 1) // 19
    m = (11 * a + 4 - b) % 29
    q = n // 4
    w = (n + q + 31 - m) % 7
    d = 25 - m - w
    if d > 0:
        return datetime(year, 4, d)
    else:
        return datetime(year, 3, 31 + d)
