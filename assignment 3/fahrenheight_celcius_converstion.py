# This is the lowest possible temperature in Celsius.
# We use it to stop the program from doing math with impossible values.
ABSOLUTE_ZERO_C = -273.15

# Show the menu so the user knows the two choices.
print("Temperature Conversion Menu")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

# Ask the user to choose the conversion direction.
choice = int(input("Choose an option (1 or 2): "))

# If the user picks option 1, we convert Fahrenheit to Celsius.
if choice == 1:
    # Ask the user for the Fahrenheit value.
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Check if the value is below absolute zero before converting.
    if fahrenheit < -459.67:
        print("Invalid input. Temperature cannot be below absolute zero.")
    else:
        # Formula for converting Fahrenheit to Celsius.
        celsius = (fahrenheit - 32) * 5 / 9

        # Show the converted result with 2 decimal places.
        print(f"{fahrenheit}F = {celsius:.2f}C")

# If the user picks option 2, we convert Celsius to Fahrenheit.
elif choice == 2:
    # Ask the user for the Celsius value.
    celsius = float(input("Enter temperature in Celsius: "))

    # Check if the value is below absolute zero before converting.
    if celsius < ABSOLUTE_ZERO_C:
        print("Invalid input. Temperature cannot be below absolute zero.")
    else:
        # Formula for converting Celsius to Fahrenheit.
        fahrenheit = (celsius * 9 / 5) + 32

        # Show the converted result with 2 decimal places.
        print(f"{celsius}C = {fahrenheit:.2f}F")

# If the user enters something other than 1 or 2, show an error.
else:
    print("Invalid choice. Please select 1 or 2.")
