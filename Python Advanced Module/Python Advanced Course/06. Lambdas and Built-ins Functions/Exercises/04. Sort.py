input_list = [int(x) for x in input().split(" ")]
new_list = list(filter(lambda x: x < 0, input_list))
print(abs(sum(new_list)))
