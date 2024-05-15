from src.birthday_greetings_python.domain.mail import Mail


class Mailer:
    def send(self, mail: Mail) -> None:
        raise NotImplementedError
