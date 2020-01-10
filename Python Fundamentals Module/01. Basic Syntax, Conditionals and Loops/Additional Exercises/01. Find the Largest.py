number = input()

result = ""

while len(number) > 0:
    largest = max(number)
    result += largest
    number = number.replace(largest, "", 1)

print(f"{result}")

