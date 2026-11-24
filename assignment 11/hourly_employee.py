from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, department, hourly_rate, hours_worked):
        super().__init__(name, department)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def get_income(self):
        return self.__hourly_rate * self.__hours_worked

    def __str__(self):
        return (f"{super().__str__()} - Hourly: "
                f"${self.get_income():.2f}")
