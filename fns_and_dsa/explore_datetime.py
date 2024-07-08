from datetime import datetime, timedelta
current_date = datetime.now()
def display_current_datetime():
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    x = int(input("Enter the number of days to add to the current date: "))
    delta = timedelta(days=x)
    #current_date = datetime.now()
    future_date = current_date + delta
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    display_current_datetime()    
    calculate_future_date()


