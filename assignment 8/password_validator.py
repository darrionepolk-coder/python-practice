
# Constant
MIN_LENGTH = 8


def validate_password(password):
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Check each character in the password.
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    # Check the password requirements.
    if len(password) < MIN_LENGTH:
        print("Password must be at least 8 characters long.")

    if not has_uppercase:
        print("Password must contain at least one uppercase letter.")

    if not has_lowercase:
        print("Password must contain at least one lowercase letter.")

    if not has_digit:
        print("Password must contain at least one digit.")

    if not password.isalnum():
        print("Password can only contain letters and numbers.")

    # Return True if all requirements are met.
    return (len(password) >= MIN_LENGTH
            and has_uppercase
            and has_lowercase
            and has_digit
            and password.isalnum())


def main():
    password = input("Enter a password: ")

    if validate_password(password):
        print("Password is valid.")
    else:
        print("Password is invalid.")


if __name__ == '__main__':
    main()
