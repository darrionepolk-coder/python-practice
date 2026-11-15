# Temperature conversion program using functions
# This script follows the assignment structure: imports, constants, functions, and a main() block.
# The goal is to let the user choose a temperature scale and convert between Celsius and Fahrenheit.

# These are the lowest possible temperatures for each scale.
# If the user enters anything below these values, the conversion should not happen.
ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67


# This function asks the user which scale they want to use.
# It keeps asking until the user enters a valid value: F or C.
def get_temperature_type():
    while True:
        temp_type = input("Enter temperature type (F for Fahrenheit, C for Celsius): ").strip().upper()
        if temp_type in ("F", "C"):
            return temp_type
        print("Invalid temperature type. Please enter F or C.")


# This function asks for the actual number the user wants to convert.
# It uses a try/except block so that letters or invalid input do not crash the program.
def get_temperature_value():
    while True:
        try:
            temp_value = float(input("Enter the temperature value: "))
            return temp_value
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


# This function converts Fahrenheit to Celsius using the standard formula.
# Formula: C = (F - 32) * 5 / 9
def convert_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# This function converts Celsius to Fahrenheit using the standard formula.
# Formula: F = (C * 9 / 5) + 32
def convert_c_to_f(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# This function validates whether the entered temperature is realistic.
# It compares the value to absolute zero for that scale.
def validate_temperature(temp_type, temp_value):
    if temp_type == "F":
        return temp_value >= ABSOLUTE_ZERO_F
    if temp_type == "C":
        return temp_value >= ABSOLUTE_ZERO_C
    return False


# This is the main part of the program.
# It calls the helper functions and decides what to do next.
def main():
    # Step 1: get the scale and the value from the user.
    temp_type = get_temperature_type()
    temp_value = get_temperature_value()

    # Step 2: check if the value is valid before converting.
    if not validate_temperature(temp_type, temp_value):
        print("Error: temperature cannot be below absolute zero.")
        print("Please enter a valid temperature.")
    else:
        # Step 3: decide which conversion to do based on the chosen scale.
        if temp_type == "F":
            converted = convert_f_to_c(temp_value)
            print(f"{temp_value}F = {converted:.2f}C")
        elif temp_type == "C":
            converted = convert_c_to_f(temp_value)
            print(f"{temp_value}C = {converted:.2f}F")


# This tells Python to run main() only when the file is executed directly.
if __name__ == "__main__":
    main()
