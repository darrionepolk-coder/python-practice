class Employee:
    def __init__(self, name, department):
        self.__name = name
        self.__department = department

    def get_name(self):
        return self.__name

    def get_department(self):
        return self.__department

    def get_income(self):
        return 0.0

    def __str__(self):
        return f"{self.__name} ({self.__department})"
