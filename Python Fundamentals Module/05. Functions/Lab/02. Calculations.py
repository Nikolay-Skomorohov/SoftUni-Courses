def calculator(operation, num1, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        return int(num1 / num2)
    elif operation == "multiply":
        return num1 * num2


operation = input()
num1 = int(input())
num2 = int(input())

print(calculator(operation, num1, num2))