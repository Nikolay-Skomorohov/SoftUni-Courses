numbers = list(map(int, input().split(" ")))
numbers_list = [int(x) for x in input().split(" ")]

result_list = []
for i in range(numbers[0]):
    result_list.append(numbers_list[i])

for index in range(numbers[1]):
    result_list.pop()

if numbers[2] in result_list:
    print(True)
else:
    if result_list:
        print(f"{min(result_list)}")
    else:
        print(0)