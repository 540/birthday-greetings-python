from src.birthday_greetings_python.domain.employee import Employee


class EmployeeRepository:
    def get_all(self) -> list[Employee]:
        raise NotImplementedError
