month = input("Enter a month: ")
if month in ["January","February","March","April","May"]:
    print("Spring")
elif month in ["June","July","August"]:
    print("summer")
elif month in ["September","October","November"]:
    print("Fall")
elif month == "December":
    print("Winter")
else:
    print("Invalid month")


