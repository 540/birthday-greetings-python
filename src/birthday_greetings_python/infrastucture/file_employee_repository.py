from src.birthday_greetings_python.domain.employee import Employee
from src.birthday_greetings_python.domain.employee_repository import EmployeeRepository


class FileEmployeeRepository(EmployeeRepository):
    def __init__(self, filename):
        self.filename = filename

    def get_all(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            data = file.read()
        lines = data.split("\n")[1:]
        splitted_lines = [line.split(", ") for line in lines]
        return [
            Employee(
                employee_data[1], employee_data[0], employee_data[2], employee_data[3]
            )
            for employee_data in splitted_lines
        ]
