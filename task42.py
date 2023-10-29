user_name = input("Enter your your name: ")
vowels = "aeiou"
i = 0
while i < len(user_name):
    if user_name[i] in vowels:
        print(True)
        break
    i += 1
else:
    print(False)
