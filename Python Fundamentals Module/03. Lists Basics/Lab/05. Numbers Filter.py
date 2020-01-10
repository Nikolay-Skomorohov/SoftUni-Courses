n = int(input())

numbers_list = []

for i in range(n):
    numbers_list.append(int(input()))

command = input()
result = []
for num in numbers_list:
    if command == "even":
        if num % 2 == 0:
            result.append(num)
    elif command == "odd":
        if num % 2 == 1:
            result.append(num)
    elif command == "negative":
        if num < 0:
            result.append(num)
    elif command == "positive":
        if num >= 0:
            result.append(num)
print(result)
