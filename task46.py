#factorial
#is the product of all positive integers less than or equal to a given positive interger
#denoted by that integer and exclamation point
user_number = int(input("enter a number: "))
factorial = 1
i = 1
while i <= user_number:
    factorial += 1
    i += 1
print(factorial)