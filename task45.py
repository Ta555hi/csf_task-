user_name = input("Enter your name: ")
vowel = "aeiou"
vowel_count = 0
for i in user_name:
    if i in vowel:
        vowel_count += 1
print(vowel_count)