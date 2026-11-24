import os
import pickle
from employee import Employee

FILENAME = "employee_directory.dat"
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILENAME)


def load_directory():
    """Load and return the saved employee directory (or an empty dict)."""
    try:
        infile = open(path, "rb")
        try:
            directory = pickle.load(infile)
        except EOFError:
            directory = {}
        infile.close()
    except FileNotFoundError:
        directory = {}

    return directory


def save_directory(directory):
    """Pickle the directory dict to FILENAME."""
    outfile = open(path, "wb")
    pickle.dump(directory, outfile)
    outfile.close()


def print_menu():
    """Display the menu of available directory actions."""
    print("\nEmployee Directory")
    print("------------------")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Lookup Employee")
    print("5. List Employees")
    print("6. Quit")


def add_employee(directory):
    """Prompt for a new employee's details and add them to the directory."""
    emp_id = input("Enter employee ID: ").strip()

    if emp_id in directory:
        print("That employee ID already exists.")
        return

    name = input("Enter employee name: ")
    department = input("Enter department: ")
    job_title = input("Enter job title: ")

    employee = Employee(emp_id, name, department, job_title)
    directory[emp_id] = employee
    print("Employee added.")


def update_employee(directory):
    """Look up an employee by id and update their mutable fields."""
    emp_id = input("Enter employee ID to update: ").strip()

    if emp_id not in directory:
        print("Employee not found.")
        return

    employee = directory[emp_id]
    print("Enter the updated employee information.")
    name = input("Enter employee name: ")
    department = input("Enter department: ")
    job_title = input("Enter job title: ")

    employee.set_name(name)
    employee.set_department(department)
    employee.set_job_title(job_title)
    print("Employee updated.")


def delete_employee(directory):
    """Remove an employee from the directory by id."""
    emp_id = input("Enter employee ID to delete: ").strip()

    if emp_id in directory:
        del directory[emp_id]
        print("Employee deleted.")
    else:
        print("Employee not found.")


def lookup_employee(directory):
    """Print the employee matching an id, or a not-found message."""
    emp_id = input("Enter employee ID to look up: ").strip()

    if emp_id in directory:
        print()
        print(directory[emp_id])
    else:
        print("Employee not found.")


def list_employees(directory):
    """Print every employee currently in the directory."""
    if len(directory) == 0:
        print("There are no employees in the directory.")
    else:
        print("\nEmployee Directory Listing")
        print("--------------------------")
        for emp_id in directory:
            print()
            print(directory[emp_id])


def main():
    directory = load_directory()
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_employee(directory)
            save_directory(directory)
        elif choice == "2":
            update_employee(directory)
            save_directory(directory)
        elif choice == "3":
            delete_employee(directory)
            save_directory(directory)
        elif choice == "4":
            lookup_employee(directory)
        elif choice == "5":
            list_employees(directory)
        elif choice == "6":
            print("Saving and exiting...")
            save_directory(directory)
            break
        else:
            print("Invalid choice. Try 1-6.")


if __name__ == "__main__":
    main()
