def sum_numbers(num1, num2, num3):
    add = num1 + num2

    def add_and_subtract(num3):
        return add - num3
    return add_and_subtract(num3)


number1 = int(input())
number2 = int(input())
number3 = int(input())

print(sum_numbers(number1, number2, number3))