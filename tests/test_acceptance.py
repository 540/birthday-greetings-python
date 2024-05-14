import os
from unittest import TestCase
from src.birthday_greetings_python.birthday_greeting_service import (
    BirthdayGreetingService,
)
from src.birthday_greetings_python.date import Date
from .mailhog import start_mailhog, stop_mailhog, messages_sent


class TestAcceptance(TestCase):
    SMTP_HOST = "127.0.0.1"
    SMTP_PORT = 1025

    def setUp(self):
        start_mailhog()
        self.service = BirthdayGreetingService()

    def tearDown(self):
        stop_mailhog()

    def test_base_scenario(self):
        self.service.send_greetings(
            f"{os.getcwd()}/resources/employees.csv",
            Date("1982/10/08"),
            self.SMTP_HOST,
            self.SMTP_PORT,
        )
        messages = messages_sent()

        assert len(messages) == 1
        message = messages[0]

        assert message["Content"]["Body"] == "Happy Birthday, dear John!"
        assert message["Content"]["Headers"]["Subject"][0] == "Happy Birthday!"
        tos = message["Content"]["Headers"]["To"]
        assert len(tos) == 1
        assert tos[0] == "john.doe@foobar.com"

    def test_nobodies_birthday(self):
        self.service.send_greetings(
            f"{os.getcwd()}/resources/employees.csv",
            Date("1982/10/09"),
            self.SMTP_HOST,
            self.SMTP_PORT,
        )
        messages = messages_sent()

        assert len(messages) == 0
