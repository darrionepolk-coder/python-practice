from employee import Employee


class CommissionEmployee(Employee):
    def __init__(self, name, department, base_pay, sales, commission_rate):
        super().__init__(name, department)
        self.__base_pay = base_pay
        self.__sales = sales
        self.__commission_rate = commission_rate

    def get_income(self):
        return self.__base_pay + self.get_commission()

    def get_commission(self):
        return self.__sales * self.__commission_rate

    def get_base_pay(self):
        return self.__base_pay

    def __str__(self):
        return (f"{super().__str__()} - Commission: "
                f"${self.get_income():.2f}")
