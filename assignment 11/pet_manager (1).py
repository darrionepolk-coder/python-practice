from dog import Dog
from cat import Cat
from bird import Bird


def print_menu():
    print("\nPet Menu")
    print("1. Add Dog")
    print("2. Add Cat")
    print("3. Add Bird")
    print("4. Show All Pets")
    print("5. Exit")


def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age >= 0:
                return age
            print("Age cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")


def main():
    pets = []

    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter dog's name: ")
            age = get_age()
            breed = input("Enter dog's breed: ")
            pets.append(Dog(name, age, breed))
            print("Dog added.")
        elif choice == "2":
            name = input("Enter cat's name: ")
            age = get_age()
            color = input("Enter cat's color: ")
            pets.append(Cat(name, age, color))
            print("Cat added.")
        elif choice == "3":
            name = input("Enter bird's name: ")
            age = get_age()
            species = input("Enter bird's species: ")
            pets.append(Bird(name, age, species))
            print("Bird added.")
        elif choice == "4":
            if len(pets) == 0:
                print("No pets have been added.")
            else:
                print("\nAll Pets:")
                for pet in pets:
                    print(pet)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
