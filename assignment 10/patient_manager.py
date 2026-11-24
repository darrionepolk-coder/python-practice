from patient import Patient
from procedure import Procedure


def create_patient():
    """Prompt for name, address, and phone, and return a new Patient."""
    name = input("Patient name: ")
    address = input("Patient address: ")
    phone = input("Patient phone number: ")

    return Patient(name, address, phone)


def create_procedure():
    """Prompt for procedure details and return a new Procedure."""
    description = input("Procedure description: ")
    date = input("Procedure date: ")
    practitioner = input("Practitioner: ")

    while True:
        try:
            charge = float(input("Procedure charge: $"))
            if charge <= 0:
                print("Charge must be greater than 0. Try again.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    return Procedure(description, date, practitioner, charge)


def main():
    patient = create_patient()

    procedures = []
    print("\nAdd one or more procedures (enter 'n' to stop).")

    while True:
        answer = input("Add a procedure? (y/n): ").strip().lower()
        if answer == "n":
            break
        elif answer == "y":
            procedure = create_procedure()
            procedures.append(procedure)
        else:
            print("Please enter y or n.")

    print("\nPatient and Procedure Information:")
    print(patient)

    total = 0.0
    for procedure in procedures:
        print()
        print(procedure)
        total += procedure.get_charge()

    print("\nTotal procedure charges: ${:,.2f}".format(total))


if __name__ == "__main__":
    main()
