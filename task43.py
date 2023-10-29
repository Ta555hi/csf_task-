user_name = input("Enter your name: ")
for i in user_name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(True)
    else:
        print(False)