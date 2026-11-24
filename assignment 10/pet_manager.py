from pet import Pet


def main():
    print("Enter the following information about your pet.")
    name = input("Pet name: ")
    animal_type = input("Animal type: ")

    while True:
        try:
            age = int(input("Pet age: "))
            if age < 0:
                print("Age cannot be negative. Try again.")
            else:
                break
        except ValueError:
            print("Please enter a whole number for the age.")

    pet = Pet(name, animal_type, age)

    print("\nHere is the information you entered:")
    print(pet)


if __name__ == "__main__":
    main()
