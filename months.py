months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}

month_number = int(input("Enter the number: "))

# chained comparison in python
if 1 <= month_number <= 12:
    for key, value in months.items():
        if value == month_number:
            print(f"Month: {key}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
