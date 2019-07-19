def calculate_area(base=None, height=None):
    return (base * height) / 2


number1 = float(input())
number2 = float(input())

result = calculate_area(number1, number2)

if result == int(result):
    result = int(result)
else:
    round(result)
print(f"{result:.12g}")
