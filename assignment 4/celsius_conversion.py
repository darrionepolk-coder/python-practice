# Celsius Conversion Program
# This program is meant for a beginner Python student.
# The goal is to convert Celsius values to Fahrenheit values.
# We start at 0 Celsius and keep going until the user chooses the ending value.

# Absolute zero is the lowest possible temperature in Celsius.
# If a user enters anything colder than this, the value is not valid.
ABSOLUTE_ZERO_C = -273.15

# We use a loop so the program keeps asking until the user enters a valid number.
while True:
    try:
        # Ask for an integer because the assignment says the input is an integer.
        limit = int(input("Enter a Celsius value to convert up to (must be an integer and not below absolute zero): "))
    except ValueError:
        # This catches things like letters or decimals that are not allowed in this program.
        print("Invalid input. Please enter a whole number.")
        continue

    # Check if the value is below absolute zero.
    if limit < ABSOLUTE_ZERO_C:
        print("Error: Temperature cannot be below absolute zero.")
        print("Please enter a valid Celsius value.")
    # This program is designed to start at 0 and go up to the user value.
    # So we do not allow negative values here.
    elif limit < 0:
        print("Error: This program converts from 0 up to the selected Celsius value.")
        print("Please enter 0 or a positive number.")
    else:
        # The input passed all checks, so we can stop the loop.
        break

# Print the heading for the two-column output.
print("Celsius\tFahrenheit")
print("---------------------")

# Use a loop to convert each Celsius value from 0 up to the ending value.
for celsius in range(0, limit + 1):
    # Formula for converting Celsius to Fahrenheit.
    fahrenheit = (celsius * 9 / 5) + 32

    # Print each row in a clean table format.
    print(f"{celsius}\t{fahrenheit:.2f}")
