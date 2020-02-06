number = int(input())
num_list = [int(x) for x in input().split(" ")]
result = list(map(lambda x: x * number, num_list))
print(*result)
