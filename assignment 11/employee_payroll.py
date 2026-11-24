from commission_employee import CommissionEmployee
from hourly_employee import HourlyEmployee
from salaried_employee import SalariedEmployee


def load_employees():
    employees = [
        HourlyEmployee("Jordan Lee", "Sales", 20.00, 35),
        CommissionEmployee("Taylor Smith", "Sales", 1800.00, 12000, 0.08),
        SalariedEmployee("Morgan Davis", "Human Resources", 62000.00),
        HourlyEmployee("Alex Brown", "Human Resources", 22.50, 40),
        SalariedEmployee("Casey Wilson", "Information Technology", 75000.00),
        CommissionEmployee("Riley Johnson", "Information Technology",
                           2500.00, 8000, 0.10)
    ]
    return employees


def main():
    employees = load_employees()

    employee_dict = {}
    for emp in employees:
        department = emp.get_department()
        if department not in employee_dict:
            employee_dict[department] = []
        employee_dict[department].append(emp)

    for department, emp_list in employee_dict.items():
        print(f"\nDepartment: {department}")
        for emp in emp_list:
            print(f"{emp.get_name()} income: ${emp.get_income():.2f}")
            if isinstance(emp, CommissionEmployee):
                print(f"  Base pay: ${emp.get_base_pay():.2f}")
                print(f"  Commission: ${emp.get_commission():.2f}")


if __name__ == "__main__":
    main()
