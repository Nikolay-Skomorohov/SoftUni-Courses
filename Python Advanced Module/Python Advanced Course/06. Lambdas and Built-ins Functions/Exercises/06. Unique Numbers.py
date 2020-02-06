input_list = [float(x) for x in input().split(" ")]
input_list = list(map(round, input_list))
result = list(map(lambda x: x * 3, input_list))
result = set(result)
print(min(input_list))
print(max(input_list))
print(*sorted(result))
