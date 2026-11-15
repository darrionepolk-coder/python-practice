# Input: ask the user for a Fahrenheit temperature
fahrenheit = float(input("Enter Fahrenheit temperature: "))

# Process: convert Fahrenheit to Celsius using the formula C = (F - 32) * 5 / 9
celsius = (fahrenheit - 32) * 5 / 9

# Output: display the result with 2 decimal places
print(f"{fahrenheit}F = {celsius:.2f}C")
