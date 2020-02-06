names_list = [x for x in input().split(" ")]
new_list = list(filter(lambda x: x[0].isupper() and x[1:].islower(), names_list))
result = len("".join(new_list))
print(result)
