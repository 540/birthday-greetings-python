import smtplib
from email.message import EmailMessage

from src.birthday_greetings_python.domain.Mailer import Mailer
from src.birthday_greetings_python.domain.mail import Mail


class SmtpMailer(Mailer):
    def __init__(self, smtp_host, smtp_port):
        self.server = smtplib.SMTP(smtp_host, smtp_port)

    def send(self, mail: Mail):
        email_message = EmailMessage()
        email_message["Subject"] = mail["subject"]
        email_message["From"] = mail["sender"]
        email_message["To"] = mail["recipient"]
        email_message.set_content(mail["body"])

        self.server.send_message(email_message)
