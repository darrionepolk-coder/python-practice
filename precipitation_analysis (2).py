import os  # os module to handle PATH flexibility for writing to the file

MIN_PRECIPITATION = 0.0
MAX_PRECIPITATION = 366.0

# Name of the text file that stores the month names and precipitation amounts.
OUTPUT_FILE = 'precipitation.txt'


def main():
    # Create a list of the month names, January through December.
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    # Use the repetition operator to initialize the precipitation list with 0.0 for each month.
    precipitation = [0.0] * 12

    # Loop through the months and prompt the user for each month's precipitation.
    for i in range(len(months)):
        precipitation[i] = get_precipitation(months[i])

    # analyze the data using list methods and functions
    analyze_precipitation(precipitation, months)

    # Save each month name with its precipitation amount to a text file.
    path = write_precipitation_file(months, precipitation)
    print(f'Data saved to {path}')


def get_precipitation(month):
    # Prompt for precipitation and repeat until the user enters a valid value.
    while True:
        try:
            amount = float(input(f'Enter precipitation for {month}: '))

            if MIN_PRECIPITATION <= amount <= MAX_PRECIPITATION:
                return amount
            else:
                print(f'Please enter a value between {MIN_PRECIPITATION} and {MAX_PRECIPITATION}.')

        except ValueError:
            print('Invalid input. Please enter a numeric value.')


def analyze_precipitation(precipitation, months):
    # Use list functions and methods to summarize the precipitation values.
    total = sum(precipitation)
    average = total / len(precipitation)

    highest = max(precipitation)
    lowest = min(precipitation)

    highest_month = months[precipitation.index(highest)]
    lowest_month = months[precipitation.index(lowest)]

    print(f'\nAnnual precipitation total: {total:.2f}')
    print(f'Average monthly precipitation: {average:.2f}')
    print(f'Highest precipitation: {highest:.2f} ({highest_month})')
    print(f'Lowest precipitation: {lowest:.2f} ({lowest_month})')


def write_precipitation_file(months, precipitation, filename=OUTPUT_FILE):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

    try:
        with open(path, 'w') as output_file:
            for i in range(len(months)):
                output_file.write(f'{months[i]},{precipitation[i]}\n')

    except OSError as error:
        print(f"Could not save the data to '{path}': {error}")
        return None

    return path


# Call the main function only if this file is run directly.
if __name__ == '__main__':
    main()
