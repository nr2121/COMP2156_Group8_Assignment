# Simple python script to print the current time of day.

from datetime import datetime

# Print current time as day-month-year hour-minute-second
print("The current time of day is:")
print(datetime.now().strftime("%d-%m-%Y %H-%M-%S"))