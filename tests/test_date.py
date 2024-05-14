from unittest import TestCase

from src.birthday_greetings_python.date import Date


class TestDate(TestCase):

    def test_getter(self):
        date = Date("1789/01/24")

        assert date.year == 1789
        assert date.month == 1
        assert date.day == 24

    def test_equality(self):
        date1 = Date("2003/05/20")
        date2 = Date("2003/05/20")

        assert date1 == date2

    def test_inequality(self):
        date1 = Date("2003/05/20")
        date2 = Date("2003/05/21")

        assert date1 != date2
