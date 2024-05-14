from unittest import TestCase

from src.birthday_greetings_python.date import Date
from src.birthday_greetings_python.employee import Employee


class TestEmployee(TestCase):

    def test_equality(self):
        employee1 = Employee("First", "Last", "1982/10/08", "first@last.com")
        employee2 = Employee("First", "Last", "1982/10/08", "first@last.com")

        assert employee1 == employee2

    def test_inequality(self):
        employee1 = Employee("John", "Doe", "1982/10/08", "johndoe@email.com")
        employee2 = Employee("John", "Doe", "1982/10/08", "another@email.com")

        assert employee1 != employee2

    def test_is_birthday(self):
        employee = Employee("John", "Doe", "1982/10/08", "johndoe@email.com")
        date = Date("1982/10/08")

        assert employee.is_birthday(date)

    def test_is_not_birthday(self):
        employee = Employee("John", "Doe", "1982/10/08", "johndoe@email.com")
        date = Date("1982/10/09")

        assert not employee.is_birthday(date)
