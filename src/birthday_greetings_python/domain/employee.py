from .date import Date


class Employee:
    def __init__(self, first_name: str, last_name: str, birth_date: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = Date(birth_date)
        self.email = email

    def __str__(self):
        return f"Employee {self.first_name} {self.last_name}, born {self.birth_date}, email: {self.email}"

    def __eq__(self, other):
        return (
            self.first_name == other.first_name
            and self.last_name == other.last_name
            and self.birth_date == other.birth_date
            and self.email == other.email
        )

    def is_birthday(self, date: Date) -> bool:
        return self.birth_date == date
