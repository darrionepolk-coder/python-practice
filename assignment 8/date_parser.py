def parse_date(date_string):
    # Remove extra whitespace and split the date.
    date_parts = date_string.strip().split('/')

    # Make sure there are three parts.
    if len(date_parts) != 3:
        raise ValueError("Date must use mm/dd/yyyy format.")

    # Separate the month, day, and year.
    month = date_parts[0]
    day = date_parts[1]
    year = date_parts[2]

    # Make sure all three parts contain digits.
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        raise ValueError("Date must contain numbers only.")

    # Convert the strings into integers.
    month = int(month)
    day = int(day)
    year = int(year)

    # List of month names.
    months = ['January', 'February', 'March', 'April',
              'May', 'June', 'July', 'August',
              'September', 'October', 'November', 'December']

    # Validate the date.
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")

    if day < 1 or day > 31:
        raise ValueError("Day must be between 1 and 31.")

    if year < 1:
        raise ValueError("Year must be greater than zero.")

    # Get the full month name using its index.
    month_name = months[month - 1]

    return month_name + " " + str(day) + ", " + str(year)


def main():
    try:
        date_string = input("Enter a date (mm/dd/yyyy): ")

        formatted_date = parse_date(date_string)

        print(formatted_date)

    except ValueError as error:
        print(f"Invalid date: {error}")


# Call the main function.
if __name__ == '__main__':
    main()
