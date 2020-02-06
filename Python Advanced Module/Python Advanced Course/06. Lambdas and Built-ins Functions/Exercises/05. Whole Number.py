input_list = [float(x) for x in input().split(" ")]
new_list = list(map(round, input_list))
result = list(map(lambda x: x * len(input_list), new_list))
print(sum(result))
