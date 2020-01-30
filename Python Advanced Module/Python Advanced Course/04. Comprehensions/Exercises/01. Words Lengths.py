input_list = [x for x in input().split(", ")]

result = {x: str(len(x)) for x in input_list}

final = [" -> ".join(kvp) for kvp in result.items()]

print(", ".join(final))
