a_string = input()
string_case = input()

lower_sum = 0
upper_sum = 0

for char in a_string:
    if char.isalpha() and char.islower():
        lower_sum += ord(char)
    elif char.isalpha() and char.isupper():
        upper_sum += ord(char)

if string_case == "LOWERCASE":
    print(f"The total sum is: {lower_sum}")
elif string_case == "UPPERCASE":
    print(f"The total sum is: {upper_sum}")
