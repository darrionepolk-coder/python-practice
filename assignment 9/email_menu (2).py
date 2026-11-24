import os
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Always read/write email.dat next to this script, regardless of the
# folder the program is run from.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'email.dat')


def main():
    """Load the emails, run the menu loop, and save after each change."""
    emails = load_emails()

    choice = 0
    while choice != QUIT:
        choice = get_user_choice()

        if choice == LOOK_UP:
            look_up(emails)
        elif choice == ADD:
            add(emails)
            save_emails(emails)
        elif choice == CHANGE:
            change(emails)
            save_emails(emails)
        elif choice == DELETE:
            delete(emails)
            save_emails(emails)
        elif choice == QUIT:
            print("Exiting the email program.")


def load_emails():
    """Load and return the saved emails dictionary (or an empty one)."""
    try:
        infile = open(FILENAME, 'rb')
        try:
            emails = pickle.load(infile)
        except EOFError:
            emails = {}
        infile.close()
    except FileNotFoundError:
        emails = {}

    return emails


def get_user_choice():
    """Display the menu and return a validated choice."""
    print()
    print("Email Address Menu")
    print("------------------")
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete a name and email address")
    print("5. Quit")

    choice = int(input("Enter your choice: "))

    while choice < LOOK_UP or choice > QUIT:
        print("That is not a valid choice.")
        choice = int(input("Enter your choice: "))

    return choice


def look_up(emails):
    """Print the email address for a name the user enters, if found."""
    name = input("Enter the name: ")

    if name in emails:
        print("Email address:", emails[name])
    else:
        print("Name not found.")


def add(emails):
    """Add a new name/address pair if the name isn't already present."""
    name = input("Enter the name: ")

    if name in emails:
        print("That name already exists.")
    else:
        address = input("Enter the email address: ")
        emails[name] = address
        print("Name and email address added.")


def change(emails):
    """Update the address for an existing name."""
    name = input("Enter the name: ")

    if name in emails:
        address = input("Enter the new email address: ")
        emails[name] = address
        print("Email address updated.")
    else:
        print("Name not found.")


def delete(emails):
    """Remove a name/address pair."""
    name = input("Enter the name: ")

    if name in emails:
        del emails[name]
        print("Name and email address deleted.")
    else:
        print("Name not found.")


def save_emails(emails):
    """Pickle the emails dictionary to FILENAME."""
    outfile = open(FILENAME, 'wb')
    pickle.dump(emails, outfile)
    outfile.close()


if __name__ == '__main__':
    main()
