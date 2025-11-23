months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month_num = int(input("Enter the month number (1-12): "))

if month_num in months:
    
    if month_num == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()
        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print(f"This month has {months[month_num]} days.")
else:
    print("Invalid month number.")