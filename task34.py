temperature = float(input("Enter the temperature: "))
if temperature >= 100:
    print("Boiling")
elif temperature >= 32 and temperature <= 99:
    print("liquid")
else:
    print("freezing")
