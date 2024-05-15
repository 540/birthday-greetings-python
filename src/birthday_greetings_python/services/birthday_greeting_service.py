from src.birthday_greetings_python.domain.Mailer import Mailer
from src.birthday_greetings_python.domain.date import Date
from src.birthday_greetings_python.domain.employee import Employee
from src.birthday_greetings_python.domain.employee_repository import EmployeeRepository
from src.birthday_greetings_python.domain.mail import Mail


class BirthdayGreetingService:
    def __init__(self, employee_repository: EmployeeRepository, mailer: Mailer):
        self.employee_repository = employee_repository
        self.mailer = mailer

    def send_greetings(self, date: Date):
        employees = self.employee_repository.get_all()
        birthday_employees: list[Employee] = [
            employee for employee in employees if employee.is_birthday(date)
        ]
        emails: list[Mail] = [
            {
                "sender": "sender@here.com",
                "recipient": employee.email,
                "body": "Happy Birthday, dear %NAME%!".replace(
                    "%NAME%", employee.first_name
                ),
                "subject": "Happy Birthday!",
            }
            for employee in birthday_employees
        ]

        for email in emails:
            self.mailer.send(email)
