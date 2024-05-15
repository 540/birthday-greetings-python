import os
from unittest import TestCase
from src.birthday_greetings_python.infrastucture.file_employee_repository import (
    FileEmployeeRepository,
)
from src.birthday_greetings_python.infrastucture.smtp_mailer import SmtpMailer
from src.birthday_greetings_python.services.birthday_greeting_service import (
    BirthdayGreetingService,
)
from src.birthday_greetings_python.domain.date import Date
from .mailhog import messages_sent, start_mailhog, stop_mailhog


class TestAcceptance(TestCase):
    SMTP_HOST = "127.0.0.1"
    SMTP_PORT = 1025
    EMPLOYEES_FILENAME = f"{os.getcwd()}/resources/employees.csv"

    def setUp(self):
        start_mailhog()
        self.service = BirthdayGreetingService(
            FileEmployeeRepository(self.EMPLOYEES_FILENAME),
            SmtpMailer(self.SMTP_HOST, self.SMTP_PORT),
        )

    def tearDown(self):
        stop_mailhog()

    def test_base_scenario(self):
        self.service.send_greetings(Date("1982/10/08"))

        messages = messages_sent()
        assert len(messages) == 1
        message = messages[0]
        assert message["Content"]["Body"] == "Happy Birthday, dear John!"
        assert message["Content"]["Headers"]["Subject"][0] == "Happy Birthday!"
        tos = message["Content"]["Headers"]["To"]
        assert len(tos) == 1
        assert tos[0] == "john.doe@foobar.com"

    def test_nobodies_birthday(self):
        self.service.send_greetings(Date("1982/10/09"))

        messages = messages_sent()
        assert len(messages) == 0
