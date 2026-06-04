day = input("Enter the day between sunday and saturday : " )
day = day.lower()

if day == "saturday " or day == "sunday":
    print("Weekend")
else:
    print("Weekday")
    