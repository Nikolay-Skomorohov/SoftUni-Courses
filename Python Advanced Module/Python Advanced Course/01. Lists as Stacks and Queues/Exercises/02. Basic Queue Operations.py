from collections import deque

numbers = [int(x) for x in input().split(" ")]
numbers_list = [int(x) for x in input().split(" ")]

result = deque()

for i in range(numbers[0]):
    result.append(numbers_list[i])

for i in range(numbers[1]):
    result.popleft()

if numbers[2] in result:
    print(True)
else:
    if result:
        print(f"{min(result)}")
    else:
        print(0)