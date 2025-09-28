

from datetime import datetime, timedelta

def display_current_datetime():
    
    current_date = datetime.now()
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted}")
    return current_date  # Return for reuse if needed


def calculate_future_date(days_to_add):
    
    future_date = datetime.now() + timedelta(days=days_to_add)
    formatted = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted}")
    return future_date


def main():
    
    display_current_datetime()

    
    while True:
        try:
            days_str = input("Enter the number of days to add to the current date: ").strip()
            days = int(days_str)
            break
        except ValueError:
            print("Please enter a valid integer for the number of days.")
    
    calculate_future_date(days)


if __name__ == "__main__":
    main()
