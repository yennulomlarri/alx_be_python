from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the specified format.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """
    Prompts the user for a number of days and calculates the future date.
    """
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=number_of_days)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    """
    Main function to run the script.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()