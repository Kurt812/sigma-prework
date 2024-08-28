from datetime import datetime


def calculate_years_difference(input_date):
    # Get the current date
    current_date = datetime.now()

    # Calculate the difference in years
    years_difference = current_date.year - input_date.year

    # Adjust for cases where the current date is before the input date's month/day
    if (current_date.month, current_date.day) < (input_date.month, input_date.day):
        years_difference -= 1

    return years_difference


date_str = input("Enter the date (DD-MM-YYYY): ")
input_date = datetime.strptime(date_str, "%d-%m-%Y")

years_diff = calculate_years_difference(input_date)
print(f"The difference in years is: {years_diff}")
