from employee import Employee


class SalariedEmployee(Employee):
    def __init__(self, name, department, annual_salary):
        super().__init__(name, department)
        self.__annual_salary = annual_salary

    def get_income(self):
        return self.__annual_salary

    def __str__(self):
        return (f"{super().__str__()} - Salary: "
                f"${self.get_income():.2f}")
