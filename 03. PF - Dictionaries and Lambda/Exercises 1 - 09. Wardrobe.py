n = int(input())

clothes_dict = {}

for num in range(n):
    input_list = list(input().split(" -> "))
    color = input_list[0]
    stuff = list(input_list[1].split(","))
    if color not in clothes_dict.keys():
        clothes_dict[color] = {}
    for item in stuff:
        if item not in clothes_dict[color]:
            clothes_dict[color][item] = 1
        else:
            clothes_dict[color][item] += 1

to_wear = list(input().split(" "))

for color in clothes_dict.keys():
    print(f"{color} clothes:")
    for k, v in clothes_dict[color].items():
        if to_wear[0] == color and to_wear[1] == k:
            print(f"* {k} - {v} (found!)")
        else:
            print(f"* {k} - {v}")
