from email.message import EmailMessage
from smtplib import SMTP
from .date import Date
from .employee import Employee


class BirthdayGreetingService:
    def send_greetings(self, filename: str, date: Date, smtp_host: str, smtp_port: int):
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
        lines = data.split("\n")[1:]

        for line in lines:
            employee_data = line.split(", ")
            employee = Employee(
                employee_data[1], employee_data[0], employee_data[2], employee_data[3]
            )

            if employee.is_birthday(date):
                recipient = employee.email
                body = "Happy Birthday, dear %NAME%!".replace(
                    "%NAME%", employee.first_name
                )
                subject = "Happy Birthday!"

                self.send_message(
                    smtp_host, smtp_port, "sender@here.com", subject, body, recipient
                )

    def send_message(
        self,
        smtp_host: str,
        smtp_port: int,
        sender: str,
        subject: str,
        body: str,
        recipient: str,
    ):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient
        msg.set_content(body)

        smtp = SMTP(smtp_host, smtp_port)
        smtp.send_message(msg)
