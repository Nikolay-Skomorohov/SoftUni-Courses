numbers_list = list(map(int, input().split(", ")))
number_beggars = int(input())

result = []

for i in range(number_beggars):
    result.append(0)

while len(numbers_list) > 0:
    for index in range(number_beggars):
        num = numbers_list.pop(0)
        result[index] += num
        if len(numbers_list) == 0:
            break

print(result)
