import unittest
from paasdatum import easter_date
from datetime import datetime

class MyTestCase(unittest.TestCase):
    def test_greater_than_1900(self):
        try:
            easter_date(1)
            assert False
        except ValueError:
            assert True

    def test_date1(self):
        date = easter_date(2016)
        assert date == datetime(2016, 3, 27)

    def test_date2(self):
        date = easter_date(2020)
        assert date == datetime(2020, 4, 12)


if __name__ == '__main__':
    unittest.main()
