day = input("Enter you day: ")
if day == 'Monday' or 'Tuesday' or 'Wednesday' or 'Thursday':
    print("Weekday")
elif day == 'friday':
    print("TGIF")
elif day == 'Saturday' or 'Sunday':
    print("Weekend")
else:
    print("invalid input")