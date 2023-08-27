# Simple Greet Functions
# Importing Time Module
import time

# Getting Timespans
timestamp = time.strftime('%H:%M:%S')
# Prime Current Full Time
print("Time -", timestamp)
# Getting Hour Timespan
hour = int(time.strftime('%H'))
# Printing Current Hour
print("Hour -", hour)

# Main Function
if __name__ == "__main__":
    if 4 < hour < 12:
        print("Good Morning!!")
    elif 12 < hour < 18:
        print("Good Afternoon!!")
    elif 18 < hour < 20:
        print("Good Evening!!")
    elif 20 < hour < 24:
        print("Good Night!!")
    else:
        print("Time Should Be Between 0 And 24")
