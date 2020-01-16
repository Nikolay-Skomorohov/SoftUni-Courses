def check_numbers(number):
    if num == num[::-1]:
        return "True"
    else:
        return "False"


integer_list = input().split(", ")

for num in integer_list:
    print(check_numbers(num))
